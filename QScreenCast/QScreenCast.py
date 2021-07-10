# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © Tom Hören
#
# Licensed under the terms of the MIT License
# ----------------------------------------------------------------------------

"""
Created on Mon Nov 25 18:13:27 2019

@author: hoeren

hints:

    Window Geometry:
        https://doc.qt.io/qt-5/application-windows.html#window-geometry

    Splash:
        QMovie *movie = new QMovie(":/images/other/images/16x16/loading.gif");
        QLabel *processLabel = new QLabel(this);
        processLabel->setMovie(movie);
        movie->start();

"""
import os
import platform
import shutil
import tempfile

from multiprocessing import Process

#from packaging import version
from qtpy import PYQT5, QT_VERSION
from qtpy import QtCore, QtGui, QtWidgets, QtMultimedia

import qtawesome as qta


PYQT_WINDOWS_MINIMUM_SUPPORTED_VERSION = "5.12.3"
PYQT_LINUX_MINIMUM_SUPPORTED_VERSION = "5.14.2"
PYQT_DARWIN_MINIMUM_SUPPORTED_VERSION = "5.14.0"

VERBOSITY = True


# TODO : also check if ffmpeg is installed (and what about the codec we need?)
def is_pyqt_version_supported(actual_version, required_version):
    return True
    # all the test done are base on pyqt5
    # unfortunately this will be required for now to run the screencaster until we test it with pyside
    if not PYQT5:
        return False
    return version.parse(actual_version) >= version.parse(required_version)


def pop_up_error_box(message):
    msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Error, 'Version not found', message)
    msg_box.exec_()


class ScreenCastToolButton(QtWidgets.QToolButton):

    rightClicked = QtCore.Signal()

    video_sizes = {480: ((854, 480), ''),
                   720: ((1280, 720), ''),
                   1080: ((1920, 1080), 'aka 1K'),
                   1440: ((2560, 1440), 'aka 2K'),
                   2160: ((3840, 2160), 'aka 4K')}

    icon_size = 16
    fps = 14

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.main_window = parent

        # safety check
        for video_size in self.video_sizes:
            if video_size != self.video_sizes[video_size][0][1]:
                raise Exception("problem with declared video sizes")

        self.required_pyqt_version = ''
        self.os = platform.system()
        if self.os == 'Windows':
            self.desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            self.required_pyqt_version = PYQT_WINDOWS_MINIMUM_SUPPORTED_VERSION
        elif self.os == 'Linux':
            self.desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            self.required_pyqt_version = PYQT_LINUX_MINIMUM_SUPPORTED_VERSION
        elif self.os == 'Darwin':
            self.desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            self.required_pyqt_version = PYQT_DARWIN_MINIMUM_SUPPORTED_VERSION
        else:
            raise Exception("unrecognized operating system")

        self._connect_event_handler()

    def setup(self, main_window):
        self.main_window = main_window
        self.setIcon(qta.icon('mdi.video', color='orange'))
        self.setIconSize(QtCore.QSize(self.icon_size, self.icon_size))
        self.state = 'idle'

        self.recorder = ScreenCastRecorder(self.main_window, self.desktop_path, self.fps)
        if self.is_microphone_available:
            self.active_input = self._get_available_audio_inputs()[0]

        self.countdown = ScreenCastCountDown(self.main_window)

    def _connect_event_handler(self):
        self.clicked.connect(self.toggle_recording)
        self.rightClicked.connect(self.settings)

    def mousePressEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            self.rightClicked.emit()
        else:
            self.clicked.emit()

    def toggle_recording(self):
        if self.state == 'idle':
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        if not is_pyqt_version_supported(QT_VERSION, self.required_pyqt_version):
            pop_up_error_box(f"pyqt version is not support: {QT_VERSION} < {self.required_pyqt_version}")
            return

        # TODO: maybe skip this, this way, if one doesn't have a microphone,
        #       one can at least record the screen ...
        if not self.is_microphone_available:
            pop_up_error_box('system microphone is not available')
            return

        self.state = 'recording'
        self.setIcon(qta.icon('mdi.stop', color='red'))

        grabRegion = self.get_grab_region()
        if grabRegion.height() not in self.video_sizes:
            self.resize()
        else:
            if grabRegion.width() != self.video_sizes[grabRegion.height()][0][0]:
                self.resize()

        self.recorder.start_recording()

    def stop_recording(self):
        self.state = 'idle'
        self.setIcon(qta.icon('mdi.video', color='orange'))

        self.recorder.stop_recording()

    def _get_available_audio_inputs(self):
        return self.recorder.get_available_audio_inputs()

    @property
    def is_microphone_available(self):
        return self.recorder.is_microphone_available()

    def _generate_audio_input_menu(self):
        if not self.is_microphone_available:
            audio_input_menu = QtWidgets.QMenu("no available microphones", parent=self)
            audio_input_menu.setIcon(qta.icon('mdi.microphone-off', color='orange'))
        else:
            audio_input_menu = QtWidgets.QMenu("available microphones", parent=self)
            audio_input_menu.setIcon(qta.icon('mdi.microphone', color='orange'))
            for source in self._get_available_audio_inputs():
                action = audio_input_menu.addAction(source)
                audio_input_menu.setIcon(qta.icon('mdi.microphone', color='orange'))
                action.triggered.connect(lambda: self.set_audio_input(source))
                if self._is_audio_input_active(source):
                    icon = qta.icon('mdi.check-bold', color='orange')
                    action.setIcon(icon)

        return audio_input_menu

    def _is_audio_input_active(self, audio_input):
        return self.active_input == audio_input

    def set_audio_input(self, audio_input):
        self.active_input = audio_input
        self.recorder.set_audio_input(audio_input)

    def _is_valid_width(self, psize_x, psize_y, screen):
        if psize_x <= screen.width() and psize_y <= screen.height():
            return True
        return False

    def settings(self):
        '''
        this method handles the settings on the screenCast (context menu)
        '''
        mainWindow = self.main_window
        screenAG = QtWidgets.QDesktopWidget().availableGeometry(mainWindow)
        screenG = QtWidgets.QDesktopWidget().screenGeometry(mainWindow)

        menu = QtWidgets.QMenu(parent=self)

        audi_menu = self._generate_audio_input_menu()
        menu.addMenu(audi_menu)

        menu.addSeparator()
        main_window_size = self.get_grab_region()
        biggest_main_window_size = self.calculate_grab_region()
        itemset = sorted(set(list(self.video_sizes) + [main_window_size.height()]))
        for item in itemset:
            if item in self.video_sizes:
                text = f"{item}p ({self.video_sizes[item][0][0]}x{self.video_sizes[item][0][1]}) {self.video_sizes[item][1]}"
                icon = None
                if main_window_size.height() == self.video_sizes[item][0][1]:
                    icon = qta.icon('mdi.check-bold', color='orange')
                enabled = self._is_valid_width(self.video_sizes[item][0][0], self.video_sizes[item][0][1], screenAG)
            else:
                text = f"({main_window_size.width()}x{main_window_size.height()}) → {biggest_main_window_size.height()}p"
                icon = qta.icon('mdi.check-bold', color='orange')
                enabled = True
            action = menu.addAction(text)
            if icon is not None:
                action.setIcon(icon)
            if item == 240 or ((item == main_window_size.height()) and biggest_main_window_size.height() == 240):
                action.triggered.connect(lambda: self.resize(240))
            elif item == 360 or ((item == main_window_size.height()) and biggest_main_window_size.height() == 360):
                action.triggered.connect(lambda: self.resize(360))
            elif item == 480 or ((item == main_window_size.height()) and biggest_main_window_size.height() == 480):
                action.triggered.connect(lambda: self.resize(480))
            elif item == 720 or ((item == main_window_size.height()) and biggest_main_window_size.height() == 720):
                action.triggered.connect(lambda: self.resize(720))
            elif item == 1080 or ((item == main_window_size.height()) and biggest_main_window_size.height() == 1080):
                action.triggered.connect(lambda: self.resize(1080))
            elif item == 1440 or ((item == main_window_size.height()) and biggest_main_window_size.height() == 1440):
                action.triggered.connect(lambda: self.resize(1440))
            elif item == 2160 or ((item == main_window_size.height()) and biggest_main_window_size.height() == 2160):
                action.triggered.connect(lambda: self.resize(2160))
            action.setEnabled(enabled)

        menu.addSeparator()

        action = menu.addAction(qta.icon('mdi.monitor', color='orange'),
                                f"{screenG.width()}x{screenG.height()}")
        action = menu.addAction(qta.icon('mdi.monitor-screenshot', color='orange'),
                                f"{screenAG.width()}x{screenAG.height()}")

        cursorPoint = QtGui.QCursor.pos()
        menuSize = menu.sizeHint()
        menuPoint = QtCore.QPoint(cursorPoint.x() - menuSize.width(),
                                  cursorPoint.y() - menuSize.height())
        menu.exec_(menuPoint)

    def resize(self, psize=-1):
        '''
        this method will resize the main window to the psize resolution.
        if none is provided (-1) then resize to the biggest possible.
        '''
        newRect = self.calculate_grab_region(psize)
        if newRect.height() != 0:  # new size needs to make sense ;-)
            Δx = self.main_window.frameGeometry().width() - self.main_window.geometry().width()
            Δy = self.main_window.frameGeometry().height() - self.main_window.geometry().height()
            self.main_window.move(newRect.x(), newRect.y())
            self.main_window.resize(newRect.width() - Δx, newRect.height() - Δy)

    def get_grab_region(self):
        '''
        this method will get the 'GrabRegion' of the main window, and
        return it as a QRect.
        '''
        retval = QtCore.QRect(self.main_window.x(),
                              self.main_window.y(),
                              self.main_window.frameGeometry().width(),
                              self.main_window.frameGeometry().height())
        return retval

    def calculate_grab_region(self, psize=-1):
        '''
        this method will determine the ideal 'GrabRegion' on the screen
        where the MainWindow currently resides given psize.
        If psize=-1, the biggest possible psize given the screen is used.
        return value is a QRect.
        '''

        screenRect = QtWidgets.QDesktopWidget().availableGeometry(self)

        if psize == -1:
            width = height = 0
            for video_size, value in self.video_sizes.items():
                if value[0][1] <= screenRect.height() and value[0][0] <= screenRect.width():
                    width = self.video_sizes[video_size][0][0]
                    height = self.video_sizes[video_size][0][1]

            x = int(((screenRect.width() - width) / 2)) + screenRect.x()
            y = int(((screenRect.height() - height) / 2)) + screenRect.y()

        elif psize in self.video_sizes:
            width = self.video_sizes[psize][0][0]
            height = self.video_sizes[psize][0][1]
            if width <= screenRect.width() and height <= screenRect.height():
                x = int(((screenRect.width() - width) / 2) + screenRect.x())
                y = int(((screenRect.height() - height) / 2) + screenRect.y())
            else:
                width = height = 0
                x = int(((screenRect.width() - width) / 2) + screenRect.x())
                y = int(((screenRect.height() - height) / 2) + screenRect.y())
        else:
            width = height = 0
            x = int(((screenRect.width() - width) / 2) + screenRect.x())
            y = int(((screenRect.height() - height) / 2) + screenRect.y())
        retval = QtCore.QRect(x, y, width, height)
        return retval


class AudioRecorder(QtMultimedia.QAudioRecorder):
    """The audio recorder class."""

    verbose = VERBOSITY
    debug = False

    def __init__(self, audio_path):
        super().__init__()
        self.audio = audio_path
        self._setup()

    def _setup(self):
        self.setContainerFormat("audio/x-wav")
        self.setOutputLocation(QtCore.QUrl.fromLocalFile(self.audio))

    def is_microphone_available(self):
        return len(self.audioInputs()) > 0

    def get_available_audio_inputs(self):
        audio_inputs = list(set(self.audioInputs()))
        # TODO: check output for device with multiple audio inputs
        if self.debug:
            print(self.audioInputs())
            print(audio_inputs)
            print(self.audioInput())
            print(self.defaultAudioInput())
        return audio_inputs

    def set_audio_input(self, audio_input):
        self.setAudioInput(audio_input)

    def start(self):
        self.record()


class VideoRecorder:
    def __init__(self, main_window, images_path, fps):
        super().__init__()
        self.main_window = main_window
        self.images = images_path
        self.counter = 0

        self.timer = QtCore.QTimer()
        self.interval = int(1000 / fps)
        self.timer.setInterval(self.interval)
        self._connect_event_handler()

    def _connect_event_handler(self):
        self.timer.timeout.connect(self._save_image)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def _save_image(self):
        os.makedirs(self.images, exist_ok=True)
        q_rec = self.main_window.geometry()
        import qtawesome as qta
        arrow = QtGui.QPixmap(qta.icon("mdi.cursor-default-outline", color="white").pixmap(13, 13))
        self.px = QtWidgets.QApplication.primaryScreen().grabWindow(0,
                                                                    q_rec.x(),
                                                                    q_rec.y(),
                                                                    q_rec.width(),
                                                                    q_rec.height())

        painter = QtGui.QPainter(self.px)
        painter.drawPixmap(QtGui.QCursor.pos() - q_rec.topLeft(), arrow)
        image = os.path.join(self.images, "image" + str(self.counter).zfill(7) + ".jpg")
        self.px.save(image, 'jpg')
        self.counter += 1


class ScreenCastRecorder:
    delay = 3000  # ms TODO: we could tickle this out ouf the gif
    video_file = 'SSC#.mp4'
    temp_file = tempfile.gettempdir()
    verbose = True

    def __init__(self, main_window, desktop_path, interval):
        super().__init__()
        self.desktop_path = desktop_path
        self.main_window = main_window
        self.audio = os.path.join(self.temp_file, 'audio.wav')
        self.video = os.path.join(self.temp_file, 'video.avi')
        self.images = os.path.join(self.temp_file, "images")

        self._setup()
        self.audio_recorder = AudioRecorder(self.audio)
        self.video_recorder = VideoRecorder(main_window, self.images, interval)
        self.countdown = ScreenCastCountDown(self.main_window)

    def _setup(self):
        # delayed timer used as a countdown and will fire only once after 3 seconds and starts the recording
        self.delay_timer = QtCore.QTimer()
        self.delay_timer.setSingleShot(True)
        self.delay_timer.timeout.connect(self._delay_timer_time_out)

        self.recording_started = False

        if os.path.exists(self.images):
            shutil.rmtree(self.images)

        os.makedirs(self.images, exist_ok=True)

        if os.path.exists(self.video):
            os.remove(self.video)

        if os.path.exists(self.audio):
            os.remove(self.audio)

    def is_microphone_available(self):
        return self.audio_recorder.is_microphone_available()

    def get_available_audio_inputs(self):
        return self.audio_recorder.get_available_audio_inputs()

    def set_audio_input(self, audio_input):
        return self.audio_recorder.set_audio_input(audio_input)

    def start_recording(self):
        # this will pop up the countdown gif to visualize the timer delay
        self.countdown.start()
        self.delay_timer.start(self.delay)

    def _delay_timer_time_out(self):
        if self.verbose:
            print("Start audio & video recording.")
        self.audio_recorder.start()
        self.video_recorder.start()
        self.recording_started = True

    def stop_recording(self):
        # we don't need to store any thing while the recording didn't even start
        if not self.recording_started:
            self.delay_timer.stop()
            self.countdown.stop()
            return
        if self.verbose:
            print("Stop audio recording ... ", end='')
        self.audio_recorder.stop()
        if self.verbose:
            print("Done.")
            print("Stop video recording ... ", end='')
        self.video_recorder.stop()
        if self.verbose:
            print("Done.")
        self.output = os.path.join(self.desktop_path, self._get_next_screencast_file())
        self.video_recorder.counter = 0
        q_rec = self.main_window.geometry()
        combine_process = Combiner(self.video, self.images, self.audio, self.output, (q_rec.height(), q_rec.width()))
        combine_process.run()
        self.recording_started = False

    def _get_next_screencast_file(self):
        '''
        this method will look on the desktop for existing screencast files,
        and determine what is the next available name (no path!)
        '''
        prefix, extension = self.video_file.split('#')
        if extension.upper() != '.MP4':
            raise Exception("only .mp4 is supported!")

        files = os.listdir(self.desktop_path)
        existing_screencasts = []
        for File in files:
            if File.startswith(prefix) and File.endswith(extension):
                existing_screencasts.append(int(File.replace(prefix, '').replace(extension, '')))
        if existing_screencasts == []:  # nothing available on the desktop
            next_number = 1
        else:
            next_number = max(existing_screencasts) + 1
        return f"{prefix}{next_number}{extension}"


# ffmpeg will be used to merge audio and video parts
# video will be generated using the stored frames (screenshots)

# TODO: move from multi-processing to QProcess
class Combiner(Process):
    """This Class will combine the recorded video and audio."""

    verbose = VERBOSITY

    def __init__(self, video_path, images_path, audio_path, output_path, window_resolution):
        super().__init__()
        self.video = video_path

        self.images = images_path
        self.audio = audio_path
        self.output = output_path

    def run(self):
        '''
            to produce the video with its assosiated audio, we muss calculate the frame rate new
            each time we do recording to prevent any overlapping error between audio and video.
        '''
        import wave
        import contextlib
        duration = 1  # if someone does stop the recording direclty after starting, this will cause a devision by zero and crash
        if self.verbose:
            print("Starting the combiner ... ", end='')
        with contextlib.closing(wave.open(self.audio, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
        frame_rate = int(len(os.listdir(self.images)) / duration)
        images = os.path.join(self.images, "image%7d.jpg")
        command = f"ffmpeg -framerate {frame_rate} -start_number 0 -i {images} -i {self.audio} -c:v libx264 -crf 25 -pix_fmt yuv420p {self.output}"
        os.system(command)
        # remove the still images (issue #32)
        print(f"removing {len(os.listdir(self.images))} still images ... ", end='')
        for still_image in os.listdir(self.images):
            os.remove(os.path.join(self.images, still_image))
        print("done.")
        if self.verbose:
            print(f"Done. ({command})")


class ScreenCastCountDown(QtWidgets.QLabel):
    gif_size = 240
    window_size = 250  # make the window a bit bigger to see the whole gif
    verbose = VERBOSITY

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def _finished(self):
        self.hide()
        self.movie.stop()
        if self.verbose:
            print("Stop countdown.")

    def _setup_window(self):
        q_rec = self.main_window.geometry()
        movie_name = os.path.join(os.path.dirname(__file__), 'countdown.gif')
        self.movie = QtGui.QMovie(movie_name)
        self.movie.setScaledSize(QtCore.QSize(self.gif_size, self.gif_size))
        self.movie.finished.connect(self._finished)
        screenWidth = q_rec.width()
        screenHeight = q_rec.height()
        x = (screenWidth - self.window_size) / 2 + q_rec.x()
        offset = 15
        y = (screenHeight - self.window_size) / 2 + q_rec.y() - offset
        self.setGeometry(int(x), int(y), self.window_size, self.window_size)
        self.setMovie(self.movie)

    def start(self):
        if self.verbose:
            print("Start countdown.")
        self._setup_window()
        self.movie.start()
        self.show()

    def stop(self):
        self._finished()


# for debug purposes
def printQ(message, QObj):
    if isinstance(QObj, QtCore.QRect):
        print(f"QRect {message} : ({QObj.x()}, {QObj.y()}) ({QObj.width()}x{QObj.height()})")
    elif isinstance(QObj, QtCore.QSize):
        print(f"QSize {message} : ({QObj.width()}x{QObj.height()})")
    elif isinstance(QObj, QtCore.QPoint):
        print(f"QPoint {message} : ({QObj.x()}, {QObj.y()})")
    else:
        print(f"message")

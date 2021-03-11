# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © Tom Hören
#
# Licensed under the terms of the MIT License
# ----------------------------------------------------------------------------
"""
Python QtScreenCaster Spyder Widgets.
"""

# Third party imports
from qtpy.QtCore import QPoint, QSize, Signal
from qtpy.QtGui import QIcon
from spyder.api.plugins import SpyderPluginV2, Plugins
from spyder.api.translations import get_translation

# Local imports
from qscreencast.spyder.container import ScreenCastContainer


# Localization
_ = get_translation('qscreencast.spyder')


class ScreenCast(SpyderPluginV2):
    NAME = 'screencast'
    CONF_SECTION = NAME
    CONTAINER_CLASS = ScreenCastContainer
    REQUIRES = [Plugins.StatusBar]

    # --- Signals
    sig_main_window_resized = Signal(QSize, QSize)
    sig_main_window_moved = Signal(QPoint, QPoint)
    sig_resize_main_window_requested = Signal(QSize)
    sig_move_main_window_requested = Signal(QPoint)

    def get_name(self):
        return _('Screencast')

    def get_description(self):
        return _('Record main window video and audio')

    def get_icon(self):
        return QIcon()

    def register(self):
        status_bar = self.get_plugin(Plugins.StatusBar)

        container = self.get_container()
        container.init_screen_cast_widget(self.get_main())

        # -- Signals
        # From plugin to child
        self.sig_main_window_resized.connect(
            self.get_container().update_size)
        self.sig_main_window_moved.connect(
            self.get_container().update_position)

        # From child to plugin
        container.sig_resize_main_window_requested.connect(
            self.sig_resize_main_window_requested)
        container.sig_move_main_window_requested.connect(
            self.sig_move_main_window_requested)

        status_bar.add_status_widget(container.status_widget)

    def check_compatibility(self):
        # Check if FFMPEG is available and show a meesage

        # Check if Qt, PyQt etc, has the appropriate things needed?

        valid = True
        message = ''  # Note: Remeber to use _('') to localize the string
        return valid, message

    def on_close(self, cancellable):
        # Stop the recording and do any cleanup
        return True

    # --- API
    # ------------------------------------------------------------------------
    def start_recording(self):
        self.get_container().start_recording()

    def stop_recording(self):
        self.get_container().stop_recording()

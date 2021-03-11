import sys
import qdarkstyle

from qtpy import QtWidgets
from QScreenCast import ScreenCastToolButton

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, app):
        super().__init__()

        self.app = app  # work-around for the 'spydercustomize.SpyderQApplication' stuff ... not sure what is going on there ...

        self.setWindowTitle('Dummy Main Window')
        self.setGeometry(100, 100, 1280, 720)
        self.statusbar = QtWidgets.QStatusBar(self)

        self.screenCastToolButton = ScreenCastToolButton(parent=self)
        self.screenCastToolButton.setup(self)
        self.statusbar.addPermanentWidget(self.screenCastToolButton)

        self.setStatusBar(self.statusbar)
        self.show()


app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
mainWindow = MainWindow(app)
app.exec_()

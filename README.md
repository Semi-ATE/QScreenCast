# QScreenCast
A no-nonsense [screen-caster](https://en.wikipedia.org/wiki/Screencast) behind a [QToolButton](https://doc.qt.io/qt-5/qtoolbutton.html). 

[![GitHub](https://img.shields.io/github/license/Semi-ATE/QScreenCast?color=black)](https://github.com/Semi-ATE/QScreenCast/blob/main/LICENSE)
[![Conda](https://img.shields.io/conda/pn/conda-forge/QScreenCast?color=black)](https://anaconda.org/conda-forge/QScreenCast)
![Supported Python versions](https://img.shields.io/badge/python-%3E%3D3.7-black)

[![CI](https://github.com/Semi-ATE/QScreenCast/workflows/CI/badge.svg?branch=main)](https://github.com/Semi-ATE/QScreenCast/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/Semi-ATE/QScreenCast/branch/main/graph/badge.svg?token=BAP0H9OMED)](https://codecov.io/gh/Semi-ATE/QScreenCast)
[![CD](https://github.com/Semi-ATE/QScreenCast/workflows/CD/badge.svg)](https://github.com/Semi-ATE/QScreenCast/actions?query=workflow%3ACD)

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/Semi-ATE/QScreenCast?color=blue&label=GitHub&sort=semver)](https://github.com/Semi-ATE/QScreenCast/releases/latest)
[![GitHub commits since latest release (by date)](https://img.shields.io/github/commits-since/Semi-ATE/QScreenCast/latest)](https://github.com/Semi-ATE/QScreenCast)
[![PyPI](https://img.shields.io/pypi/v/QScreenCast?color=blue&label=PyPI)](https://pypi.org/project/QScreenCast/)
[![Conda (channel only)](https://img.shields.io/conda/vn/conda-forge/QScreenCast?color=blue&label=conda-forge)](https://github.com/conda-forge/QScreenCast-feedstock)

[![GitHub issues](https://img.shields.io/github/issues/Semi-ATE/QScreenCast)](https://github.com/Semi-ATE/QScreenCast/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/Semi-ATE/QScreenCast)](https://github.com/Semi-ATE/QScreenCast/pulls)

Any Qt application then can use the QScreenCast button to enable the creation of screen-casts for documentation/demo/tutorial as well as bug/feature reporting.

QScreenCast also provides this functionality for Spyder >= 5 by means of a plugin declaration.

## Installation

## Example usage

```python

import qtawesome as qta

from QScreenCast import QScreenCast
from qtpy import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):

  def __init__(self, app):
    super().__init__()

    self.app = app

    self.setWindowTitle('Dummy Main Window')
    self.setGeometry(100, 100, 1280, 720)
    self.statusbar = QtWidgets.QStatusBar(self)

    self.screenCastToolButton = ScreenCastToolButton(parent=self)
    self.screenCastToolButton.set_main_window(self)
    self.screenCastToolButton.setup()
    self.statusbar.addPermanentWidget(self.screenCastToolButton)

    self.setStatusBar(self.statusbar)
    self.show()

app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
mainWindow = MainWindow(app)
app.exec_()
```


[Example](https://github.com/Semi-ATE/QScreenCast/blob/75f5ea10057a9d4827fe1b191429009f56de438f/qscreencast/QtScreenCast.py#L589)


## Work in progress

The current implementation is a fist (granted a bit naive) attempt, but we are gearing up to make a second iteration, this time by using [GStreamer](https://gstreamer.freedesktop.org/) under the hood!

There is of course the topic [pyqt 5.15.3](https://github.com/conda-forge/qt-feedstock) via conda-forge, as well as Windows/Linux/MacOS version differences ...

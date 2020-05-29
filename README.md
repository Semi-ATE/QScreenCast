# QScreenCast
A complete screen-caster behind a QToolButton

# Known issues

We need some 'services' from Qt, and it turns out that a same release doesn't implement the same things on differnt OS'es

| Qt | 5.9.2 | 5.12.3 | 5.14 | 5.15 |
|:----:|:------:|:-------:|:-------:|:-------:|
| **Channel** | anaconda | conda-forge | PIP | N/A |
|Windows| ✗¹ | ✓ | ✓ | ? |
|Linux| ✗ | ?¹ | ?² | ? |
|MacOS| ✗ | ? | ? | ? |

²³

Notes:
  * ✗ : does not work
  * ✓ : works
  * ? : not tested yet
  * ✗¹ : Complaining about availability of QMultiMedia, we need that to record the audio
  * ?¹ : Not complaining about QMultiMedia but complaining about codecs ... need to see if I can install the codecs.
  * ?² : We got it to work in the past, but can no longer reproduce ... (ask Abdu)

```shell
conda install ffmpeg
```

```
(Qt5.14.2) nerohmot@THOR:~/Desktop/Repo's/QScreenCast$ pip install pyqt5==5.14.2
Collecting pyqt5==5.14.2
  Downloading PyQt5-5.14.2-5.14.2-cp35.cp36.cp37.cp38-abi3-manylinux2014_x86_64.whl (63.6 MB)
     |████████████████████████████████| 63.6 MB 1.5 MB/s 
Collecting PyQt5-sip<13,>=12.7
  Downloading PyQt5_sip-12.7.2-cp38-cp38-manylinux1_x86_64.whl (264 kB)
     |████████████████████████████████| 264 kB 1.3 MB/s 
ERROR: spyder 4.1.3 has requirement pyqt5<5.13; python_version >= "3", but you'll have pyqt5 5.14.2 which is incompatible.
Installing collected packages: PyQt5-sip, pyqt5
  Attempting uninstall: PyQt5-sip
    Found existing installation: PyQt5-sip 4.19.18
    Uninstalling PyQt5-sip-4.19.18:
      Successfully uninstalled PyQt5-sip-4.19.18
  Attempting uninstall: pyqt5
    Found existing installation: PyQt5 5.12.3
    Uninstalling PyQt5-5.12.3:
      Successfully uninstalled PyQt5-5.12.3
Successfully installed PyQt5-sip-12.7.2 pyqt5-5.14.2
(Qt5.14.2) nerohmot@THOR:~/Desktop/Repo's/QScreenCast$ spyder
Traceback (most recent call last):
  File "/home/nerohmot/miniforge3/envs/Qt5.14.2/lib/python3.8/site-packages/qtpy/QtWebEngineWidgets.py", line 22, in <module>
    from PyQt5.QtWebEngineWidgets import QWebEnginePage
ImportError: /home/nerohmot/miniforge3/envs/Qt5.14.2/lib/python3.8/site-packages/PyQt5/../../../libQt5Network.so.5: undefined symbol: _ZN15QIPAddressUtils8toStringER7QStringPh, version Qt_5

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/nerohmot/miniforge3/envs/Qt5.14.2/bin/spyder", line 11, in <module>
    sys.exit(main())
  File "/home/nerohmot/miniforge3/envs/Qt5.14.2/lib/python3.8/site-packages/spyder/app/start.py", line 201, in main
    from spyder.app import mainwindow
  File "/home/nerohmot/miniforge3/envs/Qt5.14.2/lib/python3.8/site-packages/spyder/app/mainwindow.py", line 84, in <module>
    from qtpy import QtWebEngineWidgets  # analysis:ignore
  File "/home/nerohmot/miniforge3/envs/Qt5.14.2/lib/python3.8/site-packages/qtpy/QtWebEngineWidgets.py", line 26, in <module>
    from PyQt5.QtWebKitWidgets import QWebPage as QWebEnginePage
ModuleNotFoundError: No module named 'PyQt5.QtWebKitWidgets'
(Qt5.14.2) nerohmot@THOR:~/Desktop/Repo's/QScreenCast$ conda list qt
# packages in environment at /home/nerohmot/miniforge3/envs/Qt5.14.2:
#
# Name                    Version                   Build  Channel
pyqt5                     5.14.2                   pypi_0    pypi
pyqt5-sip                 12.7.2                   pypi_0    pypi
pyqtchart                 5.12                     pypi_0    pypi
pyqtwebengine             5.12.1                   pypi_0    pypi
qt                        5.12.5               hd8c4c69_1    conda-forge
qtawesome                 0.7.2              pyh9f0ad1d_0    conda-forge
qtconsole                 4.7.4              pyh9f0ad1d_0    conda-forge
qtpy                      1.9.0                      py_0    conda-forge
sphinxcontrib-qthelp      1.0.3                      py_0    conda-forge
(Qt5.14.2) nerohmot@THOR:~/Desktop/Repo's/QScreenCast$ pip search qtpy
QtPy (1.9.0)              - Provides an abstraction layer on top of the various Qt bindings (PyQt5, PyQt4 and PySide) and additional custom
                            QWidgets.
  INSTALLED: 1.9.0 (latest)
qtpyinheritance (0.0.1)   - Prototype qtpy inheritance-related tools
qtpi-test-kernel (0.1.4)  - Simple example of qtpi test kernel python wrapper for Jupyter to enable Qtpi quantum language
qt-reactor (0.6)          - Twisted Qt Integration for Qt4 and Qt5 using qtpy
(Qt5.14.2) nerohmot@THOR:~/Desktop/Repo's/QScreenCast$ 
```

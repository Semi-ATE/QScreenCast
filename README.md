# QScreenCast
A complete screen-caster behind a QToolButton

# Known issues

We need some 'services' from Qt, and it turns out that a same release doesn't implement the same things on differnt OS'es

| Qt | 5.9.2 | 5.12.3 | 5.14 | 5.15 |
|:----:|:------:|:-------:|:-------:|:-------:|
| **Channel** | anaconda | conda-forge | PIP | Qt 5.15 |
|Windows| ✗¹ | ✓ | ✓ | ? |
|Linux| ✗ | ?¹ | ✓ | ? |
|MacOS| ✗ | ? | ? | ? |

²³

Notes:
  * ✗ : does not work
  * ✓ : works
  * ? : not tested yet
  * ✗¹ : Complaining about availability of QMultiMedia, we need that to record the audio
  * ?¹ : Not complaining about QMultiMedia but complaining about codecs ... need to see if I can install the codecs.


```shell
conda install ffmpeg
```

```shell
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
(Qt5.14.2) nerohmot@THOR:~/Desktop/Repo's/QScreenCast$ 
```

# QScreenCast

A no-nonsense [screen-caster](https://en.wikipedia.org/wiki/Screencast) behind a [QToolButton](https://doc.qt.io/qt-5/qtoolbutton.html). 

[![GitHub](https://img.shields.io/github/license/Semi-ATE/QScreenCast?color=black)](https://github.com/Semi-ATE/QScreenCast/blob/main/LICENSE)
[![Conda](https://img.shields.io/conda/pn/conda-forge/QScreenCast?color=black)](https://anaconda.org/conda-forge/QScreenCast)
![Supported Python versions](https://img.shields.io/badge/python-%3E%3D3.7-black)

[![CI](https://github.com/Semi-ATE/QScreenCast/workflows/CI/badge.svg?branch=master)](https://github.com/Semi-ATE/QScreenCast/actions?query=workflow%3ACI)
[![CD](https://github.com/Semi-ATE/QScreenCast/workflows/CD/badge.svg)](https://github.com/Semi-ATE/QScreenCast/actions?query=workflow%3ACD)

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/Semi-ATE/QScreenCast?color=blue&label=GitHub&sort=semver)](https://github.com/Semi-ATE/QScreenCast/releases/latest)
[![GitHub commits since latest release (by date)](https://img.shields.io/github/commits-since/Semi-ATE/QScreenCast/latest)](https://github.com/Semi-ATE/QScreenCast)
[![PyPI](https://img.shields.io/pypi/v/QScreenCast?color=blue&label=PyPI)](https://pypi.org/project/QScreenCast/)
[![Conda (channel only)](https://img.shields.io/conda/vn/conda-forge/QScreenCast?color=blue&label=conda-forge)](https://anaconda.org/conda-forge/qscreencast)
[![conda-forge feedstock](https://img.shields.io/github/issues-pr/conda-forge/qscreencast-feedstock?label=feedstock)](https://github.com/conda-forge/QScreenCast-feedstock)

![PyPI - Downloads](https://img.shields.io/pypi/dm/QScreenCast?color=g&label=PyPI%20downloads)
![Conda](https://img.shields.io/conda/dn/conda-forge/qscreencast?color=g&label=conda-forge%20downloads)

[![GitHub issues](https://img.shields.io/github/issues/Semi-ATE/QScreenCast)](https://github.com/Semi-ATE/QScreenCast/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/Semi-ATE/QScreenCast)](https://github.com/Semi-ATE/QScreenCast/pulls)

A library that exposes a no-nonsense screen caster behind a QToolButton to be incorporated in any Python/Qt application.

## Work in progress

**Force majeure :** Currently `QScreenCast` only works on windows! 😭

`QScreenCast` needs the [Qt Multimedia](https://doc.qt.io/qt-5/multimediaoverview.html) module. 
- On **conda-forge** we have a [pyqt==5.12.3](https://anaconda.org/conda-forge/pyqt), which is semi-broken because for windows the Multimedia module is present, but for Linux & macOS it is not ... 🙈 🙉 🙊
- On **anaconda** the situation is even worse, as there the latest [pyqt==5.9.2](https://anaconda.org/anaconda/pyqt) and the Multimedia module is omitted all toghether. 😩
- On **PyPi** the situation is different, there one can use [PyQt**5**==5.15.4](https://pypi.org/project/PyQt5/) and there (I presume) the Multimedia module is available ... however that opens [yet another can of worms](https://www.youtube.com/watch?v=Ul79ihg41Rs) ...

That being said, [conda-forge/pyqt](https://github.com/conda-forge/pyqt-feedstock/issues) is working on a `pyqt==5.15.x` with all the goodies for all platforms (including [M1](https://www.apple.com/mac/m1/) 😍) but the ETA for that is mid 2021.

The current implementation of `QScreenCast` is a fist (granted a bit naïve) attempt, but we are gearing up to make a second iteration, this time by using [GStreamer](https://gstreamer.freedesktop.org/) under the hood! 😎


## Installation

### conda/mamba (preferred)

```bash
(myenv) me@mybox:~$ conda install -c conda-forge QScreenCast 
```

### pip

Prior to installing `QScreenCast`, you need to install [ffmpeg](https://www.ffmpeg.org/download.html#build-windows)  on your system somehow.

```bash
me@mybox:~$ pip install QScreenCast
```
## Example

The repo holds an `example` directory where it is demonstrated how to use the QScreenCast button in your own application.

## Usage

### left-click on the button

A left-click on the button will start/stop the recording. Both Audio and video are recorded, but **ONLY** the `QMainWindow` is recorded! 😇 To comply to the '[perfect YouTube Video](https://lumen5.com/learn/youtube-video-dimension-and-size/)' recommendations, the `QMainWindow` is re-scaled (in the middle of the current screen) to it's maximum available size that complies to the video sizes. 

Once a recording is stopped, the QScreenCast-er will put the .mp4 file on your desktop.

**Notes:** 

1. While recording, you are not able to re-size or move the `QMainWindow`. 🧐
2. Anything you move in front of the `QMainWindow` will be recorded! 😱
2. When you start a recording, there is a count-down displayed in the middle of your `QMainWindow` to give you the last chance to clear your throught. 🤣 

### right-click on the button

A right-click on the button will show all the different video sizes (the ones that your screen can't handle are grayed out) and a check box will indicate to what format your screen will re-size if you start a recording. By default this is the biggest size your screen can handle, but you can select a smaller size here, in which case your `QMainWindow` will resize to that. One also can select a microphone (in case you have more than one) by default the system microphone is used.

Long story short, you shouldn't have to mess with options, just start/stop your recording!
## Recording formats

- Sizes:
  - 854 x 480 (aka 480p)
  - 1280 x 720 (aka 720p)
  - 1920 x 1080 (aka 1080p and 1K)
  - 2560 x 1440 (aka 1440p and 2K)
  - 3840 x 2160 (aka 2160p and 4K)
- Container: MP4
- Audio codec: AAC-LC (stereo @ 48KHz)
- Video codec: H.264
  - Progressive scan
  - High Profile
  - 2 consecutive B frames
  - Closed GOP
  - CABAC
  - frame rate = 15 fps
  - 4:2:0 Chroma subsampling

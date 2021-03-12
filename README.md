# QScreenCast

A no-nonsense [screen-caster](https://en.wikipedia.org/wiki/Screencast) behind a [QToolButton](https://doc.qt.io/qt-5/qtoolbutton.html). 

[![GitHub](https://img.shields.io/github/license/Semi-ATE/QScreenCast?color=black)](https://github.com/Semi-ATE/QScreenCast/blob/main/LICENSE)
[![Conda](https://img.shields.io/conda/pn/conda-forge/QScreenCast?color=black)](https://anaconda.org/conda-forge/QScreenCast)
![Supported Python versions](https://img.shields.io/badge/python-%3E%3D3.7-black)

[![CI](https://github.com/Semi-ATE/QScreenCast/workflows/CI/badge.svg?branch=master)](https://github.com/Semi-ATE/QScreenCast/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/Semi-ATE/QScreenCast/branch/main/graph/badge.svg?token=BAP0H9OMED)](https://codecov.io/gh/Semi-ATE/QScreenCast)
[![CD](https://github.com/Semi-ATE/QScreenCast/workflows/CD/badge.svg)](https://github.com/Semi-ATE/QScreenCast/actions?query=workflow%3ACD)

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/Semi-ATE/QScreenCast?color=blue&label=GitHub&sort=semver)](https://github.com/Semi-ATE/QScreenCast/releases/latest)
[![GitHub commits since latest release (by date)](https://img.shields.io/github/commits-since/Semi-ATE/QScreenCast/latest)](https://github.com/Semi-ATE/QScreenCast)
[![PyPI](https://img.shields.io/pypi/v/QScreenCast?color=blue&label=PyPI)](https://pypi.org/project/QScreenCast/)
[![Conda (channel only)](https://img.shields.io/conda/vn/conda-forge/QScreenCast?color=blue&label=conda-forge)](https://github.com/conda-forge/QScreenCast-feedstock)

[![GitHub issues](https://img.shields.io/github/issues/Semi-ATE/QScreenCast)](https://github.com/Semi-ATE/QScreenCast/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/Semi-ATE/QScreenCast)](https://github.com/Semi-ATE/QScreenCast/pulls)

An application that uses pyqt >= 5.12 can use this QScreenCast library to enable the creation of screen-casts for documentation/demo/tutorial as well as bug/feature reporting of itself!

QScreenCast also provides this functionality for Spyder >= 5 by means of a plugin declaration. 😍

## Installation

### conda/mamba (preferred)

```bash
(myenv) me@mybox:~$ conda install -c conda-forge QScreenCast 
```

**Note:** that QScreenCast needs pyqt >= 5.12, conda-forge has this (eventhough semi-broken) hence the `-c conda-forge`. The anaconda channel still only has the 5.9.2, but that version doesn't have the Qt Multimedia backend, and QScreenCast needs that, so until pyqt 5.15.3 is out, pure anaconda users are left in the cold 😭

### pip

```bash
me@mybox:~$ pip install QScreenCast
```

**Note:** The pip installation is not tested so much, we test the conda installation, but as the project is released to PyPi and a conda-forge feedstock 'monitors' the Python Package Index, it should work (if pip can resolve the dependencies that is)

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
  - 462 x 240 (aka 240p)
  - 640 x 360 (aka 360p)
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

## Work in progress

The current implementation is a fist (granted a bit naive) attempt, but we are gearing up to make a second iteration, this time by using [GStreamer](https://gstreamer.freedesktop.org/) under the hood! 😎

There is of course the topic [pyqt 5.15.3](https://github.com/conda-forge/qt-feedstock) via conda-forge, as well as Windows/Linux/MacOS version differences ... 🙈 🙉 🙊

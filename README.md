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

An application that uses pyqt >= 5.12 can use this QScreenCast library to enable the creation of screen-casts for documentation/demo/tutorial as well as bug/feature reporting of itself!

QScreenCast also provides this functionality for Spyder >= 5 by means of a plugin declaration. 😍

## Installation

### conda/mamba (preferred)

```bash
(myenv) me@mybox:~$ conda install -c conda-forge QScreenCast 
```

**Note:** that QScreenCast needs pyqt >= 5.12 conda-forge has this (eventhough semi-broken) hence the `-c conda-forge`. The anaconda channel still only has the 5.9.2, but that version doesn't have the Qt Multimedia backend, and QScreenCast needs that, so until pyqt 5.15.3 is out pure anaconda users are left in the cold 😭

### pip

```bash
me@mybox:~$ pip install QScreenCast
```

**Note:** The pip installation is not tested so much, we test the conda installation, but as the project is released to PyPi and a conda-forge feedstock 'monitors' the Python Package Index, it should work (if pip can resolve the dependencies that is)

## Example

The repo holds an `example` directory where it is demonstrated how to use the QScreenCast button in your own application.


## Work in progress

The current implementation is a fist (granted a bit naive) attempt, but we are gearing up to make a second iteration, this time by using [GStreamer](https://gstreamer.freedesktop.org/) under the hood! 😎

There is of course the topic [pyqt 5.15.3](https://github.com/conda-forge/qt-feedstock) via conda-forge, as well as Windows/Linux/MacOS version differences ... 🙈 🙉 🙊

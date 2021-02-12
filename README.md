# QScreenCast
A no-nonsense [screen-caster](https://en.wikipedia.org/wiki/Screencast) behind a [QToolButton](https://doc.qt.io/qt-5/qtoolbutton.html). 

Any Qt application then can use the QScreenCast button to enable the creation of screen-casts for documentation as well as bug/feature reporting.
The idea is that by installing QScreenCast (via pip/conda) the plugin for Spyder5 to make screen casts is already there. 

The current implementation is a fist (granted a bit naive) attempt, but we are gearing up to make a second iteration, this time by using [GStreamer](https://gstreamer.freedesktop.org/) under the hood!

There is of course the topic Qt 5.15.2 via conda-forge, as well as Windows/Linux/MacOS version differences ... (note we need a conda package for this, PyPI is a bonus)

More info can be found on the [wiki](https://github.com/nerohmot/QScreenCast/wiki).

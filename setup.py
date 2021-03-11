# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © Tom Hören
#
# Licensed under the terms of the MIT License
# ----------------------------------------------------------------------------
"""
Python QScreenCaster.
"""

# Third party imports
from setuptools import find_packages, setup

# Local imports
from QScreenCast import __version__


setup(
    name="QScreenCast",
    version=__version__,
    packages=find_packages(),
    # See: https://setuptools.readthedocs.io/en/latest/setuptools.html
    entry_points={
        "spyder.plugins": [
            "screencast = QScreenCast.spyder.plugin:ScreenCast"
        ],
    }
)

# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © Tom Hören

# Licensed under the terms of the MIT License
# ----------------------------------------------------------------------------
"""
Python QtScreenCaster Spyder Widgets.
"""

# Third party imports
from qtpy.QtWidgets import QVBoxLayout, QWidget
from spyder.api.translations import get_translation

# Local imports
from qscreencast.QtScreenCast import ScreenCastToolButton


# Localization
_ = get_translation('qscreencast.spyder')


# TODO: Change to use the base status widget not yet available
class ScreenCastStatusWidget(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        # Widgets
        self.button = ScreenCastToolButton(self)

        # # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def start_recording(self):
        pass

    def stop_recording(self):
        pass

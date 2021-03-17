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
from spyder.api.widgets.status import StatusBarWidget

# Local imports
from QScreenCast import ScreenCastToolButton


# Localization
_ = get_translation('qscreencast.spyder')


# TODO: Change to use the base status widget not yet available
class ScreenCastStatusWidget(StatusBarWidget):
    ID = 'screen_caster'
    CUSTOM_WIDGET_CLASS = ScreenCastToolButton

    def __init__(self, parent, main_window):
        super().__init__(parent, show_icon=False, show_label=False)
        self.custom_widget.setup(main_window)

    def start_recording(self):
        pass

    def stop_recording(self):
        pass

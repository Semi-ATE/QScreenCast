# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © Tom Hören

# Licensed under the terms of the MIT License
# ----------------------------------------------------------------------------
"""
Python QtScreenCaster Spyder Widgets.
"""

# Third party imports
from qtpy.QtCore import QSize, QPoint, Signal
from spyder.api.translations import get_translation
from spyder.api.widgets import PluginMainContainer

# Local imports
from qscreencast.spyder.api import ScreenResolutions
from qscreencast.spyder.widgets import ScreenCastStatusWidget


# Localization
_ = get_translation('qscreencast.spyder')


class ScreenCastContainer(PluginMainContainer):
    DEFAULT_OPTIONS = {
        'resolution': ScreenResolutions.Screen1080x1020
    }

    # Signals
    sig_resize_main_window_requested = Signal(QSize)
    sig_move_main_window_requested = Signal(QPoint)

    def __init__(self, name, plugin, parent=None, options=DEFAULT_OPTIONS):
        super().__init__(name, plugin, parent, options)

        self.status = ScreenCastStatusWidget(parent=self)

    # --- PluginMainContainer API
    # ------------------------------------------------------------------------
    def setup(self):
        self.create_action(
            'screencast_action',
            test=_("Start recording..."),
            icon=self.get_icon(),
            triggered=self.start_recording,
        )

    def on_option_update(self, option, value):
        pass

    def update_actions(self):
        pass

    # --- Public API
    # ------------------------------------------------------------------------
    def start_recording(self):
        pass

    def stop_recording(self):
        pass

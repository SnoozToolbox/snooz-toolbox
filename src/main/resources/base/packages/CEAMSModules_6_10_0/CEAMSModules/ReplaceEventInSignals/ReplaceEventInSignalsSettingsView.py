"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the ReplaceEventInSignals plugin
"""

from qtpy import QtWidgets

from CEAMSModules.ReplaceEventInSignals.Ui_ReplaceEventInSignalsSettingsView import Ui_ReplaceEventInSignalsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class ReplaceEventInSignalsSettingsView( BaseSettingsView,  Ui_ReplaceEventInSignalsSettingsView, QtWidgets.QWidget):
    """
        ReplaceEventInSignalsView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
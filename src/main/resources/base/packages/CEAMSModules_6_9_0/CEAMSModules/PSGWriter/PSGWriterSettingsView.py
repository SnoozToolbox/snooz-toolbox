"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the PSGWriter plugin
"""

from qtpy import QtWidgets

from CEAMSModules.PSGWriter.Ui_PSGWriterSettingsView import Ui_PSGWriterSettingsView
from commons.BaseSettingsView import BaseSettingsView

class PSGWriterSettingsView( BaseSettingsView,  Ui_PSGWriterSettingsView, QtWidgets.QWidget):
    """
        PSGWriterView display the spectrum from SpectraViewver into
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
"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the Resample plugin
"""

from qtpy import QtWidgets

from CEAMSModules.Resample.Ui_ResampleSettingsView import Ui_ResampleSettingsView
from commons.BaseSettingsView import BaseSettingsView

class ResampleSettingsView( BaseSettingsView,  Ui_ResampleSettingsView, QtWidgets.QWidget):
    """
        ResampleView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        self.target_sample_rate_lineedit.init(self._parent_node.identifier, 
                                                'sample_rate', 
                                                self._pub_sub_manager)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
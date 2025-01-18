"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the Constant plugin
"""

from qtpy import QtWidgets

from CEAMSModules.Constant.Ui_ConstantSettingsView import Ui_ConstantSettingsView
from commons.BaseSettingsView import BaseSettingsView

class ConstantSettingsView( BaseSettingsView,  Ui_ConstantSettingsView, QtWidgets.QWidget):
    """
        ConstantView set the constant settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        self.constant_lineedit.init(self._parent_node.identifier, 
                                                'constant', 
                                                self._pub_sub_manager)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
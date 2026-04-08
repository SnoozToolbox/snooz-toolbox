"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the AliasSignals plugin
"""

from qtpy import QtWidgets

from CEAMSModules.AliasSignals.Ui_AliasSignalsSettingsView import Ui_AliasSignalsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class AliasSignalsSettingsView( BaseSettingsView,  Ui_AliasSignalsSettingsView, QtWidgets.QWidget):
    """
        AliasSignalsView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        self.alias_lineedit.init(self._parent_node.identifier, 
                                                'alias', 
                                                self._pub_sub_manager)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass
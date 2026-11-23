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
        Set the AliasSignals settings.
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        self._alias_topic = f'{self._parent_node.identifier}.alias'
        self._pub_sub_manager.subscribe(self, self._alias_topic)

    def load_settings(self):
        self._pub_sub_manager.publish(self, self._alias_topic, 'ping')

    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._alias_topic, self.alias_lineedit.text())

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        if topic == self._alias_topic:
            self.alias_lineedit.setText(str(message))

    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._alias_topic)
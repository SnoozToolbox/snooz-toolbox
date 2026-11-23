"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
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
        self._constant_topic = f'{self._parent_node.identifier}.constant'
        self._pub_sub_manager.subscribe(self, self._constant_topic)

    def load_settings(self):
        self._pub_sub_manager.publish(self, self._constant_topic, 'ping')

    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._constant_topic, self.constant_lineedit.text())

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        if topic == self._constant_topic:
            self.constant_lineedit.setText(str(message))

    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._constant_topic)
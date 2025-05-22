"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Settings viewer of the InvertSignals plugin
"""

from qtpy import QtWidgets

from CEAMSModules.InvertSignals.Ui_InvertSignalsSettingsView import Ui_InvertSignalsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class InvertSignalsSettingsView(BaseSettingsView, Ui_InvertSignalsSettingsView, QtWidgets.QWidget):
    """
        InvertSignalsView set the InvertSignals settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._signals_topic = f'{self._parent_node.identifier}.signals'
        self._pub_sub_manager.subscribe(self, self._signals_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._signals_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to InvertSignals
        self._pub_sub_manager.publish(self, self._signals_topic, str(self.signals_lineedit.text()))
        


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._signals_topic:
            self.signals_lineedit.setText(message)
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._signals_topic)
            
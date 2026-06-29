"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Settings viewer of the REMsDetectionYasa plugin
"""

from qtpy import QtWidgets

from CEAMSModules.REMsDetectionYasa.Ui_REMsDetectionYasaSettingsView import Ui_REMsDetectionYasaSettingsView
from commons.BaseSettingsView import BaseSettingsView

class REMsDetectionYasaSettingsView(BaseSettingsView, Ui_REMsDetectionYasaSettingsView, QtWidgets.QWidget):
    """
        REMsDetectionYasaView set the REMsDetectionYasa settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._signal_topic = f'{self._parent_node.identifier}.signal'
        self._pub_sub_manager.subscribe(self, self._signal_topic)
        self._events_topic = f'{self._parent_node.identifier}.events'
        self._pub_sub_manager.subscribe(self, self._events_topic)
        self._sleepstages_topic = f'{self._parent_node.identifier}.sleepstages'
        self._pub_sub_manager.subscribe(self, self._sleepstages_topic)
        self._thresholds_topic = f'{self._parent_node.identifier}.thresholds'
        self._pub_sub_manager.subscribe(self, self._thresholds_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._signal_topic, 'ping')
        self._pub_sub_manager.publish(self, self._events_topic, 'ping')
        self._pub_sub_manager.publish(self, self._sleepstages_topic, 'ping')
        self._pub_sub_manager.publish(self, self._thresholds_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to REMsDetectionYasa
        self._pub_sub_manager.publish(self, self._signal_topic, str(self.signal_lineedit.text()))
        self._pub_sub_manager.publish(self, self._events_topic, str(self.events_lineedit.text()))
        self._pub_sub_manager.publish(self, self._sleepstages_topic, str(self.sleepstages_lineedit.text()))
        self._pub_sub_manager.publish(self, self._thresholds_topic, str(self.thresholds_lineedit.text()))
        


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._signal_topic:
            self.signal_lineedit.setText(message)
        if topic == self._events_topic:
            self.events_lineedit.setText(message)
        if topic == self._sleepstages_topic:
            self.sleepstages_lineedit.setText(message)
        if topic == self._thresholds_topic:
            self.thresholds_lineedit.setText(message)
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._signal_topic)
            self._pub_sub_manager.unsubscribe(self, self._events_topic)
            self._pub_sub_manager.unsubscribe(self, self._sleepstages_topic)
            self._pub_sub_manager.unsubscribe(self, self._thresholds_topic)
            
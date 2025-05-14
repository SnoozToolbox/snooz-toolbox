"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Settings viewer of the Yasa plugin
"""

from qtpy import QtWidgets

from CEAMSModules.YasaSleepStaging.Ui_YasaSleepStagingSettingsView import Ui_YasaSleepStagingSettingsView
from commons.BaseSettingsView import BaseSettingsView

class YasaSleepStagingSettingsView(BaseSettingsView, Ui_YasaSleepStagingSettingsView, QtWidgets.QWidget):
    """
        YasaSleepStagingView set the YasaSleepStaging settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._filename_topic = f'{self._parent_node.identifier}.filename'
        self._pub_sub_manager.subscribe(self, self._filename_topic)
        self._signals_topic = f'{self._parent_node.identifier}.signals'
        self._pub_sub_manager.subscribe(self, self._signals_topic)
        self._sleep_stages_topic = f'{self._parent_node.identifier}.sleep_stages'
        self._pub_sub_manager.subscribe(self, self._sleep_stages_topic)
        self._events_topic = f'{self._parent_node.identifier}.events'
        self._pub_sub_manager.subscribe(self, self._events_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._filename_topic, 'ping')
        self._pub_sub_manager.publish(self, self._signals_topic, 'ping')
        self._pub_sub_manager.publish(self, self._sleep_stages_topic, 'ping')
        self._pub_sub_manager.publish(self, self._events_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to Yasa
        self._pub_sub_manager.publish(self, self._filename_topic, str(self.filename_lineedit.text()))
        self._pub_sub_manager.publish(self, self._signals_topic, str(self.signals_lineedit.text()))
        self._pub_sub_manager.publish(self, self._sleep_stages_topic, str(self.sleep_stages_lineedit.text()))
        self._pub_sub_manager.publish(self, self._events_topic, str(self.events_lineedit.text()))
        


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._filename_topic:
            self.filename_lineedit.setText(message)
        if topic == self._signals_topic:
            self.signals_lineedit.setText(message)
        if topic == self._sleep_stages_topic:
            self.sleep_stages_lineedit.setText(message)
        if topic == self._events_topic:
            self.events_lineedit.setText(message)
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)
            self._pub_sub_manager.unsubscribe(self, self._signals_topic)
            self._pub_sub_manager.unsubscribe(self, self._sleep_stages_topic)
            self._pub_sub_manager.unsubscribe(self, self._events_topic)
            
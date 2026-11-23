"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Settings viewer of the TrimSignal plugin
"""

from qtpy import QtWidgets

from CEAMSModules.TrimSignal.Ui_TrimSignalSettingsView import Ui_TrimSignalSettingsView
from commons.BaseSettingsView import BaseSettingsView

class TrimSignalSettingsView(BaseSettingsView, Ui_TrimSignalSettingsView, QtWidgets.QWidget):
    """
        TrimSignalView set the TrimSignal settings
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
        self._events_topic = f'{self._parent_node.identifier}.events'
        self._pub_sub_manager.subscribe(self, self._events_topic)
        self._start_sec_topic = f'{self._parent_node.identifier}.start_sec'
        self._pub_sub_manager.subscribe(self, self._start_sec_topic)
        self._duration_sec_topic = f'{self._parent_node.identifier}.duration_sec'
        self._pub_sub_manager.subscribe(self, self._duration_sec_topic)
        self._reset_time_topic = f'{self._parent_node.identifier}.reset_time'
        self._pub_sub_manager.subscribe(self, self._reset_time_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._signals_topic, 'ping')
        self._pub_sub_manager.publish(self, self._events_topic, 'ping')
        self._pub_sub_manager.publish(self, self._start_sec_topic, 'ping')
        self._pub_sub_manager.publish(self, self._duration_sec_topic, 'ping')
        self._pub_sub_manager.publish(self, self._reset_time_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to TrimSignal
        self._pub_sub_manager.publish(self, self._start_sec_topic, str(self.start_sec_lineedit.text()))
        self._pub_sub_manager.publish(self, self._duration_sec_topic, str(self.duration_sec_lineedit.text()))
        self._pub_sub_manager.publish(self, self._reset_time_topic, str(self.checkBox.isChecked()))
        


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._start_sec_topic:
            self.start_sec_lineedit.setText(message)
        if topic == self._duration_sec_topic:
            self.duration_sec_lineedit.setText(message)
        if topic == self._reset_time_topic:
            self.checkBox.setChecked(message in [True, 1, 'True' ,'true', '1', 'yes'])

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._signals_topic)
            self._pub_sub_manager.unsubscribe(self, self._events_topic)
            self._pub_sub_manager.unsubscribe(self, self._start_sec_topic)
            self._pub_sub_manager.unsubscribe(self, self._duration_sec_topic)
            self._pub_sub_manager.unsubscribe(self, self._reset_time_topic)
            
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Settings viewer of the IRASAYASA plugin
"""

from qtpy import QtWidgets

from CEAMSModules.IRASAYASA.Ui_IRASAYASASettingsView import Ui_IRASAYASASettingsView
from commons.BaseSettingsView import BaseSettingsView

class IRASAYASASettingsView(BaseSettingsView, Ui_IRASAYASASettingsView, QtWidgets.QWidget):
    """
        IRASAYASAView set the IRASAYASA settings
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
        self._win_len_sec_topic = f'{self._parent_node.identifier}.win_len_sec'
        self._pub_sub_manager.subscribe(self, self._win_len_sec_topic)
        self._win_step_sec_topic = f'{self._parent_node.identifier}.win_step_sec'
        self._pub_sub_manager.subscribe(self, self._win_step_sec_topic)
        self._window_name_topic = f'{self._parent_node.identifier}.window_name'
        self._pub_sub_manager.subscribe(self, self._window_name_topic)
        self._first_freq_topic = f'{self._parent_node.identifier}.first_freq'
        self._pub_sub_manager.subscribe(self, self._first_freq_topic)
        self._last_freq_topic = f'{self._parent_node.identifier}.last_freq'
        self._pub_sub_manager.subscribe(self, self._last_freq_topic)
        self._flag_topic = f'{self._parent_node.identifier}.flag'
        self._pub_sub_manager.subscribe(self, self._flag_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._signals_topic, 'ping')
        self._pub_sub_manager.publish(self, self._win_len_sec_topic, 'ping')
        self._pub_sub_manager.publish(self, self._win_step_sec_topic, 'ping')
        self._pub_sub_manager.publish(self, self._window_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._first_freq_topic, 'ping')
        self._pub_sub_manager.publish(self, self._last_freq_topic, 'ping')
        self._pub_sub_manager.publish(self, self._flag_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to IRASAYASA
        self._pub_sub_manager.publish(self, self._signals_topic, str(self.signals_lineedit.text()))
        self._pub_sub_manager.publish(self, self._win_len_sec_topic, str(self.win_len_sec_lineedit.text()))
        self._pub_sub_manager.publish(self, self._win_step_sec_topic, str(self.win_step_sec_lineedit.text()))
        self._pub_sub_manager.publish(self, self._window_name_topic, str(self.window_name_comboBox.currentText()))
        self._pub_sub_manager.publish(self, self._first_freq_topic, str(self.first_freq_lineedit.text()))
        self._pub_sub_manager.publish(self, self._last_freq_topic, str(self.last_freq_lineedit.text()))
        self._pub_sub_manager.publish(self, self._flag_topic, str(self.flag_lineedit.text()))
        


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._signals_topic:
            self.signals_lineedit.setText(message)
        if topic == self._win_len_sec_topic:
            self.win_len_sec_lineedit.setText(message)
        if topic == self._win_step_sec_topic:
            self.win_step_sec_lineedit.setText(message)
        if topic == self._window_name_topic:
            self.window_name_comboBox.setCurrentText(message)
        if topic == self._first_freq_topic:
            self.first_freq_lineedit.setText(message)
        if topic == self._last_freq_topic:
            self.last_freq_lineedit.setText(message)
        if topic == self._flag_topic:
            self.flag_lineedit.setText(message)
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._signals_topic)
            self._pub_sub_manager.unsubscribe(self, self._win_len_sec_topic)
            self._pub_sub_manager.unsubscribe(self, self._win_step_sec_topic)
            self._pub_sub_manager.unsubscribe(self, self._window_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._first_freq_topic)
            self._pub_sub_manager.unsubscribe(self, self._last_freq_topic)
            self._pub_sub_manager.unsubscribe(self, self._flag_topic)
            
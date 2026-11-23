"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Settings viewer of the NetworkProperties plugin
"""

from qtpy import QtWidgets

from CEAMSModules.NetworkProperties.Ui_NetworkPropertiesSettingsView import Ui_NetworkPropertiesSettingsView
from commons.BaseSettingsView import BaseSettingsView

class NetworkPropertiesSettingsView(BaseSettingsView, Ui_NetworkPropertiesSettingsView, QtWidgets.QWidget):
    """
        NetworkPropertiesView set the NetworkProperties settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._recording_path_topic = f'{self._parent_node.identifier}.recording_path'
        self._pub_sub_manager.subscribe(self, self._recording_path_topic)
        self._subject_info_topic = f'{self._parent_node.identifier}.subject_info'
        self._pub_sub_manager.subscribe(self, self._subject_info_topic)
        self._con_dict_topic = f'{self._parent_node.identifier}.con_dict'
        self._pub_sub_manager.subscribe(self, self._con_dict_topic)
        self._threshold_mode_topic = f'{self._parent_node.identifier}.threshold_mode'
        self._pub_sub_manager.subscribe(self, self._threshold_mode_topic)
        self._threshold_value_topic = f'{self._parent_node.identifier}.threshold_value'
        self._pub_sub_manager.subscribe(self, self._threshold_value_topic)
        self._output_path_topic = f'{self._parent_node.identifier}.output_path'
        self._pub_sub_manager.subscribe(self, self._output_path_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._recording_path_topic, 'ping')
        self._pub_sub_manager.publish(self, self._subject_info_topic, 'ping')
        self._pub_sub_manager.publish(self, self._con_dict_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_mode_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_value_topic, 'ping')
        self._pub_sub_manager.publish(self, self._output_path_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to NetworkProperties
        self._pub_sub_manager.publish(self, self._recording_path_topic, str(self.recording_path_lineedit.text()))
        self._pub_sub_manager.publish(self, self._subject_info_topic, str(self.subject_info_lineedit.text()))
        self._pub_sub_manager.publish(self, self._con_dict_topic, str(self.con_dict_lineedit.text()))
        self._pub_sub_manager.publish(self, self._threshold_mode_topic, str(self.threshold_mode_lineedit.text()))
        self._pub_sub_manager.publish(self, self._threshold_value_topic, str(self.threshold_value_lineedit.text()))
        self._pub_sub_manager.publish(self, self._output_path_topic, str(self.output_path_lineedit.text()))
        


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._recording_path_topic:
            self.recording_path_lineedit.setText(message)
        if topic == self._subject_info_topic:
            self.subject_info_lineedit.setText(message)
        if topic == self._con_dict_topic:
            self.con_dict_lineedit.setText(message)
        if topic == self._threshold_mode_topic:
            self.threshold_mode_lineedit.setText(message)
        if topic == self._threshold_value_topic:
            self.threshold_value_lineedit.setText(message)
        if topic == self._output_path_topic:
            self.output_path_lineedit.setText(message)
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._recording_path_topic)
            self._pub_sub_manager.unsubscribe(self, self._subject_info_topic)
            self._pub_sub_manager.unsubscribe(self, self._con_dict_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_mode_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_value_topic)
            self._pub_sub_manager.unsubscribe(self, self._output_path_topic)
            
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the OxygenDesatDetector plugin
"""

from qtpy import QtWidgets

from CEAMSModules.OxygenDesatDetector.Ui_OxygenDesatDetectorSettingsView import Ui_OxygenDesatDetectorSettingsView
from commons.BaseSettingsView import BaseSettingsView

class OxygenDesatDetectorSettingsView(BaseSettingsView, Ui_OxygenDesatDetectorSettingsView, QtWidgets.QWidget):
    """
        OxygenDesatDetectorView set the OxygenDesatDetector settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._artifact_group_topic = f'{self._parent_node.identifier}.artifact_group'
        self._pub_sub_manager.subscribe(self, self._artifact_group_topic)
        self._artifact_name_topic = f'{self._parent_node.identifier}.artifact_name'
        self._pub_sub_manager.subscribe(self, self._artifact_name_topic)
        self._arousal_group_topic = f'{self._parent_node.identifier}.arousal_group'
        self._pub_sub_manager.subscribe(self, self._arousal_group_topic)
        self._arousal_name_topic = f'{self._parent_node.identifier}.arousal_name'
        self._pub_sub_manager.subscribe(self, self._arousal_name_topic)
        self._parameters_oxy_topic = f'{self._parent_node.identifier}.parameters_oxy'
        self._pub_sub_manager.subscribe(self, self._parameters_oxy_topic)
        self._parameters_cycle_topic = f'{self._parent_node.identifier}.parameters_cycle'
        self._pub_sub_manager.subscribe(self, self._parameters_cycle_topic)
        self._cohort_filename_topic = f'{self._parent_node.identifier}.cohort_filename'
        self._pub_sub_manager.subscribe(self, self._cohort_filename_topic)
        

    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._artifact_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._artifact_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._arousal_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._arousal_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._parameters_oxy_topic, 'ping')
        self._pub_sub_manager.publish(self, self._parameters_cycle_topic, 'ping')
        self._pub_sub_manager.publish(self, self._cohort_filename_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to OxygenDesatDetector
        self._pub_sub_manager.publish(self, self._artifact_group_topic, str(self.artifact_group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._artifact_name_topic, str(self.artifact_name_lineedit.text()))
        self._pub_sub_manager.publish(self, self._arousal_group_topic, str(self.arousal_group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._arousal_name_topic, str(self.arousal_name_lineedit.text()))
        self._pub_sub_manager.publish(self, self._parameters_oxy_topic, str(self.parameters_oxy_lineedit.text()))
        self._pub_sub_manager.publish(self, self._parameters_cycle_topic, str(self.parameters_cycle_lineedit.text()))
        self._pub_sub_manager.publish(self, self._cohort_filename_topic, str(self.cohort_filename_lineedit.text()))
        

    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._artifact_group_topic:
            self.artifact_group_lineedit.setText(message)
        if topic == self._artifact_name_topic:
            self.artifact_name_lineedit.setText(message)
        if topic == self._arousal_group_topic:
            self.arousal_group_lineedit.setText(message)
        if topic == self._arousal_name_topic:
            self.arousal_name_lineedit.setText(message)
        if topic == self._parameters_oxy_topic:
            self.parameters_oxy_lineedit.setText(message)
        if topic == self._parameters_cycle_topic:
            self.parameters_cycle_lineedit.setText(message)
        if topic == self._cohort_filename_topic:
            self.cohort_filename_lineedit.setText(message)
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._artifact_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._artifact_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._arousal_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._arousal_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._parameters_oxy_topic)
            self._pub_sub_manager.unsubscribe(self, self._parameters_cycle_topic)
            self._pub_sub_manager.unsubscribe(self, self._cohort_filename_topic)
            
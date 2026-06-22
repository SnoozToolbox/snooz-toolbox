"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Settings viewer of the PSACompilationFOOOF plugin
"""

from qtpy import QtWidgets

from CEAMSModules.PSACompilationFOOOF.Ui_PSACompilationFOOOFSettingsView import Ui_PSACompilationFOOOFSettingsView
from commons.BaseSettingsView import BaseSettingsView

class PSACompilationFOOOFSettingsView(BaseSettingsView, Ui_PSACompilationFOOOFSettingsView, QtWidgets.QWidget):
    """
        PSACompilationFOOOFView set the PSACompilationFOOOF settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._subject_info_topic = f'{self._parent_node.identifier}.subject_info'
        self._pub_sub_manager.subscribe(self, self._subject_info_topic)
        self._PSD_topic = f'{self._parent_node.identifier}.PSD'
        self._pub_sub_manager.subscribe(self, self._PSD_topic)
        self._events_topic = f'{self._parent_node.identifier}.events'
        self._pub_sub_manager.subscribe(self, self._events_topic)
        self._sleep_stages_topic = f'{self._parent_node.identifier}.sleep_stages'
        self._pub_sub_manager.subscribe(self, self._sleep_stages_topic)
        self._mini_bandwidth_topic = f'{self._parent_node.identifier}.mini_bandwidth'
        self._pub_sub_manager.subscribe(self, self._mini_bandwidth_topic)
        self._first_freq_topic = f'{self._parent_node.identifier}.first_freq'
        self._pub_sub_manager.subscribe(self, self._first_freq_topic)
        self._last_freq_topic = f'{self._parent_node.identifier}.last_freq'
        self._pub_sub_manager.subscribe(self, self._last_freq_topic)
        self._dist_total_topic = f'{self._parent_node.identifier}.dist_total'
        self._pub_sub_manager.subscribe(self, self._dist_total_topic)
        self._dist_hour_topic = f'{self._parent_node.identifier}.dist_hour'
        self._pub_sub_manager.subscribe(self, self._dist_hour_topic)
        self._dist_cycle_topic = f'{self._parent_node.identifier}.dist_cycle'
        self._pub_sub_manager.subscribe(self, self._dist_cycle_topic)
        self._parameters_cycle_topic = f'{self._parent_node.identifier}.parameters_cycle'
        self._pub_sub_manager.subscribe(self, self._parameters_cycle_topic)
        self._artefact_group_topic = f'{self._parent_node.identifier}.artefact_group'
        self._pub_sub_manager.subscribe(self, self._artefact_group_topic)
        self._artefact_name_topic = f'{self._parent_node.identifier}.artefact_name'
        self._pub_sub_manager.subscribe(self, self._artefact_name_topic)
        self._cycle_labelled_topic = f'{self._parent_node.identifier}.cycle_labelled'
        self._pub_sub_manager.subscribe(self, self._cycle_labelled_topic)
        self._report_constants_topic = f'{self._parent_node.identifier}.report_constants'
        self._pub_sub_manager.subscribe(self, self._report_constants_topic)
        self._filename_topic = f'{self._parent_node.identifier}.filename'
        self._pub_sub_manager.subscribe(self, self._filename_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._subject_info_topic, 'ping')
        self._pub_sub_manager.publish(self, self._PSD_topic, 'ping')
        self._pub_sub_manager.publish(self, self._events_topic, 'ping')
        self._pub_sub_manager.publish(self, self._sleep_stages_topic, 'ping')
        self._pub_sub_manager.publish(self, self._mini_bandwidth_topic, 'ping')
        self._pub_sub_manager.publish(self, self._first_freq_topic, 'ping')
        self._pub_sub_manager.publish(self, self._last_freq_topic, 'ping')
        self._pub_sub_manager.publish(self, self._dist_total_topic, 'ping')
        self._pub_sub_manager.publish(self, self._dist_hour_topic, 'ping')
        self._pub_sub_manager.publish(self, self._dist_cycle_topic, 'ping')
        self._pub_sub_manager.publish(self, self._parameters_cycle_topic, 'ping')
        self._pub_sub_manager.publish(self, self._artefact_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._artefact_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._cycle_labelled_topic, 'ping')
        self._pub_sub_manager.publish(self, self._report_constants_topic, 'ping')
        self._pub_sub_manager.publish(self, self._filename_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to PSACompilationFOOOF
        self._pub_sub_manager.publish(self, self._subject_info_topic, str(self.subject_info_lineedit.text()))
        self._pub_sub_manager.publish(self, self._PSD_topic, str(self.PSD_lineedit.text()))
        self._pub_sub_manager.publish(self, self._events_topic, str(self.events_lineedit.text()))
        self._pub_sub_manager.publish(self, self._sleep_stages_topic, str(self.sleep_stages_lineedit.text()))
        self._pub_sub_manager.publish(self, self._mini_bandwidth_topic, str(self.mini_bandwidth_lineedit.text()))
        self._pub_sub_manager.publish(self, self._first_freq_topic, str(self.first_freq_lineedit.text()))
        self._pub_sub_manager.publish(self, self._last_freq_topic, str(self.last_freq_lineedit.text()))
        self._pub_sub_manager.publish(self, self._dist_total_topic, str(self.dist_total_lineedit.text()))
        self._pub_sub_manager.publish(self, self._dist_hour_topic, str(self.dist_hour_lineedit.text()))
        self._pub_sub_manager.publish(self, self._dist_cycle_topic, str(self.dist_cycle_lineedit.text()))
        self._pub_sub_manager.publish(self, self._parameters_cycle_topic, str(self.parameters_cycle_lineedit.text()))
        self._pub_sub_manager.publish(self, self._artefact_group_topic, str(self.artefact_group_lineedit.text()))
        self._pub_sub_manager.publish(self, self._artefact_name_topic, str(self.artefact_name_lineedit.text()))
        self._pub_sub_manager.publish(self, self._cycle_labelled_topic, str(self.cycle_labelled_lineedit.text()))
        self._pub_sub_manager.publish(self, self._report_constants_topic, str(self.report_constants_lineedit.text()))
        self._pub_sub_manager.publish(self, self._filename_topic, str(self.filename_lineedit.text()))
        


    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._subject_info_topic:
            self.subject_info_lineedit.setText(message)
        if topic == self._PSD_topic:
            self.PSD_lineedit.setText(message)
        if topic == self._events_topic:
            self.events_lineedit.setText(message)
        if topic == self._sleep_stages_topic:
            self.sleep_stages_lineedit.setText(message)
        if topic == self._mini_bandwidth_topic:
            self.mini_bandwidth_lineedit.setText(message)
        if topic == self._first_freq_topic:
            self.first_freq_lineedit.setText(message)
        if topic == self._last_freq_topic:
            self.last_freq_lineedit.setText(message)
        if topic == self._dist_total_topic:
            self.dist_total_lineedit.setText(message)
        if topic == self._dist_hour_topic:
            self.dist_hour_lineedit.setText(message)
        if topic == self._dist_cycle_topic:
            self.dist_cycle_lineedit.setText(message)
        if topic == self._parameters_cycle_topic:
            self.parameters_cycle_lineedit.setText(message)
        if topic == self._artefact_group_topic:
            self.artefact_group_lineedit.setText(message)
        if topic == self._artefact_name_topic:
            self.artefact_name_lineedit.setText(message)
        if topic == self._cycle_labelled_topic:
            self.cycle_labelled_lineedit.setText(message)
        if topic == self._report_constants_topic:
            self.report_constants_lineedit.setText(message)
        if topic == self._filename_topic:
            self.filename_lineedit.setText(message)
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._subject_info_topic)
            self._pub_sub_manager.unsubscribe(self, self._PSD_topic)
            self._pub_sub_manager.unsubscribe(self, self._events_topic)
            self._pub_sub_manager.unsubscribe(self, self._sleep_stages_topic)
            self._pub_sub_manager.unsubscribe(self, self._mini_bandwidth_topic)
            self._pub_sub_manager.unsubscribe(self, self._first_freq_topic)
            self._pub_sub_manager.unsubscribe(self, self._last_freq_topic)
            self._pub_sub_manager.unsubscribe(self, self._dist_total_topic)
            self._pub_sub_manager.unsubscribe(self, self._dist_hour_topic)
            self._pub_sub_manager.unsubscribe(self, self._dist_cycle_topic)
            self._pub_sub_manager.unsubscribe(self, self._parameters_cycle_topic)
            self._pub_sub_manager.unsubscribe(self, self._artefact_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._artefact_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._cycle_labelled_topic)
            self._pub_sub_manager.unsubscribe(self, self._report_constants_topic)
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)
            
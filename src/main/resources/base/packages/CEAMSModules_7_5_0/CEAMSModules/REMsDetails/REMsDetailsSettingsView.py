"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Settings viewer of the REMsDetails plugin
"""

from qtpy import QtWidgets

from CEAMSModules.REMsDetails.Ui_REMsDetailsSettingsView import Ui_REMsDetailsSettingsView
from commons.BaseSettingsView import BaseSettingsView

class REMsDetailsSettingsView(BaseSettingsView, Ui_REMsDetailsSettingsView, QtWidgets.QWidget):
    """
        REMsDetailsView set the REMsDetails settings
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
        self._signals_topic = f'{self._parent_node.identifier}.signals'
        self._pub_sub_manager.subscribe(self, self._signals_topic)
        self._rems_events_details_topic = f'{self._parent_node.identifier}.rems_events_details'
        self._pub_sub_manager.subscribe(self, self._rems_events_details_topic)
        self._artifact_events_topic = f'{self._parent_node.identifier}.artifact_events'
        self._pub_sub_manager.subscribe(self, self._artifact_events_topic)
        self._sleep_cycle_param_topic = f'{self._parent_node.identifier}.sleep_cycle_param'
        self._pub_sub_manager.subscribe(self, self._sleep_cycle_param_topic)
        self._stages_cycles_topic = f'{self._parent_node.identifier}.stages_cycles'
        self._pub_sub_manager.subscribe(self, self._stages_cycles_topic)
        self._rems_det_param_topic = f'{self._parent_node.identifier}.rems_det_param'
        self._pub_sub_manager.subscribe(self, self._rems_det_param_topic)
        self._report_constants_topic = f'{self._parent_node.identifier}.report_constants'
        self._pub_sub_manager.subscribe(self, self._report_constants_topic)
        self._cohort_filename_topic = f'{self._parent_node.identifier}.cohort_filename'
        self._pub_sub_manager.subscribe(self, self._cohort_filename_topic)
        self._export_rems_topic = f'{self._parent_node.identifier}.export_rems'
        self._pub_sub_manager.subscribe(self, self._export_rems_topic)
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._recording_path_topic, 'ping')
        self._pub_sub_manager.publish(self, self._subject_info_topic, 'ping')
        self._pub_sub_manager.publish(self, self._signals_topic, 'ping')
        self._pub_sub_manager.publish(self, self._rems_events_details_topic, 'ping')
        self._pub_sub_manager.publish(self, self._artifact_events_topic, 'ping')
        self._pub_sub_manager.publish(self, self._sleep_cycle_param_topic, 'ping')
        self._pub_sub_manager.publish(self, self._stages_cycles_topic, 'ping')
        self._pub_sub_manager.publish(self, self._rems_det_param_topic, 'ping')
        self._pub_sub_manager.publish(self, self._report_constants_topic, 'ping')
        self._pub_sub_manager.publish(self, self._cohort_filename_topic, 'ping')
        self._pub_sub_manager.publish(self, self._export_rems_topic, 'ping')
        


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to REMsDetails
        self._pub_sub_manager.publish(self, self._recording_path_topic, str(self.recording_path_lineedit.text()))
        self._pub_sub_manager.publish(self, self._subject_info_topic, str(self.subject_info_lineedit.text()))
        self._pub_sub_manager.publish(self, self._signals_topic, str(self.signals_lineedit.text()))
        self._pub_sub_manager.publish(self, self._rems_events_details_topic, str(self.rems_events_details_lineedit.text()))
        self._pub_sub_manager.publish(self, self._artifact_events_topic, str(self.artifact_events_lineedit.text()))
        self._pub_sub_manager.publish(self, self._sleep_cycle_param_topic, str(self.sleep_cycle_param_lineedit.text()))
        self._pub_sub_manager.publish(self, self._stages_cycles_topic, str(self.stages_cycles_lineedit.text()))
        self._pub_sub_manager.publish(self, self._rems_det_param_topic, str(self.rems_det_param_lineedit.text()))
        self._pub_sub_manager.publish(self, self._report_constants_topic, str(self.report_constants_lineedit.text()))
        self._pub_sub_manager.publish(self, self._cohort_filename_topic, str(self.cohort_filename_lineedit.text()))
        self._pub_sub_manager.publish(self, self._export_rems_topic, str(self.export_rems_lineedit.text()))
        


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
        if topic == self._signals_topic:
            self.signals_lineedit.setText(message)
        if topic == self._rems_events_details_topic:
            self.rems_events_details_lineedit.setText(message)
        if topic == self._artifact_events_topic:
            self.artifact_events_lineedit.setText(message)
        if topic == self._sleep_cycle_param_topic:
            self.sleep_cycle_param_lineedit.setText(message)
        if topic == self._stages_cycles_topic:
            self.stages_cycles_lineedit.setText(message)
        if topic == self._rems_det_param_topic:
            self.rems_det_param_lineedit.setText(message)
        if topic == self._report_constants_topic:
            self.report_constants_lineedit.setText(message)
        if topic == self._cohort_filename_topic:
            self.cohort_filename_lineedit.setText(message)
        if topic == self._export_rems_topic:
            self.export_rems_lineedit.setText(message)
        


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._recording_path_topic)
            self._pub_sub_manager.unsubscribe(self, self._subject_info_topic)
            self._pub_sub_manager.unsubscribe(self, self._signals_topic)
            self._pub_sub_manager.unsubscribe(self, self._rems_events_details_topic)
            self._pub_sub_manager.unsubscribe(self, self._artifact_events_topic)
            self._pub_sub_manager.unsubscribe(self, self._sleep_cycle_param_topic)
            self._pub_sub_manager.unsubscribe(self, self._stages_cycles_topic)
            self._pub_sub_manager.unsubscribe(self, self._rems_det_param_topic)
            self._pub_sub_manager.unsubscribe(self, self._report_constants_topic)
            self._pub_sub_manager.unsubscribe(self, self._cohort_filename_topic)
            self._pub_sub_manager.unsubscribe(self, self._export_rems_topic)
            
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the muscular detection (artefact rejection)
"""

from qtpy import QtWidgets
from qtpy import QtCore
from qtpy.QtGui import QRegularExpressionValidator # To validate waht the user enters in the interface
from qtpy.QtCore import QRegularExpression # To validate waht the user enters in the interface

from CEAMSTools.DetectArtifacts.MuscularStep.Ui_MuscularStep import Ui_MuscularStep
from CEAMSTools.DetectArtifacts.DetectorsStep.DetectorsStep import DetectorsStep
from commons.BaseStepView import BaseStepView

class MuscularStep( BaseStepView,  Ui_MuscularStep, QtWidgets.QWidget):
    """
        MuscularStep links the Settings Views of the step-by-step interface 
        to the SpectralDetector plugin and all the other plugins instanciated 
        in the process of this preset.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Node identifier taken from resources/presets/ArtefactDetection_PowerLine/ArtefactDetection_PowerLine.json
        self._node_id_SpectralDetEEG = "060cb108-2c37-4fc9-9e89-83b777133d01"
        self._node_id_SpectralDetEMG = "a64a02ed-d17b-493d-8175-2c85c48731d9"
        self._node_id_SpectralDetBoth = "77e5dad4-f76e-46a0-bf68-6f0d3c677318"
        self._node_id_EventCombineEMG = "7086f99a-7774-468d-ae49-a707a60ae645"

        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node

        # Events group for the Events Combine plugin for EMG+EEG
        self._group_both_topic = f'{self._node_id_EventCombineEMG}.new_event_group'
        self._pub_sub_manager.subscribe(self, self._group_both_topic)
        # Event name for the Events Combine plugin for EMG+EEG
        self._name_both_topic = f'{self._node_id_EventCombineEMG}.new_event_name'
        self._pub_sub_manager.subscribe(self, self._name_both_topic)

        # Event group for the SpectralDetector plugin for EEG alone
        self._group_EEG_topic = f'{self._node_id_SpectralDetEEG}.event_group'
        self._pub_sub_manager.subscribe(self, self._group_EEG_topic)        
        # Event name for the SpectralDetector plugin for EEG alone
        self._name_EEG_topic = f'{self._node_id_SpectralDetEEG}.event_name'
        self._pub_sub_manager.subscribe(self, self._name_EEG_topic)

        # Thresholds
        self._threshold_EEG_topic = f'{self._node_id_SpectralDetEEG}.threshold_val'
        self._pub_sub_manager.subscribe(self, self._threshold_EEG_topic)
        self._threshold_EMG_topic = f'{self._node_id_SpectralDetEMG}.threshold_val'
        self._pub_sub_manager.subscribe(self, self._threshold_EMG_topic)
        self._threshold_both_topic = f'{self._node_id_SpectralDetBoth}.threshold_val'
        self._pub_sub_manager.subscribe(self, self._threshold_both_topic)

        #self.picture_label.scaled(self.picture_label.size(), QtCore.Qt.KeepAspectRatio)
        # Subscribe to the context
        self._pub_sub_manager.subscribe(self, self._context_manager.topic)  


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._group_EEG_topic, 'ping')
        self._pub_sub_manager.publish(self, self._group_both_topic, 'ping')
        self._pub_sub_manager.publish(self, self._name_EEG_topic, 'ping')
        self._pub_sub_manager.publish(self, self._name_both_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_EEG_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_EMG_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_both_topic, 'ping')


    # Called when the user clicks on "Apply"
    # Settings defined in the viewer are sent to the pub_sub_manager
    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._group_EEG_topic, \
            str(self.group_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._group_both_topic, \
            str(self.group_lineEdit.text()))

        self._pub_sub_manager.publish(self, self._name_EEG_topic, \
            str(self.name_eeg_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._name_both_topic, \
            str(self.name_emg_lineEdit.text()))

        self._pub_sub_manager.publish(self, self._threshold_EEG_topic, \
            str(self.EEG_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._threshold_EMG_topic, \
            str(self.EMG_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._threshold_both_topic, \
            str(self.both_lineEdit.text()))


    # Called when a value listened is changed
    # No body asked for the value (no ping), but the value changed and
    # some subscribed to the topic
    def on_topic_update(self, topic, message, sender):
        if topic==self._context_manager.topic:
            if message==DetectorsStep.context_common_group: # key of the context dict
                # Common group
                if len(self._context_manager[DetectorsStep.context_common_group])>0:
                    self.group_lineEdit.setEnabled(True)
                    self.group_lineEdit.setText(self._context_manager[DetectorsStep.context_common_group])
                    self.group_lineEdit.setEnabled(False)
                else: # Specific -> make it editable
                    self.group_lineEdit.setEnabled(True)
            if message==DetectorsStep.context_common_name: # key of the context dict
                # Common name
                if len(self._context_manager[DetectorsStep.context_common_name])>0:
                    self.name_eeg_lineEdit.setEnabled(True)
                    self.name_eeg_lineEdit.setText(self._context_manager[DetectorsStep.context_common_name])
                    self.name_eeg_lineEdit.setEnabled(False)
                    self.name_emg_lineEdit.setEnabled(True)
                    self.name_emg_lineEdit.setText(self._context_manager[DetectorsStep.context_common_name])
                    self.name_emg_lineEdit.setEnabled(False)
                else: # Specific -> make it editable
                    self.name_eeg_lineEdit.setEnabled(True)
                    self.name_emg_lineEdit.setEnabled(True)


    # To init 
    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    def on_topic_response(self, topic, message, sender):
        if topic == self._group_EEG_topic:
            self.group_lineEdit.setText(message)   
        if topic == self._name_EEG_topic:
            self.name_eeg_lineEdit.setText(message)     
        if topic == self._name_both_topic:
            self.name_emg_lineEdit.setText(message)                   
        if topic == self._threshold_EEG_topic:
            self.EEG_lineEdit.setText(message)       
        if topic == self._threshold_EMG_topic:
            self.EMG_lineEdit.setText(message)       
        if topic == self._threshold_both_topic:
            self.both_lineEdit.setText(message)       


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._group_EEG_topic)
            self._pub_sub_manager.unsubscribe(self, self._group_both_topic)

            self._pub_sub_manager.unsubscribe(self, self._name_EEG_topic)
            self._pub_sub_manager.unsubscribe(self, self._name_both_topic)

            self._pub_sub_manager.unsubscribe(self, self._threshold_EEG_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_EMG_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_both_topic)
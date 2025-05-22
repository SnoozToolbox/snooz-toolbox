"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the Power line contamination (artefact rejection preset)
"""

from qtpy import QtWidgets
from qtpy import QtCore
from qtpy.QtGui import QRegularExpressionValidator # To validate waht the user enters in the interface
from qtpy.QtCore import QRegularExpression # To validate waht the user enters in the interface

from CEAMSTools.DetectArtifacts.PowerLineStep.Ui_PowerLineStep import Ui_PowerLineStep
from CEAMSTools.DetectArtifacts.DetectorsStep.DetectorsStep import DetectorsStep
from commons.BaseStepView import BaseStepView

class PowerLineStep( BaseStepView,  Ui_PowerLineStep, QtWidgets.QWidget):
    """
        PowerLineStep links the Settings Views of the step-by-step interface 
        to the SpectralDetector plugin and all the other plugins instanciated 
        in the process of this preset.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Node identifier taken from resources/presets/ArtefactDetection_PowerLine/ArtefactDetection_PowerLine.json
        self._node_id_SpectralDet_rel = "eb5f8c18-de1e-4bef-a747-2888c774c878" # valid
        self._node_id_SpectralDet_abs = "ff04ef89-738b-46be-a8d4-0a5f2fd3aa31" # valid
        self._node_id_EventCombine = "4e80b8d8-9152-4b8b-b0e7-58e2ca385ac2"

        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node

        # Events group for the Events Combine plugin for EMG+EEG
        self._new_group_topic = f'{self._node_id_EventCombine}.new_event_group'
        self._pub_sub_manager.subscribe(self, self._new_group_topic)
        # Event name for the Events Combine plugin for EMG+EEG
        self._new_name_topic = f'{self._node_id_EventCombine}.new_event_name'
        self._pub_sub_manager.subscribe(self, self._new_name_topic)

        # Thresholds
        self._threshold_rel_topic = f'{self._node_id_SpectralDet_rel}.threshold_val'
        self._pub_sub_manager.subscribe(self, self._threshold_rel_topic)
        self._threshold_abs_topic = f'{self._node_id_SpectralDet_abs}.threshold_val'
        self._pub_sub_manager.subscribe(self, self._threshold_abs_topic)

        # Subscribe to the context
        self._pub_sub_manager.subscribe(self, self._context_manager.topic)          


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._new_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._new_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_rel_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_abs_topic, 'ping')


    # Called when the user clicks on "Apply"
    # Settings defined in the viewer are sent to the pub_sub_manager
    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._new_group_topic, \
            str(self.group_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._new_name_topic, \
            str(self.name_rel_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._threshold_rel_topic, \
            str(self.thresh_rel_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._threshold_abs_topic, \
            str(self.tresh_abs_lineEdit.text()))


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
                    self.name_rel_lineEdit.setEnabled(True)
                    self.name_rel_lineEdit.setText(self._context_manager[DetectorsStep.context_common_name])
                    self.name_rel_lineEdit.setEnabled(False)
                else: # Specific -> make it editable
                    self.name_rel_lineEdit.setEnabled(True)


    # To init 
    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    def on_topic_response(self, topic, message, sender):
        if topic == self._new_group_topic:
            self.group_lineEdit.setText(message)   
        if topic == self._new_name_topic:
            self.name_rel_lineEdit.setText(message)                       
        if topic == self._threshold_rel_topic:
            self.thresh_rel_lineEdit.setText(message)       
        if topic == self._threshold_abs_topic:
            self.tresh_abs_lineEdit.setText(message)       


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._new_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._new_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_rel_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_abs_topic)
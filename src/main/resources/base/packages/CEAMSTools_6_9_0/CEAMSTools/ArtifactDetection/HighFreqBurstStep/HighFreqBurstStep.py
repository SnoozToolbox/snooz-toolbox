"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the Intro plugin
"""

from qtpy import QtWidgets
from qtpy import QtCore
from qtpy.QtGui import QRegExpValidator # To validate waht the user enters in the interface
from qtpy.QtCore import QRegExp # To validate waht the user enters in the interface

from CEAMSTools.ArtifactDetection.HighFreqBurstStep.Ui_HighFreqBurstStep import Ui_HighFreqBurstStep
from CEAMSTools.ArtifactDetection.DetectorsStep.DetectorsStep import DetectorsStep
from commons.BaseStepView import BaseStepView

class HighFreqBurstStep( BaseStepView,  Ui_HighFreqBurstStep, QtWidgets.QWidget):
    """
        HighFreqPowerStep links the Settings Views of the step-by-step interface 
        to the SpectralDetector plugin and all the other plugins instanciated 
        in the process of this preset.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Node identifier taken from resources/presets/ArtefactDetection_PowerLine/ArtefactDetection.json
        self._node_id_SpectralDet_ratio = "28ae29a0-a8bb-4c74-b8de-ede9f8a80a73"
        self._node_id_SpectralDet_rel = "55ca6e02-e2b3-469e-b5f9-a878d1b3ec2c"
        self._node_id_SpectralDet_abs = "787ab295-8f3b-4a76-91b6-4d0303261d73"
        self._node_id_EventCombine = "7ce07ce2-8bf7-4f06-90e7-8ae711a95b17"

        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node

        # Events group for the Events Combine plugin for EMG+EEG
        self._group_both_topic = f'{self._node_id_EventCombine}.new_event_group'
        self._pub_sub_manager.subscribe(self, self._group_both_topic)
        # Event name for the Events Combine plugin for EMG+EEG
        self._name_both_topic = f'{self._node_id_EventCombine}.new_event_name'
        self._pub_sub_manager.subscribe(self, self._name_both_topic)

        # Thresholds
        self._threshold_ratio_topic = f'{self._node_id_SpectralDet_ratio}.threshold_val'
        self._pub_sub_manager.subscribe(self, self._threshold_ratio_topic)
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
        self._pub_sub_manager.publish(self, self._group_both_topic, 'ping')
        self._pub_sub_manager.publish(self, self._name_both_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_ratio_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_rel_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_abs_topic, 'ping')


    # Called when the user clicks on "Apply"
    # Settings defined in the viewer are sent to the pub_sub_manager
    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._group_both_topic, \
            str(self.group_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._name_both_topic, \
            str(self.name_burst_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._threshold_ratio_topic, \
            str(self.thresh_ratio_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._threshold_rel_topic, \
            str(self.thresh_adp_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._threshold_abs_topic, \
            str(self.tresh_fixe_lineEdit.text()))

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
                    self.name_burst_lineEdit.setEnabled(True)
                    self.name_burst_lineEdit.setText(self._context_manager[DetectorsStep.context_common_name])
                    self.name_burst_lineEdit.setEnabled(False)
                else: # Specific -> make it editable
                    self.name_burst_lineEdit.setEnabled(True)


    # To init 
    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    def on_topic_response(self, topic, message, sender):
        if topic == self._group_both_topic:
            self.group_lineEdit.setText(message)             
        if topic == self._name_both_topic:
            self.name_burst_lineEdit.setText(message)                   
        if topic == self._threshold_abs_topic:
            self.tresh_fixe_lineEdit.setText(message)       
        if topic == self._threshold_rel_topic:
            self.thresh_adp_lineEdit.setText(message)         
        if topic == self._threshold_ratio_topic:
            self.thresh_ratio_lineEdit.setText(message)      


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._group_both_topic)
            self._pub_sub_manager.unsubscribe(self, self._name_both_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_rel_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_abs_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_ratio_topic)
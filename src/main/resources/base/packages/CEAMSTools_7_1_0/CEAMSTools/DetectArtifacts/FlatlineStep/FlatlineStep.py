"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the Intro plugin
"""

from qtpy import QtWidgets
from qtpy import QtCore
from qtpy.QtGui import QRegularExpressionValidator # To validate waht the user enters in the interface
from qtpy.QtCore import QRegularExpression # To validate waht the user enters in the interface

from CEAMSTools.DetectArtifacts.FlatlineStep.Ui_FlatlineStep import Ui_FlatlineStep
from CEAMSTools.DetectArtifacts.DetectorsStep.DetectorsStep import DetectorsStep
from commons.BaseStepView import BaseStepView

class FlatlineStep( BaseStepView,  Ui_FlatlineStep, QtWidgets.QWidget):
    """
        FlatlineStep links the Settings Views of the step-by-step interface 
        to the SpectralDetector plugin and all the other plugins instanciated 
        in the process of this preset.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Node identifier taken from resources/presets/ArtefactDetection_PowerLine/ArtefactDetection_PowerLine.json
        self._node_id_SpectralDet = "bb852d74-45b5-4bd3-9e8b-73ae5ef93f7f"
        self._node_id_resetSignal = "08d5b1a6-1549-4ac3-9b2f-c84840a632d2"

        # init UI
        self.setupUi(self)
        # Subscribe to the proper topics to send/get data from the node

        # Events group 
        self._group_topic = f'{self._node_id_SpectralDet}.event_group'
        self._pub_sub_manager.subscribe(self, self._group_topic)
        self._group_reset_topic = f'{self._node_id_resetSignal}.artefact_group'
        self._pub_sub_manager.subscribe(self, self._group_reset_topic)
        # Event name 
        self._name_topic = f'{self._node_id_SpectralDet}.event_name'
        self._pub_sub_manager.subscribe(self, self._name_topic)
        self._name_reset_topic = f'{self._node_id_resetSignal}.artefact_name'
        self._pub_sub_manager.subscribe(self, self._name_reset_topic)
        # Thresholds
        self._threshold_topic = f'{self._node_id_SpectralDet}.threshold_val'
        self._pub_sub_manager.subscribe(self, self._threshold_topic)

        # Subscribe to the context
        self._pub_sub_manager.subscribe(self, self._context_manager.topic)  


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._threshold_topic, 'ping')


    # Called when the user clicks on "Apply"
    # Settings defined in the viewer are sent to the pub_sub_manager
    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._group_topic, \
            str(self.group_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._name_topic, \
            str(self.name_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._group_reset_topic, \
            str(self.group_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._name_reset_topic, \
            str(self.name_lineEdit.text()))            
        self._pub_sub_manager.publish(self, self._threshold_topic, \
            str(self.threshold_lineEdit.text()))


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
                    self.name_lineEdit.setEnabled(True)
                    self.name_lineEdit.setText(self._context_manager[DetectorsStep.context_common_name])
                    self.name_lineEdit.setEnabled(False)
                else: # Specific -> make it editable
                    self.name_lineEdit.setEnabled(True)


    # To init 
    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    def on_topic_response(self, topic, message, sender):
        if topic == self._group_topic:
            self.group_lineEdit.setText(message) 
            if self._context_manager[DetectorsStep.context_common_group]=='':
                self.group_lineEdit.setEnabled(True)
            else:
                self.group_lineEdit.setEnabled(False)
        if topic == self._name_topic:
            self.name_lineEdit.setText(message)    
            if self._context_manager[DetectorsStep.context_common_name]=='':
                self.name_lineEdit.setEnabled(True)
            else:
                self.name_lineEdit.setEnabled(False)                     
        if topic == self._threshold_topic:
            self.threshold_lineEdit.setText(message)   
 

    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._group_topic)
            self._pub_sub_manager.unsubscribe(self, self._name_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_topic)
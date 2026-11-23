"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the baseline variation detector (artefact rejection)
"""

from qtpy import QtWidgets
from qtpy import QtCore
from qtpy.QtGui import QRegularExpressionValidator, QPixmap
from qtpy.QtCore import QRegularExpression
import base64

from CEAMSTools.DetectArtifacts.BslVarStep.Ui_BslVarStep import Ui_BslVarStep
from CEAMSTools.DetectArtifacts.DetectorsStep.DetectorsStep import DetectorsStep
from CEAMSTools.DetectArtifacts.SleepStageSelStep.SleepStageSelStep import SleepStageSelStep
from commons.BaseStepView import BaseStepView

class BslVarStep( BaseStepView,  Ui_BslVarStep, QtWidgets.QWidget):
    """
        BslVarStep links the Settings Views of the step-by-step interface 
        to the SpectralDetector plugin and all the other plugins instanciated 
        in the process of this preset.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Node identifier taken from resources/presets/DetectArtifacts_PowerLine/DetectArtifacts_PowerLine.json
        self._node_id_SpectralDet = "ea6060df-a4da-4ec1-a75c-399ece7a3c1b"

        # init UI
        self.setupUi(self)
        self._load_embedded_image()
        
        # Subscribe to the proper topics to send/get data from the node

        # Events group 
        self._group_topic = f'{self._node_id_SpectralDet}.event_group'
        self._pub_sub_manager.subscribe(self, self._group_topic)
        # Event name 
        self._name_topic = f'{self._node_id_SpectralDet}.event_name'
        self._pub_sub_manager.subscribe(self, self._name_topic)
        # Thresholds
        self._threshold_topic = f'{self._node_id_SpectralDet}.threshold_val'
        self._pub_sub_manager.subscribe(self, self._threshold_topic)

        # Subscribe to the context
        self._pub_sub_manager.subscribe(self, self._context_manager.topic)

        # Default value for the threshold [set 1 (precise-NREM), set 2 (sensitive-REM)]
        self.threshold_value = [4, 2.5] # STD of the main gaussian from 3 components

    def _load_embedded_image(self):
        """Load the embedded base64 image data into label_7."""
        from .art_image_data import BSL_VAR_IMAGE_BASE64
        
        image_bytes = base64.b64decode(BSL_VAR_IMAGE_BASE64)
        pixmap = QPixmap()
        pixmap.loadFromData(image_bytes)
        self.label_7.setPixmap(pixmap)

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
            if message==SleepStageSelStep.context_threshold_set: # key of the context dict
                self.threshold_context_changed()


    def threshold_context_changed(self):
        threshold_set = int(self._context_manager[SleepStageSelStep.context_threshold_set])
        self.threshold_lineEdit.setText(str(self.threshold_value[threshold_set-1]))


    # To init 
    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    def on_topic_response(self, topic, message, sender):
        if topic == self._group_topic:
            self.group_lineEdit.setText(message)   
        if topic == self._name_topic:
            self.name_lineEdit.setText(message)             
        if topic == self._threshold_topic:
            self.threshold_lineEdit.setText(message)       
 

    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._group_topic)
            self._pub_sub_manager.unsubscribe(self, self._name_topic)
            self._pub_sub_manager.unsubscribe(self, self._threshold_topic)
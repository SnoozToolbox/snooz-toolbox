#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite 2024
See the file LICENCE for full license details.

    OutputFiles
    Read the UI to send messages to the node of the slow wave pics generator plugin.
    Rezd a saved pipeline tp update the UI.
"""
import base64
from qtpy.QtGui import QPixmap
from qtpy import QtWidgets

from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog

from CEAMSTools.SlowWaveImages.SlowWaveAlignment.Ui_SlowWaveAlignment import Ui_SlowWaveAlignment

class SlowWaveAlignment(BaseStepView, Ui_SlowWaveAlignment, QtWidgets.QWidget):
    """
        OutputFiles
        Read the UI to send messages to the node of the slow wave pics generator plugin.
        Rezd a saved pipeline tp update the UI.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        self._load_embedded_image()

        self._sw_wave_pics_node = "34950575-1519-44e1-852d-a7720eead65f" # identifier for slow wave pics generator
        # Subscribe to the proper topics to send/get data from the node
        self._alignment_param_topic = f'{self._sw_wave_pics_node}.alignment_param'
        self._pub_sub_manager.subscribe(self, self._alignment_param_topic)

        # Dict to group all the parameters ofthe pics generation
        self.alignment_param = 'ZC'

    def _load_embedded_image(self):
        """Load the embedded base64 image data into label_7."""
        from .sw_alignment_data import SW_SIGNAL_CURVE_IMAGE_BASE64
        
        image_bytes = base64.b64decode(SW_SIGNAL_CURVE_IMAGE_BASE64)
        pixmap = QPixmap()
        pixmap.loadFromData(image_bytes)
        self.label_7.setPixmap(pixmap)

    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._alignment_param_topic, 'ping')
        # The ping will define all the settings in the self.alignment_param string
        if len(self.alignment_param) > 0:
            self.init_ui_from_alignment_param()


    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        # if topic == self._context_manager.topic:
        #     # The message will be the KEY of the value that's been updated inside the context.
        #     # If it's the one you are looking for, we can then take the updated value and use it.
        #     if message == "context_some_other_step":
        #         updated_value = self._context_manager["context_some_other_step"]
        pass
    

    def on_topic_response(self, topic, message, sender):
        # This will be called as a response to ping request.
        if topic == self._alignment_param_topic:
            if isinstance(message, str) and not (message == ''):
                self.alignment_param = message


    def on_apply_settings(self):
        # Init the dictionary to store the output options
        self.out_options_slot()
        self._pub_sub_manager.publish(self, self._alignment_param_topic, self.alignment_param)


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        return True

        
    # Slot to setup the output parameter dictionary to send to the plugin.
    # The slot is called when the user changes a UI option
    # The slot update the self.alignment_param dict based on the user input (from UI)
    def out_options_slot(self):
        # SW Aligment option
        if self.radioButton_zc.isChecked():
            self.alignment_param = "ZC"
        elif self.radioButton_np.isChecked():
            self.alignment_param = "NP"
        elif self.radioButton_pp.isChecked():
            self.alignment_param = "PP"


    # Function to set the UI according to the settings self.alignment_param loaded
    def init_ui_from_alignment_param(self):
        if self.alignment_param == "ZC":
            self.radioButton_zc.setChecked(True)
        elif self.alignment_param == "NP":
            self.radioButton_np.setChecked(True)
        elif self.alignment_param == "PP":
            self.radioButton_pp.setChecked(True)        


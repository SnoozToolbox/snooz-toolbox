#! /usr/bin/env python3
"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL 2024
See the file LICENCE for full license details.

    SlowWaveCharacteristics
    This step is used to choose the folder where the slow wave characterstics files are saved
    and send the information to the sw pics generator plugin. 
"""

from qtpy import QtWidgets
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog
from CEAMSTools.SlowWaveImages.SlowWaveCharacteristics.Ui_SlowWaveCharacteristics import Ui_SlowWaveCharacteristics

class SlowWaveCharacteristics(BaseStepView, Ui_SlowWaveCharacteristics, QtWidgets.QWidget):
    """
        SlowWaveCharacteristics
        This step is used to choose the folder where the slow wave characterstics files are saved
        and send the information to the sw pics generator plugin. 
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # You need to look into your process.json file to know the ID of the node
        # you are interest in, this is just an example value:
        identifier = "34950575-1519-44e1-852d-a7720eead65f" 
        self._sw_char_topic = identifier + ".sw_char_folder"
        

    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._sw_char_topic, 'ping')
    

    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        pass

    def on_topic_response(self, topic, message, sender):
        # This will be called as a response to ping request.
        if topic == self._sw_char_topic:
           self.lineEdit.setText(message)


    def on_apply_settings(self):
        # Send the dictionary as an input to the PSGReader module
        self._pub_sub_manager.publish(self, self._sw_char_topic, str(self.lineEdit.text()))


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.

        # Verify that the folder has been defined
        # Verify that the lineEdit has been filled
        if len(self.lineEdit.text())==0:
            WarningDialog(f"The folder to load the slow wave characteristics files has not been defined on the step '3-SW Characteristics'.")
            return False
        return True


    # Called when the user clicks on the button "choose"
    def choose_slot(self):
        # Open a file dialog to choose the folder
        folder = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select the folder to load the slow wave characteristics files."))
        if folder != '':
            self.lineEdit.setText(folder)
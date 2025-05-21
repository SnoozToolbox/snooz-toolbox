#! /usr/bin/env python3
"""
    AlgorithmDetail
    Description of the algorithm used to detect REMs.
"""

from qtpy import QtWidgets, QtCore
from qtpy.QtCore import QTimer
from PySide6.QtCore import *

from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState


from CEAMSTools.DetectREMsYASA.AlgorithmDetail.Ui_AlgorithmDetail import Ui_AlgorithmDetail

from qtpy import QtWidgets

class AlgorithmDetail(BaseStepView, Ui_AlgorithmDetail, QtWidgets.QWidget):
    """
        AlgorithmDetail
        Description of the algorithm used to detect REMs.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)


    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        pass
        

    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.

            # The message will be the KEY of the value that's been updated inside the context.
            # If it's the one you are looking for, we can then take the updated value and use it.
            #if message == "context_some_other_step":
                #updated_value = self._context_manager["context_some_other_step"]
        pass


    def on_topic_response(self, topic, message, sender):
        # This will be called as a response to ping request.
        pass
        
                
    

    def on_apply_settings(self):
        # Slot called when the user wants to apply the settings
        pass
        
    # Slot called when the user wants to write the filename
    def on_choose(self):
        pass

    def on_active_validation(self):
        pass

    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        
        return True

    # Called when the user delete an instance of the plugin
    def __del__(self):
        pass

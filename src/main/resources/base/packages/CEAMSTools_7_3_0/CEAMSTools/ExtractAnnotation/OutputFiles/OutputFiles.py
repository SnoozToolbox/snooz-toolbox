#! /usr/bin/env python3
"""
    OutputFiles
    TODO CLASS DESCRIPTION
"""

from qtpy import QtWidgets

from CEAMSTools.ExtractAnnotation.OutputFiles.Ui_OutputFiles import Ui_OutputFiles
from commons.BaseStepView import BaseStepView

class OutputFiles(BaseStepView, Ui_OutputFiles, QtWidgets.QWidget):
    """
        OutputFiles
        TODO CLASS DESCRIPTION
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # If necessary, init the context. The context is a memory space shared by 
        # all steps of a tool. It is used to share and notice other steps whenever
        # the value in it changes. It's very useful when the parameter within a step
        # must have an impact in another step.
        #self._context_manager["context_OutputFiles"] = {"the_data_I_want_to_share":"some_data"}

        # description.json file to know the ID of the node
        node_id_writer = "2103d165-8cfa-4db1-8e6a-1fbc0b1a972d" 
        self._time_elapsed_topic = node_id_writer + ".time_elapsed"
        node_id_string = "aeec670e-3e4d-41b1-97ee-09db11fbe37c" 
        self._suffix_topic = node_id_string + ".suffix"

        
    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._time_elapsed_topic, 'ping')
        self._pub_sub_manager.publish(self, self._suffix_topic, 'ping')


    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        #if topic == self._context_manager.topic:

            # The message will be the KEY of the value that's been updated inside the context.
            # If it's the one you are looking for, we can then take the updated value and use it.
            #if message == "context_some_other_step":
                #updated_value = self._context_manager["context_some_other_step"]
        pass


    def on_topic_response(self, topic, message, sender):
        # This will be called as a response to ping request.
        if topic == self._time_elapsed_topic:
           self.checkBox_time.setChecked(bool(message))
        if topic == self._suffix_topic:
           self.lineEdit_suffix.setText(str(message))        


    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._time_elapsed_topic, self.checkBox_time.isChecked())
        if not '.tsv' in self.lineEdit_suffix.text():
            self.lineEdit_suffix.setText(self.lineEdit_suffix.text()+'.tsv')
        self._pub_sub_manager.publish(self, self._suffix_topic, self.lineEdit_suffix.text())


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        return True

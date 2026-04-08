#! /usr/bin/env python3
"""
    OutputFiles
    Class to provide the report filname to the oxygen detector plugin.
"""

from qtpy import QtWidgets

from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState
from widgets.WarningDialog import WarningDialog

from CEAMSTools.OxygenSaturationReport.OutputFiles.Ui_OutputFiles import Ui_OutputFiles

class OutputFiles(BaseStepView, Ui_OutputFiles, QtWidgets.QWidget):
    """
        OutputFiles
        Class to provide the report filname to the oxygen detector plugin.
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

        self._node_id_oxy_det = "88a51ed5-da37-457f-8e32-221b0a600195"
        self._cohort_filename_topic = f'{self._node_id_oxy_det}.cohort_filename'
        self._pub_sub_manager.subscribe(self, self._cohort_filename_topic)
        self._oxy_picture_dir_topic = f'{self._node_id_oxy_det}.picture_dir'
        self._pub_sub_manager.subscribe(self, self._oxy_picture_dir_topic)
        self._node_id_PSGWriter = "b432f441-e705-432b-a772-6be62bb4216a"


    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.

        # You need to look into your process.json file to know the ID of the node
        # you are interest in
        self._pub_sub_manager.publish(self, self._cohort_filename_topic, 'ping')
        self._pub_sub_manager.publish(self, self._oxy_picture_dir_topic, 'ping')
        # Activation state
        self._pub_sub_manager.publish(self, self._node_id_PSGWriter+".get_activation_state", None)
        

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
        if topic == self._cohort_filename_topic:
           self.lineEdit_filename.setText(message)
        if topic == self._oxy_picture_dir_topic:
           self.lineEdit_picturename.setText(message)
        if topic == self._node_id_PSGWriter+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.checkBox_writeEvts.setChecked(True)
            elif message == ActivationState.BYPASS:
                self.checkBox_writeEvts.setChecked(False)


    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._cohort_filename_topic, self.lineEdit_filename.text()) 
        self._pub_sub_manager.publish(self, self._oxy_picture_dir_topic, self.lineEdit_picturename.text()) 
        if self.checkBox_writeEvts.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_PSGWriter\
                +".activation_state_change", ActivationState.ACTIVATED)
        else:
            self._pub_sub_manager.publish(self, self._node_id_PSGWriter\
                +".activation_state_change", ActivationState.BYPASS)
            

    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if len(self.lineEdit_filename.text())==0:
            WarningDialog(f"You need to define the output file report in step '4 - Output Files'.")
            return False
        return True


    # Called when the user click on the browse push button
    def browse_slot(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save as TSV file', 
            None, 
            'TSV (*.tsv)',\
            options = QtWidgets.QFileDialog.DontConfirmOverwrite)
        if filename != '':
            self.lineEdit_filename.setText(filename)


    # Called when the user click on the browse push button
    def browse_pic_slot(self):
        file = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select output directory"))
        if file != '':
            self.lineEdit_picturename.setText(file)


    # Called when the user check/unchecked write event checkbox
    def write_checkbox_slot(self):
        pass

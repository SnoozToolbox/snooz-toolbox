#! /usr/bin/env python3
"""
    Outputfiles
    Define the PSA ouput file settings
"""
from CEAMSTools.PowerSpectralAnalysis.Outputfiles.Ui_Outputfiles import Ui_Outputfiles
from CEAMSTools.PowerSpectralAnalysis.SelectionStep.SelectionStep import SelectionStep
from flowpipe.ActivationState import ActivationState
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog

from qtpy import QtWidgets

class Outputfiles(BaseStepView, Ui_Outputfiles, QtWidgets.QWidget):
    """
        Outputfiles
        Define the PSA ouput file settings
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        self._node_id_PSA_std = "4bb8c9ac-64e8-4cec-9c2c-5a00c80b4eae" # provide the output filename to the PSA Compilation
        self._node_id_PSA_Annot = "9dfbe6b9-1887-452a-ac3b-33f1235f9b0a" # provide the output filename to the PSA Compilation
        # TODO : add the R&A compilation (another instance of PSA Compilation but plugged to the R&A computation)
        # self._node_id_PSA_ra =         

        self._dist_total_topic = f'{self._node_id_PSA_std}.dist_total'
        self._pub_sub_manager.subscribe(self, self._dist_total_topic)
        self._dist_hour_topic = f'{self._node_id_PSA_std}.dist_hour'
        self._pub_sub_manager.subscribe(self, self._dist_hour_topic)
        self._dist_cycle_topic = f'{self._node_id_PSA_std}.dist_cycle'
        self._pub_sub_manager.subscribe(self, self._dist_cycle_topic)
        self._filename_topic = f'{self._node_id_PSA_std}.filename'
        self._pub_sub_manager.subscribe(self, self._filename_topic)
        self._filename_annot_topic = f'{self._node_id_PSA_Annot}.PSA_out_filename'
        self._pub_sub_manager.subscribe(self, self._filename_annot_topic)


    # To update the Settings Views
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._dist_total_topic, 'ping')
        self._pub_sub_manager.publish(self, self._dist_hour_topic, 'ping')
        self._pub_sub_manager.publish(self, self._dist_cycle_topic, 'ping')
        self._pub_sub_manager.publish(self, self._filename_topic, 'ping')
        
        self._pub_sub_manager.publish(self, self._node_id_PSA_Annot+".get_activation_state", None)


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if len(self.filename_lineEdit.text())==0:
            WarningDialog(f"The output file has to be defined by the user, see step '7-Output Files'.")
            return False
        
        # Verify if at least one checkbox is checked when the raddio button self.radioButton_stage is checked
        if self.radioButton_stage.isChecked():
            if not self.total_checkBox.isChecked() and not self.hour_checkBox.isChecked() and not self.cycle_checkBox.isChecked():
                WarningDialog(f"At least one output variable type must be selected, see step '7-Output Files'.")
                return False
        return True   


    # To save the settings in the pipeline json file
    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._dist_total_topic, int(self.total_checkBox.isChecked()))
        self._pub_sub_manager.publish(self, self._dist_hour_topic, int(self.hour_checkBox.isChecked()))
        self._pub_sub_manager.publish(self, self._dist_cycle_topic, int(self.cycle_checkBox.isChecked()))
        self._pub_sub_manager.publish(self, self._filename_topic, self.filename_lineEdit.text())
        self._pub_sub_manager.publish(self, self._filename_annot_topic, self.filename_lineEdit.text())

 
    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    # To update the Settings Views
    def on_topic_response(self, topic, message, sender):
        if topic == self._dist_total_topic:
            self.total_checkBox.setChecked(int(message))
        if topic == self._dist_hour_topic:
            self.hour_checkBox.setChecked(int(message))
        if topic == self._dist_cycle_topic:
            self.cycle_checkBox.setChecked(int(message))        
        if topic == self._filename_topic:
            self.filename_lineEdit.setText(message)  
        if topic == self._node_id_PSA_Annot+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self._enable_annot_widget(True)
            else:
                self._enable_annot_widget(False)


    def on_topic_update(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            at any update, does not necessary answer to a ping.
            To listen to any modification not only when you ask (ping)
        """
        if topic==self._context_manager.topic:
            # PSA section selection changed
            if message==SelectionStep.context_PSA_annot_selection: # key of the context dict
                annot_flag = True if self._context_manager[SelectionStep.context_PSA_annot_selection]==1 else False
                self._enable_annot_widget(annot_flag)


    # Called when the user press on the Choose button
    def choose_button_slot(self):
        # Turn off the overwrite warning when selecting an existing file
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(\
            self, 'Save file as', "", "TSV (*.tsv)",\
            options = QtWidgets.QFileDialog.DontConfirmOverwrite)
        if filename is not None and filename:
            if not filename.endswith(".tsv"):
                filename = filename + ".tsv"
            self.filename_lineEdit.setText(filename) 
        else:
            return


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._dist_total_topic)
            self._pub_sub_manager.unsubscribe(self, self._dist_hour_topic)
            self._pub_sub_manager.unsubscribe(self, self._dist_cycle_topic)
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)
            self._pub_sub_manager.unsubscribe(self, self._filename_annot_topic)


    # To enable/disable the PSA on annotations widget
    def _enable_annot_widget(self, annot_label):
        self.total_checkBox.setEnabled(not annot_label)
        self.hour_checkBox.setEnabled(not annot_label)
        self.cycle_checkBox.setEnabled(not annot_label)
        self.textEdit_tot.setEnabled(not annot_label)
        self.textEdit_hour.setEnabled(not annot_label)
        self.textEdit_cycle.setEnabled(not annot_label)

        self.radioButton_annot.setEnabled(True)
        self.radioButton_annot.setChecked(annot_label)
        self.radioButton_annot.setEnabled(annot_label) #We don't want the user to be able to change it here.

        self.radioButton_stage.setEnabled(True)
        self.radioButton_stage.setChecked(not annot_label)
        self.radioButton_stage.setEnabled(not annot_label) #We don't want the user to be able to change it here.

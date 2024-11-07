#! /usr/bin/env python3
"""
    SSWDSaveFiles
    Settings viewer of the save files plugin for the Slow Wave Detector tool
"""
from CEAMSTools.SlowWaveDetection.SSWDSaveFiles.Ui_SSWDSaveFiles import Ui_SSWDSaveFiles
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState
from widgets.WarningDialog import WarningDialog

from qtpy import QtWidgets

class SSWDSaveFiles( BaseStepView,  Ui_SSWDSaveFiles, QtWidgets.QWidget):
    """
        SSWDSaveFiles
        Displays the next steps for the selection of the files.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        self._node_id_SWDetails = "0308c274-4216-4642-9093-0ac919e9a0de"
        self._export_SW_topic = f'{self._node_id_SWDetails}.export_slow_wave'
        self._pub_sub_manager.subscribe(self, self._export_SW_topic)
        self._cohort_file_topic = f'{self._node_id_SWDetails}.cohort_filename'
        self._pub_sub_manager.subscribe(self, self._cohort_file_topic)

    
    def choose_slot(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        #file_dialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        folder_name = file_dialog.getExistingDirectory()

        if folder_name != '':
            self.foldername_lineEdit.setText(folder_name + "/")


    # Called when the user check/uncheck the checkbox to export sw char by event level
    def check_export_sw_file_slot(self):
        pass

    
    # Called when the user press the browse button to define where to save the cohort report
    def browse_cohort_slot(self):
        # define the option to disable the warning dialog when overwriting an existing file
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save as TSV file', 
            None, 
            'TSV (*.tsv)',
            options = QtWidgets.QFileDialog.DontConfirmOverwrite)
        if filename != '':
            self.lineEdit_cohort_report.setText(filename)


    # Called when the user check/uncheck the checkbox to export the cohort report
    def check_save_cohort_slot(self):
        self.lineEdit_cohort_report.setEnabled(self.checkBox_save_cohort.isChecked())
        self.pushButto_browse.setEnabled(self.checkBox_save_cohort.isChecked())


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        self._pub_sub_manager.publish(self, self._export_SW_topic, 'ping')
        self._pub_sub_manager.publish(self, self._cohort_file_topic, 'ping')


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if self.checkBox_save_cohort.isChecked():
            if len(self.lineEdit_cohort_report.text())==0:
                WarningDialog("Define a file to write the detailed events report for the cohort. In step '4-Output Files'")
                return False
        return True


    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self._export_SW_topic, \
            str(self.checkBox_export_sw.isChecked()))
        self._pub_sub_manager.publish(self, self._cohort_file_topic, \
            self.lineEdit_cohort_report.text())
        if self.checkBox_save_cohort.isChecked() or self.checkBox_export_sw.isChecked():
            self._pub_sub_manager.publish(self, self._node_id_SWDetails \
                + ".activation_state_change", ActivationState.ACTIVATED)
        else:
            self._pub_sub_manager.publish(self, self._node_id_SWDetails \
                + ".activation_state_change", ActivationState.DEACTIVATED)            
        

    # Called by the publisher to display settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if topic == self._export_SW_topic:
            self.checkBox_export_sw.setChecked(eval(message))
        if topic == self._cohort_file_topic:
            self.lineEdit_cohort_report.setText(message)
            self.checkBox_save_cohort.setChecked(len(message)>0)
            self.check_save_cohort_slot()


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._export_SW_topic)
            self._pub_sub_manager.unsubscribe(self, self._cohort_file_topic)

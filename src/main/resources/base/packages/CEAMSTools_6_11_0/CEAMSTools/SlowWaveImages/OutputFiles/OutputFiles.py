#! /usr/bin/env python3
"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL 2024
See the file LICENCE for full license details.

    OutputFiles
    Read the UI to send messages to the node of the slow wave pics generator plugin.
    Rezd a saved pipeline tp update the UI.
"""

from qtpy import QtWidgets

from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog

from CEAMSTools.SlowWaveImages.OutputFiles.Ui_OutputFiles import Ui_OutputFiles

class OutputFiles(BaseStepView, Ui_OutputFiles, QtWidgets.QWidget):
    """
        OutputFiles
        Read the UI to send messages to the node of the slow wave pics generator plugin.
        Rezd a saved pipeline tp update the UI.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        self._sw_wave_pics_node = "34950575-1519-44e1-852d-a7720eead65f" # identifier for slow wave pics generator
        # Subscribe to the proper topics to send/get data from the node
        self._pics_param_topic = f'{self._sw_wave_pics_node}.pics_param'
        self._pub_sub_manager.subscribe(self, self._pics_param_topic)

        # Dict to group all the parameters of the pics generation
        self.pics_param = {
            'cohort_avg': True,
            'cohort_sel': False,
            'subject_avg': False,
            'subject_sel': False,
            'show_sw_categories': False,
            'sw_aligment' : 'ZC',
            'display': "mean_std", # all, mean, mean_std
            'neg_up': False,
            'force_axis': False, # False or [xmin, xmax, ymin, ymax]
            'output_folder': ''
        }

    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._pics_param_topic, 'ping')
        # The ping will define all the settings in the self.pics_param dict
        if len(self.pics_param) > 0:
            self.init_ui_from_pics_param()


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
        if topic == self._pics_param_topic:
            if isinstance(message, str) and not (message == ''):
                self.pics_param = eval(message)
            elif isinstance(message, dict):
                self.pics_param = message
            else:
                self.pics_param = {}


    def on_apply_settings(self):
        # Init the dictionary to store the output options
        self.out_options_slot()
        self._pub_sub_manager.publish(self, self._pics_param_topic, self.pics_param)


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.

        # Verify that at least one checkbox is checked
        if not (self.checkBox_cohort_avg.isChecked() or self.checkBox_cohort_sel.isChecked() or\
                self.checkBox_subject_avg.isChecked() or self.checkBox_subject_sel.isChecked()):
            # Open the warning dialog
            WarningDialog(f"Make sure to select at the least one output in the step '6-Output Files'.")
            return False

        # Make sure that the output folder is set
        if self.lineEdit_output.text() == "":
            WarningDialog("Make sure to set the output folder in the step '6-Output Files'.")
            return False

        return True


    def choose_slot(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)

        if file_dialog.exec():
            folders = file_dialog.selectedFiles()
            if folders:
                self.lineEdit_output.setText(folders[0])
                self.pics_param["output_folder"] = folders[0]
            else:
                self.lineEdit_output.setText("")
            
        
    # Slot to setup the output parameter dictionary to send to the plugin.
    # The slot is called when the user changes a UI option
    # The slot update the self.pics_param dict based on the user input (from UI)
    def out_options_slot(self):

        # SW Aligment option
        if self.radioButton_zc.isChecked():
            self.pics_param["sw_aligment"] = "ZC"
        elif self.radioButton_np.isChecked():
            self.pics_param["sw_aligment"] = "NP"
        elif self.radioButton_pp.isChecked():
            self.pics_param["sw_aligment"] = "PP"

        # Display option
        if self.radioButton_mean.isChecked():
            self.pics_param["display"] = "mean"
            self.checkBox_subject_sel.setChecked(False)
            self.checkBox_subject_sel.setEnabled(False)
            self.checkBox_subject_avg.setEnabled(True)
        elif self.radioButton_all.isChecked():
            self.pics_param["display"] = "all"
            self.checkBox_subject_sel.setEnabled(True)
            self.checkBox_subject_avg.setChecked(False)
            self.checkBox_subject_avg.setEnabled(False)
        elif self.radioButton_meanstd.isChecked():
            self.pics_param["display"] = "mean_std"
            self.checkBox_subject_sel.setChecked(False)
            self.checkBox_subject_sel.setEnabled(False)
            self.checkBox_subject_avg.setEnabled(True)
        
        self.pics_param["neg_up"] = self.checkBox_inverse.isChecked()

        if self.checkBox_force_axis.isChecked():
            self.doubleSpinBox_xmin.setEnabled(True)
            self.doubleSpinBox_xmax.setEnabled(True)
            self.doubleSpinBox_ymin.setEnabled(True)
            self.doubleSpinBox_ymax.setEnabled(True)
            self.pics_param["force_axis"] = [\
                self.doubleSpinBox_xmin.value(), self.doubleSpinBox_xmax.value(), \
                self.doubleSpinBox_ymin.value(), self.doubleSpinBox_ymax.value()]
        else:
            self.pics_param["force_axis"] = False
            self.doubleSpinBox_xmin.setEnabled(False)
            self.doubleSpinBox_xmax.setEnabled(False)
            self.doubleSpinBox_ymin.setEnabled(False)
            self.doubleSpinBox_ymax.setEnabled(False)

        self.pics_param["cohort_avg"] = self.checkBox_cohort_avg.isChecked()
        self.pics_param["cohort_sel"] = self.checkBox_cohort_sel.isChecked()
        self.pics_param["subject_avg"] = self.checkBox_subject_avg.isChecked()
        self.pics_param["subject_sel"] = self.checkBox_subject_sel.isChecked()
        self.pics_param["show_sw_categories"] = self.checkBox_category.isChecked()

        self.pics_param["output_folder"] = self.lineEdit_output.text()


    # Function to set the UI according to the settings self.pics_param loaded
    def init_ui_from_pics_param(self):
        self.checkBox_cohort_avg.setChecked(self.pics_param["cohort_avg"])
        self.checkBox_cohort_sel.setChecked(self.pics_param["cohort_sel"])
        self.checkBox_subject_avg.setChecked(self.pics_param["subject_avg"])
        self.checkBox_subject_sel.setChecked(self.pics_param["subject_sel"])

        self.checkBox_category.setChecked(self.pics_param["show_sw_categories"])

        if self.pics_param["sw_aligment"] == "ZC":
            self.radioButton_zc.setChecked(True)
        elif self.pics_param["sw_aligment"] == "NP":
            self.radioButton_np.setChecked(True)
        elif self.pics_param["sw_aligment"] == "PP":
            self.radioButton_pp.setChecked(True)        

        if self.pics_param["display"]=="mean":
            self.radioButton_mean.setChecked(True)
        elif self.pics_param["display"] == "all":
            self.radioButton_all.setChecked(True)
        elif self.pics_param["display"] == "mean_std":
            self.radioButton_meanstd.setChecked(True)

        self.checkBox_inverse.setChecked(self.pics_param["neg_up"])
        
        if not self.pics_param["force_axis"]:
            self.checkBox_force_axis.setChecked(False)
            self.doubleSpinBox_xmin.setEnabled(False)
            self.doubleSpinBox_xmax.setEnabled(False)
            self.doubleSpinBox_ymin.setEnabled(False)
            self.doubleSpinBox_ymax.setEnabled(False)
        else:
            self.checkBox_force_axis.setChecked(True)
            self.doubleSpinBox_xmin.setEnabled(True)
            self.doubleSpinBox_xmax.setEnabled(True)
            self.doubleSpinBox_ymin.setEnabled(True)
            self.doubleSpinBox_ymax.setEnabled(True)
            self.doubleSpinBox_xmin.setValue(self.pics_param["force_axis"][0])
            self.doubleSpinBox_xmax.setValue(self.pics_param["force_axis"][1])
            self.doubleSpinBox_ymin.setValue(self.pics_param["force_axis"][2])
            self.doubleSpinBox_ymax.setValue(self.pics_param["force_axis"][3])

        self.lineEdit_output.setText(self.pics_param["output_folder"])
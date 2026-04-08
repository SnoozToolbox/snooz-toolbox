#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite 2025
See the file LICENCE for full license details.

    OutputFiles
    Read the UI to send messages to the node of the PSA images generator plugin.
    Read a saved pipeline to update the UI.
"""
import base64
from qtpy.QtGui import QPixmap

from qtpy import QtWidgets

from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog

from CEAMSTools.PSAImages.OutputFiles.Ui_OutputFiles import Ui_OutputFiles

class OutputFiles(BaseStepView, Ui_OutputFiles, QtWidgets.QWidget):
    """
        OutputFiles
        Read the UI to send messages to the node of the PSA images generator plugin.
        Read a saved pipeline to update the UI.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        self._load_embedded_image()

        # Connect the log scale checkbox to the options slot
        if hasattr(self, 'checkBox_log'):
            self.checkBox_log.clicked.connect(self.out_options_slot)
        
        # Connect force axis checkbox to enable/disable spinboxes
        if hasattr(self, 'checkBox_force_axis'):
            self.checkBox_force_axis.clicked.connect(self.out_options_slot)
        
        # Connect radio buttons to trigger spinbox enabling/disabling
        # Note: The button group already connects to out_options_slot, but we also need update_spinbox_states
        if hasattr(self, 'buttonGroup_section'):
            self.buttonGroup_section.buttonClicked.connect(self.update_spinbox_states)

        # Connect level selection radio buttons to enable/disable layouts
        if hasattr(self, 'radioButton_cohort_level'):
            self.radioButton_cohort_level.clicked.connect(self.update_layout_states)
        if hasattr(self, 'radioButton_report_level'):
            self.radioButton_report_level.clicked.connect(self.update_layout_states)

        self._psa_images_node = "bc3ee945-0abf-46b7-b110-db5e617ea70a" # identifier for PSA images generator
        # Subscribe to the proper topics to send/get data from the node
        self._pics_param_topic = f'{self._psa_images_node}.pics_param'
        self._pub_sub_manager.subscribe(self, self._pics_param_topic)

        # Dict to group all the parameters of the pics generation
        self.pics_param = {
            'cohort_avg': True,
            'cohort_sel': False,
            'subject_avg': False,
            'subject_sel': False,
            'sleep_stage_selection': ['All'],  # Default to All stages
            'activity_var' : 'total',  # Changed from sw_alignment for PSA
            'display': "mean_std", # all, mean, mean_std
            'hour': 1,
            'cycle': 1,
            'log_scale': True,  # Default to logarithmic scale
            'show_legend': True,  # Default to showing legend
            'force_axis': False, # False or [xmin, xmax, ymin, ymax]
            'font': 'Arial',
            'fontsize': 12,
            'figure_width': 8,
            'figure_height': 6,
            'output_folder': ''
        }

    def _load_embedded_image(self):
        """Load the embedded base64 image data into label_7."""
        try:
            from .art_image_data import PSA_SIGNAL_CURVE_IMAGE_BASE64
            
            image_bytes = base64.b64decode(PSA_SIGNAL_CURVE_IMAGE_BASE64)
            pixmap = QPixmap()
            pixmap.loadFromData(image_bytes)
            self.label_7.setPixmap(pixmap)
        except ImportError:
            # If art_image_data doesn't exist yet, skip image loading
            pass

    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._pics_param_topic, 'ping')
        # The ping will define all the settings in the self.pics_param dict
        if len(self.pics_param) > 0:
            self.init_ui_from_pics_param()
        else:
            # If no saved settings, initialize with defaults
            self.init_ui_with_defaults()


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
            WarningDialog(f"Make sure to select at the least one output in the step '3-Output Files'.")
            return False

        # Make sure that the output folder is set
        if self.lineEdit_output.text() == "":
            WarningDialog("Make sure to set the output folder in the step '3-Output Files'.")
            return False

        return True


    def update_spinbox_states(self):
        """Update spinbox enabled/disabled states based on selected radio button"""
        if self.radioButton_total.isChecked():
            self.spinBox_stage_hour.setEnabled(False)
            self.spinBox_clock_hour.setEnabled(False)
            self.spinBox_sleep_cycle.setEnabled(False)
        elif self.radioButton_sleep_cycle.isChecked():
            self.spinBox_stage_hour.setEnabled(False)
            self.spinBox_clock_hour.setEnabled(False)
            self.spinBox_sleep_cycle.setEnabled(True)
        elif self.radioButton_clock_hour.isChecked():
            self.spinBox_stage_hour.setEnabled(False)
            self.spinBox_clock_hour.setEnabled(True)
            self.spinBox_sleep_cycle.setEnabled(False)
        elif self.radioButton_stage_hour.isChecked():
            self.spinBox_stage_hour.setEnabled(True)
            self.spinBox_clock_hour.setEnabled(False)
            self.spinBox_sleep_cycle.setEnabled(False)

    def choose_slot(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.Directory) 
        file_dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)

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

        # PSA Alignment option (adapted for PSA from SW alignment)
        if self.radioButton_total.isChecked():
            self.pics_param["activity_var"] = "total"
        elif self.radioButton_sleep_cycle.isChecked():
            self.pics_param["activity_var"] = "cyc"
        elif self.radioButton_clock_hour.isChecked():
            self.pics_param["activity_var"] = "clock_h"
        elif self.radioButton_stage_hour.isChecked():
            self.pics_param["activity_var"] = "stage_h"

        # Display option
        if self.radioButton_mean.isChecked():
            self.pics_param["display"] = "mean"
        elif self.radioButton_all.isChecked():
            self.pics_param["display"] = "all"
        elif self.radioButton_meanstd.isChecked():
            self.pics_param["display"] = "mean_std"
        
        self.pics_param["log_scale"] = self.checkBox_log.isChecked()
        self.pics_param["show_legend"] = self.checkBox_legend.isChecked()
        self.pics_param["font"] = self.fontComboBox.currentText()
        self.pics_param["fontsize"] = self.spinBox_fontsize.value()
        self.pics_param["figure_width"] = self.spinBox_figwidth.value()
        self.pics_param["figure_height"] = self.spinBox_figheight.value()

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
        
        # Build sleep stage selection list based on checked checkboxes
        sleep_stages = []
        if self.checkBox_Wake.isChecked():
            sleep_stages.append('W')
        if self.checkBox_N1.isChecked():
            sleep_stages.append('N1')
        if self.checkBox_N2.isChecked():
            sleep_stages.append('N2')
        if self.checkBox_N3.isChecked():
            sleep_stages.append('N3')
        if self.checkBox_REM.isChecked():
            sleep_stages.append('R')
        if self.checkBox_Unscored.isChecked():
            sleep_stages.append('Unscored')
        if self.checkBox_All.isChecked():
            sleep_stages.append('All')
        
        # Add special combined labels and remove individual stages
        if self.checkBox_N2.isChecked() and self.checkBox_N3.isChecked():
            sleep_stages.append('N2N3')
            # Remove individual N2 and N3 when N2N3 is present
            sleep_stages = [stage for stage in sleep_stages if stage not in ['N2', 'N3']]
        
        if self.checkBox_N1.isChecked() and self.checkBox_N2.isChecked() and self.checkBox_N3.isChecked():
            sleep_stages.append('NREM')
            # Remove individual N1, N2, N3 when NREM is present
            sleep_stages = [stage for stage in sleep_stages if stage not in ['N1', 'N2', 'N3', 'N2N3']]
        
        self.pics_param["sleep_stage_selection"] = sleep_stages

        self.pics_param["output_folder"] = self.lineEdit_output.text()
        
        if self.radioButton_stage_hour.isChecked():
            self.pics_param["hour"] = self.spinBox_stage_hour.value()
        elif self.radioButton_clock_hour.isChecked():
            self.pics_param["hour"] = self.spinBox_clock_hour.value()
        elif self.radioButton_sleep_cycle.isChecked():
            self.pics_param["cycle"] = self.spinBox_sleep_cycle.value()


        if self.radioButton_total.isChecked():
            self.spinBox_stage_hour.setEnabled(False)
            self.spinBox_clock_hour.setEnabled(False)
            self.spinBox_sleep_cycle.setEnabled(False)
        elif self.radioButton_sleep_cycle.isChecked():
            self.spinBox_stage_hour.setEnabled(False)
            self.spinBox_clock_hour.setEnabled(False)
            self.spinBox_sleep_cycle.setEnabled(True)
        elif self.radioButton_clock_hour.isChecked():
            self.spinBox_stage_hour.setEnabled(False)
            self.spinBox_clock_hour.setEnabled(True)
            self.spinBox_sleep_cycle.setEnabled(False)
        elif self.radioButton_stage_hour.isChecked():
            self.spinBox_stage_hour.setEnabled(True)
            self.spinBox_clock_hour.setEnabled(False)
            self.spinBox_sleep_cycle.setEnabled(False)

    # Function to set the UI according to the settings self.pics_param loaded
    def init_ui_from_pics_param(self):
        self.checkBox_cohort_avg.setChecked(self.pics_param.get("cohort_avg", False))
        self.checkBox_cohort_sel.setChecked(self.pics_param.get("cohort_sel", False))
        self.checkBox_subject_avg.setChecked(self.pics_param.get("subject_avg", False))
        self.checkBox_subject_sel.setChecked(self.pics_param.get("subject_sel", False))
        
        # Set sleep stage checkboxes based on the list
        sleep_stages = self.pics_param.get("sleep_stage_selection", ['All'])
        
        # If no sleep stages are selected or empty list, default to "All"
        if not sleep_stages or sleep_stages == [False] or sleep_stages == False:
            self.checkBox_All.setChecked(True)
            self.checkBox_Wake.setChecked(False)
            self.checkBox_N1.setChecked(False)
            self.checkBox_N2.setChecked(False)
            self.checkBox_N3.setChecked(False)
            self.checkBox_REM.setChecked(False)
            self.checkBox_Unscored.setChecked(False)
        else:
            # Handle combined labels by setting individual checkboxes
            has_n2n3 = 'N2N3' in sleep_stages
            has_nrem = 'NREM' in sleep_stages
            
            self.checkBox_Wake.setChecked('W' in sleep_stages)
            self.checkBox_N1.setChecked('N1' in sleep_stages or has_nrem)
            self.checkBox_N2.setChecked('N2' in sleep_stages or has_n2n3 or has_nrem)
            self.checkBox_N3.setChecked('N3' in sleep_stages or has_n2n3 or has_nrem)
            self.checkBox_REM.setChecked('R' in sleep_stages)
            self.checkBox_Unscored.setChecked('Unscored' in sleep_stages)
            self.checkBox_All.setChecked('All' in sleep_stages)

        if self.pics_param.get("activity_var") == "total":
            self.radioButton_total.setChecked(True)
        elif self.pics_param.get("activity_var") == "cyc":
            self.radioButton_sleep_cycle.setChecked(True)
        elif self.pics_param.get("activity_var") == "clock_h":
            self.radioButton_clock_hour.setChecked(True)
        elif self.pics_param.get("activity_var") == "stage_h":
            self.radioButton_stage_hour.setChecked(True)

        if self.pics_param.get("display")=="mean":
            self.radioButton_mean.setChecked(True)
        elif self.pics_param.get("display") == "all":
            self.radioButton_all.setChecked(True)
        elif self.pics_param.get("display") == "mean_std":
            self.radioButton_meanstd.setChecked(True)

        self.checkBox_log.setChecked(self.pics_param.get("log_scale", True))  # Default to True
        self.checkBox_legend.setChecked(self.pics_param.get("show_legend", True))  # Default to True
        self.fontComboBox.setCurrentText(self.pics_param.get("font", "Arial"))
        self.spinBox_fontsize.setValue(self.pics_param.get("fontsize", 12))
        self.spinBox_figwidth.setValue(self.pics_param.get("figure_width", 8))
        self.spinBox_figheight.setValue(self.pics_param.get("figure_height", 6))
        
        if not self.pics_param.get("force_axis", False):
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
            force_axis = self.pics_param.get("force_axis", [0, 0, 0, 0])
            self.doubleSpinBox_xmin.setValue(force_axis[0])
            self.doubleSpinBox_xmax.setValue(force_axis[1])
            self.doubleSpinBox_ymin.setValue(force_axis[2])
            self.doubleSpinBox_ymax.setValue(force_axis[3])

        self.lineEdit_output.setText(self.pics_param.get("output_folder", ""))

        self.spinBox_stage_hour.setValue(self.pics_param.get("hour", 1))
        self.spinBox_clock_hour.setValue(self.pics_param.get("hour", 1))
        self.spinBox_sleep_cycle.setValue(self.pics_param.get("cycle", 1))
        
        # Set spinbox enabled/disabled states based on activity_var
        activity_var = self.pics_param.get("activity_var", "total")
        if activity_var == "total":
            self.spinBox_stage_hour.setEnabled(False)
            self.spinBox_clock_hour.setEnabled(False)
            self.spinBox_sleep_cycle.setEnabled(False)
        elif activity_var == "cyc":
            self.spinBox_stage_hour.setEnabled(False)
            self.spinBox_clock_hour.setEnabled(False)
            self.spinBox_sleep_cycle.setEnabled(True)
        elif activity_var == "clock_h":
            self.spinBox_stage_hour.setEnabled(False)
            self.spinBox_clock_hour.setEnabled(True)
            self.spinBox_sleep_cycle.setEnabled(False)
        elif activity_var == "stage_h":
            self.spinBox_stage_hour.setEnabled(True)
            self.spinBox_clock_hour.setEnabled(False)
            self.spinBox_sleep_cycle.setEnabled(False)

    def init_ui_with_defaults(self):
        """Initialize UI with default values when no saved settings exist"""
        # Set default checkboxes
        self.checkBox_cohort_avg.setChecked(True)
        self.checkBox_cohort_sel.setChecked(False)
        self.checkBox_subject_avg.setChecked(False)
        self.checkBox_subject_sel.setChecked(False)
        
        # Set default sleep stage to "All"
        self.checkBox_All.setChecked(True)
        self.checkBox_Wake.setChecked(False)
        self.checkBox_N1.setChecked(False)
        self.checkBox_N2.setChecked(False)
        self.checkBox_N3.setChecked(False)
        self.checkBox_REM.setChecked(False)
        self.checkBox_Unscored.setChecked(False)
        
        # Set default radio buttons
        self.radioButton_total.setChecked(True)
        self.radioButton_meanstd.setChecked(True)
        
        # Set default logarithmic scale
        self.checkBox_log.setChecked(True)
        self.checkBox_legend.setChecked(True)
        
        # Set default spinbox values
        self.spinBox_stage_hour.setValue(1)
        self.spinBox_clock_hour.setValue(1)
        self.spinBox_sleep_cycle.setValue(1)
        
        # Set default spinbox states (all disabled since total is selected)
        self.spinBox_stage_hour.setEnabled(False)
        self.spinBox_clock_hour.setEnabled(False)
        self.spinBox_sleep_cycle.setEnabled(False)

        # Initialize layout states
        self.update_layout_states()

    def update_layout_states(self):
        """Enable/disable layouts based on selected level radio button"""
        if hasattr(self, 'radioButton_cohort_level') and hasattr(self, 'radioButton_report_level'):
            if self.radioButton_cohort_level.isChecked():
                # Uncheck subject checkboxes before disabling
                self.checkBox_subject_avg.setChecked(False)
                self.checkBox_subject_sel.setChecked(False)
                # Disable subject layout, enable cohort layout
                self.set_layout_enabled(self.verticalLayout, False)
                self.set_layout_enabled(self.verticalLayout_2, True)
            elif self.radioButton_report_level.isChecked():
                # Uncheck cohort checkboxes before disabling
                self.checkBox_cohort_avg.setChecked(False)
                self.checkBox_cohort_sel.setChecked(False)
                # Enable subject layout, disable cohort layout
                self.set_layout_enabled(self.verticalLayout, True)
                self.set_layout_enabled(self.verticalLayout_2, False)

    def set_layout_enabled(self, layout, enabled):
        """Enable or disable all widgets in a layout"""
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item.widget():
                item.widget().setEnabled(enabled)
            elif item.layout():
                # Recursively handle nested layouts
                self.set_layout_enabled(item.layout(), enabled)

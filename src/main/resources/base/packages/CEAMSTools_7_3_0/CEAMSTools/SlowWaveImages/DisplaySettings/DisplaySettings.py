#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    DisplaySettings
    Class to define the list of colors for the images.
"""

from qtpy import QtWidgets

from CEAMSTools.SlowWaveImages.DisplaySettings.Ui_DisplaySettings import Ui_DisplaySettings
from commons.BaseStepView import BaseStepView

class DisplaySettings(BaseStepView, Ui_DisplaySettings, QtWidgets.QWidget):
    """
        DisplaySettings
        Class to define the list of colors for the images.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        self.colors_parameters = {
            'subject_avg': ['tab:blue', 'tab:red', 'tab:green', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'],
            'subject_sel': ['tab:blue', 'tab:red', 'tab:green', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'],
            'cohort': ['tab:blue', 'tab:red', 'tab:green', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'],
            'subject_avg_flag': False,
            'subject_sel_flag': False,
            'cohort_flag': False
        }

        self._sw_wave_pics_node = "34950575-1519-44e1-852d-a7720eead65f" # identifier for slow wave pics generator
        # Subscribe to the proper topics to send/get data from the node
        self._pics_param_topic = f'{self._sw_wave_pics_node}.colors_param'
        self._pub_sub_manager.subscribe(self, self._pics_param_topic)


        # If necessary, init the context. The context is a memory space shared by 
        # all steps of a tool. It is used to share and notice other steps whenever
        # the value in it changes. It's very useful when the parameter within a step
        # must have an impact in another step.
        #self._context_manager["context_DisplaySettings"] = {"the_data_I_want_to_share":"some_data"}
        

    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._pics_param_topic, 'ping')


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
        if topic == self._pics_param_topic:
            if isinstance(message, str) and not (message == ''):
                message = eval(message)
            if isinstance(message, dict):
                self.colors_parameters = message
                self.init_ui_from_pics_param()


    def on_apply_settings(self):
        # Init the dictionary to store the output options
        self.update_colors_slot()
        self._pub_sub_manager.publish(self, self._pics_param_topic, self.colors_parameters)


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        return True


    # Called when the user changes ant setting in the UI
    def update_colors_slot(self):

        if not self.checkBox_subject_avg_auto.isChecked():
            self.colors_parameters['subject_avg_flag']=True
            self.comboBox_subject_avg_chan1.setEnabled(True)
            self.comboBox_subject_avg_chan2.setEnabled(True)
            self.comboBox_subject_avg_chan3.setEnabled(True)
            self.comboBox_subject_avg_chan4.setEnabled(True)
            # Get the text from the combo box
            subject_avg_channels = [f"tab:{self.comboBox_subject_avg_chan1.currentText()}",\
                f"tab:{self.comboBox_subject_avg_chan2.currentText()}",\
                f"tab:{self.comboBox_subject_avg_chan3.currentText()}",\
                f"tab:{self.comboBox_subject_avg_chan4.currentText()}"]
            # Replace the first 4 elements of the list with the new colors
            self.colors_parameters['subject_avg'][0:4] = subject_avg_channels
        else:
            self.colors_parameters['subject_avg_flag']=False
            self.comboBox_subject_avg_chan1.setEnabled(False)
            self.comboBox_subject_avg_chan2.setEnabled(False)
            self.comboBox_subject_avg_chan3.setEnabled(False)
            self.comboBox_subject_avg_chan4.setEnabled(False)

        if not self.checkBox_subject_sel_auto.isChecked():
            self.colors_parameters['subject_sel_flag']=True
            self.comboBox_subject_sel_cat1.setEnabled(True)
            self.comboBox_subject_sel_cat2.setEnabled(True)
            self.comboBox_subject_sel_cat3.setEnabled(True)
            self.comboBox_subject_sel_cat4.setEnabled(True)
            # Get the text from the combo box
            subject_sel_categories = [f"tab:{self.comboBox_subject_sel_cat1.currentText()}",\
                f"tab:{self.comboBox_subject_sel_cat2.currentText()}",\
                f"tab:{self.comboBox_subject_sel_cat3.currentText()}",\
                f"tab:{self.comboBox_subject_sel_cat4.currentText()}"]
            # Replace the first 4 elements of the list with the new colors
            self.colors_parameters['subject_sel'][0:4] = subject_sel_categories
        else:
            self.colors_parameters['subject_sel_flag']=False
            self.comboBox_subject_sel_cat1.setEnabled(False)
            self.comboBox_subject_sel_cat2.setEnabled(False)
            self.comboBox_subject_sel_cat3.setEnabled(False)
            self.comboBox_subject_sel_cat4.setEnabled(False)

        if not self.checkBox_cohort_auto.isChecked():
            self.colors_parameters['cohort_flag']=True
            self.comboBox_cohort_group1.setEnabled(True)
            self.comboBox_cohort_group2.setEnabled(True)
            self.comboBox_cohort_group3.setEnabled(True)
            self.comboBox_cohort_group4.setEnabled(True)
            # Get the text from the combo box
            cohort_groups = [f"tab:{self.comboBox_cohort_group1.currentText()}",\
                f"tab:{self.comboBox_cohort_group2.currentText()}",\
                f"tab:{self.comboBox_cohort_group3.currentText()}",\
                f"tab:{self.comboBox_cohort_group4.currentText()}"]
            # Replace the first 4 elements of the list with the new colors
            self.colors_parameters['cohort'][0:4] = cohort_groups
        else:
            self.colors_parameters['cohort_flag']=False
            self.comboBox_cohort_group1.setEnabled(False)
            self.comboBox_cohort_group2.setEnabled(False)
            self.comboBox_cohort_group3.setEnabled(False)
            self.comboBox_cohort_group4.setEnabled(False)
        

    # Function to set the UI according to the settings self.pics_param loaded
    def init_ui_from_pics_param(self):  
        self.checkBox_subject_avg_auto.setChecked(not self.colors_parameters['subject_avg_flag'])
        self.checkBox_subject_sel_auto.setChecked(not self.colors_parameters['subject_sel_flag'])
        self.checkBox_cohort_auto.setChecked(not self.colors_parameters['cohort_flag'])
        if self.colors_parameters['subject_avg_flag']:
            self.comboBox_subject_avg_chan1.setEnabled(True)
            self.comboBox_subject_avg_chan1.setCurrentText(self.colors_parameters['subject_avg'][0])
            self.comboBox_subject_avg_chan2.setEnabled(True)
            self.comboBox_subject_avg_chan2.setCurrentText(self.colors_parameters['subject_avg'][1])
            self.comboBox_subject_avg_chan3.setEnabled(True)
            self.comboBox_subject_avg_chan3.setCurrentText(self.colors_parameters['subject_avg'][2])
            self.comboBox_subject_avg_chan4.setEnabled(True)
            self.comboBox_subject_avg_chan4.setCurrentText(self.colors_parameters['subject_avg'][3])
        else:
            self.comboBox_subject_avg_chan1.setEnabled(False)
            self.comboBox_subject_avg_chan2.setEnabled(False)
            self.comboBox_subject_avg_chan3.setEnabled(False)
            self.comboBox_subject_avg_chan4.setEnabled(False)
        if self.colors_parameters['subject_sel_flag']:
            self.comboBox_subject_sel_cat1.setEnabled(True)
            self.comboBox_subject_sel_cat2.setEnabled(True)
            self.comboBox_subject_sel_cat3.setEnabled(True)
            self.comboBox_subject_sel_cat4.setEnabled(True)
            self.comboBox_subject_sel_cat1.setCurrentText(self.colors_parameters['subject_sel'][0])
            self.comboBox_subject_sel_cat2.setCurrentText(self.colors_parameters['subject_sel'][1])
            self.comboBox_subject_sel_cat3.setCurrentText(self.colors_parameters['subject_sel'][2])
            self.comboBox_subject_sel_cat4.setCurrentText(self.colors_parameters['subject_sel'][3])
        else:
            self.comboBox_subject_sel_cat1.setEnabled(False)
            self.comboBox_subject_sel_cat2.setEnabled(False)
            self.comboBox_subject_sel_cat3.setEnabled(False)
            self.comboBox_subject_sel_cat4.setEnabled(False)
        if self.colors_parameters['cohort_flag']:
            self.comboBox_cohort_group1.setEnabled(True)
            self.comboBox_cohort_group2.setEnabled(True)
            self.comboBox_cohort_group3.setEnabled(True)
            self.comboBox_cohort_group4.setEnabled(True)
            self.comboBox_cohort_group1.setCurrentText(self.colors_parameters['cohort'][0])
            self.comboBox_cohort_group2.setCurrentText(self.colors_parameters['cohort'][1])
            self.comboBox_cohort_group3.setCurrentText(self.colors_parameters['cohort'][2])
            self.comboBox_cohort_group4.setCurrentText(self.colors_parameters['cohort'][3])
        else:
            self.comboBox_cohort_group1.setEnabled(False)
            self.comboBox_cohort_group2.setEnabled(False)
            self.comboBox_cohort_group3.setEnabled(False)
            self.comboBox_cohort_group4.setEnabled(False)
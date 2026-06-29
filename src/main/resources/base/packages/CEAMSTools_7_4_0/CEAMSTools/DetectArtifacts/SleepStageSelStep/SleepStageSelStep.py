#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    SleepStageSelStep
    Class to define the Sleep Stage selection step for the artifact detection.
    The detection threholds may vary depending on the sleep stage.
"""

from qtpy import QtWidgets

from CEAMSTools.DetectArtifacts.SleepStageSelStep.Ui_SleepStageSelStep import Ui_SleepStageSelStep
from commons.BaseStepView import BaseStepView

class SleepStageSelStep(BaseStepView, Ui_SleepStageSelStep, QtWidgets.QWidget):
    """
        SleepStageSelStep
        Class to define the Sleep Stage selection step for the artifact detection.
        The detection threholds may vary depending on the sleep stage.
    """

    # The context key to share the set of thresholds chosen by the user
    context_threshold_set = "threshold_set"
    # The context key to share the sleep stages chosen by the user
    context_stages_sel = "stages_sel"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Sleep Stage Events selection
        self.stages_sel = '1,2,3'
        self._node_id_sleep_stages = "d7196198-e2f9-432c-9134-c825e7a19193"
        self._sleep_stage_topic = f'{self._node_id_sleep_stages}.stages'
        self._pub_sub_manager.subscribe(self, self._sleep_stage_topic)
        # The sleep stage selection needs to be sent to the FilterEvents Module
        self._node_id_filter_events ="8b9ceb12-694f-4289-a611-d46e85b57cb5"
        self._filter_events_topic = f'{self._node_id_filter_events}.stages_selection'
        self._pub_sub_manager.subscribe(self, self._filter_events_topic)      

        # Define the default value of the context (set 1 of thresholds)
        self._context_manager[self.context_threshold_set] = "1"  
        # Define the default sleep stages
        self._context_manager[self.context_stages_sel] = "NREM"     


    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._sleep_stage_topic, 'ping')
        self.checkBox_0.setChecked('0' in self.stages_sel)
        self.checkBox_1.setChecked('1' in self.stages_sel)
        self.checkBox_2.setChecked('2' in self.stages_sel)
        self.checkBox_3.setChecked('3' in self.stages_sel)
        self.checkBox_5.setChecked('5' in self.stages_sel)
        self.checkBox_9.setChecked('9' in self.stages_sel)


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
        if topic == self._sleep_stage_topic:
            self.stages_sel = message


    def on_apply_settings(self):
        # Stages
        #self.check_stages_slot()
        self._pub_sub_manager.publish(self, self._sleep_stage_topic, self.stages_sel) 
        self._pub_sub_manager.publish(self, self._filter_events_topic, self.stages_sel) 
        

    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        return True


    def check_stages_slot(self):
        stages_message = []
        if self.checkBox_0.isChecked():
            stages_message.append('0')
        if self.checkBox_1.isChecked():
            stages_message.append('1')
        if self.checkBox_2.isChecked():
            stages_message.append('2')
        if self.checkBox_3.isChecked():
            stages_message.append('3')
        if self.checkBox_5.isChecked():
            stages_message.append('5')
        if self.checkBox_9.isChecked():
            stages_message.append('9')
        self.stages_sel = (','.join(stages_message))
        
        if (self.stages_sel == '1,2,3'):
            stage_names = 'NREM'
        elif (self.stages_sel == '1,2,3,5'):
            stage_names = 'SLEEP'
        elif self.stages_sel == '0,1,2,3,5' or self.stages_sel == '0,1,2,3,5,9':
            stage_names = 'ALL'    
        elif (self.stages_sel == '9'):
            stage_names = 'UNS'    
        else:
            stage_names = ''
            if '1' in self.stages_sel:
                stage_names = stage_names+'N1'
            if '2' in self.stages_sel:   
                stage_names = stage_names+'N2'
            if '3' in self.stages_sel:   
                stage_names = stage_names+'N3'
            if '5' in self.stages_sel:   
                stage_names = stage_names+'REM'
            if '0' in self.stages_sel:   
                stage_names = stage_names+'W'
        
        # Update the context to inform the Detector Settings Step of the new sleep stages
        self._context_manager[self.context_stages_sel] = stage_names


    # Called when the radio button is changed
    # The value is stored in the context
    def radio_threshold_slot(self):
        if self.radioButton_set1.isChecked():
            self._context_manager[self.context_threshold_set] = "1"
        if self.radioButton_set2.isChecked():
            self._context_manager[self.context_threshold_set] = "2"


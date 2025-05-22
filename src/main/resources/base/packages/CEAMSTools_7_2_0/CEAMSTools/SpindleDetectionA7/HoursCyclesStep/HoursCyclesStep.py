#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    HoursCyclesStep
    Class to provide the maximum number of hours and sleep cycle to be used in the report.
"""

from qtpy import QtWidgets

from CEAMSTools.SpindleDetectionA7.HoursCyclesStep.Ui_HoursCyclesStep import Ui_HoursCyclesStep
from commons.BaseStepView import BaseStepView

class HoursCyclesStep(BaseStepView, Ui_HoursCyclesStep, QtWidgets.QWidget):
    """
        HoursCyclesStep
        Class to provide the maximum number of hours and sleep cycle to be used in the report.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        # You need to look into your process.json file to know the ID of the node
        # you are interest in, this is just an example value:
        self._SpindleDetails_id = "0e3df2c0-7c41-4fa5-89bb-f6601ef8831a"
        self._constants_report_topic = self._SpindleDetails_id + ".report_constants" 
        self._SpindleDetails_anal_id = "28929dd9-a992-4e7b-be6b-9e0a6053ae4e"
        self._constants_report_anal_topic = self._SpindleDetails_anal_id + ".report_constants" 
        
        self.report_constants = {}
        self.report_constants['N_HOURS'] = 9
        self.report_constants['N_CYCLES'] = 6


    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._constants_report_topic, 'ping')


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
        if topic == self._constants_report_topic:
            if isinstance(message, str) and not message == "":
                message = eval(message)
            if isinstance(message, dict) and not message == {}:
                self.report_constants = message
            self.spinBox_hours.setValue(self.report_constants['N_HOURS'])
            self.spinBox_cycles.setValue(self.report_constants['N_CYCLES'])


    def on_apply_settings(self):
        self.report_constants['N_HOURS'] = self.spinBox_hours.value()
        self.report_constants['N_CYCLES'] = self.spinBox_cycles.value()
        self._pub_sub_manager.publish(self, self._constants_report_topic, self.report_constants)
        self._pub_sub_manager.publish(self, self._constants_report_anal_topic, self.report_constants)


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        return True

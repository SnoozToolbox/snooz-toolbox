#! /usr/bin/env python3
"""
    DetectionSettings
    Class step to define the parameters of the oxygen desaturation.
    The Settings view is used to buil a dictionary to provide to the 
    oxygen desaturation detector.
"""

from qtpy import QtWidgets

from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog

from CEAMSTools.OxygenSaturationReport.DetectionSettings.Ui_DetectionSettings import Ui_DetectionSettings

class DetectionSettings(BaseStepView, Ui_DetectionSettings, QtWidgets.QWidget):
    """
        DetectionSettings
        Class step to define the parameters of the oxygen desaturation.
        The Settings view is used to buil a dictionary to provide to the 
        oxygen desaturation detector.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # If necessary, init the context. The context is a memory space shared by 
        # all steps of a tool. It is used to share and notice other steps whenever
        # the value in it changes. It's very useful when the parameter within a step
        # must have an impact in another step.
        #self._context_manager["context_DetectionSettings"] = {"the_data_I_want_to_share":"some_data"}
        self.parameters_oxy = {}
        self._node_id_oxy_det = "88a51ed5-da37-457f-8e32-221b0a600195"
        self._oxy_topic = f'{self._node_id_oxy_det}.parameters_oxy'
        self._pub_sub_manager.subscribe(self, self._oxy_topic)
        

    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.

        # You need to look into your process.json file to know the ID of the node
        # you are interest in
        self._pub_sub_manager.publish(self, self._oxy_topic, 'ping')


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
        if topic == self._oxy_topic:
            if isinstance(message, str):
                self.parameters_oxy = eval(message)
                if self.parameters_oxy['desaturation_drop_percent']==3:
                    self.radioButton_3perc.setChecked(True)
                else:
                    self.radioButton_4perc.setChecked(True)
                if self.parameters_oxy['max_slope_drop_sec']==120:
                    self.radioButton_120s.setChecked(True)
                else:
                    self.radioButton_20s.setChecked(True)                
                if self.parameters_oxy['min_hold_drop_sec']==10:
                    self.radioButton_hold_10s.setChecked(True)
                else:
                    self.radioButton_hold_5s.setChecked(True)


    def on_apply_settings(self):
        if self.radioButton_3perc.isChecked():
            self.parameters_oxy['desaturation_drop_percent'] = 3
        elif self.radioButton_4perc.isChecked():
            self.parameters_oxy['desaturation_drop_percent'] = 4
        if self.radioButton_120s.isChecked():
            self.parameters_oxy['max_slope_drop_sec'] = 120
        elif self.radioButton_20s.isChecked():
            self.parameters_oxy['max_slope_drop_sec'] = 20        
        if self.radioButton_hold_10s.isChecked():
            self.parameters_oxy['min_hold_drop_sec'] = 10
        elif self.radioButton_hold_5s.isChecked():
            self.parameters_oxy['min_hold_drop_sec'] = 5     
        self._pub_sub_manager.publish(self, self._oxy_topic, str(self.parameters_oxy)) 


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        return True

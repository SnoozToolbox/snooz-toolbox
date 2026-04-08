#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    FilterStep
    Step to define the filter settings: exclusive selection among standard bands.
"""

from qtpy import QtWidgets

from CEAMSTools.AnalyzeEEGConnectivity.FilterStep.Ui_FilterStep import Ui_FilterStep
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState
from widgets.WarningDialog import WarningDialog


class FilterStep(BaseStepView, Ui_FilterStep, QtWidgets.QWidget):
    """
        FilterStep
        Allows the user to pick exactly one of five standard bands (full, delta, theta, alpha, beta)
        and pushes the corresponding cutoff to the backend nodes, bypassing all others.

    """
    context_Con_annot_selection = "annotation_selection"
    context_Con_sleep_stages = "sleep_stages_selection"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # self.fullband_radioButton.setChecked(True)             # Set Full Band as default checked
        # self.custom_radioButton.setChecked(False)              # Ensure Custom is NOT checked
        self.lowcutoff_doubleSpinBox.setEnabled(False)         # Disable custom spinboxes
        self.highcutoff_doubleSpinBox.setEnabled(False)
        self.low_cutoff_label.setEnabled(False)
        self.high_cutoff_label.setEnabled(False)    
        self.trim_checkBox.setChecked(False)                    # Set Trim as default unchecked  
        self.start_time_doubleSpinBox.setEnabled(False)
        self.duration_time_doubleSpinBox.setEnabled(False)
        self.start_time_label.setEnabled(False)
        self.duration_time_label.setEnabled(False)

        # If necessary, init the context. The context is a memory space shared by 
        # all steps of a tool. It is used to share and notice other steps whenever
        # the value in it changes. It's very useful when the parameter within a step
        # must have an impact in another step.
        #self._context_manager["context_FilterStep"] = {"the_data_I_want_to_share":"some_data"}

        # Node‐IDs for band‐pass filters
        self._node_id_bandpass_filter = "1dbffc28-380f-4ca4-ae73-16cdd6e4b60c"
        self._node_id_SignalsFromEvents = "7b92caa3-9e9e-46bc-b790-6175abb7ae45"  
        self._node_id_trim_signal = "d6266576-d0da-4a9a-adb4-2cc7e01308ef"  

        # self._events_names_topic = f"{self._node_id_SignalsFromEvents}.events_names"   

        self.bypass_node(self._node_id_trim_signal)

        # Input node topic
        self._low_high_cutoff_topic = f'{self._node_id_bandpass_filter}.cutoff'
        self._pub_sub_manager.subscribe(self, self._low_high_cutoff_topic)

        self._trim_start_time_topic = f'{self._node_id_trim_signal}.start_sec'
        self._trim_duration_time_topic = f'{self._node_id_trim_signal}.duration_sec'
        self._pub_sub_manager.subscribe(self, self._trim_start_time_topic)
        self._pub_sub_manager.subscribe(self, self._trim_duration_time_topic)
        
        self.sleep_stages_names = ''
        self.update_section_selection_slot()

        # Connect the radio button to a method that enables/disables the spinboxes
        self.custom_radioButton.toggled.connect(self.on_custom_radio_toggled)
        self.trim_checkBox.toggled.connect(self.on_trim_checkbox_toggled)
        self.unscored_radioButton.toggled.connect(self.on_unscored_toggled)
        self.sleep_stages_radioButton.toggled.connect(self.on_sleep_stages_toggled)
        self.specific_annotations_radioButton.toggled.connect(self.on_specific_annotations_toggled)
        


    def update_section_selection_slot(self):
        self._context_manager[FilterStep.context_Con_annot_selection] = 1 if self.specific_annotations_radioButton.isChecked() else 0
        self._context_manager[FilterStep.context_Con_sleep_stages] = self.sleep_stages_names if self.sleep_stages_radioButton.isChecked() else ''


    def on_unscored_toggled(self, checked: bool):
        if checked:
            self.trim_checkBox.setEnabled(True)
            self.bypass_node(self._node_id_SignalsFromEvents)
        else:
            self.trim_checkBox.setEnabled(False)
            self.trim_checkBox.setChecked(False)
            self.activate_node(self._node_id_SignalsFromEvents)

    def on_sleep_stages_toggled(self, checked: bool):
        if checked:
            self.n1_checkBox.setEnabled(True)
            self.n2_checkBox.setEnabled(True)
            self.n3_checkBox.setEnabled(True)
            self.rem_checkBox.setEnabled(True)
        else:
            self.n1_checkBox.setEnabled(False)
            self.n2_checkBox.setEnabled(False)
            self.n3_checkBox.setEnabled(False)
            self.rem_checkBox.setEnabled(False)


    def on_specific_annotations_toggled(self, checked: bool):
        self.update_section_selection_slot()

    def on_custom_radio_toggled(self, checked):
        # Enable spinboxes only when Custom radio is selected
        self.lowcutoff_doubleSpinBox.setEnabled(checked)
        self.highcutoff_doubleSpinBox.setEnabled(checked)
        self.low_cutoff_label.setEnabled(checked)
        self.high_cutoff_label.setEnabled(checked)


    def activate_node(self, node_id):
        """
        Helper to activate a module/node by its ID.
        """
        self._pub_sub_manager.publish(
            self, f"{node_id}.activation_state_change", ActivationState.ACTIVATED
        )

    def bypass_node(self, node_id):
        """
        Helper to activate a module/node by its ID.
        """
        self._pub_sub_manager.publish(
            self, f"{node_id}.activation_state_change", ActivationState.BYPASS
        )

    def on_trim_checkbox_toggled(self, checked):
        if checked:
            self.activate_node(self._node_id_trim_signal)
            self.start_time_doubleSpinBox.setEnabled(True)
            self.duration_time_doubleSpinBox.setEnabled(True)
            self.start_time_label.setEnabled(True)
            self.duration_time_label.setEnabled(True)
        else:
            self.bypass_node(self._node_id_trim_signal)
            self.start_time_doubleSpinBox.setEnabled(False)
            self.duration_time_doubleSpinBox.setEnabled(False)
            self.start_time_label.setEnabled(False)
            self.duration_time_label.setEnabled(False)

        
    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        self._pub_sub_manager.publish(self, self._low_high_cutoff_topic, 'ping')
        # Activation state
        self._pub_sub_manager.publish(self, self._node_id_bandpass_filter+".get_activation_state", None)

        self._pub_sub_manager.publish(self, self._trim_duration_time_topic, 'ping')
        self._pub_sub_manager.publish(self, self._trim_start_time_topic, 'ping')
        # Activation state
        self._pub_sub_manager.publish(self, self._node_id_bandpass_filter+".get_activation_state", None)
        self._pub_sub_manager.publish(self, self._node_id_trim_signal+".get_activation_state", None)




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
        #if topic == self._somevalue_topic:
        #    self._somevalue = message
        # pass
        """
        Handle replies to our ping for activation state.
        We check the box if the node reports ACTIVATED.
        """
        if topic == self._low_high_cutoff_topic:
            cutoff = message
        #     if cutoff == "0.16 4":
        #         self.delta_radioButton.setChecked(True)
        #     elif cutoff == "4 8":
        #         self.theta_radioButton.setChecked(True)
        #     elif cutoff == "8 13":
        #         self.alpha_radioButton.setChecked(True)
        #     elif cutoff == "13 30":
        #         self.beta_radioButton.setChecked(True)
        #     else:
        #         self.fullband_radioButton.setChecked(True)

            if cutoff == "0.16 4":
                self.delta_radioButton.setChecked(True)
            elif cutoff == "4 8":
                self.theta_radioButton.setChecked(True)
            elif cutoff == "8 13":
                self.alpha_radioButton.setChecked(True)
            elif cutoff == "13 30":
                self.beta_radioButton.setChecked(True)
            elif cutoff == "0.16 30":
                self.fullband_radioButton.setChecked(True)
            else:
                # This block now catches both "0.16 30" (full band) and any other custom band
                self.custom_radioButton.setChecked(True)
            try:
                low, high = map(float, cutoff.split())
                self.lowcutoff_doubleSpinBox.setValue(low)
                self.highcutoff_doubleSpinBox.setValue(high)
            except Exception as e:
                print("Failed to parse custom cutoff:", e)
        
        elif topic == self._trim_start_time_topic:
            if message:
                self.trim_checkBox.setChecked(True)
                start_sec = message
                try:
                    self.start_time_doubleSpinBox.setValue(float(start_sec))
                except Exception as e:
                    print("Failed to set start time:", e)

        elif topic == self._trim_duration_time_topic:
            if message:
                self.trim_checkBox.setChecked(True)
                duration_sec = message
                try:
                    self.duration_time_doubleSpinBox.setValue(float(duration_sec))
                except Exception as e:
                    print("Failed to set duration time:", e)


    def on_validate_settings(self):
        if self.sleep_stages_radioButton.isChecked():
            if not (self.n1_checkBox.isChecked() or self.n2_checkBox.isChecked()
                or self.n3_checkBox.isChecked() or self.rem_checkBox.isChecked()):
                WarningDialog(f"If you have selected <<Sleep Stages>> for the scope of analysis, select at least one sleep stage in step '3 - Filter Settings'.")   
                return False
        return True
    #     # Validate that all input were set correctly by the user.
    #     # If everything is correct, return True.
    #     # If not, display an error message to the user and return False.
    #     # This is called just before the apply settings function.
    #     # Returning False will prevent the process from executing.
    #     if float(self.high_cutoff_lineEdit.text())>(self.min_fs/2):
    #         message = f'The high frequency cutoff ({self.high_cutoff_lineEdit.text()}Hz) '\
    #             + f'of the band pass filter is higher than the Nyquist frequency ({self.min_fs/2}Hz)'\
    #                 + f'\n\nIn step 3- Filter Settings : lower the high frequency cutoff of the band '\
    #                     + f'pass below the Nyquist frequency of {self.min_fs/2}Hz.'
    #         WarningDialog(message) 
    #         return False
    #     return True


    def on_apply_settings(self):
        """
        Publish for filter node:
        """
        if self.delta_radioButton.isChecked():
            cutoff = "0.16 4"
        elif self.theta_radioButton.isChecked():
            cutoff = "4 8"
        elif self.alpha_radioButton.isChecked():
            cutoff = "8 13"
        elif self.beta_radioButton.isChecked():
            cutoff = "13 30"
        elif self.fullband_radioButton.isChecked():
            cutoff = "0.16 30"
        elif self.custom_radioButton.isChecked():
            low = self.lowcutoff_doubleSpinBox.value()
            high = self.highcutoff_doubleSpinBox.value()
            cutoff = f"{low} {high}"
        else:
            # fallback default if nothing selected (rare)
            cutoff = "0.16 30"

        self._pub_sub_manager.publish(self, self._low_high_cutoff_topic, cutoff)
        
        if self.unscored_radioButton.isChecked():
            # Bypass SignalsFromEvents module
            self._pub_sub_manager.publish(
                self,
                self._node_id_SignalsFromEvents + ".activation_state_change",
                ActivationState.BYPASS
            )
        else:
            # Activate SignalsFromEvents module
            self._pub_sub_manager.publish(
                self,
                self._node_id_SignalsFromEvents + ".activation_state_change",
                ActivationState.ACTIVATED
            )

        if self.sleep_stages_radioButton.isChecked():
            self.sleep_stages_names = []
            if self.n1_checkBox.isChecked():
                self.sleep_stages_names.append("1")
            if self.n2_checkBox.isChecked():
                self.sleep_stages_names.append("2")
            if self.n3_checkBox.isChecked():
                self.sleep_stages_names.append("3")
            if self.rem_checkBox.isChecked():
                self.sleep_stages_names.append("5")
            
            self.sleep_stages_names = ','.join(self.sleep_stages_names)
            self.update_section_selection_slot()
            # self._pub_sub_manager.publish(self, self._events_names_topic, events_names)
  
            # if self.specific_annotations_radioButton.isChecked():
                # self._pub_sub_manager.publish(self, self._events_names_topic, events_names)
            
    
        if self.trim_checkBox.isChecked():
            self.activate_node(self._node_id_trim_signal)
            start_sec = self.start_time_doubleSpinBox.value()
            duration_sec = self.duration_time_doubleSpinBox.value()
            self._pub_sub_manager.publish(self, self._trim_start_time_topic, start_sec)
            self._pub_sub_manager.publish(self, self._trim_duration_time_topic, duration_sec)
        else:
            self.bypass_node(self._node_id_trim_signal)

    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._low_high_cutoff_topic)
            self._pub_sub_manager.unsubscribe(self, self._trim_start_time_topic)
            self._pub_sub_manager.unsubscribe(self, self._trim_duration_time_topic)
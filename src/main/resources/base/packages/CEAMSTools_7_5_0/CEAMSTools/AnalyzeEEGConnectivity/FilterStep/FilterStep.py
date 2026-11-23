#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    FilterStep
    Step to define the filter settings: exclusive selection among standard bands.
"""

from qtpy import QtCore, QtWidgets

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
    # Explicit analysis scope shared with the other steps:
    # "sleep_stages" | "specific_annotations" | "unscored"
    context_Con_scope = "connectivity_scope"

    def __init__(self, **kwargs):
        self._settings_loaded = False
        self._activation_states = {}
        self._sleep_stages_received = False
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
        self._node_id_SignalsFromEvents = "7b92caa3-9e9e-46bc-b790-6175abb7ae45"        # annotation branch
        self._node_id_SignalsFromEvents_sleep = "57a3efc2-afb7-45ac-9384-b5ab46d77cab"  # sleep branch
        self._node_id_sleep_stage_events = "3b6e3aba-4c49-4fd9-b41d-0a6a22004957"       # SleepStageEvents
        self._node_id_trim_signal = "d6266576-d0da-4a9a-adb4-2cc7e01308ef"  
 

        # Input node topic
        self._low_high_cutoff_topic = f'{self._node_id_bandpass_filter}.cutoff'
        self._pub_sub_manager.subscribe(self, self._low_high_cutoff_topic)

        self._trim_start_time_topic = f'{self._node_id_trim_signal}.start_sec'
        self._trim_duration_time_topic = f'{self._node_id_trim_signal}.duration_sec'
        self._sleep_stages_topic = f'{self._node_id_sleep_stage_events}.stages'
        self._pub_sub_manager.subscribe(self, self._trim_start_time_topic)
        self._pub_sub_manager.subscribe(self, self._trim_duration_time_topic)
        self._pub_sub_manager.subscribe(self, self._sleep_stages_topic)
        
        self.sleep_stages_names = ''

        # Connect the radio button to a method that enables/disables the spinboxes
        self.custom_radioButton.toggled.connect(self.custom_radio_toggled_slot)
        self.trim_checkBox.toggled.connect(self.trim_checkbox_toggled_slot)
        self.unscored_radioButton.toggled.connect(self.scope_changed_slot)
        self.sleep_stages_radioButton.toggled.connect(self.scope_changed_slot)
        self.specific_annotations_radioButton.toggled.connect(self.scope_changed_slot)
        for checkbox in (self.n1_checkBox, self.n2_checkBox, self.n3_checkBox, self.rem_checkBox):
            checkbox.toggled.connect(self.sleep_stages_changed_slot)

        self._update_scope_widgets()


    def _current_scope(self):
        """Return the currently selected analysis scope."""
        if self.specific_annotations_radioButton.isChecked():
            return "specific_annotations"
        if self.unscored_radioButton.isChecked():
            return "unscored"
        return "sleep_stages"

    def update_section_selection_slot(self):
        if not self._settings_loaded:
            return
        scope = self._current_scope()
        self._context_manager[FilterStep.context_Con_scope] = scope
        self._context_manager[FilterStep.context_Con_annot_selection] = 1 if scope == "specific_annotations" else 0
        self._context_manager[FilterStep.context_Con_sleep_stages] = self.sleep_stages_names if scope == "sleep_stages" else ''

    def _set_scope_nodes(self, scope):
        """
        Activate/deactivate/bypass the SignalsFromEvents (annotation and sleep
        branches) and SleepStageEvents nodes according to the selected scope.
        The connectivity chains (epoch/connectivity/details) are handled by the
        ConnectivitySettings step.
        """
        if not self._settings_loaded:
            return
        if scope == "sleep_stages":
            self.activate_node(self._node_id_sleep_stage_events)
            self.activate_node(self._node_id_SignalsFromEvents_sleep)
            self.deactivate_node(self._node_id_SignalsFromEvents)
        elif scope == "specific_annotations":
            self.deactivate_node(self._node_id_sleep_stage_events)
            self.deactivate_node(self._node_id_SignalsFromEvents_sleep)
            self.activate_node(self._node_id_SignalsFromEvents)
        elif scope == "unscored":
            self.deactivate_node(self._node_id_sleep_stage_events)
            self.deactivate_node(self._node_id_SignalsFromEvents_sleep)
            # Bypass: pass the (trimmed) full signal through without cropping by events.
            self.bypass_node(self._node_id_SignalsFromEvents)


    def _update_scope_widgets(self):
        """Enable scope-specific controls without changing the saved selections or nodes."""
        is_sleep = self._current_scope() == "sleep_stages"
        is_unscored = self._current_scope() == "unscored"
        for checkbox in (self.n1_checkBox, self.n2_checkBox, self.n3_checkBox, self.rem_checkBox):
            checkbox.setEnabled(is_sleep)
        self.trim_checkBox.setEnabled(is_unscored)
        enable_trim = is_unscored and self.trim_checkBox.isChecked()
        self.start_time_doubleSpinBox.setEnabled(enable_trim)
        self.duration_time_doubleSpinBox.setEnabled(enable_trim)
        self.start_time_label.setEnabled(enable_trim)
        self.duration_time_label.setEnabled(enable_trim)

    def scope_changed_slot(self, checked: bool):
        """Route user scope changes; restoration only updates the UI."""
        if not checked or not self._settings_loaded:
            return
        if self._current_scope() != "unscored":
            self.trim_checkBox.setChecked(False)
        self._update_scope_widgets()
        self._set_scope_nodes(self._current_scope())
        self.update_section_selection_slot()

    def _selected_sleep_stages(self):
        return ','.join(
            stage for stage, checkbox in (
                ("1", self.n1_checkBox), ("2", self.n2_checkBox),
                ("3", self.n3_checkBox), ("5", self.rem_checkBox)
            ) if checkbox.isChecked()
        )

    def sleep_stages_changed_slot(self):
        if not self._settings_loaded:
            return
        self.sleep_stages_names = self._selected_sleep_stages()
        self.update_section_selection_slot()

    def custom_radio_toggled_slot(self, checked):
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
        Helper to bypass a module/node by its ID.
        """
        self._pub_sub_manager.publish(
            self, f"{node_id}.activation_state_change", ActivationState.BYPASS
        )

    def deactivate_node(self, node_id):
        """
        Helper to deactivate a module/node by its ID.
        """
        self._pub_sub_manager.publish(
            self, f"{node_id}.activation_state_change", ActivationState.DEACTIVATED
        )

    def trim_checkbox_toggled_slot(self, checked):
        """Update trim controls and route activation only after settings have loaded."""
        self._update_scope_widgets()
        if not self._settings_loaded:
            return
        if checked:
            self.activate_node(self._node_id_trim_signal)
        else:
            self.bypass_node(self._node_id_trim_signal)


    def load_settings(self):
        """Restore scope, stages and trim from the process without changing its nodes."""
        self._settings_loaded = False
        self._sleep_stages_received = False
        self._activation_states = dict.fromkeys((
            f"{self._node_id_sleep_stage_events}.get_activation_state",
            f"{self._node_id_SignalsFromEvents_sleep}.get_activation_state",
            f"{self._node_id_SignalsFromEvents}.get_activation_state",
            f"{self._node_id_trim_signal}.get_activation_state",
        ))
        for topic in self._activation_states:
            self._pub_sub_manager.publish(self, topic, None)

        sleep_state, sleep_signal_state, annotation_state, trim_state = self._activation_states.values()
        scopes_by_states = {
            (ActivationState.ACTIVATED, ActivationState.ACTIVATED, ActivationState.DEACTIVATED):
                self.sleep_stages_radioButton,
            (ActivationState.DEACTIVATED, ActivationState.DEACTIVATED, ActivationState.ACTIVATED):
                self.specific_annotations_radioButton,
            (ActivationState.DEACTIVATED, ActivationState.DEACTIVATED, ActivationState.BYPASS):
                self.unscored_radioButton,
        }
        scope_button = scopes_by_states.get((sleep_state, sleep_signal_state, annotation_state))
        if scope_button is None or trim_state not in (ActivationState.ACTIVATED, ActivationState.BYPASS):
            self._pub_sub_manager.publish(
                self, "show_error_message",
                "Could not restore filter settings: inconsistent or missing scope/trim module states."
            )
            return

        with QtCore.QSignalBlocker(self.sleep_stages_radioButton), \
                QtCore.QSignalBlocker(self.unscored_radioButton), \
                QtCore.QSignalBlocker(self.specific_annotations_radioButton), \
                QtCore.QSignalBlocker(self.trim_checkBox):
            scope_button.setChecked(True)
            self.trim_checkBox.setChecked(trim_state == ActivationState.ACTIVATED)

        self._pub_sub_manager.publish(self, self._low_high_cutoff_topic, 'ping')
        self._pub_sub_manager.publish(self, self._trim_duration_time_topic, 'ping')
        self._pub_sub_manager.publish(self, self._trim_start_time_topic, 'ping')
        self._pub_sub_manager.publish(self, self._sleep_stages_topic, 'ping')
        if not self._sleep_stages_received:
            self._pub_sub_manager.publish(
                self, "show_error_message",
                "Could not restore filter settings: expected a comma-separated sleep stage list."
            )
            return
        self._update_scope_widgets()
        self._settings_loaded = True
        self.update_section_selection_slot()




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
        if topic in self._activation_states:
            self._activation_states[topic] = message
        elif topic == self._sleep_stages_topic:
            if not isinstance(message, str):
                return
            self._sleep_stages_received = True
            self.sleep_stages_names = message
            stages = {stage.strip() for stage in message.split(',')}
            for stage, checkbox in (
                ("1", self.n1_checkBox), ("2", self.n2_checkBox),
                ("3", self.n3_checkBox), ("5", self.rem_checkBox)
            ):
                with QtCore.QSignalBlocker(checkbox):
                    checkbox.setChecked(stage in stages)
        elif topic == self._low_high_cutoff_topic:
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
            if message not in (None, ''):
                start_sec = message
                try:
                    self.start_time_doubleSpinBox.setValue(float(start_sec))
                except Exception as e:
                    print("Failed to set start time:", e)

        elif topic == self._trim_duration_time_topic:
            if message not in (None, ''):
                duration_sec = message
                try:
                    self.duration_time_doubleSpinBox.setValue(float(duration_sec))
                except Exception as e:
                    print("Failed to set duration time:", e)


    def on_validate_settings(self):
        if not self._settings_loaded:
            self._pub_sub_manager.publish(
                self, "show_error_message",
                "Filter settings could not be restored. Please check the scope/trim modules in the process."
            )
            return False
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
        # Also called when the workspace is saved (without validation): keep the
        # saved process untouched if it could not be restored.
        if not self._settings_loaded:
            return
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

        scope = self._current_scope()
        # Activate/deactivate/bypass the SignalsFromEvents + SleepStageEvents nodes
        # according to the selected analysis scope.
        self._set_scope_nodes(scope)

        if scope == "sleep_stages":
            self.sleep_stages_names = self._selected_sleep_stages()
            # Push the selected sleep stages to the SleepStageEvents node so that
            # only those stages are turned into events for the sleep branch.
            self._pub_sub_manager.publish(
                self, f"{self._node_id_sleep_stage_events}.stages", self.sleep_stages_names)
        else:
            self.sleep_stages_names = ''

        self.update_section_selection_slot()

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
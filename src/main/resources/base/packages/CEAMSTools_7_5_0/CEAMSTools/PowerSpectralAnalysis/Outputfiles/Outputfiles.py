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
        # The PSA output does not support Total unchecked
        self.total_checkBox.setChecked(True)
        self.total_checkBox.setEnabled(False)

        # Define modules and nodes to talk to
        self._node_id_PSA_std = "4bb8c9ac-64e8-4cec-9c2c-5a00c80b4eae" # provide the output filename to the PSA Compilation
        self._node_id_PSA_Annot = "bd2ef4ac-7b23-4494-8c5b-22f188fd1f87" # provide the output filename to the PSA Compilation
        self._node_id_rhythmic_IRASA = "d16022c4-3ac0-4982-aa3e-dfff4cada99a"
        self._node_id_Arhythmic_IRASA = "0ddf2d8d-943d-4583-8b2d-6184ad208119"
        self._node_id_PSA_FOOOF = "05044aa2-4a45-44ae-a5a8-b6182ecf8ec2"
        self._node_id_constant_total = "6d0d60d8-a16f-4b24-b04e-95883536f52d"
        self._node_id_constant_hour = "83e327c4-36fe-4231-9e6a-9b7ef04e6fc8"
        self._node_id_constant_cycle = "f2103119-88d0-4edb-958c-6243a7d0674f"

        self._filename_topic = f'{self._node_id_PSA_std}.filename'
        self._pub_sub_manager.subscribe(self, self._filename_topic)
        self._filename_annot_topic = f'{self._node_id_PSA_Annot}.PSA_out_filename'
        self._pub_sub_manager.subscribe(self, self._filename_annot_topic)

        self._filename_rhythmic_topic = f'{self._node_id_rhythmic_IRASA}.filename'
        self._pub_sub_manager.subscribe(self, self._filename_rhythmic_topic)

        self._filename_arhythmic_topic = f'{self._node_id_Arhythmic_IRASA}.filename'
        self._pub_sub_manager.subscribe(self, self._filename_arhythmic_topic)

        self._filename_fooof_topic = f'{self._node_id_PSA_FOOOF}.filename'
        self._pub_sub_manager.subscribe(self, self._filename_fooof_topic)

        self._selected_filename_topic = None
        self._output_activation_states = {}

        self._dist_total_constant_topic = f'{self._node_id_constant_total}.constant'
        self._pub_sub_manager.subscribe(self, self._dist_total_constant_topic)
        self._dist_hour_constant_topic = f'{self._node_id_constant_hour}.constant'
        self._pub_sub_manager.subscribe(self, self._dist_hour_constant_topic)
        self._dist_cycle_constant_topic = f'{self._node_id_constant_cycle}.constant'
        self._pub_sub_manager.subscribe(self, self._dist_cycle_constant_topic)

    # To update the Settings Views
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView

        self._selected_filename_topic = None
        output_topics = {
            f'{self._node_id_PSA_std}.get_activation_state': self._filename_topic,
            f'{self._node_id_PSA_Annot}.get_activation_state': self._filename_annot_topic,
            f'{self._node_id_rhythmic_IRASA}.get_activation_state': self._filename_rhythmic_topic,
            f'{self._node_id_PSA_FOOOF}.get_activation_state': self._filename_fooof_topic,
        }
        self._output_activation_states = dict.fromkeys(output_topics)
        # Activation-state responses are synchronous.
        for topic in output_topics:
            self._pub_sub_manager.publish(self, topic, None)

        active_topics = [
            output_topics[topic]
            for topic, state in self._output_activation_states.items()
            if state == ActivationState.ACTIVATED
        ]
        if None in self._output_activation_states.values() or len(active_topics) != 1:
            self.filename_lineEdit.clear()
            WarningDialog(
                "Unable to load the output filename. Exactly one output analysis "
                "(Welch, annotations, IRASA or FOOOF) must be active, "
                "and all output module states must be available."
            )
        else:
            self._selected_filename_topic = active_topics[0]
            self._pub_sub_manager.publish(self, self._selected_filename_topic, 'ping')
        self._pub_sub_manager.publish(self, self._dist_total_constant_topic, 'ping')
        self._pub_sub_manager.publish(self, self._dist_hour_constant_topic, 'ping')
        self._pub_sub_manager.publish(self, self._dist_cycle_constant_topic, 'ping')

    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if len(self.filename_lineEdit.text())==0:
            WarningDialog(f"The output file has to be defined by the user, see step '7-Output Files'.")
            return False
        
        return True   


    # To save the settings in the pipeline json file
    def on_apply_settings(self):

        self._pub_sub_manager.publish(self, self._filename_topic, self.filename_lineEdit.text())
        self._pub_sub_manager.publish(self, self._filename_annot_topic, self.filename_lineEdit.text())
        self._pub_sub_manager.publish(self, self._filename_rhythmic_topic, self.filename_lineEdit.text()[:-4] + "_periodic.tsv")
        self._pub_sub_manager.publish(self, self._filename_arhythmic_topic, self.filename_lineEdit.text()[:-4] + "_aperiodic.tsv")
        self._pub_sub_manager.publish(self, self._filename_fooof_topic, self.filename_lineEdit.text())
        # Filenames with flags are published when psd data arrives (see on_topic_response)
        self._pub_sub_manager.publish(self, self._dist_total_constant_topic, int(self.total_checkBox.isChecked()))
        self._pub_sub_manager.publish(self, self._dist_hour_constant_topic, int(self.hour_checkBox.isChecked()))
        self._pub_sub_manager.publish(self, self._dist_cycle_constant_topic, int(self.cycle_checkBox.isChecked()))
 
    # Called by a node in response to a ping request. 
    # Ping request are sent whenever we need to know the value of a parameter of a node.
    # To update the Settings Views
    def on_topic_response(self, topic, message, sender):
        
        if topic in self._output_activation_states:
            self._output_activation_states[topic] = message
            return

        if topic == self._selected_filename_topic:
            filename = message
            if topic == self._filename_rhythmic_topic:
                suffix = "_periodic.tsv"
                if filename == suffix:
                    filename = ""
                elif filename.endswith(suffix):
                    filename = filename[:-len(suffix)] + ".tsv"
            self.filename_lineEdit.setText(filename)
        if topic == self._dist_total_constant_topic:
            self.total_checkBox.setChecked(int(message))
        if topic == self._dist_hour_constant_topic:
            self.hour_checkBox.setChecked(int(message))
        if topic == self._dist_cycle_constant_topic:
            self.cycle_checkBox.setChecked(int(message))

    def on_topic_update(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            at any update, does not necessary answer to a ping.
            To listen to any modification not only when you ask (ping)
        """
        pass


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
            self._pub_sub_manager.unsubscribe(self, self._filename_topic)
            self._pub_sub_manager.unsubscribe(self, self._filename_annot_topic)
            self._pub_sub_manager.unsubscribe(self, self._filename_fooof_topic)
            self._pub_sub_manager.unsubscribe(self, self._filename_rhythmic_topic)
            self._pub_sub_manager.unsubscribe(self, self._filename_arhythmic_topic)
            self._pub_sub_manager.unsubscribe(self, self._dist_total_constant_topic)
            self._pub_sub_manager.unsubscribe(self, self._dist_hour_constant_topic)
            self._pub_sub_manager.unsubscribe(self, self._dist_cycle_constant_topic)

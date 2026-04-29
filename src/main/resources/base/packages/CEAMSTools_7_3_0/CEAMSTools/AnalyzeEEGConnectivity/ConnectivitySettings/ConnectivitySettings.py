#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    ConnectivitySettings
    Settings step for connectivity analysis (wPLI/dPLI, parameters, and routing).
"""

from qtpy import QtWidgets

from CEAMSTools.AnalyzeEEGConnectivity.ConnectivitySettings.Ui_ConnectivitySettings import Ui_ConnectivitySettings
from CEAMSTools.AnalyzeEEGConnectivity.FilterStep.FilterStep import FilterStep
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState

class ConnectivitySettings(BaseStepView, Ui_ConnectivitySettings, QtWidgets.QWidget):
    """
    Step to let the user:
    - Pick between wPLI and dPLI (radio buttons)
    - Set epoch and connectivity parameters (line edits)
    - Automatically routes/activates all modules and sends parameters to the correct nodes.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self)

        # Annotation branch nodes
        self.annotation_wpli = {
            "details": "803b6207-918f-4e3e-b5be-48ad9fc8b01c",
            "conn": "3cace954-8d81-4039-8730-b2a90a67c93b",
            "epoch": "b680606e-dd88-442e-8969-19b71ea377a0",
        }
        self.annotation_dpli = {
            "details": "cc042193-2e41-49e0-b80e-973b1174cdb9",
            "conn": "327736b2-6d0a-4186-a123-f0e93a85d232",
            "epoch": "fdc0c057-3fb5-4c9f-92f5-23b1474f7a2d",
        }
        # Sleep-stage branch nodes
        self.sleep_wpli = {
            "details": "2ed43dd6-b69b-4fe2-a443-89f7b066e3b2",
            "conn": "d71e961f-5d95-415b-a4f0-934c3af7b19d",
            "epoch": "c36ee8d3-7f95-4690-b5c6-b53bf7cf803b",
        }
        self.sleep_dpli = {
            "details": "c5a51a23-6afb-444f-a746-3c8e9c5be5ab",
            "conn": "b7f4254a-adb5-4ede-9a9c-39cffe235232",
            "epoch": "eec3640c-7e80-4912-9700-d5fe4a32a02b",
        }
        self._scope = "specific_annotations"

        # --- Connect radio buttons to method change handler ---
        self.dpli_radioButton.toggled.connect(self.on_method_changed)
        self.wpli_radioButton.toggled.connect(self.on_method_changed)

        # # --- Default to wPLI checked and modules activated ---
        # self.wpli_radioButton.setChecked(True)
        # self.on_method_changed()  # Ensures everything is initialized correctly

    def on_method_changed(self):
        """
        When user switches between wPLI and dPLI, activate the relevant modules
        and deactivate the irrelevant ones.
        """
        self._sync_method_scope_activation()

    def _set_chain_state(self, chain_dict, activated):
        for node_id in chain_dict.values():
            if activated:
                self.activate_node(node_id)
            else:
                self.deactivate_node(node_id)

    def _active_chains(self):
        if self._scope == "sleep_stages":
            return self.sleep_wpli, self.sleep_dpli
        return self.annotation_wpli, self.annotation_dpli

    def _sync_method_scope_activation(self):
        wpli_chain, dpli_chain = self._active_chains()
        inactive_wpli_chain, inactive_dpli_chain = (
            (self.annotation_wpli, self.annotation_dpli)
            if self._scope == "sleep_stages"
            else (self.sleep_wpli, self.sleep_dpli)
        )

        # Make sure the non-selected scope is always OFF.
        self._set_chain_state(inactive_wpli_chain, False)
        self._set_chain_state(inactive_dpli_chain, False)

        # Activate only one method inside selected scope.
        if self.wpli_radioButton.isChecked():
            self._set_chain_state(wpli_chain, True)
            self._set_chain_state(dpli_chain, False)
        else:
            self._set_chain_state(wpli_chain, False)
            self._set_chain_state(dpli_chain, True)

    def activate_node(self, node_id):
        """
        Helper to activate a module/node by its ID.
        """
        self._pub_sub_manager.publish(
            self, f"{node_id}.activation_state_change", ActivationState.ACTIVATED
        )

    def deactivate_node(self, node_id):
        """
        Helper to deactivate a module/node by its ID.
        """
        self._pub_sub_manager.publish(
            self, f"{node_id}.activation_state_change", ActivationState.DEACTIVATED
        )

    def on_apply_settings(self):
        """
        When user hits Apply/OK, push the lineEdit values to the right modules,
        depending on method selected (wPLI or dPLI).
        """
        epoch_length = self.epoch_length_lineEdit.text().strip()
        epoch_overlap = self.epoch_overlap_lineEdit.text().strip()
        num_surr = self.num_surr_lineedit.text().strip()
        p_value = self.p_value_lineedit.text().strip()

        self._sync_method_scope_activation()

        if self.wpli_radioButton.isChecked():
            active_chain = self._active_chains()[0]
        else:
            active_chain = self._active_chains()[1]

        self._pub_sub_manager.publish(self, f"{active_chain['epoch']}.epoch_length_sec", epoch_length)
        self._pub_sub_manager.publish(self, f"{active_chain['epoch']}.overlap_sec", epoch_overlap)
        self._pub_sub_manager.publish(self, f"{active_chain['conn']}.num_surr", num_surr)
        self._pub_sub_manager.publish(self, f"{active_chain['conn']}.p_value", p_value)

    def load_settings(self):
        self._scope = self._context_manager.get(FilterStep.context_Con_scope, "specific_annotations")
        self._sync_method_scope_activation()

    def on_validate_settings(self):
        """
        Optional: Check if all fields are filled before allowing to apply settings.
        """
        # You could add more checks here if needed
        return True

    def on_topic_update(self, topic, message, sender):
        if topic == self._context_manager.topic and message == FilterStep.context_Con_scope:
            self._scope = self._context_manager.get(FilterStep.context_Con_scope, "specific_annotations")
            self._sync_method_scope_activation()

    def on_topic_response(self, topic, message, sender):
        # Not used, but could be for advanced sync
        pass

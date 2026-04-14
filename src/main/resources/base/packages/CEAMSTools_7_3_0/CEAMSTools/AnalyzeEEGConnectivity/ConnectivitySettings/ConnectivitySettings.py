#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    ConnectivitySettings
    Settings step for connectivity analysis (wPLI/dPLI, parameters, and routing).
"""

from qtpy import QtWidgets

from CEAMSTools.AnalyzeEEGConnectivity.ConnectivitySettings.Ui_ConnectivitySettings import Ui_ConnectivitySettings
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

        # --- Node IDs for WPLI and DPLI chains ---
        self.connectivitydetails_node_id_wpli = "803b6207-918f-4e3e-b5be-48ad9fc8b01c"
        self.wpliconnectivity_node_id = "3cace954-8d81-4039-8730-b2a90a67c93b"
        self.epochsignal_node_id_wpli = "b680606e-dd88-442e-8969-19b71ea377a0"
        self.networkproperties_node_id = "8608df84-c1f5-4568-bba9-ea8c8aa456ae"

        self.connectivitydetails_node_id_dpli = "cc042193-2e41-49e0-b80e-973b1174cdb9"
        self.dpliconnectivity_node_id = "327736b2-6d0a-4186-a123-f0e93a85d232"
        self.epochsignal_node_id_dpli = "fdc0c057-3fb5-4c9f-92f5-23b1474f7a2d"

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
        if self.wpli_radioButton.isChecked():
            # Activate wPLI modules, deactivate dPLI modules
            self.activate_node(self.connectivitydetails_node_id_wpli)
            self.activate_node(self.wpliconnectivity_node_id)
            self.activate_node(self.epochsignal_node_id_wpli)
            self.activate_node(self.networkproperties_node_id)

            self.deactivate_node(self.connectivitydetails_node_id_dpli)
            self.deactivate_node(self.dpliconnectivity_node_id)
            self.deactivate_node(self.epochsignal_node_id_dpli)

        elif self.dpli_radioButton.isChecked():
            # Activate dPLI modules, deactivate wPLI modules
            self.activate_node(self.connectivitydetails_node_id_dpli)
            self.activate_node(self.dpliconnectivity_node_id)
            self.activate_node(self.epochsignal_node_id_dpli)

            self.deactivate_node(self.connectivitydetails_node_id_wpli)
            self.deactivate_node(self.wpliconnectivity_node_id)
            self.deactivate_node(self.epochsignal_node_id_wpli)
            self.deactivate_node(self.networkproperties_node_id)

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

        if self.wpli_radioButton.isChecked():
            # Push epoch parameters to epochsignal_node_id_wpli
            self._pub_sub_manager.publish(self, f"{self.epochsignal_node_id_wpli}.epoch_length_sec", epoch_length)
            self._pub_sub_manager.publish(self, f"{self.epochsignal_node_id_wpli}.overlap_sec", epoch_overlap)
            # Push connectivity params to wpliconnectivity_node_id
            self._pub_sub_manager.publish(self, f"{self.wpliconnectivity_node_id}.num_surr", num_surr)
            self._pub_sub_manager.publish(self, f"{self.wpliconnectivity_node_id}.p_value", p_value)
        elif self.dpli_radioButton.isChecked():
            # Push epoch parameters to epochsignal_node_id_dpli
            self._pub_sub_manager.publish(self, f"{self.epochsignal_node_id_dpli}.epoch_length_sec", epoch_length)
            self._pub_sub_manager.publish(self, f"{self.epochsignal_node_id_dpli}.overlap_sec", epoch_overlap)
            # Push connectivity params to dpliconnectivity_node_id
            self._pub_sub_manager.publish(self, f"{self.dpliconnectivity_node_id}.num_surr", num_surr)
            self._pub_sub_manager.publish(self, f"{self.dpliconnectivity_node_id}.p_value", p_value)

    def load_settings(self):
        # Could ping nodes for initial values to display (optional, not strictly needed)
        pass

    def on_validate_settings(self):
        """
        Optional: Check if all fields are filled before allowing to apply settings.
        """
        # You could add more checks here if needed
        return True

    def on_topic_update(self, topic, message, sender):
        # Not used, but could be for advanced sync
        pass

    def on_topic_response(self, topic, message, sender):
        # Not used, but could be for advanced sync
        pass

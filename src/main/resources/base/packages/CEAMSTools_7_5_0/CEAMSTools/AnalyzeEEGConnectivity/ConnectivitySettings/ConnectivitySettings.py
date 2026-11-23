#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    ConnectivitySettings
    Settings step for connectivity analysis (wPLI/dPLI/AEC, parameters, and routing).

    The pipeline has two branches (annotation and sleep stages) and three
    connectivity methods (wPLI, dPLI, AEC). This step activates only the chain
    matching the current scope (from FilterStep) and the selected method, and
    routes the epoch / connectivity / network-properties parameters to it.
"""

from qtpy import QtCore, QtWidgets

from CEAMSTools.AnalyzeEEGConnectivity.ConnectivitySettings.Ui_ConnectivitySettings import Ui_ConnectivitySettings
from CEAMSTools.AnalyzeEEGConnectivity.FilterStep.FilterStep import FilterStep
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState

class ConnectivitySettings(BaseStepView, Ui_ConnectivitySettings, QtWidgets.QWidget):
    """
    Step to let the user:
    - Pick between wPLI, dPLI, and AEC (radio buttons)
    - Set epoch and connectivity parameters (line edits)
    - Automatically routes/activates the correct chain for the current scope
      (annotation vs sleep stages) and sends parameters to the correct nodes.
    """
    def __init__(self, **kwargs):
        self._settings_loaded = False
        self._connectivity_states = {}
        self._saved_parameters = {}
        super().__init__(**kwargs)
        self.setupUi(self)

        # --- Node IDs grouped by scope + method chains ---
        # Each chain: epoch -> connectivity -> details (+ network for wPLI).
        self.annotation_wpli = {
            "epoch":   "b680606e-dd88-442e-8969-19b71ea377a0",
            "conn":    "3cace954-8d81-4039-8730-b2a90a67c93b",
            "details": "803b6207-918f-4e3e-b5be-48ad9fc8b01c",
            "network": "02d58c3b-80ec-4e80-8a3c-33d9ee521c18",
        }
        self.annotation_dpli = {
            "epoch":   "fdc0c057-3fb5-4c9f-92f5-23b1474f7a2d",
            "conn":    "327736b2-6d0a-4186-a123-f0e93a85d232",
            "details": "cc042193-2e41-49e0-b80e-973b1174cdb9",
        }
        self.annotation_aec = {
            "epoch":   "829d7060-7e36-412a-9857-bfa39dfacaf0",
            "conn":    "a8b8a023-ed8d-4a5c-a896-1d7051ee058c",
            "details": "838795ca-9563-4370-918e-f8f92cc23220",
        }
        self.sleep_wpli = {
            "epoch":   "5a62634e-6fad-4e52-8d8a-01e4f3ce6dbd",
            "conn":    "727ba862-fd21-43df-82b9-f399918f587d",
            "details": "209980db-ecf3-4d88-9f66-c27373268a3b",
            "network": "9b9b5bb5-f0a3-44f4-8d31-b3ee1896f725",
        }
        self.sleep_dpli = {
            "epoch":   "a120bd2f-4d9b-4e08-8e45-ce51d577ae9f",
            "conn":    "2c8437e3-9a1b-4584-86b0-54308d9bb6f2",
            "details": "82b687e5-9cb4-43bc-80a8-b1cd735ded9b",
        }
        self.sleep_aec = {
            "epoch":   "41f96138-814c-492c-bac8-fe01b4c3f65e",
            "conn":    "2d967628-7e28-4b27-98f7-2abb069204df",
            "details": "7f93939c-b105-4637-a8e9-eae8fc40ceb1",
        }

        # --- Connect radio buttons to method change handler ---
        self.dpli_radioButton.toggled.connect(self.method_changed_slot)
        self.wpli_radioButton.toggled.connect(self.method_changed_slot)
        self.aec_radioButton.toggled.connect(self.method_changed_slot)
        self.custom_threshold_radioButton.toggled.connect(self.threshold_mode_changed_slot)
        self.mst_radioButton.toggled.connect(self.threshold_mode_changed_slot)

        self._update_method_widgets() # Update UI widgets based on the currently selected method
        self.threshold_mode_changed_slot() # Update threshold UI based on the current mode


    # ------------------------------------------------------------------ #
    #  Scope / method helpers
    # ------------------------------------------------------------------ #
    def _all_chains(self):
        return [
            self.annotation_wpli, self.annotation_dpli, self.annotation_aec,
            self.sleep_wpli, self.sleep_dpli, self.sleep_aec,
        ]

    def _active_scope_branch(self):
        """
        Return "sleep" when the FilterStep scope is sleep stages, "annotation"
        otherwise (specific annotations OR unscored both use the annotation
        branch nodes, the latter with SignalsFromEvents bypassed).
        """
        try:
            scope = self._context_manager[FilterStep.context_Con_scope]
        except (KeyError, TypeError):
            scope = "sleep_stages"
        return "sleep" if scope == "sleep_stages" else "annotation"

    def _active_method(self):
        if self.dpli_radioButton.isChecked():
            return "dpli"
        if self.aec_radioButton.isChecked():
            return "aec"
        return "wpli"

    def _active_chain(self):
        return getattr(self, f"{self._active_scope_branch()}_{self._active_method()}")

    def _can_update_process(self):
        """
        True once this step and FilterStep restored the saved settings
        (FilterStep shares the scope through the context only after restoring it).
        """
        return self._settings_loaded and FilterStep.context_Con_scope in self._context_manager

    def _sync_activation(self):
        """Deactivate every chain, then activate only the active scope+method chain."""
        if not self._can_update_process():
            return
        for chain in self._all_chains():
            for node_id in chain.values():
                self.deactivate_node(node_id)
        for node_id in self._active_chain().values():
            self.activate_node(node_id)


    # ------------------------------------------------------------------ #
    #  UI widget state
    # ------------------------------------------------------------------ #
    def threshold_mode_changed_slot(self):
        """Enable the threshold value only when wPLI uses a custom threshold."""
        is_wpli = (self._active_method() == "wpli")
        if is_wpli and self.custom_threshold_radioButton.isChecked():
            self.threshold_val_doubleSpinBox.setEnabled(True)
            self.threshold_val_label.setEnabled(True)
        else:
            self.threshold_val_doubleSpinBox.setEnabled(False)
            self.threshold_val_label.setEnabled(False)

    def _update_method_widgets(self):
        """Enable parameter sections for the method; threshold mode is handled separately."""
        method = self._active_method()
        is_wpli = (method == "wpli")
        is_stats = method in ("wpli", "dpli")  # surrogate-based statistics

        self.connectivity_settings_header_label.setEnabled(is_stats)
        self.connectivity_settings_label.setEnabled(is_stats)
        self.num_surr_label.setEnabled(is_stats)
        self.num_surr_lineedit.setEnabled(is_stats)
        self.p_value_label.setEnabled(is_stats)
        self.p_value_lineedit.setEnabled(is_stats)

        # Network properties (and its thresholding) are only relevant for wPLI.
        self.network_properties_header_label.setEnabled(is_wpli)
        self.network_properties_textEdit.setEnabled(is_wpli)
        self.select_mode_label.setEnabled(is_wpli)
        self.custom_threshold_radioButton.setEnabled(is_wpli)
        self.mst_radioButton.setEnabled(is_wpli)
        self.threshold_val_doubleSpinBox.setEnabled(is_wpli)
        self.threshold_val_label.setEnabled(is_wpli)

    def method_changed_slot(self):
        """
        When the user switches method, activate the correct chain for the current
        scope and update which parameter widgets are enabled.
        """
        self._sync_activation()
        self._update_method_widgets()
        self.threshold_mode_changed_slot()


    # ------------------------------------------------------------------ #
    #  Node activation helpers
    # ------------------------------------------------------------------ #
    def activate_node(self, node_id):
        """Helper to activate a module/node by its ID."""
        self._pub_sub_manager.publish(
            self, f"{node_id}.activation_state_change", ActivationState.ACTIVATED
        )

    def deactivate_node(self, node_id):
        """Helper to deactivate a module/node by its ID."""
        self._pub_sub_manager.publish(
            self, f"{node_id}.activation_state_change", ActivationState.DEACTIVATED
        )


    # ------------------------------------------------------------------ #
    #  Settings lifecycle
    # ------------------------------------------------------------------ #
    def on_apply_settings(self):
        """
        Push the lineEdit values to the active chain, depending on the selected
        scope (annotation/sleep) and method (wPLI/dPLI/AEC).
        """
        # Also called when the workspace is saved (without validation): keep the
        # saved process untouched if it could not be restored.
        if not self._can_update_process():
            return
        epoch_length = self.epoch_length_lineEdit.text().strip()
        epoch_overlap = self.epoch_overlap_lineEdit.text().strip()
        num_surr = self.num_surr_lineedit.text().strip()
        p_value = self.p_value_lineedit.text().strip()

        self._sync_activation()

        chain = self._active_chain()
        method = self._active_method()

        # Epoch parameters (all methods use EpochSignal).
        self._pub_sub_manager.publish(self, f"{chain['epoch']}.epoch_length_sec", epoch_length)
        self._pub_sub_manager.publish(self, f"{chain['epoch']}.overlap_sec", epoch_overlap)

        # Surrogate-based statistics (wPLI and dPLI only).
        if method in ("wpli", "dpli"):
            self._pub_sub_manager.publish(self, f"{chain['conn']}.num_surr", num_surr)
            self._pub_sub_manager.publish(self, f"{chain['conn']}.p_value", p_value)

        # Network properties thresholding (wPLI only).
        if method == "wpli" and "network" in chain:
            if self.custom_threshold_radioButton.isChecked():
                threshold = self.threshold_val_doubleSpinBox.value()
                self._pub_sub_manager.publish(self, f"{chain['network']}.threshold_value", threshold)
                self._pub_sub_manager.publish(self, f"{chain['network']}.threshold_mode", 'custom_threshold')
            elif self.mst_radioButton.isChecked():
                self._pub_sub_manager.publish(self, f"{chain['network']}.threshold_mode", 'minimally_spanning_tree')

    def load_settings(self):
        """Restore the method and its parameters from the process without changing it."""
        self._settings_loaded = False
        chains_by_topic = {
            f"{getattr(self, f'{scope}_{method}')['conn']}.get_activation_state": (scope, method)
            for scope in ("annotation", "sleep")
            for method in ("wpli", "dpli", "aec")
        }
        self._connectivity_states = dict.fromkeys(chains_by_topic)
        # NodeGraphicsItem replies synchronously through on_topic_response.
        for topic in chains_by_topic:
            self._pub_sub_manager.publish(self, topic, None)

        active_chains = [
            chains_by_topic[topic]
            for topic, state in self._connectivity_states.items()
            if state == ActivationState.ACTIVATED
        ]
        if None in self._connectivity_states.values() or len(active_chains) != 1:
            self._pub_sub_manager.publish(
                self, "show_error_message",
                "Could not restore connectivity settings: expected exactly one "
                "active connectivity module and a response from all six modules."
            )
            return
        scope, method = active_chains[0]

        with QtCore.QSignalBlocker(self.wpli_radioButton), \
                QtCore.QSignalBlocker(self.dpli_radioButton), \
                QtCore.QSignalBlocker(self.aec_radioButton):
            getattr(self, f"{method}_radioButton").setChecked(True)
        if not self._load_parameters(getattr(self, f"{scope}_{method}"), method):
            return
        self._update_method_widgets()
        self.threshold_mode_changed_slot()
        self._settings_loaded = True

    def _load_parameters(self, chain, method):
        """
        Read the parameters of the saved active chain and show them in the UI
        (same parameters as on_apply_settings). An empty value was never set:
        the UI default is kept. Return False if a saved value is invalid.
        """
        topics = {
            "epoch_length_sec": f"{chain['epoch']}.epoch_length_sec",
            "overlap_sec": f"{chain['epoch']}.overlap_sec",
        }
        if method in ("wpli", "dpli"):
            topics["num_surr"] = f"{chain['conn']}.num_surr"
            topics["p_value"] = f"{chain['conn']}.p_value"
        if "network" in chain:
            topics["threshold_mode"] = f"{chain['network']}.threshold_mode"
            topics["threshold_value"] = f"{chain['network']}.threshold_value"

        # NodePortGraphicsItem replies synchronously through on_topic_response.
        self._saved_parameters = dict.fromkeys(topics.values())
        for topic in topics.values():
            self._pub_sub_manager.publish(self, topic, 'ping')
        saved = {
            name: str(self._saved_parameters[topic]).strip()
            for name, topic in topics.items()
            if self._saved_parameters[topic] not in (None, '')
        }

        threshold_mode = saved.get("threshold_mode")
        if threshold_mode not in (None, 'custom_threshold', 'minimally_spanning_tree'):
            self._pub_sub_manager.publish(
                self, "show_error_message",
                f"Could not restore connectivity settings: unknown threshold mode '{threshold_mode}'."
            )
            return False
        try:
            threshold_value = float(saved["threshold_value"]) if "threshold_value" in saved else None
        except ValueError:
            self._pub_sub_manager.publish(
                self, "show_error_message",
                f"Could not restore connectivity settings: invalid threshold value "
                f"'{saved['threshold_value']}'."
            )
            return False

        line_edits = {
            "epoch_length_sec": self.epoch_length_lineEdit,
            "overlap_sec": self.epoch_overlap_lineEdit,
            "num_surr": self.num_surr_lineedit,
            "p_value": self.p_value_lineedit,
        }
        for name, line_edit in line_edits.items():
            if name in saved:
                line_edit.setText(saved[name])
        if threshold_mode is not None:
            with QtCore.QSignalBlocker(self.custom_threshold_radioButton), \
                    QtCore.QSignalBlocker(self.mst_radioButton):
                self.custom_threshold_radioButton.setChecked(threshold_mode == 'custom_threshold')
                self.mst_radioButton.setChecked(threshold_mode == 'minimally_spanning_tree')
        if threshold_value is not None:
            self.threshold_val_doubleSpinBox.setValue(threshold_value)
        return True

    def on_validate_settings(self):
        if not self._settings_loaded:
            self._pub_sub_manager.publish(
                self, "show_error_message",
                "Connectivity settings could not be restored. "
                "Please check the connectivity modules in the process."
            )
        return self._settings_loaded

    def on_topic_update(self, topic, message, sender):
        # React to a scope change from FilterStep by re-routing the active chain.
        if topic == self._context_manager.topic:
            if message == FilterStep.context_Con_scope:
                self._sync_activation()

    def on_topic_response(self, topic, message, sender):
        if topic in self._connectivity_states:
            self._connectivity_states[topic] = message
        elif topic in self._saved_parameters:
            self._saved_parameters[topic] = message

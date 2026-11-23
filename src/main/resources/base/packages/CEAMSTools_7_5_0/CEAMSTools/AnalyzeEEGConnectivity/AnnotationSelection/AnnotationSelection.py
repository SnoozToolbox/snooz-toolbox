#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    AnnotationSelection
    TODO CLASS DESCRIPTION
"""

from qtpy import QtWidgets

from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep import NonValidEventStep
from CEAMSTools.AnalyzeEEGConnectivity.FilterStep.FilterStep import FilterStep

class AnnotationSelection(NonValidEventStep):
    """
        AnnotationSelection
        TODO CLASS DESCRIPTION
    """

    node_id_ResetSignalArtefact_0 = None  

    node_id_Dictionary_group = "3be09df1-eda9-4ef7-a415-74404a6ce78b" # select the list of group for the current filename
    node_id_Dictionary_name = "92ab2bd0-7063-4b43-8ce0-1c2fa7df1200" # select the list of name for the current filename    

    # group_input_label = 'constant'
    # name_input_label = 'constant'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.reset_excl_event_checkBox.setEnabled(False)
        # Subscribe to context manager for each node you want to talk to
        # self._artefact_group_topic = f'{self._node_id_Dictionary_group}.{self.group_input_label}'
        # self._pub_sub_manager.subscribe(self, self._artefact_group_topic)
        # self._artefact_name_topic = f'{self._node_id_Dictionary_name}.{self.name_input_label}'
        # self._pub_sub_manager.subscribe(self, self._artefact_name_topic)

        self._node_id_SignalsFromEvents = "7b92caa3-9e9e-46bc-b790-6175abb7ae45"
        self.sleep_stage_scope = False
        self.annot_selection_scope = False
        self.enable_widgets(False)
        self.match_event_channels_checkBox.setChecked(True)


    def on_apply_settings(self):

        if self.annot_selection_scope:
            # Specific annotations: publish the user-selected group/name dicts so
            # SignalsFromEvents crops the signal on those annotations.
            super().on_apply_settings()
        else:
            # Sleep stages OR unscored: publish empty group/name dicts.
            # For the sleep branch, SleepStageEvents has already filtered the events
            # to the selected stages, and SignalsFromEvents keeps ALL received
            # events when events_groups == ''. Empty strings (not None) also avoid
            # the downstream None.split() crash.
            files_list = self.reader_settings_view.get_files_list(self.files_check_event_model)
            empty_dict = {file: "" for file in files_list}
            self._pub_sub_manager.publish(self, self._artefact_group_topic, str(empty_dict))
            self._pub_sub_manager.publish(self, self._artefact_name_topic, str(empty_dict))



    def load_settings(self):
        super().load_settings()
        # Sync the scope from the context (it may have been set by FilterStep
        # before this step subscribed to the context manager).
        self._sync_scope_from_context()
        # To activate the Signals From Events on annotations branch
        self._pub_sub_manager.publish(self, self._node_id_SignalsFromEvents+".get_activation_state", None)


    def _sync_scope_from_context(self):
        try:
            scope = self._context_manager[FilterStep.context_Con_scope]
        except (KeyError, TypeError):
            scope = "sleep_stages"
        self.annot_selection_scope = (scope == "specific_annotations")
        self.sleep_stage_scope = (scope == "sleep_stages")
        # Only enable the annotation selection widgets for the annotation scope.
        self.enable_widgets(self.annot_selection_scope)


    def on_topic_update(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            at any update, does not necessary answer to a ping.
            To listen to any modification not only when you ask (ping)
        """
        super().on_topic_update(topic, message, sender)

        if topic==self._context_manager.topic:
            # The analysis scope changed in FilterStep.
            if message==FilterStep.context_Con_scope:
                self._sync_scope_from_context()


    # Answer to a ping
    #  The UI or the properties are updated from the pipeline.json
    def on_topic_response(self, topic, message, sender):
        super().on_topic_response(topic, message, sender)


    def enable_widgets(self, bool_flag):
        self.file_listview.setEnabled(bool_flag)
        self.event_treeview.setEnabled(bool_flag)
        self.select_all_checkBox.setEnabled(False)
        self.search_lineEdit.setEnabled(bool_flag)
        self.reset_all_files_pushButton.setEnabled(bool_flag)

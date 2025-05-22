"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    AnnotationsSelStep
    Step in the PowerSpectralAnalysis interface to select annotations to run the PSA.
    This step is really similar to NonValidEventStep, 
    but the interface needs to be desabled or enabled depending on a selection in the step "4-Section Slection".
    So, we inherit from NonValidEventStep and add the function to desable widgets.
        Doc to open and read to understand : 
        Model and item : QAbstractItemModel -> QStandardItemModel -> QStandardItem
        View : QAbstractItemView -> QTreeView
"""
from flowpipe.ActivationState import ActivationState

from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep import NonValidEventStep
from CEAMSTools.PowerSpectralAnalysis.SelectionStep.SelectionStep import SelectionStep

DEBUG = True
class AnnotationsSelStep( NonValidEventStep):

    # Define modules and nodes to talk to
    node_id_ResetSignalArtefact_0 = None
    node_id_Dictionary_group = "1ee9e510-d78b-48e4-8a81-dbd37093f2b3" # select the list of group for the current filename
    node_id_Dictionary_name = "57d1acd5-f2a5-49fc-a93a-422b334f2112"  # select the list of name for the current filename    

    group_input_label = 'constant'
    name_input_label = 'constant'
    
    """
        PowerSpectralAnalysis
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform "Reset Signal Interface" and "Discard Events" modules.
    """
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.reset_excl_event_checkBox.setEnabled(False)
        # Subscribe to context manager for each node you want to talk to
        self._artefact_group_topic = f'{self._node_id_Dictionary_group}.{self.group_input_label}'
        self._pub_sub_manager.subscribe(self, self._artefact_group_topic)
        self._artefact_name_topic = f'{self._node_id_Dictionary_name}.{self.name_input_label}'
        self._pub_sub_manager.subscribe(self, self._artefact_name_topic)

        self._node_id_SignalsFromEvents_Annot = "d3620a6b-03f5-444f-b93e-e3ca23983b56" # To activate for PSA on annot


    def load_settings(self):
        super().load_settings()
        # To activate the PSA on annotations branch
        self._pub_sub_manager.publish(self, self._node_id_SignalsFromEvents_Annot+".get_activation_state", None)


    def on_topic_update(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            at any update, does not necessary answer to a ping.
            To listen to any modification not only when you ask (ping)
        """
        super().on_topic_update(topic, message, sender)

        if topic==self._context_manager.topic:
            # PSA section selection changed
            if message==SelectionStep.context_PSA_annot_selection: # key of the context dict
                bool_flag = True if self._context_manager[SelectionStep.context_PSA_annot_selection]==1 else False
                self.enable_widgets(bool_flag)


    # Answer to a ping
    #  The UI or the properties are updated from the pipeline.json
    def on_topic_response(self, topic, message, sender):
        super().on_topic_response(topic, message, sender)
        if topic == self._node_id_SignalsFromEvents_Annot+".get_activation_state":
            if message == ActivationState.ACTIVATED:
                self.enable_widgets(True)
            else:
                self.enable_widgets(False)


    def enable_widgets(self, bool_flag):
        self.file_listview.setEnabled(bool_flag)
        self.event_treeview.setEnabled(bool_flag)
        self.select_all_checkBox.setEnabled(bool_flag)
        self.search_lineEdit.setEnabled(bool_flag)
        self.reset_all_files_pushButton.setEnabled(bool_flag)

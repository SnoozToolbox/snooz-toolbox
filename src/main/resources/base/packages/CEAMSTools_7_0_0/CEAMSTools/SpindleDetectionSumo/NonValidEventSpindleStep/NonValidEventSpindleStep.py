"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
"""
    NonValidEventStep
    Step in the spindle detection interface to exclude non valid events for the spindle detection.
    Doc to open and read to understand : 
    Model and item : QAbstractItemModel -> QStandardItemModel -> QStandardItem
    View : QAbstractItemView -> QTreeView
"""
from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep import NonValidEventStep

class NonValidEventSpindleStep(NonValidEventStep):

    # Define modules and nodes to talk to
    node_id_ResetSignalArtefact_0 = "141974a3-d09b-4e05-9f85-a8a908d80449" # to activate if the signal during artifact are reset
    node_id_Dictionary_group = "93f0bc13-163b-4ab9-9af8-9b1cceb519f7" # select the list of group for the current filename
    node_id_Dictionary_name = "0dfe9ca8-4683-4a3b-bc95-029bc282301a" # select the list of name for the current filename    
    """
        NonValidEventStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform "Reset Signal Interface" and "Discard Events" modules.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reset_excl_event_checkBox.setEnabled(False)
        
        
# For the other functions see CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep
"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    NonValidEventStep
    Step in the SW interface to exclude non valid events for the SW detection.
    Doc to open and read to understand : 
    Model and item : QAbstractItemModel -> QStandardItemModel -> QStandardItem
    View : QAbstractItemView -> QTreeView
"""
from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep import NonValidEventStep

class ArousalAnnotSel(NonValidEventStep):

    # Define modules and nodes to talk to
    node_id_ResetSignalArtefact_0 = None # reset the signal during artifact
    node_id_Dictionary_group = "35ade33a-576d-40b5-ad36-9c1e994d08e7" # select the list of group for the current filename
    node_id_Dictionary_name = "de5c0d66-bd34-418a-acf7-4941cbbf8937" # select the list of name for the current filename    
    """
        NonValidEventStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform "Discard Events" modules via 2 dictionaries (artifact group and name)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reset_excl_event_checkBox.setEnabled(False)
        
# For the other functions see CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep
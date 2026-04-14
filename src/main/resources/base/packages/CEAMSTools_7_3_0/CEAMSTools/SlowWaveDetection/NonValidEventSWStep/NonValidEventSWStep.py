"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    NonValidEventStep
    Step in the SW interface to exclude non valid events for the SW detection.
    The class is inherited from NonValidEventStep of PowerSpectralAnalysis.
        Doc to open and read to understand : 
        Model and item : QAbstractItemModel -> QStandardItemModel -> QStandardItem
        View : QAbstractItemView -> QTreeView
"""
from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep import NonValidEventStep

class NonValidEventSWStep(NonValidEventStep):

    # Define modules and nodes to talk to
    node_id_ResetSignalArtefact_0 = "a3e5858b-7448-41cd-9be4-617fc25be9e1" # reset the signal during artifact
    node_id_Dictionary_group = "5c74bd80-a2e5-430b-a454-e188c0a257df" # select the list of group for the current filename
    node_id_Dictionary_name = "ed03c6cf-eecc-4826-9f43-015366108011" # select the list of name for the current filename    
    """
        NonValidEventStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform "Discard Events" modules via 2 dictionaries (artifact group and name)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reset_excl_event_checkBox.setEnabled(False)
        
# For the other functions see CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep
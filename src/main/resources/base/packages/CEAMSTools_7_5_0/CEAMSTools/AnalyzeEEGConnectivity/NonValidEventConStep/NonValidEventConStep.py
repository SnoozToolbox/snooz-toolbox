"""
© 2025 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    NonValidEventConStep
    Step in the Connectivity interface to exclude non valid events for the Connectivity Analysis.
    The class is inherited from NonValidEventStep of PowerSpectralAnalysis.
        Doc to open and read to understand : 
        Model and item : QAbstractItemModel -> QStandardItemModel -> QStandardItem
        View : QAbstractItemView -> QTreeView
"""
from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep import NonValidEventStep

class NonValidEventConStep(NonValidEventStep):

    # Define modules and nodes to talk to
    node_id_ResetSignalArtefact_0 = "0da1f12b-6531-4ea3-9bb7-24e19d84d367" # reset the signal during artifact
    node_id_Dictionary_group = "91c5a05d-7239-421a-b2af-72432918e291" # select the list of group for the current filename
    node_id_Dictionary_name = "436be2e9-932b-46d2-afcf-7ff0903d1978" # select the list of name for the current filename    
    """
        NonValidEventStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform "Discard Events" modules via 2 dictionaries (artifact group and name)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reset_excl_event_checkBox.setChecked(True)
        self.reset_excl_event_checkBox.setEnabled(False)
        # Usefull to select many annotations at the same time on the UI
        #self.select_all_checkBox.setEnabled(False)
        
# For the other functions see CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep
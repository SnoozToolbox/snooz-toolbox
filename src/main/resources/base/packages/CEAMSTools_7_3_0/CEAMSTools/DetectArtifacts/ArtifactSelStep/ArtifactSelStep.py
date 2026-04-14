"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    NonValidEventStep
    Step in the PSA interface to exclude non valid events for the PSA analysis.
    Doc to open and read to understand : 
    Model and item : QAbstractItemModel -> QStandardItemModel -> QStandardItem
    View : QAbstractItemView -> QTreeView
"""
from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep import NonValidEventStep

class ArtifactSelStep(NonValidEventStep):

    # The class ArtifactSelStep is created only to define the modules and nodes to talk to
    # Define modules and nodes to talk to
    node_id_ResetSignalArtefact_0 = None # to activate if the signal during artifact are reset
    node_id_Dictionary_group = "fdffc3b0-7ef0-4b45-98a3-63093adae04a" # select the list of group for the current filename
    node_id_Dictionary_name = "41a6b6f1-08b3-417c-bafb-30dc2274c24b" # select the list of name for the current filename    
    """
        NonValidEventStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform "Reset Signal Interface" and "Discard Events" modules.
    """
        
# For the other functions see CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep
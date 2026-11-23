#! /usr/bin/env python3
"""
    SelectEventsStep
    Step to select specific annotations to save in the output tsv file.
"""

from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep import NonValidEventStep

class SelectEventsStep(NonValidEventStep):
    # Define modules and nodes to talk to
    node_id_ResetSignalArtefact_0 = None # reset the signal during artifact
    node_id_Dictionary_group = "9e2e8c71-d2cc-48a3-89a0-c1241e66ab4e" # select the list of group for the current filename
    node_id_Dictionary_name = "c111e8b0-e11c-4846-8c1a-46352f849203" # select the list of name for the current filename    
    """
        NonValidEventStep
        Class to send messages between step-by-step interface and plugins.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reset_excl_event_checkBox.setEnabled(False)
        
# For the other functions see CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.NonValidEventStep

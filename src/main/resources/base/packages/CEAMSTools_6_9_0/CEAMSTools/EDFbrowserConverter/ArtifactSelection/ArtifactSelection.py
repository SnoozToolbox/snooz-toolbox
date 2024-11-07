#! /usr/bin/env python3
"""
    ArtifactSelection
    Step in the EDFbrowser converter interface to select the artifact annotations and define the proper group event.
"""

# Exact same straetegy than the StadeSelection
from CEAMSTools.EDFbrowserConverter.Commons import ContextConstants
from CEAMSTools.EDFbrowserConverter.StadeSelection.StadeSelection import StadeSelection

class ArtifactSelection(StadeSelection):
    """
        ArtifactSelection
        Step in the EDFbrowser converter interface to select the artifact annotations and define the proper group event.
    """
    event_group = 'art_snooz'
    context_event_sel_def = ContextConstants.context_artifact_check_model


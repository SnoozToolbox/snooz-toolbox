"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the ResetSignalArtefact plugin
"""

# Take the the result view from the CsvReader
# CsvReader results view show a dataframe of events
from CEAMSModules.EventReader.EventReaderResultsView import EventReaderResultsView

class ResetSignalArtefactResultsView(EventReaderResultsView):
    """
        ResetSignalArtefactResultsView shows selected artefact event
    """
    pass
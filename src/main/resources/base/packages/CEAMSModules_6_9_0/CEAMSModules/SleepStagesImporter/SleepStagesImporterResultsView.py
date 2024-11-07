"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    Results viewer of the SleepStagesImporter plugin
"""

# Take the the result view from the CsvReader
# CsvReader results view show a dataframe of events
from CEAMSModules.EventReader.EventReaderResultsView import EventReaderResultsView

class SleepStagesImporterResultsView(EventReaderResultsView):
    """
        SleepStagesImporterResultsView display the sleep stages list read.
    """
    pass
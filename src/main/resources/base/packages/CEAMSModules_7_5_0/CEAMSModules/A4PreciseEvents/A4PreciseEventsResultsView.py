"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the A4PreciseEvents plugin
"""

from qtpy import QtWidgets

# Take the the result view from the CsvReader
# CsvReader results view show a dataframe of events
from CEAMSModules.EventReader.EventReaderResultsView import EventReaderResultsView

class A4PreciseEventsResultsView(EventReaderResultsView):
    """
        A4PreciseEventsResultsView shows precised events
    """
    pass
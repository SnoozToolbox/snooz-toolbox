"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    Results viewer of the DefineEventGroup plugin
"""

from qtpy import QtWidgets

from CEAMSModules.EventReader.EventReaderResultsView import EventReaderResultsView

class DefineEventGroupResultsView(EventReaderResultsView, QtWidgets.QWidget):
    """
        DefineEventGroupResultsView displays the events list modified
    """
    pass
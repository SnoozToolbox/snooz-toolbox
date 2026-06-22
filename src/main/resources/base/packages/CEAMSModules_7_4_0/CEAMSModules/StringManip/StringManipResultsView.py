"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the StringManip plugin
"""

from qtpy import QtWidgets

from CEAMSModules.StringManip.Ui_StringManipResultsView import Ui_StringManipResultsView

class StringManipResultsView( Ui_StringManipResultsView, QtWidgets.QWidget):
    """
        StringManipResultsView nohting to show.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(StringManipResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)

    def load_results(self):
        pass
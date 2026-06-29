"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the Constant plugin
"""

from qtpy import QtWidgets

from CEAMSModules.Constant.Ui_ConstantResultsView import Ui_ConstantResultsView

class ConstantResultsView( Ui_ConstantResultsView, QtWidgets.QWidget):
    """
        ConstantResultsView nohting to show.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(ConstantResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)

    def load_results(self):
        pass
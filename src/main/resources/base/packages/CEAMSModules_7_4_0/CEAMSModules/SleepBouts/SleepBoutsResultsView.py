"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the SleepBouts plugin
"""

from qtpy import QtWidgets

from CEAMSModules.SleepBouts.Ui_SleepBoutsResultsView import Ui_SleepBoutsResultsView

class SleepBoutsResultsView( Ui_SleepBoutsResultsView, QtWidgets.QWidget):
    """
        SleepBoutsView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(SleepBoutsResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)
        

    def load_results(self):
        pass
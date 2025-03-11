"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    Results viewer of the RenameFileList plugin
"""

from qtpy import QtWidgets

from CEAMSModules.RenameFileList.Ui_RenameFileListResultsView import Ui_RenameFileListResultsView

class RenameFileListResultsView(Ui_RenameFileListResultsView, QtWidgets.QWidget):
    """
        RenameFileListResultsView.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(RenameFileListResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)

    def load_results(self):
        # Code example to load the cache from the module
        # cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)
        # print(cache)
        pass
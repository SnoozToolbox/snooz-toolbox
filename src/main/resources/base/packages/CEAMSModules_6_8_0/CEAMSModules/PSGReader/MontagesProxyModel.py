"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
from qtpy import QtCore

class MontagesProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filenames_filters = []
        self.montage_search_pattern = None

    def filterAcceptsRow(self, sourceRow, sourceParent):
        index0 = self.sourceModel().index(sourceRow, 0, sourceParent)
        index1 = self.sourceModel().index(sourceRow, 1, sourceParent)
        index2 = self.sourceModel().index(sourceRow, 2, sourceParent)

        first_search_criteria = False
        second_search_criteria = False
        if len(self.filenames_filters) > 0:
            first_search_criteria = index2.data() in self.filenames_filters
        else:
            first_search_criteria = True

        if self.montage_search_pattern is not None and self.montage_search_pattern:
            second_search_criteria = self.montage_search_pattern.lower() in index1.data().lower()
        else:
            second_search_criteria = True

        return first_search_criteria and second_search_criteria

    def set_filenames_filters(self, filenames):
        self.filenames_filters = filenames
        self.invalidate()
    
    def set_montages_search_pattern(self, pattern):
        self.montage_search_pattern = pattern
        self.invalidate()

    @property
    def selection(self):
        return self._selection
    
    @selection.setter
    def selection(self, value):
        self._selection = value
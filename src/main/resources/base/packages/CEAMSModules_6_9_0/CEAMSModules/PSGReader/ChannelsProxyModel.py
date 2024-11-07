"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
from qtpy import QtCore

class ChannelsProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filename_montage_pairs_filter = []
        self.channels_search_pattern = None

    def filterAcceptsRow(self, sourceRow, sourceParent):
        index0 = self.sourceModel().index(sourceRow, 0, sourceParent)
        index1 = self.sourceModel().index(sourceRow, 1, sourceParent)
        index2 = self.sourceModel().index(sourceRow, 2, sourceParent)
        index3 = self.sourceModel().index(sourceRow, 3, sourceParent)
        index4 = self.sourceModel().index(sourceRow, 4, sourceParent)

        first_search_criteria = False
        second_search_criteria = False
        if len(self.filename_montage_pairs_filter) > 0:
            montage_filename_pair = (index3.data(), index4.data())
            first_search_criteria = montage_filename_pair in self.filename_montage_pairs_filter

        if self.channels_search_pattern is not None and self.channels_search_pattern:
            second_search_criteria = self.channels_search_pattern.lower() in index1.data().lower()
        else:
            second_search_criteria = True

        return first_search_criteria and second_search_criteria

    def clear_filename_montage_pair_filter(self):
        self.filename_montage_pairs_filter = []
        self.invalidate()

    def set_filename_montage_pair_filter(self, filename_montage_pairs):
        self.filename_montage_pairs_filter = filename_montage_pairs
        self.invalidate()
    
    def set_channels_search_pattern(self, pattern):
        self.channels_search_pattern = pattern
        self.invalidate()

    @property
    def selection(self):
        return self._selection
    
    @selection.setter
    def selection(self, value):
        self._selection = value
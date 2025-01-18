"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
import os
from qtpy import QtCore
""" 
    Model to placed between the model (QAbstractModel) and 
    the tableView (QTableView) in order to filter PSG files.
    i.e. Filter the view to see only the PSG with a specific label via the search line edit.

    A custom model has been created to re-implement filterAcceptsRow.
    The default behavior of QSortFilterProxyModel is to filter the parent and 
    all the children.  FileProxyModel only filters the events group 
    (not the filename and not the events name).
"""
class FileProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filenames_search_pattern = None


    # source_row – PySide.QtCore.int, source_parent – PySide.QtCore.QModelIndex
    def filterAcceptsRow(self, sourceRow, source_parent):
        index0 = self.sourceModel().index(sourceRow, 0, source_parent) # string (filename, group)
        item = self.sourceModel().itemFromIndex(index0)
        cur_text = self.sourceModel().data(index0)
        cur_text = os.path.basename(cur_text)
        if item is not None:
            if self.filenames_search_pattern is not None:
                return self.filenames_search_pattern in cur_text
            else:
                return True
        # Name or filename
        else:
            return True
    

    def set_files_search_pattern(self, pattern):
        self.filenames_search_pattern = pattern
        self.invalidate()


    @property
    def selection(self):
        return self._selection
    
    
    @selection.setter
    def selection(self, value):
        self._selection = value
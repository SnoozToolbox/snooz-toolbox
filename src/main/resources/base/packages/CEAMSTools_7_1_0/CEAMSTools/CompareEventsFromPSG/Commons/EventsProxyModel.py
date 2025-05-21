"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from qtpy import QtCore
""" 
    Model to placed between the files_check_event_model(QAbstractModel) and 
    the event_treeview (QTreeView) in order to filter groups.
    i.e. Filter the Tree viee to see only the artifacts via the search line edit "Comp".

    A custom model has been created to re-implement filterAcceptsRow.
    The default behavior of QSortFilterProxyModel is to filter the parent and 
    all the children.  EventsProxyModel only filters the events group 
    (not the filename and not the events name).
"""
class EventsProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filenames_filters = None
        self.group_search_pattern = None


    # source_row – PySide.QtCore.int, source_parent – PySide.QtCore.QModelIndex
    def filterAcceptsRow(self, sourceRow, sourceParent):
        #if self.filenames_filters is not None :
        # index(int row, int column, const QModelIndex &parent = QModelIndex())
        index0 = self.sourceModel().index(sourceRow, 0, sourceParent) # string (filename, group, name)
        index1 = self.sourceModel().index(sourceRow, 1, sourceParent) # count useless
        item = self.sourceModel().itemFromIndex(index0)
        cur_text = self.sourceModel().data(index0)
        cur_count = self.sourceModel().data(index1)
        #print(f"all row:{sourceRow} : text={cur_text} and count={cur_count}")
        if ((item is not None) and item.hasChildren()) and (item.parent() is not None):
            # Group
            #print(f"group row:{sourceRow} : text={cur_text} and count={cur_count}")
            if self.group_search_pattern is not None:
                return self.group_search_pattern in cur_text
            else:
                return True
        # Name or filename
        else:
            return True


    def set_filenames_filters(self, filenames):
        self.filenames_filters = filenames
        self.invalidate()
    

    def set_groups_search_pattern(self, pattern):
        self.group_search_pattern = pattern
        self.invalidate()


    @property
    def selection(self):
        return self._selection
    
    
    @selection.setter
    def selection(self, value):
        self._selection = value
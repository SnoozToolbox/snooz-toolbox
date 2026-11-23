"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from qtpy import QtCore
""" 
    Model to placed between the files_check_event_model(QAbstractModel) and 
    the event_treeview (QTreeView) in order to filter groups and names.
    i.e. Filter the Tree viee to see only the artifacts via the search line edit "Comp".

    A custom model has been created to re-implement filterAcceptsRow.
    The default behavior of QSortFilterProxyModel is to filter the parent and 
    all the children.  EventsProxyModel only filters the events group and names 
    (not the filename).
"""
class EventsProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filenames_filters = None
        self.group_name_search_pattern = None


    # source_row – PySide.QtCore.int, source_parent – PySide.QtCore.QModelIndex
    def filterAcceptsRow(self, sourceRow, sourceParent):
        if not self.filenames_filters:
            return True
        
        # index(int row, int column, const QModelIndex &parent = QModelIndex())
        source_model = self.sourceModel()
        index = source_model.index(sourceRow, 0, sourceParent) # string (filename, group, name)
        item = source_model.itemFromIndex(index)
        
        # Only the file item has a data set to the complete path
        # It is a file, so we display it only if it is selected
        if item.data():
            return item.data() in self.filenames_filters
        
        # Extract the parent item to evaluate if it is a group or a name
        parent_item = item.parent()
        # Extract the grand parent item to evaluate if it is a name item
        grand_parent = parent_item.parent()
        

        # If the parent item is a file item, we know that the item is a group item
        if parent_item is not None and parent_item.data():
            if parent_item.data() in self.filenames_filters:
                # If we filter for a pattern
                if self.group_name_search_pattern is not None:
                    # Display only if it matches the pattern
                    if self.group_name_search_pattern in item.text():
                        return True
                    # A child item matches the pattern
                    elif item.rowCount() > 0:
                        for i_child in range(item.rowCount()):
                            if self.group_name_search_pattern in item.child(i_child).text():
                                return True
                        return False
                    else:
                        return False
                else:
                    return True 
            else:
                return False

        # If the grand parent item is a file item, we know that the item is a name item
        if grand_parent is not None and grand_parent.data():
            if grand_parent.data() in self.filenames_filters:
                # If we filter for a pattern
                if self.group_name_search_pattern is not None:
                    # Display only if it matches the pattern
                    if self.group_name_search_pattern in item.text():
                        return True
                    # Return True if the parent (group item) matches the pattern
                    elif self.group_name_search_pattern in parent_item.text():
                        return True
                    else:
                        return False
                else:
                    return True 
            else:
                return False

        return True


    def set_filenames_filters(self, filenames):
        self.filenames_filters = filenames
        self.invalidateFilter()
    

    def set_groups_names_search_pattern(self, pattern):
        self.group_name_search_pattern = pattern
        self.invalidateFilter()


    @property
    def selection(self):
        return self._selection
    
    
    @selection.setter
    def selection(self, value):
        self._selection = value

    def count_checked_items_cohort(self):
        def count_checked_recursive(item):
            name_checked = 0
            group_checked = 0
            for row in range(item.rowCount()):
                child = item.child(row)
                if child.isCheckable() and child.checkState() == QtCore.Qt.Checked:
                    if not child.hasChildren() and (not child in childlist):
                        name_checked += 1
                        childlist.append(child.text())
                    if child.hasChildren() and (not child in childlist):
                        group_checked += 1
                        childlist.append(child.text())
                # Recurse into deeper levels if needed
                child_name_checked, child_group_checked = count_checked_recursive(child)
                name_checked += child_name_checked
                group_checked += child_group_checked
            return name_checked, group_checked

        total_name_checked = 0
        total_group_checked = 0
        childlist = []
        top_item_list = []
        model = self.sourceModel()
        if model is not None:
            for row in range(model.rowCount()):
                top_item = model.item(row)
                if top_item is not None:
                    if top_item.isCheckable() and top_item.checkState() == QtCore.Qt.Checked:
                        if not top_item.hasChildren() and (not top_item in top_item_list):
                            total_name_checked += 1
                            top_item_list.append(top_item.text())
                        if top_item.hasChildren() and (not top_item in top_item_list):
                            total_group_checked += 1
                            top_item_list.append(top_item.text())
                    top_item_total_name_checked, top_item_total_group_checked = count_checked_recursive(top_item)
                    total_name_checked += top_item_total_name_checked
                    total_group_checked += top_item_total_group_checked

        return total_name_checked, total_group_checked
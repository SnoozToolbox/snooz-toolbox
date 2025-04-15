"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    CheckBoxDelegate 
    Delegate item used to add a checkbox to a QTableView. It assumes the value
    is a Boolean. 

    How to use:
    # Setup a dataframe.
    data = pd.DataFrame([
        [True, 'Fz', 'EEG', 'Mon montage 1', 256,2],
        [True, 'Fz', 'EEG', 'Mon montage 5', 256,2],
        [False, 'Cz', 'EEG', 'Mon montage 4', 256,2],
        [False, 'Cz', 'EEG', 'Mon montage 3', 256,2],
        [False, 'Cz', 'EEG', 'Mon montage 2', 256,2],
    ], columns = ['Use', 'Channel', 'Type', 'Montage','Sample rate', 'File count'])

    # Create a TableModel which is a custom QtCore.QAbstractTableModel
    self.model = TableModel(data)

    # Set the model of the QTableView
    self.channels_tableview.setModel(self.model)

    # Create a CheckBoxDelegate.
    delegate = CheckBoxDelegate(None)
    self.channels_tableview.setItemDelegateForColumn(0, delegate)

    # Resize all columns, it's especially important for the check mark column or it will not appear properly
    self.channels_tableview.resizeColumnsToContents()

"""
from qtpy import QtWidgets
from qtpy import QtCore

class CheckBoxDelegate(QtWidgets.QItemDelegate):
    """
    A delegate that places a fully functioning QCheckBox cell of the column to which it's applied.
    """
    def __init__(self, parent):
        QtWidgets.QItemDelegate.__init__(self, parent)
        self._on_changed_callback = None

    def createEditor(self, parent, option, index):
        """
        Important, otherwise an editor is created if the user clicks in this cell.
        """
        return None

    def paint(self, painter, option, index):
        """
        Paint a checkbox without the label.
        """
        self.drawCheck(painter, option, option.rect, QtCore.Qt.Checked if index.data() else QtCore.Qt.Unchecked)

    def editorEvent(self, event, model, option, index):
        '''
        Change the data in the model and the state of the checkbox
        if the user presses the left mousebutton and this cell is editable. Otherwise do nothing.
        '''
        if not (index.flags() & QtCore.Qt.ItemIsEditable):
            return False

        if event.type() == QtCore.QEvent.MouseButtonRelease and event.button() == QtCore.Qt.LeftButton:
            # Change the checkbox-state
            self.setModelData(None, model, index)
            return True

        return False

    def setModelData (self, editor, model, index):
        '''
        The user wanted to change the old state in the opposite.
        '''
        is_checked = not index.data()
        model.setData(index, is_checked, QtCore.Qt.EditRole)
        if (self._on_changed_callback is not None):
            self._on_changed_callback()

    def set_on_change_callback(self, callback):
        self._on_changed_callback = callback

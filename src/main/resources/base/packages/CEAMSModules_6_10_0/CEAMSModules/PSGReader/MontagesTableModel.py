"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    MontagesTableModel
    Table model for the selection of montages
"""
from qtpy import QtCore

class MontagesTableModel(QtCore.QAbstractTableModel):
    # Custom signal with the count of checked items
    dataChangedWithCheckState = QtCore.Signal(int)  # Custom signal with the count of checked items
    def __init__(self, data):
        super(MontagesTableModel, self).__init__()
        self._data = data

    def remove_by_filename(self, filename):
        self._data = self._data[self._data.Filename != filename]

    """ data function is called when showing the data in the table """
    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            value = self._data.iloc[index.row(), index.column()]
            return value

    """ setData function is called when editing the data """
    def setData(self, index, value, role):
        if role == QtCore.Qt.EditRole:
            if index.isValid():
                self._data.iat[index.row(),index.column()] = value
                # Emit the signal dataChanged even when only the channel selection is changed
                self.dataChanged.emit(index, index) 
                self.dataChangedWithCheckState.emit(self.checkedItemCount())  # Emit the custom signal
                return True
        return None

    """ rowCount Return the number of rows in the dataframe """
    def rowCount(self, index):
        return self._data.shape[0]

    """ columnCount Return the number of columns in the dataframe """
    def columnCount(self, index):
        return self._data.shape[1]-1 # -1 to skip the index column, we need to data internally, just not to show to the user

    """ headerData Return the label of each columns """
    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return str(self._data.columns[section])

    """
        flags Set the flags for each cell
        Set the first column as editable, others columns are simply enabled
    """
    def flags(self, index):
        if(index.column() == 0):
            return QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsEditable
        else:
            return QtCore.Qt.ItemIsEnabled

    def get_data(self):
        """ return the Data """
        return self._data

    def checkedItemCount(self):
        # Return the number of self._data["Use"] == True
        return sum(self._data["Use"])
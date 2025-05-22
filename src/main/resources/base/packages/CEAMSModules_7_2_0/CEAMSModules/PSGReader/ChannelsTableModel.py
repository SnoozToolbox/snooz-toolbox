"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    ChannelsTableModel
    Table model for the selection of channels
"""
from qtpy import QtCore

class ChannelsTableModel(QtCore.QAbstractTableModel):
    dataChangedWithCheckState = QtCore.Signal(int)  # Custom signal with the count of checked items
    def __init__(self, data):
        super(ChannelsTableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        """ data function is called when showing the data in the table """
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            value = self._data.iloc[index.row(), index.column()]
            return value

    def setData(self, index, value, role):
        """ setData function is called when editing the data """
        if role == QtCore.Qt.EditRole:
            if index.isValid():
                self._data.iat[index.row(),index.column()] = value
                # Emit the signal dataChanged even when only the channel selection is changed
                self.dataChanged.emit(index, index) 
                self.dataChangedWithCheckState.emit(self.checkedItemCount())  # Emit the custom signal
                return True
        return None

    def rowCount(self, index):
        """ rowCount Return the number of rows in the dataframe """
        return self._data.shape[0]

    def columnCount(self, index):
        """ columnCount Return the number of columns in the dataframe """
        return self._data.shape[1] # -1 to skip the index column, we need to data internally, just not to show to the user

    def headerData(self, section, orientation, role):
        """ headerData Return the label of each columns """
        # section is the index of the column/row.
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return str(self._data.columns[section])

    def flags(self, index):
        """
        flags Set the flags for each cell
        Set the first column as editable, others columns are simply enabled
        """
        if(index.column() == 0):
            return QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsEditable
        elif(index.column() == 1):
            return QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable
        else:
            return QtCore.Qt.ItemIsEnabled

    def remove_by_filename(self, filename):
        """ Remove all rows for a filename """
        self._data = self._data[self._data.Filename != filename]

    def get_data(self):
        """ return the Data """
        return self._data

    def checkedItemCount(self):
        # Return the number of self._data["Use"] == True
        return sum(self._data["Use"])
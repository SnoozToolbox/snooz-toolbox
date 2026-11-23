import numpy as np
import pandas as pd
from qtpy.QtCore import Qt, QAbstractTableModel
from qtpy.QtWidgets import QMessageBox
from widgets.WarningDialog import WarningDialog

# A custom model to show dataframe data on a QTableView 
#
# The word Abstract it meant to be subclassed
# QAbstractTableModel is from QAbstractItemModel
# 
class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data # DataFrame from pandas
        self.low_limit = None # Limit value to evaluate when the user edit the tableView
        self.high_limit = None # Limit value to evaluate when the user edit the tableView


    def get_data(self):
        return self._data


    def rowCount(self, parent=None):
        return self._data.shape[0]


    def columnCount(self, parnet=None):
        return self._data.shape[1]


    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            # Both roles to see the text while editing
            if role == Qt.DisplayRole or role == Qt.EditRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None


    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._data.columns[section]

            if orientation == Qt.Vertical:
                return self._data.index[section]
        return None


    # Needed to edit the field in the table view
    # otherwise user can only select the field without modifying it.
    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsEditable


    # called when data is edited from the tableView
    def setData(self, index, value, role):
        if role == Qt.EditRole:
            if index.isValid():
                # Update the current model 
                # To see the edited data on the table view
                if self.isfloat(value):
                    if (self.low_limit is not None) and (self.high_limit is not None):
                        if (float(value)>= self.low_limit) and (float(value)<= self.high_limit):
                            self._data.iat[index.row(), index.column()] = value
                            self.layoutChanged.emit()
                            return True
                        else:
                            error_message = f"The edited value {value} is outside the frequency bins available. Try again."
                            WarningDialog(error_message)
                            return False
                    else:
                        error_message = "Load a PSA file first to know the frequency bins available and try again."
                        WarningDialog(error_message)
                        return False
                else:
                    error_message = f"{value} is not a number! Try again."
                    WarningDialog(error_message)
                    return False
        return None


    def append_row(self, data):
        self._data = pd.concat([self._data ,data],ignore_index=True)


    def define_data(self, data):
        self._data = data


    def drop_row(self, index):
        self._data.drop(index=index, inplace=True)
        self._data.reset_index(inplace=True, drop=True)


    def isfloat(self,num):
        try:
            float(num)
            return True
        except ValueError:
            return False
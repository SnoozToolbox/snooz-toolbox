from datetime import datetime, timedelta

import pytz
import typing


from qtpy.QtCore import Qt, QAbstractTableModel, QModelIndex, QDateTime

class IdentificationModel(QAbstractTableModel):
    def __init__(self, id_data):
        super().__init__()
        self._id_data = id_data

        if self._id_data["birthdate"] is None:
            self._id_data["birthdate"] = None
        else:
            birthdate_datetime = datetime(1970, 1, 1) + timedelta(seconds=self._id_data["birthdate"])
            q_datetime = QDateTime(birthdate_datetime)
            q_datetime.setTimeSpec(Qt.UTC)
            self._id_data["birthdate"] = q_datetime

        creationdate_datetime = datetime.utcfromtimestamp(self._id_data["creation_date"])
        q_datetime = QDateTime(creationdate_datetime)
        q_datetime.setTimeSpec(Qt.UTC)
        self._id_data["creation_date"] = q_datetime

        self._header_data = ["Filename", "Id1", "Id2", "First name", "Last name", "Sex", "Birthdate", "Record date","Age", "Height", "Weight", "BMI", "Waistline", "Height unit", "Weight unit", "Waistline unit"]

    @property
    def id_data(self):
        return self._id_data

    @id_data.setter
    def id_data(self, value):
        self._id_data = value

    def rowCount(self, parent=QModelIndex()):
        return 1

    def columnCount(self, parent=QModelIndex()):
        return len(self._header_data)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole or role == Qt.ToolTipRole or Qt.EditRole:
            i = index.row()
            j = index.column()
            return list(self._id_data.values())[j]
        else:
            return None

    def setData(self, index: QModelIndex, value: typing.Any, role: int = ...) -> bool:
        if role ==  Qt.EditRole:
            i = index.row()
            j = index.column()
            key = list(self._id_data)[j]
            self._id_data[key] = value
            return True
        return super().setData(index, value, role)
        

    def flags(self, index):
        return Qt.ItemIsEnabled

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._header_data[section]
        else:
            return super().headerData(section, orientation, role)
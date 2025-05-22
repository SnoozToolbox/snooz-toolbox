import os
import typing

from qtpy.QtCore import Qt, QAbstractTableModel, QModelIndex

from CEAMSTools.SleepReport.Commons.FileItem import FileItem

class SleepReportModel(QAbstractTableModel):
    def __init__(self, pub_sub_manager):
        super().__init__()
        self._files = []
        self._pub_sub_manager = pub_sub_manager
        self._header_data = ["Filename", "Filepath", "Report Count", "Temporal Link Count"]

    @property
    def files(self):
        return self._files

    def update_reports_count(self):
        self.beginResetModel()
        for file in self._files:
            file.update_reports_count()
        self.endResetModel()

    def get_file_item_by_name(self, full_filename):
        for file_item in self._files:
            if file_item.full_filename == full_filename:
                return file_item
        return None

    def add_file(self, full_filename, id_data, events_data):
        self.beginResetModel()
        _, filename = os.path.split(full_filename)
        filedata = [filename, full_filename, 0,0]

        file = FileItem(filedata, id_data, events_data, self._pub_sub_manager)
        self._files.append(file)
        self.endResetModel()
        self.dataChanged.emit(QModelIndex(),QModelIndex())

    def remove_file(self, row):
        self.beginResetModel()
        self._files.pop(row)
        self.endResetModel()
        self.dataChanged.emit(QModelIndex(),QModelIndex())

    def get_id_model(self, row):
        return self._files[row].id_model

    def get_events_model(self, row):
        return self._files[row].events_model
    
    def get_temporal_links_model(self, row):
        return self._files[row].temporal_links_model

    def rowCount(self, parent=QModelIndex()):
        return len(self._files)

    def columnCount(self, parent=QModelIndex()):
        return len(self._header_data)

    def data(self, index, role=Qt.DisplayRole):
        # Show the full path for the tooltip of a filename
        if role == Qt.ToolTipRole and index.column() == 1:
            i = index.row()
            return self._files[i].data[0]
        if role == Qt.DisplayRole or role == Qt.ToolTipRole:
            i = index.row()
            j = index.column()
            return self._files[i].data[j]
        else:
            return None

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._header_data[section]
        else:
            return super().headerData(section, orientation, role)


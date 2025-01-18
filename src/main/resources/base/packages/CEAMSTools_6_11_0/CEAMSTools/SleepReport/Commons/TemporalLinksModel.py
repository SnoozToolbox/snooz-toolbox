"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *
import typing

class TemporalLinksModel(QAbstractTableModel):
    def __init__(self, file_item):
        super().__init__(None)
        self._temporal_links = []
        self._file_item = file_item
        self._reports = {}

    @property
    def temporal_links(self):
        return self._temporal_links

    def reports_count(self):
        count = 0
        for temporal_link in self.temporal_links:
            if temporal_link[0]:
                count = count + 1
        return count

    def unselect_all(self):
        self.beginResetModel()
        for i in range(len(self._temporal_links)):
            self._temporal_links[i][0] = False
        self.endResetModel()

    def on_add_report(self, report):
        report_label = self.report_to_string(report)
        self.beginResetModel()
        if report_label not in self._reports:
            self._reports[report_label] = report.copy()
            self._reports = dict(sorted(self._reports.items()))
            self.update_pairs()
        self.endResetModel()

    def on_modify_report(self, report, previous_name):
        report_label = self.report_to_string(report, previous_name)
        self.beginResetModel()
        if report_label in self._reports:

            # If the report name changed, remove the old one and create a new one
            if report["name"] != previous_name:
                # Remove the previous one
                del self._reports[report_label]
                self.remove_report_from_pairs(report, previous_name)
                
                # Add the new one
                report_label = self.report_to_string(report)
                self._reports[report_label] = report.copy()
                self._reports = dict(sorted(self._reports.items()))

                self.update_pairs()
            # If not, just update its data
            else:
                report_label = self.report_to_string(report)
                self._reports[report_label] = report.copy()

        self.endResetModel()
        self._file_item._pub_sub_manager.publish(self, "TemporalLinkStep.update_model", None)

    def on_remove_report(self, report):
        report_label = self.report_to_string(report)
        self.beginResetModel()
        if report_label in self._reports:
            del self._reports[report_label]
            self.remove_report_from_pairs(report)
        self.endResetModel()
        self._file_item._pub_sub_manager.publish(self, "TemporalLinkStep.update_model", None)

    def update_pairs(self):
        for idx, key in enumerate(self._reports):
            jdx = 0
            report1 = self._reports[key]
            while jdx < len(self._reports):
                if jdx != idx:
                    keys = list(self._reports)
                    report2 = self._reports[keys[jdx]]
                    # Is this pair already in the table?
                    if not self.is_in_table(report1, report2):
                        pair = [False, report1.copy(), report2.copy()]
                        self._temporal_links.insert(idx+jdx-1,pair)

                jdx = jdx + 1

    def is_in_table(self, report1, report2):
        report1_label = self.report_to_string(report1)
        report2_label = self.report_to_string(report2)
        for i in range(len(self._temporal_links)):
            r1_label = self.report_to_string(self._temporal_links[i][1])
            r2_label = self.report_to_string(self._temporal_links[i][2])
            if report1_label == r1_label and report2_label == r2_label:
                return True
        return False

    def remove_report_from_pairs(self, report, previous_name=None):
        i = len(self._temporal_links)-1
        report_label = self.report_to_string(report, previous_name)
        while i >=0:
            r1_label = self.report_to_string(self._temporal_links[i][1], previous_name)
            r2_label = self.report_to_string(self._temporal_links[i][2], previous_name)
            if report_label == r1_label or report_label == r2_label:
                del self._temporal_links[i]
            i = i - 1

    def report_to_string(self, report, report_name=None):
        if report['event_name'] is not None:
            if report_name is not None:
                return f"{report_name}:{report['group_name']}:{report['event_name']}"
            else:
                return f"{report['name']}:{report['group_name']}:{report['event_name']}"
        elif report['group_name'] is not None:
            if report_name is not None:
                return f"{report_name}:{report['group_name']}"
            else:
                return f"{report['name']}:{report['group_name']}"

        else:
            return None

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self._temporal_links)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 3

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        row = index.row()
        col = index.column()
        
        if not index.isValid():
            return None

        if row >= len(self._temporal_links):
            return None

        if (role == Qt.DisplayRole or role == Qt.ToolTipRole) and col != 0:
            report = self._temporal_links[row][col]
            report_label = self.report_to_string(report)
            return report_label
        elif role == Qt.CheckStateRole and col == 0:
             return Qt.Checked if self._temporal_links[row][col] else Qt.Unchecked
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False

        if role == Qt.CheckStateRole:
            self._temporal_links[index.row()][index.column()] = True if value == 2 else False
            self._file_item._pub_sub_manager.publish(self, "TemporalLinkStep.update_model", None)
            return True
        return False

    def add_temporal_link(self, temporal_link):
        self._temporal_links.append(temporal_link)
        index = self.createIndex(0,0)
        self.dataChanged.emit(index, index)

    def flags(self, index):
        flags = QAbstractTableModel.flags(self, index)
        if(index.column() == 0):
            flags = flags | Qt.ItemIsUserCheckable|Qt.ItemIsEditable|Qt.ItemIsEnabled
        else:
            flags = Qt.ItemIsEnabled

        return flags

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                value = ""
            elif section == 1:
                value = "1st report"
            elif section == 2:
                value = "2nd report"
            else:
                value = ""
            return value
        elif role == Qt.DisplayRole and orientation == Qt.Vertical:
            return None

    
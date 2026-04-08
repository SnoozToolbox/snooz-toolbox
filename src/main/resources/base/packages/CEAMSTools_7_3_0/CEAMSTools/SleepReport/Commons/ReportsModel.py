import typing

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

#from CEAMSTools.SleepReport.Commons.GroupItem import GroupItem
import CEAMSTools.SleepReport.Commons.GroupItem

class ReportsModel(QAbstractTableModel):
    add_report_signal = Signal(object)
    modify_report_signal = Signal(object, str)
    remove_report_signal = Signal(object)

    def __init__(self, parent_item, pub_sub_manager, file_item) -> None:
        super().__init__(None)
        self._reports = []
        self._parent_item = parent_item
        self._pub_sub_manager = pub_sub_manager
        self._file_item = file_item
        
        self.add_report_signal.connect(self._file_item.on_add_report)
        self.remove_report_signal.connect(self._file_item.on_remove_report)
        self.modify_report_signal.connect(self._file_item.on_modify_report)

    @property
    def reports(self):
        return self._reports

    def clear(self):
        self.remove_all_reports()

    def report_count(self):
        return len(self._reports)

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self._reports)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 11

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if not index.isValid():
            return None

        if role != Qt.DisplayRole and role != Qt.EditRole:
            return None
        
        keys = list(self._reports[index.row()])
        return self._reports[index.row()][keys[index.column()]]

    def setData(self, index, value, role=Qt.EditRole):

        if not index.isValid() or role != Qt.EditRole:
            return False

        keys = list(self._reports[index.row()])
        self._reports[index.row()][keys[index.column()]] = value
        self.dataChanged.emit(index, index)
        return True

    def find_report_by_name(self, report_name):
        for report in self._reports:
            if report['name'] == report_name:
                return report
        return None

    def add_report(self, report):
        # Create a list of dict ("events_definition") that represents each 
        # events within the group.
        #[( "group_name":group_name, 
        #   "event_name":event_name)]
        report = report.copy()
        report['events_definition'] = []

        group_name = self._parent_item.group_name

        # If the current item is a group.
        if not isinstance(self._parent_item, CEAMSTools.SleepReport.Commons.EventItem.EventItem):
            report['event_name'] = None
            report['group_name'] = group_name

             # Only if there are any events in the group.
            if self._parent_item.childCount() > 0:

                # For all events within the group
                for i in range(self._parent_item.childCount()):
                    parent_item = self._parent_item.child(i)
                    event_name = parent_item.event_name

                    # Overwrite the group_name when the group is a combined one
                    if parent_item.original_group_name is not None:
                        group_event_ch = {  "group_name":parent_item.original_group_name,
                                            "event_name":event_name}
                    else:
                        group_event_ch = {  "group_name":group_name,
                                            "event_name":event_name}
                    report['events_definition'].append(group_event_ch)

        # If this report is added to an event within a group
        else:
            parent_item = self._parent_item
            report['group_name'] = group_name
            event_name = parent_item.event_name
            report['event_name'] = event_name
            
            # Overwrite the group_name when the group is a combined one
            if parent_item.original_group_name is not None:
                group_event_ch = {  "group_name":parent_item.original_group_name,
                                    "event_name":event_name}
            else:
                event_group_name = group_name
                group_event_ch = {  "group_name":event_group_name,
                                    "event_name":event_name}
            report['events_definition'] = []
            report['events_definition'].append(group_event_ch)

        self._reports.append(report)
        self.add_report_signal.emit(report)
        index = self.createIndex(0,0)
        self.dataChanged.emit(index, index)
        return report

    def modify_report(self, reportToModify, previousName):
        for idx, report in enumerate(self._reports):
            if report['name'] == previousName:
                self._reports[idx] = reportToModify
                self.modify_report_signal.emit(reportToModify, previousName)
                index = self.createIndex(0,0)
                self.dataChanged.emit(index, index)

    def get_report(self, report_name):
        for report in self._reports:
            if report['name'] == report_name:
                return report
        return None
        
    def remove_report(self, report_name):
        report_index = 0
        for report in self._reports:
            if report['name'] == report_name:
                del self._reports[report_index]
                self.remove_report_signal.emit(report)
                index = self.createIndex(0,0)
                self.dataChanged.emit(index, index)
            report_index = report_index + 1

    def remove_all_reports(self):
        i = self.rowCount()-1
        while i >= 0:
            report = self._reports[i]
            self.remove_report(report['name'])
            i = i - 1


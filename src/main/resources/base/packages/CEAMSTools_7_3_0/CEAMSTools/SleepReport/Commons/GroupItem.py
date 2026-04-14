import typing

from qtpy.QtWidgets import QTreeWidgetItem
from qtpy.QtCore import Qt

from CEAMSTools.SleepReport.Commons.ReportsModel import ReportsModel

class GroupItem(QTreeWidgetItem):
    def __init__(self, group_name, file_item):
        super().__init__(None)
        self._group_name = group_name
        self._reports_model = ReportsModel(self, None, file_item)

    def data(self, column: int, role: int) -> typing.Any:
        if column == 2 and role == Qt.DisplayRole:
            return self._reports_model.report_count()
        return super().data(column, role)

    @property
    def event_count(self):
        return self.data(1, Qt.DisplayRole)

    @property
    def reports_model(self):
        return self._reports_model

    @property
    def group_name(self):
        return self._group_name

    def reports_count(self):
        count = 0
        for i in range(self.childCount()):
            child_item = self.child(i)
            count = count + child_item.reports_count()
        count = count + self._reports_model.report_count()
        return count

    def find_report_by_name(self, report_name):
        return self._reports_model.find_report_by_name(report_name)

    def add_report(self, report):
        report = self._reports_model.add_report(report)
        self.emitDataChanged()
        return report

    def remove_report(self, report_name):
        self._reports_model.remove_report(report_name)
        self.emitDataChanged()

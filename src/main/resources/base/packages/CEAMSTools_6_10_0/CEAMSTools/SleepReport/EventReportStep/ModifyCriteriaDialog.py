"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    ModifyCriteriaDialog
"""

from qtpy import QtWidgets, QtCore
from CEAMSTools.SleepReport.Commons.EventItem import EventItem

from CEAMSTools.SleepReport.EventReportStep.Ui_ModifyCriteriaDialog import Ui_ModifyCriteriaDialog

class ModifyCriteriaDialog(QtWidgets.QDialog, Ui_ModifyCriteriaDialog):
    """
        ModifyCriteriaDialog
    """
    on_ok_signal = QtCore.Signal(str, object, dict, object)
    on_ok_to_all_signal = QtCore.Signal(str, object, dict, object)

    def __init__(self, event_tree_item, row, previous_name, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        self._event_tree_item = event_tree_item
        self._report_model = event_tree_item.reports_model
        
        self._previous_name = previous_name
        self._creation_mode = previous_name is None

        # Adjust the ui if it's in creation or modification mode.
        if self._creation_mode:
            self.ok_pushbutton.setText("Add")
            self.ok_to_all_pushbutton.setText("Add to all files")
        else:
            self.ok_pushbutton.setText("Modify")
            self.ok_to_all_pushbutton.setText("Modify in all files")
            report = self._report_model.get_report(previous_name)
            self._events_definition = report['events_definition']
            self._event_name = report['event_name']
            self._group_name = report['group_name']

        if not self._creation_mode:
            self.report_criteria_mapper = QtWidgets.QDataWidgetMapper(self)
            self.report_criteria_mapper.setSubmitPolicy(QtWidgets.QDataWidgetMapper.SubmitPolicy.ManualSubmit)
            self.report_criteria_mapper.setModel(self._report_model)
            self.report_criteria_mapper.addMapping(self.report_name_lineedit,0)
            self.report_criteria_mapper.addMapping(self.duration_from_doublespinbox,1)
            self.report_criteria_mapper.addMapping(self.duration_to_doublespinbox,2)
            self.report_criteria_mapper.addMapping(self.interval_from_doublespinbox,3)
            self.report_criteria_mapper.addMapping(self.interval_to_doublespinbox,4)
            self.report_criteria_mapper.addMapping(self.minimum_count_spinbox,5)
            self.report_criteria_mapper.addMapping(self.end_period_after_doublespinbox,6)
            self.report_criteria_mapper.addMapping(self.se_from_doublespinbox,7)
            self.report_criteria_mapper.addMapping(self.se_to_doublespinbox,8)
            self.report_criteria_mapper.setCurrentIndex(row)
        self.report_name = None

    def on_cancel(self):
        self.close()

    def on_ok_to_all(self):
        # Get all data from the UI
        report_data = self._get_ui_data()

        # Set back the data from the original report
        if not self._creation_mode:
            report_data['events_definition'] = self._events_definition
            report_data['event_name'] = self._event_name
            report_data['group_name'] = self._group_name

        # Validate the name of the report
        if report_data["name"] != self._previous_name:
            success = self._validate_name()
            if not success:
                return
        
        # Get the target group name and event name
        group_name = self._event_tree_item.group_name
        event_name = None
        if isinstance(self._event_tree_item, EventItem):
            event_name = self._event_tree_item.event_name

        self.on_ok_to_all_signal.emit(group_name, event_name, report_data, self._previous_name)
        self.close()

    def on_ok(self):
        # Get all data from the UI
        report_data = self._get_ui_data()

        # Set back the data from the original report
        if not self._creation_mode:
            report_data['events_definition'] = self._events_definition
            report_data['event_name'] = self._event_name
            report_data['group_name'] = self._group_name

        # Validate the name of the report
        if report_data["name"] != self._previous_name:
            success = self._validate_name()
            if not success:
                return
        
        # Get the target group name and event name
        group_name = self._event_tree_item.group_name
        event_name = None
        if isinstance(self._event_tree_item, EventItem):
            event_name = self._event_tree_item.event_name

        # Call the callback and close the dialog
        self.on_ok_signal.emit(group_name, event_name, report_data, self._previous_name)
        self.close()

    def _validate_name(self):
        report_name = self.report_name_lineedit.text()

        # Check if the name is empty
        if report_name == '':
            msgBox = QtWidgets.QMessageBox()
            msgBox.critical(None,"Error","The name can't be empty.")
            return False
        
        # Check if the name is already in used
        report = self._report_model.find_report_by_name(report_name)

        if report is not None:
            msgBox = QtWidgets.QMessageBox()
            msgBox.critical(None,"Error","The name is already in used.")
            return False
        return True

    def _get_ui_data(self):
        # Get all data from the UI
        report_data = {}
        report_data["name"] = self.report_name_lineedit.text()
        report_data["min_duration"] = self.duration_from_doublespinbox.value()
        report_data["max_duration"] = self.duration_to_doublespinbox.value()
        report_data["min_interval"] = self.interval_from_doublespinbox.value()
        report_data["max_interval"] = self.interval_to_doublespinbox.value()
        report_data["min_count"] = self.minimum_count_spinbox.value()
        report_data["end_period_delay"] = self.end_period_after_doublespinbox.value()
        report_data["sleep_event_association_min"] = self.se_from_doublespinbox.value()
        report_data["sleep_event_association_max"] = self.se_to_doublespinbox.value()
        report_data["events_section"] = self.events_in_combobox.currentText()
        report_data["graphics"] = self.graphic_combobox.currentText()

        # Call the callback and close the dialog
        return report_data

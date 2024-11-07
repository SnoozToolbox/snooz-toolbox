"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    GenerateReportStep
"""

from qtpy import QtWidgets

from CEAMSTools.SleepReport.Commons import ContextConstants
from CEAMSTools.SleepReport.GenerateReportStep.Ui_GenerateReportStep import Ui_GenerateReportStep
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog


class GenerateReportStep( BaseStepView,  Ui_GenerateReportStep, QtWidgets.QWidget):
    """
        GenerateReportStep
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI1
        self.setupUi(self)

        self.output_prefix_identifier = "b23c561c-4201-448e-83ec-2c64a5f94e56"
        self.output_prefix_topic = f"{self.output_prefix_identifier}.constant"
        self.output_directory_identifier = "dda1783f-8192-42a2-b736-6602424f1e0a"
        self.output_directory_topic = f"{self.output_directory_identifier}.constant"

        self._sleep_report_id = "01b09d5b-0f48-4569-a4ec-075c11501985"
        self._sleep_report_csv_report_topic = f"{self._sleep_report_id}.csv_report"


    def load_settings(self):
        self._pub_sub_manager.publish(self, self.output_prefix_topic, "ping")
        self._pub_sub_manager.publish(self, self.output_directory_topic, "ping")
        self._pub_sub_manager.publish(self, self._sleep_report_csv_report_topic, "ping")


    def on_apply_settings(self):
        self._pub_sub_manager.publish(self, self.output_prefix_topic, self.prefix_lineedit.text())
        self._pub_sub_manager.publish(self, self.output_directory_topic, self.output_lineedit.text())
        self._pub_sub_manager.publish(self, self._sleep_report_csv_report_topic, 
            self.csv_report_checkbox.isChecked())


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if len(self.output_lineedit.text())==0:
            WarningDialog(f"The output file has to be defined by the user, see step '4-Generate Reports'.")
            return False
        return True            


    def on_topic_response(self, topic, message, sender):
        if topic == self.output_prefix_topic:
            self.prefix_lineedit.setText(message)
        if topic == self.output_directory_topic:
            self.output_lineedit.setText(message)
        if topic == self._sleep_report_csv_report_topic:
            self.csv_report_checkbox.setChecked(message)


    # Called when a value listened is changed
    # No body asked for the value (no ping), but the value changed and
    # some subscribed to the topic
    def on_topic_update(self, topic, message, sender):
        if topic == self._context_manager.topic:
            if message==ContextConstants.context_event_report_list: # key of the context dict
                self._update_report_list()

            if message==ContextConstants.context_temporal_links_report_list: # key of the context dict
                self._update_report_list()


    def _update_report_list(self):
        self.event_report_listwidget.clear()
        self.temporallinks_listwidget.clear()

        # Add all event reports
        items = self._context_manager[ContextConstants.context_event_report_list].items()
        self._add_report_to_list(items, self.event_report_listwidget)
        
        # Add all temporal link reports
        items = self._context_manager[ContextConstants.context_temporal_links_report_list].items()
        self._add_report_to_list(items, self.temporallinks_listwidget)
    

    def _add_report_to_list(self, items, widget):
        report_list = {}
        for _,reports in items:
            for report in reports:
                if report not in report_list:
                    report_list[report] = 1
                else:
                    report_list[report] = report_list[report] + 1

        for report, count in report_list.items():
            widget.addItem(f"{report} ({count})")


    def on_choose(self):
        file = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select output directory"))

        if file != '':
            self.output_lineedit.setText(file)


    def on_detailed_report(self):
        pass

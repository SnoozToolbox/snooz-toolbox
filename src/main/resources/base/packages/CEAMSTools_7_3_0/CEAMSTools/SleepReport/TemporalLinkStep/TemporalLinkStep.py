"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    TemporalLinkStep
"""

from qtpy import QtWidgets, QtCore

from CEAMSTools.SleepReport.Commons import ContextConstants
from CEAMSTools.SleepReport.Commons.FileErrorDialog import FileErrorDialog
from CEAMSTools.SleepReport.TemporalLinkStep.Ui_TemporalLinkStep import Ui_TemporalLinkStep
from CEAMSTools.SleepReport.InputFilesStep.InputFilesStep import InputFilesStep
from commons.BaseStepView import BaseStepView

class TemporalLinkStep( BaseStepView,  Ui_TemporalLinkStep, QtWidgets.QWidget):
    """
        TemporalLinkStep
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # init variables
        self._error_dialog = None
        self._current_filename = None
        
        self._temp_links_dict_id = "f141fb03-3258-4b0b-9ef4-d4af40d0b2d7"
        self._temp_links_dict_topic = f"{self._temp_links_dict_id}.dictionary"

        self._temp_links_id = "032fada6-d00a-4167-99ca-79f1d9cf9baa"
        self._temp_links_window_size_topic = f"{self._temp_links_id}.window_size"
        self._temp_links_csv_report_topic = f"{self._temp_links_id}.csv_report"

        self._update_model_topic = "TemporalLinkStep.update_model"
        self._pub_sub_manager.subscribe(self, self._update_model_topic)

        # Init context variables
        self._report_names = {}
        self._context_manager[ContextConstants.context_temporal_links_report_list] = self._report_names
        
    def load_settings(self):
        self._pub_sub_manager.publish(self, self._temp_links_dict_topic, "ping")
        self._pub_sub_manager.publish(self, self._temp_links_window_size_topic, "ping")
        self._pub_sub_manager.publish(self, self._temp_links_csv_report_topic, "ping")

    # Response to a ping
    def on_topic_response(self, topic, message, sender):
        if topic == self._temp_links_window_size_topic:
            self.analysis_window_lineedit.setText(message)
        if topic == self._temp_links_csv_report_topic:
            if isinstance(message, str):
                self.csv_reports_checkbox.setChecked(eval(message))
            elif isinstance(message, bool):
                self.csv_reports_checkbox.setChecked(message)
            else:
                print(f"TemporalLinkStep error. Value must be a string or a bool for: {self._temp_links_csv_report_topic}")
            
        if topic == self._temp_links_dict_topic:

            model = self.file_tableview.model()
            for filename, reports in message.items():
                file_item = model.get_file_item_by_name(filename)
                
                for report in reports:
                    for temporal_link in file_item.temporal_links_model.temporal_links:
                        if temporal_link[1] == report[1] and \
                            temporal_link[2] == report[2]:
                            temporal_link[0] = report[0]
            model.update_reports_count()
            self._update_context()

    def on_apply_settings(self):

        # Fill the dict to provide the temporal links info
        # keys are filenames
        # values are the temporal_link_report
        files = {}
        model = self.file_tableview.model()
        for idx in range(model.rowCount(QtCore.QModelIndex())):
            filename = model.files[idx].full_filename
            file_item = model.get_file_item_by_name(filename)

            temporal_links = []
            for temporal_link in file_item.temporal_links_model.temporal_links:
                if temporal_link[0]:
                    temporal_links.append(temporal_link.copy())
            if len(temporal_links) > 0:
                files[filename] = temporal_links

        self._pub_sub_manager.publish(self, self._temp_links_dict_topic, files)
        self._pub_sub_manager.publish(self, self._temp_links_window_size_topic, 
            self.analysis_window_lineedit.text())
        self._pub_sub_manager.publish(self, self._temp_links_csv_report_topic, 
            self.csv_reports_checkbox.isChecked())

    # Any request
    def on_topic_update(self, topic, message, sender):
        if topic == self._context_manager.topic:
            if message == ContextConstants.context_input_files:
                self.context = self._context_manager[ContextConstants.context_input_files]
                model = self.context["model"]
                self.file_tableview.setModel(model)
                model.dataChanged.connect(self.on_files_change)
                self.file_tableview.setColumnHidden(1, True)
                self.file_tableview.resizeColumnsToContents()
        if topic == self._update_model_topic:
            model = self.file_tableview.model()
            model.update_reports_count()
            self._update_context()


    def _update_context(self):
        self._report_names = {}
        model = self.file_tableview.model()

        # Unselect all reports for each files
        for i in range(len(model.files)):
            file_item = model.files[i]
            filename = file_item.full_filename
            self._report_names[filename] = []
            
            temporal_links = file_item.temporal_links_model.temporal_links

            for temporal_link in temporal_links:
                if temporal_link[0]:
                    report_1_label = file_item.temporal_links_model.report_to_string(temporal_link[1])
                    report_2_label = file_item.temporal_links_model.report_to_string(temporal_link[2])
                    report_label = f"{report_1_label} - {report_2_label}"
                    self._report_names[filename].append(report_label)
            
        self._context_manager[ContextConstants.context_temporal_links_report_list] = self._report_names


    def get_current_filename(self):
        return self._current_filename


    def clear_all_reports(self):
        model = self.file_tableview.model()

        # Unselect all reports for each files
        for i in range(len(model.files)):
            model.files[i].temporal_links_model.unselect_all()
            
        model.update_reports_count()
        self._update_context()


    def on_files_change(self, index1, index2):
        self.temporal_links_tableview.setModel(None)


    def on_file_selection_change(self):
        model = self.file_tableview.model()
        index = self.file_tableview.currentIndex()
        temporal_links_model = model.get_temporal_links_model(index.row())

        proxyModel = QtCore.QSortFilterProxyModel()
        proxyModel.setSourceModel(temporal_links_model)
        self.temporal_links_tableview.setModel(proxyModel)
        self.temporal_links_tableview.setSortingEnabled(True)
        self.temporal_links_tableview.sortByColumn(1, QtCore.Qt.AscendingOrder)

        header = self.temporal_links_tableview.horizontalHeader()
        header.setMinimumSectionSize(25)
        header.resizeSection(0,25)
        header.setSectionResizeMode(1,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2,QtWidgets.QHeaderView.Stretch)
        header.setStretchLastSection(True)

        self._current_filename = model.files[index.row()].full_filename

    def _get_file_item_by_filename(self, filename):
        '''Get a file item by its filename'''
        model = self.file_tableview.model()

        for i in range(len(model.files)):
            if filename == model.files[i].full_filename:
                return model.files[i]
        return None

    def on_apply_to_all(self):
        error_files = []
        model = self.file_tableview.model()

        # Get the source model
        filename = self.get_current_filename()
        file_item  = self._get_file_item_by_filename(filename)
        src_temporal_links_model = file_item.temporal_links_model

        # For each files
        for i in range(len(model.files)):
            filename = model.files[i].full_filename
            file_item = model.files[i]

            # If it's a different file than the source one.
            if file_item.temporal_links_model is not src_temporal_links_model:
                
                # Clear all previous selection
                for temporal_link in file_item.temporal_links_model.temporal_links:
                    temporal_link[0] = False

                # Replicate selection
                success = True
                for src_tempo_link in src_temporal_links_model.temporal_links:
                    
                    # Since everything has been reset to False, just copy the selection
                    # when it's at True
                    if src_tempo_link[0]:

                        # Find the corresponding pair of report and set it to True
                        found = False
                        for temporal_link in file_item.temporal_links_model.temporal_links:
                            if src_tempo_link[1] == temporal_link[1] and \
                               src_tempo_link[2] == temporal_link[2]:
                                temporal_link[0] = True
                                found = True
                                break
                        
                        # If the source pair is not found, this file is faulty.
                        if not found:
                            success = False

                    # When a temporal link isn't found, we log the filename but 
                    # continue anyway.
                    if not success:
                        if filename not in error_files:
                            error_files.append(filename)

        if len(error_files) > 0:

            if self._error_dialog is not None:
                self._error_dialog.close()

            self._error_dialog = FileErrorDialog(error_files)
            self._error_dialog.show()            
        
        model.update_reports_count()
        self._update_context()

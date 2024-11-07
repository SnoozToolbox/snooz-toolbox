"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    InputFilesStep
    TODO CLASS DESCRIPTION
"""
import os
import sys
from datetime import datetime, timedelta
from qtpy import QtWidgets, QtCore, QtGui
from qtpy.QtCore import QDateTime

from commons.BaseStepView import BaseStepView
from CEAMSModules.PSGReader.commons import Units, Sex
from CEAMSModules.PSGReader import commons
from CEAMSModules.PSGReader.PSGReaderManager import PSGReaderManager
from CEAMSTools.SleepReport.Commons import ContextConstants
from CEAMSTools.SleepReport.Commons.SleepReportModel import SleepReportModel
from CEAMSTools.SleepReport.InputFilesStep.Ui_InputFilesStep import Ui_InputFilesStep
from widgets.WarningDialog import WarningDialog

class InputFilesStep( BaseStepView,  Ui_InputFilesStep, QtWidgets.QWidget):
    """
        InputFilesStep
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # init variables
        self._identification_mapper = None
        self._file_context = None
        self._record_info_key = 'record_info'
        self._psg_reader_identifier = 'f2eccd70-fcb6-4ee8-bea8-76103e706827'
        self._psg_reader_files_topic = f"{self._psg_reader_identifier}.files"
        self._subject_info_dict_identifier = '5866b374-c3e8-4f07-8702-35abd46ce4b2'
        self._dict_subject_info_topic = f"{self._subject_info_dict_identifier}.dictionary"
        
        # init UI
        self.setupUi(self)

        # TODO
        # Fix the problem with the timezone.
        # The data from Harmonie and Xltek is set in a UTC timezone.
        # We need to convert it to local using EST timezone
        # Problem is that when the data comes from Xltek, there's sometime an offset
        # of 1 hour. It might be due to the daylight saving time.
        # Also, Dates from EDF are local and not in UTC we also need to take that into account.
        # Since the birthdate and creation_date isn't really important for the report
        # I put these invisible and go do something more productive...
        self.birthdate_timeedit.setVisible(False)
        self.label_5.setVisible(False)
        self.record_date_timeedit.setVisible(False)
        self.label_6.setVisible(False)

        # init model and context
        self._model = SleepReportModel(self._pub_sub_manager)
        self.file_tableview.setModel(self._model)
        self.file_tableview.setColumnHidden(2, True)
        self.file_tableview.setColumnHidden(3, True)
        selectionModel = self.file_tableview.selectionModel()
        selectionModel.selectionChanged.connect(self.on_file_selection_change)

        # Init EEG reader modules
        self._psg_reader_manager = PSGReaderManager()
        self._psg_reader_manager._init_readers()


    def load_settings(self):
        context = {
            "model":self._model
        }
        self._context_manager[ContextConstants.context_input_files] = context

        # Ask for the settings to the publisher to display on the SettingsView
        # The order is important, we need to load the files before loading it 
        # identification data.
        self._pub_sub_manager.publish(self, self._psg_reader_files_topic, 'ping')
        self._pub_sub_manager.publish(self, self._dict_subject_info_topic, 'ping')


    def on_apply_settings(self):
        # Fill input files data
        files = {}
        model = self.file_tableview.model()
        for idx in range(model.rowCount(QtCore.QModelIndex())):
            file_item = model.files[idx]
            files[file_item.full_filename] = None

        self._pub_sub_manager.publish(self, self._psg_reader_files_topic, files)

        # Fill file/identification dict
        identifications = {}
        model = self.file_tableview.model()
        for filename in files.keys():
            file_item = model.get_file_item_by_name(filename)
            identifications[filename] = file_item.id_model.id_data.copy()

            if isinstance(identifications[filename]["birthdate"], QDateTime):
                identifications[filename]["birthdate"] = identifications[filename]["birthdate"].toSecsSinceEpoch()

            if isinstance(identifications[filename]["creation_date"], QDateTime):
                identifications[filename]["creation_date"] = identifications[filename]["creation_date"].toSecsSinceEpoch()

            if self.deidentify_checkbox.checkState():
                identifications[filename]['first_name'] = ''
                identifications[filename]['last_name'] = ''
                identifications[filename]['birthdate'] = None

        self._pub_sub_manager.publish(self, self._dict_subject_info_topic, identifications)
        

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._psg_reader_files_topic:
            # message is a dict and the keys are the filenames
            for filename in message.keys():
                self._add_file(filename)
        if topic == self._dict_subject_info_topic:
            # message is a dict and the keys are the filenames
            model = self.file_tableview.model()
            for filename in message.keys():
                file_item = model.get_file_item_by_name(filename)
                file_item.id_model.id_data = message[filename]

                birthdate = datetime(1970, 1, 1) + timedelta(seconds=file_item.id_model.id_data["birthdate"])
                birthdate_datetime = QDateTime(birthdate)
                file_item.id_model.id_data["birthdate"] = birthdate_datetime

                creation_date = datetime(1970, 1, 1) + timedelta(seconds=file_item.id_model.id_data["creation_date"])
                creation_date_datetime = QDateTime(creation_date)
                file_item.id_model.id_data["creation_date"] = creation_date_datetime

    def on_file_selection_change(self):
        index = self.file_tableview.currentIndex()
        id_model = self._model.get_id_model(index.row())
        if self._identification_mapper is not None:
            self._identification_mapper.clearMapping()
        self._identification_mapper = QtWidgets.QDataWidgetMapper(self)
        self._identification_mapper.setModel(id_model)
        self._identification_mapper.addMapping(self.id1_lineedit, 1)
        self._identification_mapper.addMapping(self.id2_lineedit, 2)
        self._identification_mapper.addMapping(self.first_name_lineedit, 3)
        self._identification_mapper.addMapping(self.last_name_lineedit, 4)
        self._identification_mapper.addMapping(self.sex_combobox, 5)
        self._identification_mapper.addMapping(self.birthdate_timeedit, 6)
        self._identification_mapper.addMapping(self.record_date_timeedit, 7)
        self._identification_mapper.addMapping(self.age_spinbox, 8)
        self._identification_mapper.addMapping(self.height_doublespinbox, 9)
        self._identification_mapper.addMapping(self.weight_doublespinbox, 10)
        self._identification_mapper.addMapping(self.bmi_doublespinbox, 11)
        self._identification_mapper.addMapping(self.waistline_doublespinbox, 12)
        self._identification_mapper.addMapping(self.height_unit_combobox, 13)
        self._identification_mapper.addMapping(self.weight_unit_combobox, 14)
        self._identification_mapper.addMapping(self.waistline_unit_combobox, 15)

        self.first_name_lineedit.textChanged.connect(self._identification_mapper.submit)
        self.id1_lineedit.textChanged.connect(self._identification_mapper.submit)
        self.id2_lineedit.textChanged.connect(self._identification_mapper.submit)
        self.first_name_lineedit.textChanged.connect(self._identification_mapper.submit)
        self.last_name_lineedit.textChanged.connect(self._identification_mapper.submit)
        self.sex_combobox.currentTextChanged.connect(self._identification_mapper.submit)
        self.birthdate_timeedit.dateChanged.connect(self._identification_mapper.submit)
        self.record_date_timeedit.dateChanged.connect(self._identification_mapper.submit)
        self.age_spinbox.textChanged.connect(self._identification_mapper.submit)
        self.height_doublespinbox.textChanged.connect(self._identification_mapper.submit)
        self.weight_doublespinbox.textChanged.connect(self._identification_mapper.submit)
        self.bmi_doublespinbox.textChanged.connect(self._identification_mapper.submit)
        self.waistline_doublespinbox.textChanged.connect(self._identification_mapper.submit)
        self.height_unit_combobox.currentTextChanged.connect(self._identification_mapper.submit)
        self.weight_unit_combobox.currentTextChanged.connect(self._identification_mapper.submit)
        self.waistline_unit_combobox.currentTextChanged.connect(self._identification_mapper.submit)
        
        self._identification_mapper.toFirst()


    def _add_file(self, filename):
        file_item = self._model.get_file_item_by_name(filename)

        if file_item is None:
            success = self._psg_reader_manager.open_file(filename)
            if not success:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Could not open file")
                msg.setInformativeText("Format is not compatible.")
                msg.setWindowTitle("Error loading file")
                msg.exec()
                return
            id_data = self._psg_reader_manager.get_subject_info()
            events_data = self._psg_reader_manager.get_events()
            sleep_stages = self._psg_reader_manager.get_sleep_stages()

            if len(sleep_stages) == 0 or len(sleep_stages[sleep_stages["name"] != "9"]) == 0:
                WarningDialog(f"This file has not been scored and will be not added:{filename}")
            else:
                self._model.add_file(filename, id_data, events_data)
                self.file_tableview.resizeColumnsToContents()

    def on_add_files(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        dlg.setNameFilters(self._psg_reader_manager.get_file_extensions_filters())
        if dlg.exec_():
            filenames = dlg.selectedFiles()

            for filename in filenames:
                self._add_file(filename)


    def on_deidentify_change(self, checked):
        self.first_name_lineedit.setEnabled(not checked)
        self.last_name_lineedit.setEnabled(not checked)
        self.birthdate_timeedit.setEnabled(not checked)

    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        model = self.file_tableview.model()
        if model.rowCount(QtCore.QModelIndex()) == 0:
            WarningDialog(f"The files in the Input File Step is empty. You need to select at least one file.")
            return False
        return True

    def on_add_from_folder(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly) # Allows the user to select only directories (folders).
        # The non native QFileDialog supports only local files.
            # So it is better to use the native dialog instead to see athena
        # The native dialog does not support multiple folders selection in windows
            # Natus needs the option to select multiple folders
        if not sys.platform.startswith("darwin"):
            file_dialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        file_view = file_dialog.findChild(QtWidgets.QListView, 'listView')

        if file_view:
                file_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        f_tree_view = file_dialog.findChild(QtWidgets.QTreeView)
        if f_tree_view:
            f_tree_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        if file_dialog.exec():
            folders = file_dialog.selectedFiles()

            for folder in folders:
                filenames = self._psg_reader_manager.find_psg_within_folder(folder)
                for filename in filenames:
                    self._add_file(filename)

    def on_remove_file(self):
        if self._identification_mapper is not None:
            self._identification_mapper.clearMapping()

        index = self.file_tableview.currentIndex()
        filename = index.data(3)
        
        # Remove event reports related to this file and update the context
        reports = self._context_manager[ContextConstants.context_event_report_list]
        if filename in reports:
            del reports[filename]
        self._context_manager[ContextConstants.context_event_report_list] = reports

        # Remove temporal links reports related to this file and update the context
        reports = self._context_manager[ContextConstants.context_temporal_links_report_list]
        if filename in reports:
            del reports[filename]
        self._context_manager[ContextConstants.context_temporal_links_report_list] = reports

        self._model.remove_file(index.row())

        
    def get_current_filename(self):
        ind = self.file_tableview.currentIndex()
        return 
#! /usr/bin/env python3
"""
    InputFilesStep
    Step to open files .txt (csv) annotation files from EDFbrowser.
"""

from qtpy import QtWidgets, QtCore, QtGui

from CEAMSTools.ConvertEDFbrowser.Commons import ContextConstants
from CEAMSTools.ConvertEDFbrowser.InputFilesStep.Ui_InputFilesStep import Ui_InputFilesStep
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog
from widgets.TableDialog import TableDialog
import pandas as pd

class InputFilesStep(BaseStepView, Ui_InputFilesStep, QtWidgets.QWidget):
    """
        InputFilesStep
        Allows the opening of the file
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        self._csv_reader_master_identifier = "663cd8ee-9ca5-4956-9a4f-82561c6adadf"

        # To use the SettingsView of a plugin and interract with its fonctions
        module = self.process_manager.get_node_by_id(self._csv_reader_master_identifier)
        if module is None:
            print(f'ERROR module_id isn\'t found in the process:{self._csv_reader_master_identifier}')
        else:
            # To extract the SettingsView and add it to our Layout in the preset
            self.my_CsvReaderSettingsView = module.create_settings_view()
            self.my_CsvReaderSettingsView.file_filter = self.filter_input_files
            self.verticalLayout.addWidget(self.my_CsvReaderSettingsView)
            # _context_manager is inherited from the BaseStepView
            # it allows to share information between steps in the step-by-step interface
            # ContextManager is a dictionary that publish an update through the 
            # PubSubManager whenever a value is modified.
            self._context_manager[ContextConstants.context_files_event_names] = self.my_CsvReaderSettingsView
            self.my_CsvReaderSettingsView.model_updated_signal.connect(self.on_model_modified)


    # Slot created to receive the signal emitted from PSGReaderSettingsView when the files_model is modified
    @QtCore.Slot()
    def on_model_modified(self):
        self._context_manager[ContextConstants.context_files_event_names] = self.my_CsvReaderSettingsView     


    def load_settings(self):
        pass


    # Called when the user clic on RUN
    # Message are sent to the publisher   
    def on_apply_settings(self):
        pass


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if self.my_CsvReaderSettingsView.fileListWidget.count()==0:
            WarningDialog(f"Add a file to convert in the step '1-Input Files'")
            return False
        filelists = [self.my_CsvReaderSettingsView.fileListWidget.item(i).text() for i in range(self.my_CsvReaderSettingsView.fileListWidget.count())]
        results = self.validate_input_files(filelists)
        if results:
            self.show_file_errors(
                results,
                "The analysis cannot run because some input files are invalid. "
                "Please correct or remove the files listed below.",
            )
            return False
        return True


    def filter_input_files(self, filenames):
        """Reject invalid files before the reader publishes its updated models."""
        results = self.validate_input_files(filenames)
        if results:
            self.show_file_errors(
                results,
                "The files listed below were rejected and were not added. "
                "Please correct their format before adding them again.",
            )
        rejected_files = {result['file'] for result in results}
        return [filename for filename in filenames if filename not in rejected_files]


    def validate_input_files(self, filenames):
        """Check the EDFbrowser columns and values used by the annotation models and conversion."""
        results = []
        for filename in filenames:
            file_result = {'file': filename, 'errors': []}
            try:
                df = pd.read_csv(filename, sep='\t', usecols=['Onset', 'Duration', 'Annotation'])
                for idx, row in df.iterrows():
                    for column in ('Onset', 'Duration'):
                        if pd.isna(row[column]):
                            file_result['errors'].append(f"Row {idx}: {column} is NaN")
                        elif not isinstance(row[column], (int, float)):
                            file_result['errors'].append(
                                f"Row {idx}: {column} is not numeric (value: {row[column]})"
                            )
                    if pd.isna(row['Annotation']):
                        file_result['errors'].append(f"Row {idx}: Annotation is NaN")
                    elif not isinstance(row['Annotation'], str):
                        file_result['errors'].append(
                            f"Row {idx}: Annotation is not a string (value: {row['Annotation']})"
                        )
            except (OSError, UnicodeError, pd.errors.ParserError, ValueError) as error:
                file_result['errors'].append(f"Cannot read EDFbrowser annotations: {error}")
            if not file_result['errors']:
                item = self.my_CsvReaderSettingsView.create_file_item_name_group_list(filename, 'EDFbrowser')
                if not isinstance(item, QtGui.QStandardItem):
                    file_result['errors'].append(
                        "Cannot build the annotation model with the current reader settings."
                    )
            if file_result['errors']:
                results.append(file_result)
        return results


    def show_file_errors(self, results, message):
        details_df = pd.DataFrame(
            [(result['file'], "\n".join(result['errors'])) for result in results],
            columns=["File", "Errors"],
        )
        dialog = TableDialog(
            df=details_df,
            title="Invalid EDFbrowser files",
            message=message,
        )
        dialog.exec_()


    # Called when a value listened is changed
    # No body asked for the value (no ping), but the value changed and
    # some subscribed to the topic
    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        pass


    # Called when the user delete an instance of the plugin
    def __del__(self):
        pass

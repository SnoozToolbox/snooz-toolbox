#! /usr/bin/env python3
"""
    InputFilesStep
    TODO CLASS DESCRIPTION
"""

from qtpy import QtWidgets, QtCore

from CEAMSTools.ConvertEDFbrowser.Commons import ContextConstants
from CEAMSTools.ConvertEDFbrowser.InputFilesStep.Ui_InputFilesStep import Ui_InputFilesStep
from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog
from widgets.WarningDialogWithButtons import WarningDialogWithButtons
import pandas as pd
import re
import os

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
        # Validate the files in the file list to follow the EDFbrowser format
        filelists = [self.my_CsvReaderSettingsView.fileListWidget.item(i).text() for i in range(self.my_CsvReaderSettingsView.fileListWidget.count())]
        results = []
        time_pattern = re.compile(r'^\d{2}:\d{2}:\d{2}$')
        if len(filelists) != 0:
            for file in filelists:
                file_result = {'file': os.path.basename(file), 'errors': []}
                try:
                    df = pd.read_csv(file, sep = '\t', usecols = ['Onset', 'Duration', 'Annotation'])
                    # Check if all required columns are present
                    required_columns = {'Onset', 'Duration', 'Annotation'}
                    if not all(col in df.columns for col in required_columns):
                        missing_cols = required_columns - set(df.columns)
                        file_result['errors'].append(f"Missing columns: {missing_cols}")
                        results.append(file_result)
                        continue
                # Validate data types and content for each row
                    for idx, row in df.iterrows():
                        # Check Onset
                        if pd.isna(row['Onset']):
                            file_result['errors'].append(f"Row {idx}: Onset is NaN")
                        elif not isinstance(row['Onset'], (int, float)):
                            file_result['errors'].append(f"Row {idx}: Onset is not numeric (value: {row['Onset']})")
                        elif isinstance(row['Onset'], str) and time_pattern.match(str(row['Onset'])):
                            file_result['errors'].append(f"Row {idx}: Onset matches HH:MM:SS pattern ({row['Onset']})")
                        
                        # Check Duration
                        if pd.isna(row['Duration']):
                            file_result['errors'].append(f"Row {idx}: Duration is NaN")
                        elif not isinstance(row['Duration'], (int, float)):
                            file_result['errors'].append(f"Row {idx}: Duration is not numeric (value: {row['Duration']})")
                        elif isinstance(row['Duration'], str) and time_pattern.match(str(row['Duration'])):
                            file_result['errors'].append(f"Row {idx}: Duration matches HH:MM:SS pattern ({row['Duration']})")
                        
                        # Check Annotation
                        if pd.isna(row['Annotation']):
                            file_result['errors'].append(f"Row {idx}: Annotation is NaN")
                        elif not isinstance(row['Annotation'], str):
                            file_result['errors'].append(f"Row {idx}: Annotation is not a string (value: {row['Annotation']})")

                except FileNotFoundError:
                    file_result['errors'].append("File not found")
                except pd.errors.ParserError:
                    file_result['errors'].append("Failed to parse CSV (check file format or delimiter)")
                except ValueError as e:
                    file_result['errors'].append(f"Error reading columns: Usecols do not match columns, columns format expected but not found: ['Onset', 'Duration', 'Annotation']")
                except Exception as e:
                    file_result['errors'].append(f"Unexpected error: {str(e)}")
                
                if len(file_result['errors']) != 0:
                    results.append(file_result)

        if len(results) > 0:
            if WarningDialogWithButtons.show_warning(f"Some files do not follow the EDFbrowser format. Please verify.\nDetails:\n{results}"):
                return True
            else:
                return False

        return True      


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


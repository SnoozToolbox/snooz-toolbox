"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Settings viewer of the EDFAnnotationsReader plugin
"""
import os
from qtpy import QtWidgets

from CEAMSModules.EDFAnnotationsReader.Ui_EDFAnnotationsReaderSettingsView import Ui_EDFAnnotationsReaderSettingsView
from commons.BaseSettingsView import BaseSettingsView
from widgets.WarningDialog import WarningDialog

class EDFAnnotationsReaderSettingsView(BaseSettingsView, Ui_EDFAnnotationsReaderSettingsView, QtWidgets.QWidget):
    """
        EDFAnnotationsReaderView set the EDFAnnotationsReader settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._annot_files_topic = f'{self._parent_node.identifier}.annot_files'
        self._pub_sub_manager.subscribe(self, self._annot_files_topic)
        self._psg_files_topic = f'{self._parent_node.identifier}.psg_files'
        self._pub_sub_manager.subscribe(self, self._psg_files_topic)

        self.tableWidget_files.setColumnCount(1)
        self.tableWidget_files.setHorizontalHeaderLabels(['Annotations Filenames'])
        self.tableWidget_files.horizontalHeader().setStretchLastSection(True)
        self._annot_files = []

        self.tableWidget_psg_files.setColumnCount(1)
        self.tableWidget_psg_files.setHorizontalHeaderLabels(['PSG Filenames'])
        self.tableWidget_psg_files.horizontalHeader().setStretchLastSection(True)
        self._psg_files = []
        


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._annot_files_topic, 'ping')
        self._pub_sub_manager.publish(self, self._psg_files_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Open a warning message dialog when the length of self._psg_files and self._annot_files are different
        n_annot_files = len(self._annot_files)
        n_PSG_files = len(self._psg_files)
        if not n_annot_files==n_PSG_files:
            WarningDialog(f"The number of EDF+ annotations files ({n_annot_files}) is not matching PSG files ({n_PSG_files})")
        # Send the settings to the publisher for inputs to EDFAnnotationsReader
        self._pub_sub_manager.publish(self, self._annot_files_topic, str(self._annot_files))
        self._pub_sub_manager.publish(self, self._psg_files_topic, str(self._psg_files))
        

    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        # This will be called as a response to ping request.
        if topic == self._annot_files_topic:
            if not message == '':
                self._annot_files = eval(message)
                self.fill_annot_table()
            else:
                self._annot_files = []
        if topic == self._psg_files_topic:
            if not message == '':
                self._psg_files = eval(message)
                self.fill_psg_table()
            else:
                self._psg_files = []
        
        
   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._annot_files_topic)
            self._pub_sub_manager.unsubscribe(self, self._psg_files_topic)
            
        
    # Called when the user click on "Choose" in the SettingsView
    def choose_slot(self):
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, 
            'Open .edf files', 
            None, 
            '.EDF files (*.edf *.EDF)')
        if files != '':
            self._annot_files = files
            self.fill_annot_table()


    def choose_psg_slot(self):
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, 
            'Open .edf files', 
            None, 
            '.EDF files (*.edf *.EDF)')
        if files != '':
            self._psg_files = files
            self.fill_psg_table()
            

    # Called when the user click on "Clear" in the SettingsView
    def clear_slot(self):
        self.tableWidget_files.clearContents()
        self.tableWidget_psg_files.clearContents()
        self._annot_files = []
        self._psg_files = []


    def fill_psg_table(self):
        self.tableWidget_psg_files.setRowCount(len(self._psg_files))
        for row, filename in enumerate(self._psg_files):
            # extract the basename of the filename
            basename = os.path.basename(filename)
            self.tableWidget_psg_files.setItem(row, 0, QtWidgets.QTableWidgetItem(basename))    


    def fill_annot_table(self):
        self.tableWidget_files.setRowCount(len(self._annot_files))
        for row, filename in enumerate(self._annot_files):
            # extract the basename of the filename
            basename = os.path.basename(filename)
            self.tableWidget_files.setItem(row, 0, QtWidgets.QTableWidgetItem(basename))         
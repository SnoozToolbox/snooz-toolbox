"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Settings viewer of the SleepStagesImporter plugin
"""

from qtpy import QtWidgets

from CEAMSModules.SleepStagesImporter.Ui_SleepStagesImporterSettingsView import Ui_SleepStagesImporterSettingsView
from commons.BaseSettingsView import BaseSettingsView

class SleepStagesImporterSettingsView(BaseSettingsView, Ui_SleepStagesImporterSettingsView, QtWidgets.QWidget):
    """
        SleepStagesImporterView set the SleepStagesImporter settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Add the column label to the table 
        self.tableWidget_files.setColumnCount(1)
        self.tableWidget_files.setHorizontalHeaderLabels(['Filenames'])
        self.tableWidget_files.horizontalHeader().setStretchLastSection(True)
        self._files = []
        self._file_params = self.default_file_params()

        # Subscribe to the proper topics to send/get data from the node
        self._stages_files_topic = f'{self._parent_node.identifier}.stages_files'
        self._pub_sub_manager.subscribe(self, self._stages_files_topic)
        self._file_params_topic = f'{self._parent_node.identifier}.file_params'
        self._pub_sub_manager.subscribe(self, self._file_params_topic)
        

    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._stages_files_topic, 'ping')
        self._pub_sub_manager.publish(self, self._file_params_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to SleepStagesImporter
        self._pub_sub_manager.publish(self, self._stages_files_topic, self._files)
        # Read the UI and fill the file_params dict
        self._file_params = self.get_file_params()
        self._pub_sub_manager.publish(self, self._file_params_topic, self._file_params)
        

    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._stages_files_topic:
            if isinstance(message, str) and not message == '':
                self._files = eval(message)
            elif isinstance(message, list):
                self._files = message
            else:
                self._files = []
            self.fill_table_files()
        elif topic == self._file_params_topic:
            if isinstance(message, str) and not message == '':
                self._file_params = eval(message)
            elif isinstance(message, dict):
                self._file_params = message
            else:
                self._file_params = self.default_file_params()
            self.fill_stages_ui()
            
        
   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._stages_files_topic)
            self._pub_sub_manager.unsubscribe(self, self._file_params_topic)

    
    def choose_slot(self):
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, 
            'Open text files', 
            None, 
            'CSV Files (*.csv *.CSV);;Text Files (*.txt *.TXT);;TSV Files (*.tsv *.TSV);;All Files (*)')
        self._files = files
        if files != '':
            self.fill_table_files()
            

    def clear_slot(self):
        self.tableWidget_files.clearContents()
        self._files = []
            
        
    def fill_table_files(self):
        self.tableWidget_files.setRowCount(len(self._files))
        for row, filename in enumerate(self._files):
            self.tableWidget_files.setItem(row, 0, QtWidgets.QTableWidgetItem(filename))


    def default_file_params(self):
        file_params = {}
        file_params['sep'] = None
        file_params['n_rows_hdr'] = 0
        file_params['encoding'] = 'utf-8'
        file_params['column_stages'] = 1
        file_params['stages_sec'] = 30
        file_params['prefix_filename'] = ''
        file_params['suffix_filename'] = ''
        file_params['case_sensitive'] = True
        file_params['rename_values'] = {}
        file_params['rename_values']['0'] = 'W'
        file_params['rename_values']['1'] = 'N1'
        file_params['rename_values']['2'] = 'N2'
        file_params['rename_values']['3'] = 'N3'
        file_params['rename_values']['5'] = 'R'
        file_params['rename_values']['6'] = 'Mov'
        file_params['rename_values']['7'] = 'Tech'
        file_params['rename_values']['9'] = 'Unscored'
        return file_params


    def get_file_params(self):
        file_params = {}
        file_params['sep'] = self.comboBox_sep.currentText()
        if file_params['sep'] == 'None':
            file_params['sep'] = None
        file_params['encoding'] = self.comboBox_encoding.currentText()
        file_params['n_rows_hdr'] = int(self.spinBox_n_rows.value())
        file_params['column_stages'] = int(self.spinBox_colstage.value())
        file_params['stages_sec'] = int(self.comboBox_stage_s.currentText())
        file_params['prefix_filename'] = self.lineEdit_prefix.text()
        file_params['suffix_filename'] = self.lineEdit_suffix.text()
        file_params['case_sensitive'] = self.checkBox_case_sensitive.isChecked()
        file_params['rename_values'] = {}
        file_params['rename_values']['0'] = self.lineEdit_ori_0.text()
        file_params['rename_values']['1'] = self.lineEdit_ori_1.text()
        file_params['rename_values']['2'] = self.lineEdit_ori_2.text()
        file_params['rename_values']['3'] = self.lineEdit_ori_3.text()
        file_params['rename_values']['5'] = self.lineEdit_ori_5.text()
        file_params['rename_values']['6'] = self.lineEdit_ori_6.text()
        file_params['rename_values']['7'] = self.lineEdit_ori_7.text()
        file_params['rename_values']['9'] = self.lineEdit_ori_9.text()
        return file_params


    def fill_stages_ui(self):
        self.comboBox_sep.setCurrentText(str(self._file_params['sep']))
        self.spinBox_n_rows.setValue(self._file_params['n_rows_hdr'])
        self.comboBox_encoding.setCurrentText(str(self._file_params['encoding']))
        self.spinBox_colstage.setValue(self._file_params['column_stages'])
        self.comboBox_stage_s.setCurrentText(str(self._file_params['stages_sec']))
        self.lineEdit_prefix.setText(self._file_params['prefix_filename'])
        self.lineEdit_suffix.setText(self._file_params['suffix_filename'])
        self.checkBox_case_sensitive.setChecked(self._file_params['case_sensitive'])
        self.lineEdit_ori_0.setText(self._file_params['rename_values']['0'])
        self.lineEdit_ori_1.setText(self._file_params['rename_values']['1'])
        self.lineEdit_ori_2.setText(self._file_params['rename_values']['2'])
        self.lineEdit_ori_3.setText(self._file_params['rename_values']['3'])
        self.lineEdit_ori_5.setText(self._file_params['rename_values']['5'])
        self.lineEdit_ori_6.setText(self._file_params['rename_values']['6'])
        self.lineEdit_ori_7.setText(self._file_params['rename_values']['7'])
        self.lineEdit_ori_9.setText(self._file_params['rename_values']['9'])
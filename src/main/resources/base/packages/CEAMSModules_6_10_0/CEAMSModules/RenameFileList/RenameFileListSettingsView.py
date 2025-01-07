"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    Settings viewer of the RenameFileList plugin
"""

from qtpy import QtWidgets

from CEAMSModules.RenameFileList.Ui_RenameFileListSettingsView import Ui_RenameFileListSettingsView
from commons.BaseSettingsView import BaseSettingsView

class RenameFileListSettingsView(BaseSettingsView, Ui_RenameFileListSettingsView, QtWidgets.QWidget):
    """
        RenameFileListView set the RenameFileList settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        self.tableWidget_files.setColumnCount(1)
        self.tableWidget_files.setHorizontalHeaderLabels(['Filenames'])
        self.tableWidget_files.horizontalHeader().setStretchLastSection(True)
        self._files = []

        # Subscribe to the proper topics to send/get data from the node
        self._file_list_topic = f'{self._parent_node.identifier}.file_list'
        self._pub_sub_manager.subscribe(self, self._file_list_topic)
        self._prefix_topic = f'{self._parent_node.identifier}.prefix'
        self._pub_sub_manager.subscribe(self, self._prefix_topic)
        self._suffix_topic = f'{self._parent_node.identifier}.suffix'
        self._pub_sub_manager.subscribe(self, self._suffix_topic)
        self._n_char_to_keep_topic = f'{self._parent_node.identifier}.n_char_to_keep'
        self._pub_sub_manager.subscribe(self, self._n_char_to_keep_topic)
        self._pattern_to_rem_topic = f'{self._parent_node.identifier}.pattern_to_rem'
        self._pub_sub_manager.subscribe(self, self._pattern_to_rem_topic)
        self._ext_selection_topic = f'{self._parent_node.identifier}.ext_selection'
        self._pub_sub_manager.subscribe(self, self._ext_selection_topic)
        self._keep_original_file_topic = f'{self._parent_node.identifier}.keep_original_file'
        self._pub_sub_manager.subscribe(self, self._keep_original_file_topic)
        

    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._file_list_topic, 'ping')
        self._pub_sub_manager.publish(self, self._prefix_topic, 'ping')
        self._pub_sub_manager.publish(self, self._suffix_topic, 'ping')
        self._pub_sub_manager.publish(self, self._n_char_to_keep_topic, 'ping')
        self._pub_sub_manager.publish(self, self._pattern_to_rem_topic, 'ping')
        self._pub_sub_manager.publish(self, self._ext_selection_topic, 'ping')
        self._pub_sub_manager.publish(self, self._keep_original_file_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to RenameFileList
        self._pub_sub_manager.publish(self, self._file_list_topic, self._files)
        self._pub_sub_manager.publish(self, self._prefix_topic, str(self.prefix_lineedit.text()))
        self._pub_sub_manager.publish(self, self._suffix_topic, str(self.suffix_lineedit.text()))
        if self.checkBox_keep_all_char.isChecked():
            self._pub_sub_manager.publish(self, self._n_char_to_keep_topic, str(-1))
        else:
            self._pub_sub_manager.publish(self, self._n_char_to_keep_topic, self.spinBox_n_char_to_keep.value())
        self._pub_sub_manager.publish(self, self._pattern_to_rem_topic, str(self.pattern_to_rem_lineedit.text()))
        self._pub_sub_manager.publish(self, self._ext_selection_topic, str(self.ext_selection_lineedit.text()))
        self._pub_sub_manager.publish(self, self._keep_original_file_topic, str(int(self.checkBox_keep_original.isChecked())))
        

    def on_topic_update(self, topic, message, sender):
        pass

    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._file_list_topic:
            if isinstance(message, str) and not message == '':
                self._files = eval(message)
            else:
                self._files = []
            self.fill_file_table()
        if topic == self._prefix_topic:
            self.prefix_lineedit.setText(message)
        if topic == self._suffix_topic:
            self.suffix_lineedit.setText(message)
        if topic == self._n_char_to_keep_topic:
            if isinstance(message, str) and not message == '': message = int(message)
            if message == -1:
                self.checkBox_keep_all_char.setChecked(True)
            else:
                self.spinBox_n_char_to_keep.setValue(message)
        if topic == self._pattern_to_rem_topic:
            self.pattern_to_rem_lineedit.setText(message)
        if topic == self._ext_selection_topic:
            self.ext_selection_lineedit.setText(message)
        if topic == self._keep_original_file_topic:
            if isinstance(message, str) and not message == '':
                message = int(message)
            self.checkBox_keep_original.setChecked(message)
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._file_list_topic)
            self._pub_sub_manager.unsubscribe(self, self._prefix_topic)
            self._pub_sub_manager.unsubscribe(self, self._suffix_topic)
            self._pub_sub_manager.unsubscribe(self, self._n_char_to_keep_topic)
            self._pub_sub_manager.unsubscribe(self, self._pattern_to_rem_topic)
            self._pub_sub_manager.unsubscribe(self, self._ext_selection_topic)
            self._pub_sub_manager.unsubscribe(self, self._keep_original_file_topic)
            

    def choose_slot(self):
        # open a file dialog with many selections of extensions such as .xml, .tsv, .txt, .edf
        file_filter = 'All Files (*);; TSV Files (*.tsv, *.TSV);;Text Files (*.txt, *.TXT);;CSV Files (*.csv, *.CSV);;XML Files (*.xml, *.XML);;EDF Files (*.edf, *.EDF);;'
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, 
            'Open files, select the right extension', 
            None, 
            file_filter)
        
        self._files = files
        if files != '':
            self.fill_file_table()
            

    def clear_slot(self):
        self.tableWidget_files.clearContents()
        self._files = []


    def fill_file_table(self):
        self.tableWidget_files.setRowCount(len(self._files))
        for row, filename in enumerate(self._files):
            self.tableWidget_files.setItem(row, 0, QtWidgets.QTableWidgetItem(filename))     

    def keep_all_char_slot(self):
        if self.checkBox_keep_all_char.isChecked():
            self.spinBox_n_char_to_keep.setValue(-1)
            self.spinBox_n_char_to_keep.setEnabled(False)
        else:
            self.spinBox_n_char_to_keep.setEnabled(True)
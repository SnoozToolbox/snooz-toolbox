"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the DominoConverter plugin
"""
from qtpy import QtWidgets
import sys

from CEAMSModules.DominoConverter.Ui_DominoConverterSettingsView import Ui_DominoConverterSettingsView
from commons.BaseSettingsView import BaseSettingsView
from widgets.WarningDialog import WarningDialog

class DominoConverterSettingsView(BaseSettingsView, Ui_DominoConverterSettingsView, QtWidgets.QWidget):
    """
        DominoConverterView set the DominoConverter settings
    """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Subscribe to the proper topics to send/get data from the node
        self._folders_topic = f'{self._parent_node.identifier}.folders'
        self._pub_sub_manager.subscribe(self, self._folders_topic)
        self._log_file_topic = f'{self._parent_node.identifier}.log_filename'
        self._pub_sub_manager.subscribe(self, self._log_file_topic)

        self.folders = []


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._folders_topic, 'ping')
        self._pub_sub_manager.publish(self, self._log_file_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to DominoConverter
        self._pub_sub_manager.publish(self, self._folders_topic, str(self.folders_lineedit.text()))
        self._pub_sub_manager.publish(self, self._log_file_topic, str(self.lineEdit_logfilename.text()))
        

    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        if len(self.folders_lineedit.text())==0:
            WarningDialog(f"Add a folder to convert in the step '1-Input Folders'")
            return False      
        if len(self.lineEdit_logfilename.text())==0:
            WarningDialog(f"Define a file to save the conversion log warning message in the step '1-Input Folders")
            return False      
        return True      


    def on_topic_update(self, topic, message, sender):
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._folders_topic:
            self.folders_lineedit.setText(message)
        if topic == self._log_file_topic:
            self.lineEdit_logfilename.setText(message)
        

   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._folders_topic)
            self._pub_sub_manager.unsubscribe(self, self._log_file_topic)


    # Called when the user press Add Folder push button
    def add_folder_slot(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly) # Allows the user to select only directories (folders).
        # The non native QFileDialog supports only local files.
            # So it is better to use the native dialog instead to see athena
        # The native dialog does not support multiple folders selection in windows and macOS
            # Natus needs the option to select multiple folders
        file_dialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        file_view = file_dialog.findChild(QtWidgets.QListView, 'listView')
        if file_view:
            file_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        f_tree_view = file_dialog.findChild(QtWidgets.QTreeView)
        if f_tree_view:
            f_tree_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        if file_dialog.exec():
            self.folders = file_dialog.selectedFiles()
            self.folders_lineedit.setText(str(self.folders))
        

    # Called when the user press Browse Folder push button 
    def browse_log_slot(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, 
            'Save TSV file', 
            None, 
            'TSV (*.tsv)')
        if filename != '':
            self.lineEdit_logfilename.setText(filename)
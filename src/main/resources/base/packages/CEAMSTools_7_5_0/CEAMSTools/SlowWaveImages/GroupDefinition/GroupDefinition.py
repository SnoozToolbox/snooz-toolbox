#! /usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite 2024
See the file LICENCE for full license details.

    GroupDefinition
    The step to define the group of each PSG recording.
"""

from qtpy import QtWidgets, QtCore, QtGui
from qtpy.QtCore import Qt
import os

from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog

from CEAMSTools.SlowWaveImages.InputFilesStep.InputFilesStep import InputFilesStep
from CEAMSTools.SlowWaveImages.GroupDefinition.Ui_GroupDefinition import Ui_GroupDefinition
from CEAMSTools.SlowWaveImages.GroupDefinition.FileProxyModel import FileProxyModel


class GroupDefinition(BaseStepView, Ui_GroupDefinition, QtWidgets.QWidget):
    """
        GroupDefinition
        The step to define the group of each PSG recording.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Key is the filename and the value is the group label
        self.group_dict = {}

        # Define the header of the table view
        self.files_table_model = QtGui.QStandardItemModel(0, 2)
        self.files_table_model.setHeaderData(0, QtCore.Qt.Horizontal, 'Filename')
        self.files_table_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Group')
        self.files_table_model.setHorizontalHeaderLabels(["Filename", "Group"])
        # The proxy model allows to filter the view
        self.file_proxy_model = FileProxyModel(self)
        self.file_proxy_model.setSourceModel(self.files_table_model)
        self.file_proxy_model.setFilterKeyColumn(0) # col0: filename, col1:group label
        self.file_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.file_proxy_model.setRecursiveFilteringEnabled(False)
        self.tableView_group.setModel(self.file_proxy_model)
        # Extend the header width to fit the window
        self.tableView_group.resizeColumnsToContents() # extend the column width to fit the text in the self.tableView_group
        # Connect the itemChanged signal to the on_item_changed method
        self.files_table_model.itemChanged.connect(self.on_item_changed)

        self._sw_wave_pics_node = "34950575-1519-44e1-852d-a7720eead65f" # identifier for slow wave pics generator
        # Subscribe to the proper topics to send/get data from the node
        self._file_group_topic = f'{self._sw_wave_pics_node}.file_group'
        self._pub_sub_manager.subscribe(self, self._file_group_topic)

        
    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._file_group_topic, 'ping')


    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        if topic == self._context_manager.topic:
            if message == InputFilesStep.context_files_view:
                # Access to the PsgReaderSettingsView to access easily informations about the files
                self.reader_settings_view = self._context_manager[InputFilesStep.context_files_view]
                # Create the model for the checkable table, based on self.files_model
                self.files_table_model = self.update_table_model()


    def on_topic_response(self, topic, message, sender):
        if topic == self._file_group_topic:
            if isinstance(message, str) and not message=="":
                message = eval(message)
            if isinstance(message, dict):
                self.group_dict = message
            else:
                self.group_dict = {}
            # Create or update the model for the table view, based on self.files_model and self.group_dict
            self.files_table_model = self.update_table_model()


    def on_apply_settings(self):
        # Send the dictionary as an input to the PSGReader module
        self._pub_sub_manager.publish(self, self._file_group_topic, str(self.group_dict))


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.

        # Make sure that all the files have a group label defined
        # Verify that each file of the model has a group label defined
        for row in range(self.files_table_model.rowCount()):
            if len(self.files_table_model.item(row, 1).text())==0:
                WarningDialog(f"At least one recording has no group label defined, start looking at the file : {self.files_table_model.item(row, 0).text()} on the step '2-Group Definition'.")
                return False
        return True


    def update_table_model(self):
        # Create the model for the checkable table, based on self.reader_settings_view.files_model
        for filename in self.reader_settings_view.get_files_list(self.reader_settings_view.files_model):
            # Add in the table view self.tableView_group the files included in the reader_settings_view.files_model
            if filename in self.group_dict.keys():
                group = self.group_dict[filename]
            else:
                group = ""
                self.group_dict[filename] = group
            # Verify if the file is already in the model, find match of the filename
            matches = self.files_table_model.findItems(os.path.basename(filename),QtCore.Qt.MatchExactly)
            if len(matches)==0:
                # Add in the table view self.tableView_group the files included in the reader_settings_view.files_model
                file_item = QtGui.QStandardItem(os.path.basename(filename))
                file_item.setData(filename)
                group_item = QtGui.QStandardItem(group)
                # set the file item checkable
                file_item.setCheckable(True)
                # Set the group item as editable
                group_item.setEditable(True)
                self.files_table_model.appendRow([file_item, group_item])
            else:
                # Update the table view with the group label from self.group_dict
                group_item = self.files_table_model.item(matches[0].row(), 1)
                group_item.setText(group)
        # Update the group dict if files are removed
        upd_group_dict = self.group_dict.copy()
        file_2_rm = []
        for filename in self.group_dict.keys():
            if filename not in self.reader_settings_view.get_files_list(self.reader_settings_view.files_model):
                file_2_rm.append(filename)
                upd_group_dict.pop(filename)
        # Remove the file from the model for the table view
        self.files_table_model = self.remove_files(file_2_rm, self.files_table_model)
        self.group_dict = upd_group_dict
        # extend the column width to fit the text in the self.tableView_group
        self.tableView_group.resizeColumnsToContents()
        return self.files_table_model


    def remove_files(self, file_to_rem, model):
        # Pass through the files to remove row for each column
        column=0
        row_to_rem = []
        for filename in file_to_rem :
            file_item = model.findItems(os.path.basename(filename), flags=QtCore.Qt.MatchExactly, column=column)
            row_to_rem.append(file_item[0].row())
        # Remove the last first to avoid changing the index file
        row_to_rem.sort(reverse=True)
        for row in row_to_rem:
            model.removeRow(row)
        return model

    # Called when the user apply the group to all files selected
    def apply_group_slot(self):
        # Get the group to apply
        group_to_apply = self.lineEdit_group.text()
        # For each file
        for i in range(self.files_table_model.rowCount()):
            # If the file is selected
            if self.files_table_model.item(i, 0).checkState() == QtCore.Qt.Checked:
                # Get the filename
                filename = self.files_table_model.item(i, 0).data()
                # Set the text of the group item to the group to apply
                self.files_table_model.item(i, 1).setText(group_to_apply)
                # Update the group dict
                self.group_dict[filename] = group_to_apply
                # extend the column width to fit the text in the self.tableView_group
                self.tableView_group.resizeColumnsToContents()


    # Called when the user edit the search pattern
    def edit_search_slot(self):
        self.file_proxy_model.invalidate()
        search_pattern = self.lineEdit_search.text()
        self.file_proxy_model.set_files_search_pattern(search_pattern)


    # Called when the user check/unchecked the SelectAll checkbox
    def select_all_slot(self):
        # Check all the file items from the self.tableView_group if self.checkBox_SelectAll is checked
        if self.checkBox_SelectAll.isChecked():
            for i in range(self.file_proxy_model.rowCount()):
                # Get the index from the self.file_proxy_model
                proxy_index = self.file_proxy_model.index(i, 0)
                source_index = self.file_proxy_model.mapToSource(proxy_index)
                item_source = self.files_table_model.itemFromIndex(source_index)
                item_source.setCheckState(QtCore.Qt.Checked)
        else:
            for i in range(self.file_proxy_model.rowCount()):
                # Get the index from the self.file_proxy_model
                proxy_index = self.file_proxy_model.index(i, 0)
                source_index = self.file_proxy_model.mapToSource(proxy_index)
                item_source = self.files_table_model.itemFromIndex(source_index)
                item_source.setCheckState(QtCore.Qt.Unchecked)
        

    # Called when the user edit the group label directly in the tableView_group
    def on_item_changed(self, item):
        # find out if the item is the column 1 (group)
        index = self.files_table_model.indexFromItem(item)
        # Find out the row of the item
        row = index.row()
        # Extract the file item from the row
        file_item = self.files_table_model.item(row, 0)
        # Extract the filename from the file item
        filename = file_item.data()
        if item.column() == 1:
            self.group_dict[filename] = item.text()
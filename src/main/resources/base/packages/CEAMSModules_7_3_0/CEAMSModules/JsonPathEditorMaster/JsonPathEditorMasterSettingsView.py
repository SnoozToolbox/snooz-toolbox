"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    Settings viewer of the JsonPathEditorMaster plugin
"""

from qtpy import QtWidgets, QtCore, QtGui
import os
import re
import json
import ast

from CEAMSModules.JsonPathEditorMaster.Ui_JsonPathEditorMasterSettingsView import Ui_JsonPathEditorMasterSettingsView
from commons.BaseSettingsView import BaseSettingsView
from widgets.WarningDialog import WarningDialog
from widgets.WarningDialogWithButtons import WarningDialogWithButtons

DEBUG = False

class JsonPathEditorMasterSettingsView(BaseSettingsView, Ui_JsonPathEditorMasterSettingsView, QtWidgets.QWidget):
    """
        JsonPathEditorMasterView set the JsonPathEditorMaster settings
    """

    # To send a signal each time the self.files_model is modified
    # It allows to define QtCore.Slot() to do action each time the self.files_model is modified
    model_updated_signal = QtCore.Signal()

    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        #setup the model
        self.files_model = QtGui.QStandardItemModel(0,1)
        self.Files_listView.setModel(self.files_model)

        self.Add_from_folders_pushButton.clicked.connect(self.on_add_folder)
        self.Add_files_pushButton.clicked.connect(self.on_add)
        #self.Remove_pushButton.clicked.connect(self.Files_listView.removeItemWidget)
        self.Remove_pushButton.clicked.connect(self.clear_list_slot)

        self.Files_listView.selectionModel().currentChanged.connect(self.on_file_selected)

        self.SelectAll_pushButton.clicked.connect(self.select_all_items)
        self.selectAll_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+A"), self)
        self.selectAll_shortcut.activated.connect(self.select_all_items)
        self.Files_listView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        self.New_files_lineEdit.setPlaceholderText("Choose the folder that you want to save the new JSON files")
        self.Choose_pushButton.clicked.connect(self.select_save_folder)

        self.editable_model = None
        self.table_model = None
        self.per_file_original_paths = {}  # key: file_path, value: list of original paths
        self.per_file_edited_paths = {}  # key: file_path, value: list of edited paths
        self.per_file_mode = True  # True means per-file mode, False means select-all mode


        # Subscribe to the proper topics to send/get data from the node
        self._files_topic = f'{self._parent_node.identifier}.files'
        self._pub_sub_manager.subscribe(self, self._files_topic)

        self._path_mapping_topic = f'{self._parent_node.identifier}.path_mapping'
        self._pub_sub_manager.subscribe(self, self._path_mapping_topic)

        self._newfilespath_topic = f'{self._parent_node.identifier}.newfilespath'
        self._pub_sub_manager.subscribe(self, self._newfilespath_topic)

        self._suffix_topic = f'{self._parent_node.identifier}.suffix'
        self._pub_sub_manager.subscribe(self, self._suffix_topic)
    
    def validate_all_paths(self):
        """
        Validate paths only for the currently selected files.
        Returns a dictionary of file_path → missing original/edited paths.
        """
        missing_report = {}

        selected_indexes = self.Files_listView.selectedIndexes()
        selected_files = [self.files_model.data(index, QtCore.Qt.DisplayRole) for index in selected_indexes]

        for file_path in selected_files:
            originals = self.per_file_original_paths.get(file_path, [])
            edits = self.per_file_edited_paths.get(file_path, originals)  # fallback to original
            file_report = {
                "Missing Edited Paths": []
            }

            for new_path in edits:
                if not os.path.exists(new_path):
                    file_report["Missing Edited Paths"].append(new_path)

            if file_report["Missing Edited Paths"]:
                missing_report[file_path] = file_report

        return missing_report

    def get_all_path_mappings(self):
        """
        Returns a dictionary: {json_file_path: {original_path: edited_path, ...}, ...}
        Ensures latest UI edits are written back to per_file_edited_paths first.
        """
        path_mapping = {}

        if not self.table_model or not self.editable_model:
            return {}

        original_paths = [self.table_model.item(row, 0).text() for row in range(self.table_model.rowCount())]
        edited_paths = [self.editable_model.item(row, 0).text() for row in range(self.editable_model.rowCount())]

        if self.per_file_mode:
            # Update only the currently selected file
            current_index = self.Files_listView.currentIndex()
            if not current_index.isValid():
                return {}

            file_path = self.files_model.data(current_index, QtCore.Qt.DisplayRole)
            if not file_path:
                return {}

            self.per_file_edited_paths[file_path] = edited_paths

        else:
            # Select-all mode: apply edits to matching paths in all files
            for orig_path, edit_path in zip(original_paths, edited_paths):
                for file_path, orig_list in self.per_file_original_paths.items():
                    if orig_path in orig_list:
                        idx = orig_list.index(orig_path)
                        # Update only the matching path
                        if file_path not in self.per_file_edited_paths:
                            self.per_file_edited_paths[file_path] = orig_list.copy()
                        self.per_file_edited_paths[file_path][idx] = edit_path
                        break  # Apply to first matching file only

        # Build final path mapping
        for file_path in self.per_file_original_paths:
            originals = self.per_file_original_paths[file_path]
            edits = self.per_file_edited_paths.get(file_path, originals.copy())
            path_mapping[file_path] = {o: e for o, e in zip(originals, edits)}

        return path_mapping

        
    def select_save_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(
           None, 
            'Select folder', 
            '', 
            QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.DontResolveSymlinks)
        if folder:
            if not folder.endswith('/') and not folder.endswith('\\'):
                folder += '/'
            self.New_files_lineEdit.setText(folder)

    def store_current_edits(self):
        if (
            not hasattr(self, 'editable_model')
            or not hasattr(self, 'table_model')
            or self.editable_model is None
            or self.table_model is None):
            return  # Nothing to store
        
        if self.per_file_mode:
            # Save edits for currently selected file
            current_index = self.Files_listView.currentIndex()
            if not current_index.isValid():
                return

            file_path = self.files_model.data(current_index, QtCore.Qt.DisplayRole)
            if not file_path:
                return

            edited_paths = [
                self.editable_model.item(row, 0).text()
                for row in range(self.editable_model.rowCount())
            ]

            self.per_file_edited_paths[file_path] = edited_paths

        else:
            # In select-all mode: propagate merged edits back to each file
            current_mapping = {
                self.table_model.item(row, 0).text(): self.editable_model.item(row, 0).text()
                for row in range(self.editable_model.rowCount())
            }

            for file_path, original_paths in self.per_file_original_paths.items():
                existing_edits = self.per_file_edited_paths.get(file_path, original_paths.copy())
                updated_edits = []

                for orig_path in original_paths:
                    # Priority: merged view edit → existing edit → original
                    if orig_path in current_mapping:
                        updated_edits.append(current_mapping[orig_path])
                    else:
                        idx = original_paths.index(orig_path)
                        updated_edits.append(existing_edits[idx] if idx < len(existing_edits) else orig_path)

                self.per_file_edited_paths[file_path] = updated_edits

    def select_all_items(self):
        self.per_file_mode = False  # Enter select-all mode
        if hasattr(self, 'editable_model') and hasattr(self, 'table_model'):
            if self.editable_model is not None and self.table_model is not None:
                self.store_current_edits()

        merged_originals = []
        merged_edits = []
        seen_pairs = set()

        # Ensure all files are selected
        selection_model = self.Files_listView.selectionModel()
        selection = QtCore.QItemSelection()

        for row in range(self.files_model.rowCount()):
            index = self.files_model.index(row, 0)
            file_path = self.files_model.data(index, QtCore.Qt.DisplayRole)

            # Select this file in the QListView
            selection.select(index, index)

            # Ensure original paths are loaded
            if file_path not in self.per_file_original_paths:
                results = self.process_file(file_path)
                original_paths = [str(v) for _, v in results.items()]
                self.per_file_original_paths[file_path] = original_paths

            # Ensure edited paths are initialized
            if file_path not in self.per_file_edited_paths:
                self.per_file_edited_paths[file_path] = self.per_file_original_paths[file_path].copy()

            originals = self.per_file_original_paths[file_path]
            edits = self.per_file_edited_paths[file_path]

            for orig, edit in zip(originals, edits):
                if (orig, edit) not in seen_pairs:
                    seen_pairs.add((orig, edit))
                    merged_originals.append(orig)
                    merged_edits.append(edit)

        # Apply full selection to the view
        selection_model.select(selection, QtCore.QItemSelectionModel.Select)

        # Collect all original paths from all files
        all_originals = []
        for file_path, paths in self.per_file_original_paths.items():
            all_originals.extend(paths)

        # Check for duplicates
        duplicates = set([p for p in all_originals if all_originals.count(p) > 1])

        if duplicates:
            duplicate_list = '\n'.join(sorted(duplicates))
            WarningDialog(f"Some original paths are duplicated across JSON files.\n\n"
                f"This may cause confusion when viewing edits in select-all mode.\n\n"
                f"Duplicated folders:\n{duplicate_list}")
            return  # Optionally stop execution here
        
        # === Display original paths (left) ===
        temp_orig_model = QtGui.QStandardItemModel()
        temp_orig_model.setHorizontalHeaderLabels(["Original Paths"])
        for path in merged_originals:
            item = QtGui.QStandardItem(path)
            item.setEditable(False)
            item.setForeground(QtGui.QBrush(QtGui.QColor('#888888')))
            temp_orig_model.appendRow([item])
        self.Paths_tableView.setModel(temp_orig_model)
        self.Paths_tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # === Display edited paths (right, view-only) ===
        temp_edit_model = QtGui.QStandardItemModel()
        temp_edit_model.setHorizontalHeaderLabels(["New Paths (View Only)"])
        for orig, edit in zip(merged_originals, merged_edits):
            item = QtGui.QStandardItem(edit)
            item.setEditable(False)
            if edit == orig:
                font = item.font()
                font.setItalic(True)
                item.setFont(font)
                item.setForeground(QtGui.QBrush(QtGui.QColor('orange')))
            temp_edit_model.appendRow([item])
        self.New_paths_tableView.setModel(temp_edit_model)
        self.New_paths_tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # DO NOT assign to self.editable_model or self.table_model → avoids corrupting per-file logic



    def clone_model_as_editable(self, source_model):
        editable_model = QtGui.QStandardItemModel()
        editable_model.setHorizontalHeaderLabels(["New Paths (To be edited)"])

        for row in range(source_model.rowCount()):
            value_item = source_model.item(row, 0).clone()
            # Mark value as editable
            value_item.setEditable(True)
            value_item.setForeground(QtGui.QBrush())
            editable_model.appendRow([value_item])

        return editable_model


    def collect_paths(self, obj, found_paths):
        """
        Recursively collect all unique folder paths from keys and values in the JSON structure.
        Handles string paths, and also parses stringified lists/dicts.
        """
        folder_set = set()

        def is_path(s):
            return (
                isinstance(s, str)
                and re.search(r'(^[A-Za-z]:[/\\])|(^//[^/\\])|(^\\\\[^\\])', s)
            )

        def get_folder(s):
            s = s.replace('\\', '/')
            if not re.search(r'\.[a-zA-Z0-9]{2,4}$', os.path.basename(s)):
                return s.rstrip('/')
            return os.path.dirname(s).replace('\\', '/')

        def recurse(item):
            if isinstance(item, dict):
                for k, v in item.items():
                    recurse(k)
                    recurse(v)
            elif isinstance(item, list):
                for sub in item:
                    recurse(sub)
            elif isinstance(item, str):
                # Try to evaluate stringified structures
                try:
                    parsed = ast.literal_eval(item)
                    recurse(parsed)
                except (ValueError, SyntaxError):
                    if is_path(item):
                        folder_set.add(get_folder(item))
            elif is_path(item):
                folder_set.add(get_folder(item))

        recurse(obj)
        found_paths.extend(sorted(folder_set))

    def on_file_selected(self, current, previous):
        self.per_file_mode = True
        # Save edits from previously selected file
        if previous.isValid() and hasattr(self, 'editable_model') and getattr(self, 'per_file_mode', True):
            prev_path = self.files_model.data(previous, QtCore.Qt.DisplayRole)
            self.per_file_edited_paths[prev_path] = [
                self.editable_model.item(row, 0).text()
                for row in range(self.editable_model.rowCount())
            ]

        if not current.isValid():
            return

        file_path = self.files_model.data(current, QtCore.Qt.DisplayRole)
        if not file_path:
            return

        if file_path not in self.per_file_original_paths:
            results = self.process_file(file_path)
            original_paths = [str(value) for _, value in results.items()]
            self.per_file_original_paths[file_path] = original_paths
        else:
            original_paths = self.per_file_original_paths[file_path]

        edited_paths = self.per_file_edited_paths.get(file_path, original_paths)
        if len(edited_paths) != len(original_paths):
            edited_paths = original_paths.copy()
            self.per_file_edited_paths[file_path] = edited_paths

        orig_model = QtGui.QStandardItemModel()
        orig_model.setHorizontalHeaderLabels(["Original Paths"])
        for path in original_paths:
            item = QtGui.QStandardItem(path)
            item.setEditable(False)
            item.setForeground(QtGui.QBrush(QtGui.QColor('#888888')))
            orig_model.appendRow([item])
        self.Paths_tableView.setModel(orig_model)
        self.Paths_tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_model = orig_model

        edit_model = QtGui.QStandardItemModel()
        edit_model.setHorizontalHeaderLabels(["New Paths (To be edited)"])
        for orig, edit in zip(original_paths, edited_paths):
            item = QtGui.QStandardItem(edit)
            item.setEditable(True)
            if edit == orig:
                font = item.font()
                font.setItalic(True)
                item.setFont(font)
                item.setForeground(QtGui.QBrush(QtGui.QColor('orange')))
            edit_model.appendRow([item])
        self.New_paths_tableView.setModel(edit_model)
        self.editable_model = edit_model
        self.New_paths_tableView.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)


    def process_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            found_paths = []
            self.collect_paths(data, found_paths)
            return {i: path for i, path in enumerate(found_paths)}

    
    # Slot called when user wants to add folders
    def on_add_folder(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            'Select Folder Containing json Files',
            QtCore.QDir.homePath()
        )

        if folder_path:
            valid_extensions = ('json')
            file_list = [
                os.path.join(folder_path, f)
                for f in os.listdir(folder_path)
                if f.lower().endswith(valid_extensions)
            ]

            if not file_list:
               WarningDialog(f"No Valid Files. No json files found in the selected folder.")
               return

            for file_path in file_list:
                #self.Files_listView.addItem(file_path)
                # Later for better visualisation, we can only show the name of the file
                item = QtGui.QStandardItem(file_path)
                self.files_model.appendRow(item)

            self.model_updated_signal.emit()

    # Slot called when user wants to add files
    def on_add(self):
        filenames_add, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, 
            'Open json file', 
            None, 
            'JSON Files (*.json)')
        if filenames_add != '':
            # Fill the QListView
            for filename in filenames_add:
                #self.Files_listView.addItem(filename)
                # tree item : parent=file, child=name
                item = QtGui.QStandardItem(filename)
                self.files_model.appendRow(item) 
            # Generate a signal to inform that self.files_model has been updated
            self.model_updated_signal.emit() 

    def load_files_from_data(self, data, saved_path_map=None):
        """
        Load the list of JSON files into the view and optionally restore their original/edited path mappings.

        Args:
            data (list): List of file paths.
            saved_path_map (dict, optional): Dictionary of form:
                {
                    "file_path1": {
                        "original_path1": "edited_path1",
                        ...
                    },
                    ...
                }
        """
        self.files_model.clear()
        self.per_file_original_paths.clear()
        self.per_file_edited_paths.clear()
        self.Paths_tableView.setModel(None)
        self.New_paths_tableView.setModel(None)

        for file_path in data:
            item = QtGui.QStandardItem(file_path)
            self.files_model.appendRow(item)

            if saved_path_map and file_path in saved_path_map:
                # Restore from saved path mapping
                restored = saved_path_map[file_path]
                original_paths = list(restored.keys())
                edited_paths = list(restored.values())

                self.per_file_original_paths[file_path] = original_paths
                self.per_file_edited_paths[file_path] = edited_paths
            else:
                # Will be filled during selection
                self.per_file_original_paths[file_path] = []
                self.per_file_edited_paths[file_path] = []

        self.model_updated_signal.emit()


    def clear_list_slot(self):
        selected_indexes = self.Files_listView.selectedIndexes()
        if not selected_indexes:
            return

        # Get paths to remove
        paths_to_remove = [
            self.files_model.data(index, QtCore.Qt.DisplayRole)
            for index in selected_indexes
        ]

        # Remove from model (bottom-up)
        for index in sorted(selected_indexes, key=lambda x: x.row(), reverse=True):
            self.files_model.removeRow(index.row())

        # Remove from stored path dictionaries
        for path in paths_to_remove:
            self.per_file_original_paths.pop(path, None)
            self.per_file_edited_paths.pop(path, None)

        # Clear the table views if any displayed file is being deleted
        # Get the currently displayed file in table views
        current_index = self.Files_listView.currentIndex()
        current_file = None
        if current_index.isValid():
            current_file = self.files_model.data(current_index, QtCore.Qt.DisplayRole)

        # If current_file is missing or removed, clear the views
        if current_file is None or current_file in paths_to_remove:
            self.Paths_tableView.setModel(None)
            self.New_paths_tableView.setModel(None)
            self.table_model = None
            self.editable_model = None

        self.model_updated_signal.emit()


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self._pub_sub_manager.publish(self, self._files_topic, 'ping')
        self._pub_sub_manager.publish(self, self._path_mapping_topic, 'ping')
        self._pub_sub_manager.publish(self, self._suffix_topic, 'ping')
        self._pub_sub_manager.publish(self, self._newfilespath_topic, 'ping')


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save workspace"
        """
        # Send the settings to the publisher for inputs to JsonPathEditorMaster
        selected_indexes = self.Files_listView.selectedIndexes()

        '''if not selected_indexes:
           WarningDialog(f"No Selection", "Please select at least one file.")
           return'''

        selected_files = [self.files_model.data(index, QtCore.Qt.DisplayRole) for index in selected_indexes]
        # Send the full list to the backend
        self._pub_sub_manager.publish(self, self._files_topic, selected_files)

        self._pub_sub_manager.publish(self, self._path_mapping_topic, self.get_all_path_mappings())
        self._pub_sub_manager.publish(self, self._suffix_topic, str(self.Suffix_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._newfilespath_topic, str(self.New_files_lineEdit.text()))
        #self._pub_sub_manager.publish(self, self._newpaths_topic, str(self.newpaths_lineedit.text()))
        #self._pub_sub_manager.publish(self, self._newfilespath_topic, str(self.newfilespath_lineedit.text()))
        
    def on_topic_update(self, topic, message, sender):
        """ Only used in a custom step of a tool, you can ignore it.
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if DEBUG: print(f'JsonPathEditorSettingsView.on_topic_response:{topic} message:{message}')
        if topic == self._files_topic:
            self.load_files_from_data(message)  # No saved mappings
        elif topic == self._path_mapping_topic:
            self.saved_path_mapping = message  # Store temporarily
        elif topic == self._suffix_topic:
            self.Suffix_lineEdit.setText(message)
        elif topic == self._newfilespath_topic:
            self.New_files_lineEdit.setText(message)

        # After all topics responded, bind paths to files
        if hasattr(self, 'saved_path_mapping') and hasattr(self, 'files_model'):
            files = [self.files_model.data(self.files_model.index(i, 0), QtCore.Qt.DisplayRole)
                    for i in range(self.files_model.rowCount())]
            self.load_files_from_data(files, saved_path_map=self.saved_path_mapping)
            del self.saved_path_mapping  # Clean up


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._files_topic)
            self._pub_sub_manager.unsubscribe(self, self._path_mapping_topic)
            self._pub_sub_manager.unsubscribe(self, self._suffix_topic)
            self._pub_sub_manager.unsubscribe(self, self._newfilespath_topic)  

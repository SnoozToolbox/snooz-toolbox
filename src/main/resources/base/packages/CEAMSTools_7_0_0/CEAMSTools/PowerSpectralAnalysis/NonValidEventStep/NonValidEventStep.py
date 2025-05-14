"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    NonValidEventStep
    Step in the PSA interface to exclude non valid events for the PSA analysis.
    Doc to open and read to understand : 
    Model and item : QAbstractItemModel -> QStandardItemModel -> QStandardItem
    View : QAbstractItemView -> QTreeView
"""
import ast
import os
from qtpy import QtWidgets, QtCore, QtGui
from qtpy.QtCore import Qt

from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState
from widgets.WarningDialog import WarningDialog

from CEAMSTools.PowerSpectralAnalysis.InputFilesStep.InputFilesStep import InputFilesStep
from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.Ui_NonValidEventStep import Ui_NonValidEventStep
from CEAMSTools.PowerSpectralAnalysis.NonValidEventStep.EventsProxyModel import EventsProxyModel

DEBUG = True

class NonValidEventStep( BaseStepView,  Ui_NonValidEventStep, QtWidgets.QWidget):

    node_id_ResetSignalArtefact_0 = "97edecf3-ab9b-4e8e-8759-2f117ac54221" # to activate if the signal during artifact are reset
    node_id_Dictionary_group = "9d7a24dd-ef7b-47ab-81c1-2986d7462b0d" # select the list of group for the current filename
    node_id_Dictionary_name = "668f9ecf-9498-4bf6-85d8-7e73002c66a9" # select the list of name for the current filename
    
    """
        NonValidEventStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform "Reset Signal Interface" and "Discard Events" modules.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        self._node_id_ResetSignalArtefact_0 = self.node_id_ResetSignalArtefact_0 # to activate if the signal during artifact are reset
        self._node_id_Dictionary_group = self.node_id_Dictionary_group # select the list of group for the current filename
        self._node_id_Dictionary_name = self.node_id_Dictionary_name # select the list of name for the current filename

        # Subscribe to context manager for each node you want to talk to
        self._artefact_group_topic = f'{self._node_id_Dictionary_group}.dictionary'
        self._pub_sub_manager.subscribe(self, self._artefact_group_topic)
        self._artefact_name_topic = f'{self._node_id_Dictionary_name}.dictionary'
        self._pub_sub_manager.subscribe(self, self._artefact_name_topic)

        # Dict to keep track of selected events
        self.group_dict = {} # the key is the filename and the item a string of groups
        self.name_dict = {}  # the key is the filename and the item a string of names

        self.files_check_event_model = self.create_empty_files_model()
        self.event_proxy_model = EventsProxyModel(self)
        self.event_proxy_model.setSourceModel(self.files_check_event_model)
        self.event_proxy_model.setFilterKeyColumn(0) # col0: label, col1:count
        self.event_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.event_proxy_model.setRecursiveFilteringEnabled(False)

        if self._node_id_ResetSignalArtefact_0 is None : 
            self.reset_excl_event_checkBox.setChecked(False)
            self.reset_excl_event_checkBox.setEnabled(False)
        

    def init_models(self):
        # Access to the PsgReaderSettingsView to access easily informations about the files
        self.reader_settings_view = self._context_manager[InputFilesStep.context_files_view]
        # Extract the model (where the file information is stored) 
        #   To be aware of any change from the InputFiles Step
        self.files_model = self.reader_settings_view.files_model
        # Create the model for the checkable events tree, based on self.files_model
        self.files_check_event_model = self.update_checkable_model(self.files_check_event_model)
        # The model for the list of files is from the PsgReaderSettingsView
        self.file_listview.setModel(self.files_model)
        # The model for the events checkable is created locally
        self.event_treeview.setModel(self.event_proxy_model)
        # Connect selection changed signal from file list view
        self.file_listview.selectionModel().selectionChanged.connect(self.on_file_selected())
        self.event_treeview.expandAll()
        self.event_treeview.resizeColumnToContents(0)


    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView

        self._pub_sub_manager.publish(self, self._artefact_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._artefact_name_topic, 'ping')
        # self.group_dict and self.name_dict are updated from the pipeline.json

        if self._node_id_ResetSignalArtefact_0 is not None:
            self._pub_sub_manager.publish(self, self._node_id_ResetSignalArtefact_0+".get_activation_state", None)

        # Init the models and load the context manager
        self.init_models()
        if DEBUG:
            if not self._validate_model_from_ref(self.files_model, self.files_check_event_model):
                print("Model corrupted after the init_models in load_settings")
        
        # To read the local dicts in order to select the right events in the view.
        self._set_event_lst_to_view()
        if DEBUG:
            if not self._validate_model_from_ref(self.files_model, self.files_check_event_model):
                print("Model corrupted after the _set_event_lst_to_view in load_settings")
       
        # connect the checkbox state to the item selection
        #   Each time a user changes the event selection, the model 
        #   and the self.group_dict and self.name_dict are updated
        self.files_check_event_model.itemChanged.connect(self.on_item_changed)


    def on_topic_update(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            at any update, does not necessary answer to a ping.
            To listen to any modification not only when you ask (ping)
        """
        if topic==self._context_manager.topic:
            if message==InputFilesStep.context_files_view: # key of the context dict

                # Access to the PsgReaderSettingsView to access easily informations about the files
                self.reader_settings_view = self._context_manager[InputFilesStep.context_files_view]
                # Extract the model (where the file information is stored) 
                #   To be aware of any change from the InputFiles Step
                self.files_model = self.reader_settings_view.files_model
                # Update the model for the checkable events tree, based on modification made in self.files_model
                #   The checksate are not modified, only the files are added or removed.
                self.files_check_event_model = self.update_checkable_model(self.files_check_event_model)
                self.event_treeview.resizeColumnToContents(0)
                if DEBUG:
                    if not self._validate_model_from_ref(self.files_model, self.files_check_event_model):
                        print("Model corrupted after the update_checkable_model in on_topic_update")


    # Answer to a ping
    #  The UI or the properties are updated from the pipeline.json
    def on_topic_response(self, topic, message, sender):
        if self._node_id_ResetSignalArtefact_0 is not None:
            if topic == self._node_id_ResetSignalArtefact_0+".get_activation_state":
                if message==ActivationState.ACTIVATED:
                    self.reset_excl_event_checkBox.setChecked(True)
                if message==ActivationState.BYPASS:
                    self.reset_excl_event_checkBox.setChecked(False)
        if topic == self._artefact_group_topic:
            if isinstance(message,dict):
                self.group_dict = message
            elif isinstance(message,str):
                self.group_dict = ast.literal_eval(message)
            else:
                self.group_dict = {}
        if topic == self._artefact_name_topic:   
            if isinstance(message,dict):
                self.name_dict = message
            elif isinstance(message,str):
                self.name_dict = ast.literal_eval(message)
            else:
                self.name_dict = {}


    # Function to uncheck all groups and names.
    def on_reset_all_files(self):
        # Get the file list from the model
        n_files = len(self.reader_settings_view.get_files_list(self.files_check_event_model))
        # For each file of the list
        for i_file in range(n_files):
            file_index = self.files_check_event_model.index(i_file,0)
            # Set the CheckState to all groups and names of a file index selected
            #   set_check_state_file(index, check_state, model)
            #   and return the model updated
            self.files_check_event_model = self.reader_settings_view.set_check_state_file(\
                file_index, QtCore.Qt.CheckState.Unchecked, self.files_check_event_model)
        # Read the event group and name from the model and update the local dict           
        # 2 dictionaries :
        # - group dictionary where the key is the filename and the item a string of groups
        # - name dictionary where the key is the filename and the item a string of names
        self.group_dict, self.name_dict = self._store_event_dict()
        # Uncheck the Select all checkbox
        self.select_all_checkBox.setChecked(False)
        

    # Called when the user clicks on RUN or when the pipeline is saved
    # Message are sent to the publisher   
    def on_apply_settings(self):
        if self._node_id_ResetSignalArtefact_0 is not None:
            # Activate ResetSignalArtefact module if the excluded events signal is reset
            if self.reset_excl_event_checkBox.isChecked():
                self._pub_sub_manager.publish(self, self._node_id_ResetSignalArtefact_0\
                    +".activation_state_change", ActivationState.ACTIVATED)
            else:
                self._pub_sub_manager.publish(self, self._node_id_ResetSignalArtefact_0\
                    +".activation_state_change",ActivationState.BYPASS)
        # Read the event group and name from the model and update the local dict           
        # 2 dictionaries :
        # - group dictionary where the key is the filename and the item a string of groups
        # - name dictionary where the key is the filename and the item a string of names
        self.group_dict, self.name_dict = self._store_event_dict()
        # send dictionaries to appropriate modules
        self._pub_sub_manager.publish(self, self._artefact_group_topic, str(self.group_dict))
        self._pub_sub_manager.publish(self, self._artefact_name_topic, str(self.name_dict))


    # Called when the user finish editing the search_event line edit
    def search_pattern_slot(self):
        self.event_proxy_model.invalidate()
        search_pattern = self.search_lineEdit.text()
        self.event_proxy_model.set_groups_names_search_pattern(search_pattern)


    # To read the local dicts in order to select the right events in the view.
    def _set_event_lst_to_view(self):
        if len(self.group_dict)>0 and len(self.name_dict)>0:
            group_dict = self.group_dict
            name_dict = self.name_dict
            # For each opened file
            for file_key in self.group_dict:

                # Extract which event groups and names are selected
                group_lst = group_dict[file_key]
                group_lst = group_lst.split(',')
                name_list = name_dict[file_key]
                name_list = name_list.split(',')

                # Find in the model the index of current filename
                file_check_index = self.reader_settings_view.get_file_index(file_key, self.files_check_event_model)

                # Set the CheckState to events listed in group_lst and name_list
                #   and returns evt_found_tab (array of number of events)
                #   usage : set_check_state_list(files_check_model, file_index, group_lst, name_list, check_state)
                    # files_check_model : QtGui.QStandardItemModel
                    # file_index : QtCore.QModelIndex
                    # group_lst : list of string 
                    # name_list : list of string
                    # check_state : QtCore.Qt.CheckState
                self.files_check_event_model, evt_found_tab = self.reader_settings_view.set_check_state_list(\
                    self.files_check_event_model, file_check_index, group_lst, name_list, QtCore.Qt.CheckState.Checked)


    # To read and save locally the selected events in the files_check_event_model
    #   in order to send the information to the dictionary modules in the pipeline
    def _store_event_dict(self):       
        # Clean the local dictionary 
        group_dict = {}
        name_dict = {}
        # Get the file list from the model
        files_list = self.reader_settings_view.get_files_list(self.files_check_event_model)
        n_files = len(files_list)
        # For each file of the list
        for i_file in range(n_files):
            filename = files_list[i_file]
            file_checkable_index = self.reader_settings_view.get_file_index(filename, self.files_check_event_model)
            # # If the file is new and will be added in the model
            # if isinstance(file_checkable_index, list) and len(file_checkable_index)==0:
            #     group_dict[filename] = 'None'  # letting the field empty '' does not work
            #     name_dict[filename] = 'None'   # letting the field empty '' does not work
            if isinstance(file_checkable_index, QtCore.QModelIndex):
                # group_lst and name_list are list of string 
                group_list, name_list = self.reader_settings_view.get_checked_event_lst_from_file(\
                    self.files_check_event_model, file_checkable_index)
                if len(group_list)>0:
                    # Construct the 2 local dicts: the key is the filename and the value is a string of groups or names
                    group_dict[filename] = ",".join(group_list) # string : groups separated by a comma
                    name_dict[filename] =  ",".join(name_list) # string : names separated by a comma
                else:
                    group_dict[filename] = 'None' # letting the field empty '' does not work
                    name_dict[filename] = 'None'  # letting the field empty '' does not work
            # else:
            #     raise NodeRuntimeException(self.identifier, "_store_event_dict", \
            #         f"NonValidEventStep : the selected index is not valid")

        return group_dict, name_dict


    # Called when the user checked\unchecked a group or a name
    # The input parameter item is the one changed
    def on_item_changed(self, item):
        # If a file item, do nothing
        if item.data() is None:
            # Disconnect the signal the time the states are analyzed and updated
            self.files_check_event_model.itemChanged.disconnect(self.on_item_changed)
            # If the user check/uncheck an event group propagate the state to children
            if item.hasChildren():
                self.files_check_event_model = self.reader_settings_view.apply_state_to_child_item(\
                    item, self.files_check_event_model)
            # If the user check/uncheck an event name, 
            #   look the other names and propagate to the group
            else:
                item.setAutoTristate(False)
                # Set the parent state depending of children
                self.files_check_event_model = self.reader_settings_view.apply_state_to_parent_item(\
                    item, self.files_check_event_model)
            # Update the self.group_dict and self.name_dict
            self.group_dict, self.name_dict = self._store_event_dict()
            # Connect the signal to listen to modification
            self.files_check_event_model.itemChanged.connect(self.on_item_changed)
        if DEBUG :
            if not self._validate_model_from_ref(self.files_model, self.files_check_event_model):
                print("Model corrupted after the on_item_changed")


    # Called when the user select a file in the PSG Files list
    def on_file_selected(self):
        # Extract files index selected on file_listview
        indexes = self.file_listview.selectedIndexes()
        files = []
        for index in indexes:
            files.append(self.files_model.itemFromIndex(index))
        filenames = [f.data(Qt.UserRole + 1) for f in files]
        if len(filenames)>0:
            self.event_proxy_model.set_filenames_filters(filenames)
        # The model for the events checkable is created locally
        self.event_treeview.setModel(self.event_proxy_model) 
        self.event_treeview.expandAll()
        self.event_treeview.resizeColumnToContents(0)


    # Find the tree view index linked to the list view index
    def find_checkable_index(self, file_list_index):
        # Extract filename
        filename = file_list_index.data(Qt.UserRole + 1)
        # Get the file index for the self.files_check_event_model model
        file_check_item = self.files_check_event_model.findItems(\
            os.path.basename(filename), flags=QtCore.Qt.MatchExactly, column=0)
        if len(file_check_item)>0:
            index = file_check_item[0].index()
            if isinstance(index, list):
                index = index[0]
        else:
            index = file_check_item
        return index


    # When the user checked/unchecked "Select all"
    def on_select_all_groups(self):
        # Extract how many event groups or names are available
        # Need to extract info from the proxy model since only the visible group or names has been selected all
        # How many rows available at the file_model pointer
        indexes = self.file_listview.selectedIndexes()
        if len(indexes)==0:
            WarningDialog(f"You need to select files (from the PSG Files list) before 'selecting all'.")
        for file_index in indexes:
            proxy_index = self.event_proxy_model.mapFromSource(self.find_checkable_index(file_index))
            self.set_check_state_file_via_proxy(proxy_index, self.select_all_checkBox.checkState())
        # Read the event group and name from the model and update the local dict           
        # 2 dictionaries :
        # - group dictionary where the key is the filename and the item a string of groups
        # - name dictionary where the key is the filename and the item a string of names
        self.group_dict, self.name_dict = self._store_event_dict()
            

    def set_check_state_file_via_proxy(self, file_index, check_state):
        """
       Set the CheckState to all names displayed of a file index selected
        
        Parameters
        -----------
            file_index : QtCore.QModelIndex
            check_state : QtCore.Qt.CheckState
        """
        n_groups = self.event_proxy_model.rowCount(file_index)
        for group_row in range(n_groups):
            group_index = self.event_proxy_model.index(group_row, 0, file_index)
            source_index = self.event_proxy_model.mapToSource(group_index)
            # for each child, set the check state
            n_names = self.event_proxy_model.rowCount(group_index)
            for name_row in range(n_names):
                name_index = self.event_proxy_model.index(name_row, 0, group_index)
                source_index = self.event_proxy_model.mapToSource(name_index)
                name_item = self.files_check_event_model.itemFromIndex(source_index)
                name_item.setCheckState(check_state)
            

    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._artefact_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._artefact_name_topic)


    # Update the model for the checkable events tree, based on modification made in self.files_model
    #   The checksate are not modified, only the files are added or removed.
    def update_checkable_model(self, checkable_model_outdated):
        if checkable_model_outdated == None:
            # Create checkable item based on self.reader_settings_view.files_model
            #   events are not checked at this point
            files_check_event_model = self.reader_settings_view.create_files_model_checkable(self.files_model)
        else:
            # Add and remove only the modified file
            updated_file_list = self.reader_settings_view.get_files_list(self.files_model)
            outdated_file_list = self.reader_settings_view.get_files_list(checkable_model_outdated)
            # Finding missing filename in the outdated_file_list
            file_to_rem = [outdated_file for outdated_file in outdated_file_list if outdated_file not in updated_file_list]
            # pass through the new list of files and add the new files into the checkable_model_outdated
            for filename in updated_file_list:
                file_item = self.reader_settings_view.get_file_item(filename, checkable_model_outdated)
                # If it is a new file -> add it
                if isinstance(file_item, list) and len(file_item)==0:
                    # Make the file item children checkable and checked (file item is copied from self.files_model)
                    # Copy a file item as parent and make its children checkable and checked : group and count, name and count.
                    # tree item : parent=file, child=group and count, child=name and count
                    item = self.reader_settings_view.make_checkable_file_item_count(filename, self.files_model)
                    checkable_model_outdated.appendRow(item)
                # Otherwise -> nothing to do
            # remove the files from checkable_model_outdated
            if len(file_to_rem):
                checkable_model_outdated = self.remove_files(file_to_rem, checkable_model_outdated)
            files_check_event_model = checkable_model_outdated
        return files_check_event_model


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
        if DEBUG : 
            if not self._validate_model_from_ref(self.files_model, model):
                print("Model corrupted in remove_files")
        return model


    # Create an empty model based with the column Group-Name and Count
    def create_empty_files_model(self):
        files_model = QtGui.QStandardItemModel(0, 2)
        files_model.setHeaderData(0, QtCore.Qt.Horizontal, 'Group-Name')
        files_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Count')
        files_model.setHorizontalHeaderLabels(['Group-Name', 'Count'])
        return files_model


    # Function to evaluate the validity of the model
    # This debug function is helpuful to find out when the model is corrupted
    def _validate_model_from_ref(self, master_model, model_to_validate):
        n_files = master_model.rowCount()
        for i_file in range(n_files):
            filename = master_model.item(i_file, 0).text()
            # get the file index
            file_index_ref = self.reader_settings_view.get_file_index(filename, master_model)
            file_index_test = self.reader_settings_view.get_file_index(filename, model_to_validate)
            n_groups = master_model.rowCount(file_index_ref)
            for i_group in range(n_groups):
                group_index_ref = master_model.index(i_group, 0, file_index_ref)
                group_item_ref = master_model.itemFromIndex(group_index_ref)
                group_index_test = model_to_validate.index(i_group, 0, file_index_test)
                group_item_test = model_to_validate.itemFromIndex(group_index_test)
                if not (group_item_ref.text() == group_item_test.text()):
                    print(f"{filename} : reference group {group_item_ref.text()} is different in checkable model = {group_item_test.text()}")
                    return False                   
                n_names = master_model.rowCount(group_index_ref)
                for i_name in range(n_names):
                    name_index_ref = master_model.index(i_name, 0, group_index_ref)
                    name_item_ref = master_model.itemFromIndex(name_index_ref)
                    name_index_test = model_to_validate.index(i_name, 0, group_index_test)
                    name_item_test = model_to_validate.itemFromIndex(name_index_test)
                    if not (name_item_ref.text() == name_item_test.text()):
                        print(f"{filename} : reference name {name_item_ref.text()} is different in checkable model = {name_item_test.text()}")
                        return False
        return True
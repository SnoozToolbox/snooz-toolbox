"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    StadeSelection
    Step in the EDFbrowser converter interface to select the stage annotations and define the proper group event.
"""
import numpy as np
import os
import pandas as pd
from qtpy import QtWidgets, QtCore
from qtpy.QtCore import Qt
from qtpy import QtGui

from commons.BaseStepView import BaseStepView
from widgets.TableDialog import TableDialog
from widgets.WarningDialog import WarningDialog

from CEAMSTools.ConvertEDFbrowser.Commons import ContextConstants # Import the keys for the context
from CEAMSTools.ConvertEDFbrowser.StadeSelection.Ui_StadeSelection import Ui_StadeSelection # UI
from CEAMSTools.ConvertEDFbrowser.Commons.EventsProxyModel import EventsProxyModel # To filter events on the UI

class StadeSelection( BaseStepView,  Ui_StadeSelection, QtWidgets.QWidget):

    # These variables are defined outside the constructor to be more easily overwrite
    #  when the StadeSelection is being inherited. I.e. ArtifactSelection Step
    event_group = 'stage'                                           # The group label to add
    context_event_sel_def = ContextConstants.context_stage_check_model # The key of the context

    """
        StadeSelection
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform the group dictionary to add or modify group to events.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Model of events checked (selected for sleep stages)
        self.files_check_event_model = self.create_empty_files_model()
        self.file_editable_model = self.create_empty_files_model()

        # -----------------------------------------------------------------------------------
        # Init the context
        # -----------------------------------------------------------------------------------
        # Update the context to inform the other steps of modification in the checkable model for sleep stage
        self._context_manager[self.context_event_sel_def] = self.files_check_event_model
        self.event_proxy_model = EventsProxyModel(self)
        self.event_proxy_model.setSourceModel(self.files_check_event_model)
        self.event_proxy_model.setFilterKeyColumn(0) # col0: label, col1:count
        self.event_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.event_proxy_model.setRecursiveFilteringEnabled(False)


    def init_models(self):
        # Access to the PsgReaderSettingsView to access easily informations about the files
        self.reader_settings_view = self._context_manager[ContextConstants.context_files_event_names]
        # Extract the model (where the file information is stored) 
        #   To be aware of any change from the InputFiles Step
        self.files_model = self.reader_settings_view.files_model
        # Create the model for the checkable events tree, based on self.files_model
        self.files_check_event_model = self.update_checkable_model(self.files_check_event_model)
        # The model for the list of files is from the PsgReaderSettingsView
        self.file_listview.setModel(self.files_model)
        # The model for the events checkable is created locally
        self.event_treeview.setModel(self.event_proxy_model) 
        # Select/show the first file if any
        if self.files_check_event_model.rowCount()>0:
            filename = self.reader_settings_view.get_files_list(self.files_model)[0]
            self.file_listview.setCurrentIndex(self.reader_settings_view.get_file_index(filename,self.files_model))
            #self.on_file_selected()
            checkable_index = self.reader_settings_view.get_file_index(filename,self.files_check_event_model)
            # Map the index for the proxy model
            proxy_index = self.event_proxy_model.mapFromSource(checkable_index)
            self.event_treeview.setRootIndex(proxy_index)


    # Ask for the settings to the publisher to display on the SettingsView
    def load_settings(self):
        #--------------------------------------------------------------------------------------
        # Read context from other steps
        #--------------------------------------------------------------------------------------
        # Read the context from the Define Groupe step
        self.file_editable_model = self._context_manager[ContextConstants.context_editable_model]
        # Init the models and load the context
        self.init_models()
        # connect the checkbox state to the item selection
        self.files_check_event_model.itemChanged.connect(self.on_item_changed)


    def on_topic_update(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            at any update, does not necessary answer to a ping.
            To listen to any modification not only when you ask (ping)
        """
        if topic==self._context_manager.topic:
            
            if message==ContextConstants.context_files_event_names: # key of the context dict
                self.init_models()
            
            # Read the stage\artifact context from the Group Definition Step
            if message==ContextConstants.context_editable_model: # key of the context dict 
                self.file_editable_model = self._context_manager[ContextConstants.context_editable_model]
                if hasattr(self, "reader_settings_view"):
                    for filename in self.reader_settings_view.get_files_list(self.files_check_event_model):
                        # We update the model because of a modification on other step, we dont assert an itemChanged
                        if not self.files_check_event_model==None:
                            self.files_check_event_model.itemChanged.disconnect()
                        event_name_to_check = []
                        # Look for any event_group in the modified model
                        index_edit_model = self.reader_settings_view.get_file_index(filename, self.file_editable_model)
                        # name_group_dict is a dict : 
                        #           {name1 : group1}
                        #           {name2 : group2}
                        name_group_dict = self.reader_settings_view.get_name_group_from_file(self.file_editable_model, index_edit_model)
                        for name_key, group_val in name_group_dict.items():      
                            if group_val== self.event_group:
                                event_name_to_check.append(name_key)
                        # Set the CheckState to events listed in group_lst and name_list (only those)
                        index_check_model = self.reader_settings_view.get_file_index(filename, self.files_check_event_model)      
                        # Uncheck events (reset before select)
                        self.files_check_event_model = self.reader_settings_view.set_check_state_file(\
                            index_check_model, QtCore.Qt.CheckState.Unchecked, self.files_check_event_model)
                        #   usage : set_check_state_list(files_check_model, file_index, name_list, check_state)      
                        self.files_check_event_model, evt_found_tab = self.reader_settings_view.set_check_state_list(\
                            self.files_check_event_model, index_check_model,event_name_to_check, QtCore.Qt.CheckState.Checked)
                        self.files_check_event_model.itemChanged.connect(self.on_item_changed)


    def on_topic_response(self, topic, message, sender):
        pass # model is updated from context then in on_topic_update


    # When the user pressed bush button "Apply to all files"
    def on_apply_to_all_files(self):
        # Extract the index of the selected file from the file list view
        file_index = self.file_listview.currentIndex()
        checkable_index = self.find_checkable_index(file_index)
        # Read the selected events for one file
            # group_list : list of string 
            # name_list : list of string          
        name_list = self.reader_settings_view.get_checked_event_lst_from_file(\
            self.files_check_event_model, checkable_index)
        # Uncheck all before applying the selection
        self.on_reset_all_files()                  
        # Apply the event list to all files
            # Set the CheckState to events listed in group_list and name_list
            #   group_list : list of string 
            #   name_list : list of string
            #   check_state : QtCore.Qt.CheckState
        n_files = len(self.reader_settings_view.get_files_list(self.files_check_event_model))
        n_events_to_find = len(name_list)
        evt_found_tab = np.zeros((n_files,n_events_to_find)) # Usefull to show a message of the events not found
        for i_file in range(n_files):
            index_file_model = self.files_check_event_model.index(i_file,0)
            # Set the CheckState to events listed in group_lst and name_list
            #   and returns evt_found_tab (array of number of events)
            #   usage : set_check_state_list(files_check_model, file_index, group_lst, name_list, check_state)            
            self.files_check_event_model, evt_found_tab[i_file, :] = self.reader_settings_view.set_check_state_list(\
                self.files_check_event_model, index_file_model, name_list, QtCore.Qt.CheckState.Checked)
        # Manage error message when the event is not found
        error_files = []
        if not evt_found_tab.all():
            for i_file, events_found in enumerate(evt_found_tab):
                if not events_found.all():
                    for i_event, event_found in enumerate(events_found):
                        if not event_found:
                            index_file_model = self.files_check_event_model.index(i_file,0)
                            file_item = self.files_check_event_model.itemFromIndex(index_file_model)
                            error_files.append((file_item.text(),name_list[i_event]))
            error_msg_pd = pd.DataFrame(data=error_files,columns=['file', 'name'])
            table_dialog_msg = TableDialog(df=error_msg_pd, title="Warning Message",message="Those events were not found", showDownloadButton=True)
            table_dialog_msg.exec_()      
        self._context_manager[self.context_event_sel_def] = self.files_check_event_model


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
        self._context_manager[self.context_event_sel_def] = self.files_check_event_model


    # Called when the user clicks on RUN or when the pipeline is saved
    # Message are sent to the publisher   
    def on_apply_settings(self):
        pass


    # Called when the user finish editing the search_event line edit
    def search_pattern_slot(self):
        self.event_proxy_model.invalidate()
        search_pattern = self.search_lineEdit.text()
        self.event_proxy_model.set_names_search_pattern(search_pattern)


    # Called when the user checked\unchecked a group or a name
    # The input parameter item is the one changed
    def on_item_changed(self, item):
        self._context_manager[self.context_event_sel_def] = self.files_check_event_model


    # Called when the user select a file in the PSG Files list
    def on_file_selected(self):
        # Extract file index selected, from the self.files_model
        file_index = self.file_listview.currentIndex()
        self.event_proxy_model.set_filenames_filters(file_index.data())
        # Map the index for the proxy model
        checkable_index = self.find_checkable_index(file_index)
        proxy_index = self.event_proxy_model.mapFromSource(checkable_index)
        self.event_treeview.setRootIndex(proxy_index)


    # Find the tree view index linked to the list view index
    def find_checkable_index(self, file_list_index):
        # Extract filename
        filename = file_list_index.data()
        # Get the file index for the self.files_check_event_model model
        file_check_item = self.files_check_event_model.findItems(\
            filename, flags=QtCore.Qt.MatchExactly, column=0)
        if len(file_check_item)>0:
            index = file_check_item[0].index()
            if isinstance(index, list):
                index = index[0]
        else:
            index = file_check_item
        return index


    # When the user checked/unchecked "Select all"
    def on_select_all_groups(self):
        # Extract how many event groups are available
        # Need to extract info from the proxy model since only the visible group has been selected all
        # How many rows available at the file_model pointer
        file_index = self.file_listview.currentIndex()
        proxy_index = self.event_proxy_model.mapFromSource(self.find_checkable_index(file_index))
        self.set_check_state_file_via_proxy(proxy_index, self.select_all_checkBox.checkState())
        self._context_manager[self.context_event_sel_def] = self.files_check_event_model


    def set_check_state_file_via_proxy(self, file_index, check_state):
        """
       Set the CheckState to all groups and names of a file index selected
        
        Parameters
        -----------
            file_index : QtCore.QModelIndex
            check_state : QtCore.Qt.CheckState
        """
        n_names = self.event_proxy_model.rowCount(file_index)
        for name_row in range(n_names):
            column = 0
            name_index = self.event_proxy_model.index(name_row, column, file_index)
            source_index = self.event_proxy_model.mapToSource(name_index)
            name_item = self.files_check_event_model.itemFromIndex(source_index)
            name_item.setCheckState(check_state)


    # Called when the user delete an instance of the plugin
    def __del__(self):
        pass


    # Create the model for the checkable events tree, based on self.files_model
    def update_checkable_model(self, checkable_model_outdated):
        if checkable_model_outdated == None:
            # Create checkable item based on self.reader_settings_view.files_model
            #   events are not checked at this point
            files_check_event_model = self.reader_settings_view.\
                create_files_model_checkable()
        else:
            # Add and remove only the modified file
            updated_file_list = self.reader_settings_view.get_files_list(self.files_model)
            outdated_file_list = self.reader_settings_view.get_files_list(checkable_model_outdated)
            # Finding missing filename in the outdated_file_list
            file_to_rem = [outdated_file for outdated_file in outdated_file_list if outdated_file not in updated_file_list]
            # pass through the new list of files and add the new files into the checkable_model_outdated
            for filename in updated_file_list:
                file_item = checkable_model_outdated.findItems(filename, flags=QtCore.Qt.MatchExactly, column=0)
                # If it is a new file -> add it
                if len(file_item)==0:
                    # tree item : parent=file, child=name
                    item = self.reader_settings_view.create_file_item_tree(filename, True)
                    if isinstance(item,QtGui.QStandardItem):
                        checkable_model_outdated.appendRow(item)
                    else:
                        # Clear the list of file, because at least one is corrupted
                        checkable_model_outdated.clear()
                        WarningDialog(f"The file {filename} cannot be read properly. Check the access. Please ensure the format is consistent throughout the file.")
                # Otherwise -> nothing to do
            # remove the files from checkable_model_outdated
            if len(file_to_rem):
                # Clear the model, there is not the possibility to remove individually file, it is only a clear
                checkable_model_outdated.clear()
                #checkable_model_outdated = self.remove_files(file_to_rem, checkable_model_outdated)
            files_check_event_model = checkable_model_outdated
        return files_check_event_model


    def remove_files(self, file_to_rem, model):
        # Pass through the files to remove row for each column
        column=0
        row_to_rem = []
        for filename in file_to_rem :
            file_item = model.findItems(filename, flags=QtCore.Qt.MatchExactly, column=column)
            row_to_rem.append(file_item[0].row())
        # Remove the last first to avoid changing the index file
        row_to_rem.sort(reverse=True)
        for row in row_to_rem:
            model.removeRow(row)
        return model



    # Create an empty model based with the column Group-Name and Count
    def create_empty_files_model(self):
        files_model = QtGui.QStandardItemModel(0, 2)
        files_model.setHeaderData(0, QtCore.Qt.Horizontal, 'Group-Name')
        files_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Count')
        files_model.setHorizontalHeaderLabels(['Group-Name', 'Count'])
        return files_model
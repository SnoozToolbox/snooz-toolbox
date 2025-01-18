#! /usr/bin/env python3
"""
    GroupDefinition
    The step to edit the group of the events to import from EDFbrowser
"""
import ast
from qtpy import QtWidgets, QtCore
import os

from commons.BaseStepView import BaseStepView
from commons.NodeRuntimeException import NodeRuntimeException

from CEAMSTools.ConvertEDFbrowser.Commons import ContextConstants
from CEAMSTools.ConvertEDFbrowser.StadeSelection.StadeSelection import StadeSelection
from CEAMSTools.ConvertEDFbrowser.ArtifactSelection.ArtifactSelection import ArtifactSelection
from CEAMSTools.ConvertEDFbrowser.GroupDefinition.Ui_GroupDefinition import Ui_GroupDefinition


class GroupDefinition(BaseStepView, Ui_GroupDefinition, QtWidgets.QWidget):
    """
        GroupDefinition
        The step to edit the group of the events to import from EDFbrowser
    """
    node_id_Dictionary_name = "a42e544f-13dc-4148-93fe-6493e383c417" # select the list of name for the current filename
    event_group = 'EDFbrowser'
    
    """
        GroupDefinition
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform the group dictionary to add or modify group to events.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        self._node_id_Dictionary_name = self.node_id_Dictionary_name # select the list of name for the current filename

        # Subscribe to context manager for each node you want to talk to
        self._event_group_topic = f'{self._node_id_Dictionary_name}.dictionary'
        self._pub_sub_manager.subscribe(self, self._event_group_topic)
        # Dict to keep track of edited event group
        self.name_group_dict = {}  # the key is the filename and the item is a dict (name : group)
        # self.stage_dict = {}
        # self.artifact_dict = {}
        self.files_editable_event_model = None
        # Update the context 
        self._context_manager[ContextConstants.context_editable_model] = self.files_editable_event_model

    
    def init_models(self):
        # Access to the PsgReaderSettingsView to access easily informations about the files
        self.reader_settings_view = self._context_manager[ContextConstants.context_files_event_names]
        # Extract the model (where the file information is stored) 
        #   To be aware of any change from the InputFiles Step
        self.files_model = self.reader_settings_view.files_model
        # Create the model for the checkable events tree, based on self.files_model
        self.files_editable_event_model = self.update_editable_model(self.files_editable_event_model)
        # The model for the list of files is from the PsgReaderSettingsView
        self.file_listview.setModel(self.files_model)
        # The model for the events checkable is created locally
        self.event_treeview.setModel(self.files_editable_event_model) 
        # Select/show the first file if any
        self.select_first_file()
        # Update the local dictionary of events name and edited group
        #self.name_group_dict = self.get_dict_from_editable_model() 


    def load_settings(self):
        # Init the models and load the context manager
        self.init_models()
        # Read the context
        self.file_checkable_stage_model = self._context_manager[ContextConstants.context_stage_check_model]
        self.file_checkable_artifact_model = self._context_manager[ContextConstants.context_artifact_check_model]

        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._event_group_topic, 'ping')
        # connect the checkbox state to the item selection
        self.files_editable_event_model.itemChanged.connect(self.on_item_changed)


    def on_topic_update(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            at any update, does not necessary answer to a ping.
            To listen to any modification not only when you ask (ping)
        """
        if topic==self._context_manager.topic:
            if message==ContextConstants.context_files_event_names: # key of the context dict
                self.init_models()
                # Update the model for the file list
                self.reader_settings_view = self._context_manager[ContextConstants.context_files_event_names]
                self.files_model = self.reader_settings_view.files_model
                # Create the model for the editable group events
                self.files_editable_event_model = self.update_editable_model(self.files_editable_event_model)
                self.files_editable_event_model.itemChanged.connect(self.on_item_changed)

            # Dictionary for the stage events definition
            if message==ContextConstants.context_stage_check_model: # key of the context dict
                self.file_checkable_stage_model = self._context_manager[ContextConstants.context_stage_check_model]
                if hasattr(self, "reader_settings_view"): # Need the context from InputFilesStep first
                    # The model is updated because of another step, we turn off the signal on on_item_changed to avoid circular modification
                    if not self.files_editable_event_model==None:
                        self.files_editable_event_model.itemChanged.disconnect()
                    # Update self.files_editable_event_model based on file_checkable_stage
                    self.files_editable_event_model = self.update_editable_model_from_check_model(\
                        self.reader_settings_view.get_files_list(self.files_model), self.files_editable_event_model, \
                            self.file_checkable_stage_model, StadeSelection.event_group)
                    self.files_editable_event_model.itemChanged.connect(self.on_item_changed)

                # Select/show the first file if any
                self.select_first_file()

            # Dictionary for the artifact events definition
            if message==ContextConstants.context_artifact_check_model: # key of the context dict
                self.file_checkable_artifact_model = self._context_manager[ContextConstants.context_artifact_check_model]
                if hasattr(self, "reader_settings_view"): # Need the context from InputFilesStep first
                    # The model is updated because of another step, we turn off the signal on on_item_changed to avoid circular modification
                    if not self.files_editable_event_model==None:
                        self.files_editable_event_model.itemChanged.disconnect()                    
                    # Update self.files_editable_event_model based on file_checkable_stage
                    self.file_checkable_artifact_model = self.update_editable_model_from_check_model(\
                        self.reader_settings_view.get_files_list(self.files_model), self.files_editable_event_model, \
                            self.file_checkable_artifact_model, ArtifactSelection.event_group)
                    self.files_editable_event_model.itemChanged.connect(self.on_item_changed)

                # Select/show the first file if any
                self.select_first_file()


    def on_topic_response(self, topic, message, sender):
        if topic == self._event_group_topic:   
            if isinstance(message,str) and (not message==''):
                message = ast.literal_eval(message)
            if isinstance(message,dict) and len(message)>0:
                self.name_group_dict = message
                self.set_group_from_dict()


    # Called when the user clicks on RUN or when the pipeline is saved
    # Message are sent to the publisher   
    def on_apply_settings(self):
        # send dictionaries to appropriate modules
        self.name_group_dict = self.get_dict_from_editable_model() 
        self._pub_sub_manager.publish(self, self._event_group_topic, str(self.name_group_dict))


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._event_group_topic)


    def update_editable_model_from_check_model(self, file_list, editable_model, checkable_model, check_event_group): 
        for filename in file_list:
            
            # Reset files_editable_event_model for stage
            # Any group defined as check_event_group must be marked as event_group in case stages have been unckecked
            file_editable_index = self.reader_settings_view.get_file_index(filename, editable_model)
            name_group_dict = self.reader_settings_view.get_name_group_from_file(editable_model, file_editable_index)
            if check_event_group in name_group_dict.values():
                for name_key, group_value in name_group_dict.items():
                    if group_value==check_event_group:
                        name_group_dict[name_key] = self.event_group
                editable_model, evt_found_tab = self.reader_settings_view.set_groups_from_dict(\
                    editable_model, file_editable_index, name_group_dict)

            # Extract stage from file_checkable_stage_model
            file_checkable_index = self.reader_settings_view.get_file_index(filename, checkable_model)
            name_list = self.reader_settings_view.get_checked_event_lst_from_file(checkable_model, file_checkable_index)

            # Set selected stage in files_editable_event_model
            for name_key, group_value in name_group_dict.items():
                if name_key in name_list:
                    name_group_dict[name_key] = check_event_group
            editable_model, evt_found_tab = self.reader_settings_view.set_groups_from_dict(\
                editable_model, file_editable_index, name_group_dict)

        return editable_model


    # Select/show the first file if any
    def select_first_file(self):
        if not self.files_editable_event_model==None:
            if self.files_editable_event_model.rowCount()>0:
                filename = self.reader_settings_view.get_files_list(self.files_model)[0]
                self.file_listview.setCurrentIndex(self.reader_settings_view.get_file_index(filename,self.files_model))
                editable_index = self.reader_settings_view.get_file_index(filename,self.files_editable_event_model)
                self.event_treeview.setRootIndex(editable_index)
                

    # When the user pressed bush button "Apply to all files"
    def on_apply_to_all_files(self):

        # Save current modification
        file_index = self.file_listview.currentIndex()
        editable_index = self.find_editable_index(file_index)
        name_group_dict = self.reader_settings_view.get_name_group_from_file(\
            self.files_editable_event_model, editable_index)

        # Apply the modification saved to all the files included in the model.
        for file_key in self.reader_settings_view.get_files_list(self.files_editable_event_model) :
            self.files_editable_event_model, evt_found_tab = \
                self.set_group_from_dict_selected_file(file_key, name_group_dict)

        # Update the context 
        self._context_manager[ContextConstants.context_editable_model] = self.files_editable_event_model
        # Select/show the first file if any
        self.select_first_file()


    # Function to uncheck all groups and names.
    def on_reset_all_files(self):
        self.files_editable_event_model = None
        self.init_models()
        # Update the context 
        self._context_manager[ContextConstants.context_editable_model] = self.files_editable_event_model
        # Select/show the first file if any
        self.select_first_file()
        

    # To generate the dictionary of selected events for stages to provide to the Stage selection step or
    # to generate the dictionary of selected events for artifacts to provide to the Artifact selection step.
    def generate_stage_artifact_sel_from_group_name(self, group_2_look_4):
        stage_dict = {}
        for file_key, group_name_dict in self.name_group_dict.items():
            if group_2_look_4 in group_name_dict.values():
                stage_name_str_lst = ""
                for name_key, group_val in group_name_dict.items():
                    if group_val==group_2_look_4:
                        if len(stage_name_str_lst)>0:
                            stage_name_str_lst=stage_name_str_lst+','+name_key
                        else:
                            stage_name_str_lst = name_key
                stage_dict[file_key]=stage_name_str_lst
            else:
                stage_dict[file_key]=''
        return stage_dict    



    # To read the local dicts in order to define the right group in the view.
    def set_group_from_dict(self):
        if len(self.name_group_dict)>0:
            # For each opened file
            for file_key, name_group_dict in self.name_group_dict.items():
                self.files_editable_event_model, evt_found_tab = \
                    self.set_group_from_dict_selected_file(file_key, name_group_dict)


    # To read the local dicts in order to define the right group in the view for a selected file.
    def set_group_from_dict_selected_file(self, filename, name_group_dict):
        # Find in the model the index of current filename
        view_index = self.reader_settings_view.get_file_index(filename, self.files_model)
        # Set the view to the index of the file
        self.file_listview.setCurrentIndex(view_index)
        # Set the group to events listed in name_group_dict
        #   and returns evt_found_tab (array of number of events)
        #   usage : set_groups_from_dict(files_check_model, file_index, name_group_dict)
            # files_check_model : QtGui.QStandardItemModel
            # file_index : QtCore.QModelIndex
            # name_group_dict : dict
            #   keys are the event name
            #   values are the event group
        file_editable_index = self.find_editable_index(view_index)
        self.files_editable_event_model, evt_found_tab = self.reader_settings_view.set_groups_from_dict(\
            self.files_editable_event_model, file_editable_index, name_group_dict)
        return self.files_editable_event_model, evt_found_tab


    def update_dicts_from_stage_artifact(self):
        for file_key, name_group_dict in self.name_group_dict.items():
            if file_key in self.stage_dict.keys():
                # Set the group of stage events
                stage_event_dict = self.stage_dict[file_key]
                # If there is no stage selection
                if len(stage_event_dict)==0:
                    name_group_dict[name_event_key] = self.event_group
                else:
                    for name_event_key, group_event_val in stage_event_dict.items():
                        name_group_dict[name_event_key] = group_event_val
            if file_key in self.artifact_dict.keys():
                # Set the group of artifact events
                artifact_event_dict = self.artifact_dict[file_key]
                if len(artifact_event_dict)==0:
                    name_group_dict[name_event_key] = self.event_group
                else:
                    for name_event_key, group_event_val in artifact_event_dict.items():
                        name_group_dict[name_event_key] = group_event_val


    # To read and save locally the edited groups.
    # Read file list from the updated model (self.files_model) and 
    #   the group from the self.files_editable_event_model 
    #   in order to send the information to the dictionary modules in the pipeline
    def get_dict_from_editable_model(self):       
        # Clean the local dictionary 
        name_group_dict = {} 
        # Get the file list from the model
        files_list = self.reader_settings_view.get_files_list(self.files_model)
        n_files = len(files_list)
        # For each file of the list
        for i_file in range(n_files):
            filename = files_list[i_file]
            file_index = self.reader_settings_view.get_file_index(filename, self.files_model)
            file_editable_index = self.find_editable_index(file_index)
            # group_lst and name_list are list of string 
            name_group_dict[filename] = self.reader_settings_view.get_name_group_from_file(\
                self.files_editable_event_model, file_editable_index)
        return name_group_dict


    # Called when the user checked\unchecked a group or a name
    # The input parameter item is the one changed
    def on_item_changed(self, item):
        self._context_manager[ContextConstants.context_editable_model] = self.files_editable_event_model


    # Called when the user select a file in the PSG Files list
    def on_file_selected(self):
        # Extract file index selected, from the self.files_model
        file_index = self.file_listview.currentIndex()
        editable_index = self.reader_settings_view.get_file_index(file_index.data(),self.files_editable_event_model)
        #editable_index = self.find_editable_index(file_index)
        self.event_treeview.setRootIndex(editable_index)


    # Find the tree view index linked to the list view index
    def find_editable_index(self, file_list_index):
        # Extract filename
        filename = file_list_index.data()
        # Get the file index for the self.files_editable_event_model model
        file_check_item = self.files_editable_event_model.findItems(\
            filename, flags=QtCore.Qt.MatchExactly, column=0)
        if len(file_check_item)>0:
            index = file_check_item[0].index()
            if isinstance(index, list):
                index = index[0]
        else:
            index = file_check_item
        return index


    # Create the model for the checkable events tree, based on self.files_model
    def update_editable_model(self, editable_model_outdated):
        if editable_model_outdated == None:
            # Create checkable item based on self.reader_settings_view.files_model
            #   events are not checked at this point
            files_editable_event_model = self.reader_settings_view.create_files_group_model_editable(self.event_group)
        else:
            # The list of files is not item removable, the user can add or clear the list.
            # Add and remove only the modified file
            updated_file_list = self.reader_settings_view.get_files_list(self.files_model)
            outdated_file_list = self.reader_settings_view.get_files_list(editable_model_outdated)

            # Finding missing filename in the outdated_file_list
            file_to_rem = [outdated_file for outdated_file in outdated_file_list if outdated_file not in updated_file_list]
            # pass through the new list of files and add the new files into the editable_model_outdated
            for filename in updated_file_list:
                file_item = editable_model_outdated.findItems(filename, flags=QtCore.Qt.MatchExactly, column=0)
                # If it is a new file -> add it
                if len(file_item)==0:
                    # tree item : parent=file, child=name (non editable), child=group (editable)
                    item = self.reader_settings_view.create_file_item_name_group_list(filename, self.event_group)
                    editable_model_outdated.appendRow(item)
                # Otherwise -> nothing to do
            # remove the files from editable_model_outdated
            if len(file_to_rem):
                # Clear the model self.files_editable_event_model
                editable_model_outdated.clear()
            files_editable_event_model = editable_model_outdated
        return files_editable_event_model


    # Obsolete
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
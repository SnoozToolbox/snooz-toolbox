#! /usr/bin/env python3
"""
    EditorStep
    The class of the step to remove event or to edit the group and /or name of the events to write back in the file.
"""

import ast
import os
import pandas as pd
from qtpy import QtWidgets, QtCore, QtGui

from commons.BaseStepView import BaseStepView
from commons.NodeRuntimeException import NodeRuntimeException
from CEAMSTools.AnnotationsEditor.EditorStep.Ui_EditorStep import Ui_EditorStep
from CEAMSTools.AnnotationsEditor.InputFileAnnotStep.InputFileAnnotStep import InputFileAnnotStep
from commons.BaseStepView import BaseStepView
from widgets.TableDialog import TableDialog

DEBUG = True

class EditorStep(BaseStepView, Ui_EditorStep, QtWidgets.QWidget):
    """
        EditorStep
        The class of the step to remove event or to edit the group and /or name of the events to write back in the file.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to

        # Dictionaries of tuple
        self._node_id_dict_drop = "ede9def7-2c4f-46f5-ad44-72760ec86f87" 
        # Dictionary of tuple, the key is the filename and the value is the tuple of group/name to rename
        self._node_id_dict_rename = "67b8852a-b6ab-4e10-9b7b-a3cca3bd1a6e"

        # Subscribe to message manager for each node you want to talk to
        self._event_drop_topic = f'{self._node_id_dict_drop}.dictionary'
        self._pub_sub_manager.subscribe(self, self._event_drop_topic)
        self._event_rename_topic = f'{self._node_id_dict_rename}.dictionary'
        self._pub_sub_manager.subscribe(self, self._event_rename_topic)
        
        # Dictionaries
        self._dict_loaded = 0
        #   the key is the filename and the value is the list of tuple of group/name to drop
        #   ex. [('group1', 'name1'), ('group2', 'name2')]
        self.dict_drop = {}
        #   the key is the filename and the value is the list of tuple of group/name to rename
        #   [(group1_ori, name1_ori, group1_new, name1_new)
        #   (group2_ori, name2_ori, group2_new, name2_new)]
        self.dict_rename = {}  

        # Model of the tree views
        self.files_editable_subject_model = None
        self.files_editable_cohort_model = None

    
    def init_models(self):
        # Access to the PsgReaderSettingsView to access easily informations about the files
        self.reader_settings_view = self._context_manager[InputFileAnnotStep.context_files_view]
        # Extract the model (where the file information is stored) 
        #   To be aware of any change from the InputFiles Step
        self.files_model = self.reader_settings_view.files_model
        # Create the model for the checkable events tree, based on self.files_model
        self.files_editable_subject_model = self.update_editable_subject_model(self.files_editable_subject_model) 
        # The model for the list of files is from the PsgReaderSettingsView
        self.file_listview.setModel(self.files_model)
        # The model for the events checkable is created locally
        self.treeView_subject.setModel(self.files_editable_subject_model)
        self.treeView_subject.resizeColumnToContents(0)
        self.update_editable_cohort_model()
        self.treeView_cohort.setModel(self.files_editable_cohort_model)
        self.treeView_cohort.resizeColumnToContents(0)
        # Select/show the first file if any
        self.select_first_file()


    def load_settings(self):
        # Init the models and load the context manager
        self.init_models()
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._event_drop_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_rename_topic, 'ping')


    def on_topic_update(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            at any update, does not necessary answer to a ping.
            To listen to any modification not only when you ask (ping)
        """
        if topic==self._context_manager.topic:
            if message==InputFileAnnotStep.context_files_view: # key of the context dict
                self.try_disconnect_UI()
                #self.init_models()
                # Update the model for the file list
                self.reader_settings_view = self._context_manager[InputFileAnnotStep.context_files_view]
                self.files_model = self.reader_settings_view.files_model
                # Create the model for the editable group events
                self.files_editable_subject_model = self.update_editable_subject_model(self.files_editable_subject_model)
                self.update_editable_cohort_model()
                self.treeView_subject.resizeColumnToContents(0)
                self.treeView_cohort.resizeColumnToContents(0)
                # Select/show the first file if any
                self.select_first_file()


    def try_disconnect_UI(self):
        try : 
            self.files_editable_cohort_model.itemChanged.disconnect()
        except :
            pass
        try : 
            self.files_editable_subject_model.itemChanged.disconnect()
        except :
            pass


    def on_topic_response(self, topic, message, sender):
        if topic == self._event_drop_topic:   
            self._dict_loaded = self._dict_loaded + 1
            if isinstance(message,str) and (not message==''):
                message = ast.literal_eval(message)
            if isinstance(message,dict) and len(message)>0:
                self.dict_drop = message
                # Read the local dicts and uncheck or rename items in the model that is linked to the tree view.
                if self._dict_loaded==2:
                    self.set_group_from_dict()
                    self.update_editable_cohort_model()
        if topic == self._event_rename_topic:   
            self._dict_loaded = self._dict_loaded + 1
            if isinstance(message,str) and (not message==''):
                message = ast.literal_eval(message)        
            if isinstance(message,dict) and len(message)>0:
                self.dict_rename = message
                # Read the local dicts and uncheck or rename items in the model that is linked to the tree view.
                if self._dict_loaded==2:
                    self.set_group_from_dict()
                    self.update_editable_cohort_model()


    # Called when the user clicks on RUN or when the pipeline is saved
    # Message are sent to the publisher   
    def on_apply_settings(self):
        # send dictionaries to appropriate modules
        #
        # self.dict_rename
        #   --------------
        #   the key is the filename and the value is the list of tuple of group/name to rename
        #   [(group1_ori, name1_ori, group1_new, name1_new)
        #   (group2_ori, name2_ori, group2_new, name2_new)]
        #
        # self.dict_drop
        #   --------------
        #   the key is the filename and the value is the list of tuple of group/name to drop
        #   ex. [('group1', 'name1'), ('group2', 'name2')]
        self.dict_drop = self.get_dict_drop_from_editable_model()

        # Clean-up the self.dict_rename in case we went back and forth on the same group/name
        # Create a list of 5 columns ('original group', 'original name', 'new group', 'new name', 'file') 
        #   if the group or the name has been renamed.
        #   The dict_rename_clean has a key for each file even if the value is an empty list.
        dict_rename_clean = {}
        for file_key, renaming_list in self.dict_rename.items():
            rename_annot = [(tup_g, tup_n, tup_gn, tup_nn) for tup_g, tup_n, tup_gn, tup_nn in renaming_list\
                 if ((not tup_g==tup_gn) or (not tup_n==tup_nn))]
            dict_rename_clean[file_key] = rename_annot
        files_list = self.reader_settings_view.get_files_list(self.files_model)
        for file in files_list:
            if not file in dict_rename_clean.keys():
                dict_rename_clean[file]=[]

        # Send the message
        self._pub_sub_manager.publish(self, self._event_rename_topic, str(dict_rename_clean))
        self._pub_sub_manager.publish(self, self._event_drop_topic, str(self.dict_drop))


    # Select/show the first file if any
    def select_first_file(self):
        if not self.files_editable_subject_model==None:
            if self.files_editable_subject_model.rowCount()>0:
                filename = self.reader_settings_view.get_files_list(self.files_model)[0]
                self.file_listview.setCurrentIndex(self.reader_settings_view.get_file_index(filename,self.files_model))
                editable_index = self.reader_settings_view.get_file_index(filename,self.files_editable_subject_model)
                self.treeView_subject.setRootIndex(editable_index)
                

    # Function to go back to the original group/name labels
    def on_reset_all_files(self):
        self.files_editable_subject_model = None
        self.files_editable_cohort_model = None
        self.init_models() # self.files_editable_subject_model is updated
        self.update_editable_cohort_model()
        # Select/show the first file if any
        self.select_first_file()
          

    # To read the local dicts in order to define the right group in the model that is linked to the tree view.
    #   Useful when the pipeline that include files is being loaded.
    #   Also useful to apply modification from one file to all other files.
    def set_group_from_dict(self):

        if len(self.dict_drop)>0:
            # For each opened file Uncheck events group/name to remove
            for file_key, group_name_tup in self.dict_drop.items():
                file_index = self.reader_settings_view.get_file_index(file_key, self.files_editable_subject_model)
                # group_name_tup : 
                #   [(group1, name1)
                #   (group2, name2)]
                # Convert the group_name tuple into 2 lists
                group_lst = []
                name_lst = []
                for group, name in group_name_tup: 
                    group_lst.append(group)
                    name_lst.append(name)
                self.files_editable_subject_model, evt_found_tab = self.reader_settings_view.set_check_state_list(\
                    self.files_editable_subject_model, file_index, group_lst, name_lst, QtCore.Qt.CheckState.Unchecked)

        if len(self.dict_rename)>0:
            # For each opened file edit group/name to rename
            for file_key, group_name_tup in self.dict_rename.items():
                file_index = self.reader_settings_view.get_file_index(file_key, self.files_editable_subject_model)
                # group_name_tup : 
                #   [(group1_ori, name1_ori, group1_new, name1_new)
                #   (group2_ori, name2_ori, group2_new, name2_new)]
                self.files_editable_subject_model, evt_found = self.reader_settings_view.rename_group_name(\
                    self.files_editable_subject_model, file_index, group_name_tup)
                
        return evt_found_tab


    # To read and save locally the edited groups.
    # Read file list from the updated model (self.files_model) and 
    #   the group from the self.files_editable_subject_model 
    #   in order to send the information to the dictionary modules in the pipeline
    def get_dict_drop_from_editable_model(self):       
        # Clean the local dictionary 
        dict_drop = {} 
        # Get the file list from the model
        files_list = self.reader_settings_view.get_files_list(self.files_model)
        n_files = len(files_list)
        # For each file of the list
        for i_file in range(n_files):
            filename = files_list[i_file]
            # file_index = self.reader_settings_view.get_file_index(filename, self.files_model)
            # file_editable_index = self.find_editable_index(file_index)
            # Get group/name to remove
            #  Return the unselected events (event unchecked) of a file index.
            # group_list, name_list =  self.reader_settings_view.get_unchecked_event_lst_from_file(\
            #     self.files_editable_subject_model, file_editable_index, self.files_model, file_index)
            group_list, name_list =  self.reader_settings_view.get_unchecked_event_lst_from_file(self.files_editable_subject_model, filename)
            # Convert separated lists into a list of tuple.
                # events_to_remove : list of tuple
                #     Events group and name to remove from the file.
                #     ex. [('group1', 'name1'), ('group2', 'name2')]
            events_to_remove = []
            for group, name in zip(group_list, name_list):
                cur_tuple = (group , name)
                events_to_remove.append(cur_tuple)
            dict_drop[filename] = events_to_remove
        return dict_drop


    # Called when the user checked\unchecked a group/name or edit a group/name
    #   in the subject window
    # The input parameter item is the one changed
    def on_item_changed(self, item):
        # TODO find out why this function is called twice for one modification
        # Disconnect the signal the time the states are analyzed and updated
        try: self.files_editable_subject_model.itemChanged.disconnect()
        except: pass
        # Update the local dictionary of events name and edited group
        #   self.dict_rename is updated in the function
        self.update_dict_rename_from_subject_item_changed(item)
        # Propagate states (unchecked, checked...)
        if item.hasChildren():
            self.files_editable_subject_model = self.reader_settings_view.apply_state_to_child_item(item, self.files_editable_subject_model)
        else:
            self.files_editable_subject_model = self.reader_settings_view.apply_state_to_parent_item(item, self.files_editable_subject_model)             
        # Connect the signal to listen to modification
        self.files_editable_subject_model.itemChanged.connect(self.on_item_changed)
        # Fill the cohort tree widget with the modifications    
        self.update_editable_cohort_model()


    # Called when the user checked\unchecked a group/name or edit a group/name
    #   in the cohort window
    # The input parameter item is the one changed
    def item_changed_cohort_slot(self, item):
        # Disconnect the signal the time the states are analyzed and updated
        self.try_disconnect_UI()

        # Propagate states (unchecked, checked...) and name edited from cohort tree widget to the model
        if item.hasChildren(): # it is a group
            new_group_label = item.text()
            # Return the original information from the modified item (column 1)
            filename, previous_group_label, ori_name_lst = self.reader_settings_view.get_info_from_edit_group_item(\
                item, self.files_editable_cohort_model)
            
            # If the item is really modified
            if (not new_group_label==previous_group_label) or (not item.checkState()==QtCore.Qt.CheckState.PartiallyChecked):
                # Apply on every file
                for file in self.reader_settings_view.get_files_list(self.files_editable_subject_model):
                    file_index = self.reader_settings_view.get_file_index(file, self.files_editable_subject_model)

                    # If the state is modified (not a child modification propagated to the parent)
                    if not item.checkState()==QtCore.Qt.CheckState.PartiallyChecked:
                        # Apply state modification to the subject tree model
                        self.files_editable_subject_model = self.reader_settings_view.set_check_state_group(\
                            self.files_editable_subject_model, file_index, previous_group_label, item.checkState())
                    # If the group label is edited
                    if not new_group_label==previous_group_label:
                        # Apply edit modification to the subject tree model
                        # Return the editable model updated and ori_info.
                        #   ori_info : tuple (filename, group_ori_value, ori_name_lst) of the events found in the subject tree model                   
                        self.files_editable_subject_model, ori_info = self.reader_settings_view.rename_group_item(\
                            self.files_editable_subject_model, file_index, previous_group_label, new_group_label)
                        # Update dict_rename
                        if not ori_info==None:
                            self.update_dict_rename_for_group_edit(ori_info[0], ori_info[1], ori_info[2], new_group_label)
                        # This will be called only when the last modification is applied (since names are modified before the group)
                        # no !!! this is called at the beginning when the group name is modified.
                        # self.update_editable_cohort_model()
                            
        else: # it is a name or empty

            # Even if we uncheck the group, it pass accross all names
            #  find the group
            group_item = item.parent()
            if group_item is not None :
                new_name_label = item.text()

                # Find the original name label form the column 1 of the item.
                filename, previous_group, previous_name = self.reader_settings_view.get_info_from_edit_name_item(\
                    item, self.files_editable_cohort_model)
                # Apply on every file
                for file in self.reader_settings_view.get_files_list(self.files_editable_subject_model):
                    file_index = self.reader_settings_view.get_file_index(file, self.files_editable_subject_model)
                    # if really edited
                    if not new_name_label==previous_name:                      
                        
                        # Rename group/name
                        group_name_tup = [(previous_group, previous_name, previous_group, new_name_label)]          
                        # Apply edit modification to the subject tree model        
                        self.files_editable_subject_model, file_group_name_tup = self.reader_settings_view.rename_group_name(\
                            self.files_editable_subject_model, file_index, group_name_tup)
                        
                        # Update dict_rename - could have many names within a group 
                        #   if groups are duplicated (possible in the renaming process) 
                        #       CompSpecXXX_f4 -> CompSpec
                        #           art._f4 -> art
                        #       CompSpecXXX_f3 -> CompSpec
                        #           art._f3 -> art
                        #       CompSpecXXX_c4 -> CompSpec
                        #           art._c4 -> art
                        # Here CompSpec will appear a few times since the original value is kept on the right column
                        for group_ori, name_ori, group_mod, name_mod in file_group_name_tup:
                            self.update_dict_rename_for_name_edit(group_ori, name_ori, group_mod, name_mod)

                    # Check or uncheck
                    # Apply state modification to the subject tree model
                    self.files_editable_subject_model, evt_found = self.reader_settings_view.set_check_state_list(\
                        self.files_editable_subject_model, file_index, [previous_group], [new_name_label], item.checkState())

        # Propagate states (unchecked, checked...) in the cohort tree model
        if item.hasChildren():
            self.files_editable_cohort_model = self.reader_settings_view.apply_state_to_child_item(item, self.files_editable_cohort_model)
        else:
            self.files_editable_cohort_model = self.reader_settings_view.apply_state_to_parent_item(item, self.files_editable_cohort_model)       

        # Fill the cohort tree widget with the modifications
        #  it allows to merge 2 same groups but it makes snooz crashes...     
        #   self.update_editable_cohort_model()   
        self.files_editable_cohort_model.itemChanged.connect(self.item_changed_cohort_slot)
        self.files_editable_subject_model.itemChanged.connect(self.on_item_changed)
        

    # Function to update the dict_rename from the modified subject item 
    #   The original value are taken from the files_model (untouched model from input_step)
    #   the key is the filename and the value is the list of tuple of group/name to rename
        #   [(group1_ori, name1_ori, group1_new, name1_new)
        #   (group2_ori, name2_ori, group2_new, name2_new)]
    def update_dict_rename_from_subject_item_changed(self, item):
        # Extract original value from files_model
        is_group = item.hasChildren()
        if is_group:
            # Return the original information (from an untouched model) about a modified item (event group)
            filename, group_ori_value, ori_name_lst = self.reader_settings_view.get_info_from_edit_group_item(\
                item, self.files_editable_subject_model)
            # Value modified
            new_group_value = item.text()
            # Update dict_rename        
            #if not new_group_value==group_ori_value: # need to remove this condition in case we go back to the original name
            self.update_dict_rename_for_group_edit(filename, group_ori_value, ori_name_lst, new_group_value)
        else:
            # Return the original information (from an untouched model) about a modified item (event name)
            filename, group_ori_value, ori_name_value = self.reader_settings_view.get_info_from_edit_name_item(\
                item, self.files_editable_subject_model)
            # Value modified
            new_name_value = item.text()
            # Update dict_rename     
            #if not new_name_value==ori_name_value: # need to remove this condition in case we go back to the original name
            self.update_dict_rename_for_name_edit(filename, group_ori_value, ori_name_value, new_name_value)


    # Update the dict_rename when a event group has bee edited
    #   called when the subject tree or the cohort tree is edited
    def update_dict_rename_for_group_edit(self, filename, group_ori_value, ori_name_lst, new_group_value):
        group_name_list_mod = []
        
        # If the file is modified for the first time
        if not (filename in self.dict_rename.keys()):
            # Loop through all names under the group to modify all children
            for name in ori_name_lst:
                group_name_list_mod.append((group_ori_value, name, new_group_value, name))

        # if self.dict_rename contains already modification for the file
        else:
            group_name_list_ori = self.dict_rename[filename]
            item_modified = False
            for group_ori, name_ori, new_group, new_name in group_name_list_ori:
                # Replace the original value in the dict by the new value
                if group_ori==group_ori_value:
                    group_name_list_mod.append((group_ori, name_ori, new_group_value, new_name))
                    item_modified = True
                # Keep the old events_to_rename
                else:
                    group_name_list_mod.append((group_ori, name_ori, new_group, new_name))

            # If the group/name is modified for the first time for that file
            if not item_modified :
                # Add all the names modification for the current group
                # Loop through all names under the group to modify all children
                for name in ori_name_lst:
                    group_name_list_mod.append((group_ori_value, name, new_group_value, name))
            
        self.dict_rename[filename] = group_name_list_mod


    # Update the dict_rename when a event name has bee edited
    #   called when the subject tree or the cohort tree is edited
    def update_dict_rename_for_name_edit(self, filename, group_ori_value, ori_name_value, new_name_value):
        group_name_list_mod = []
        
        # If the file is modified for the first time
        if not (filename in self.dict_rename.keys()):
            group_name_list_mod.append((group_ori_value, ori_name_value, group_ori_value, new_name_value))

        # if self.dict_rename contains already modification for the file
        else:
            group_name_list_ori = self.dict_rename[filename]
            item_modified = False
            for group_ori, name_ori, new_group, new_name in group_name_list_ori:
                # Replace the original value in the dict by the new value
                if (group_ori==group_ori_value) and (name_ori==ori_name_value):
                    group_name_list_mod.append((group_ori, name_ori, new_group, new_name_value))
                    item_modified = True
                # Keep the old events_to_rename
                else:
                    group_name_list_mod.append((group_ori, name_ori, new_group, new_name))
            # If the group/name is modified for the first time for that file
            if not item_modified :
                # Add the new name modification
                group_name_list_mod.append((group_ori_value, ori_name_value, group_ori_value, new_name_value))
            
        self.dict_rename[filename] = group_name_list_mod            


    # Called when the user select a file in the PSG Files list
    def on_file_selected(self):
        # Extract file index selected, from the self.files_model
        file_index = self.file_listview.currentIndex()
        editable_index = self.reader_settings_view.get_file_index(file_index.data(),self.files_editable_subject_model)
        self.treeView_subject.setRootIndex(editable_index)


    # Find the tree view index linked to the list view index
    def find_editable_index(self, file_list_index):
        # Extract filename
        filename = file_list_index.data()
        # Get the file index for the self.files_editable_subject_model model
        file_check_item = self.files_editable_subject_model.findItems(\
            os.path.basename(filename), flags=QtCore.Qt.MatchExactly, column=0)
        if len(file_check_item)>0:
            index = file_check_item[0].index()
            if isinstance(index, list):
                index = index[0]
        else:
            index = file_check_item
        return index


    # Create the model for the checkable and editable events tree, based on self.files_model
    # Called when a file is removed or add in the step "1-Input Files".
    # Should not trig any changes in the cohort tree_widget
    def update_editable_subject_model(self, editable_model_outdated):
        if editable_model_outdated == None:
            # Create checkable item based on self.reader_settings_view.files_model
            #   events are not checked at this point
            files_editable_subject_model = self.reader_settings_view.create_files_model_editable(self.files_model, checkable=True)
        else:
            # Add and remove only the modified file
            updated_file_list = self.reader_settings_view.get_files_list(self.files_model)
            outdated_file_list = self.reader_settings_view.get_files_list(editable_model_outdated)
            # Finding missing filename in the outdated_file_list
            file_to_rem = [outdated_file for outdated_file in outdated_file_list if outdated_file not in updated_file_list]
            # pass through the new list of files and add the new files into the editable_model_outdated
            for filename in updated_file_list:
                file_item = editable_model_outdated.findItems(os.path.basename(filename), flags=QtCore.Qt.MatchExactly, column=0)
                # If it is a new file -> add it
                if len(file_item)==0:
                    # tree item : parent=file, child=name (non editable), child=group (editable)
                    item = self.reader_settings_view.make_editable_file_item_count(filename, self.files_model, checkable=True)
                    editable_model_outdated.appendRow(item)
                # Otherwise -> nothing to do
            # remove the files from editable_model_outdated
            if len(file_to_rem):
                editable_model_outdated = self.remove_files(file_to_rem, editable_model_outdated)
            files_editable_subject_model = editable_model_outdated
        files_editable_subject_model.sort(0)
        files_editable_subject_model.itemChanged.connect(self.on_item_changed)
        #self.files_editable_cohort_model.itemChanged.connect(self.item_changed_cohort_slot)
        return files_editable_subject_model


    # Should not trig any change in the self.files_editable_subject_model
    def update_editable_cohort_model(self):
        # Disconnect the signal the time the states are analyzed and updated
        try : self.files_editable_cohort_model.itemChanged.disconnect()
        except: pass
        # Create checkable and editable item based on self.files_editable_subject_model
        #   Show all the cohort, do not keep track of the subject just plot all groups with all names in.
        #   Pass through the files_editable_subject_model 
        #       deal with dict where the key is the group and the value a list of names
        self.files_editable_cohort_model = self.reader_settings_view.create_empty_edit_files_model()

        # get_group_name_from_cohort returns group_name_dict          
            # group_name_dict : dict
            #     keys are the event group
            #     values are a list of strings (the event names)
            # tristate_dict : dict of dict
            #     keys are the event group
            #     value is a dict where the key is the name and the value is the state
        group_name_dict, tristate_dict  = self.reader_settings_view.get_group_name_from_cohort(\
            self.files_editable_subject_model)

        # Fill the tree view model
        for group, name_list in group_name_dict.items():
            group_item = QtGui.QStandardItem(group)
            group_item.setCheckable(True)
            group_item.setEditable(True)
            group_item.setTristate(True)
            ori_group_item = QtGui.QStandardItem(group)
            ori_group_item.setCheckable(False)
            ori_group_item.setEditable(False)
            tristate = []
            for name in name_list:
                name_item = QtGui.QStandardItem(name)
                name_item.setCheckable(True)
                name_item.setEditable(True)
                name_item.setTristate(False)
                name_item.setCheckState(tristate_dict[group][name])
                ori_name_item = QtGui.QStandardItem(name)
                ori_name_item.setCheckable(False)
                ori_name_item.setEditable(False)
                group_item.appendRow([name_item, ori_name_item])
                tristate.append(tristate_dict[group][name])

            # The parent (group) takes the state of the children (if all the same)
            if tristate.count(tristate[0]) == len(tristate):
                group_item.setCheckState(tristate[0])
            else:
                group_item.setCheckState(QtCore.Qt.CheckState.PartiallyChecked)     
            self.files_editable_cohort_model.appendRow([group_item, ori_group_item])       

        # Add the new created model to the view
        self.treeView_cohort.setModel(self.files_editable_cohort_model) 
        self.files_editable_cohort_model.sort(0)
        # connect the checkbox state and editable labels to the item selection
        self.files_editable_cohort_model.itemChanged.connect(self.item_changed_cohort_slot) 


    # Called when a file is removed in the step "1-Input Files".
    def remove_files(self, file_to_rem, model):
        # Pass through the files to remove row for each column
        column=0
        row_to_rem = []
        for filename in file_to_rem :
            file_item = model.findItems(os.path.basename(filename), flags=QtCore.Qt.MatchExactly, column=column)
            row_to_rem.append(file_item[0].row())
            # # clean dict if modifications were made to the file removed
            # if filename in self.dict_drop.keys():
            #     del self.dict_drop[filename]
            if filename in self.dict_rename.keys():
                del self.dict_rename[filename]
        # Remove the last first to avoid changing the index file
        row_to_rem.sort(reverse=True)
        for row in row_to_rem:
            model.removeRow(row)
        return model        


    # Called when the user press refresh push button
    def refresh_view_slot(self):
        self.files_editable_subject_model.itemChanged.connect(self.on_item_changed)
        self.files_editable_subject_model.sort(0)
        self.files_editable_cohort_model.itemChanged.connect(self.item_changed_cohort_slot)
        self.update_editable_cohort_model()


    # Called when the user press Export push button
    # To display the modification about to be done in a table
    def export_modifications_slot(self):    
        
        # self.dict_drop
        #   the key is the filename and the value is the list of tuple of group/name to drop
        #   ex. [('group1', 'name1'), ('group2', 'name2')]

        # self.dict_rename
        #   the key is the filename and the value is the list of tuple of group/name to rename
        #   [(group1_ori, name1_ori, group1_new, name1_new)
        #   (group2_ori, name2_ori, group2_new, name2_new)] 

        # Create a list of 5 columns ('original group', 'original name', 'new group', 'new name', 'file') 
        #   if the group or the name has been renamed.
        rename_annot_all_files = []
        for file_key, renaming_list in self.dict_rename.items():
            rename_annot = [[tup_g, tup_n, tup_gn, tup_nn, file_key] for tup_g, tup_n, tup_gn, tup_nn in renaming_list if ((not tup_g==tup_gn) or (not tup_n==tup_nn))]
            rename_annot_all_files.append(rename_annot)
        rename_annot_flat = [item for row in rename_annot_all_files for item in row]
        table_df = pd.DataFrame(data=rename_annot_flat,columns=['original group', 'original name', 'new group', 'new name', 'file'])
        table_edit_msg = TableDialog(df=table_df, title="Edits to apply",message="Those edits will be made at runtime.", showDownloadButton=True)
        table_edit_msg.exec_()

        self.dict_drop = self.get_dict_drop_from_editable_model()
        drop_annot = []
        for file_key, drop_list in self.dict_drop.items():
            if len(drop_list)>0:
                for drop_tup in drop_list:
                    drop_conv_lst = list(drop_tup)
                    drop_conv_lst.append(file_key)
                    drop_annot.append(drop_conv_lst)
        if len(drop_annot)>0:
            table_df = pd.DataFrame(data=drop_annot,columns=['group', 'name', 'file'])
        else:
            table_df = pd.DataFrame(None,columns=['group', 'name', 'file'])
        table_drop_msg = TableDialog(df=table_df, title="Annotations to remove",message="Those annotations will be removed at runtime.", showDownloadButton=True)
        table_drop_msg.exec_()
"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the CsvReaderMaster plugin
"""

from qtpy import QtWidgets, QtCore, QtGui

from CEAMSModules.CsvReaderMaster.Ui_CsvReaderMasterSettingsView import Ui_CsvReaderMasterSettingsView
from commons.BaseSettingsView import BaseSettingsView
from widgets.WarningDialog import WarningDialog


import numpy as np
import pandas as pd

DEBUG = False

class CsvReaderMasterSettingsView( BaseSettingsView,  Ui_CsvReaderMasterSettingsView, QtWidgets.QWidget):
    """
        CsvReaderMasterSettingsView is the view to define parameters to read properly the input file.
        The data read can be organized in different models to suit different views.

        self.files_model : the model for the PSG Files lists 
            (event if the PSG files list here is a widget, tools can need to have a model for their views)


    """
    # To send a signal each time the self.files_model is modified
    #   It allows to define QtCore.Slot() to do action each time the self.files_model is modified
    model_updated_signal = QtCore.Signal()

    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        self.filenames = []
        # Subscribe to the proper topics to send/get data from the node
        self._files_topic = f'{self._parent_node.identifier}.files'
        self._pub_sub_manager.subscribe(self, self._files_topic)
        self._input_as_time_topic = f'{self._parent_node.identifier}.input_as_time'
        self._pub_sub_manager.subscribe(self, self._input_as_time_topic)  
        self._group_topic = f'{self._parent_node.identifier}.group_col_i'
        self._pub_sub_manager.subscribe(self, self._group_topic)
        self._event_name_topic = f'{self._parent_node.identifier}.name_col_i'
        self._pub_sub_manager.subscribe(self, self._event_name_topic)
        self._onset_topic = f'{self._parent_node.identifier}.onset_col_i'
        self._pub_sub_manager.subscribe(self, self._onset_topic)        
        self._duration_topic = f'{self._parent_node.identifier}.duration_col_i'
        self._pub_sub_manager.subscribe(self, self._duration_topic)    
        self._channel_topic = f'{self._parent_node.identifier}.channels_col_i'
        self._pub_sub_manager.subscribe(self, self._channel_topic)    
        self._sample_rate_topic = f'{self._parent_node.identifier}.sample_rate'
        self._pub_sub_manager.subscribe(self, self._sample_rate_topic)
        self._event_center_topic = f'{self._parent_node.identifier}.event_center'
        self._pub_sub_manager.subscribe(self, self._event_center_topic)
        self._file_sep_topic = f'{self._parent_node.identifier}.file_separator'
        self._pub_sub_manager.subscribe(self, self._file_sep_topic)                
        self._fixed_dur_topic = f'{self._parent_node.identifier}.fixed_dur'
        self._pub_sub_manager.subscribe(self, self._fixed_dur_topic) 
        self._personnalized_header_topic = f'{self._parent_node.identifier}.personnalized_header'
        self._pub_sub_manager.subscribe(self, self._personnalized_header_topic)   
        self._file_sep_topic = f'{self._parent_node.identifier}.file_separator'
        self._pub_sub_manager.subscribe(self, self._file_sep_topic)   

        self.files_model = QtGui.QStandardItemModel(0,1) 


    def load_files_from_data(self, data):
        self.fileListWidget.clear()
        self.files_model = QtGui.QStandardItemModel(0,1) 
        for filename in data:
            # Add files to listView
            self.fileListWidget.addItem(filename)
            # tree item : parent=file, child=name
            item = QtGui.QStandardItem(filename)
            self.files_model.appendRow(item) 
        # Generate a signal to inform that self.files_model has been updated
        self.model_updated_signal.emit() 


    def clear_list_slot(self):
        self.fileListWidget.clear()
        # Clear the model
        # Important to remove the last row first since the model is updated after each removeRow
        # we dont want to change file index.
        for row in range(self.files_model.rowCount()-1,-1,-1):
            self.files_model.removeRow(row)
        # Generate a signal to inform that self.files_model has been updated
        self.model_updated_signal.emit()         


    # Called when the settingsView is opened by the user
    # The node asks to the publisher the settings
    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._input_as_time_topic, 'ping')
        self._pub_sub_manager.publish(self, self._group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_name_topic, 'ping')
        self._pub_sub_manager.publish(self, self._onset_topic, 'ping')
        self._pub_sub_manager.publish(self, self._duration_topic, 'ping')
        self._pub_sub_manager.publish(self, self._channel_topic, 'ping')
        self._pub_sub_manager.publish(self, self._sample_rate_topic, 'ping')
        self._pub_sub_manager.publish(self, self._event_center_topic, 'ping')
        self._pub_sub_manager.publish(self, self._file_sep_topic, 'ping')
        self._pub_sub_manager.publish(self, self._fixed_dur_topic, 'ping') 
        self._pub_sub_manager.publish(self, self._personnalized_header_topic, 'ping') 
        self._pub_sub_manager.publish(self, self._files_topic, 'ping')


    # Called when the user clicks on "Apply"
    def on_apply_settings(self):
        # Send the settings to the publisher for inputs to CsvReaderMaster
        items = []
        for x in range(self.fileListWidget.count()):
            items.append(self.fileListWidget.item(x).text())
        self._pub_sub_manager.publish(self, self._files_topic, items)
        self._pub_sub_manager.publish(self, self._input_as_time_topic, \
            str(int(self.time_radiobutton.isChecked())))
        self._pub_sub_manager.publish(self, self._group_topic, \
            str(self.group_spinbox.value()))
        self._pub_sub_manager.publish(self, self._event_name_topic, \
            str(self.event_name_spinbox.value()))
        self._pub_sub_manager.publish(self, self._onset_topic, \
            str(self.onset_spinbox.value()))
        self._pub_sub_manager.publish(self, self._duration_topic, \
            str(self.duration_spinbox.value()))
        self._pub_sub_manager.publish(self, self._channel_topic, \
            str(self.channel_spinBox.value()))            
        self._pub_sub_manager.publish(self, self._sample_rate_topic, \
            str(self.sample_rate_lineedit.text()))
        self._pub_sub_manager.publish(self, self._event_center_topic, \
            str(int(self.center_checkBox.isChecked())))
        if self.radioButton_comma.isChecked():
            self._pub_sub_manager.publish(self, self._file_sep_topic, ',')
        if self.radioButton_tab.isChecked():
            self._pub_sub_manager.publish(self, self._file_sep_topic, '\\t')
        self._pub_sub_manager.publish(self, self._fixed_dur_topic, \
            str(self.fixed_dur_lineEdit.text()))
        self._pub_sub_manager.publish(self, self._personnalized_header_topic, \
            str(int(self.personnalized_header_checkBox.isChecked())))


    # Slot called when user wants to add files
    def on_choose(self):
        filenames_add, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, 
            'Open CSV, TSV or TXT file', 
            None, 
            'CSV TSV (*.csv *.tsv *.txt)')
        if filenames_add != '':
            # Fill the QListWidget
            for filename in filenames_add:
                self.fileListWidget.addItem(filename)
                # tree item : parent=file, child=name
                item = QtGui.QStandardItem(filename)
                self.files_model.appendRow(item) 
            # Generate a signal to inform that self.files_model has been updated
            self.model_updated_signal.emit() 


    # Slot called when user changes the radio box
    def on_input_format_changed(self):
        print("on_input_format_changed")
        if self.time_radiobutton.isChecked():
            self.sample_rate_lineedit.setEnabled(False)
        else:
            self.sample_rate_lineedit.setEnabled(True)


    # Called when user checks Disable duration column
    def on_event_pos_changed(self):
        if self.duration_spinbox.value()==0:
            self.fixed_dur_lineEdit.setEnabled(True)
        else:
            self.fixed_dur_lineEdit.setEnabled(False)

    def on_topic_update(self, topic, message, sender):
        pass

    # Called by the publisher to init settings in the SettingsView
    def on_topic_response(self, topic, message, sender):
        if DEBUG: print(f'CsvReaderMasterSettingsView.on_topic_update:{topic} message:{message}')
        if topic == self._files_topic:
            self.load_files_from_data(message)
        # Exclusive radio button : only check the one checked
        if topic == self._input_as_time_topic:
            if message=='1':
                self.time_radiobutton.setChecked(True)
            else:
                self.sample_radiobutton.setChecked(True)        
        if topic == self._group_topic:
            self.group_spinbox.setValue(int(message))
        if topic == self._event_name_topic:
            self.event_name_spinbox.setValue(int(message))
        if topic == self._onset_topic:
            self.onset_spinbox.setValue(int(message))
        if topic == self._duration_topic:
            self.duration_spinbox.setValue(int(message))
        if topic == self._channel_topic:
            self.channel_spinBox.setValue(int(message))
        if topic == self._sample_rate_topic:
            self.sample_rate_lineedit.setText(message)        
        if topic == self._event_center_topic:
            self.center_checkBox.setChecked(int(message))   
        if topic == self._file_sep_topic:
            if message == ',':
                self.radioButton_comma.setChecked(True)
            elif message == '\\t':
                self.radioButton_tab.setChecked(True)
        if topic == self._fixed_dur_topic:
            self.fixed_dur_lineEdit.setText(message)
        if topic == self._personnalized_header_topic:
            self.personnalized_header_checkBox.setChecked(int(message))  


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._files_topic)
            self._pub_sub_manager.unsubscribe(self, self._input_as_time_topic)  
            self._pub_sub_manager.unsubscribe(self, self._group_topic)
            self._pub_sub_manager.unsubscribe(self, self._event_name_topic)
            self._pub_sub_manager.unsubscribe(self, self._onset_topic)
            self._pub_sub_manager.unsubscribe(self, self._duration_topic)
            self._pub_sub_manager.unsubscribe(self, self._channel_topic)
            self._pub_sub_manager.unsubscribe(self, self._sample_rate_topic)
            self._pub_sub_manager.unsubscribe(self, self._event_center_topic)
            self._pub_sub_manager.unsubscribe(self, self._file_sep_topic)
            self._pub_sub_manager.unsubscribe(self, self._fixed_dur_topic)  
            self._pub_sub_manager.unsubscribe(self, self._personnalized_header_topic)     

    #-----------------------------------------------------------------------------------------------
    # Many functions to manage models and views.  No called by the SettingsView but can be called by tools.
    #-----------------------------------------------------------------------------------------------

    # Creates an empty model to display the unique list of names for a selected file.
    def create_empty_files_names_model(self):
        files_model = QtGui.QStandardItemModel(0, 1)
        files_model.setHeaderData(0, QtCore.Qt.Horizontal, 'Event Name')
        files_model.setHorizontalHeaderLabels(['Name'])
        return files_model


    # Create checkable item based on self.files_model to select events
    def create_files_model_checkable(self):
        # Create an empty model based with the column Group-Name and Count
        files_check_event_model = self.create_empty_files_names_model()
        files_lst = self.get_files_list(self.files_model)
        # Create checkable item
        for filename in files_lst:
            # tree item : parent=file, child=name
            item = self.create_file_item_tree(filename, True)
            files_check_event_model.appendRow(item)
        return files_check_event_model


    # Return an tree item to display the name : parent=file, child=events name list
    def create_file_item_tree(self, filename, check_state):
        file_item = QtGui.QStandardItem(filename)

        file_separator = '\\t' if self.radioButton_tab.isChecked() else ','
        try:
            events = pd.read_csv(filename, sep=file_separator, usecols=[self.event_name_spinbox.value()-1], \
                                engine='python', header=0, encoding='utf_8', names=['name'])
        except:
            WarningDialog(f"The file {filename} cannot be read properly. Check the access. Check that the separator is correct.")
           
        # Get a list of unique groups
        names = events['name'].unique().tolist()
        # Strip the @@channel
        names_strip = [list(new_name.split("@@"))[0] if (isinstance(new_name,str) and '@@' in new_name) else new_name for new_name in names]
        names_strip = list(set(names_strip))
        names_strip.sort()

        # Form a tree of standardItem for the name of events 
        for name in names_strip:
            name_item = QtGui.QStandardItem(name)
            if check_state:
                name_item.setCheckable(check_state)
            file_item.appendRow(name_item)

        return file_item


    # Create editable item based (group) on self.files_model
    def create_files_group_model_editable(self, default_event_group):
        # Create an empty model based with the column Group-Name
        files_editable_event_model = QtGui.QStandardItemModel(0, 2)
        files_editable_event_model.setHeaderData(0, QtCore.Qt.Horizontal, 'Name')
        files_editable_event_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Group')
        files_editable_event_model.setHorizontalHeaderLabels(['Name','Group'])
        files_lst = self.get_files_list(self.files_model)
        # Create checkable item
        for filename in files_lst:
            # tree item : parent=file, child=name (non editable), child=group (editable)
            item = self.create_file_item_name_group_list(filename, default_event_group)
            files_editable_event_model.appendRow(item)
        return files_editable_event_model


    # Return an tree item to edit the group : parent=file, column 0 : child=events name list, column 1 : child=event group list
    def create_file_item_name_group_list(self, filename, default_event_group):
        file_item = QtGui.QStandardItem(filename)

        file_separator = '\\t' if self.radioButton_tab.isChecked() else ','
        events = pd.read_csv(filename, sep=file_separator, usecols=[self.event_name_spinbox.value()-1], \
                            engine='python', header=0, encoding='utf_8', names=['name'])

        # Get a list of unique groups
        names = events['name'].unique().tolist()
        # Strip the @@channel
        names_strip = [list(new_name.split("@@"))[0] if (isinstance(new_name,str) and '@@' in new_name) else new_name for new_name in names]
        names_strip = list(set(names_strip))
        names_strip.sort()

        # Form a tree of standardItem for the name of events 
        for name in names_strip:
            name_item = QtGui.QStandardItem(name)
            name_item.setEditable(False)
            name_item.setCheckable(False)
            group_item = QtGui.QStandardItem('')
            group_item.setCheckable(False)
            group_item.setEditable(True)
            group_item.setText(default_event_group)
            file_item.appendRow([name_item, group_item])

        return file_item


    # To get the files list in the list view.
    def get_files_list(self, model):
        file_list = []
        for i_f in range(model.rowCount()):
            item = model.item(i_f)
            file_list.append(item.text())        
        return file_list


    # Return the index of a filename
    def get_file_index(self, filename, files_model):
        # Find in the model the current file item
        # Returns an item only (not a list)
        file_item = self.get_file_item(filename, files_model)
        if (file_item is not None):
            # Extract the index of the item
            return files_model.indexFromItem(file_item)
        else:
            return None


    # Return filename from an index
    def get_file_name(self, file_index):
        file_item = self.files_model.itemFromIndex(file_index)
        if (file_item is not None) and (isinstance(file_item,list)):
            if len(file_item)>0:
                file_item = file_item[0]
        return file_item.text()


    # Return the item of a filename
    def get_file_item(self, filename, files_model):
        file_item = files_model.findItems(filename, flags=QtCore.Qt.MatchExactly, column=0)
        if (file_item is not None) and (isinstance(file_item,list)):
            if len(file_item)>0:
                return file_item[0]
            else:
                return file_item
        else:
            return None


    def get_checked_event_lst_from_file(self, files_check_model, file_index):
        """
        Return the selected events (event checked) of a file index.
        
        Parameters
        -----------
            files_check_model : QtGui.QStandardItemModel
            file_index : QtCore.QModelIndex
        Returns
        -----------    
            name_list : list of string
        """
        n_names = files_check_model.rowCount(file_index)
        file_item = files_check_model.itemFromIndex(file_index)
        name_list = []
        for i_c in range(n_names):
            child_item = file_item.child(i_c)
            if child_item is not None:
                if child_item.checkState()==QtCore.Qt.CheckState.Checked:
                    name_list.append(child_item.text())
        return name_list


    def get_name_group_from_file(self, files_editable_model, file_index):
        """
        Return a dict of events name with its editable group of a file index.
        
        Parameters
        -----------
            files_check_model : QtGui.QStandardItemModel
            file_index : QtCore.QModelIndex
        Returns
        -----------    
            name_group_dict : dict
                keys are the event name
                values are the event group
        """
        n_names = files_editable_model.rowCount(file_index)
        file_item = files_editable_model.itemFromIndex(file_index)
        name_group_dict = {}
        for i_c in range(n_names):
            # PySide2.QtGui.QStandardItem.child(row[, column=0])
            name_item = file_item.child(i_c, 0)
            group_item = file_item.child(i_c, 1)
            if (name_item is not None) and (group_item is not None):
                name_group_dict[name_item.text()]=group_item.text()
        return name_group_dict


    def set_check_state_list(self, files_check_model, file_index, name_list, check_state):
        """
        Set the CheckState to events listed in name_list.
        
        Parameters
        -----------
            files_check_model : QtGui.QStandardItemModel
            file_index : QtCore.QModelIndex
            name_list : list of string
            check_state : QtCore.Qt.CheckState
        Returns
        ----------- 
            files_check_model :  QtGui.QStandardItemModel
            evt_found_tab : array of number of events
        """
        # By default the events are not found
        evt_found_tab = np.zeros((1,len(name_list)))
        # Extract the file index from the model
        n_names_model = files_check_model.rowCount(file_index)
        for i_event_2_sel, name_2_sel in enumerate(name_list):
            for i_name_model in range(n_names_model):  
                column = 0
                name_index = files_check_model.index(i_name_model, column, file_index)
                name_item = files_check_model.itemFromIndex(name_index)
                # If the group from the model needs to be checked 
                if name_item.text()==name_2_sel:
                    if len(name_list)==1:
                        evt_found_tab[i_event_2_sel] = 1
                    else:
                        evt_found_tab[0,i_event_2_sel] = 1
                    name_item.setCheckState(check_state)
                         
        return files_check_model, evt_found_tab


    def set_groups_from_dict(self, files_editable_model, file_index, name_group_dict):
        """
        Set the group of events as defined in the name_group_dict.
        
        Parameters
        -----------
            files_editable_model : QtGui.QStandardItemModel
            file_index : QtCore.QModelIndex
            name_group_dict : dict
                keys are the event name
                values are the event group
        Returns
        ----------- 
            files_editable_model :  QtGui.QStandardItemModel
            evt_found_tab : array of number of events
        """
        # By default the events are not found
        evt_found_tab = np.zeros((1,len(name_group_dict)))
        # Extract the file index from the model
        n_events_model = files_editable_model.rowCount(file_index)
        for i_event in range(n_events_model):
            name_index = files_editable_model.index(i_event, 0, file_index)
            name_item = files_editable_model.itemFromIndex(name_index)
            group_index = files_editable_model.index(i_event, 1, file_index)
            group_item = files_editable_model.itemFromIndex(group_index)
            if name_item.text() in name_group_dict.keys():
                group_item.setText(name_group_dict[name_item.text()])
                if len(name_group_dict)==1:
                    evt_found_tab[i_event] = 1
                else:
                    evt_found_tab[0,i_event] = 1                  
        return files_editable_model, evt_found_tab


    def set_check_state_file(self, file_index, check_state, files_check_model):
        """
        Set the CheckState to all groups and names of a file index selected
        
        Parameters
        -----------
            file_index : QtCore.QModelIndex
            check_state : QtCore.Qt.CheckState
            files_check_model : QtGui.QStandardItemModel
        Returns
        ----------- 
            files_check_model :  QtGui.QStandardItemModel
        usage 
        -----------
            model = set_check_state_file(index, check_state, model)
        """
        n_names = files_check_model.rowCount(file_index)
        for name_row in range(n_names):
            column = 0
            name_index = files_check_model.index(name_row, column, file_index)
            name_item = files_check_model.itemFromIndex(name_index)
            name_item.setCheckState(check_state)
        return files_check_model
"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Copy of the settings viewer of the PSGReader plugin.
    The settings viewer has been adapted because the SlowWaveImages plugin is 
    run without master process.  The whole list of PSG file is read and compiled
    in order to generate images of the cohort.
"""
import numpy as np
import os
import pandas as pd
from qtpy import QtWidgets
from qtpy import QtCore
from qtpy import QtGui
from qtpy.QtCore import Qt, QTimer
from qtpy.QtWidgets import QProgressDialog
import sys

from commons.BaseStepView import BaseStepView
from commons.CheckBoxDelegate import CheckBoxDelegate
from widgets.WarningDialog import WarningDialog

from CEAMSModules.PSGReader.PSGReaderManager import PSGReaderManager
from CEAMSModules.PSGReader.MontagesTableModel import MontagesTableModel
from CEAMSModules.PSGReader.MontagesProxyModel import MontagesProxyModel
from CEAMSModules.PSGReader.ChannelsTableModel import ChannelsTableModel
from CEAMSModules.PSGReader.ChannelsProxyModel import ChannelsProxyModel
from CEAMSTools.SlowWaveImages.InputFilesStep.Ui_InputFilesStep import Ui_InputFilesStep


DEBUG = False

class InputFilesStep( BaseStepView,  Ui_InputFilesStep, QtWidgets.QWidget):
    
    context_files_view      = "input_files_settings_view"

    """ InputFilesStep display the settings. """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._sw_wave_pics_node = "34950575-1519-44e1-852d-a7720eead65f" # identifier for slow wave pics generator

        # init UI
        self.setupUi(self)
        self.montages_tableview.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        self.channels_tableview.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)

        # init 
        self.files_details = {}

        # Init EEG reader modules
        self._psg_reader_manager = PSGReaderManager()
        self._psg_reader_manager._init_readers()

        # Init table models
        self.files_model = self.create_empty_files_model()

        self.files_listview.setModel(self.files_model)
        self.events_treeView.setModel(self.files_model)
        self.init_montage_table_model()
        self.init_channels_table_model()

        # itemChanged is a signal in QStandardItemModel Class
        # Connect itemChanged to the slot on_item_changed allows to perform 
        self.files_model.itemChanged.connect(self.on_file_selection_changed)
        
        # Subscribe to the proper topics to send/get data from the node
        self._files_topic = f'{self._sw_wave_pics_node}.files'
        self._pub_sub_manager.subscribe(self, self._files_topic)

        self.frame_montages.setVisible(True)
        self.frame_channels.setVisible(True)

        self._context_manager[self.context_files_view] = self

        self._emit_timer = QTimer()
        self._emit_timer.setSingleShot(True)
        self._emit_timer.timeout.connect(self._emit_timeout_reached)


    def on_topic_update(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            at any update, does not necessary answer to a ping.
            To listen to any modification not only when you ask (ping)
        """
        if DEBUG: print(f'InputFilesStep.on_topic_update:{topic} message:{message}')


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            Called after a ping.
        """
        if DEBUG: print(f'InputFilesStep.on_topic_response:{topic} message:{message}')
        if topic == self._files_topic:
            self.load_files_from_data(message)


    def load_files_from_data(self, data):
        """  Called to load files asked (saved) in the file list.
             data is a dict with the parameters to init PSGReader.files input.
             Each key of the dict data is the filename of the PSG file loaded.
        """
        self.files_model.clear()
        self.files_model.setColumnCount(2)
        self.files_model.setHorizontalHeaderLabels(['Group-Name', 'Count'])

        # Clear old data
        self.montages_table_model._data = self.montages_table_model._data[0:0]
        self.channels_table_model._data = self.channels_table_model._data[0:0]
        
        # Create file details and add filenames to the listWidget
        self.files_details = {}
        removed_files = []
        for filename in data:
            # Check if the file exist
            if not os.path.isfile(filename):
                removed_files.append(filename)
                continue

            self.files_details[filename] = {
                'event_groups':data[filename]['event_groups'],
                #'events':data[filename]['events']
            }
            
            # tree item : parent=file, child=group and count, child=name and count
            item = self.create_file_item_count(filename)
            self.files_model.appendRow(item) 

            # For each file, load its montages in the montages table model
            for montage in data[filename]['montages']:
                is_selected = data[filename]['montages'][montage]['is_selected']
                montage_index = data[filename]['montages'][montage]['montage_index']
                # Get the channels of this montage
                channels = data[filename]['montages'][montage]['channels']
                channels_text = ','.join([ch for ch in channels])
                ## Add montages to tableView
                montage_dict = {
                    'Use':is_selected, 
                    'Montage':montage,
                    'Filename':filename,
                    'Channels':channels_text,
                    'Index':montage_index
                    }
                self.montages_table_model._data = pd.concat([self.montages_table_model._data,pd.DataFrame(data=montage_dict, index=[0])], ignore_index=True)

                # For each montage, load its channels in the channels table model
                for channel in data[filename]['montages'][montage]['channels']:
                    ch = data[filename]['montages'][montage]['channels'][channel]
                    is_selected = ch['is_selected']
                    sample_rate = ch['sample_rate']

                    channel_dict = {
                    'Use':is_selected, 
                    'Channel':channel,
                    'Sample rate':sample_rate,
                    'Montage':montage,
                    'Filename':filename
                    }
                    self.channels_table_model._data = pd.concat([self.channels_table_model._data,pd.DataFrame(data=channel_dict, index=[0])], ignore_index=True)

        if len(removed_files) > 0:
            error_message = "These files were removed from the selection because they could not be found:\n"
            for filepath in removed_files:
                error_message = error_message + filepath + "\n"

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText(error_message)
            msg.setWindowTitle("File not found")
            msg.exec()

        # Invalide the models so it refreshes the UI
        self.montages_proxy_model.invalidate()
        self.montages_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly
        self.channels_proxy_model.invalidate()
        self.channels_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly
        self.on_montages_selection_changed()

        # Update the context to notify that the files model has been updated
        self._context_manager[self.context_files_view] = self
        

    # Create an empty model based with the column Group-Name and Count
    def create_empty_files_model(self):
        files_model = QtGui.QStandardItemModel(0, 2)
        files_model.setHeaderData(0, QtCore.Qt.Horizontal, 'Group-Name')
        files_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Count')
        files_model.setHorizontalHeaderLabels(['Group-Name', 'Count'])
        return files_model


    # Create an empty model based with the column Group-Name and Count
    def create_empty_edit_files_model(self):
        files_model = QtGui.QStandardItemModel(0, 2)
        files_model.setHeaderData(0, QtCore.Qt.Horizontal, 'Group-Name')
        files_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Original label')
        files_model.setHorizontalHeaderLabels(['Group-Name', 'Original label'])
        return files_model


    def init_montage_table_model(self):
        self.df_montages = pd.DataFrame([], columns = ['Use', 'Montage','Filename', 'Channels'])
        self.montages_table_model = MontagesTableModel(self.df_montages)
        self.montages_proxy_model = MontagesProxyModel(self)
        self.montages_proxy_model.setSourceModel(self.montages_table_model)
        self.montages_proxy_model.setFilterKeyColumn(2)
        self.montages_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)

        self.montages_tableview.setModel(self.montages_proxy_model)
        self.montages_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly

        self.montage_use_delegate = CheckBoxDelegate(None)
        self.montage_use_delegate.set_on_change_callback(self.on_montages_selection_changed)

        self.montages_tableview.setItemDelegateForColumn(0, self.montage_use_delegate)


    def init_channels_table_model(self):
        self.df_channels = pd.DataFrame([], columns = ['Use', 'Channel','Sample rate', 'Montage', 'Filename'])
        self.channels_table_model = ChannelsTableModel(self.df_channels)
        self.channels_proxy_model = ChannelsProxyModel(self)
        self.channels_proxy_model.setSourceModel(self.channels_table_model)
        self.channels_proxy_model.setFilterKeyColumn(2)
        self.channels_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)

        self.channels_tableview.setModel(self.channels_proxy_model)
        self.channels_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly
        
        self.channel_use_delegate = CheckBoxDelegate(None)
        self.channels_tableview.setItemDelegateForColumn(0, self.channel_use_delegate)

        # Connect the data_changed signal from channels_table_model to the on_channels_selection_changed
        self.channels_table_model.dataChanged.connect(self.on_channels_selection_changed)


    def on_add_files(self):
        dlg = QtWidgets.QFileDialog()
        #dlg.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        dlg.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        dlg.setNameFilters(self._psg_reader_manager.get_file_extensions_filters())

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            # Add the file only if is it not already added
            for filename in filenames:
                matches = self.files_model.findItems(os.path.basename(filename),QtCore.Qt.MatchExactly)
                if len(matches) == 0:
                    success = self.load_file_info(filename) # self._psg_reader_manager is used

                    if success:
                        # tree item : parent=file, child=group and count, child=name and count
                        item = self.create_file_item_count(filename) # The file is read
                        self.files_model.setColumnCount(2)
                        self.files_model.appendRow(item)           
                    
            # Update the context to notify that the files model has been updated
            self._context_manager[self.context_files_view] = self

        for i in range(self.files_model.columnCount()):
            self.events_treeView.hideColumn(i)


    # Return an tree item : parent=file, child=group and count, child=name and count
    def create_file_item_count(self, filename):
        """
        Create an file item as parent with its children : group and count, name and count.
        The file "filename" is opened and its events are read.
            
            Parameters
            -----------
                filename    : string
                    filename as a text to add to the item.
            Returns
            ----------- 
                file_item :  QtGui.QStandardItem
                    A tree item : parent=file, child=group and count, child=name and count
            usage 
            -----------
                file_item = create_file_item_count(filename)
        """

        file_item = QtGui.QStandardItem(os.path.basename(filename))
        file_item.setToolTip(filename)
        file_item.setData(filename, Qt.UserRole + 1)
        self._psg_reader_manager.open_file(filename)
        stages = self._psg_reader_manager.get_sleep_stages()
        events = self._psg_reader_manager.get_events()
        self._psg_reader_manager.close_file()

        # First step, organize the list of events in a dictionary where the key
        # is the name of group and the value is another dictionary for its
        # list of items. The value of the second dictionary is the total count of
        # event of this kind.
        
        # Initialize an empty dictionary to store the events and their counts for each group
        events_groups = {}

        # Group the events by 'group' and 'name' columns, count the number of events in each group, and create a new dataframe with the count
        group_df = events.groupby(['group', 'name']).size().reset_index(name='count')

        # Get a list of unique groups
        groups = group_df['group'].unique().tolist()

        # Iterate over the groups
        for group in groups:
            # Filter the group_df to only get the events for this group
            list_of_event_for_this_group = group_df[group_df['group'] == group]
            # Create a dictionary where the key is the event name and the value is the count
            event_count_dict = list_of_event_for_this_group.set_index('name')['count'].to_dict()
            # Add the dictionary for this group to the events_groups dictionary
            events_groups[group] = event_count_dict

        # Second step, form a tree of standardItem for the group of events and their events
        # from this dictionary.
        for group in events_groups:
            total_events_count = sum(events_groups[group].values())
            group_item = QtGui.QStandardItem(group)
            group_count_item = QtGui.QStandardItem(str(total_events_count))
            for event in events_groups[group].items():
                name_item = QtGui.QStandardItem(event[0])
                count_item = QtGui.QStandardItem(str(event[1]))
                group_item.appendRow([name_item, count_item])

            # Set the scoring status
            file_item.appendRow([group_item,group_count_item])
            if len(stages)==0:
                file_item.setData('unscored', Qt.UserRole + 2)
            elif any(stages['name']!='9'):
                file_item.setData('scored', Qt.UserRole + 2)
            else:
                file_item.setData('unscored', Qt.UserRole + 2)

        return file_item


    # Return an tree item : parent=file, child=group and count, child=name and count
    def make_checkable_file_item_count(self, filename, model):
        """
        Make the file item children checkable but not checked (file item is copied from model)
        Copy a file item as parent and make its children checkable and checked : group and count, name and count.
            
            Parameters
            -----------
                filename    : string
                    filename as a text to add to the item.
                model : QtGui.QStandardItemModel
                    model to copy the tree item
            Returns
            ----------- 
                file_item :  QtGui.QStandardItem
                    A tree item : parent=file, child=group and count, child=name and count
            usage 
            -----------
                # create a checkable item copied from self.files_model
                file_item = make_checkable_file_item_count(filename, self.files_model) 
        """
        ori_file_item =self.get_file_item(filename, model)
        if not isinstance(ori_file_item, QtGui.QStandardItem):
            return None

        # Create a file item based on the original file item
        file_item = QtGui.QStandardItem(ori_file_item.text())
        file_item.setData(ori_file_item.data(Qt.UserRole + 1),Qt.UserRole + 1)

        # For all group and count children of the original file item
        for i_group in range(0, ori_file_item.rowCount()):
            # Create a new checkable item
            group_item = QtGui.QStandardItem(ori_file_item.child(i_group,0).text())
            group_count_item = QtGui.QStandardItem(ori_file_item.child(i_group,1).text())
            # Make checkable and check the state of the group_item
            group_item.setCheckable(True)
            group_item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            # For each child of the group_item
            for i_name in range(0, ori_file_item.child(i_group,0).rowCount()):
                name_item = QtGui.QStandardItem(ori_file_item.child(i_group,0).child(i_name,0).text())
                count_item = QtGui.QStandardItem(ori_file_item.child(i_group,0).child(i_name,1).text())
                # Make checkable and check the state of the name_item
                name_item.setCheckable(True)
                name_item.setCheckState(QtCore.Qt.CheckState.Unchecked)
                group_item.appendRow([name_item, count_item])
            # Add the new checkable item to the file_item
            file_item.appendRow([group_item, group_count_item])
        
        # Copy the scoring status
        file_item.setData(ori_file_item.data(Qt.UserRole + 2), Qt.UserRole + 2)

        return file_item


    def on_channel_search_changed(self, search_pattern):
        self.update_channels_filter()
    

    def on_add_folders(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        #file_dialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        file_view = file_dialog.findChild(QtWidgets.QListView, 'listView')

        if file_view:
            file_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        f_tree_view = file_dialog.findChild(QtWidgets.QTreeView)
        if f_tree_view:
            f_tree_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        if file_dialog.exec():
            folders = file_dialog.selectedFiles()

            for folder in folders:
                filenames = self._psg_reader_manager.find_psg_within_folder(folder)

                for filename in filenames:
                    matches = self.files_model.findItems(os.path.basename(filename),QtCore.Qt.MatchExactly)
                    if len(matches) == 0:
                        if filename is not None:
                            success = self.load_file_info(filename) # self._psg_reader_manager is used

                            if success:
                                # tree item : parent=file, child=group and count, child=name and count
                                item = self.create_file_item_count(filename) # The file is read
                                self.files_model.setColumnCount(2)
                                self.files_model.appendRow(item)    
                        else:
                            #TODO Log empty folders
                            # Couldnt find PSG file in folder:{folder}
                            pass
            # Update the context to notify that the files model has been updated
            self._context_manager[self.context_files_view] = self


    def on_channel_search_changed(self, search_pattern):
        self.update_channels_filter()


    def on_add_folders(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
        if not sys.platform.startswith("darwin"):
            file_dialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        file_view = file_dialog.findChild(QtWidgets.QListView, 'listView')

        if file_view:
            file_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        f_tree_view = file_dialog.findChild(QtWidgets.QTreeView)
        if f_tree_view:
            f_tree_view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        if file_dialog.exec():
            folders = file_dialog.selectedFiles()

            for folder in folders:
                filenames = self._psg_reader_manager.find_psg_within_folder(folder)

                for filename in filenames:
                    matches = self.files_model.findItems(os.path.basename(filename),QtCore.Qt.MatchExactly)
                    if len(matches) == 0:
                        if filename is not None:
                            success = self.load_file_info(filename) # self._psg_reader_manager is used

                            if success:
                                # tree item : parent=file, child=group and count, child=name and count
                                item = self.create_file_item_count(filename) # The file is read
                                self.files_model.setColumnCount(2)
                                self.files_model.appendRow(item)    
                        else:
                            #TODO Log empty folders
                            # Couldnt find PSG file in folder:{folder}
                            pass
            # Update the context to notify that the files model has been updated
            self._context_manager[self.context_files_view] = self

    
    # Called when the user press on Remove push button
    def on_remove_entries(self):
        # The rows have to be removed once all the models are updated because
        # the self.files_listview.selectedIndexes() is not in sync with the model
        # With this technic the multiple selection from top to bottom or bottom up works
        row_selected = [] # To keep track of the rows to remove from the model
        for index in self.files_listview.selectedIndexes():
            row_selected.append(index.row())
            filename_item = self.files_model.takeItem(index.row())
            filename = filename_item.data(Qt.UserRole + 1)

            self.montages_table_model.remove_by_filename(filename)
            self.montages_proxy_model.invalidate()
            self.montages_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly

            self.channels_table_model.remove_by_filename(filename)
            self.channels_proxy_model.invalidate()
            self.channels_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly

            self.files_details.pop(filename, None)
            #self.events_treeView.setTreePosition(-1)
            for i in range(self.files_model.columnCount()):
                self.events_treeView.hideColumn(i)

        # Important to remove the last row first since the model is updated after each removeRow
        # we dont want to change file index.
        row_selected.sort(reverse=True) 
        for row in row_selected:
            self.files_model.removeRow(row)

        # Update the context to notify that the files model has been updated
        self._context_manager[self.context_files_view] = self


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
       
        channels_info_df = self.channels_table_model.get_data()
        file_list = channels_info_df['Filename'].unique()
        if len(file_list)>0:
            # For each recording check the channel selection
            for file in file_list:
                chans_used = channels_info_df[(channels_info_df['Filename']==file) & (channels_info_df['Use']==True)]
                if len(chans_used)==0:
                    WarningDialog(f"At least one recording has no channel selected, check the channel selection of the file : {file}.")
                    return False
        else:
            WarningDialog(f"Add files before running the pipeline.")    
            return False
        return True   


    # Called when the user save a tool that include the InputFilesStep or 
    # press the "apply" push button of the settingsView
    def on_apply_settings(self):

        files = self.files_details.copy()

        # Get the data we'll need to record
        montages_df = self.montages_table_model.get_data()
        channels_df = self.channels_table_model.get_data()

        # We start by making a list of montages for all filenames
        for _, row in montages_df.iterrows():
            montage = row['Montage']
            filename = row['Filename']
            is_selected = row['Use']
            montage_index = row['Index']
            
            if 'montages' not in files[filename]:
                files[filename]['montages'] = {}

            files[filename]['montages'][montage] = {
                'is_selected':is_selected,
                'montage_index':montage_index,
                'channels':{}
            }

        # Then we add the channels to all montages
        for _, row in channels_df.iterrows():
            filename = row['Filename']
            montage = row['Montage']
            channel = row['Channel']
            is_selected = row['Use']
            sample_rate = row['Sample rate']

            files[filename]['montages'][montage]['channels'][channel] = {
                'is_selected':is_selected,
                'sample_rate':sample_rate
            }

        # Send the dictionary as an input to the PSGReader module
        self._pub_sub_manager.publish(self, self._files_topic, files)


    def on_export(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Export channels selection as',filter="*.tsv,*.txt")
        if filename is not None and filename:
            with open(filename, 'w') as tsv_file:
                export_df = self.channels_table_model._data.loc[self.channels_table_model._data['Use'] == True]
                export_df.to_csv(tsv_file, sep='\t', encoding="utf_8")
            

    def on_file_selection_changed(self):
        indexes = self.files_listview.selectedIndexes()
        files = []
        for index in indexes:
            files.append(self.files_model.itemFromIndex(index))
        # If only 1 file is selected, show its detail in the details text box
        if len(files) == 1:
            for i in range(self.files_model.columnCount()):
                self.events_treeView.showColumn(i)
            # Extract file index selected
            file_index = self.files_listview.currentIndex()
            self.events_treeView.setRootIndex(file_index)
            self.events_treeView.resizeColumnToContents(0)
        else:
            for i in range(self.files_model.columnCount()):
                self.events_treeView.hideColumn(i)
        filenames = [f.data(Qt.UserRole + 1) for f in files]
        self.montages_proxy_model.set_filenames_filters(filenames)
        # Update the montages selection to change the list of channels
        self.on_montages_selection_changed()


    def on_montages_selection_changed(self):
        self.channels_proxy_model.clear_filename_montage_pair_filter()
        montage_filename_pairs = []
        for row in range(self.montages_proxy_model.rowCount()):
            is_checked = self.montages_proxy_model.data(self.montages_proxy_model.index(row,0))
            if is_checked:
                montage = self.montages_proxy_model.data(self.montages_proxy_model.index(row,1))
                filename = self.montages_proxy_model.data(self.montages_proxy_model.index(row,2))
                montage_filename_pairs.append((montage, filename))
        self.channels_proxy_model.set_filename_montage_pair_filter(montage_filename_pairs)


    def on_montage_seach_changed(self):
        self.montages_proxy_model.set_montages_search_pattern(self.montage_search_lineedit.text())
        # Update the montages selection to change the list of channels
        self.on_montages_selection_changed()


    def on_montages_select_all(self):
        for row in range(self.montages_proxy_model.rowCount()):
            self.montages_proxy_model.setData(self.montages_proxy_model.index(row,0), True)
        self.on_montages_selection_changed()
        self.montages_proxy_model.invalidate()
        self.montages_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly


    def on_montages_unselect_all(self):
        for row in range(self.montages_proxy_model.rowCount()):
            self.montages_proxy_model.setData(self.montages_proxy_model.index(row,0), False)
        self.on_montages_selection_changed()
        self.montages_proxy_model.invalidate()
        self.montages_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly


    def on_channels_select_all(self):
        n_chans = self.channels_proxy_model.rowCount()
        progress = QProgressDialog("Selecting all channels...", "Abort", 0, n_chans)
        progress.setWindowModality(Qt.ApplicationModal)
        progress.setMinimumDuration(0) # Settings a minimum time greater than 0 makes the UI update slower
        progress.show()
        for row in range(n_chans):
            # if the row is a multiple of 100, update the progress bar
            if row % 200 == 0:
                progress.setValue(row)
            if progress.wasCanceled():
                break
            self.channels_proxy_model.setData(self.channels_proxy_model.index(row,0), True)
        progress.setValue(n_chans)
        self.channels_proxy_model.invalidate()
        self.channels_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly
        progress.close()


    def on_channels_unselect_all(self):
        n_chans = self.channels_proxy_model.rowCount()
        progress = QProgressDialog("Unselecting all channels...", "Abort", 0, n_chans, self)
        progress.setWindowModality(Qt.ApplicationModal)
        progress.setMinimumDuration(0)  # Settings a minimum time greater than 0 makes the UI update slower
        progress.show()
        for row in range(n_chans):
            # if the row is a multiple of 1000, update the progress bar
            if row % 200 == 0:
                progress.setValue(row)
            if progress.wasCanceled():
                break
            self.channels_proxy_model.setData(self.channels_proxy_model.index(row,0), False)
        progress.setValue(n_chans)
        self.channels_proxy_model.invalidate()
        self.channels_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly
        progress.close()


    def load_settings(self):
        self._pub_sub_manager.publish(self, self._files_topic, 'ping')

    def load_file_info(self, filename):
        """ Function to read the file, init the table montage model, the channel model and self.files_details.

            self.files_details[filename] = 
                'event_groups':event_groups,
        """
        success = self._psg_reader_manager.open_file(filename)

        if not success:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText(f"Could not open file. The format is not valid: {filename}")
            msg.setWindowTitle("File load error")
            msg.exec()
            return False

        # For each montage get the list of channels
        montages = self._psg_reader_manager.get_montages()

        # count list size
        count = 0
        for montage in montages:
            channels = self._psg_reader_manager.get_channels(montage.index)
            count = count + len(channels)

        total_uses = np.full(count, False)
        total_chs = np.empty(count, dtype=object)
        total_sample_rates = np.empty(count, dtype=object)
        total_montages = np.empty(count, dtype=object)
        total_filenames = np.empty(count, dtype=object)
        total_montage_indexes = np.empty(count, dtype=object)

        montage_uses = np.full(len(montages), False)
        montage_names = np.empty(len(montages), dtype=object)
        montage_filename = np.empty(len(montages), dtype=object)
        montage_channels = np.empty(len(montages), dtype=object)
        montage_indexes = np.empty(len(montages), dtype=object)

        index = 0
        for jdx, montage in enumerate(montages):
            channels = self._psg_reader_manager.get_channels(montage.index)
            channels_text = ','.join([ch.name for ch in channels])
            
            montage_uses[jdx] = False
            montage_names[jdx] = montage.name
            montage_filename[jdx] = filename
            montage_channels[jdx] = channels_text
            montage_indexes[jdx] = montage.index

            for channel in channels:
                total_chs[index] = channel.name
                total_sample_rates[index] = str(channel.sample_rate)
                total_montages[index] = montage.name
                total_filenames[index] = filename
                total_montage_indexes[index] = montage.index
                index = index + 1

        montage_dict = {
                    'Use':montage_uses,
                    'Montage':montage_names,
                    'Filename':montage_filename,
                    'Channels':montage_channels,
                    'Index':montage_indexes
                }
        self.montages_table_model._data = pd.concat([self.montages_table_model._data, pd.DataFrame(montage_dict)], ignore_index=True)
        data = {
            'Use':total_uses,
            'Channel':total_chs,
            'Sample rate':total_sample_rates,
            'Montage':total_montages,
            'Filename':total_filenames,
            'Montage Index':total_montage_indexes,
        }

        self.channels_table_model._data = pd.concat([self.channels_table_model._data, pd.DataFrame(data)], ignore_index=True)

        self.montages_proxy_model.invalidate()
        self.montages_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly

        self.on_montages_selection_changed()

        self.channels_proxy_model.invalidate()
        self.channels_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly

        event_groups = []
        for event_group in self._psg_reader_manager.get_event_groups():
            event_groups.append(event_group.name)
        self.files_details[filename] = {
            'event_groups':event_groups
        }

        self._psg_reader_manager.close_file()
        return True

    def update_channels_filter(self):
        self.channels_proxy_model.set_channels_search_pattern(self.search_channels_lineedit.text())
        self.channels_proxy_model.invalidate()
    
    # To get the files list in the list view.
    def get_files_list(self, model):
        file_list = []
        column_group = 0
        for i_f in range(model.rowCount()):
            item = model.item(i_f,column_group)
            file_list.append(item.data())        
        return file_list


    # To get the files list in the list view.
    def get_files_list(self, model):
        file_list = []
        column_group = 0
        for i_f in range(model.rowCount()):
            item = model.item(i_f,column_group)
            file_list.append(item.data(Qt.UserRole + 1))        
        return file_list


    # Return the index of a filename
    def get_file_index(self, filename, files_model):
        # Find in the model the current file item
        file_item = self.get_file_item(filename, files_model)
        # Extract the index of the item
        if isinstance(file_item, QtGui.QStandardItem):
            return files_model.indexFromItem(file_item)
        else:
            return []


    # Return the ith group item for a filename
    def get_group_item(self, filename, i_group, files_model):
        file_item = self.get_file_item(filename, files_model)
        return file_item.child(i_group)


    # Return the item of a filename
    def get_file_item(self, filename, files_model):
        file_item = files_model.findItems(os.path.basename(filename), flags=QtCore.Qt.MatchExactly, column=0)
        if file_item is not None:
            if len(file_item)>0:
                return file_item[0]
            else:
                return file_item
        else:
            return None
            

    # Return True if there is at least one valid sleep stage in the recording
    def is_stages_scored(self, filename, files_model):
        file_item = self.get_file_item(filename, files_model)
        if isinstance(file_item, QtGui.QStandardItem):
            scoring_status = file_item.data(Qt.UserRole + 2)
            if scoring_status=='scored':
                return True
            else:
                return False
        else:
            return False


    # Called when a event name state is changed
    def apply_state_to_parent_item(self, item, files_check_model):
        parent_item = item.parent()
        if parent_item is not None:
            #view_index = files_check_model.indexFromItem(parent_item)
            n_child = parent_item.rowCount()
            state_lst = []
            for i_c in range(n_child):
                child_item = parent_item.child(i_c)
                if child_item is not None:
                    state_lst.append(child_item.checkState())
            # The parent (group) takes the state of the children (if all the same)
            if state_lst.count(state_lst[0]) == len(state_lst):
                parent_item.setCheckState(item.checkState())
            else:
                parent_item.setCheckState(QtCore.Qt.CheckState.PartiallyChecked)
        return files_check_model


    # Called when a event group state is changed
    def apply_state_to_child_item(self, item, files_check_model):
        # view_index.row() is the group order or the name order
        # if the user checked the first name of the third group, the row is 0
        if not item.checkState()==QtCore.Qt.CheckState.PartiallyChecked:
            view_index = files_check_model.indexFromItem(item)
            if files_check_model.hasChildren(view_index):
                n_child = files_check_model.rowCount(view_index)
                for i_c in range(n_child):
                    child_item = item.child(i_c)
                    child_item.setTristate(False)
                    if child_item is not None:
                        child_item.setCheckState(item.checkState())
        return files_check_model


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
        n_groups = files_check_model.rowCount(file_index)
        for group_row in range(n_groups):
            column = 0
            group_index = files_check_model.index(group_row, column, file_index)
            group_item = files_check_model.itemFromIndex(group_index)
            group_item.setCheckState(check_state)
            files_check_model = self.apply_state_to_child_item(group_item, files_check_model)
        return files_check_model


    def set_check_state_list(self, files_check_model, file_index, group_lst, name_list, check_state):
        """
        Set the CheckState to events listed in group_lst and name_list.
        
        Parameters
        -----------
            files_check_model : QtGui.QStandardItemModel
            file_index : QtCore.QModelIndex
            group_lst : list of string 
            name_list : list of string
            check_state : QtCore.Qt.CheckState
        Returns
        ----------- 
            files_check_model :  QtGui.QStandardItemModel
            evt_found_tab : array of number of events
        """
        # By default the events are not found
        evt_found_tab = np.zeros((1,len(group_lst)))
        # Extract the file index from the model
        n_groups_model = files_check_model.rowCount(file_index)
        for i_event_2_sel, group_2_sel in enumerate(group_lst):
            for i_group_model in range(n_groups_model):  
                column = 0
                group_index = files_check_model.index(i_group_model, column, file_index)
                group_item = files_check_model.itemFromIndex(group_index)
                # If the group from the model needs to be checked 
                if group_item.text()==group_2_sel:
                    # Loop through all event names of the current group
                    for i_c in range(group_item.rowCount()):
                        name_item = group_item.child(i_c)
                        # If the event name exist, check the event and mark the tab as found
                        if name_item.text()==name_list[i_event_2_sel]:
                            if len(group_lst)==1:
                                evt_found_tab[i_event_2_sel] = 1
                            else:
                                evt_found_tab[0,i_event_2_sel] = 1
                            name_item.setCheckState(check_state)
                            # files_check_model.setItem(i_c, column, name_item)
                            # Set the parent state depending of children
                            files_check_model = self.apply_state_to_parent_item(name_item, files_check_model)                            
        return files_check_model, evt_found_tab


    def set_check_state_group(self, files_check_model, file_index, group_label, check_state):
        """
        Set the CheckState to events listed in group_lst and name_list.
        
        Parameters
        -----------
            files_check_model : QtGui.QStandardItemModel
            file_index : QtCore.QModelIndex
            group_label : string 
            check_state : QtCore.Qt.CheckState
        Returns
        ----------- 
            files_check_model :  QtGui.QStandardItemModel
        """
        # Extract the file index from the model
        n_groups_model = files_check_model.rowCount(file_index)
        for i_group_model in range(n_groups_model):  
            column = 0
            group_index = files_check_model.index(i_group_model, column, file_index)
            group_item = files_check_model.itemFromIndex(group_index)
            # If the group from the model needs to be checked 
            if group_item.text()==group_label:
                group_item.setCheckState(check_state)
                files_check_model = self.apply_state_to_child_item(group_item, files_check_model)                       
        return files_check_model


    def get_checked_event_lst_from_file(self, files_check_model, file_index):
        """
        Return the selected events (event checked) of a file index.
        
        Parameters
        -----------
            files_check_model : QtGui.QStandardItemModel
            file_index : QtCore.QModelIndex
        Returns
        -----------    
            group_list : list of string 
            name_list : list of string
        """
        n_groups = files_check_model.rowCount(file_index)
        group_list = []
        name_list = []
        for group_row in range(n_groups):
            column = 0
            group_index = files_check_model.index(group_row, column, file_index)
            group_item = files_check_model.itemFromIndex(group_index)
            if not group_item.checkState()==QtCore.Qt.CheckState.Unchecked:
                n_child = files_check_model.rowCount(group_index)
                for i_c in range(n_child):
                    child_item = group_item.child(i_c)
                    if child_item is not None:
                        if child_item.checkState()==QtCore.Qt.CheckState.Checked:
                            group_list.append(group_item.text())
                            name_list.append(child_item.text())
        return group_list, name_list


    # Create checkable item based on self.files_model
    def create_files_model_checkable(self, model):
        # Create an empty model based with the column Group-Name and Count
        files_check_event_model = self.create_empty_files_model()
        files_lst = self.get_files_list(model)
        # Create checkable item
        for filename in files_lst:
            # Make the file item children checkable (file item is copied from self.files_model)
            # tree item : parent=file, child=group and count, child=name and count
            item = self.make_checkable_file_item_count(filename, model)
            files_check_event_model.appendRow(item)
        return files_check_event_model


    def rename_group_name(self, files_editable_model, file_index, group_name_tup):
        """
        Rename the group name provided by the tuple in the model files_editable_model.
        
        Parameters
        -----------
            files_editable_model : QtGui.QStandardItemModel
            file_index : QtCore.QModelIndex
            group_name_tup : list of tuple 
                events to rename defined as below
                    [(group1_ori, name1_ori, group1_new, name1_new)
                    (group2_ori, name2_ori, group2_new, name2_new)]
        Returns
        -----------    
            files_editable_model : QtGui.QStandardItemModel
            ori_info : list of tuple (filename_lst, group_ori_lst, ori_name_list, new_name_list)
        """
        # model example
        #   group1
        #       - name1
        #       - name2
        #       - name3
        #   group2
        #       - name1
        rename_info = []
        n_groups = files_editable_model.rowCount(file_index)
        for group_row in range(n_groups):
            column = 0
            group_index = files_editable_model.index(group_row, column, file_index)
            group_item = files_editable_model.itemFromIndex(group_index)
            # Find all indices in the tuple that correspond to the current group
            indices_group = [i for i, one_group_name in enumerate(group_name_tup) if group_item.text()==one_group_name[0]]
            # The group has to be evaluated because its text is part of the groups to rename
            cur_name_renamed = 0
            if len(indices_group)>0:
                n_names = files_editable_model.rowCount(group_index)
                for i_c in range(n_names):
                    name_item = group_item.child(i_c)
                    for index in indices_group:
                        one_group_name = group_name_tup[index]
                        # Right group/name to rename
                        if name_item.text() == one_group_name[1]:
                            if not name_item.isEditable():
                                print("Try to modify item not editable")
                                return files_editable_model
                            # Only the name is renamed 
                            #   to find additional names to rename included in the current group
                            name_item.setText(one_group_name[3])
                            cur_name_renamed = 1 # To know when to rename also the group
                            filename, group_ori_text, name_ori_text = self.get_info_from_edit_name_item(name_item, files_editable_model)
                            rename_info.append((filename,group_ori_text,name_ori_text,one_group_name[3]))

                if cur_name_renamed==1:
                    group_item.setText(one_group_name[2])
        return files_editable_model, rename_info


    def rename_group_item(self, files_editable_model, file_index, previous_group_label, new_group_label):
        """
        Rename the group name provided by the tuple in the model files_editable_model.
        Parameters
        -----------
            files_editable_model : QtGui.QStandardItemModel
            file_index : QtCore.QModelIndex
            previous_group_label : string
            new_group_label : string
        Returns
        -----------    
            files_editable_model : QtGui.QStandardItemModel
            ori_info : tuple (filename, group_ori_value, ori_name_lst)

        """
        n_groups = files_editable_model.rowCount(file_index)
        group_is_found = False
        for group_row in range(n_groups):
            column = 0
            group_index = files_editable_model.index(group_row, column, file_index)
            group_item = files_editable_model.itemFromIndex(group_index)
            if group_item.text()==previous_group_label:
                group_item.setText(new_group_label)
                # Return the original information from the modified item (column 1)
                filename, group_ori_value, ori_name_lst = self.get_info_from_edit_group_item(group_item, files_editable_model)
                group_is_found = True
        if group_is_found:
            return files_editable_model, (filename, group_ori_value, ori_name_lst)
        else:
            return files_editable_model, None


    def get_group_name_from_cohort(self, files_editable_model):
        """
        Return a dict of groups with its names under for the whole cohort.
        
        Parameters
        -----------
            files_editable_model : QtGui.QStandardItemModel
        Returns
        -----------    
            group_name_dict : dict
                keys are the event group
                values are a list of strings (the event names)
            tristate_dict : dict of dict
                keys are the event group
                value is a dict where the key is the name and the value is the state
                    
        """
        group_name_dict = {}    # store group and names labels
        tristate_dict = {}      # store state of each name (through cohort)
        file_list = self.get_files_list(files_editable_model)
        for filename in file_list:
            file_index = self.get_file_index(filename, files_editable_model)
            n_groups = files_editable_model.rowCount(file_index)
            for group_row in range(n_groups):
                column = 0
                group_index = files_editable_model.index(group_row, column, file_index)
                group_item = files_editable_model.itemFromIndex(group_index)
                #cur_group_state = group_item.checkState()
                n_names = files_editable_model.rowCount(group_index)
                names_list = []
                # Dict with key = name, value = state
                names_states = {}
                # Pass through all names
                for i_c in range(n_names):
                    name_item = group_item.child(i_c)
                    if not name_item.text() in names_list:
                        names_list.append(name_item.text())
                    names_states[name_item.text()]=name_item.checkState()
                # Save the name and the states
                    # If it is the first file with this group
                if not group_item.text() in group_name_dict.keys():
                    group_name_dict[group_item.text()]=names_list
                    tristate_dict[group_item.text()]=names_states
                else:
                    # If we need to combine with the previous file
                    previous_names = group_name_dict[group_item.text()]
                    previous_states = tristate_dict[group_item.text()]
                    for name in names_list:
                        # Add new only
                        if not name in previous_names:
                            previous_names.append(name)
                            previous_states[name]=names_states[name]
                        else:
                            # If they are the same, no change of the state
                            # if they are different, now they are partially checked
                            if not previous_states[name]==names_states[name]:
                               previous_states[name] = QtCore.Qt.CheckState.PartiallyChecked
                    #group_name_dict[group_item.text()] = previous_names.sort()
                    group_name_dict[group_item.text()] = previous_names
                    tristate_dict[group_item.text()] = previous_states
        return group_name_dict, tristate_dict


    def get_unchecked_event_lst_from_file(self, files_editable_model, filename):
        """
        Return the original name of unchecked events (event editable) for a file index.
        Evaluate the state in the files_editable_model but export the group/name label from the unedited_model.
        
        Parameters
        -----------
            files_editable_model : QtGui.QStandardItemModel
            filename : string
        Returns
        -----------    
            group_list : list of string 
            name_list : list of string
        """
        item_list = files_editable_model.findItems(os.path.basename(filename),QtCore.Qt.MatchExactly)
        group_list = []
        name_list = []
        if len(item_list)==1:
            file_item = item_list[0]
            file_index = file_item.index()
            n_groups = files_editable_model.rowCount(file_index)
            for group_row in range(n_groups):
                # Modified value is column 0 and original label is column 1
                edit_group_item = file_item.child(group_row, 0)
                ori_group_item = file_item.child(group_row, 1)
                # Could be PartiallyChecked is some of the names under is checked
                if not edit_group_item.checkState()==QtCore.Qt.CheckState.Checked:
                    n_child = files_editable_model.rowCount(edit_group_item.index())
                    for i_c in range(n_child):
                        # Modified value is column 0 and original label is column 1
                        edit_child_item = edit_group_item.child(i_c, 0)
                        ori_child_item = edit_group_item.child(i_c, 1)
                        if edit_child_item is not None:
                            if edit_child_item.checkState()==QtCore.Qt.CheckState.Unchecked:
                                group_list.append(ori_group_item.text())
                                name_list.append(ori_child_item.text())
        return group_list, name_list


    def get_info_from_edit_group_item(self, modified_item, editable_model):
        """
        Return the original information of a modified item from its model. 
        
        Parameters
        -----------
            modified_item : QtGui.QStandardItem
            editable_model : QtGui.QStandardItemModel
        Returns
        -----------    
            filename : string
                filename modified
            group_ori_text : string
                Original text label of the group modified
            ori_name_lst : list of string
                List of name for the modified group.
        """
        file_item = modified_item.parent()
        group_row = modified_item.row()

        # subject tree model
        if file_item is not None:
            filename = file_item.data(Qt.UserRole + 1)
            # column 0 is the new and column 1 is the original
            group_ori_text = file_item.child(group_row, 1).text()

        # cohort tree model
        else:
            filename = None
            # column 0 is the new and column 1 is the original
            group_ori_text = editable_model.item(group_row,1).text()

        ori_name_lst = []
        n_names = modified_item.rowCount()
        for i_name in range(n_names):
            # column 0 is the new and column 1 is the original
            name_item = modified_item.child(i_name,1) 
            ori_name_lst.append(name_item.text())

        return filename, group_ori_text, ori_name_lst


    def get_info_from_edit_name_item(self, modified_item, editable_model):
        """
        Return the original information about a modified item.
        
        Parameters
        -----------
            modified_item : QtGui.QStandardItem
            editable_model : QtGui.QStandardItemModel
        Returns
        -----------    
            filename : string
                filename modified
            group_ori_text : string
                Original text label of the group linked to the name modified
            name_ori_text : string
                Original text label of the name modified
        """
        name_row = modified_item.row()
        group_item = modified_item.parent()

        # column 0 is the new and column 1 is the original
        name_ori_text = group_item.child(name_row,1).text()
        group_row = group_item.row()
        file_item = group_item.parent()
        
        #  Subject tree view
        if file_item is not None:
            group_ori_text = file_item.child(group_row,1).text()
            filename = file_item.data(Qt.UserRole + 1)
        # Cohort tree view
        else:
            # column 0 is the new and column 1 is the original
            group_ori_text = editable_model.item(group_row,1).text()
            filename = None
        return filename, group_ori_text, name_ori_text


    # Called when the timout is reached
    @QtCore.Slot()
    def _emit_timeout_reached(self):
        self._context_manager[self.context_files_view] = self


    # Update the context to notify that the channel selection has been changed
    # The ChannelsTableModel emit a dataChanged when the data is set
    def on_channels_selection_changed(self):
        # Add a timer delay to accumulate all the channel selection change before update the context
        self._emit_timer.start(2)

"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the PSGReader plugin
"""
import datetime
import numpy as np
import os
import pandas as pd
from qtpy import QtWidgets
from qtpy import QtCore
from qtpy import QtGui
from qtpy.QtCore import Qt
import sys

from . import commons
from commons.CheckBoxDelegate import CheckBoxDelegate
from commons.BaseSettingsView import BaseSettingsView
from commons.NodeRuntimeException import NodeRuntimeException
from commons.Utils import deleteItemsOfLayout
from widgets.WarningDialog import WarningDialog

from CEAMSModules.PSGReader.PSGReaderManager import PSGReaderManager
from CEAMSModules.PSGReader.Ui_PSGReaderSettingsView import Ui_PSGReaderSettingsView
from CEAMSModules.PSGReader.MontagesTableModel import MontagesTableModel
from CEAMSModules.PSGReader.MontagesProxyModel import MontagesProxyModel
from CEAMSModules.PSGReader.ChannelsTableModel import ChannelsTableModel
from CEAMSModules.PSGReader.ChannelsProxyModel import ChannelsProxyModel

DEBUG = False

class PSGReaderSettingsView( BaseSettingsView,  Ui_PSGReaderSettingsView, QtWidgets.QWidget):
    
    # To send a signal each time the self.files_model is modified
    #   It allows to define QtCore.Slot() to do action each time the self.files_model is modified
    model_updated_signal = QtCore.Signal()

    """ PSGReaderSettingsView display the settings. """
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)
        self.montages_tableview.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        self.channels_tableview.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)

        # init 
        self.files_details = {}

        # Update Alias UI
        self._alias_layout = None
        self._alias_line_edit = None

        # Init EEG reader modules
        self._psg_reader_manager = PSGReaderManager()
        self._psg_reader_manager._init_readers()

        # Init table models
        self.files_model = self.create_empty_files_model() # with events
        self.files_stages_model = self.create_empty_files_model() # with stages

        self.files_listview.setModel(self.files_model)
        self.events_treeView.setModel(self.files_model)
        self.init_montage_table_model()
        self.init_channels_table_model()
        self._alias_topic = f'{self._parent_node.identifier}.alias'
        self._pub_sub_manager.subscribe(self, self._alias_topic)

        # itemChanged is a signal in QStandardItemModel Class
        # Connect itemChanged to the slot on_item_changed allows to perform 
        self.files_model.itemChanged.connect(self.file_selection_changed_slot)
        # Connect the custom signal to update the label
        self.montages_table_model.dataChangedWithCheckState.connect(self.updateLabel_Montages)
        self.channels_table_model.dataChangedWithCheckState.connect(self.updateLabel_Channels)
        
        # Subscribe to the proper topics to send/get data from the node
        self._files_topic = f'{self._parent_node.identifier}.files'
        self._pub_sub_manager.subscribe(self, self._files_topic)

        if 'file_selection_only' in self._options:
            if self._options['file_selection_only']['value'] == "0":
                self.frame_montages.setVisible(True)
                self.frame_channels.setVisible(True)
            else:
                self.frame_montages.setVisible(False)
                self.frame_channels.setVisible(False)
        

    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._files_topic)
            self._pub_sub_manager.unsubscribe(self, self._alias_topic)


    def on_topic_update(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            at any update, does not necessary answer to a ping.
            To listen to any modification not only when you ask (ping)
        """
        if DEBUG: print(f'PSGReaderSettingsView.on_topic_update:{topic} message:{message}')


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            Called after a ping.
        """
        if DEBUG: print(f'PSGReaderSettingsView.on_topic_response:{topic} message:{message}')
        if topic == self._files_topic:
            self.load_files_from_data(message)
        elif topic == self._alias_topic:
            self.load_alias_from_data(message)


    def load_files_from_data(self, data):
        """  Called to load files asked (saved) in the file list.
             data is a dict with the parameters to init PSGReader.files input.
             Each key of the dict data is the filename of the PSG file loaded.
        """
        # A model which includes files, events
        self.files_model.clear()
        self.files_model.setColumnCount(2)
        self.files_model.setHorizontalHeaderLabels(['Group-Name', 'Count'])

        # A model which includes files and stages
        self.files_stages_model.clear()
        self.files_stages_model.setColumnCount(2)
        self.files_stages_model.setHorizontalHeaderLabels(['Group-Name', 'Count'])

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
            item, item_stages = self.create_file_item_count(filename)
            self.files_model.appendRow(item) 
            self.files_stages_model.appendRow(item_stages) 

            # For each file, load its montages in the montages table model
            if self._options['file_selection_only']['value'] == "0":
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

        if self._options['file_selection_only']['value'] == "0":
            # Invalide the models so it refreshes the UI
            self.montages_proxy_model.invalidate()
            self.montages_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly
            self.channels_proxy_model.invalidate()
            self.channels_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly
            self.on_montages_selection_changed()

        # Update the number of files in the title
        self.label_PSG.setText(f"PSG files ({self.files_model.rowCount()})")
        # Generate a signal to inform that self.files_model has been updated
        self.model_updated_signal.emit()   
        if self._options['file_selection_only']['value'] == "0":
            # Generate signals to inform that Montage and Channel tables have been updated and the check state has changed
            self.montages_table_model.dataChangedWithCheckState.emit(self.montages_table_model.checkedItemCount())
            self.channels_table_model.dataChangedWithCheckState.emit(self.channels_table_model.checkedItemCount())      


    # Create an empty model based with the column Group-Name and Count
    def create_empty_files_model(self):
        files_model = QtGui.QStandardItemModel(0, 2)
        files_model.setHeaderData(0, QtCore.Qt.Horizontal, 'Group-Name')
        files_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Count')
        files_model.setHorizontalHeaderLabels(['Group-Name', 'Count'])
        return files_model


    # Create an empty model based with the column 'Group-Name', 'Original label'
    def create_empty_edit_files_model(self):
        files_model = QtGui.QStandardItemModel(0, 2)
        files_model.setHeaderData(0, QtCore.Qt.Horizontal, 'Group-Name')
        files_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Original label')
        files_model.setHorizontalHeaderLabels(['Group-Name', 'Original label'])
        return files_model


    def load_alias_from_data(self, data):
        for alias in data:
            if alias in self._alias_line_edit:
                self._alias_line_edit[alias].setText(';'.join(data[alias]))


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


    def init_alias_ui(self):
        self._alias_line_edit = {}

        if self._alias_layout is not None:
            deleteItemsOfLayout(self._alias_layout)

        # If there is no alias
        alias = self._options['alias']['value']
        if alias is None:
            return

        # if there is an alias but its just space charaters
        if alias.strip() == "":
            return

        if self._alias_layout is None:
            self._alias_layout = QtWidgets.QVBoxLayout()

        self._alias_layout.setObjectName("Alias Layout")
        self._alias_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        
        alias_title = QtWidgets.QLabel(text="Alias")
        title_font = QtGui.QFont()
        title_font.setBold(True)
        alias_title.setFont(title_font)
        self._alias_layout.addWidget(alias_title)

        for a in alias.split(";"):

            row_layout = QtWidgets.QHBoxLayout()

            button = QtWidgets.QPushButton()
            button.setText(">")
            button.clicked.connect(lambda checked=None, x=a:self.on_add_alias(x))
            button.setMaximumSize(20, 20)
            size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)
            size_policy.setHorizontalStretch(0)
            button.setSizePolicy(size_policy)
            
            row_layout.addWidget(button)

            label = QtWidgets.QLabel(a)
            row_layout.addWidget(label)

            line_edit = QtWidgets.QLineEdit()
            row_layout.addWidget(line_edit)
            self._alias_line_edit[a] = line_edit
            size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Fixed)
            size_policy.setHorizontalStretch(1)
            line_edit.setSizePolicy(size_policy)

            self._alias_layout.addLayout(row_layout)

        self._alias_layout.addStretch(1)
        alias_widget = QtWidgets.QWidget()
        alias_widget.setLayout(self._alias_layout)
        self.splitter.addWidget(alias_widget)


    def on_add_alias(self, alias):
        # Get selected channels
        selected_channels = [r.data() for r in self.channels_tableview.selectedIndexes()]

        current_aliases = self._alias_line_edit[alias].text()
        aliases_list = current_aliases.split(';')
        for ch in selected_channels:
            if aliases_list.count(ch) == 0:
                if current_aliases:
                    current_aliases = f"{current_aliases};{ch}"
                else:
                    current_aliases = ch

        self._alias_line_edit[alias].setText(current_aliases)


    def add_files_slot(self):
        dlg = QtWidgets.QFileDialog()
        #dlg.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        dlg.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        dlg.setNameFilters(self._psg_reader_manager.get_file_extensions_filters())

        if dlg.exec_():
            filenames = dlg.selectedFiles()

            # Add a QProgressDialog to show the progression bar
            n_files = len(filenames)
            progress = QtWidgets.QProgressDialog("Loading files...", None, 0, n_files)
            progress.setWindowModality(Qt.ApplicationModal)
            progress.setMinimumDuration(0) # Settings a minimum time greater than 0 makes the UI update slower
            progress.show()

            # Add the file only if is it not already added
            for i, filename in enumerate(filenames):
                progress.setValue(i)
                matches = self.files_model.findItems(os.path.basename(filename),QtCore.Qt.MatchExactly)
                if len(matches) == 0:
                    success = self.load_file_info(filename) # self._psg_reader_manager is used

                    if success:
                        # tree item : parent=file, child=group and count, child=name and count
                        item, item_stages = self.create_file_item_count(filename) # The file is read
                        self.files_model.setColumnCount(2)
                        self.files_model.appendRow(item)  
                        self.files_stages_model.setColumnCount(2)
                        self.files_stages_model.appendRow(item_stages)  

            progress.setValue(n_files)
            progress.close()
                        
            # Update the number of files in the title
            self.label_PSG.setText(f"PSG files ({self.files_model.rowCount()})")
            # Generate a signal to inform that self.files_model has been updated
            self.model_updated_signal.emit() 

        for i in range(self.files_model.columnCount()):
            self.events_treeView.hideColumn(i)


    # Return 2 tree items : parent=file, child=group and count, child=name and count
    # file_item includes events
    # file_stages_item includes stages (Useful for NATUS and Stellate because the sleep stages are renamed within Snooz)
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
                file_item, file_stages_item = create_file_item_count(filename)
        """

        file_item = QtGui.QStandardItem(os.path.basename(filename))
        file_item.setToolTip(filename)
        file_item.setData(filename, Qt.UserRole + 1) # "file_item.setData(filename, 0)" overwrites file_item.text()

        file_stages_item = QtGui.QStandardItem(os.path.basename(filename))
        file_stages_item.setToolTip(filename)
        file_stages_item.setData(filename, Qt.UserRole + 1) # "file_item.setData(filename, 0)" overwrites file_item.text()

        self._psg_reader_manager.open_file(filename)
        stages = self._psg_reader_manager.get_sleep_stages() # need to make them visible from the settings view
        events = self._psg_reader_manager.get_events()
        self._psg_reader_manager.close_file()

        # First step, organize the list of events in a dictionary where the key
        # is the name of group and the value is another dictionary for its
        # list of items. The value of the second dictionary is the total count of
        # event of this kind.
        
        # Initialize an empty dictionary to store the events and their counts for each group
        events_groups = {}
        stages_groups = {}

        # Group the events by 'group' and 'name' columns, count the number of events in each group, and create a new dataframe with the count
        group_df = events.groupby(['group', 'name']).size().reset_index(name='count')
        # Group the events by 'group' and 'name' columns, count the number of events in each group, and create a new dataframe with the count
        stage_df = stages.groupby(['group', 'name']).size().reset_index(name='count')

        # Get a list of unique groups
        groups_ext_evts = group_df['group'].unique().tolist()
        groups_ext_stgs = stage_df['group'].unique().tolist()

        # Iterate over the groups
        for group in groups_ext_evts:
            # Filter the group_df to only get the events for this group
            list_of_event_for_this_group = group_df[group_df['group'] == group]
            # Create a dictionary where the key is the event name and the value is the count
            event_count_dict = list_of_event_for_this_group.set_index('name')['count'].to_dict()
            # Add the dictionary for this group to the events_groups dictionary
            events_groups[group] = event_count_dict

        # Iterate over the groups of stages (only one)
        for group in groups_ext_stgs:
            # Filter the stage_df to only get the events for this group
            list_of_event_for_this_group = stage_df[stage_df['group'] == group]
            # Create a dictionary where the key is the event name and the value is the count
            event_count_dict = list_of_event_for_this_group.set_index('name')['count'].to_dict()
            # Add the dictionary for this group to the events_groups dictionary
            stages_groups[group] = event_count_dict

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
            file_item.appendRow([group_item,group_count_item])

            # Set the scoring status
            if len(stages)==0:
                file_item.setData('unscored', Qt.UserRole + 2)
            elif any(stages['name']!='9'):
                file_item.setData('scored', Qt.UserRole + 2)
            else:
                file_item.setData('unscored', Qt.UserRole + 2)

        # Second step, form a tree of standardItem for the group of events and their events
        # from this dictionary.
        for group in stages_groups:
            total_events_count = sum(stages_groups[group].values())
            group_item = QtGui.QStandardItem(group)
            group_count_item = QtGui.QStandardItem(str(total_events_count))
            for event in stages_groups[group].items():
                name_item = QtGui.QStandardItem(event[0])
                count_item = QtGui.QStandardItem(str(event[1]))
                group_item.appendRow([name_item, count_item])
            file_stages_item.appendRow([group_item,group_count_item])

        return file_item, file_stages_item
    

    # Return an tree item : parent=file, child=group and count, child=name and count
    #   Only the sleep stages are read (instead of the events)
    def create_file_item_stage_count(self, filename):
        """
        Create an file item as parent with its children : group and count, name and count.
        The file "filename" is opened and its sleep stages are read.
            
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
                file_item = create_file_item_stage_count(filename)
        """

        file_item = QtGui.QStandardItem(os.path.basename(filename))
        file_item.setToolTip(filename)
        file_item.setData(filename, Qt.UserRole + 1) # "file_item.setData(filename, 0)" overwrites file_item.text()
        self._psg_reader_manager.open_file(filename)
        stages = self._psg_reader_manager.get_sleep_stages() # need to make them visible from the settings view
        #events = self._psg_reader_manager.get_events()
        self._psg_reader_manager.close_file()

        # First step, organize the list of events in a dictionary where the key
        # is the name of group and the value is another dictionary for its
        # list of items. The value of the second dictionary is the total count of
        # event of this kind.
        
        # Initialize an empty dictionary to store the events and their counts for each group
        events_groups = {}

        # Group the events by 'group' and 'name' columns, count the number of events in each group, and create a new dataframe with the count
        group_df = stages.groupby(['group', 'name']).size().reset_index(name='count')

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



    # Return an tree item : parent=file, child=group and original name, child=name and original label
    def make_editable_file_item_count(self, filename, model, checkable=False): 
        """
        Make the file item children editable, checkable (if applied) (file item is copied from model).
        Copy the file item from the model as parent and make its children editable : group and original label, name and original label.
        If checkable, the items are checked when created.
            
            Parameters
            -----------
                filename    : string
                    filename as a text to add to the item.
                checkable : bool
                    Bool flag to create a checkable item.
                    Items are checked when created.
            Returns
            ----------- 
                file_item :  QtGui.QStandardItem
                    A tree item : parent=file, child=group and original label, child=name and original label
            usage 
            -----------
                file_item = create_file_editable_item(filename, self.files_model, True)
        """
        ori_file_item =self.get_file_item(filename, model)

        # Create a file item based on the original file item
        file_item = QtGui.QStandardItem(ori_file_item.text())
        file_item.setData(ori_file_item.data(Qt.UserRole + 1),Qt.UserRole + 1)

        # For all group and count children of the original file item
        for i_group in range(0, ori_file_item.rowCount()):
            # Create a new checkable item
            group_item = QtGui.QStandardItem(ori_file_item.child(i_group,0).text())
            group_item.setEditable(True)
            ori_group_item = QtGui.QStandardItem(ori_file_item.child(i_group,0).text())
            ori_group_item.setCheckable(False)
            ori_group_item.setEditable(False)
            if checkable:
                # Make checkable and check the state of the group_item
                group_item.setCheckable(True)
                group_item.setTristate(True)
                group_item.setCheckState(QtCore.Qt.CheckState.Checked)
            # For each child of the group_item
            for i_name in range(0, ori_file_item.child(i_group,0).rowCount()):
                name_item = QtGui.QStandardItem(ori_file_item.child(i_group,0).child(i_name,0).text())
                name_item.setEditable(True)
                ori_name_item = QtGui.QStandardItem(ori_file_item.child(i_group,0).child(i_name,0).text())
                ori_name_item.setCheckable(False)
                ori_name_item.setEditable(False)
                if checkable:
                    # Make checkable and check the state of the name_item
                    name_item.setCheckable(True)
                    name_item.setTristate(False)
                    name_item.setCheckState(QtCore.Qt.CheckState.Checked)
                group_item.appendRow([name_item, ori_name_item])
            # Add the new checkable item to the file_item
            file_item.appendRow([group_item, ori_group_item])
        
        # Copy the scoring status
        file_item.setData(ori_file_item.data(Qt.UserRole + 2), Qt.UserRole + 2)

        return file_item


    def channel_search_changed_slot(self, search_pattern):
        self.update_channels_filter()
    

    def add_folders_slot(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly) # Allows the user to select only directories (folders).
        # The non native QFileDialog supports only local files.
            # So it is better to use the native dialog instead to see athena
        # The native dialog does not support multiple folders selection in windows
            # Natus needs the option to select multiple folders
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

            # Add a QProgressDialog to show the progression bar
            n_files = len(folders)
            if n_files > 1:
                progress = QtWidgets.QProgressDialog("Loading files...", None, 0, n_files)
                progress.setWindowModality(Qt.ApplicationModal)
                progress.setMinimumDuration(0) # Settings a minimum time greater than 0 makes the UI update slower
                progress.show()
            for i, folder in enumerate(folders):
                filenames = self._psg_reader_manager.find_psg_within_folder(folder)

                if n_files > 1:
                    progress.setValue(i)
                else:
                    progress = QtWidgets.QProgressDialog("Loading files...", None, 0, len(filenames))
                    progress.setWindowModality(Qt.ApplicationModal)
                    progress.setMinimumDuration(0) # Settings a minimum time greater than 0 makes the UI update slower
                    progress.show()                    

                for i_f, filename in enumerate(filenames):
                    progress.setValue(i_f)
                    matches = self.files_model.findItems(os.path.basename(filename),QtCore.Qt.MatchExactly)
                    if len(matches) == 0:
                        if filename is not None:
                            success = self.load_file_info(filename) # self._psg_reader_manager is used

                            if success:
                                # tree item : parent=file, child=group and count, child=name and count
                                item, item_stages = self.create_file_item_count(filename) # The file is read
                                self.files_model.setColumnCount(2)
                                self.files_model.appendRow(item)    
                                self.files_stages_model.setColumnCount(2)
                                self.files_stages_model.appendRow(item_stages)    
                        else:
                            #TODO Log empty folders
                            # Couldnt find PSG file in folder:{folder}
                            pass
            if n_files > 1:
                progress.setValue(n_files)
            else:
                progress.setValue(len(filenames))
            progress.close()
            # Update the number of files in the title
            self.label_PSG.setText(f"PSG files ({self.files_model.rowCount()})")
            # Generate a signal to inform that self.files_model has been updated
            self.model_updated_signal.emit() 

    
    # Called when the user press on Remove push button
    def remove_entries_slot(self):
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
            self.files_stages_model.removeRow(row)

        # Update the number of files in the title
        self.label_PSG.setText(f"PSG files ({self.files_model.rowCount()})")
        # Generate a signal to inform that self.files_model has been updated
        self.model_updated_signal.emit() 
        if self._options['file_selection_only']['value'] == "0":
            # Generate signals to inform that Montage and Channel tables have been updated and the check state has changed
            self.montages_table_model.dataChangedWithCheckState.emit(self.montages_table_model.checkedItemCount())
            self.channels_table_model.dataChangedWithCheckState.emit(self.channels_table_model.checkedItemCount())


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
       
        # If the file list is empty -> open a warning dialog
        # If none of the channels is selected for a subject -> open a warning dialog
        if self._options['file_selection_only']['value'] == "1":
            file_list = self.get_files_list(self.files_model)
        else:
            channels_info_df = self.channels_table_model.get_data()

            montages_info_df = self.montages_table_model.get_data()


            file_list = channels_info_df['Filename'].unique()
        if len(file_list)>0:
            if self._options['file_selection_only']['value'] == "0":

                for file in file_list:
                    montage_used = montages_info_df[(montages_info_df['Filename']==file) & (montages_info_df['Use']==True)]
                    if len(montage_used) > 1:
                        WarningDialog(f"Only one montage per recording is allowed. Check the montages selection of the file : {file}.")
                        return False

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


    # Update the files selection (montage and channels) and return the dict of files
    def update_files_selection(self):

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
        
        return files


    # Called when the user save a tool that include the PsgReaderSettingsView or 
    # press the "apply" push button of the settingsView
    def on_apply_settings(self):
        files = self.files_details.copy()
        if self._options['file_selection_only']['value'] == "0":
            # Update the files selection (montage and channels) and return the dict of files
            files = self.update_files_selection()
            # Get the list of alias
            alias = self.get_alias()
            # Send the list of alias to the PSGReader module        
            self._pub_sub_manager.publish(self, self._alias_topic, alias)
        # Send the dictionary as an input to the PSGReader module
        self._pub_sub_manager.publish(self, self._files_topic, files)


    # Called when the user click on the export button
    def export_slot(self):

        # Get the current date as a string YYYYMMDD
        current_date = datetime.datetime.now().strftime("%Y%m%d")

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(\
            None, 'Export channels selection in a table format as',\
                 f'Snooz-Channel_selections_log_table-{current_date}.txt', filter="*.txt")
        if filename is not None and filename:
            with open(filename, 'w') as tsv_file:
                export_df = self.channels_table_model._data.loc[self.channels_table_model._data['Use'] == True]
                export_df.to_csv(tsv_file, sep='\t', encoding="utf_8")

        files = self.files_details.copy()
        if self._options['file_selection_only']['value'] == "0":
            # Update the files selection (montage and channels) and return the dict of files
            files = self.update_files_selection()
            # Get the list of alias
            alias = self.get_alias()
            if len(alias) > 0:
                # Save the dictionnary alias in a text file
                alias_filename, _ = QtWidgets.QFileDialog.getSaveFileName(\
                    None, 'Save alias definition as text file to import later in an Input Files step in Snooz',\
                         f'Snooz-Input_Files_Export-Alias-{current_date}.txt', filter="*.txt")
                if alias_filename is not None and alias_filename:
                    with open(alias_filename, 'w') as txt_file:
                        # Write the dictionary converted to a string
                        txt_file.write(str(alias))

        # Save the dictionnary files in a text file
        # Snooz_Input_Files_Selection_Export_{date}.tsv
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(None, \
            'Save files selection as text file to import later in an Input Files step in Snooz',\
                f'Snooz-Input_Files_Export-Files_Montages_Channels-{current_date}.txt', filter="*.txt")
        if filename is not None and filename:
            with open(filename, 'w') as txt_file:
                # Write the dictionary converted to a string
                txt_file.write(str(files))


    # Called when the user click on the import button
    def import_slot(self):
        # Open a file. Ask the user for a txt file
        alias_filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, \
            'Open alias definition if any (i.e. Previously exported from Snooz as Snooz-Input_Files_Export-Alias-date.txt)', \
                f'Snooz-Alias.txt', filter="*.txt")
        if alias_filename is not None and alias_filename:
            with open(alias_filename, 'r') as txt_file:
                alias = eval(txt_file.read())
                self.load_alias_from_data(alias)

        # Open a file. Ask the user for a txt file
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, \
            'Open files selection (i.e. Previously exported from Snooz as Snooz-Input_Files_Export-Files_Montages_Channels-date.txt)', \
                'Snooz-Files.txt\r', filter="*.txt")
        if filename is not None and filename:
            # Display a loading dialog
            self._open_loading_dialog()
            with open(filename, 'r') as txt_file:
                files = eval(txt_file.read())
                self.load_files_from_data(files)
            # Close the loading dialog
            self._close_loading_dialog()


    def file_selection_changed_slot(self):
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


    def montage_seach_changed_slot(self):
        self.montages_proxy_model.set_montages_search_pattern(self.montage_search_lineedit.text())
        # Update the montages selection to change the list of channels
        self.on_montages_selection_changed()


    def montages_select_all_slot(self):
        for row in range(self.montages_proxy_model.rowCount()):
            self.montages_proxy_model.setData(self.montages_proxy_model.index(row,0), True)
        self.on_montages_selection_changed()
        self.montages_proxy_model.invalidate()
        # Update the title label_Montages to add in the title the number of selected montages
        self.label_Montages.setText(f"Montages ({self.montages_proxy_model.rowCount()})")
        self.montages_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly


    def montages_unselect_all_slot(self):
        for row in range(self.montages_proxy_model.rowCount()):
            self.montages_proxy_model.setData(self.montages_proxy_model.index(row,0), False)
        self.on_montages_selection_changed()
        self.montages_proxy_model.invalidate()
        # Update the title label_Montages to add in the title the number of selected montages
        self.label_Montages.setText(f"Montages (0)")
        self.montages_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly


    def channels_select_all_slot(self):
        n_chans = self.channels_proxy_model.rowCount()
        progress = QtWidgets.QProgressDialog("Selecting all channels...", None, 0, n_chans)
        progress.setWindowModality(Qt.ApplicationModal)
        progress.setMinimumDuration(0) # Settings a minimum time greater than 0 makes the UI update slower
        progress.show()
        for row in range(n_chans):
            # if the row is a multiple of 100, update the progress bar
            if row % 200 == 0:
                progress.setValue(row)
            self.channels_proxy_model.setData(self.channels_proxy_model.index(row,0), True)
        progress.setValue(n_chans)
        self.channels_proxy_model.invalidate()
        self.channels_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly
        progress.close()


    def channels_unselect_all_slot(self):
        n_chans = self.channels_proxy_model.rowCount()
        progress = QtWidgets.QProgressDialog("Unselecting all channels...", None, 0, n_chans, self)
        progress.setWindowModality(Qt.ApplicationModal)
        progress.setMinimumDuration(0)  # Settings a minimum time greater than 0 makes the UI update slower
        progress.show()
        for row in range(n_chans):
            # if the row is a multiple of 1000, update the progress bar
            if row % 200 == 0:
                progress.setValue(row)
            self.channels_proxy_model.setData(self.channels_proxy_model.index(row,0), False)
        progress.setValue(n_chans)
        self.channels_proxy_model.invalidate()
        self.channels_tableview.resizeColumnsToContents() # Especially important for the check mark column or it will not appear properly
        progress.close()


    def load_settings(self):
        self.init_alias_ui()
        self._pub_sub_manager.publish(self, self._files_topic, 'ping')
        if self._options['file_selection_only']['value'] == "0":
            self._pub_sub_manager.publish(self, self._alias_topic, 'ping')


    def load_file_info(self, filename):
        """ Function to read the file, init the table montage model, the channel model and self.files_details.

            self.files_details[filename] = 
                'event_groups':event_groups,
        """
        success = self._psg_reader_manager.open_file(filename)

        if not success:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText(f"Could not open the PSG or the accessory file. The format is not valid for {filename}")
            msg.setWindowTitle("File load error")
            msg.exec()
            return False

        if self._options['file_selection_only']['value'] == "0":
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

    # Return the ith group item for a filename
    def get_group_item(self, filename, i_group, files_model):
        file_item = self.get_file_item(filename, files_model)
        return file_item.child(i_group)


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
            
    
    # Get the list of alias
    def get_alias(self):
        alias = {}
        for idx, a in enumerate(self._alias_line_edit):
            alias[a] = self._alias_line_edit[a].text().split(';')
        return alias


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

    
    # Create editable item based on a provided model
    def create_files_model_editable(self, model, checkable=False):

        # Create an empty model based with the column Group-Name and Count
        files_editable_event_model = self.create_empty_edit_files_model()
        files_lst = self.get_files_list(model)
        # Create checkable item
        for filename in files_lst:
            # Make the file item children checkable (file item is copied from self.files_model)
            # tree item : parent=file, child=group and count, child=name and count
            item = self.make_editable_file_item_count(filename, model, checkable)
            files_editable_event_model.appendRow(item)

        return files_editable_event_model


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

    # Private functions
    def _open_loading_dialog(self):
        self._progress = QtWidgets.QMessageBox()
        self._progress.setText("Loading ...\nPlease wait a moment.")
        self._progress.setWindowTitle("Loading ... Please wait a moment.      ")
        self._progress.setStandardButtons(QtWidgets.QMessageBox.NoButton)
        self._progress.show()

    def _close_loading_dialog(self):
        if self._progress is not None:
            self._progress.close()
            self._progress = None


    def updateLabel_Montages(self, count):
        self.label_Montages.setText(f"Montages ({count})")

    def updateLabel_Channels(self, count):
        self.label_Channels.setText(f"Channels ({count})")
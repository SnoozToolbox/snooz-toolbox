"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    Settings viewer of the DetectionsCohortReview plugin
    The settings viewer allows to select and rename channels and add ROIs.
"""
from CEAMSModules.DetectionsCohortReview.Ui_DetectionsCohortReviewSettingsView import Ui_DetectionsCohortReviewSettingsView
from CEAMSModules.DetectionsCohortReview.DialogROI import DialogROI

from commons.BaseSettingsView import BaseSettingsView

import io
import numpy as np
import pandas as pd
from qtpy import QtWidgets, QtCore
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QFileDialog, QListWidgetItem
from qtpy.QtGui import QStandardItemModel, QStandardItem


class DetectionsCohortReviewSettingsView(BaseSettingsView, Ui_DetectionsCohortReviewSettingsView, QtWidgets.QWidget):
    """
        DetectionsCohortReviewView set the DetectionsCohortReview settings
    """

    # To send a signal each time the self.files_model is modified
    #   It allows to define QtCore.Slot() to do action each time the self.files_model is modified
    filenames_updated_signal = QtCore.Signal()
    
    def __init__(self, parent_node, pub_sub_manager, **kwargs):
        super().__init__(**kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager

        # init UI
        self.setupUi(self)

        # Properties of DetectionsCohortReviewView
        self.data_df = pd.DataFrame()
        self.labels_to_extract = ['filename',  'chan_label']

        # ---------------------------------------------------------------------------------------
        # Settings definition to display information on Settings view
        # ---------------------------------------------------------------------------------------
        # Create an empty model for 2 QListView (Subject list and Subject Channel List).
        self.model_subject_chan = QStandardItemModel()
         # Apply the model to the QListView
        self.subject_listView.setModel(self.model_subject_chan) 
        self.chan_subject_listView.setModel(self.model_subject_chan)  
        # Unique list of channel for the cohort is managed through a standard list 
        #   and displayed on a QListWidjet 
        self.cohort_chan_list = []
        
        # itemChanged is a signal in QStandardItemModel Class
        # When an item is changed via the model (from the list view or directly into the model)
        #   the item_changed_subject_slot is called.
        self.model_subject_chan.itemChanged.connect(self.item_changed_subject_slot)
        self.chan_cohort_listWidget.itemChanged.connect(self.item_changed_cohort_slot)

        # ---------------------------------------------------------------------------------------
        # Settings definition to send information to the DetectionsCohortReview plugin
        # ---------------------------------------------------------------------------------------
        # List of filenames (including path) to the detector output file.
        self.filenames = []

        # Dictionary to keep original and modified channel name to apply the change to self.data_df
        # Keys are the subjects
        #   each item is a list of 3 elements [original chan label, modified chan label, bool selection flag]
        self.subject_chans_label = {}
        # Column number of each feature
        self.ori_chan_label_col = 0
        self.mod_chan_label_col = 1
        self.chan_state_col = 2

        # Dict to manage the ROI created at the cohort level
        #   keys are ROIs labels
        #   Each item is a list of 3 elements [channel list to average, blank flag]
        self.ROIs_cohort = {}
        
        # Dict to manage the ROI at the subject level
        #   keys are the subjects
        #   Each item is a list of n_ROIs with its selection label  [ROI#1 label, bool selection flag]
        #                                                           [ROI#2 label, bool selection flag]
        #                                                               ...
        self.ROIs_subjects = {} 

        self.ping_complete = 0
        # Subscribe to the proper topics to send/get data from the node to the DetectionsCohortReview plugin
        self._filenames_topic = f'{self._parent_node.identifier}.filenames'
        self._pub_sub_manager.subscribe(self, self._filenames_topic)  
        self._subject_chans_label_topic = f'{self._parent_node.identifier}.subject_chans_label'
        self._pub_sub_manager.subscribe(self, self._subject_chans_label_topic)  
        self._ROIs_cohort_topic = f'{self._parent_node.identifier}.ROIs_cohort'
        self._pub_sub_manager.subscribe(self, self._ROIs_cohort_topic)  
        self._ROIs_subjects_topic = f'{self._parent_node.identifier}.ROIs_subjects' 
        self._pub_sub_manager.subscribe(self, self._ROIs_subjects_topic)  
        

    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        self.ping_complete = 1
        self._pub_sub_manager.publish(self, self._filenames_topic, 'ping')
        self._pub_sub_manager.publish(self, self._subject_chans_label_topic, 'ping')
        self._pub_sub_manager.publish(self, self._ROIs_cohort_topic, 'ping')
        self._pub_sub_manager.publish(self, self._ROIs_subjects_topic, 'ping')
        

    def on_apply_settings(self):
        """ Called when the user clicks on "Apply" 
        """
        # Send the settings to the publisher for inputs to DetectionsCohortReview
        self._pub_sub_manager.publish(self, self._filenames_topic, str(self.filenames))
        self._pub_sub_manager.publish(self, self._subject_chans_label_topic, str(self.subject_chans_label))
        self._pub_sub_manager.publish(self, self._ROIs_cohort_topic, str(self.ROIs_cohort))
        self._pub_sub_manager.publish(self, self._ROIs_subjects_topic, str(self.ROIs_subjects))
        

    def on_topic_update(self, topic, message, sender):
        """ Called Whenever a value is updated within the context, all steps receives a 
            self._context_manager.topic message and can then act on it.
            
                if topic == self._context_manager.topic:

                    The message will be the KEY of the value that's been updated inside the context.
                    If it's the one you are looking for, we can then take the updated value and use it.
                    if message == "context_some_other_step":
                        updated_value = self._context_manager["context_some_other_step"]
        """
        pass


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._filenames_topic:
            if len(message)>0:
                self.filenames = eval(message)
        if topic == self._subject_chans_label_topic:
            self.subject_chans_label = eval(message)
            self.ping_complete = self.ping_complete + 1
        if topic == self._ROIs_cohort_topic:
            self.ROIs_cohort = eval(message)
            self.ping_complete = self.ping_complete + 1
        if topic == self._ROIs_subjects_topic:   
            self.ROIs_subjects = eval(message)
            self.ping_complete = self.ping_complete + 1
        if self.ping_complete == 4:
            if self.filenames:
                # Generate a signal to inform that self.filenames has been updated
                self.filenames_updated_signal.emit()
                # Read the files to fill self.data_df
                for file in self.filenames:
                    self._read_detector_file(file)
                # Update the model based on the self.subject_chans_label loaded from the pipeline
                self.create_model_subject_chan()
                self.update_items_from_subject_chans_label_and_ROIs_subjects()
                # Generate a signal to inform that self.filenames has been updated
                #self.filenames_updated_signal.emit()
                self.select_first_subject()


    # Called when the user push on the button clear subject list
    def clear_subject_slot(self):
        self.model_subject_chan.clear()
        self.chan_cohort_listWidget.clear()
        self.data_df = pd.DataFrame()
        self.subject_chans_label = {}
        self.ROIs_cohort = {}
        self.ROIs_subjects = {} 
        # Modify the channel label in the model and update the view (including the Cohort List Widjet)
        self.update_items_from_subject_chans_label_and_ROIs_subjects()
        # Generate a signal to inform that self.filenames has been updated
        self.filenames = []
        self.filenames_updated_signal.emit()
        # Clear ROI
        self.message_textEdit.append( "clear subject list" )


    # Called when the user push on the button Add Events report file
    def add_subject_slot(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileNames, _ = QFileDialog.getOpenFileNames(
                        None,
                        "Open Detailed Event Cohort Report File",
                        "",
                        "Detailed Event Cohort Report files (*.tsv)",
                        options=options)        
        if isinstance(fileNames,list):
            for fileName in fileNames:
                try :
                    self._read_detector_file(fileName)
                    self.filenames.append(fileName)
                    # Generate a signal to inform that self.filenames has been updated
                    self.filenames_updated_signal.emit()
                    self.create_models_and_fill_views()

                except (ValueError, KeyError) as e:     
                    self.message_textEdit.append( "Error when reading {} : {}".format(fileName,e) )
                    self.clear_subject_slot()  
        else:
            self.message_textEdit.append("No file selected")

    
    # Called when the user checked or unchecked Select All of the subject channel list
    def select_all_subject_chan_slot(self):
        # The checkbox state will be apply to all channels : Checked or unchecked 
        checkbox_state = self.all_subject_chan_checkBox.isChecked()
        # Find the current subject
        subject_index = self.subject_listView.currentIndex()
        subject_item = self.model_subject_chan.itemFromIndex(subject_index)
        # self.subject_chans_label is a dict and its keys are the subjects
        #   each item is a list of 3 elements [original chan label, modified chan label, selected flag]
        # Update the selected_flag
        ori_channels_state = self.subject_chans_label[subject_item.text()][self.chan_state_col]
        mod_channels_state = np.ones(len(ori_channels_state))*checkbox_state
        self.subject_chans_label[subject_item.text()][self.chan_state_col][:]=mod_channels_state.astype(bool)
        # Dict to manage the ROI at the subject level
        #   keys are the subjects
        #   Each item is a list of n_ROIs with its selection label  [ROI#1 label, selection flag]
        #                                                           [ROI#2 label, selection flag]
        #    
        #                                                                ...
        if subject_item.text() in self.ROIs_subjects.keys():
            temp_ROIs_subjects = {}                                                           
            temp_ROIs_subjects[subject_item.text()] = []
            for roi_label, roi_state in self.ROIs_subjects[subject_item.text()]:
                temp_ROIs_subjects[subject_item.text()].append([roi_label, self.all_subject_chan_checkBox.isChecked()])
            self.ROIs_subjects[subject_item.text()] = temp_ROIs_subjects[subject_item.text()]
            
        # Modify the channel label in the model and update the view (including the Cohort List Widjet)
        self.update_items_from_subject_chans_label_and_ROIs_subjects()


    # Called when the user checked or unchecked Select All of the cohort channel list
    def select_all_cohort_chan_slot(self):
        # The checkbox state will be apply to all channels : Checked or unchecked 
        checkbox_state = self.all_cohort_chan_checkBox.isChecked()
        # Set checkstates of the model
        # self.subject_chans_label is a dict and its keys are the subjects
        #   each item is a list of 3 elements [original chan label, modified chan label, selected flag]
        # Update the selected_flag
        for subject_id in self.subject_chans_label:
            ori_channels_state = self.subject_chans_label[subject_id][self.chan_state_col]
            mod_channels_state = np.ones(len(ori_channels_state))*checkbox_state
            self.subject_chans_label[subject_id][self.chan_state_col][:]=mod_channels_state.astype(bool)
        # Dict to manage the ROI at the subject level
        #   keys are the subjects
        #   Each item is a list of n_ROIs with its selection label  [ROI#1 label, selection flag]
        #                                                           [ROI#2 label, selection flag]
        #                                                               ...
        for subject_id in self.subject_chans_label:    
            if subject_id in self.ROIs_subjects.keys():
                temp_ROIs_subjects = {}                                                           
                temp_ROIs_subjects[subject_id] = []
                for roi_label, roi_state in self.ROIs_subjects[subject_id]:
                    temp_ROIs_subjects[subject_id].append([roi_label, self.all_cohort_chan_checkBox.isChecked()])
                self.ROIs_subjects[subject_id] = temp_ROIs_subjects[subject_id]

        # Modify the channel label in the model and update the view (including the Cohort List Widjet)
        self.update_items_from_subject_chans_label_and_ROIs_subjects()        


    # Called when the user push on the button Add ROI
    def add_ROI_slot(self):
        # Open a dialog window to ask to user which channel to average
        roi_dialog = DialogROI(self.cohort_chan_list)
        if roi_dialog.exec_():
            roi_blank_cur = True if roi_dialog.blank_checkBox.checkState()==Qt.Checked else False
            if len(roi_dialog.label_checked_lst)>0:
                # Save the ROI just added by user at the cohort level
                roi_label = self._name_roi(roi_dialog.label_checked_lst, roi_blank_cur)

                # Dict to manage the ROI created at the cohort level
                #   keys are ROIs labels
                #   Each item is a list of 3 elements [channel list to average, blank flag]
                self.ROIs_cohort[roi_label] = [roi_dialog.label_checked_lst, roi_blank_cur]

                # Dict to manage the ROI at the subject level
                #   keys are the subjects
                #   Each item is a list of n_ROIs with its selection label  [ROI#1 label, selection flag]
                #                                                           [ROI#2 label, selection flag]
                #                                                               ...
                for subject_id in list(self.subject_chans_label.keys()):
                    # If an ROI has already been added for the subject -> append
                    if subject_id in list(self.ROIs_subjects.keys()):
                        self.ROIs_subjects[subject_id].append([roi_label, True])
                    else:
                        self.ROIs_subjects[subject_id]=[[roi_label, True]]

                # Fill the model_subject_chan based on the self.subject_chans_label and update the channel cohort list widget.
                self.update_items_from_subject_chans_label_and_ROIs_subjects()
                self.select_first_subject()            

                # Display message about the created ROI
                if roi_blank_cur== Qt.Checked:
                    self.message_textEdit.append(f"ROI {roi_label} created with blank checked")
                else:
                    self.message_textEdit.append(f"ROI {roi_label} created with blank unchecked")
            else:
                self.message_textEdit.append( "No ROI created" ) 
        else:
            self.message_textEdit.append( "No ROI created" ) 


    def _name_roi( self, roi_chan_lst, roi_blank):
        # To name the ROI based on the selected channels
        #item_label = "ROI_avg_"
        item_label = "ROI_"
        for chan_i in roi_chan_lst:
            item_label += chan_i
        if roi_blank:
            item_label += "_b"
        return item_label


    def _read_detector_file(self, fileName, item_sep='\t', decimal_sep='.'):
        """ Read the csv file, save the data locally and fill all the views.
        """
        # Read the csv file and convert the content into a Data Frame
        data_df = pd.read_csv(fileName, delimiter=item_sep, \
            decimal=decimal_sep, header=0, usecols=self.labels_to_extract, dtype=str)
        data_df = data_df.dropna(how='all')
        # Save the data loaded
        if self.data_df.empty:
            self.data_df=data_df
        else: 
            self.data_df = pd.concat([self.data_df, data_df])


    # Select by default the first subject
    def select_first_subject(self):
        if self.model_subject_chan.rowCount()>0:
            first_subect_item = self.model_subject_chan.item(0)
            first_subject_index = self.model_subject_chan.indexFromItem(first_subect_item)
            self.subject_listView.setCurrentIndex(first_subject_index)
            self.subject_selection_changed_slot(first_subject_index)


    def create_models_and_fill_views(self):
        # Fill the model with all the subjects and theirs channels states
        #   channels states are taken from self.subject_chans_label if available otherwise they are checked
        # Items are added into QListWidjet for the cohort channel list
        
        self.create_model_subject_chan()
        self.select_first_subject()

        # Channel box at the subject level
        self.all_subject_chan_checkBox.setChecked(True)
        # Channel box at the cohort level (all subject)
        self.all_cohort_chan_checkBox.setChecked(True)

        # print info about the dataframe loaded
        self.message_textEdit.append("Detailed events cohort report file loaded:")
        self.print_PSA_df_info(self.data_df)


    # Return an tree item : parent=subject, (child=channels (checkable), ROI flag)
    def create_subject_item(self, subject_id, chan_lst, chan_state=None):
        subject_item = QStandardItem(subject_id)
        for chan_i, chan_label in enumerate(chan_lst):
            chan_item = QStandardItem(chan_label)
            chan_item.setCheckable(True)
            if chan_state is None:
                chan_item.setCheckState(Qt.Checked)
            else:
                chan_item.setCheckState(Qt.Checked if chan_state[chan_i] else Qt.Unchecked)
            ROI_item = QStandardItem('0')
            subject_item.appendRow([chan_item, ROI_item])
        return subject_item


    # Return the tree tiem subject_item with an ROI added
    def add_ROI_to_subject_item(self, subject_item, roi_label, roi_state):
        # Create the ROI item flag to identify that it is an ROI
        label_item = QStandardItem(roi_label)
        #label_item.setEditable(False)
        label_item.setCheckable(True)
        label_item.setCheckState(Qt.Checked if roi_state else Qt.Unchecked)
        flag_item = QStandardItem('1')
        subject_item.appendRow([label_item, flag_item])
        return subject_item


    # Return the item of a filename
    def get_file_item(self, filename, files_model):
        file_item = files_model.findItems(filename, flags=QtCore.Qt.MatchExactly, column=0)
        if file_item is not None:
            if len(file_item)>0:
                return file_item[0]
            else:
                return file_item
        else:
            return None


    # Fill the model_subject_chan model by creating items based on the self.data_df and self.subject_chans_label.
        #   channels states are taken from self.subject_chans_label if available otherwise they are checked
    # model is a tree
    # subject   -> (channel1, ROI flag)
    #           -> (channel2, ROI flag)
    #           -> ...
    # Also add items to the QlistWidjet for cohort channel list
    def create_model_subject_chan(self):
        chan_cohort_list = []
        subject_list = self.data_df[self.labels_to_extract[0]].drop_duplicates().to_list()
        for subject_i in subject_list:
            # self.subject_chans_label is a dict and the Keys are the subjects
            #   each item is a list of 3 elements [original chan label, modified chan label, selected flag]
            if subject_i in list(self.subject_chans_label.keys()):
                cur_chan_lst_ori, cur_chan_lst, cur_chan_states = self.subject_chans_label[subject_i]
                chan_cohort_list.append(cur_chan_lst)
                # If the model does not have yet the subject (load_settings_view)
                file_item = self.get_file_item(subject_i, self.model_subject_chan)
                if file_item is None or (isinstance(file_item,list) and len(file_item)==0): 
                    subject_item = self.create_subject_item(subject_i, cur_chan_lst, cur_chan_states)
                    self.model_subject_chan.appendRow(subject_item)
            else:
                cur_sjt_df = self.data_df[self.data_df[self.labels_to_extract[0]]==subject_i]
                cur_chan_lst = cur_sjt_df[self.labels_to_extract[1]].drop_duplicates().to_list()
                mod_chan_lst = cur_sjt_df[self.labels_to_extract[1]].drop_duplicates().to_list()
                chan_cohort_list.append(cur_chan_lst)
                # subject_item   -> (channel1, ROI flag)
                #                -> (channel2, ROI flag)
                #                -> ...
                subject_item = self.create_subject_item(subject_i, cur_chan_lst)
                self.model_subject_chan.appendRow(subject_item)
                # Create the dict to send to the DetectionsCohortReview plugin and used to load a saved pipeline
                states_lst = [True for i in range(len(cur_chan_lst))]
                self.subject_chans_label[subject_i] = [cur_chan_lst, mod_chan_lst, states_lst]

        # Create the unique list of channel for the subjects in extracted_data
        #   -> the channel list for the current extracted_data
        flat_list = [item for sublist in chan_cohort_list for item in sublist]
        chan_cohort_list = (list(set(flat_list)))
        #   -> the channel list for the whole cohort
        self.cohort_chan_list.append(chan_cohort_list)
        flat_list = []
        for sublist in self.cohort_chan_list:
            if isinstance(sublist,list):
                for item in sublist:
                    flat_list.append(item)
            else:
                flat_list.append(sublist)
        self.cohort_chan_list = (list(set(flat_list)))
        self.cohort_chan_list = sorted(self.cohort_chan_list)

        # Fill the channel cohort list widget
        self.create_channel_cohort_list(self.cohort_chan_list)

        self.message_textEdit.append('\nTotal number of subjects : {}'.format(len(subject_list)))
        self.message_textEdit.append(f'\n{len(self.cohort_chan_list)} channel labels available')


    # Fill the model_subject_chan based on the self.subject_chans_label and update the channel cohort list widget.
    # model is a tree
    # subject   -> (channel1, ROI flag)
    #           -> (channel2, ROI flag)
    #           -> ...
    # subject items are displayed on the self.subject_listView and
    # channels items are displayed on the self.chan_subject_listView
    # unique list of channels are displayed on self.chan_cohort_listWidget
    def update_items_from_subject_chans_label_and_ROIs_subjects(self):
        chan_cohort_list = []
        state_cohort_list = []
        
        # We disconnect the model because we are modifying in loop the items
        self.model_subject_chan.itemChanged.disconnect(self.item_changed_subject_slot)
        
        # ---------  model_subject_chan --------------
        # Through all subjects update the model
        for subject_i in list(self.subject_chans_label.keys()):
            # Find in the model the item of the current subject
            item_lst = self.model_subject_chan.findItems(subject_i, flags=Qt.MatchExactly)
            if len(item_lst)>0: 
                subject_item = item_lst[0]

                # Update the current subject item (new channel label and new channel state)
                chan_cohort_list, state_cohort_list = \
                    self._update_1_item_subject_for_std_chan(subject_item, chan_cohort_list, state_cohort_list)
                        
                # Update the current subject item (new ROI label and new ROI state)
                chan_cohort_list, state_cohort_list = \
                    self._update_1_item_subject_for_ROI(subject_item, chan_cohort_list, state_cohort_list)

        # Reconnect what we disconnect
        self.model_subject_chan.itemChanged.connect(self.item_changed_subject_slot)

        # ---------  cohort list widget --------------        
        # Create the unique list of channel for the subjects 
        #   chan_cohort_list and state_cohort_list include all the occurrences through the subjects
        self._generate_unique_cohort_channel_list(chan_cohort_list, state_cohort_list)

        # Fill the channel cohort list widget based on the unique channel list and state
        self.create_channel_cohort_list(self.cohort_chan_list, self.cohort_state_list)


    # Create the unique list of channel for the subjects 
    #   chan_cohort_list and state_cohort_list include all the occurrences through the subjects
    def _generate_unique_cohort_channel_list(self, chan_cohort_list, state_cohort_list):
        # Unique list of channel label
        self.cohort_chan_list = (list(set(chan_cohort_list)))
        self.cohort_chan_list = sorted(self.cohort_chan_list)
        # State list of the unique channel list
        self.cohort_state_list = []
        # Loop through the unique channel list
        for i_chan in self.cohort_chan_list:
            # All indexes of the current channel
            chan_idx_lst = [i for i, x in enumerate(chan_cohort_list) if x == i_chan]
            # States of the current channel
            states = [state_cohort_list[i] for i in chan_idx_lst]
            # Verify if the final state is Unchecked, PartiallyChecked or Checked
            if sum(states)==len(states):
                self.cohort_state_list.append(Qt.Checked)
            elif sum(states)==0:
                self.cohort_state_list.append(Qt.Unchecked)
            else:
                self.cohort_state_list.append(Qt.PartiallyChecked)


    # Update the current subject item (new channel label and new channel state)
    def _update_1_item_subject_for_std_chan(self, subject_item, chan_cohort_list, state_cohort_list):    
        subject_i = subject_item.text()    
        # For all the channels of the current subject
        for channel_row in range(subject_item.rowCount()):
            chan_label_col = 0
            ROI_flag_col = 1
            # Any change to the model will call item_changed_subject_slot
            ROI_flag = subject_item.child(channel_row, ROI_flag_col).text()
            channels_label_item = subject_item.child(channel_row,chan_label_col)
            if not int(ROI_flag):
                # Update the model from subject_chans_label
                channels_label_item.setText(self.subject_chans_label[subject_i][self.mod_chan_label_col][channel_row])
                channels_label_item.setCheckState(Qt.Checked if self.subject_chans_label[subject_i][self.chan_state_col][channel_row] else Qt.Unchecked)
                state_cohort_list.append(1 if self.subject_chans_label[subject_i][self.chan_state_col][channel_row] else 0)
                chan_cohort_list.append(channels_label_item.text())
        return chan_cohort_list, state_cohort_list


    # Update the current subject item (new ROI label and new ROI state)
    def _update_1_item_subject_for_ROI(self, subject_item, chan_cohort_list, state_cohort_list):    
        subject_i = subject_item.text()    
        # For all the ROIs of the current subject if any
        if subject_i in list(self.ROIs_subjects.keys()):
            for cur_ROI, cur_sel in self.ROIs_subjects[subject_i]:
                new_item=1 # Flag to verify if the ROI item is new
                for row_i in range(subject_item.rowCount()):
                    child_item = subject_item.child(row_i)
                    # Modify an existing item
                    if child_item.text()==cur_ROI:
                        child_item.setCheckState(Qt.Checked if cur_sel else Qt.Unchecked)
                        new_item=0    
                if new_item==1:                        
                    # Return the tree item subject_item with an ROI added
                    subject_item = self.add_ROI_to_subject_item(subject_item, cur_ROI, cur_sel)
                chan_cohort_list.append(cur_ROI)
                state_cohort_list.append(cur_sel)
        return chan_cohort_list, state_cohort_list


    # Fill the channels cohort list (checkable)
    # Fill the QListWidget "chan_cohort_listWidget"
    def create_channel_cohort_list(self, chan_lst, cohort_state_list=None):
        self.chan_cohort_listWidget.clear()
        for i, chan in enumerate(chan_lst):
            chan_item = QListWidgetItem(chan)
            if cohort_state_list is not None: 
                chan_item.setCheckState(cohort_state_list[i])
            else:
                chan_item.setCheckState(Qt.Checked)
            chan_item.setFlags(Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            self.chan_cohort_listWidget.addItem(chan_item) 
 

    def subject_selection_changed_slot(self, index):
        ''' Called when the user select another subjects from the subject list
        ''' 
        # Display the right subject in the chan_subject_listView
        self.chan_subject_listView.setRootIndex(index)        


    def item_changed_subject_slot(self, item):
        ''' Called when the user changes an item (check or uncheck) from the 
        channel list (this slot is also connected to the channel list model (model_subject_chan)).
        ''' 
        # Find the parent item in the model
        subject_item = item.parent()
        subject_id = subject_item.text()
        # identify the row
        channel_row = item.row()     
        # Find out if it is a standard channel or ROI
        roi_flag = subject_item.child(channel_row,1).text()

        if not int(roi_flag):
            # self.subject_chans_label is a dict and its keys are the subjects
            #   each item is a list of 3 elements [original chan label, modified chan label, selected flag]
            # Update the modified channel label
            self.subject_chans_label[subject_id][self.mod_chan_label_col][channel_row]=item.text()
            # Update the selected_flag
            self.subject_chans_label[subject_id][self.chan_state_col][channel_row]=True if item.checkState()==Qt.Checked else False
        else:
            # Dict to manage the ROI at the subject level
            #   keys are the subjects
            #   Each item is a list of n_ROIs with its selection label  [ROI#1 label, selection flag]
            #                                                           [ROI#2 label, selection flag]
            #                                                               ...

            # Dict to manage the ROI at the cohort level
            #   keys are ROIs labels
            #   Each item is a list of 3 elements [channel list to average, blank flag, bool selected flag]
            self.ROIs_cohort[item.text()][2] = True if item.checkState()==Qt.Checked else False

            ROI_row = 0
            for ROI_label, ROI_sel in self.ROIs_subjects[subject_id]:
                if ROI_label==item.text():
                    # Update the modified channel label and state
                    self.ROIs_subjects[subject_id][ROI_row]=[item.text(), True if item.checkState()==Qt.Checked else False]  
                ROI_row += 1   
        
        # Modify the channel label in the model and update the view (including the Cohort List Widjet)
        self.update_items_from_subject_chans_label_and_ROIs_subjects()


    def item_changed_cohort_slot(self, item):
        ''' Called when the user changes an item (check or uncheck) from the 
        chan cohort list (this slot is connected to the QListWidjetItem ).
        '''   
        # Manage the channel labels if edited via self.subject_chans_label
        channel_row = self.chan_cohort_listWidget.indexFromItem(item).row()
        channel_mod = self.cohort_chan_list[channel_row]
        # Modify the channel label and the state in the self.subject_chans_label
        for subject_id in list(self.subject_chans_label.keys()):
            chan_lst_mod = self.subject_chans_label[subject_id][self.mod_chan_label_col]
            if subject_id in self.ROIs_subjects.keys():
                roi_lst_mod = [label for label, state in self.ROIs_subjects[subject_id]]
            else:
                roi_lst_mod = []
            if (channel_mod in chan_lst_mod) or (channel_mod in roi_lst_mod):
                if (channel_mod in chan_lst_mod):
                    channel_row = chan_lst_mod.index(channel_mod)
                    self.subject_chans_label[subject_id][self.mod_chan_label_col][channel_row]= item.text()
                    # The name could have been changed without modifying the state
                    # Modifying the state makes it Checked or Unchecked
                    #   If the state is PartiallyChecked, it is because it has not been modified by the user
                    if not item.checkState()==Qt.PartiallyChecked:
                        self.subject_chans_label[subject_id][self.chan_state_col][channel_row]=True if item.checkState()==Qt.Checked else False
                else:
                    channel_row = roi_lst_mod.index(channel_mod)
                    self.ROIs_subjects[subject_id][channel_row][0]= item.text()
                    self.ROIs_subjects[subject_id][channel_row][1]= True if item.checkState()==Qt.Checked else False              
        # Modify the channel label in the model and update the view (including the Cohort List Widjet)
        self.update_items_from_subject_chans_label_and_ROIs_subjects()


    def print_PSA_df_info( self, PSA_df):
        ''' Print the data frame info in the Message windows
        '''
        buffer = io.StringIO()
        PSA_df.info(buf=buffer,verbose=False)
        message_to_show = buffer.getvalue()
        start = message_to_show.find('>')
        stop = message_to_show.find('memory')
        self.message_textEdit.append(message_to_show[start+1:stop]) 


   # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._filenames_topic)
            self._pub_sub_manager.unsubscribe(self, self._subject_chans_label_topic)
            self._pub_sub_manager.unsubscribe(self, self._ROIs_cohort_topic)
            self._pub_sub_manager.unsubscribe(self, self._ROIs_subjects_topic)
        
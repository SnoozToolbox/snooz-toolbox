#! /usr/bin/env python3
"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    ROIStep
    Step to define the ROIs if any (select the appropriate channels).
    The ROI definition are send to the slow wave pics generator plugin.
"""
from qtpy import QtWidgets
from qtpy.QtWidgets import QListWidgetItem
from qtpy.QtCore import Qt

from commons.BaseStepView import BaseStepView

from CEAMSTools.SlowWaveImages.InputFilesStep.InputFilesStep import InputFilesStep
from CEAMSTools.SlowWaveImages.ROIStep.Ui_ROIStep import Ui_ROIStep
from CEAMSTools.SlowWaveImages.ROIStep.DialogROI import DialogROI

class ROIStep(BaseStepView, Ui_ROIStep, QtWidgets.QWidget):
    """
        ROIStep
        Step to define the ROIs if any (select the appropriate channels).
        The ROI definition are send to the slow wave pics generator plugin.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        self._sw_wave_pics_node = "34950575-1519-44e1-852d-a7720eead65f" # identifier for slow wave pics generator
        # Subscribe to the proper topics to send/get data from the node
        self._ROI_topic = f'{self._sw_wave_pics_node}.ROIs_def'
        self._pub_sub_manager.subscribe(self, self._ROI_topic)
        self._chan_ROI_sel_topic = f'{self._sw_wave_pics_node}.chans_ROIs_sel'
        self._pub_sub_manager.subscribe(self, self._chan_ROI_sel_topic)
        
        self.cohort_chan_list = [] # The list of selected channels across subjects
        self.cohort_chanROI_state = {} # Dict to keep track of channels\ROIs selected by user
        # Keys are ROI label and values are the list of channels in the ROI and the blank flag
        self.ROIs_def = {}


    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        # It is a good place to do all ping calls that will request the 
        # underlying process to get the value of a module.
        self._pub_sub_manager.publish(self, self._ROI_topic, 'ping')
        self._pub_sub_manager.publish(self, self._chan_ROI_sel_topic, 'ping')
        self.refresh_chan_sel_slot()
        # Generate the cohort channel list based on the file model
        #self.generate_cohort_chan_list()
        # Populate the list widget with the checkbox slection
        #self.populate_list_widget()


    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        if topic == self._context_manager.topic:
            if message == InputFilesStep.context_files_view:
                self.refresh_chan_sel_slot()


    def on_topic_response(self, topic, message, sender):
        # This will be called as a response to ping request.
        if topic == self._ROI_topic:
            if isinstance(message, str) and not message=="":
                self.ROIs_def = eval(message)
            elif isinstance(message, dict):
                self.ROIs_def = message
            else:
                self.ROIs_def = {}
        if topic == self._chan_ROI_sel_topic:
            if isinstance(message, str) and not message=="":
                self.cohort_chanROI_state = eval(message)
            elif isinstance(message, dict):
                self.cohort_chanROI_state = message
            else:
                self.cohort_chanROI_state = {}


    def on_apply_settings(self):
        # Send the dictionary as an input to the PSGReader module
        self._pub_sub_manager.publish(self, self._ROI_topic, self.ROIs_def)
        self._pub_sub_manager.publish(self, self._chan_ROI_sel_topic, self.cohort_chanROI_state)


    def on_validate_settings(self):
        # Validate that all input were set correctly by the user.
        # If everything is correct, return True.
        # If not, display an error message to the user and return False.
        # This is called just before the apply settings function.
        # Returning False will prevent the process from executing.
        return True


    # Called when the user push the button to refresh channels selection
    def refresh_chan_sel_slot(self):
        # Access to the PsgReaderSettingsView to access easily informations about the files
        self.reader_settings_view = self._context_manager[InputFilesStep.context_files_view]
        # Generate the cohort channel list (used) based on the file model
        self.generate_cohort_chan_list()
        # Populate the list widget with the checkbox selection
        self.populate_list_widget()


    # Called when the user push on the button Add ROI
    def add_ROI_slot(self):
        # Open a dialog window to ask to user which channel to average
        roi_dialog = DialogROI(self.cohort_chan_list)
        if roi_dialog.exec_():
            roi_blank_cur = True if roi_dialog.blank_checkBox.checkState()==Qt.Checked else False
            if len(roi_dialog.label_checked_lst)>0:
                # Save the ROI just added by user at the cohort level
                #roi_label = self._name_roi(roi_dialog.label_checked_lst, roi_blank_cur)
                roi_label_user = roi_dialog.lineEdit_ROI.text()
                if "roi" not in roi_label_user.lower():
                    roi_label = f"ROI_{roi_label_user}"
                else:
                    roi_label = roi_label_user
                if roi_blank_cur:
                    roi_label = roi_label + " " + str(roi_dialog.label_checked_lst) + " blank"
                else:
                    roi_label = roi_label + str(roi_dialog.label_checked_lst)

                # Dict to manage the ROI created at the cohort level
                #   keys are ROIs labels
                #   Each item is a list of 3 elements [channel list to average, blank flag]
                self.ROIs_def[roi_label] = [roi_dialog.label_checked_lst, roi_blank_cur]
                
                # Add ROI to the cohort_chanROI_state
                for ROI_label in self.ROIs_def.keys():
                    self.cohort_chanROI_state[ROI_label] = True

                # Refresh the list widget
                self.populate_list_widget()

        self.refresh_chan_sel_slot()


    # Called when the user push on the button Remove ROI
    def rem_ROI_slot(self):
        # Remove the ROI selected by user at the cohort level
        roi_label = self.chan_cohort_listWidget.currentItem().text()
        if roi_label in self.ROIs_def.keys():
            del self.ROIs_def[roi_label]
            del self.cohort_chanROI_state[roi_label]
            self.refresh_chan_sel_slot()


    def generate_cohort_chan_list(self):
        # Get the list of channels used in the cohort
        channels_info_df = self.reader_settings_view.channels_table_model.get_data()
        file_list = channels_info_df['Filename'].unique()
        all_chan_sel = []
        if len(file_list)>0:
            # For each recording check the channel selection
            for file in file_list:
                chans_used = channels_info_df[(channels_info_df['Filename']==file) & (channels_info_df['Use']==True)]
                if len(chans_used)>0:
                    all_chan_sel.append(list(chans_used['Channel']))
        cohort_chan_list = list(set([item for sublist in all_chan_sel for item in sublist]))
        # Make the list unique
        self.cohort_chan_list = list(set(cohort_chan_list))

        # Update the cohort_chanROI_state
        cohort_chanROI_state = {}
        # If the item of the list is new, add it to the cohort_chanROI_state dict to True
        for item in self.cohort_chan_list:
            # For each new item, add it to the cohort_chanROI_state dict
            if item not in self.cohort_chanROI_state.keys():
                cohort_chanROI_state[item] = True
            else:
                cohort_chanROI_state[item] = self.cohort_chanROI_state[item]
        # Add the ROI to the cohort_chanROI_state dict usinf the state from self.cohort_chanROI_state
        for ROI_label in self.ROIs_def.keys():
            cohort_chanROI_state[ROI_label] = self.cohort_chanROI_state[ROI_label]
        self.cohort_chanROI_state = cohort_chanROI_state


    def item_changed_slot(self, item):
        if item.checkState() == Qt.Checked:
            self.cohort_chanROI_state[(item.text())] = True
        else:
            self.cohort_chanROI_state[(item.text())] = False


    def populate_list_widget(self):
        # Fill the list widget with the cohort channel list
        self.chan_cohort_listWidget.clear()
        # For each item in the cohort_chanROI_state dict, add it to the list widget
        for item_label in self.cohort_chanROI_state.keys():
            # Create an item with the label item_label and the bool value in the cohort_chanROI_state as the state
            item = QListWidgetItem(item_label, self.chan_cohort_listWidget)
            item.setCheckState(Qt.Checked if self.cohort_chanROI_state[item_label] else Qt.Unchecked)
            # Rename the item that start with ROI for the name included the ROI label
        self.chan_cohort_listWidget.itemChanged.connect(self.item_changed_slot)
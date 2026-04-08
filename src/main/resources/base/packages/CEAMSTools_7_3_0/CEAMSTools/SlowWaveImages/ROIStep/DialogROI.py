from CEAMSTools.SlowWaveImages.ROIStep.Ui_DialogAddChan import Ui_DialogAddChan

import numpy as np
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QDialog
from qtpy.QtGui import QStandardItemModel, QStandardItem


class DialogROI(QDialog, Ui_DialogAddChan): 
    def __init__(self, chan_cohort_list, *args, **kwargs):
        super(DialogROI, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # The list read by the PSACohortReviewSettingsView to know which chan is selected
        self.check_state_lst = []
        self.label_checked_lst = []
        
        # Create an empty model and add it to the QListView
        self.model_chan_roi_list = QStandardItemModel(self.listView_addChan)
        self.listView_addChan.setModel(self.model_chan_roi_list)
        # itemChanged is a signal in QStandardItemModel Class
        # Connect itemChanged to the slot on_item_changed allows to perform 
        # operations when a channel is checked or unchecked
        self.model_chan_roi_list.itemChanged.connect(self.on_item_changed_ROI)
        # Create the model with the channel list (all channels unchecked)
        self.create_roi_model( chan_cohort_list )      


    def create_roi_model( self, channel_lst ):
        """ Fill the roi model and its QListView.
        """
        self.check_state_lst = np.zeros(len(channel_lst))
        for channel_i in channel_lst:
            # Create an item with a caption
            item = QStandardItem(channel_i)
            # Add a checkbox to it
            item.setCheckable(True)
            item.setCheckState(Qt.Unchecked)
            if "roi" in item.text().lower():
                item.setEnabled(False)
            else:
                item.setEnabled(True)
            # Add the item to the model
            self.model_chan_roi_list.appendRow(item)
        self.model_chan_roi_list.layoutChanged.emit()


    def on_item_changed_ROI(self, item):
        ''' Called when the user changes an item (check or uncheck) from the 
        channel list (this slot is connected to the model_chan_roi_list).
        '''        
        # Saved the new state of the item modified
        self.check_state_lst[item.row()]=int(item.checkState()==Qt.CheckState.Checked)
        if item.checkState()==Qt.Checked:
            self.label_checked_lst.append(item.text())
        else:
            self.label_checked_lst.remove(item.text())
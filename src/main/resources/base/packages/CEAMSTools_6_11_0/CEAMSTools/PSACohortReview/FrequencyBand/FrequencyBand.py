#! /usr/bin/env python3
"""
    FrequencyBand
    TODO CLASS DESCRIPTION
"""
from io import StringIO
import numpy as np
import pandas as pd
from qtpy import QtWidgets
from qtpy.QtWidgets import QFileDialog, QHeaderView, QMessageBox

from commons.BaseStepView import BaseStepView
from widgets.WarningDialog import WarningDialog
from commons.NodeRuntimeException import NodeRuntimeException
from CEAMSTools.PSACohortReview.FrequencyBand.PandasModel import PandasModel
from CEAMSTools.PSACohortReview.FrequencyBand.Ui_FrequencyBand import Ui_FrequencyBand
from CEAMSTools.PSACohortReview.InputFiles.InputFiles import InputFiles

class FrequencyBand(BaseStepView, Ui_FrequencyBand, QtWidgets.QWidget):
    
    """
        FrequencyBand
        Step to define the frequency bands to average the PSA.
        Each band is specified with a num-start(Hz), num-end(Hz), den-start(Hz) and den-end(Hz) to allow 
        absolute or relative band.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Define modules and nodes to talk to
        self._PSA_review_identifier = "8df6ac98-9c6c-4f97-a579-5464ba4b6fe1"
        # Subscribe to the proper topics to send/get data from the node to the PSACohortReview plugin
        self._freq_band_topic = f'{self._PSA_review_identifier}.freq_band'
        self._pub_sub_manager.subscribe(self, self._freq_band_topic)  

        # init UI
        self.setupUi(self)
        self.filenames = [] # will be defined with context manager from the step InputFiles.
        self.labels_to_extract = ['freq_low_Hz', 'freq_high_Hz']

        # If necessary, init the context. The context is a memory space shared by 
        # all steps of a tool. It is used to share and notice other steps whenever
        # the value in it changes. It's very useful when the parameter within a step
        # must have an impact in another step.
        # self._context_manager[self.context_FrequencyBand] = {"the_data_I_want_to_share":"some_data"}
    
        # Model to define the new bands (absolute or relative freq bands)
        self.freq_band_labels = ['num-start(Hz)','num-end(Hz)','den-start(Hz)','den-end(Hz)']
        self.model_freq_band = PandasModel(pd.DataFrame(columns=self.freq_band_labels)) 
        self.new_band_tableView.setModel(self.model_freq_band)
        header = self.new_band_tableView.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

        # Model to define the tiny bands included in the PSA file
        cur_freq_df = pd.DataFrame(columns=['start', 'stop'])
        self.model_freq_bin = PandasModel(cur_freq_df) 
        self.tiny_band_tableView.setModel(self.model_freq_bin)
        header = self.tiny_band_tableView.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)    


    def load_settings(self):
        """ Called when the settingsView is opened by the user
        Ask for the settings to the publisher to display on the SettingsView 
        """
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        self._pub_sub_manager.publish(self, self._freq_band_topic, 'ping')


    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        if topic == self._context_manager.topic:
            # The message will be the KEY of the value that's been updated inside the context.
            # If it's the one you are looking for, we can then take the updated value and use it.
            if message == InputFiles.context_InputFiles:
                self.filenames = self._context_manager[InputFiles.context_InputFiles]
                self.fill_tiny_band_view()


    def on_topic_response(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
        """
        if topic == self._freq_band_topic:
            # If empty, the constructor has already defined the data on the self.model_freq_band
            if (not message=='') and not ("Empty DataFrame" in message):
                temp_df = pd.read_csv(StringIO(message), sep='\s+', index_col=0)
                temp_df.dropna(how='all')
                temp_df.reset_index(drop=True, inplace=True)
                self.model_freq_band.define_data(temp_df)
                self.model_freq_band.layoutChanged.emit()
            

    # To fill tiny_band_tableView with the tuiny frequency band from the PSA file.
    def fill_tiny_band_view(self):
        # Read the csv file and convert the content into a Data Frame
        for filename in self.filenames:
            PSA_df = pd.read_csv(filename, delimiter='\t', \
                decimal='.', header=0, usecols=self.labels_to_extract)
            PSA_df = PSA_df.dropna(how='all')
            PSA_df = PSA_df.drop_duplicates()
            PSA_df.reset_index(drop=True, inplace=True)
            self.tiny_freq_band = PSA_df
            self.model_freq_band.low_limit = self.tiny_freq_band[self.labels_to_extract[0]].min()
            self.model_freq_band.high_limit = self.tiny_freq_band[self.labels_to_extract[1]].max()
            self.model_freq_band.layoutChanged.emit()
        self.model_freq_bin.define_data(self.tiny_freq_band)
        self.model_freq_bin.layoutChanged.emit()


    def on_apply_settings(self):
        """ Called when the user clicks on "Run" or "Save" tool. 
        """
        # export self.model_freq_band.get_data to PSACohortReview.freq_band
        # Evaluate the frequency bands and drop duplicates
        self.drop_duplicated_frequency_bands()
        # Need to convert the dataframe into a string (convert with a comma)
        freq_band_df = self.model_freq_band.get_data()
        freq_band_str = freq_band_df.to_string()
        # Send the message (dataframe converted) to the publisher
        self._pub_sub_manager.publish(self, self._freq_band_topic, freq_band_str)


    def add_row_freq_band_slot(self):
        ''' Called when the user presses "Add" from the Frequency Bands to Compute.
        '''
        # Pandas dataframe are not suited to add row in the middle
        # Let's juste append the new row.
        # Create an empty data frame filled with nan
        a = np.empty((1,4))
        a[:]=np.nan
        empty_df = pd.DataFrame(data = a, columns=self.freq_band_labels)
        # Add the row to the model to view the change on the QTableView
        self.model_freq_band.append_row(empty_df)
        self.model_freq_band.layoutChanged.emit()


    def rem_row_freq_band_slot(self):
        ''' Called when the user presses "Rem" from the Frequency Bands to Compute.
        '''
        # Find the selected row
            # new_band_tableView is a QTableView Class and it Inherits QAbstractItemView
            # QAbstractItemView has a public function currentIndex()
            # the function currentIndex returns a QModelIndex Class
            # QModelIndex has a function row() and it returns a int
        my_qmodelindex = self.new_band_tableView.currentIndex()
        freq_band_sel_row = my_qmodelindex.row()
        self.model_freq_band.drop_row(freq_band_sel_row)
        self.model_freq_band.layoutChanged.emit()

    
    def load_freq_band_slot(self):
        ''' Called when the user presses the Load button in the frequency band
        to compute.
        '''
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
                        None,
                        "getOpenFileName()",
                        "",
                        "*.tsv",
                        options=options)        
        if fileName:
            # Read the csv file and convert the content into a Data Frame
            # TODO add a try + error window
            cur_data = pd.read_csv(fileName, delimiter='\t')
            cur_data = cur_data.dropna(how='all')
            cur_data.reset_index(drop=True, inplace=True)
            self.model_freq_band.define_data(cur_data)                    
            self.model_freq_band.layoutChanged.emit()                        

    
    def save_freq_band_slot(self):
        # Ask to the user to select or write the filename to save the csv
        sl_file_name = QFileDialog.getSaveFileName(self, \
            'Write the filename to save the tsv')
        # Concatenate .csv if missing
        if not '.tsv' in sl_file_name[0]:
            filepath = sl_file_name[0]
            filepath = filepath  + '.tsv'
        else:
            filepath = sl_file_name[0]
        # Write the new csv file
        data_to_write = self.model_freq_band.get_data()
        try :
            data_to_write.to_csv(filepath, sep='\t', index=False)  
        except : 
            error_message = f"Snooz can not write in the file {filepath}."+\
                f" Check if the drive is accessible and ensure the file is not already open."
            raise NodeRuntimeException(self.identifier, "FrequencyBand", error_message)              

    # Evaluate the frequency bands and drop duplicates
    def drop_duplicated_frequency_bands(self):
        freq_band_df = self.model_freq_band.get_data()
        freq_band_df.dropna(axis=0, how='all', inplace=True)
        self.model_freq_band.define_data(freq_band_df)
        self.model_freq_band.layoutChanged.emit()
        message_warning = ''
        if freq_band_df.empty:
            message_warning = message_warning + "No frequency band is defined."
        # Drop duplicated freq band
        if np.any(freq_band_df.duplicated().values):
            freq_band_df.drop_duplicates(inplace=True)
            self.model_freq_band.define_data(freq_band_df)
            self.model_freq_band.layoutChanged.emit()
            message_warning = message_warning + "\nDuplicated frequency bands have been dropped."
        # Drop duplicated numerator for relative band.  
        #   Because each variable is renamed as "activity_rel_chan_numerator" 
        #   therefore we can not have the same numerator in more than one relative band
        numerator = freq_band_df[['num-start(Hz)','num-end(Hz)']].astype(float)
        relative_band_mask = freq_band_df['den-start(Hz)'].notna().values
        if any(numerator.iloc[relative_band_mask].duplicated()):
            index_2_drop = numerator.iloc[relative_band_mask].duplicated()
            index_2_drop = index_2_drop[index_2_drop==True]
            for i in index_2_drop.index.values:
                self.model_freq_band.drop_row(i)
            self.model_freq_band.layoutChanged.emit()
            message_warning = message_warning + "\nDuplicated numerators for relative bands have been dropped."
        if len(message_warning)>0:
            WarningDialog(message_warning)
        
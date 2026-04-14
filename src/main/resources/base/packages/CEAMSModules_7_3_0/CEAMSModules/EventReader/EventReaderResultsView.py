#! /usr/bin/env python3

"""
    Results viewer of the EventReader plugin
"""

from qtpy import QtWidgets
from CEAMSModules.EventReader.Ui_EventReaderResultsView import Ui_EventReaderResultsView

import numpy as np
import pandas as pd

class EventReaderResultsView( Ui_EventReaderResultsView, QtWidgets.QWidget):
    """
        EventReaderView display the events list read
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(EventReaderResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)

    def load_results(self):
        # Clear the data if any
        self.result_tablewidget.setRowCount(0)        
        # Read result cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)
        if cache is not None:
            # Add time elapsed to the events list
            events = cache['events']
            if len(events)>0:
                time_elapsed_df = pd.DataFrame()
                # Compute the time elapsed for each event
                time_elapsed_df["HH"] = (np.floor(events.start_sec/3600)).astype(int)
                time_elapsed_df["MM"] = ( np.floor( (events.start_sec-time_elapsed_df["HH"]*3600) / 60 )).astype(int)
                time_elapsed_df["SS"] = np.around( (events.start_sec-time_elapsed_df["HH"]*3600 \
                    - time_elapsed_df["MM"]*60).astype(np.double),decimals=2,out=None)
                # It is important to make a copy otherwise other instance of events
                # will also be modified.
                events_to_show = events.copy()
                # concatenate the time as HH:MM:SS and add it to the events dataframe
                events_to_show['time elapsed(HH:MM:SS)'] = time_elapsed_df.HH.apply(str)\
                        + ':' + time_elapsed_df.MM.apply(str) + ':' + time_elapsed_df.SS.apply(str)
                self.write_df_to_qtable(events_to_show, self.result_tablewidget)
            else:
                self.write_df_to_qtable(events, self.result_tablewidget)
    

    def write_df_to_qtable(self, df, table):
        headers = list(df)
        table.setRowCount(df.shape[0])
        table.setColumnCount(df.shape[1])
        table.setHorizontalHeaderLabels(headers)        

        # getting data from df is computationally costly so convert it to array first
        df_array = df.values
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                table.setItem(row, col, QtWidgets.QTableWidgetItem(str(df_array[row,col])))

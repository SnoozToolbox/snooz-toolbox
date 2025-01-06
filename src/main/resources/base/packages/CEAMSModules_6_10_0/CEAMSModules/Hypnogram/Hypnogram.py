"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Module to display in the results view an hypnogram and its sleep cycles.

    Parameters
    ----------
        sleep_stages : pandas DataFrame
            List of sleep stages. (columns=['group','name','start_sec','duration_sec','channels'])
        sleep_cycles : List of tuples
            Each element of the list defines a sleep cycle. The first tuple is the 
            beginning and end of the NREM period. The second tuple is the beginning 
            and end of the REM period. Both beginning and end are inclusive indexes.
            The last variable [is_complete] tells of this cycle is complete. An incomplete
            cycle would be one without a REM period, it's often found at the end of the night.
            ((NREM_BEGIN,NREM_END), (REM_BEGIN,REM_END), is_complete)
        sleep_latency : int
            Sleep latency in epoch count
        epoch_len : int
            Epoch length in seconds
        fig_name : String
            Path to save the hypnogram picture (jpg). 
    Returns
    -----------
        None
"""

from ..PSGReader import commons
from flowpipe import SciNode, InputPlug, OutputPlug
from .HypnogramResultsView import HypnogramResultsView

# Take the the result view from the CsvReader
# CsvReader results view show a dataframe of events
#from CEAMSModules.Hypnogram.Ui_HypnogramResultsView import Ui_HypnogramResultsView

import pandas as pd
import shutil
from scipy import signal
import matplotlib.pyplot as plt
plt.switch_backend('agg')  # turn off gui

DEBUG = False

class Hypnogram(SciNode):
    """ Module to display in the results view an hypnogram and its sleep cycles.

    Parameters
    ----------
        sleep_stages : pandas DataFrame
            List of sleep stages. (columns=['group','name','start_sec','duration_sec','channels'])
        sleep_cycles : List of tuples
            Each element of the list defines a sleep cycle. The first tuple is the 
            beginning and end of the NREM period. The second tuple is the beginning 
            and end of the REM period. Both beginning and end are inclusive indexes.
            The last variable [is_complete] tells of this cycle is complete. An incomplete
            cycle would be one without a REM period, it's often found at the end of the night.
            ((NREM_BEGIN,NREM_END), (REM_BEGIN,REM_END), is_complete)
        epoch_len : int
            Epoch length in seconds
        fig_name : String
            Path to save the hypnogram picture (jpg). 
    Returns
    -----------
        None
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('Hypnogram.__init__')
        InputPlug('sleep_stages', self)
        InputPlug('sleep_cycles', self)
        InputPlug('epoch_len_sec', self)
        InputPlug('fig_name', self )

    def subscribe_topics(self):
        pass

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'Hypnogram.on_topic_update {topic}:{message}')

    def compute(self, sleep_stages, sleep_cycles, epoch_len_sec, fig_name):
        """
            Compute record the sleep stages and sleep cycles in the cache.
            The hypnogram will be built by the HypnogramResultsView class.
        """
        if DEBUG: print('Hypnogram.compute')

        if isinstance(epoch_len_sec,str):
            if epoch_len_sec=='':
                epoch_len_sec=None
            else:
                epoch_len_sec = int(epoch_len_sec)

        sleep_stages = sleep_stages.copy()
        sleep_cycles = sleep_cycles.copy()

        self._cache_manager.write_mem_cache(self.identifier, {"sleep_stages":sleep_stages,\
                                                              "sleep_cycles":sleep_cycles, \
                                                              "epoch_len_sec":epoch_len_sec})
        if isinstance(fig_name, str) and (len(fig_name)>0):
            # Plot and save Hypnogram
            if sleep_stages is not None:
                self.figure, self.hypno_ax = plt.subplots()
                self.figure.set_size_inches(15,4)
                self.hypno_ax.clear()
                HypnogramResultsView.plot_hypnogram(self, sleep_stages, sleep_cycles, epoch_len=epoch_len_sec)
                if not '.' in fig_name:
                    fig_name = fig_name + '.pdf'
                self.figure.savefig(fig_name)

        return None

"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    SpindleDetectorSumo
    Class to detect spindles based on the SUMO deep learning algorithm
"""
from .get_model import get_model
from .sumo.config import Config
from .sumo.data import spindle_vect_to_indices
import numpy as np
import os
from os.path import isfile, join
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
import pytorch_lightning as pl
import sys

import config as snooz_config
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from flowpipe import SciNode, InputPlug, OutputPlug
from flowpipe.ActivationState import ActivationState

from CEAMSModules.EventReader import manage_events

# Comment out the following imports if no need to plot the spindles
# import matplotlib
# import matplotlib.pyplot as plt
# matplotlib.use("Agg")

# Set environment variables for evaluation timeout
os.environ['PYDEVD_WARN_EVALUATION_TIMEOUT'] = '10'
os.environ['PYDEVD_UNBLOCK_THREADS_TIMEOUT'] = '5'
os.environ['PYDEVD_THREAD_DUMP_ON_WARN_EVALUATION_TIMEOUT'] = 'true'
os.environ['PYDEVD_INTERRUPT_THREAD_TIMEOUT'] = '5'

DEBUG = False
EXPECTED_SAMPLING_RATE = 100


class SimpleDataset(Dataset):
    def __init__(self, data_vectors, mean, std):
        super(SimpleDataset, self).__init__()

        self.data = data_vectors
        self.mean = mean
        self.std = std

    def __len__(self) -> int:
        return len(self.data)

    @staticmethod
    def preprocess(data, mean, std):
        return (data-mean)/std

    def __getitem__(self, idx):
        data = self.preprocess(self.data[idx], self.mean[idx], self.std[idx])
        return torch.from_numpy(data).float(), torch.zeros(0)
    

class SpindleDetectorSumo(SciNode):
    """
    Class to detect spindles based on the SUMO deep learning algorithm

    Parameters
    ----------
        signals: List of SignalModel
            List of signal with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original         
        event_group : String
            List of Event group to filter separated by comma (discard too long, short)
        event_name : String
            List of Event name to filter separated by comma (discard too long, short)
        
    Returns
    -------
        events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            Events list for spindle detections.   
    """

    def __init__(self, **kwargs):
        """ Initialize module SpindleDetectorSumo """
        super().__init__(**kwargs)
        if DEBUG: print('SpindleDetectorSumo.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('event_group',self)
        InputPlug('event_name',self)

        # Output plugs
        OutputPlug('events',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    

    def compute(self, signals, event_group, event_name):
        """
        Detect spindles based on the SUMO deep learning algorithm

        Parameters
        ----------
        signals: List of SignalModel
            List of signal with dictionary of channels with SignalModel with        
        event_group : String
            List of Event group to filter separated by comma (discard too long, short)
        event_name : String
            List of Event name to filter separated by comma (discard too long, short)
        
        Returns
        -------
        events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            Events list for spindle detections.
            
        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """

        # Raise NodeInputException if an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if isinstance(signals, str) and signals=='':
            raise NodeInputException(self.identifier, "signals", \
                f"SpindleDetectorSUMO this input is empty, no signals no spindles.")    
        if isinstance(event_group, str) and event_group=='':
            raise NodeInputException(self.identifier, "event_group", \
                f"SpindleDetectorSUMO this input is empty, no event_group no spindles.")
        if isinstance(event_name, str) and event_name=='':
            raise NodeInputException(self.identifier, "event_name", \
                f"SpindleDetectorSUMO this input is empty, no event_name no spindles.")        

        # It is possible to bypass the "WindowsToSamples" by passing the input 
        # signals_windows to the output samples_values without any modification
        if self.activation_state == ActivationState.BYPASS:
            return {
                'events': manage_events.create_event_dataframe(None)
            }   
        if isinstance(signals, list) and len(signals) == 0:        
            return {
                'events': manage_events.create_event_dataframe(None)
            }      

        sample_rate = signals[0].sample_rate
        if sample_rate>EXPECTED_SAMPLING_RATE:
            raise NodeInputException(self.identifier, "signals", \
                f"SpindleDetectorSUMO signals are sampled at {sample_rate}Hz, it is expected to be {EXPECTED_SAMPLING_RATE}Hz.")

        # Calculate mean and std of signal epochs 
        mean = [np.nanmean(x.samples) for x in signals]
        std = [np.nanstd(x.samples) for x in signals]

        data = [x.samples for x in signals]

        # Create a dataset and dataloader
        dataset = SimpleDataset(data, mean, std)
        dataloader = DataLoader(dataset, num_workers=3, persistent_workers=True)

        # Set up the model and its config
        model_path = snooz_config.app_context.get_resource(join('models','SUMO','final.ckpt'))      
        config = Config('predict', create_dirs=False)
        model = get_model(model_path, config)

        # Safe check for terminal support - turn it off to avoid threading issues
        use_progress_bar = False#sys.stdout is not None and sys.stdout.isatty()
        trainer = pl.Trainer(num_sanity_val_steps=0, logger=False, enable_progress_bar=use_progress_bar)
 
        # Predict the spindles
        predictions = trainer.predict(model, dataloader)  # 0/1 label for each data point of each segment (takes ~50 sec)
        predictions = [pred.detach().cpu().numpy() for pred in predictions]

        # Compute spindle indices list (list comprehension method, faster, less memory)
        spindle_indices_list = [spindle_vect_to_indices(pred.flatten()) for pred in predictions]  # indices of spindles within each segment
        
        if DEBUG:
            # Compute spindle counts (keeping empty elements as 0)
            spindle_counts = [spindle.shape[0] if spindle.size > 0 else 0 for spindle in spindle_indices_list]
            total_spindles = sum(spindle_counts)  # Total spindles across all signals
            print(f"Total number of spindles detected: {total_spindles}")

        # Add the event_name and the channel label to the events list
        event_lst = []
        for i, spindle_samples in enumerate(spindle_indices_list):
            for start_smp, stop_smp in spindle_samples:
                signal_start_smp = int(round(signals[i].start_time*EXPECTED_SAMPLING_RATE))
                spindle_start_time = (signal_start_smp+start_smp)/EXPECTED_SAMPLING_RATE
                spindle_dur_time = (stop_smp-start_smp)/EXPECTED_SAMPLING_RATE
                event_lst.append((event_group, event_name, spindle_start_time, \
                    spindle_dur_time, signals[i].channel))
        
        # Create a pandas dataframe of events (each row is an event) for the current pds
        events_df = manage_events.create_event_dataframe(event_lst)

        return {
            'events': events_df
        }


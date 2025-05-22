"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    REMsDetectionYasa
    This class detects Rapid Eye Movements (REMs) in sleep recordings using YASA.
"""
import matplotlib.pyplot as plt
import mne
import numpy as np
import os
import pandas as pd
import yasa

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class REMsDetectionYasa(SciNode):
    """
    REMsDetectionYasa detects Rapid Eye Movements (REMs) in EEG/EOG sleep recordings.

    Parameters
    ----------
        signals: list
            List of raw signal objects containing EEG/EOG data.
        events: DataFrame
            DataFrame containing event-related information.
        sleepstages: DataFrame
            Sleep stage classification for each epoch.
        filename: str
            Name of the file being processed.
        amplitude: float
            Minimum amplitude threshold for REM detection.
        duration: float
            Minimum duration threshold for REM events.
        freq_rem: tuple
            Frequency range for REM detection (e.g., (0.5, 4 Hz)).
        relative_prominence: float
            Relative prominence threshold for REM detection.
        remove_outliers: bool
            Whether to remove statistical outliers in detection.
        rems_event_name: str
            Name assigned to detected REM events.
        rems_event_group: str
            Group name for REM events.
        include: int or list
            Sleep stage(s) to include in REM detection.
    
    Returns
    -------
        detectiondataframe: DataFrame
            A DataFrame containing detected REM events.

    Raises
    ------
        NodeInputException
            If input parameters have invalid types or missing keys.
        NodeRuntimeException
            If an error occurs during execution.
    """
    def __init__(self, **kwargs):
        """Initialize the REMsDetectionYasa module."""
        super().__init__(**kwargs)
        if DEBUG: print('REMsDetectionYasa.__init__')

        # Input plugs
        InputPlug('signals', self)
        InputPlug('events', self)
        InputPlug('sleepstages', self)
        InputPlug('filename', self)
        InputPlug('amplitude', self)
        InputPlug('duration', self)
        InputPlug('freq_rem', self)
        InputPlug('relative_prominence', self)
        InputPlug('remove_outliers', self)
        InputPlug('rems_event_name', self)
        InputPlug('rems_event_group', self)
        InputPlug('include', self)
        
        # Output plugs
        OutputPlug('detectiondataframe', self)

        # Define master module behavior
        self._is_master = False 
    
    def compute(self, filename, signals, events, sleepstages, amplitude, duration, freq_rem, 
                relative_prominence, remove_outliers, rems_event_name, rems_event_group, include):     
        """
        Perform REM detection using YASA.

        Returns
        -------
            detectiondataframe: DataFrame
                A DataFrame containing detected REM events.
        
        Raises
        ------
            NodeInputException
                If input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during execution.
        """
        filename = filename[:-4]  # Remove file extension
        error_flag = False

        # Validate inputs
        if not isinstance(signals, list) or len(signals) < 2:
            raise NodeInputException(self.identifier, "Invalid 'signals' input. Must be a list containing at least two elements.")
        if not isinstance(sleepstages, pd.DataFrame):
            raise NodeInputException(self.identifier, "Invalid 'sleepstages' input. Must be a DataFrame.")

        try:
            # Extract sleep stage information
            hypno = np.squeeze(sleepstages["name"].values).tolist()
            raw = self.prepare_raw_data(signals)
            hypno_up = yasa.hypno_upsample_to_data(hypno, sf_hypno=1/30, 
                                                    data=raw._data[0, :], 
                                                    sf_data=raw.info['sfreq'])
            # Extract EOG signals
            loc = raw._data[0, :] * 1e6  # Convert from V to µV
            roc = raw._data[1, :] * 1e6

            # Process inclusion list
            include = self.extract_ints(include)
            include = include[0] if len(include) == 1 else include
            
            # Check if the user provided the sleep stages or not
            if set(list(sleepstages['name'].unique())) == {'9'}:
                hypno_up = None
                include = None
                
            # Detect REMs
            rem = yasa.rem_detect(loc, roc, raw.info['sfreq'], 
                                  hypno=hypno_up, include=include, 
                                  amplitude=amplitude, duration=duration, 
                                  freq_rem=freq_rem, relative_prominence=relative_prominence, 
                                  remove_outliers=remove_outliers, verbose='info')

            # Save results
            rems_detection_df = rem.summary().round(3)
            rems_detection_df.to_csv(f"{filename}_YASA_REMs_summary.tsv", sep='\t')

            # Convert results to Snooz format
            snooz_rem = pd.DataFrame({
                'group': rems_event_group,
                'name': rems_event_name,
                'start_sec': rems_detection_df['Start'],
                'duration_sec': rems_detection_df['Duration'],
                'channels': [f"{raw.ch_names[0]}, {raw.ch_names[1]}" for _ in range(len(rems_detection_df))]
            })
            snooz_rem.to_csv(f"{filename}_YASA_REMs_snooz.tsv", sep='\t', index=False)
        
        except Exception as e:
            raise NodeRuntimeException(f"Error during REM detection: {str(e)}")

        self._log_manager.log(self.identifier, "This module detects Rapid Eye Movements.")

        return {'detectiondataframe': snooz_rem}
    
    def prepare_raw_data(self, raw):
        """Prepare raw data for processing."""
        ch_names = [raw[0].channel, raw[1].channel]
        ch_type = ['eog', 'eog']
        sfreq = raw[0].sample_rate
        data = np.array([r.samples * 1e-6 for r in raw])
        info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_type)
        return mne.io.RawArray(data, info)
    
    def extract_ints(self, s):
        """Extract integer values from a comma-separated string."""
        return [int(word) for word in s.replace(' ', '').split(',') if word.lstrip('-').isdigit()]

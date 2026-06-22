"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    REMsDetectionYasa
    This class detects Rapid Eye Movements (REMs) in sleep recordings using YASA.
"""
import matplotlib
import mne
import numpy as np
import os
import pandas as pd
import yasa
import sys
import warnings
import logging
matplotlib.use('Agg') # Use non-interactive Agg backend for matplotlib

# Suppress warnings from YASA and MNE
logging.getLogger('yasa').setLevel(logging.ERROR)
logging.getLogger('mne').setLevel(logging.ERROR)
logging.basicConfig(level=logging.WARNING)
# Suppress all warnings
warnings.filterwarnings("ignore")
mne.set_log_level('WARNING')

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
        events_details: DataFrame
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
        OutputPlug('events', self)
        OutputPlug('events_details', self)

        # Define master module behavior
        self._is_master = False 
    
    def compute(self, filename, signals, events, sleepstages, amplitude, duration, freq_rem, 
                relative_prominence, remove_outliers, rems_event_name, rems_event_group, include):     
        """
        Perform REM detection using YASA.

        Returns
        -------
            events_details: DataFrame
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
        
        use_progress_bar = sys.stdout is not None and sys.stdout.isatty() ### added to check
        sections_start_times = np.unique([signal.start_time for signal in signals])  # Get unique start times of signals
        try:
            rems_events = []  # Initialize a list to hold detected REM events across all sections
            NoneSections = 0 # Counter for sections where no REMs were detected
            for section in range(len(sections_start_times)):
                section_signal = []  # Initialize a list to hold signals for the current section
                for signal in signals:
                    if signal.start_time == sections_start_times[section]:  # Check if the signal corresponds to the current section
                        section_signal.append(signal)  # Append the signal to the section-specific list
                raw = self.prepare_raw_data(section_signal)
                end_time = section_signal[-1].end_time
                # Extract sleep stage information
                if len(sections_start_times) > 1:
                    sleepstages_sig = sleepstages[(sleepstages['start_sec'].astype(int) < int(end_time)) & (sleepstages['start_sec'].astype(int) >= int(sections_start_times[section]))]
                else:
                    sleepstages_sig = sleepstages
                hypno = np.squeeze(sleepstages_sig["name"].values) if not sleepstages_sig.empty else np.array([])
                hypno_up = yasa.hypno_upsample_to_data(hypno, sf_hypno=1/30, 
                                                        data=raw._data[0, :], 
                                                        sf_data=np.round(raw.info['sfreq']))
                # Extract EOG signals
                loc = raw._data[0, :] * 1e6  # Convert from V to µV
                roc = raw._data[1, :] * 1e6

                # Process inclusion list
                if include is not None:
                    if isinstance(include, str) and include.strip() != "":
                        include = self.extract_ints(include)
                    elif isinstance(include, int):
                        include = [include]
                    else:
                        include = include if isinstance(include, list) else []
                else:
                    include = []
            
                # Check if the user provided the sleep stages or not
                if set(list(sleepstages['name'].unique())) == {'9'}:
                    hypno_up = None
                    include = None
                if all(str(val) in set(str(h) for h in np.unique(hypno)) for val in include):
                    # Detect REMs
                    rem = yasa.rem_detect(loc, roc, raw.info['sfreq'], 
                                        hypno=hypno_up, include=include, 
                                        amplitude=amplitude, duration=duration, 
                                        freq_rem=freq_rem, relative_prominence=relative_prominence, 
                                        remove_outliers=remove_outliers, verbose= False)
                    if rem is not None and rem._events is not None and len(rem._events) > 0:
                        rem_dataframe = rem.summary().round(3)  # Get summary of detected REM events for the current section
                        # Adjust REM event times to be relative to the recording start
                        rem_dataframe['Start'] = rem_dataframe['Start'] + sections_start_times[section]  # Adjust start times to be relative to the recording start
                        rem_dataframe['End'] = rem_dataframe['End'] + sections_start_times[section]  # Adjust end times to be relative to the recording start
                        rem_dataframe['Peak'] = rem_dataframe['Peak'] + sections_start_times[section]  # Adjust peak times to be relative to the recording start                    
                        # Filter REMs: keep only events where start + 1/3 duration falls in sleep stage 5
                        valid_indices = []
                        for idx, row in rem_dataframe.iterrows():
                            check_time1 = row['Start'] + (row['Duration'] / 3)
                            check_time2 = row['End'] - (row['Duration'] / 3)
                            previous_stage_at_time = sleepstages_sig[(sleepstages_sig['start_sec'] <= check_time1) & 
                                                            (sleepstages_sig['start_sec'] + 30 > check_time1)]
                            next_stage_at_time = sleepstages_sig[(sleepstages_sig['start_sec'] <= check_time2) & 
                                                            (sleepstages_sig['start_sec'] + 30 > check_time2)]
                            if not previous_stage_at_time.empty and not next_stage_at_time.empty and (str(previous_stage_at_time.iloc[0]['name']) == '5' or str(next_stage_at_time.iloc[0]['name']) == '5'):
                                    valid_indices.append(idx)
                                    if row['Stage'] != 5:
                                        rem_dataframe.loc[idx, 'Stage'] = 5
                        
                        if len(valid_indices) > 0:
                            rem_dataframe = rem_dataframe.loc[valid_indices].reset_index(drop=True)
                            rems_events.append(rem_dataframe)  # Append detected REM events for the current section to the list
                        else:
                            NoneSections += 1
                    else:
                        NoneSections += 1
                        continue  # Skip to the next section if no REMs were detected
            
            if NoneSections == len(sections_start_times):
                raise NodeRuntimeException(self.identifier, "REMs detection", f"No REMs were found in data. Returning None.")
            # Save results
            if len(rems_events) > 1:
                rems_detection_df = pd.concat(rems_events, ignore_index=True)
            else:
                rems_detection_df = rems_events[0] if len(rems_events) == 1 else pd.DataFrame()

            if len(filename)>0:
                subject_id = os.path.basename(filename)
                # Extract folder of the file
                folder_cohort = os.path.dirname(filename)
                # Make directory specific for rems characteristics
                folder_rems_char = os.path.join(folder_cohort, 'rems_characteristics')
                if not os.path.isdir(folder_rems_char):
                    os.makedirs(folder_rems_char)
                rems_char_filename = os.path.join(folder_rems_char,subject_id)
                rems_detection_df.to_csv(f"{rems_char_filename}_YASA_REMs_summary.tsv", sep='\t')

            # Convert results to Snooz format
            snooz_rem = pd.DataFrame({
                'group': rems_event_group,
                'name': rems_event_name,
                'start_sec': rems_detection_df['Start'],
                'duration_sec': rems_detection_df['Duration'],
                'channels': [f"{raw.ch_names[0]}" for _ in range(len(rems_detection_df))]
            })
            #snooz_rem.to_csv(f"{filename}_YASA_REMs_snooz.tsv", sep='\t', index=False) # We can save this if we needed it later on. Now something similar is exported.
            # Add group, name and channels to the rems_detection_df as well.
            rems_detection_df['group'] = rems_event_group
            rems_detection_df['name'] = rems_event_name
            rems_detection_df['start_sec'] = snooz_rem['start_sec']
            rems_detection_df['duration_sec'] = snooz_rem['duration_sec']
            rems_detection_df['channels'] = [f"{raw.ch_names[0]}, {raw.ch_names[1]}" for _ in range(len(rems_detection_df))]
        except Exception as e:
            raise NodeRuntimeException(self.identifier, "REMs detection", f"Error during REM detection: {str(e)}")

        self._log_manager.log(self.identifier, "This module detects Rapid Eye Movements.")

        return {'events_details': rems_detection_df, 'events': snooz_rem}
    
    def prepare_raw_data(self, raw):
        """Prepare raw data for processing."""
        ch_names = [raw[0].channel, raw[1].channel]
        ch_type = ['eog', 'eog']
        sfreq = raw[0].sample_rate
        data = np.array([r.samples * 1e-6 for r in raw])  # Convert from V to µV
        info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_type)
        return mne.io.RawArray(data, info)
    
    def extract_ints(self, s):
        """Extract integer values from a comma-separated string."""
        return [int(word) for word in s.replace(' ', '').split(',') if word.lstrip('-').isdigit()]

"""
@ Valorisation Recherche HSCM, Société en Commandite – 2025
See the file LICENCE for full license details.

    YasaSleepStaging
    A module that performs automatic sleep stage scoring using YASA (Yet Another Spindle Algorithm).
    This node processes EEG, EOG, and EMG signals to predict sleep stages according to standard AASM guidelines.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import os
import mne
import yasa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import resample
from sklearn.metrics import classification_report, confusion_matrix, cohen_kappa_score

DEBUG = False

class YasaSleepStaging(SciNode):
    """
    Automatic sleep stage classification using YASA's machine learning model.
    Handles both validation (against expert scores) and prediction modes.

    Parameters
    ----------
        filename: str
            Path to the input data file
        signals_EEG: list
            List of EEG signal objects (required)
        signals_EOG: list
            List of EOG signal objects (optional)
        signals_EMG: list
            List of EMG signal objects (optional)
        sleep_stages: pd.DataFrame
            Expert-scored sleep stages (required in validation mode)
        stage_group: str
            group to add the predicted stages
        validation_on: bool
            Flag indicating validation mode (True) or prediction mode (False)

    Returns
    -------
        results: pd.DataFrame
            Classification metrics (accuracy, kappa, confidence, F1 scores)
        info: list
            Contains [ground_truth_hypnogram, predicted_hypnogram, filename]
        new_events: pd.DataFrame
            Updated events with predicted sleep stages
        events_to_remove :  list of tuple of n events to remove.
            [('group1', 'name1'), ('group2', 'name2')]
    """
    def __init__(self, **kwargs):
        """ Initialize module YasaSleepStaging """
        super().__init__(**kwargs)
        if DEBUG: print('YasaSleepStaging.__init__')

        # Input plugs
        InputPlug('filename', self)          # Input file path
        InputPlug('signals_EEG', self)       # EEG signals (required)
        InputPlug('signals_EOG', self)       # EOG signals (optional)
        InputPlug('signals_EMG', self)       # EMG signals (optional)
        InputPlug('sleep_stages', self)      # Expert-scored stages (validation)
        InputPlug('stage_group', self)            # Sleep events annotation
        InputPlug('validation_on', self)          # Validation mode flag

        # Output plugs
        OutputPlug('results', self)          # Classification metrics
        OutputPlug('info', self)             # Hypnogram comparison data
        OutputPlug('new_events', self)       # Updated events with predictions
        OutputPlug('events_to_remove', self) # Events to remove in order to totally replace the previous sleep stages

        # Processing state flags
        self.is_done = False                 # Completion status
        self._is_master = False              # Master module flag
    
    def compute(self, filename, signals_EEG, signals_EOG, signals_EMG , sleep_stages, stage_group, validation_on):
        """
        Main processing method that performs sleep stage classification.

        Parameters
        ----------
            filename: str
                Path to the input data file
            signals_EEG: list
                EEG signal objects
            signals_EOG: list
                EOG signal objects
            signals_EMG: list
                EMG signal objects
            sleep_stages: pd.DataFrame
                Expert-scored stages (validation mode)
            stage_group: pd.DataFrame
                Sleep events annotation
            validation_on: bool
                Validation mode flag

        Returns
        -------
            results: pd.DataFrame
                Classification metrics (accuracy, kappa, confidence, F1 scores)
            info: list
                Contains [ground_truth_hypnogram, predicted_hypnogram, filename]
            new_events: pd.DataFrame
                Updated events with predicted sleep stages

        Raises
        ------
            NodeInputException
                If required inputs are missing or invalid
            NodeRuntimeException
                If processing fails at any stage
        """
        # split the ext from the filename
        filename_no_path, file_ext = os.path.splitext(filename)
        # Snooz can write the sleep staging only for the .edf format 
        if file_ext.lower() == '.edf':
            # Events to remove, provided to the PSGWriter, in order to replace the previous sleep stages.
            # It is important to remove previous stages with the exact same group label 
            # if they do not match the current unique list of sleep stages exactly.
            # PSGWriter replaces event with the same group and name (but here a name can be missing and then not replaced).
            events_to_remove = \
                [(stage_group, '9'), \
                (stage_group, '0'),
                (stage_group, '1'),
                (stage_group, '2'),
                (stage_group, '3'),
                (stage_group, '5')]
        else:
            events_to_remove = []

        # Split the data into EEG, EOG, and EMG signals
        signals = self.SplitData(signals_EEG, signals_EOG, signals_EMG)
        y_pred_list = []
        confidence_list = []
        for signal in signals:
            # Prepare raw data for sleep staging
            signal = self.prepare_raw_data(signal)
            # Apply sleep staging
            sls = self.apply_sleep_staging(signal)
            # Check the features
            #features = sls.get_features()
            # Predict sleep stages
            y_pred = sls.predict()
            y_pred_list.append(y_pred)
            # Get the probability of each stage
            proba = sls.predict_proba()        
            # Get the confidence
            confidence = proba.max(axis=1)
            confidence_list.append(confidence)
        # Perform majority vote for each element across all lists in y_pred_list
        y_pred_majority_vote = []
        Decided_Confidence = []
        for i in range(len(y_pred_list[0])):
            max_confidence_index = np.argmax([confidence[i] for confidence in confidence_list])
            Decided_Confidence.append(confidence_list[max_confidence_index][i])
            y_pred_majority_vote.append(y_pred_list[max_confidence_index][i])
        '''for i in range(len(y_pred_list[0])):
            votes = [y_pred[i] for y_pred in y_pred_list]
            majority_vote = max(set(votes), key=votes.count)
            y_pred_majority_vote.append(majority_vote)'''
        Avg_Confidence = 100 * np.mean(Decided_Confidence)
        y_pred = y_pred_majority_vote
        y_pred = yasa.Hypnogram(y_pred, freq="30s")

        # Convert prediction to Snooz format
        y_pred_YASA_lst = list(y_pred.hypno)
        stage_mapping_to_snooz = {
        'WAKE': '0',
        'N1': '1',
        'N2': '2',
        'N3': '3',
        'REM': '5',
        'UNS': '9'
        }
        y_pred_snooz = [stage_mapping_to_snooz.get(stage, '9') for stage in y_pred_YASA_lst]
        
        # If validation_on is True, we are in validation mode, else we are in prediction mode
        if validation_on:
            # Convert snooz sleep stages into YASA labels
            stage_mapping_to_YASA = {
                '0': 'WAKE',
                '1': 'N1',
                '2': 'N2',
                '3': 'N3',
                '4': 'N3',
                '5': 'REM',
                '9': 'UNS'
            }
            labels_snooz_val = sleep_stages['name'].values
            labels_yasa = [stage_mapping_to_YASA.get(stage, 'UNS') for stage in labels_snooz_val]
            # TODO : what is the difference between labels_yasa and labels_lst
            labels_hyp = yasa.Hypnogram(labels_yasa, freq="30s")
            labels_lst = list(labels_hyp.hypno)

            # Filter out "UNS" stages to evaluate the performance on scored data only
            labels_no_uns, y_pred_no_uns = self.filter_uns(labels_lst, y_pred_YASA_lst)

            # Calculate Accuracy
            Accuracy = 100 * (pd.Series(labels_no_uns) == pd.Series(y_pred_no_uns)).mean()
            # Calculate Cohen's Kappa
            kappa = cohen_kappa_score(labels_no_uns, y_pred_no_uns)
            report_dict = classification_report(labels_no_uns, y_pred_no_uns, output_dict=True)

            # Calculate F1 scores for each stage
            F1_scores = {stage: report_dict[stage]['f1-score']*100 if stage in report_dict else None for stage in ['WAKE', 'N1', 'N2', 'N3', 'REM']}

            # Convert lists back to Hypnogram objects
            labels_no_uns_hyp = yasa.Hypnogram(labels_no_uns, freq="30s")
            y_pred_no_uns_hyp = yasa.Hypnogram(y_pred_no_uns, freq="30s")

            # Cache the results
            file_name = filename[:-4] # Extract the file name from the path
            self.cache_signal(labels_no_uns_hyp, y_pred_no_uns_hyp, Accuracy, sls, Avg_Confidence, file_name, kappa)

            # Log the results
            self._log_manager.log(self.identifier, "Hypnogram computed.")
            self._log_manager.log(self.identifier, f"The overall agreement is {Accuracy:.2f}%")
            filenamewe = os.path.basename(file_name)
            name_without_extension = os.path.splitext(filenamewe)[0]
            # Create a DataFrame for the classification report
            df_Classification_report = pd.DataFrame({'Subject Name': [name_without_extension], \
                                                     'Accuracy': [Accuracy], 'kappa':[kappa],\
                                                     'Average Confidence':[Avg_Confidence], \
                                                    **{f'F1-{stage}': [F1_scores[stage]] for stage in F1_scores}})
        else:
            df_Classification_report = pd.DataFrame()
            labels_no_uns_hyp = None
            y_pred_no_uns_hyp = None
            file_name = None

        # Replace the group and name of the sleep_stages for the predicted ones
        if len(y_pred_snooz) == len(sleep_stages):
            sleep_stages['group'] = stage_group
            sleep_stages['name'] = y_pred_snooz
        elif len(y_pred_snooz) == len(sleep_stages) + 1:
            # If the length of y_pred_snooz is one more than sleep_stages, remove the last element
            sleep_stages['group'] = stage_group
            sleep_stages['name'] = y_pred_snooz[:-1]
        elif len(y_pred_snooz) == len(sleep_stages) - 1:
            # If the length of y_pred_snooz is one less than sleep_stages, add a 'UNS' stage
            sleep_stages['group'] = stage_group
            sleep_stages['name'] = y_pred_snooz + [stage_mapping_to_snooz['UNS']]
        else:
            raise NodeRuntimeException(self.identifier, "sleep_stages", \
                    f"The number of predicted sleep stages {len(y_pred_snooz)} does not match the number of expected epochs {len(sleep_stages)}.")
        
        # Snooz can write the sleep staging only for the .edf format 
        if file_ext.lower() != '.edf':
            sleep_stages = pd.DataFrame(data=None, columns=sleep_stages.columns)

        return {
            'results': df_Classification_report,
            'info': [labels_no_uns_hyp, y_pred_no_uns_hyp, file_name],
            'new_events': sleep_stages,
            'events_to_remove' : events_to_remove
        }

    def SplitData(self, raw_EEG, raw_EOG, raw_EMG):
        """
        Split the data into EEG, EOG, and EMG signals based on available inputs.
        EEG is mandatory, while EOG and EMG are optional.

        Parameters
        ----------
        raw_EEG : list
            List of EEG signal objects (mandatory)
        raw_EOG : list or None
            List of EOG signal objects (optional)
        raw_EMG : list or None
            List of EMG signal objects (optional)

        Returns
        -------
        list
            List of signal combinations for each EEG signal. Each combination will include
            available EOG and EMG signals.

        Raises
        ------
        NodeInputException
            If raw_EEG is empty or None
        """
        # Validate that EEG is present (mandatory)
        if not raw_EEG:
            raise NodeInputException(self.identifier, "raw_EEG", "EEG signal is mandatory but was not provided")

        rawlist = []
        
        # Get optional EOG and EMG signals if available
        eog = next(iter(raw_EOG), None) if raw_EOG else None
        emg = next(iter(raw_EMG), None) if raw_EMG else None
        
        # Create combinations based on available signals
        for eeg in raw_EEG:
            if eog and emg:  # All signals available
                rawlist.append([eeg, eog, emg])
            elif eog:  # Only EEG and EOG
                rawlist.append([eeg, eog])
            elif emg:  # Only EEG and EMG
                rawlist.append([eeg, emg])
            else:  # Only EEG
                rawlist.append([eeg])
        
        return rawlist
        '''eog = next(s for s in raw_EOG)
        emg = next(s for s in raw_EMG)
        rawlist = [[i, eog, emg] for i in raw_EEG]'''

    def prepare_raw_data(self, raw):
        """
        Prepare raw data for sleep staging.

        Parameters
        ----------
        raw: list
            List of raw signal objects.

        Returns
        -------
        RawArray
            Prepared raw data.
        """
        # Check the number of channels as input
        if len(raw) == 3:
            raw = self.sort_and_resample(raw, ['EEG', 'EOG', 'EMG'])
            ch_names = [raw[0].channel, raw[1].channel, raw[2].channel]
            ch_type = ['eeg', 'eog', 'emg']
        elif len(raw) == 2:
            raw = self.sort_and_resample(raw, ['EEG', 'EOG', 'EMG'])
            ch_names = [raw[0].channel, raw[1].channel]
            ch_type = ['eeg', 'emg' if 'EMG' in raw[1].channel else 'eog']
        elif len(raw) == 1:
            ch_names = [raw[0].channel]
            ch_type = ['eeg']
        else:
            raise NodeInputException(self.identifier, "raw", "The number of channels is not supported.")

        # Create MNE RawArray object
        sfreq = raw[0].sample_rate
        data = np.array([r.samples*1e-6 for r in raw])
        
        info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_type)
        return mne.io.RawArray(data, info)

    def sort_and_resample(self, raw, channel_order):
        """
        Sort and resample raw data.

        Parameters
        ----------
        raw: list
            List of raw signal objects.
        channel_order: list
            List of channel types in order.

        Returns
        -------
        list
            Sorted and resampled raw data.
        """
        # Order the channels from EEG, EOG, EMG
        channel_order = {ch: i for i, ch in enumerate(channel_order)}
        raw = sorted(raw, key=lambda x: channel_order.get(x.alias.upper(), len(channel_order)))
        # Resample the signals if the sampling frequency is different
        sfreq = raw[0].sample_rate
        for r in raw[1:]:
            if r.sample_rate != sfreq:
                num_samples = int(len(r.samples) * sfreq / r.sample_rate)
                r.samples = resample(r.samples, num_samples)
                r.sample_rate = sfreq
        return raw

    def apply_sleep_staging(self, raw):
        """
        Apply sleep staging using Yasa.

        Parameters
        ----------
        raw: RawArray
            Prepared raw data.

        Returns
        -------
        SleepStaging
            Yasa SleepStaging object.
        """
        ch_names = raw.ch_names
        ch_types = raw.get_channel_types()
        if len(ch_names) == 3:
            return yasa.SleepStaging(raw, eeg_name=ch_names[0], eog_name=ch_names[1], emg_name=ch_names[2])
        else:
            return yasa.SleepStaging(raw, eeg_name=ch_names[0], eog_name=ch_names[1] if 'eog' in ch_types else None, emg_name=ch_names[1] if 'emg' in ch_types else None)

    def cache_signal(self, labels_new, y_pred_new, Accuracy, sls, Avg_Confidence, file_name, kappa):
        """
        Cache the hypnogram.

        Parameters
        ----------
        labels_new : Hypnogram
            The new labels hypnogram.
        y_pred_new : Hypnogram
            The predicted labels hypnogram.
        Accuracy : float
            The Accuracy of the prediction.
        sls : SleepStaging
            The Yasa SleepStaging object.
        first_wake : int
            Index of the first wake.
        last_wake : int
            Index of the last wake.
        """
        cache = {
            'labels_new': labels_new,
            'y_pred_new': y_pred_new,
            'Accuracy': Accuracy,
            'sls': sls,
            'Avg_Confidence': Avg_Confidence,
            'file_name': file_name,
            'kappa': kappa
        }
        self._cache_manager.write_mem_cache(self.identifier, cache)

    def mask_list(self, lst, mask_value=None, first_wake=None, last_wake=None, flag=False):
        """
        Mask elements outside the range of first and last "WAKE".

        Parameters
        ----------
        lst : list
            List to be masked.
        mask_value : any
            Value to mask with.
        first_wake : int
            Index of the first wake.
        last_wake : int
            Index of the last wake.
        flag : bool
            Flag to indicate if first and last wake should be found.

        Returns
        -------
        tuple
            Masked list, first wake index, last wake index.
        """
        try:
            if flag:
                first_wake = lst.index("WAKE")
                last_wake = len(lst) - 1 - lst[::-1].index("WAKE")
            masked_list = [mask_value if i < first_wake or i > last_wake else lst[i] for i in range(len(lst))]
            return masked_list, first_wake, last_wake
        except ValueError:
            return [mask_value] * len(lst), None, None

    def filter_uns(self, labels, preds):
        """
        Filter out "UNS" labels and corresponding predictions.

        Parameters
        ----------
        labels : list
            List of labels.
        preds : list
            List of predictions.

        Returns
        -------
        tuple
            Filtered labels and predictions.
        """
        filtered_labels = []
        filtered_preds = []
        for label, pred in zip(labels, preds):
            if label != "UNS":
                filtered_labels.append(label)
                filtered_preds.append(pred)
        return filtered_labels, filtered_preds


    

    

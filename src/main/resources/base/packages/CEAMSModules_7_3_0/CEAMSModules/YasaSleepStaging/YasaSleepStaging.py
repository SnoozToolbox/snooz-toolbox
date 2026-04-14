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
from scipy.signal import resample
from sklearn.metrics import classification_report, confusion_matrix, cohen_kappa_score

# Conditionally import matplotlib based on headless mode
import config
if config.HEADLESS_MODE:
    # Use Agg backend in headless mode (no GUI required, perfect for PDF generation)
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib.figure import Figure
    import matplotlib.pyplot as plt
else:
    # Use QtAgg backend in GUI mode
    import matplotlib
    matplotlib.use('QtAgg')
    import matplotlib.pyplot as plt


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
        signals, number_of_parts = self.SplitData(signals_EEG, signals_EOG, signals_EMG)
        y_pred_list = []
        confidence_list = []
        proba_list = []
        Combination_names = []
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
            proba_list.append(proba)
            names = ", ".join(signal.ch_names[:])
            Combination_names.append(names)
            # Get the confidence
            confidence = proba.max(axis=1)
            confidence_list.append(confidence)
        # Perform majority vote for each element across all lists in y_pred_list
        # Merge the discontinuities to create a single prediction
        if number_of_parts is not None and number_of_parts > 1:
            y_pred_list, part_lengths = self.merge_by_parts(y_pred_list, number_of_parts)
            confidence_list, part_lengths  = self.merge_by_parts(confidence_list, number_of_parts)
            proba_list, part_lengths = self.merge_by_parts(proba_list, number_of_parts)
            sleep_stages.drop(index=np.cumsum(part_lengths)[:-1], inplace=True)
            sleep_stages.reset_index(drop=True, inplace=True)
            
        y_pred_majority_vote = []
        Decided_Confidence = []
        for i in range(len(y_pred_list[0])):
            max_confidence_index = np.argmax([confidence[i] for confidence in confidence_list])
            Decided_Confidence.append(confidence_list[max_confidence_index][i])
            y_pred_majority_vote.append(y_pred_list[max_confidence_index][i])
        
        # Add the maximum confidence to the proba_list to plot the hypnodensity for it later on
        Combination_names = list(dict.fromkeys(Combination_names))
        proba_list.append(proba_list[-1])
        Combination_names.append('Maximum Confidence')

        '''for i in range(len(y_pred_list[0])):
            votes = [y_pred[i] for y_pred in y_pred_list]
            majority_vote = max(set(votes), key=votes.count)
            y_pred_majority_vote.append(majority_vote)'''

        # Calculate average confidence
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
            file_name = os.path.splitext(filename)[0] # Extract the file name from the path
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
            file_name = os.path.splitext(filename)[0]

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
            'info': [labels_no_uns_hyp, y_pred_no_uns_hyp, file_name, proba_list, Decided_Confidence, Combination_names],
            'new_events': sleep_stages,
            'events_to_remove' : events_to_remove
        }

    def merge_by_parts(self, data_list, number_of_parts):
        """
        Merge elements that belong to the same relative index across parts.

        Works with both:
        • list of np.ndarray  – concatenated with np.concatenate(axis=0)
        • list of pd.DataFrame – concatenated with pd.concat(axis=0, ignore_index=True)

        Parameters
        ----------
        data_list : list[np.ndarray] | list[pd.DataFrame]
            Items to merge. The length must be divisible by `number_of_parts`.
        number_of_parts : int
            Into how many equal chunks the list is logically split.

        Returns
        -------
        merged : list[np.ndarray | pd.DataFrame]
            Merged objects, length = len(data_list) // number_of_parts.
        part_lengths : list[int]
            One length per part (non-repeated).
        """
        if not data_list:
            raise ValueError("Input list is empty.")
        
        n = len(data_list)
        if n % number_of_parts != 0:
            raise ValueError(f"List of length {n} is not divisible by {number_of_parts}.")

        # Determine merge strategy from the first element
        first = data_list[0]
        if isinstance(first, np.ndarray):
            concat = lambda grp: np.concatenate(grp, axis=0)
        elif isinstance(first, (pd.DataFrame, pd.Series)):
            concat = lambda grp: pd.concat(grp, axis=0, ignore_index=True)
        else:
            raise TypeError(
                "Unsupported element type. Expected np.ndarray or pd.DataFrame."
            )

        stride = n // number_of_parts
        merged = []

        # Merge arrays from each part per index
        merged = [
            concat([data_list[i + p * stride] for p in range(number_of_parts)])
            for i in range(stride)]

        # Get one length from the first item in each part
        part_lengths = [len(data_list[p * stride]) for p in range(number_of_parts)]

        return merged, part_lengths
    
    def SplitData(self, raw_EEG, raw_EOG, raw_EMG):
        """
        Split EEG signals into groups by part and combine with corresponding EOG and EMG signals,
        if available. If both EOG and EMG are missing, return EEGs as-is.

        Parameters
        ----------
        raw_EEG : list
            List of EEG signal objects (mandatory)
        raw_EOG : list or None
            List of EOG signal objects (optional, 1 per part)
        raw_EMG : list or None
            List of EMG signal objects (optional, 1 per part)

        Returns
        -------
        list
            Grouped [EEG (+EOG/EMG)] combinations, or EEG-only if no EOG/EMG present.

        Raises
        ------
        NodeInputException
            If raw_EEG is empty or not divisible by number of parts (if EOG/EMG exist)
        """
        if not raw_EEG:
            raise NodeInputException(self.identifier, "raw_EEG", "EEG signal is mandatory but was not provided")

        # If no EOG and EMG, return EEGs individually
        if not raw_EOG and not raw_EMG:
            return [[eeg] for eeg in raw_EEG], None

        # Infer number of parts from EOG or EMG
        num_parts = 0
        if raw_EOG:
            num_parts = len(raw_EOG)
        elif raw_EMG:
            num_parts = len(raw_EMG)
        else:
            raise NodeInputException(self.identifier, "parts", "Cannot determine number of parts without EOG or EMG")

        if len(raw_EEG) % num_parts != 0:
            raise NodeInputException(
                self.identifier, "raw_EEG",
                f"EEG signals ({len(raw_EEG)}) cannot be evenly divided into {num_parts} parts"
            )

        eegs_per_part = len(raw_EEG) // num_parts
        rawlist = []
        eeg_index = 0

        for i in range(num_parts):
            eog = raw_EOG[i] if raw_EOG else None
            emg = raw_EMG[i] if raw_EMG else None

            for _ in range(eegs_per_part):
                eeg = raw_EEG[eeg_index]
                eeg_index += 1

                combo = [eeg]
                if eog:
                    combo.append(eog)
                if emg:
                    combo.append(emg)
                rawlist.append(combo)

        return rawlist, num_parts

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

        # Check if all signals have the same number of samples
        sfreq = raw[0].sample_rate
        for i, rate in enumerate([r.sample_rate for r in raw]):
            if rate != sfreq:
                raise NodeInputException(self.identifier, "raw", f"All signals must have the same sampling frequency. Found {sfreq} and {rate}.")

        max_len = max(len(r.samples) for r in raw)
        padded_samples = [np.pad(sig.samples, (0, max_len - len(sig.samples)), mode='constant', constant_values=0.0) for sig in raw]
        for item in range(len(padded_samples)):
            raw[item].samples = padded_samples[item]
        # Create MNE RawArray object
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


    

    

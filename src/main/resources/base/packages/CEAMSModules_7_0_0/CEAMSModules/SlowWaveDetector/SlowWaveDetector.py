"""
© 2022 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""

"""
    This plugin detects slow wave events based on the Carrier method.
    The plugin allows for modification of the criterias to detect slow waves.
    In a future implementation, automatic modification of the criterias will be
    possible according to age and sex of subject.

    Parameters
    -----------
        signals    : a list of SignalModel
            signal.samples : the actual signal data as numpy list
            signal.sample_rate : sampling rate of the signal
            signal.channel : current channel label                 
        event_group : String, event group.
        event_name : String, event label.
        f_min   : float, minimal wave frequency
        f_max   : float, maximal wave frequency
        th_PaP  : float, peak-to-peak minimal amplitude
        th_Neg  : float, negative minimal amplitude
        min_tNe : int, minimal duration of negative part of the slow wave
        max_tNe : int, maximal duration of negative part of the slow wave
        min_tPo : int, minimal duration of positive part of the slow wave
        max_tPo : int, maximal duration of positive part of the slow wave
        age_criterion   : String, '1' or '0'
            '1' to modify criterias according to age
            '0' to keep criterias as they are
        years   : int, 0 to 122
        months  : int, 0 to 11
        sex_criterion   : String, '1' or '0'
            '1' to modify criterias according to sex
            '0' to keep criterias as they are
        sex : String, 'Female' or 'Male'
    
    Returns
    -----------  
        event_group : String, event group.
        events  : Pandas DataFrame
            DataFrame events (columns=['group','name','start_sec','duration_sec','channels']) 
            containing a slow wave event    
        events_details    : Pandas DataFrame
            DataFrame events (columns=['start_sec', 'duration_sec', 'n_t','pkpk_amp_uV','neg_amp_uV', 'neg_sec', 
                'pos_sec', 'Pap_raw', 'Neg_raw', 'mfr', 'trans_freq_Hz', 'slope_0_min', 'slope_min_max', 'slope_max_0', 'channels','name'])
            containing data of each detected slow wave for further analysis
        signals : list of SignalModel
            The original list of SignalModel was modified to fit a time window
            of 30 s for the epochs.   
        signals_modified : list of SignalModel
            The original list of SignalModel was modified to fit a time window
            of 30 s for the epochs.   
        signals_time    : Pandas DataFrame
            DataFrame events (columns=['start_time','end_time','channels','name'])
            containing information on the start_time, end_time and name of each signal.
            Used to retrieve which signal came from which file.

    @author: Cloé Dutil (cloe.dutil.1@ens.etsmtl.ca)

    Log : 
        2022-0X-XX : First release, Cloé Dutil
"""

from scipy import signal as sci
import numpy as np
import pandas as pd

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import config

from CEAMSModules.EventReader import manage_events
from CEAMSModules.PSGReader.SignalModel import SignalModel

DEBUG = False

class SlowWaveDetector(SciNode):
    """
    This plugin detects slow wave events based on multiple criterias such as 
    Carrier's, sex and / or age of subject.
    The plugin also keeps in memory the caracteristics of the slow wave, 
    including the transition frequency of the wave in order to eventually 
    classify the slow waves collected.
    To assure best results, the detector keeps only 30 s or + epochs. If epochs 
    aren't the same size, the detector reformats the signal and keeps only 30 s
    segments.

    Parameters
    -----------
        signals    : a list of SignalModel
            signal.samples : the actual signal data as numpy list
            signal.sample_rate : sampling rate of the signal
            signal.channel : current channel label                 
        event_group : String, event group.
        event_name : String, event label.
        f_min   : float, minimal wave frequency
        f_max   : float, maximal wave frequency
        th_PaP  : float, peak-to-peak minimal amplitude
        th_Neg  : float, negative minimal amplitude
        min_tNe : int, minimal duration of negative part of the slow wave
        max_tNe : int, maximal duration of negative part of the slow wave
        min_tPo : int, minimal duration of positive part of the slow wave
        max_tPo : int, maximal duration of positive part of the slow wave
        age_criterion   : String, '1' or '0'
            '1' to modify criterias according to age
            '0' to keep criterias as they are
        years   : int, 0 to 122
        months  : int, 0 to 11
        sex_criterion   : String, '1' or '0'
            '1' to modify criterias according to sex
            '0' to keep criterias as they are
        sex : String, 'Female' or 'Male'
    
    Returns
    -----------  

        events  : Pandas DataFrame
                DataFrame events (columns=['group','name','start_sec','duration_sec','channels']) 
                containing a slow wave event    
        events_details    : Pandas DataFrame
            DataFrame events (columns=['start_sec', 'duration_sec', 'n_t','pkpk_amp_uV','neg_amp_uV', 'neg_sec', 'pos_sec', 'Pap_raw', 'Neg_raw', 'mfr', 'trans_freq_Hz', 'slope_0_min', 'slope_min_max', 'slope_max_0', 'channels','name'])
            containing data of each detected slow wave for further analysis

    @author: Cloé Dutil (cloe.dutil.1@ens.etsmtl.ca)    
    """


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('SlowWaveDetector.__init__')
        InputPlug('signals', self)
        InputPlug('event_group', self)
        InputPlug('event_name', self)
        InputPlug('f_min', self)
        InputPlug('f_max', self)
        InputPlug('th_PaP', self)
        InputPlug('th_Neg', self)
        InputPlug('min_tNe', self)
        InputPlug('max_tNe', self)
        InputPlug('min_tPo', self)
        InputPlug('max_tPo', self)
        InputPlug('age_criterion', self)
        InputPlug('years', self)
        InputPlug('months', self)
        InputPlug('sex_criterion', self)
        InputPlug('sex', self)
        
        OutputPlug('events', self)
        OutputPlug('events_details', self)

        #self.order = 30


    def __del__(self):
        if DEBUG: print('SlowWaveDetector.__del__')


    def subscribe_topics(self):
        pass


    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'SlowWaveDetector.on_topic_update {topic}:{message}')


    def compute(self, signals, event_group, event_name, f_min, f_max, th_PaP,
        th_Neg, min_tNe, max_tNe, min_tPo, max_tPo, age_criterion, years,
        months, sex_criterion, sex):
        """
        This function detects events based on Carrier criterias:
            - minimal peak-to-peak amplitude
            - minimal negative amplitude
            - duration of negative part of slow wave
            - duration of positive par of slow wave
        The function also keeps in memory the caracteristics of the slow wave, 
        including the transition frequency of the wave in order to eventually 
        classify the slow waves collected.

        Parameters
        -----------
            signals    : a list of SignalModel
                signal.samples : the actual signal data as numpy list
                signal.sample_rate : sampling rate of the signal
                signal.channel : current channel label                 
            event_group : String, event group.
            event_name : String, event label.
            f_min   : float, minimal wave frequency
            f_max   : float, maximal wave frequency
            th_PaP  : float, peak-to-peak minimal amplitude
            th_Neg  : float, negative minimal amplitude
            min_tNe : int, minimal duration of negative part of the slow wave
            max_tNe : int, maximal duration of negative part of the slow wave
            min_tPo : int, minimal duration of positive part of the slow wave
            max_tPo : int, maximal duration of positive part of the slow wave
            age_criterion   : String, '1' or '0'
                '1' to modify criterias according to age
                '0' to keep criterias as they are
            years   : int, 0 to 122
            months  : int, 0 to 11
            sex_criterion   : String, '1' or '0'
                '1' to modify criterias according to sex
                '0' to keep criterias as they are
            sex : String, 'Female' or 'Male'
        
        Returns
        -----------  
            events  : Pandas DataFrame
                DataFrame events (columns=['group','name','start_sec','duration_sec','channels']) 
                containing a slow wave event    
            events_details    : Pandas DataFrame
                DataFrame events (columns=['group', 'name', 'start_sec', 'duration_sec', 'n_t','pkpk_amp_uV','neg_amp_uV', 'neg_sec', 'pos_sec', 'Pap_raw', 'Neg_raw', 'mfr', 'trans_freq_Hz', 'slope_0_min', 'slope_min_max', 'slope_max_0', 'channels'])
                containing data of each detected slow wave for further analysis


        @author: Cloé Dutil (cloe.dutil.1@ens.etsmtl.ca)
        """
        if DEBUG: print('SlowWaveDetector.compute {}'.format(event_name))

        self.clear_cache()

        if not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"SlowWaveDetector input of wrong type. Expected: <class 'list'> received: {type(signals)}")
        
        elif len(signals) == 0:
            raise NodeInputException(self.identifier, "signals", \
                f"SlowWaveDetector input empty.")

        elif len(signals[0].samples) == 0:
            raise NodeInputException(self.identifier, "signals", \
                f"No samples for first signal.")


        # Modify parameters based on sex (TODO: implement feature)
        if eval(sex_criterion):
            sex = sex
            pass

        # Modify parameters based on age (TODO: implement feature)
        if eval(age_criterion):
            years = int(years)
            months = int(months)
            pass

        self.WANTED_TIME_EPOCHS = 30
        self.reshaped_signals = self.reshape_data(signals)

        # Slow wave detection variables
        self.dataframe = []
        self.sww_data = []
        self.detections = 0
        self.skipped_epochs = 0
        self.signals_used = self.reshaped_signals.copy()

        self.detect_slow_waves(event_group, event_name, float(f_min), float(f_max), float(th_PaP), \
                                float(th_Neg), int(min_tNe), int(max_tNe), int(min_tPo), int(max_tPo))
        
        num_ssw_detected = f"Detected {self.detections} sleep slow waves (SSW) over {len(self.signals_used)} epochs of {self.signals_used[0].duration} seconds"
        self._log_manager.log(self.identifier, num_ssw_detected)

        # Create Dataframes
        self.dataframe = manage_events.create_event_dataframe(self.dataframe)
        self.sww_data = pd.DataFrame(self.sww_data, \
            columns=['group', 'name','start_sec', 'duration_sec', 'pkpk_amp_uV','neg_amp_uV', 'neg_sec', 'pos_sec', 'Pap_raw', 'Neg_raw', 'mfr', 'trans_freq_Hz', 'slope_0_min', 'slope_min_max', 'slope_max_0', 'channels'])

        # Reset index
        self.dataframe.reset_index(inplace=True, drop=True)
        # Sort events based on the start_sec
        self.dataframe.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')        

        n_chan = self.extract_number_channels(self.signals_used)

        # Save the information to show on the results View
        if config.is_dev:
            cache = {}
            cache['events'] = self.dataframe
            cache['events_details'] = self.sww_data
            cache['signals'] = signals
            cache['signals_modified'] = self.signals_used
            cache['n_chan'] = n_chan
            self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'events': self.dataframe,
            'events_details' : self.sww_data
        }


    def detect_slow_waves(self, event_group, event_name, f_min, f_max, th_PaP, \
                            th_Neg, min_tNe, max_tNe, min_tPo, max_tPo):
        """
        Detects and compiles slow waves according to input criterias.

        Parameters
        -----------
            event_group : String, event group.
            event_name : String, event label.
            f_min   : float, minimal wave frequency
            f_max   : float, maximal wave frequency
            th_PaP  : float, peak-to-peak minimal amplitude
            th_Neg  : float, negative minimal amplitude
            min_tNe : int, minimal duration of negative part of the slow wave
            max_tNe : int, maximal duration of negative part of the slow wave
            min_tPo : int, minimal duration of positive part of the slow wave
            max_tPo : int, maximal duration of positive part of the slow wave     
        """
        
        fmin_max = [f_min, f_max]

        for signal_model in self.reshaped_signals:
            fs = float(signal_model.sample_rate)

            # Extract the time series
            signal_data = signal_model.samples       

            # Skip ValueError for filtfilt because of small data
            if round(signal_model.duration) < self.WANTED_TIME_EPOCHS:
                del self.signals_used[self.reshaped_signals.index(signal_model) - self.skipped_epochs]
                self.skipped_epochs += 1
                continue                

            # Filter signal in the frequency range 0.16-4.0 Hz   
            order_filtfilt = int(30)/2
            sos = sci.butter(int(order_filtfilt), fmin_max, btype="bandpass", output='sos', fs=fs)
            signal_filtre = sci.sosfiltfilt(sos, signal_model.samples)

            # Find zero-crossings
            fa = signal_filtre[1:] # signal delayed by 1 sample
            fb = signal_filtre[:-1] # original signal
            f1 = [1 if (a * b) < 0 else 0 for a, b in zip(fa, fb)] # 1 when fa and fb have different signs
            f2 = [1 if (a > 0) else 0 for a in fb] # 1 when fb > 0
            # Indexes where the sw is passing the zero from positive to negative
            n_zc = np.nonzero([a * b for a, b in zip(f1, f2)])[0] # indexes where fa and fb have different signs and fb > 0

            # For each zero crossing from positive to negative
            for i in range(len(n_zc)-1):
                n_t = [n_zc[i], n_zc[i+1]]
                segment = signal_filtre[n_zc[i] + 1 : n_zc[i+1]]    # exclude sides
                    
                if len(segment) > 1:
                    segment_pos = np.where(segment > 0)[0]
                    segment_neg = np.where(segment < 0)[0]

                    pkpk_amp_uV = (abs(max(segment) - min(segment)))
                    seg_val = [abs(segment[i]) for i in segment_neg]
                    neg_amp_uV = max(seg_val)
                    neg_sec = (len(segment_neg) - 1) / fs 
                    pos_sec = (len(segment_pos) - 1) / fs

                    # Compute transition frequency
                    index_u = np.argmin(segment)
                    index_v = np.argmax(segment)
                    if (index_v - index_u) == 0:
                        trans_freq_Hz = 0
                        slope_min_max = 0
                    else:
                        trans_freq_Hz = fs / (index_v - index_u) / 2
                        slope_min_max = pkpk_amp_uV*fs/(index_v-index_u)
                    mfr = fs / (n_zc[i+1] - n_zc[i])
                    # Compute slope characteristics
                    if index_u == 0:
                        slope_0_min = 0
                    else:
                        slope_0_min = neg_amp_uV*fs/index_u
                    slope_max_0 = max(segment)*fs/(len(segment)-index_v)
                    # Raw data
                    segment_brut = signal_data[n_zc[i] + 1 : n_zc[i+1] - 1]
                    PaP_brut = abs(max(segment_brut) - min(segment_brut))
                    Neg_brut = min(segment_brut)

                    # Criterias to flag the segment as a slow wave
                    if (pkpk_amp_uV > th_PaP) and (neg_amp_uV > th_Neg) and ((neg_sec*1000) > min_tNe) \
                            and ((neg_sec*1000) < max_tNe) and ((pos_sec*1000) > min_tPo) and ((pos_sec*1000) < max_tPo):
                        self.detections += 1 
                        start_sec = float(n_t[0] / fs + signal_model.start_time)
                        duration_sec = float((n_t[1] - n_t[0]) / fs)
                        self.dataframe.append([event_group, event_name, start_sec, duration_sec, signal_model.channel])
                        data = [event_group, event_name, start_sec, duration_sec, pkpk_amp_uV, -neg_amp_uV, neg_sec, pos_sec, PaP_brut, Neg_brut, mfr, trans_freq_Hz, \
                            slope_0_min, slope_min_max, slope_max_0, signal_model.channel]
                        self.sww_data.append(data)


    def reshape_data(self, signals):
        """
        Reshapes a signal according to a wanted time for epochs.
        The strategy is divided in two parts:
        1- if the signal doesn't have same length epocs
            signals is divided into parts according to the wanted time for epochs.
            Parts smaller than the wanted time are kept.
        2- if the signal has same length epocs AND is smaller than the wanted time
        for epochs
            signals is divided into parts according to a ratio factor to fit the
            wanted time for epochs. Parts smaller than the wanted time are kept.
        
        Parameters
        -----------
            signals : list of SignalModel
                signal.samples : the actual signal data as numpy list
                signal.sample_rate : sampling rate of the signal
                signal.channel : current channel label 
        
        Returns
        -----------
            wanted_signals : list of SignalModel
                The original list of SignalModel was modified to fit a time window
                of 30 s for the epochs.   
        """
        
        wanted_signals = []
        data = signals[0].samples
        equal_size = all(len(signal.samples) == len(data) for signal in signals) # TODO : test with non integer fs and merge

        # If segments are not of same size
        if not equal_size:
            i = 0
            for signal_model in signals:
                
                if signal_model.duration <= self.WANTED_TIME_EPOCHS:
                    self. add_signal_data(i, wanted_signals, signal_model.samples, \
                        signal_model.sample_rate, signal_model.start_time, signal_model.duration, \
                        signal_model.end_time, signal_model.channel)
                    i += 1

                elif signal_model.duration > self.WANTED_TIME_EPOCHS:
                    INDEX_SEGMENT = int(self.WANTED_TIME_EPOCHS * signal_model.sample_rate)
                    signal_start_time = 0
                    for index in range(0, len(signal_model.samples), INDEX_SEGMENT):
                        samples = signal_model.samples[index: index + INDEX_SEGMENT]
                        duration = len(samples) / signal_model.sample_rate
                        self.add_signal_data( i,wanted_signals, samples, \
                            signal_model.sample_rate, signal_model.start_time + signal_start_time, duration, \
                            signal_model.start_time + signal_start_time + duration, \
                            signal_model.channel)
                        signal_start_time += duration
                        i += 1
        
        # If each segment has the same length
        else:
            current_time_segment = len(data) / signals[0].sample_rate
            # Find number of segments to merge for 30 s epochs
            n_segments_to_merge = round(self.WANTED_TIME_EPOCHS / current_time_segment)    
            n_segments = 0
            signal_data_to_analyse = []
                        
            # Modify time epochs if not already 30 s epochs
            if current_time_segment < self.WANTED_TIME_EPOCHS:
                wanted_signal_data = []
                i = 0
                for signal_model in enumerate(signals):
                    signal_data_to_analyse.extend(signal_model.samples)
                    n_segments += 1
                    if n_segments == n_segments_to_merge:
                        wanted_signal_data.append(signal_data_to_analyse)
                        start = signal_model.end_time - self.WANTED_TIME_EPOCHS
                        self.add_signal_data(i, wanted_signals, wanted_signal_data[i], \
                            signal_model.sample_rate, start, self.WANTED_TIME_EPOCHS, \
                            signal_model.end_time, signal_model.channel)
                        signal_data_to_analyse = []
                        n_segments = 0
                        i += 1
                
                # Add last bit of data
                if len(signal_data_to_analyse) > 0:
                    wanted_signal_data.append(signal_data_to_analyse)
                    start = signal_model.end_time - self.WANTED_TIME_EPOCHS
                    self.add_signal_data(i, wanted_signals, wanted_signal_data[i], \
                        signal_model.sample_rate, start, self.WANTED_TIME_EPOCHS, \
                        signal_model.end_time, signal_model.channel)

            else:
                wanted_signals = signals.copy()

        return wanted_signals


    def add_signal_data(self, i, signal_list, signal_data, sample_rate, start, duration, end, channel):
        """
        Add signal to a list of SignalModel.

        Parameters
        -----------
            i   : int, index for signal_list
            signal_list : list of SignalModel
                signal.samples : the actual signal data as numpy list
                signal.sample_rate : sampling rate of the signal
                signal.channel : current channel label
            signal_data : list of float containing each point to form the signal
            sample_rate : int, rate of the signal
            start   : float, start time of signal
            duration    : float, total duration of signal
            end : float, end time of signal
            channel : String, channel of signal
        """

        signal_list.append(SignalModel())
        signal_list[i].samples = signal_data
        signal_list[i].sample_rate = sample_rate
        signal_list[i].start_time = start
        signal_list[i].duration = duration
        signal_list[i].end_time = end
        signal_list[i].channel = channel


    def extract_number_channels(self, signals):
        """
        Extracts the number of channels parsed in the list of signals

        Parameters
        -----------
            signals : list of SignalModel
                signal.samples : the actual signal data as numpy list
                signal.sample_rate : sampling rate of the signal
                signal.channel : current channel label
        
        Returns
        -----------
            an int representing the number of channels parsed
        """
        channel_lst = [signal.channel for signal in signals]
        return len(np.unique(np.array(channel_lst)))

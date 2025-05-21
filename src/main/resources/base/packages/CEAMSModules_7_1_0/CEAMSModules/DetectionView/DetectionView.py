"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    This plugin organizes detection information and saves it into the cache in 
    order to plot it.  Helpfil to degub detector.

    Parameters
    -----------
        time_elapsed    : string "HH:MM:S.S"
            Time elapsed since the beginning of the recording to show.
        win_len_show    : double
            Window length in sec to show.
        signals : a list of SignalModel
            signal.samples : The actual signal data as numpy list
            signal.sample_rate : the original  sampling rate of the signal
            signal.channel : current channel label             
        event_name      : string
            Event label selected for display
        channel         : string
            Channel label selected for display
        win_step_sec    : float 
            Window step in sec (each time the fft is applied)
        events          : Pandas DataFrame
            DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])     
        win_activity    : list of ndarray of n_windows
            Each item correspond to an item of signals for the selected channel to display
            Spectral power in the frequency bins from low_freq to high_freq. 
        threshold : list of double
            Each item correspond to an item of signals for the selected channel to display
            The threshold to detect events.
        threshold_unit : string
            The threshold unit (fixed, x BSL median or x BSL STD).
        filename : string
            Python filename to save data to display an additional detection window.
        win_bsl     : list of ndarray of n_windows (or [2 x n_windows])
            Each item correspond to an item of signals for the selected channel to display
            median_use==True : Median spectral power of the baseline window 
            median_use==False : Mean and standard deviation of the baseline 
            spectral power (row1: mean, row2: std). 
    Returns
    -----------  

    @author: David Lévesque (david.levesque.cnmtl@ssss.gouv.qc.ca)
    @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)

    Log : 
        2021-04-23 : First release, klacourse
        
"""

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import numpy as np
import pandas as pd
from scipy import signal
import os

DEBUG = True

class DetectionView(SciNode):
    """
        This plugin organizes detection information and saves it into the cache in 
        order to plot it.  Helpfil to degub detector.

        Parameters
        -----------
            time_elapsed    : string "HH:MM:S.S"
                Time elapsed since the beginning of the recording to show.
            win_len_show    : double
                Window length in sec to show.        
            signals : a list of SignalModel
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the original  sampling rate of the signal
                signal.channel : current channel label                  
            event_name      : string
                Event label selected for display
            channel         : string
                Channel label selected for display                
            win_step_sec    : float 
                Window step in sec (each time the fft is applied)
            events          : Pandas DataFrame
                DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])     
            win_activity    : list of ndarray of n_windows
                Each item correspond to an item of signals for the selected channel to display
                Spectral power in the frequency bins from low_freq to high_freq. 
            threshold : list of double
                Each item correspond to an item of signals for the selected channel to display
                The threshold to detect events.
            threshold_unit : string
                The threshold unit (fixed, x BSL median or x BSL STD).
            filename : string
                Python filename to save data to display an additional detection window.
            win_bsl     : list of ndarray of n_windows (or [2 x n_windows])
                Each item correspond to an item of signals for the selected channel to display
                median_use==True : Median spectral power of the baseline window 
                median_use==False : Mean and standard deviation of the baseline 
                spectral power (row1: mean, row2: std). 

        Returns
        -----------  

        @author: David Lévesque (david.levesque.cnmtl@ssss.gouv.qc.ca)
        @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)

        Log : 
            2021-04-23 : First release, klacourse
            2021-06-28 : Change SignalModel to Signal dictionary
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('DetectionView.__init__')
        InputPlug('time_elapsed', self)
        InputPlug('win_len_show', self)
        InputPlug('signals', self)
        InputPlug('event_name', self)
        InputPlug('channel', self)
        InputPlug('win_step_sec', self)
        InputPlug('events', self)
        InputPlug('win_activity', self)
        InputPlug('threshold', self)
        InputPlug('threshold_unit', self)
        InputPlug('filename', self)
        InputPlug('win_bsl', self)        

    def __del__(self):
        if DEBUG: print('DetectionView.__del__')

    def subscribe_topics(self):
        pass

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'DetectionView.on_topic_update {topic}:{message}')

    def compute(self, time_elapsed, win_len_show, signals, event_name, channel, \
        win_step_sec, events, win_activity, threshold, threshold_unit, filename, \
             win_bsl=None):
        """
            This plugin organizes detection information and saves it into the cache in 
            order to plot it.  Helpfil to degub detector.

            Parameters
            -----------
                time_elapsed    : string "HH:MM:S.S"
                    Time elapsed since the beginning of the recording to show.
                win_len_show    : double
                    Window length in sec to show.            
                signals : a list of SignalModel
                    signal.samples : The actual signal data as numpy list
                    signal.sample_rate : the original  sampling rate of the signal
                    signal.channel : current channel label      
                event_name      : string
                    Event label selected for display                    
                channel         : string
                    Channel label selected for display                    
                win_step_sec    : float 
                    Window step in sec (each time the fft is applied)
                events          : Pandas DataFrame
                    DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])     
                win_activity    : list of ndarray of n_windows
                    Each item correspond to an item of signals for the selected channel to display
                    Spectral power in the frequency bins from low_freq to high_freq. 
                threshold : list of double
                    Each item correspond to an item of signals for the selected channel to display
                    The threshold to detect events.
                threshold_unit : string
                    The threshold unit (fixed, x BSL median or x BSL STD).
                filename : string
                    Python filename to save data to display an additional detection window.
                win_bsl     : list of ndarray of n_windows (or [2 x n_windows])
                    Each item correspond to an item of signals for the selected channel to display
                    median_use==True : Median spectral power of the baseline window 
                    median_use==False : Mean and standard deviation of the baseline 
                    spectral power (row1: mean, row2: std).                  
        """
        if DEBUG: print('DetectionView.compute {}'.format(event_name))

        # Clear the cache and the file on the disk (usefull for the second run)
        self.clear_cache()
        if not filename=='':
            if os.path.exists(filename):
                os.remove(filename)
                war_message = "WARNING : {} has been erased".format(filename)
                self._log_manager.log(self.identifier, war_message)

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if isinstance(signals,str) and signals=='':
            raise NodeInputException(self.identifier, "signals", \
                f"DetectionView this input is not connected.")
        elif not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"DetectionView input of wrong type. Expected: <class 'list'> received: {type(signals)}")     

        if isinstance(win_activity, str) and win_activity=='':
            err_message = "ERROR : win_activity not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "win_activity", f"DetectionView this input is not connected.")         

        if isinstance(threshold, str) and threshold=='':
            err_message = "ERROR : threshold not initialized"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "threshold", f"DetectionView this input is not defined.")

        if isinstance(filename, str) and filename=='':
            err_message = "ERROR: filename not initialized"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "filename", f"DetectionView this input is not defined.")

        # Convert from string all inputs from the settings view
        win_len_show = float(win_len_show)
        if isinstance(threshold, str):
            threshold = float(threshold)

        # Not a detection based on windows
        if win_step_sec=='':
            win_step_sec = 0
        else:
            win_step_sec = float(win_step_sec)             

        if "median" in threshold_unit.lower():
            median_use = True
        else:
            median_use = False

        # When win_bsl is not connected
        if isinstance(win_bsl,str):
            win_bsl=None
            if not ("fixed" in threshold_unit.lower()):
                err_message = "ERROR : a fixed threshold is expected when no baseline info are provided"
                self._log_manager.log(self.identifier, err_message)

        # Manage more than one channel
        # Accumulate the info for the selected channel
        signals_chan = []
        threshold_cpy = []
        for i, signal_model_cur in enumerate(signals):
        #for i, (label, channel_data) in enumerate(signals.items()):
            if signal_model_cur.channel in channel:
                signals_chan.append(signal_model_cur)
                if isinstance(threshold,list):
                    threshold_cpy.append(threshold[i])
                else:
                    threshold_cpy.append(threshold)

        if len(signals_chan)>0:
            # if len(signal_model)>1:
            #     err_message = "ERROR DetectionView ({}): more than one channel were found.\n" +\
            #         "Only the first channel found is selected for display".format(event_name)
            #     self._log_manager.log(self.identifier, err_message)

            # # Extract the first channel found
            # signal_model = signal_model[0]
            # if isinstance(threshold, list):
            #     threshold = threshold_cpy[0]

            # Add a reference to the signal_model
            fs = signals_chan[0].sample_rate

            # Extract the events_name
            if len(events)>0:
                spec_df_events = events[events.name == event_name]
                spec_df_events = spec_df_events[spec_df_events.channels == channel]
            else:
                spec_df_events = ''            

            # -----------------------------------------------------------------
            # Convert a by-window information to by-sample information to match the signal
            # -----------------------------------------------------------------
            if win_step_sec != 0:
                det_act_smp = []
                for win_activity_cur in win_activity:
                    nsample_step = win_step_sec*fs
                    if not nsample_step.is_integer():
                        # Compute the real win_step used
                        print("Warning : win_step {} is changed for {}".format(win_step_sec, int(round(nsample_step))/fs))
                        win_step_sec = int(round(nsample_step))/fs
                    nsample_step = int(round(win_step_sec*fs))

                    reps = np.ones(win_activity_cur.shape[0],dtype=int) * nsample_step
                    det_act_smp_cur = np.repeat(win_activity_cur, reps)
                    det_act_smp.append(det_act_smp_cur)
            else:
                det_act_smp = win_activity

            for i, signal_chan in enumerate(signals_chan):
                # Different length when the last window is incomplete
                # I think the best way is to duplicate the last info
                if len(signal_chan.samples) > len(det_act_smp[i]):
                    values_2_pad = np.ones(len(signal_chan.samples)-len(det_act_smp[i]))*det_act_smp[i][-1]
                    det_act_smp[i] = np.concatenate((det_act_smp[i],values_2_pad))
                elif len(signal_chan.samples) < len(det_act_smp[i]):
                    err_message = 'ERROR : unexpected length of windows detection'
                    self._log_manager.log(self.identifier, err_message)

            # Adaptive spectral detections are shown
            # win_bsl can be 1D or 2 dimensions
            bsl_smp = []
            #if not all([elem == None for elem in win_bsl]):
            if not win_bsl==None:
                for i, signal_chan in enumerate(signals_chan):
                    bsl_smp_cur = np.repeat(win_bsl[i], nsample_step, axis=-1)
                    if len(bsl_smp_cur.shape)<2:
                        # To be able to select the first dim (in a 1D array)
                        bsl_smp_cur = np.expand_dims(bsl_smp_cur,axis=0)
                    if len(signal_chan.samples) != len(bsl_smp_cur[0,:]):
                        nvalues_2_pad = len(signal_chan.samples)-len(bsl_smp[0,:])
                        value_tmp = bsl_smp_cur[:,-1][np.newaxis]
                        values_2_pad = np.ones((bsl_smp_cur.shape[0],nvalues_2_pad))*value_tmp.T
                        bsl_smp_cur = np.concatenate((bsl_smp_cur,values_2_pad),axis=-1)     
                    bsl_smp.append(bsl_smp_cur)

            # -----------------------------------------------------------------
            # Get Seconds from time asked, it is the starting time
            # -----------------------------------------------------------------
            nhour, nmin, nsec = time_elapsed.split(':')
            winshow_start_sec = int(nhour) * 3600 + int(nmin) * 60 + float(nsec)

            # Save the whole data into the file in settings (on disk)
            cache = {}
            cache['win_len_show'] = win_len_show
            cache['signal_model'] = signals_chan
            cache['event_name'] = event_name
            cache['events'] = events
            cache['det_act_smp'] = det_act_smp
            cache['threshold'] = threshold_cpy
            cache['median_use'] = median_use
            # Adaptive spectral detections are shown
            #if not all([elem == None for elem in win_bsl]):
            if not win_bsl==None:
                cache['bsl_smp'] = bsl_smp

            np.save(filename, cache)
            war_message = "WARNING : {} has been written".format(filename)
            self._log_manager.log(self.identifier, war_message)                

            # -----------------------------------------------------------------
            # Extract signal and info detection to save in the workspace cache 
            # -----------------------------------------------------------------
            # Find the item from the list where the data starts
            signal_chan_start = None
            signal_i = None
            threshold_chan_start = None
            for i, signal in enumerate(signals_chan):
                if (signal.start_time+signal.duration)>=winshow_start_sec:
                    signal_i = i
                    signal_chan_start = signal
                    threshold_chan_start = threshold_cpy[i]
                    break
            #signal_chan_start = [signal for signal in signals_chan if any((signal.start_time+signal.duration)>=winshow_start_sec)]
            #signal_i = [signal_i for signal_i, signal in enumerate(signals_chan) if (signal.start_time+signal.duration)>=winshow_start_sec]
            if not signal_chan_start==None:
                computed_start = signal_chan_start.start_time
                smp_start_i = int((winshow_start_sec-computed_start) * fs)
                if smp_start_i<0:
                    smp_start_i = 0
                    winshow_start_sec = signal_chan_start.start_time
                    nmin, nsec = divmod(winshow_start_sec, 60)
                    nhour, nmin = divmod(nmin, 60)
                    time_elapsed = f'{int(nhour):02d}:{int(nmin):02d}:{int(nsec):02d}'
                smp_stop_i = smp_start_i + int(win_len_show * fs)

                # Pad with nans if the window to show ends after the actual recording
                nanpad = 0
                if smp_start_i > len(signal_chan_start.samples):
                    nanpad = int(win_len_show * fs)
                    smp_start_i = len(signal_chan_start.samples)
                    smp_stop_i = len(signal_chan_start.samples)
                elif smp_stop_i > len(signal_chan_start.samples):
                    nanpad = smp_stop_i-len(signal_chan_start.samples)
                    smp_stop_i = len(signal_chan_start.samples)

                nan_array = np.empty(nanpad)
                nan_array[:] = np.nan
                ts_extracted = np.concatenate((signal_chan_start.samples[smp_start_i:smp_stop_i],nan_array),axis=0)
                det_smp_extracted = np.concatenate((det_act_smp[signal_i][smp_start_i:smp_stop_i],nan_array),axis=0)
                #if not all([elem == None for elem in win_bsl]):
                if not win_bsl==None:
                    nan_array = np.empty((bsl_smp[signal_i].shape[0],nanpad))
                    bsl_smp_extracted = np.concatenate((bsl_smp[signal_i][:,smp_start_i:smp_stop_i],nan_array),axis=-1)

                # To avoid reference
                signal_extracted = signal_chan_start.clone(clone_samples=False)
                signal_extracted.samples = ts_extracted

                # Extract events
                if len(spec_df_events):
                    #   event starts before the end of the window showed (winshow_offset_sec+win_len_show)
                    #   event ends after the start of the window showed (winshow_offset_sec) and 
                    new_df_events = spec_df_events[(spec_df_events.start_sec < (winshow_start_sec+win_len_show))\
                                            & ((spec_df_events.start_sec+spec_df_events.duration_sec) > winshow_start_sec)]
                    # when the window ends before the time serie, the detection can ends before the time serie
                    # to avoid that problem the detection could be regenerated from 
                    #   det_smp_extracted and bsl_smp_extracted (with the threshold)
                else:
                    new_df_events = ''

                cache = {}
                cache['time_elapsed'] = time_elapsed
                cache['win_len_show'] = win_len_show
                cache['signal_model'] = signal_extracted
                cache['signal_i'] = signal_i
                cache['n_signals_chan'] = len(signals_chan)
                cache['events'] = new_df_events
                cache['det_act_smp'] = det_smp_extracted
                cache['threshold'] = threshold_chan_start
                cache['median_use'] = median_use
                cache['filename'] = filename
                #if not all([elem == None for elem in win_bsl]):
                if not win_bsl==None:
                    cache['bsl_smp'] = bsl_smp_extracted
                self._cache_manager.write_mem_cache(self.identifier, cache)
            else:
                err_message = "ERROR : Time asked is outside the signals"
                self._log_manager.log(self.identifier, err_message)
                raise NodeRuntimeException(self.identifier, "time_elapsed", f"DetectionView this input is outside the signals.")            

        elif len(signals_chan)==0:
            err_message = "ERROR : Channel label not found"
            self._log_manager.log(self.identifier, err_message)
            err_message = "ERROR DetectionView ({}): Channel label not found".format(event_name)
            print(err_message)

           

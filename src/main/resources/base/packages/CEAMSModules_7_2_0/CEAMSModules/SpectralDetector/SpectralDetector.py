"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    This plugin detects events based on the spectrum.
    The plugin is flexible, an event can be detected when power goes above 
    or below the threshold.  The threshold can be fixed or adaptive based on 
    a baseline window around the event.  The adaptive threshold can be x times 
    the baseline median value or x times the standard deviation of the baseline.
    When a z-score is used as threshold (x BSL STD log10), the power values are log10 
    transformed to make them more normally distributed.

    Parameters
    -----------
        psds        : dict
            The power spectral density of all windows.
            p = psd['psd'], narray [n_windows x n_freq_bins]
            freq_bins = psd['freq_bins']; The frequencies of the bins within the psds
            win_len = psd['win_len']; The length of the detection windows on which the psds was done (in seconds)
            win_step = psd['win_step']; The step between the detection windows on which the psds was done (in seconds)
        event_group  : string
            Event group.
        event_name  : string
            Event label.
        low_freq    : string
            The lower frequency of the bandwidth targeted by the detection
        high_freq   : string
            The higher frequency of the bandwidth targeted by the detection
        rel_freq : string
            '0' the frequency band is absolute (low_freq to high_freq)
            '1' the frequency band is relative (absolute band / background band)
        bsl_low_freq : string
            The lower frequency of the baseline used to compute the relative power.
        bsl_high_freq : string
            The higher frequency of the baseline used to compute the relative power.
        threshold_val : string or a list of float
            String : the value to threshold to detect events.
            list : the value to threshold for each signal included in signals.
        threshold_unit : string
            The threshold unit
            -fxed
            -x BSL median, x BSL STD or x BSL STD(log10)
            -x epochs STD, x epochs STD(log10)
        threshold_behavior : string
            Above : Event is detected when activity goes above the threshold. 
            Below : Event is detected when activity goes below the threshold. 
        sleep_stages : pandas dataframe (columns=['group','name','start_sec','duration_sec','channels']) 
            (optional) Sleep stages list.
        baseline_win_len : string
            (optional) The baseline window length in seconds
        art_events : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])   
            (optional) Artefact events previously detected
        channel_dbg : String
            Channel label to save and exit detection info.

    Returns
    -----------  
        events          : Pandas DataFrame
            DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])     
        win_activity    : ndarray of n_windows
            Spectral power in the frequency bins from low_freq to high_freq.
        win_bsl     : ndarray of n_windows
            (Optional) Median\STD spectral power of the baseline window (low_freq to high_freq).   

    @author: David Lévesque (david.levesque.cnmtl@ssss.gouv.qc.ca)
    @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)

    Log : 
        2021-04-22 : Output detection_win_activity and med_bsl_win, klacourse
        2021-05-04 : Managed the fixed spectral detector, klacourse
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.mixture import GaussianMixture

import config
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from flowpipe.ActivationState import ActivationState
from flowpipe import SciNode, InputPlug, OutputPlug

from CEAMSModules.EventCompare import performance as performance
from CEAMSModules.EventReader import manage_events
from CEAMSModules.Stft import spectral_detection as spectral_detection

DEBUG = False

class SpectralDetector(SciNode):
    """
    This plugin detects events based on the spectrum.
    The plugin is flexible, an event can be detected when power goes above 
    or below the threshold.  The threshold can be fixed (as a uV^2 value) 
    , adaptive based on a baseline window around the event (x BSL median) 
    or adaptif based on the epochs of the recording (x epochs STD).
    The adaptive threshold can be x times the baseline median value or
     x times the standard deviation of the baseline.
    When a z-score is used as threshold (x BSL STD log10), the power values are log10 
    transformed to make them more normally distributed.

    Parameters
    -----------
        psds        : dict
            The power spectral density of all windows.
                psd : power (µV^2) narray [n_fft_windows x n_frequency_bins]
                freq_bins : frequency bins (Hz); The frequencies of the bins within the psds
                win_len : windows length (s); The length of the detection windows on which the psds was done (in seconds)
                win_step : windows step (s); The step between the detection windows on which the psds was done (in seconds)
                sample_rate : sampling rate of the original signal (Hz)
                chan_label : channel label
                start_time : start (s) of the signal (item of signals) on which the ffts are performed
                end_time : end (s) of the signal (item of signals) on which the ffts are performed
                duration : duraiton (s) of the signal (item of signals) on which the ffts are performed
        event_group  : string
            Event group.
        event_name  : string
            Event label.
        low_freq    : string
            The lower frequency of the bandwidth targeted by the detection
        high_freq   : string
            The higher frequency of the bandwidth targeted by the detection
        rel_freq : string
            '0' the frequency band is absolute (low_freq to high_freq)
            '1' the frequency band is relative (absolute band / background band)
        bsl_low_freq : string
            The lower frequency of the baseline used to compute the relative power.
        bsl_high_freq : string
            The higher frequency of the baseline used to compute the relative power.
        threshold_val : string or a list of float
            String : the value to threshold to detect events.
            list : the value to threshold for each signal included in signals.
        threshold_unit : string
            The threshold unit
              -fxed
              -x BSL median, x BSL STD or x BSL STD(log10)
              -x epochs STD, x epochs STD(log10)
        threshold_behavior : string
            Above : Event is detected when activity goes above the threshold. 
            Below : Event is detected when activity goes below the threshold. 
        sleep_stages : pandas dataframe (columns=['group','name','start_sec','duration_sec','channels']) 
            (optional) Sleep stages list.
        baseline_win_len : string
            (optional) The baseline window length in seconds
        art_events : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])   
            (optional) Artefact events previously detected
        channel_dbg : String
            Channel label to save and exit detection info.      
    Returns
    -----------  
        events          : Pandas DataFrame
            DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])     
        win_activity    : ndarray of n_windows
            Spectral power in the frequency bins from low_freq to high_freq.
        win_bsl     : ndarray of n_windows
            (Optional) Median\STD spectral power of the baseline window (low_freq to high_freq).     
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('SpectralDetector.__init__')
        InputPlug('psds', self)
        InputPlug('event_group', self)
        InputPlug('event_name', self)
        InputPlug('low_freq', self)
        InputPlug('high_freq', self)
        InputPlug('rel_freq', self)
        InputPlug('bsl_low_freq', self)
        InputPlug('bsl_high_freq', self)        
        InputPlug('threshold_val', self)
        InputPlug('threshold_unit', self)
        InputPlug('threshold_behavior', self)
        InputPlug('sleep_stages', self)
        InputPlug('baseline_win_len', self)  
        InputPlug('art_events', self)  
        InputPlug('channel_dbg', self)  
        OutputPlug('events', self)
        OutputPlug('win_activity', self)
        OutputPlug('win_bsl', self)

        # Counter of sets of events if the plugin is called in a loop
        self._event_set_i = 1 # Only used in debug mode to save png histograms with different name
        # The number of components from the gaussian mixture
        self._n_gauss_components = 3 # 2 (not enough), 3 (the best results), 4 (thresholds=3 is more adapted)
          

    def __del__(self):
        if DEBUG: print('SpectralDetector.__del__')

    def subscribe_topics(self):
        pass

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'SpectralDetector.on_topic_update {topic}:{message}')

    def compute(self, psds, event_group, event_name, low_freq, high_freq, rel_freq, \
        bsl_low_freq, bsl_high_freq, threshold_val, threshold_unit, \
        threshold_behavior, sleep_stages, baseline_win_len, art_events, channel_dbg):
        """
        This function detects events based on the spectrum.
        An event can be detected when activity goes above or below the threshold.  
        The threshold can be fixed or adaptive based on a baseline window around
        the event.  The adaptive threshold can be x times the baseline median 
        value or x times the standard deviation of the baseline.
        When a z-score is used as threshold (x BSL STD log10), the PSD values are log10 
        transformed to make them more normally distributed.

        Parameters
        -----------
            psds        : dict
                The power spectral density of all windows.
                p = psd['psd'], narray [n_windows x n_freq_bins]
                freq_bins = psd['freq_bins']; The frequencies of the bins within the psds
                win_len = psd['win_len']; The length of the detection windows on which the psds was done (in seconds)
                win_step = psd['win_step']; The step between the detection windows on which the psds was done (in seconds)
            event_group  : string
                Event group.
            event_name  : string
                Event label.
            low_freq    : string
                The lower frequency of the bandwidth targeted by the detection
            high_freq   : string
                The higher frequency of the bandwidth targeted by the detection
            rel_freq : string
                '0' the frequency band is absolute (low_freq to high_freq)
                '1' the frequency band is relative (absolute band / background band)
            bsl_low_freq : string
                The lower frequency of the baseline used to compute the relative power.
            bsl_high_freq : string
                The higher frequency of the baseline used to compute the relative power.
            threshold_val : string or a list of float
                String : the value to threshold to detect events.
                list : the value to threshold for each signal included in signals.
            threshold_unit : string
                The threshold unit
                -fxed
                -x BSL median, x BSL STD or x BSL STD(log10)
                -x epochs STD, x epochs STD(log10)
            threshold_behavior : string
                Above : Event is detected when activity goes above the threshold. 
                Below : Event is detected when activity goes below the threshold. 
            sleep_stages : pandas dataframe (columns=['group','name','start_sec','duration_sec','channels']) 
                (optional) Sleep stages list.
            baseline_win_len : string
                (optional) The baseline window length in seconds if threshold_unit=x BSL 
            art_events : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])   
                (optional) Artefact events previously detected
            channel_dbg : String
                Channel label to save and exit detection info.     

        Returns
        -----------  
            events          : Pandas DataFrame
                DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])     
            win_activity    : ndarray of n_windows
                Spectral power in the frequency bins from low_freq to high_freq.
            win_bsl         : ndarray of n_windows (or [2 x n_windows])
                median_use==True : Median spectral power of the baseline window 
                median_use==False : Mean and standard deviation of the baseline 
                spectral power (row1: mean, row2: std).
        """
        if DEBUG: print('SpectralDetector.compute {}'.format(event_name))
        # Clear the cache (usefull for the second run)
        self.clear_cache() 

        # It is possible to bypass the SpectralDetector by passing 
        # the input art_events directly to the output events without any modification
        if self.activation_state == ActivationState.BYPASS:
            if isinstance(art_events,pd.DataFrame):
                return {
                    'events': art_events,
                    'win_activity' : [],
                    'win_bsl'  : []
                }
            else:
                return {
                    'events': manage_events.create_event_dataframe(None),
                    'win_activity' : [],
                    'win_bsl'  : []
                }                

        # If psds is not connected
        if isinstance(psds,str) and psds=='':
            raise NodeInputException(self.identifier, \
                "psds", f"SpectralDetector this input is not connected.")
        # If psds type is wrong
        if not isinstance(psds,list):
            raise NodeInputException(self.identifier, "psds", \
                f"SpectralDetector input of wrong type. Expected: <class 'list'> received: {type(psds)}")    
        # Threshold is not connected
        if isinstance(threshold_val,str) and threshold_val=='':
            raise NodeInputException(self.identifier, "threshold_val", \
                f"SpectralDetector is not connected")
        if isinstance(sleep_stages,str) and sleep_stages=='':
            if "x epochs STD" in threshold_unit:
                raise NodeInputException(self.identifier, "sleep_stages", \
                    f"SpectralDetector is not connected")

        # There are default values to avoid error
        low_freq = float(low_freq)              # Absolute freq band
        high_freq = float(high_freq)            # Absolute freq band
        if int(rel_freq):
            bsl_low_freq = float(bsl_low_freq)  # Relative freq band
            bsl_high_freq = float(bsl_high_freq)# Relative freq band
        else:
            bsl_low_freq = None
            bsl_high_freq = None       

        if 'above' in threshold_behavior.lower():
            above_thresh_det=True
        elif 'below' in threshold_behavior.lower():
            above_thresh_det=False
        else:
            above_thresh_det=False
            err_message = 'ERROR: unexpected threshold_behavior from the combobox = {}'\
                .format(threshold_behavior)
            self._log_manager.log(self.identifier, err_message)
            if DEBUG: 
                print('SpectralDetector ' + err_message)        

        log10_transform = True if 'log10' in threshold_unit.lower() else False     

        # If art_events is not connected
        if isinstance(art_events,str):
            if art_events=='':
                art_events = manage_events.create_event_dataframe(None)
            else:
                raise NodeInputException(self.identifier, "art_events", \
                    f"SpectralDetector input of wrong type. Expected: <class 'list'> received: {type(art_events)}")   
        elif not isinstance(art_events, pd.DataFrame):
            raise NodeInputException(self.identifier, "art_events", \
                f"SpectralDetector input of wrong type. Expected: <class 'list'> received: {type(art_events)}")     

        # Create a pandas dataframe of events (each row is an event)
        events_df = manage_events.create_event_dataframe(None)         

        # Debug information to save and exit
        dbg_chan_found = 0
        psd_dbg = []
        detections_dbg = manage_events.create_event_dataframe(None) 
        win_activity_dbg = []
        win_bsl_dbg = []

        # A fixed threshold is used for all channels for all the recording
        if baseline_win_len=='':
            win_bsl = None
            if ("BSL" in threshold_unit.lower()) :
                raise NodeInputException(self.identifier, "threshold_unit", \
                    f"SpectralDetector threshold_unit includes the use of a baseline and no baseline length was provided")     

            # The threshold is based on the histogram
            if "x epochs std" in threshold_unit.lower():
                # Prepare the array to accumulate the window activity
                tot_win_act = np.empty([0])
                        
                # Extract the sleep stages information
                stage_start_all = sleep_stages['start_sec'].to_numpy()
                stage_start_all = stage_start_all.astype(float)
                stage_start_all = np.around(stage_start_all, 2)
                stage_duration_all = sleep_stages['duration_sec'].to_numpy()
                stage_duration_all = stage_duration_all.astype(float)
                stage_duration_all = np.around(stage_duration_all, 2)

                # Loop on the psds (hopefullty one per channel)
                for psd in psds:

                    # Compute/accumulate the win activity
                    detections, win_activity  = spectral_detection.fix_compute(
                        psd['psd'],
                        psd['freq_bins'],
                        low_freq,
                        high_freq,
                        threshold_val = None,
                        above_thresh_det = None,
                        log10_transform = log10_transform,
                        bsl_low_freq=bsl_low_freq,
                        bsl_high_freq=bsl_high_freq)

                    # Extract only the activity of the selected sleep stages
                    for stage_start, stage_dur in zip(stage_start_all, stage_duration_all):
                        # Extract the psd values data for the current stage
                        psd_values_current, psd_start_current = self.extract_psd_from_event(\
                            win_activity, psd['start_time'], psd['end_time'],\
                                psd['win_step'], psd['win_len'], stage_start, stage_dur)
                        # If found in the current bout add it to the list
                        if len(psd_values_current)>0:
                            # Vertical concatenation of the psd values
                            # Make the psd_values_current(x,) into 2D array (x,1)
                            psd_values_current = np.reshape(psd_values_current, (psd_values_current.shape[0], 1))
                            tot_win_act = np.vstack((tot_win_act, psd_values_current)) if len(tot_win_act)>0 else psd_values_current

                # Fit the gaussian mixture
                if len(tot_win_act)>3:
                    # Remove nan from the tot_win_act (possible when run after the Reset Signal Artifact )
                    tot_win_act = tot_win_act[~np.isnan(tot_win_act)]
                    # The weights favorize one gaussien if only one component is needed.
                    def_weights_gauss = np.ones((self._n_gauss_components,1))
                    def_weights_gauss = def_weights_gauss*10**(-10)
                    def_weights_gauss[0] = 1-10**(-10)                    
                    # init_params="random" is chosen to avoid a dead lock in multi threading (https://github.com/MeteoSwiss/ampycloud/issues/97) 
                    gaus_mixt = GaussianMixture(n_components=self._n_gauss_components, covariance_type='spherical', \
                        weights_init=def_weights_gauss.reshape(self._n_gauss_components), \
                            init_params="random", random_state=0).fit(tot_win_act.reshape(-1,1))
                    # The main gaussian distribution has the greatest weight
                    main_component = np.argmax(gaus_mixt.weights_)
                    # Extract the stats of the main gaussian
                    std_main=np.sqrt(gaus_mixt.covariances_[main_component])
                    mean_main=gaus_mixt.means_[main_component,0]
                    if isinstance(threshold_val, str):
                        threshold_val = float(threshold_val)
                    # The threshold is negative when data to mark is lower than the mode.
                    threshold_val = mean_main + threshold_val*std_main
                    if DEBUG:
                        # save the hypnogram with the normal fit, mode, std and current threshold
                        figure, histo_ax = plt.subplots()
                        nbins=50
                        n, bins, patches = histo_ax.hist(tot_win_act, bins=nbins, density=True)
                        # add a 'best fit' line on the data normally distributed
                        x = np.linspace(min(bins), max(bins), nbins)
                        p = norm.pdf(x, mean_main, std_main)
                        histo_ax.plot(x, p, 'r--', linewidth=2)
                        histo_ax.axvline(x=mean_main,color='b')
                        histo_ax.axvline(x=mean_main+std_main,c='b',ls='--')
                        histo_ax.axvline(x=mean_main+2*std_main,c='b',ls='--')
                        histo_ax.axvline(x=threshold_val,color='k')
                        figure.savefig(f"histogram_{event_name}_{self._event_set_i}.pdf")
                        self._event_set_i = self._event_set_i + 1
                else:
                    raise NodeRuntimeException(self.identifier, "psds", \
                        f"SpectralDetector does not have enough statistics to compute standard deviation")

            # Detects events based on the PSD information
            # Loop through channels
            for i, psd in enumerate(psds):

                # Detects events based on the PSD information
                # Add references
                p = psd['psd']                    
                freq_bins = psd['freq_bins']
                fs = psd['sample_rate']
                win_len = psd['win_len']
                win_step = psd['win_step']

                # Setect the right threshold if it is provided via list
                if isinstance(threshold_val, str):
                    threshold_val_cur = float(threshold_val)
                elif isinstance(threshold_val, list):
                    threshold_val_cur = threshold_val[i]
                else:
                    threshold_val_cur = threshold_val

                # The windows size (length and step) in second are adjusted for the sampling rate
                nsample_win = win_len*fs
                if not nsample_win.is_integer():
                    if DEBUG:
                        print("SpectralDetector.Warning : win_len {} is changed for {}".\
                            format(win_len, int(round(nsample_win))/fs))
                    self._log_manager.log(self.identifier, "win_len {} is changed for {}".\
                        format(win_len, int(round(nsample_win))/fs))
                    win_len = int(round(nsample_win))/fs
                nsample_step = win_step*fs
                if not nsample_step.is_integer():
                    if DEBUG:
                        print("SpectralDetector.Warning : win_step {} is changed for {}".\
                            format(win_step, int(round(nsample_step))/fs))
                    self._log_manager.log(self.identifier, "win_step {} is changed for {}".\
                            format(win_step, int(round(nsample_step))/fs))
                    win_step = int(round(nsample_step))/fs   

                # Run detector
                detections, win_activity  = spectral_detection.fix_compute(
                    p,
                    freq_bins,
                    low_freq,
                    high_freq,
                    threshold_val_cur,
                    above_thresh_det,
                    log10_transform, 
                    bsl_low_freq=bsl_low_freq,
                    bsl_high_freq=bsl_high_freq)

                # Add the spectral detections into the dataframe as events named
                # with the event_name and the channel as suffix
                (events_df, events_df_psd) = self._add_spectral_events(\
                    events_df, event_group, event_name, detections, psd)

                # Save debugging info
                if config.is_dev: # Avoid save of the recording when not developping
                    if channel_dbg in psd['chan_label']:
                        dbg_chan_found = 1
                        psd_dbg = psd
                        detections_dbg = pd.concat([detections_dbg,events_df_psd])
                        win_activity_dbg.append(win_activity)
                        win_bsl_dbg = win_bsl

        # An adaptive threhold is used
        else:
            if "median" in threshold_unit.lower():
                median_use = True
                log10_data = False
            elif "std" in threshold_unit.lower():
                median_use = False
                if "log10" in threshold_unit.lower():
                    log10_data = True
                else:
                    log10_data = False
            else:
                err_message = "ERROR : threshold_unit is not relative to " + \
                    "the baseline and a baseline length is provided"
                self._log_manager.log(self.identifier, err_message)
                if DEBUG: 
                    print('SpectralDetector ' + err_message)                         
                median_use = False
                log10_data = False

            baseline_win_len = float(baseline_win_len)

            # For each channel detects events based on the PSD information
            for i, psd in enumerate(psds):

                # Filter the previously detected artifact for the current channel
                # Only based on the event group that must be artifact
                # and the artifact event must be on the current channel
                art_events_chan = art_events[(art_events.group=='artifact') & (art_events.channels==psd['chan_label'])]

                # Detects events based on the PSD information
                # Add references
                p = psd['psd']
                freq_bins = psd['freq_bins']
                fs = psd['sample_rate']
                win_len = psd['win_len']
                win_step = psd['win_step']

                # Setect the right threshold if it is provided via list
                if isinstance(threshold_val, str):
                    threshold_val_cur = float(threshold_val)
                elif isinstance(threshold_val, list):
                    threshold_val_cur = threshold_val[i]
                else:
                    threshold_val_cur = threshold_val

                # The windows size (length and step) in second are adjusted for the sampling rate
                nsample_win = win_len*fs
                if not nsample_win.is_integer():
                    if DEBUG:
                        print("SpectralDetector.Warning : win_len {} is changed for {}".\
                            format(win_len, int(round(nsample_win))/fs))
                    self._log_manager.log(self.identifier, "win_len {} is changed for {}".\
                        format(win_len, int(round(nsample_win))/fs))
                    win_len = int(round(nsample_win))/fs
                nsample_step = win_step*fs
                if not nsample_step.is_integer():
                    if DEBUG:
                        print("SpectralDetector.Warning : win_step {} is changed for {}".\
                            format(win_step, int(round(nsample_step))/fs))
                    self._log_manager.log(self.identifier, "win_step {} is changed for {}".\
                            format(win_step, int(round(nsample_step))/fs))
                    win_step = int(round(nsample_step))/fs  

                # detection_win : ndarray of n_windows
                #   Events array, 0 means no event and 1 means an event.
                #   detection_win is windows based
                # detection_win_activity : ndarray of n_windows
                #   Spectral power in the frequency bins from low_freq to high_freq.
                #   detection_win_activity is windows based
                # bsl_win : ndarray of n_windows (or [2 x n_windows])
                #   bsl_win is windows based
                detections, win_activity, win_bsl  = spectral_detection.adp_compute(
                    p,
                    freq_bins,
                    low_freq,
                    high_freq,
                    win_len,
                    win_step,
                    threshold_val_cur,
                    above_thresh_det,
                    baseline_win_len, 
                    median_use,
                    log10_data,
                    art_events=art_events_chan,
                    bsl_low_freq=bsl_low_freq,
                    bsl_high_freq=bsl_high_freq)

                # Add the spectral detections into the events_df as events named
                # with the event_name and the channel as suffix
                (events_df, events_df_psd) = self._add_spectral_events(\
                    events_df, event_group, event_name, detections, psd)

                # Save debugging info 
                if config.is_dev: # Avoid save of the recording when not developping
                    if channel_dbg in psd['chan_label']:
                        dbg_chan_found = 1
                        psd_dbg = psd
                        detections_dbg = pd.concat([detections_dbg,events_df_psd])
                        win_activity_dbg.append(win_activity)
                        win_bsl_dbg.append(win_bsl)

        # Add the events from previous artefact detector
        events_df = pd.concat([events_df,art_events])
        # Reset index
        events_df.reset_index(inplace=True, drop=True)
        # Sort events based on the start_sec
        events_df.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')  

        if config.is_dev: # Avoid save of the recording when not developping
            if dbg_chan_found==0 and len(psds)>0:
                err_message = 'ERROR: no debug channel found'
                self._log_manager.log(self.identifier, err_message)
                if DEBUG: 
                    print('SpectralDetector ' + err_message)  
                psd_dbg = psd
                detections_dbg = pd.concat([detections_dbg,events_df_psd])
                win_activity_dbg.append(win_activity)
                win_bsl_dbg.append(win_bsl)

        # The plugin outputs all the events from previous plugins and 
        # the events detected in this plugin on all the selected channels, 
        # however, the win_activity and win_bsl are only from the debug channel.
        cache = {}
        if config.is_dev: # Avoid save of the recording when not developping
            if dbg_chan_found==1:
                cache['detections'] = detections_dbg
            else:
                cache['detections'] = events_df
            cache['psd_data'] = psd_dbg
            cache['low_freq'] = low_freq
            cache['high_freq'] = high_freq
            self._cache_manager.write_mem_cache(self.identifier, cache)
            return {
                'events': events_df,
                'win_activity' : win_activity_dbg,
                'win_bsl'  : win_bsl_dbg
            }     
        else:
            return {
                'events': events_df,
                'win_activity' : "",
                'win_bsl'  : ""
            }                 


    def _add_spectral_events(self, events_df, event_group, event_name, detections, psd):
        """ 
            Add the spectral detections into the events_df as events named
            "event_name" with the channel label added in the dataframe (label saved in the psd dict).

            Parameters
            -----------
            events_df : pandas dataframe 
                List of events (each row is an event)
            event_group : string
                Event group.
            event_name : string
                Event name
            detections : ndarray of n_windows
                Events array, 0 means no event and 1 means an event.
            psd : dict
                Dict of the spectral information (channel specific)
                    sample_rate : sampling rate of the signal (used to STFT)
                    chan_label : current channel label                 
                    win_step : window step in sec
                    win_len : window length in sec
            Returns
            -----------  
            events_df : pandas dataframe
                List of events including previously detected events.
            events_df_psd : pandas dataframe
                List of events detected in the current instance.
        """
        # Create an event for each pair of starts and ends
        #   event_list is a list of events and its units are windows
        event_list = performance.bin_evt_to_lst(detections)

        # event_list is windows based
        #   events is in seconds because the win_step are in seconds
        #   warning : the duration of the event cannot be multiplied by win_dur
        #       imagine you have win_len=5s and win_step=1s and an event
        #       5 "step" window long, it would make the event duration
        #       5 win * 5 sec = 25 seconds long and only 
        #       9 seconds of data was taken into account 
        #       Taking dur*win_step+(win_len-win_step) means that the
        #       artefact will be as long as the data taken for the STFT.
        #       ex) win_len=5s and win_step=1s; 5 windows * 1s + 4s = 9 s
        win_step = psd['win_step']
        win_len = psd['win_len']
        fs = psd['sample_rate']
        channel = psd['chan_label']

        nsample_win = win_len*fs
        if not nsample_win.is_integer():
            # Compute the real win_len used
            if DEBUG:
                print("Warning : win_len {} is changed for {}".\
                    format(win_len, int(round(nsample_win))/fs))
            win_len = int(round(nsample_win))/fs

        nsample_step = win_step*fs
        if not nsample_step.is_integer():
            # Compute the real win_step used
            if DEBUG:
                print("Warning : win_step {} is changed for {}".\
                    format(win_step, int(round(nsample_step))/fs))
            win_step = int(round(nsample_step))/fs   

        events = [(psd['start_time']+start*win_step, dur*win_step+(win_len-win_step)) for start, dur in event_list]

        if len(events)>0:
            # dur*win_len when win_len>win_step can supperpose events
            # We re-create the events list to merge any suppoerposed events
            #   events is a list of events in secondes
            #   det_event_bin is a binary vector in samples
            det_event_bin = performance.evt_lst_to_bin(events, fs=fs)
            #   events is a list of events in secondes without supperposition
            events = performance.bin_evt_to_lst_sec(det_event_bin, fs=fs)

        # Add the event_name and the channel label to the events list
        events = [(event_group, event_name, start, dur, channel) for start, dur in events]

        # Create a pandas dataframe of events (each row is an event) for the current pds
        events_df_psd = manage_events.create_event_dataframe(events)
        # Events detected from other psds (channels) are also added to the df
        return (pd.concat([events_df,events_df_psd]), events_df_psd)


    def extract_psd_from_event(self, psd_data, psd_start, psd_end, fft_win_step_s, fft_win_len_s, event_start, event_dur):
        """
        The psd_data must contain the information for only one channel.
        Parameters :
            psd_data : 2D array
                psd of the signal [n_fft_win, n_freq_bin]
            psd_start : float
                start time in sec of the first fft window in psd_data.
            psd_end : float
                end time in sec of the last fft window in psd_data.
            fft_win_step_s : float
                window step in sec
            fft_win_len_s : float
                window length in sec
            event_start : float
                start time in sec of the psd
            event_dur : float
                duration in sec of the psd
        Return : 
            psd_data_sel : 2D array (n_fft_win, n_freq_bin)
                psd_data modified (truncated) to extract the samples linked to the event specified by event_start and event_dur
            psd_start_sel : 1D array (n_fft_win,)
                The start time in sec of each fft window returned
        """

        # Because of the discontinuity, the signal can start with an offset (second section)
        #   if the event starts before the signal, we cut the signal
        if (event_start <= psd_start) and ((event_start + event_dur) > psd_start):
            psd_start_sel_s = psd_start
        elif (event_start >= psd_start) and ((event_start + event_dur) <= psd_end):
            psd_start_sel_s = event_start
        else: 
            psd_start_sel_s = None
        #   if the event ends after the signal, we cut the signal
        if ((event_start + event_dur) > psd_end) and (event_start < psd_end):
            psd_end_sel_s = psd_end
        elif ((event_start + event_dur) <= psd_end) and (event_start >= psd_start):
            psd_end_sel_s = event_start + event_dur
        else:
            psd_end_sel_s = None
        
        if psd_start_sel_s is None or psd_end_sel_s is None:
            return np.empty(0), np.empty(0)

        psd_duration_sel_s = psd_end_sel_s - psd_start_sel_s

        # Define the first fft window from the psd_data to extract the event
        # ex. event_dur = 30 s, fft_win_step_s = 5 s
        # 6 windows are extracted
        offset_from_psd_start_s = psd_start_sel_s-psd_start
        first_fft_win = int( np.round(offset_from_psd_start_s / fft_win_step_s) )
        # We remove the last fft window length, because it is included in the psd information
        #    important when the fft_win_step is not the same as the fft_win_len
        last_fft_win = int( np.round(( (offset_from_psd_start_s + psd_duration_sel_s)-fft_win_len_s) / fft_win_step_s))
        # Because of the truncation, we make sure we have enough fft windows
        n_fft_win = (last_fft_win-first_fft_win)+1

        # Each new fft window represents + fft_win_step_s and the last fft window represents + fft_win_len_s
        # data_sel_len_s = (n_fft_win-1)*fft_win_step_s+fft_win_len_s 
        # expected_data_len_s = psd_duration_sel_s
        # if (not data_sel_len_s == expected_data_len_s):
        #     print(f'WARNING provided data length = {data_sel_len_s}, expected data length = {expected_data_len_s}')

        # The offset of the signal is removed to extract the event
        psd_data_sel = psd_data[first_fft_win:first_fft_win+n_fft_win] # the last fft window
        psd_start_sel = [psd_start_sel_s + (i-1)*fft_win_step_s for i in range(1, n_fft_win+1)]
        # Round the start time to the nearest second with 2 decimals
        psd_start_sel = np.round(np.array(psd_start_sel), 2)
        return psd_data_sel, psd_start_sel
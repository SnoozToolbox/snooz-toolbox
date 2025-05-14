"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from CEAMSModules.Stft import ts2windows as ts2w
from CEAMSModules.EventCompare import performance as perf

import numpy as np
import pandas as pd


DEBUG = True

def adp_compute(signal, pad_sec, threshold, above_thresh_det,\
        baseline_win_len, median_use, log10_data, fs, art_events=None):
                      
    """
    This function detects events based on absolute amplitude of the time series.
    An event is detected when activity goes above (if above_thresh_det=True)
    the threshold otherwise it's below the theshold.  The adaptive threshold 
    can be x times the baseline median value (if median_use=True) or 
    x times the standard deviation (if median_use=False) of the baseline.  
    When a z-score is used as threshold (x BSL STD), the PSD values can be 
    log10 transformed to make them more normally distributed.

    Parameters
    -----------
        signal        : narray
            The time series.
        pad_sec  : float
            The padding event (length in second) to add to the beginning and 
            the end of the originally detected event.
        threshold   : double
            The threshold to detect events. 
        above_thresh_det : bool
            True : Event is detected when activity exceeds the threshold. 
            False : Event is detected when activity goes below the threshold. 
        baseline_win_len : double
            The baseline window length in seconds. 
        median_use : bool
            The relative threshold is 'x times the baseline median' otherwise the 
            threshold is 'x times the baseline standard deviation'
        log10_data : bool
            Log10 transform the data if True. 
        fs : float
            Sampling rate (Hz)
        art_events : Pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])   
            (optional) Artefact events previously detected   

    Returns
    -----------  
        detection_bin : ndarray
            Events array, 0 means no event and 1 means an event (the size of the signal)
        detection_activity : ndarray
            Absolute amplitude of the signal.
        bsl_win : ndarray (or 2D array)
            median_use==True : Median absolute amplitude of the baseline.
            median_use==False : Mean and standard deviation of the baseline amplitude.
            row1: mean, row2: std.

    @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)

    Log : 
        2021-05-17 : first release, klacourse
    """
    #--------------------------------------------------------------------------
    # Extract the absolute ampltitude of the signal
    #--------------------------------------------------------------------------
    detection_activity = np.abs(signal)
    if log10_data:
        # To compute log10 : all data must be > than 0
        # Energy is always >= 0
        detection_activity = np.where(detection_activity==0,np.nan,detection_activity)
        detection_activity = np.log10(detection_activity)

    #--------------------------------------------------------------------------
    # Extract/compute the baseline information
    #--------------------------------------------------------------------------
    nsamples_bsl = int(round(baseline_win_len * fs))

    # To shape baseline windows without artifact as the activity window.
    # bsl_win_act : ndarray of n_windows (or [2 x n_windows])
    #     median_use==True : Median activity of the baseline window
    #     median_use==False : Mean and standard deviation of the baseline activity.
    #     row1: mean, row2: std.
    bsl_win = ts2w.shape_valid_bsl_as_act_win(detection_activity, \
        1/fs, 1/fs, nsamples_bsl, median_use, art_events)

    # Detection based on the baseline value of each window
    if above_thresh_det:
        if median_use:
            detection_win = detection_activity > (bsl_win * threshold)  
        else:
            detection_activity = (detection_activity-bsl_win[0,:]) / bsl_win[1,:]
            detection_win = detection_activity > threshold
    else:
        if median_use:
            detection_win = detection_activity < (bsl_win * threshold)
        else:
            detection_win_activity = (detection_activity-bsl_win[0,:]) / bsl_win[1,:]
            detection_win = detection_win_activity < threshold

    #--------------------------------------------------------------------------
    # Add padding to the event (original event can be only one sample long)
    #--------------------------------------------------------------------------
    # Convert the events array into a list of events with start and duration in samples. 
    # The array must contain only 0 and 1, 0 means no events and 1 means an event.
    event_list = perf.bin_evt_to_lst_sec(detection_win, fs=fs)
    # Add padding to both the beginning and the end of the original event
    event_list_pad = [(start-pad_sec, dur+pad_sec) for start, dur in event_list]
    # Convert the events list (start and duration) into a binary vector of samples,
    #  0 means no events and 1 means a event.
    detection_bin = perf.evt_lst_to_bin(event_list_pad, fs=fs)

    return detection_bin, detection_activity, bsl_win


def fix_compute(signal, pad_sec, threshold_val, above_thresh_det, fs):          
    """
        Function to detect events based on absolute amplitude signal.
        The detection window must respect a fixed threshold.
        Ex. above 200 µV to detect a high amplitude.

        Parameters
        -----------
            signal        : narray
                The time series.
            pad_sec  : float
                The padding event (length in second) to add to the beginning and 
                the end of the originally detected event.
            event_name  : string
                Event label.
            threshold_val : double
                The threshold to detect events.
            above_thresh_det : bool
                True : Event is detected when activity exceeds the threshold. 
                False : Event is detected when activity goes below the threshold. 
            fs : float
                Sampling rate (Hz)
        Returns
        -----------  
            det_event_bin   : ndarray
                Array of zeros and ones where zero means no event and one means an event.
            det_activity    : ndarray
                Absolute amplitude of the time series.

        @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)
    """
    #--------------------------------------------------------------------------
    # Extract the absolute ampltitude of the signal
    #--------------------------------------------------------------------------
    det_activity = np.abs(signal)

    #--------------------------------------------------------------------------
    # Detection based on the threshold_val
    #--------------------------------------------------------------------------
    if above_thresh_det:
        det_event_bin = det_activity > threshold_val
    else:
        det_event_bin = det_activity < threshold_val

    #--------------------------------------------------------------------------
    # Add padding to the event (original event can be only one sample long)
    #--------------------------------------------------------------------------
    # Convert the events array into a list of events with start and duration in samples. 
    # The array must contain only 0 and 1, 0 means no events and 1 means an event.
    event_list = perf.bin_evt_to_lst_sec(det_event_bin, fs=fs)

    if len(event_list)>0:
        # Add padding to both the beginning and the end of the original event
        event_list_pad = [(start-pad_sec, dur+pad_sec*2) for start, dur in event_list]
        # Convert the events list (start and duration) into a binary vector of samples,
        #  0 means no events and 1 means a event.
        det_event_bin_pad = perf.evt_lst_to_bin(event_list_pad, fs=fs)
    else:
        det_event_bin_pad = np.zeros(np.size(det_activity))

    return det_event_bin_pad, det_activity


def var_adp_compute(signal, win_len_sec, win_step_sec, threshold, above_thresh_det,\
        baseline_win_len, median_use, log10_data, fs, art_events=None):
                      
    """
    Function to detect events based on maximum amplitude variation in a narrow time windows. 
    An event is detected when activity goes above (if above_thresh_det=True)
    the threshold otherwise it's below the theshold.  The adaptive threshold 
    can be x times the baseline median value (if median_use=True) or 
    x times the standard deviation (if median_use=False) of the baseline.  
    When a z-score is used as threshold (x BSL STD), the PSD values can be 
    log10 transformed to make them more normally distributed.

    Parameters
    -----------
        signal          : narray
            The time series.
        win_len_sec     : string
            The window length (in second) used to compute the amplitude variation. 
        win_step_sec    : string
            The window step (in seconds) between two amplitude variation calculations.
        threshold       : double
            The threshold to detect events. 
        above_thresh_det : bool
            True : Event is detected when activity exceeds the threshold. 
            False : Event is detected when activity goes below the threshold. 
        baseline_win_len : double
            The baseline window length in seconds. 
        median_use      : bool
            The relative threshold is 'x times the baseline median' otherwise the 
            threshold is 'x times the baseline standard deviation'
        log10_data      : bool
            Log10 transform the data if True. 
        fs              : float
            Sampling rate (Hz)
        art_events      : Pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])   
            (optional) Artefact events previously detected   

    Returns
    -----------  
        det_bin_win : ndarray 
            Events array, 0 means no event and 1 means an event (each value represents a window).
        var_win_act : ndarray
            Maximum variation within each window.
        bsl_win : ndarray of n_windows (or [2 x n_windows])
            Baseline windows shaped to match the var_win_act.
            Each row includes the baseline information around the activitiy window.
    """
    #--------------------------------------------------------------------------
    # Convert sample by sample vector to a windows
    #--------------------------------------------------------------------------
    nsample_win = win_len_sec*fs
    if not nsample_win.is_integer():
        # Compute the real win_len used
        print("Warning : win_len_sec {} is changed for {}".format(win_len_sec, int(round(nsample_win))/fs))
        win_len_sec = int(round(nsample_win))/fs

    nsample_step = win_step_sec*fs
    if not nsample_step.is_integer():
        # Compute the real win_step used
        print("Warning : win_step_sec {} is changed for {}".format(win_step_sec, int(round(nsample_step))/fs))
        win_step_sec = int(round(nsample_step))/fs

    nsample_win = int(round(win_len_sec*fs))
    nsample_ovlp = int(round((win_len_sec-win_step_sec)*fs))

    # Shapes a 1-D array into 2D array of windows such as [nwindows x nsamples_per_win]
    win_activity = ts2w.compute_windows(signal, nsample_win, nsample_ovlp)

    #--------------------------------------------------------------------------
    # Compute the max variation per windows
    #--------------------------------------------------------------------------
    var_win_act = np.amax(win_activity, axis=-1)-np.amin(win_activity, axis=-1)

    if log10_data:
        # To compute log10 : all data must be > than 0
        # Energy is always >= 0
        var_win_act = np.where(var_win_act==0,np.nan,var_win_act)
        var_win_act = np.log10(var_win_act)

    #--------------------------------------------------------------------------
    # Extract/compute the baseline information
    #--------------------------------------------------------------------------
    nbaseline_win = int(baseline_win_len / win_len_sec) # int truncates

    # To shape baseline windows without artifact as the activity window.
    # bsl_win : ndarray of n_windows (or [2 x n_windows])
    #     Baseline windows shaped to match the detection_win_activity.
    #     Each row includes the baseline information around the activitiy window.
    # median_use==True : Median activity of the baseline window
    # median_use==False : Mean and standard deviation of the baseline activity
    # row1: mean, row2: std.
    bsl_win = ts2w.shape_valid_bsl_as_act_win(var_win_act, win_len_sec, \
        win_step_sec, nbaseline_win, median_use, art_events)

    # Detection based on the baseline value of each window
    if above_thresh_det:
        if median_use:
            det_bin_win = var_win_act > (bsl_win * threshold)  
        else:
            var_win_act = (var_win_act-bsl_win[0,:]) / bsl_win[1,:]
            det_bin_win = var_win_act > threshold
    else:
        if median_use:
            det_bin_win = var_win_act < (bsl_win * threshold)
        else:
            var_win_act = (var_win_act-bsl_win[0,:]) / bsl_win[1,:]
            det_bin_win = var_win_act < threshold

    return det_bin_win, var_win_act, bsl_win


def var_fix_compute(signal, win_len_sec, win_step_sec, threshold_val, above_thresh_det, fs):          
    """
        Function to detect events based on maximum amplitude variation in a 
        narrow time windows. The detection window must respect a fixed threshold.
        ex) below 6 µV to detect a flatline

        Parameters
        -----------
            signal        : narray
                The time series.
            win_len_sec : string
                The window length (in second) used to compute the amplitude variation. 
            win_step_sec : string
                The window step (in seconds) between two amplitude variation calculations.              
            event_name  : string
                Event label.
            threshold_val : double
                The threshold to detect events.
            above_thresh_det : bool
                True : Event is detected when activity exceeds the threshold. 
                False : Event is detected when activity goes below the threshold. 
            fs : float
                Sampling rate (Hz)
        Returns
        -----------  
            det_bin_win : ndarray 
                Events array, 0 means no event and 1 means an event (each value represents a window).
            var_win_act : ndarray
                Maximum variation within each window.

        @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)
    """
    #--------------------------------------------------------------------------
    # Convert sample by sample vector to a windows
    #--------------------------------------------------------------------------
    nsample_win = win_len_sec*fs
    if not nsample_win.is_integer():
        # Compute the real win_len used
        print("Warning : win_len_sec {} is changed for {}".format(win_len_sec, int(round(nsample_win))/fs))
        win_len_sec = int(round(nsample_win))/fs

    nsample_step = win_step_sec*fs
    if not nsample_step.is_integer():
        # Compute the real win_step used
        print("Warning : win_step_sec {} is changed for {}".format(win_step_sec, int(round(nsample_step))/fs))
        win_step_sec = int(round(nsample_step))/fs

    nsample_win = int(round(win_len_sec*fs))
    nsample_ovlp = int(round((win_len_sec-win_step_sec)*fs))

    # Shapes a 1-D array into 2D array of windows such as [nwindows x nsamples_per_win]
    win_activity = ts2w.compute_windows(signal, nsample_win, nsample_ovlp)

    #--------------------------------------------------------------------------
    # Compute the max variation per windows
    #--------------------------------------------------------------------------
    var_win_act = np.amax(win_activity, axis=-1)-np.amin(win_activity, axis=-1)

    #--------------------------------------------------------------------------
    # Detection based on the threshold_val
    #--------------------------------------------------------------------------
    if above_thresh_det:
        det_bin_win = var_win_act > threshold_val
    else:
        det_bin_win = var_win_act < threshold_val

    return det_bin_win, var_win_act


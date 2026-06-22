"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
import numpy as np
from CEAMSModules.Stft import ts2windows as ts2w

DEBUG = False

def adp_compute(psds, freq_bins, low_freq, high_freq, win_len, win_step, \
    threshold, above_thresh_det, baseline_win_len, median_use,\
         log10_data, art_events=None, bsl_low_freq=None, bsl_high_freq=None):
                      
    """
    This function detects events based on PSD (Power Spectral Density) information.
    An event is detected when activity goes above (if above_thresh_det=True)
    the threshold otherwise it's below the theshold.  The adaptive threshold 
    can be x times the baseline median value (if median_use=True) or 
    x times the standard deviation (if median_use=False) of the baseline.  
    When a z-score is used as threshold (x BSL STD), the PSD values are 
    log10 transformed to make them more normally distributed.

    Parameters
    -----------
        psds        : narray [n_windows x n_freq_bins]
            The power spectral density of all windows.
        freq_bins   : narray of n_freq_bins
            The frequencies of the bins within the psds.
        low_freq    : double
            The lower frequency of the bandwidth targeted by the detection.
        high_freq   : double
            The higher frequency of the bandwidth targeted by the detection.  
        win_len     : double
            The length of the detection windows on which the psds was done (in seconds).
        win_step    : double
            The step between the detection windows on which the psds was done (in seconds).                 
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
            Log10 transform the data if True. freq_binsund the curretn window.        
        art_events: Pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])   
            (optional) Artefact events previously detected   
        bsl_low_freq: double
            (optional) The low frequency (Hz) band denominator to compute relative power.
        bsl_high_freq: double
            (optional) The high frequency (Hz) band denominator to compute relative power.

    Returns
    -----------  
        detection_win           : ndarray of n_windows
            Events array, 0 means no event and 1 means an event.
        detection_win_activity  : ndarray of n_windows
            Spectral power in the frequency bins from low_freq to high_freq.
        bsl_win                 : ndarray of n_windows (or [2 x n_windows])
            median_use==True : Median spectral power of the baseline window (low_freq to high_freq).
            median_use==False : Mean and standard deviation of the baseline spectral power 
            (low_freq to high_freq). row1: mean, row2: std.

    @author: David Lévesque (david.levesque.cnmtl@ssss.gouv.qc.ca)
    @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)

    Log : 
        2021-04-22 : Output detection_win_activity and med_bsl_win, klacourse
        2021-05-10 : Added median_use and rename med_bsl_win for bsl_win, klacourse
        2021-07-12 : Added relative frequency band, klacourse
    """

    # Find the index relative to the frequency bins of interest
    # A low freq = 0 will return the first freq bins
    # An high freq higher than the last freq_bins will return the last freq_bins
    freq1_index = np.where(freq_bins >= low_freq)
    freq2_index = np.where(freq_bins <= high_freq)

    # For each detection window, sum the power spectral of the frequency band 
    # of interest.
    detection_win_activity = np.sum(psds[:,freq1_index[0][0]:freq2_index[-1][-1]],axis=-1)
    # The detector uses a relative power (not only absolute power)
    if not bsl_high_freq==None and bsl_high_freq>0:
        # Find the index relative to the frequency bins of interest
        freq1_index = np.where(freq_bins >= bsl_low_freq)
        freq2_index = np.where(freq_bins <= bsl_high_freq)        
        den_win_act = np.sum(psds[:,freq1_index[0][0]:freq2_index[-1][-1]],axis=-1)
        detection_win_activity = np.divide(detection_win_activity, den_win_act)

    # Number of win_len used for each baseline
    nbaseline_win = int(baseline_win_len / win_len) # int truncates

    if log10_data:
        # To compute log10 : all data must be > than 0
        # Energy is always >= 0
        detection_win_activity = np.where(detection_win_activity==0,np.nan,detection_win_activity)
        detection_win_activity = np.log10(detection_win_activity)

    # To shape baseline windows without artifact as the activity window.
    # bsl_win_act : ndarray of n_windows (or [2 x n_windows])
    #     median_use==True : Median activity of the baseline window
    #     median_use==False : Mean and standard deviation of the baseline activity.
    #     row1: mean, row2: std.
    bsl_win = ts2w.shape_valid_bsl_as_act_win(detection_win_activity, \
        win_len, win_step, nbaseline_win, median_use, art_events)

    # Detection based on the baseline value of each window
    if above_thresh_det:
        if median_use:
            detection_win = detection_win_activity > (bsl_win * threshold)  
        else:
            detection_win_activity = (detection_win_activity-bsl_win[0,:]) / bsl_win[1,:]
            detection_win = detection_win_activity > threshold
    else:
        if median_use:
            detection_win = detection_win_activity < (bsl_win * threshold)
        else:
            detection_win_activity = (detection_win_activity-bsl_win[0,:]) / bsl_win[1,:]
            detection_win = detection_win_activity < threshold

    return detection_win, detection_win_activity, bsl_win


def fix_compute(psds, freq_bins, low_freq, high_freq, threshold_val=None, \
    above_thresh_det=None, log10_transform=False, bsl_low_freq=None, bsl_high_freq=None):        
    """
        Function to detect events based on the spectrum information.
        The detection window must respect a fixed threshold.
        Ex. below 7 µV² to detect a flatline.
        Ex. above 3000 µV² to detect a high fixed power.

        Parameters
        -----------
            psds        : dict
                The power spectral density of all windows.
                p = psd['psd'], narray [n_windows x n_freq_bins]
                freq_bins = psd['freq_bins']; The frequencies of the bins within the psds
                win_len = psd['win_len']; The length of the detection windows on which the psds was done (in seconds)
                win_step = psd['win_step']; The step between the detection windows on which the psds was done (in seconds)
            event_name  : string
                Event label.
            low_freq    : double
                The lower frequency of the bandwidth targeted by the detection
            high_freq   : double
                The higher frequency of the bandwidth targeted by the detection
            threshold_val : double
                The threshold to detect events.
                (optional) if interrested only in the win_activity
            above_thresh_det : bool
                True : Event is detected when activity exceeds the threshold. 
                False : Event is detected when activity goes below the threshold. 
                (optional) if interrested only in the win_activity
            log10_transform : bool
                (optional) flag to log10 transform the data
            bsl_low_freq: double
                (optional) The low frequency (Hz) band denominator to compute relative power.
            bsl_high_freq: double
                (optional) The high frequency (Hz) band denominator to compute relative power.
                * Here the bsl refers to the background activity of the current window
                (could be activity from 4.5-30 Hz) not the 3 mins window around the current window.  

        Returns
        -----------  
            detection_win   : ndarray of n_windows
                Array of zeros and ones where zero means no event and one means an event.
            win_activity    : ndarray of n_windows
                Spectral power in the frequency bins from low_freq to high_freq.

        @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)
    Log : 
        2021-07-12 : Added relative frequency band, klacourse
    """

    # Find the index relative to the frequency bins of interest
    freq1_index = np.where(freq_bins >= low_freq)
    freq2_index = np.where(freq_bins <= high_freq)

    # For each detection window, sum the power spectral of the frequency band 
    # of interest.
    detection_win_activity = np.sum(psds[:,freq1_index[0][0]:freq2_index[-1][-1]],axis=-1)

    # The detector uses a relative power (not only absolute power)
    if not bsl_high_freq==None and bsl_high_freq>0:
        # Find the index relative to the frequency bins of interest
        freq1_index = np.where(freq_bins >= bsl_low_freq)
        freq2_index = np.where(freq_bins <= bsl_high_freq)        
        den_win_act = np.sum(psds[:,freq1_index[0][0]:freq2_index[-1][-1]],axis=-1)
        detection_win_activity = np.divide(detection_win_activity, den_win_act)

    # Compute the threshold based on the distribution of all the window activity
    if log10_transform:
        detection_win_activity = np.where(detection_win_activity==0,np.nan,detection_win_activity)
        detection_win_activity = np.log10(detection_win_activity)

    # Detection based on the threshold_val
    if (threshold_val is not None) and (above_thresh_det is not None):
        if above_thresh_det:
            detection_win = detection_win_activity > threshold_val
        else:
            detection_win = detection_win_activity < threshold_val
    else:
        detection_win = np.empty([0])

    return detection_win, detection_win_activity

"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
# -*- coding: utf-8 -*-
"""
Module to shape a 1-D wide array of samples into 2D array of windows of samples.
The compute function needs the inputs : 1-D array to convert, number of 
samples in the sliding window, number of samples that overlaps between 2 
windows and returns a 2-D array shaped as [nwin x nsample_win].  The return 
2D-array is a view in the memory, the real data is not duplicated in case of
overlap between windows, therefore it is not writable.
for more information see : 
https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.as_strided.html

Created on Wed Jan 27 15:24:41 2021

@author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)
"""
from CEAMSModules.EventCompare import performance as perf

import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time


def plot_windows(ts_signal, time_vect, title_fig):
    """ Open a figure and plot the time series signal. 
    
    Parameters
    -----------
    ts_signal       : any form that can be converted to an array. 
        This includes lists, tuples and ndarrays. 
        Array of data divided into windows [nwindow x nsamples_win]
    time_vect       : array like 
        Array of time samples in second
    title_fig       : string
        The title of the figure to plot the signal
    
    """
    # Ensure we have np.arrays, get outdtype
    ts_signal = np.asarray(ts_signal)
    time_vect = np.asarray(time_vect)
    plt.figure(figsize=(15, 35), dpi=80)
    if ts_signal.ndim == 1: 
        plt.plot(time_vect, ts_signal, 'b', linewidth=1.75, alpha=0.75)
    elif ts_signal.ndim == 2:
        for dim_index in range(ts_signal.shape[0]):
            plt.plot(time_vect, ts_signal[dim_index,0:], label = "window{}".format(dim_index))
    else:
        print("Reduce the dimension to plot the signal")
    plt.title(title_fig)
    plt.legend()
    plt.xlabel('sample index')
    plt.ylabel('amplitude of sample')        
    plt.grid(True,which='both',axis='both')
    plt.show()   


def compute_windows(data1D, nsample_win, nsample_ovlp, verbose=False):
    """ Shapes a 1-D array into 2D array of windows such as 
    [nwindown x nsamples_per_win]
    
    Parameters
    -----------
    data1D              : any form that can be converted to an 1-D array. 
        This includes lists, tuples and ndarrays. 
    nsample_win     : int
        Number of samples in the sliding window
    nsample_ovlp        : int
        Number of samples that overlaps between 2 windows
    verbose             : bool
        (optional) Flag to view figures of the process and print 
        informative messages in the console
    Returns
    -----------
    data2D       : an array of 2 dimensions
        This includes lists, tuples and ndarrays. 
        Array of data divided into windows as [nwindown x nsamples_per_win]
    
    """
    # Look at the def _fft_helper function from scipy
    # https://github.com/scipy/scipy/blob/9da1c4bad19f434e7e511a164e0a7af954a4202d/scipy/signal/spectral.py#L1869
    # https://stackoverflow.com/a/5568169
    # https://ajcr.net/stride-guide-part-1/
    # https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.as_strided.html
    
        # Some key array attributes were highlighted above in the diagram above. 
        #   In more detail:
        
        #   np.data returns a memoryview of the underlying buffer holding the twelve integers.
        #   np.itemsize is the number of bytes occupied by a single item in the buffer 
        #       (each item uses the same number of bytes).
        #   np.shape holds the length of each dimension of the array.
        #   np.strides holds the number of bytes needed to advance one value along each dimension. 

    data1D = np.asarray(data1D)
    # Make sure the signal is 1-D
    if data1D.ndim>1:
        data1D = np.squeeze(data1D)

    if nsample_ovlp>=nsample_win:
        raise ValueError('ts2windows.compute_windows : nsample_ovlp has to be smaller than nsample_win')

    # Number of samples to step between 2 windows
    nsample_step = nsample_win-nsample_ovlp
    
    # number of sample available to start a window
    # Some samples could be missing when using nsample_ovlp 
    nsample_avail = len(data1D)-nsample_win
    
    # number of windows
    tot_nwin = nsample_avail//nsample_step+1 # we keep an extra windows higher

    # Extract the wanted shape [tot_nwin x nsample_win]
    shape = (tot_nwin, nsample_win)
    if verbose == 1:
        print("data in windows dimension is {}\n"
              "\t which is {} windows of {} samples".\
                  format(shape, tot_nwin, nsample_win))
    # The number of bytes needed to advance one value along each dimension.
    # -> in windows dimension : nsample_step * 8 bytes
    # -> in samples dimension : 8 bytes        
    strides = (nsample_step*data1D.strides[-1], data1D.strides[-1])
    if verbose == 1:
        print("The strides are {} bytes\n"\
              "\t which is {} step samples per window x 8 bytes\n"\
              "\t and 1 sample x 8 bytes".format(strides, nsample_step))
            
    # # Create a view into the array with the given shape and strides.
    # return np.lib.stride_tricks.as_strided(data1D, shape=shape,
    #                                           strides=strides, writeable=False)
    # Create a view into the array with the given shape and strides.
    return np.lib.stride_tricks.as_strided(data1D, shape=shape, strides=strides)


def shape_valid_bsl_as_act_win( detection_win_activity, win_len, win_step, \
    nbaseline_win, median_use, art_events=None):
    """
        Function to shape baseline windows without artifact as the activity window.
        This fucntion helps to compute stats on clean windows around the current activity.

        Parameters
        -----------
        detection_win_activity   : ndarray of n_windows
            Detection activity (ex power or amplitude)
        win_len     : double
            The length of the detection windows.  
            How many seconds does each value of detection_win_activity represent?
            ex) the psds window length (in seconds).
        win_step    : double
            The step between the detection windows.
            How often are windows calculated (in seconds)?
        nbaseline_win : integer
            Number of win_len used for each baseline.  For each current activity window, 
            how many win_len we need to compute stats on the baseline around.
        median_use : bool
            Flag to use the adaptive threshold as x times the baseline median value, 
            otherwise it's x times the standard deviation of the baseline.
        art_events : Pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])   
            (optional) Artefact events previously detected

        Returns
        -----------  
        bsl_win_act : ndarray of n_windows (or [2 x n_windows])
            median_use==True : Median activity of the baseline window
            median_use==False : Mean and standard deviation of the baseline activity.
            row1: mean, row2: std.
            
    """

    VERBOSE = False

    nwindows = len(detection_win_activity)

    if VERBOSE:
        start_time_bsl = time.time()

    if isinstance(art_events,pd.DataFrame):    

        # Convert the previously detected artefact into detection window.
        # If any artefact occures within the window length the window is marked as artefacted
        # Any artefacted window is not included in the stats to compute the median baseline
        art_events_mod = art_events.copy(deep=True)
        # Make sure the artefact length is at least the window length
        duration_2mod = art_events.duration_sec < win_len
        art_events_mod.loc[duration_2mod,"duration_sec"] = win_len
        # Convert pandas artefact events into events in window
        art_events_lst, art_events_win = perf.evt_df_to_bin(art_events_mod, 1/win_step)
        # The length of art_events_bin depends when the last artefact occurs
        # zeros pad to have the same length as detection_win_activity
        # art_events_win can be longer than detection_win_activity if the last detection
        # was at the end and its length was < win_len
        npads = nwindows-len(art_events_win)
        if npads>=0:
            art_events_win = np.pad(art_events_win, (0, npads), 'constant', constant_values=(0, 0))
        else:
            art_events_win = art_events_win[0:nwindows]
        # Create the baseline index to select only artifact-free window
        possible_bsl = np.asarray(art_events_win==0).nonzero()
        possible_bsl = possible_bsl[0]
    else:
        possible_bsl = np.arange(nwindows)

    if len(possible_bsl)<nbaseline_win:
        # print("ERROR: miss baseline ({} windows and we need {})"\
        #     .format(len(possible_bsl),nbaseline_win))
        # Take all windows as baseline
        possible_bsl = np.arange(nwindows)
        nbaseline_win = nwindows

    if nwindows > 100000:
        #print('Too many windows {} to process to discard artefact'.format(nwindows))
        # Take all windows as baseline
        possible_bsl = np.arange(nwindows)        

    # If there is artefact, extract the closest baseline windows for each current activity window
    if len(possible_bsl) < nwindows:

        # --------------------------------
        # This part is heavy to run because of the loop
        # --------------------------------
        # tried comprehensions loop : it was longer
        # ex) dist_act_win_i = [np.abs(act_win_i-possible_bsl) for act_win_i in range(nwindows)]
        #
        # tried to compute the median directly in the for loop to avoid duplication of data : it was longer
        # ex) bsl_data_win = detection_win_activity[possible_bsl[bsl_idx[0:nbaseline_win]]]
        # ex) bsl_win_act[act_win_i] = np.median(bsl_data_win)
        #
        # Tried to use numpy methods : it was longer
        # Exemple
        # # det_win_act_2d = [1 x nwindows]
        # det_win_act_2d = np.expand_dims(detection_win_activity,axis=0)
        # # det_win_act_rep_bsl = [nwindows x nwindows] the first row is repeated nwindows times
        # det_win_act_rep_bsl = np.repeat(det_win_act_2d, nwindows, axis=0)
        # # bsl_data_win = [nwindows x nbaseline_win]
        # bsl_data_win = np.take_along_axis(det_win_act_rep_bsl, bsl_idx_all.astype(int), axis=1)


        # Baseline windows organized as the activity windows [n_windows x nbaseline_win]
        bsl_data_win = np.zeros((nwindows,nbaseline_win))
        # Find the closest nbaseline_win (ex 45) windows to the current act window 
        for act_win_i in range(nwindows):
            dist_act_win_i = np.abs(act_win_i-possible_bsl)
            bsl_idx = np.argpartition(dist_act_win_i, nbaseline_win)
            # Extract the "nbaseline_win" baseline values from the detection_win_activity for each activity window
            bsl_data_win[act_win_i,:] = detection_win_activity[possible_bsl[bsl_idx[0:nbaseline_win]]]    

    else:

        # Here the loop is avoid, we use stride

        # The detection windows at the beginning of the recording does not have any 
        # full baseline windows in the past, therefore the baseline is
        # calculated on a window happening mostly after the detection window.
        bsl_data_first = detection_win_activity[0:nbaseline_win]
        bsl_data_first = np.expand_dims(bsl_data_first, axis=0)
        # The same idea is applied to the last detection windows.
        bsl_data_last = detection_win_activity[-nbaseline_win:]
        bsl_data_last = np.expand_dims(bsl_data_last, axis=0)
        # Shape a 1-D wide array into 2D array of windows such as [nbaseline_win x nwin]
        bsl_data_mid = compute_windows(detection_win_activity, nbaseline_win, nbaseline_win - 1)
        # Array of the threshold to use for detection window
        nbsl_duplicate = int((nbaseline_win-1)//2)
        bsl_first_all = bsl_data_first
        for i_first in range(nbsl_duplicate-1):
            bsl_first_all = np.vstack((bsl_first_all,bsl_data_first))
        bsl_data_win = np.concatenate( (bsl_first_all, bsl_data_mid) )
        nbsl_duplicate = len(detection_win_activity)-len(bsl_data_win)
        bsl_last_all = bsl_data_last
        for i_last in range(nbsl_duplicate-1):
            bsl_last_all = np.vstack((bsl_last_all,bsl_data_last))        
        bsl_data_win = np.concatenate( (bsl_data_win, bsl_last_all), axis=0)

    # Compute the baseline statistic (across nbaseline_win values) for each baseline
    # Threshold unit is [ x BSL median ]
    if median_use:
        bsl_act_stats = np.median(bsl_data_win,axis=-1)
    # Threshold unit is [ x BSL STD ]
    else:
        std_bsl = np.nanstd(bsl_data_win,axis=-1)
        mean_bsl = np.nanmean(bsl_data_win,axis=-1)
        bsl_act_stats = np.vstack((mean_bsl,std_bsl))

    if VERBOSE:
        eval_time_bsl = time.time() - start_time_bsl
        feval_time = dt.timedelta(seconds=eval_time_bsl)
        print('Process time to compte bsl : {}'.format(feval_time))

    return bsl_act_stats


#------------------------------------------------------------------------------
# Main to test the class
#------------------------------------------------------------------------------            
if __name__ == "__main__":
    from scipy import signal # since the module should be used mostly without the 
                             # main, I decided to import scipy only here
    
    test_funct_num = 2

    if test_funct_num==1:
        verbose = 0             # to print informative message in the console
        ntest = 3               # number of tests

        tot_nsample = 200       # Total number of samples in the signal
        nsample_win = 10        # number of samples in the sliding window
        nsample_ovlp_init = [0,3,7]  # number of samples that overlaps between 2 windows
        # Trying nsample_ovlp=nsample_win raise an error

        for test_i in range(ntest):
            # number of samples that overlaps between 2 windows
            nsample_ovlp = nsample_ovlp_init[test_i]        
            
            print("\nTest#{} : {} total nb of samples, {} samples per win"\
                " and {} samples in overlap".\
                format(test_i, tot_nsample, nsample_win, nsample_ovlp))
                    
            # Creation of a 1-D signal (only incremental data to debug)
            ts_signal = np.asarray(range(tot_nsample))
        
            # Shape a 1-D wide array into 2D array of windows such as [nwin x nsample_win] 
            ts_in_win = compute_windows(ts_signal, nsample_win, nsample_ovlp, verbose=1)
        
            # Visual validation
            if verbose == 1:
                sample_index = np.asarray(range(0, nsample_win))
                plot_windows(ts_in_win, sample_index,\
                            "{} overlap, only incremental data".\
                                format(nsample_ovlp/nsample_win))
                # Window function
                win_func = signal.windows.get_window('hann',nsample_win)
                plot_windows(win_func * ts_in_win, sample_index, \
                "{} overlap, data windowed by hann".format(nsample_ovlp/nsample_win))
            
        # Additional test: remove the mean of each window
        nsample_ovlp = 5
        # Number of samples to step between 2 windows
        nsample_step = nsample_win-nsample_ovlp   

        print('\nRemove the mean of each window')
        print("{} total nb of samples, {} samples per win"\
            " and {} samples in overlap".\
            format( tot_nsample, nsample_win, nsample_ovlp))    
            
        # number of sample available to start a window
        nsample_avail = tot_nsample-nsample_win
        # number of windows
        tot_nwin = nsample_avail//nsample_step 
    
        # Shape a 1-D wide array into 2D array of windows such as [nwin x nsample_win] 
        ts_in_win = compute_windows(ts_signal, nsample_win, nsample_ovlp, verbose=1)    
        ts_nodc_win = ts_in_win - np.mean(ts_in_win, axis=-1, keepdims=True)
        print("data modified in windows dimension is {}\n"
            "\t which is {} windows of {} samples".\
                format(ts_nodc_win.shape, tot_nwin, nsample_win))
        
        print("The strides are {} bytes\n"\
            "\t which is {} samples per window x 8 bytes (the whole window was modified)\n"\
            "\t and 1 sample x 8 bytes".format(ts_nodc_win.strides, nsample_win))    
        
        # Visual validation
        if verbose == 1:
            plot_windows(ts_nodc_win, sample_index,"{} overlap, no dc".\
                                format(nsample_ovlp/nsample_win))

        print('\nTest a 3D time series')
        ts_signal = np.random.rand(1,1,tot_nsample)
        # Shape a 1-D wide array into 2D array of windows such as [nwin x nsample_win] 
        ts_in_win = compute_windows(ts_signal, nsample_win, nsample_ovlp, verbose=1)       


    else:
        # The second function od this module can be really long to run
        #
        # detection_win_activity   : ndarray of n_windows
        #     Spectral power in the frequency bins from low_freq to high_freq.
        # win_len     : double
        #     The length of the detection windows on which the psds was done (in seconds).
        # win_step    : double
        #     The step between the detection windows on which the psds was done (in seconds).  
        # nbaseline_win : integer
        #     Number of win_len used for each baseline.  For each current activity window, 
        #     how many win_len we need to compute stats on the baseline around.
        # art_events : Pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])   
        #     (optional) Artefact events previously detected
        
        
        # 70 000 takes 40 sec to run
        # 90 000 takes 1 m 10 sec to run
        n_windows = 100000 # real test is 750 000

        # Creation of a 1-D signal (only incremental data to debug)
        detection_win_activity = np.asarray(range(n_windows))
        detection_win_activity = detection_win_activity.astype(float)
        win_len = 0.05
        win_step = 0.05
        nbaseline_win = 600
        median_use = True
        # To specify the number of window (multiply it by the win len)
        dur1 = 100*win_len # 100 windows
        str2 = 500*win_len
        dur2 = 500*win_len
        str3 = 2000*win_len
        dur3 = 1000*win_len
        art_events = pd.DataFrame([['grp','test',0, dur1,'ch1'],['grp','test', str2, dur2,'ch1'],['grp','test', str3, dur3,'ch1']], \
            columns=['group', 'name','start_sec','duration_sec','channels'])

        bsl_win_act = shape_valid_bsl_as_act_win( detection_win_activity, win_len, win_step, \
            nbaseline_win, median_use, art_events=art_events)

        # plot_windows(detection_win_activity, np.asarray(range(n_windows)), 'det_win')
        # plot_windows(bsl_win_act, np.asarray(range(n_windows)), 'bsl_win')

# plt.close('all')
    
            
            
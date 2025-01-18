"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
# -*- coding: utf-8 -*-
"""
Module to compute the performance of estimated list of events against 
a gold standard list of events.  Performance is estimated as recall, precision, 
f1-score and kappa.  The performance can be computed by-sample or by-event.  

The pandas DataFrame must have these columns =
['group','name', 'start_sec', 'duration_sec','channels']

Created on Mon Feb  8 11:29:09 2021

@author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)
"""

import numpy as np
import pandas as pd

def performance_by_event(df_event_gs, df_event_est, fs, overlap_thresh=0.2, \
            gs_event_label=None, est_event_label=None):
    """
    Compute the performance by event of estimated events against the 
    gold standard (GS) events.  To resolve the less-than-perfect overlap and 
    multiple overlap problems between events (E) from GS and estimated 
    detections (D), a matching procedure is used to establish event-detection
    (ED) pairs.  Multiple overlaps are not allowed; only one D can be matched 
    with one E.  The best match is determined by the Jaccard index, which is 
    the intersection/union score between ED pairs.  Only ED pairs that exceeds 
    the overlap threshold are considered ED matches or valid detections (TP), 
    all unmatched E’s are FN, and all unmatched D’s are FP.
    * Since the function plays with events (with a duration) the tn and 
    threfore the kappa can not be computed.
    
    Parameters
    -----------
        df_event_gs : Pandas DataFrame ['group','name', 'start_sec', 'duration_sec','channels']
            Gold standard events list.
        df_event_est : Pandas DataFrame ['group','name', 'start_sec', 'duration_sec','channels']
            Estimated events list
        fs          : float
            Sampling frequency used to detect events.
        overlap_thresh : float, optional
            Overlap threshold, which is the needed Jaccard index to consider 
            an event-detection pair as a valid match (TP).
        gs_event_label : string, optional
            Event label to extract from the gs data frame, if None, all the events
            are extracted.
        est_event_label : string, optional
            Event label to extract from the estimated data frame, if None, all the events
            are extracted.            

    Returns
    -----------    
        fn : float
            False negative (event not detected)
        fp : float 
            False positive (wrong detection)
        tp : float
            True positive (event detected)
        precision : float
            TP / (TP + FP) (proportion of valid detection)
        recall : float
            TP / (TP + FN) (proportion of events found) 
        f1 : float
            2 * (Precision  * Recall) / (Precision  + Recall) 
          (harmonic mean of precision and recall)
        gs_evt_match : array
            1 when the event is detected
            0 when the event is missed
        est_evt_match : array
            1 when the detection is valid
            0 when the detection is a false positive

    Usage
    -----------
    fn, fp, tp, precision, recall, f1, gs_evt_match, est_evt_match = \
        performance_by_event(df_event_gs, df_event_est, gs_event_label, est_event_label)

    """
    # Gold standard : Convert the events dataframe into a binary events vector
    gs_event_lst, gs_bin_events = evt_df_to_bin(df_event_gs, fs, \
                                event_label=gs_event_label)
    # Estimated event : Convert the events dataframe into a binary events vector
    est_event_lst, est_bin_events = evt_df_to_bin(df_event_est, fs, \
                                event_label=est_event_label)
    
    # zeros pad to have the same length
    npads = len(gs_bin_events)-len(est_bin_events)
    if npads<0:
        gs_bin_events = np.pad(gs_bin_events, (0, abs(npads)), 'constant', \
                               constant_values=(0, 0))
    elif npads>0:
        est_bin_events = np.pad(est_bin_events, (0, npads), 'constant', \
                                constant_values=(0, 0))
    
    # Detection end in sample
    if len(est_event_lst)>0:
        est_event_end = est_event_lst[:,0]+est_event_lst[:,1]
    else:
        est_event_end = []
    
    # Compute and return the performance by event
    # Pre-allocate the array to store the ED pair match
    gs_evt_match = np.zeros(len(gs_event_lst))
    est_evt_match = np.zeros(len(est_event_lst))
    # For each GS event, look for the best ED match if any
    for gs_evt_i in range(len(gs_event_lst)):
        # If there is a detection during the gs event
        gs_start_i = int(gs_event_lst[gs_evt_i,0])
        gs_end_i = int(gs_start_i + gs_event_lst[gs_evt_i,1])
        if sum(est_bin_events[gs_start_i:gs_end_i])>0:
            # for a detection D to intersect with an GS event E
            #   D_end >= E_start && D_start =< E_end
            # detection index which intercept the gs event
            est_intersect = (est_event_end >= gs_start_i) & \
                (est_event_lst[:,0] <= gs_end_i)
            est_start = est_event_lst[est_intersect,0]
            est_end = est_event_end[est_intersect]
            # For each detection that intercept the gs event
            jaccord_array = np.zeros(len(est_start))
            for d_i in range(len(est_start)):
                # Compute the jaccord_index
                jaccord_array[d_i] = _jaccord_index([gs_start_i,gs_end_i],\
                                                [int(est_start[d_i]),int(est_end[d_i])])
            # Only one ED pair: Evaluate the overlap threshold on the highest jaccord index
            if jaccord_array[jaccord_array.argmax()]>overlap_thresh:
                # make sure the detection was not already an ED pair
                est_end_sl = est_end[jaccord_array.argmax()]
                if np.any(est_evt_match[est_event_end==est_end_sl]) == 0:
                    gs_evt_match[gs_evt_i]=1
                    est_evt_match[est_event_end==est_end[jaccord_array.argmax()]]=1
                # else no ED pair match
            # else, no ED pair match
        # else no ED pair match
        # tp = sum(gs_evt_match)
        # if tp != sum(est_evt_match):
        #     print('Coding error, the TP should be equal to the ED pair matches')
    
    tp = int(sum(gs_evt_match))
    if tp != sum(est_evt_match):
        print('Coding error, the TP should be equal to the ED pair matches')
    fn = int(sum(gs_evt_match==0))
    fp = int(sum(est_evt_match==0))
    
    if tp==0:
        precision = 0
        recall = 0
        f1 = 0
    else:
        # Performance metrics
        precision = round(tp/(tp+fp),ndigits=2)
        recall = round(tp/(tp+fn),ndigits=2) # Sensitivity, Hit Rate
        if precision==0 and recall==0:
            f1 = 0
        else:
            f1 = round(2 * (precision * recall) / (precision + recall),ndigits=2)    
    return fn, fp, tp, precision, recall, f1, gs_evt_match, est_evt_match


def compute_longest_est(gs_event_lst, gs_bin_events, df_event_est, fs):
    """
    Find the longest estimated event (df_event_est) included in each Gold Standard
    event (gs_event_lst, gs_bin_events).  Here the jaccord index is not used,
    the selection is based on the duration only.  The same event could be chosen 
    more than once. The objective is to add a group and a name to each non concurrent event.

    * This function is writen to merge without concurrent events 2 lists of events.
    gs_event_lst are the events without concurrent.
    df_event_est are the union list of all the events.

    Parameters
    -----------
        gs_event_lst : list
            Numerical values of the events listed as start(sample) and duration(sample)
        gs_bin_events : array
            Binary events vector, 0 means no events and 1 means a event. 
        df_event_est : Pandas DataFrame ['group','name', 'start_sec', 'duration_sec','channels']
            Estimated events list
        fs : float
            Sampling frequency in Hz.

    Returns
    -----------   
        gs_longest_est : nparray [n gs events x 2]
            0: longest etimated event index
            1: duration 
    """
    # Estimated event : Convert the events dataframe into a binary events vector
    est_event_lst, est_bin_events = evt_df_to_bin(df_event_est, fs)
    
    # zeros pad to have the same length
    npads = len(gs_bin_events)-len(est_bin_events)
    if npads<0:
        gs_bin_events = np.pad(gs_bin_events, (0, abs(npads)), 'constant', \
                               constant_values=(0, 0))
    elif npads>0:
        est_bin_events = np.pad(est_bin_events, (0, npads), 'constant', \
                                constant_values=(0, 0))
    
    # gs_longest_est : nparray [n gs events x 2]
    #   0: the longest etimated event index
    #   1: duration
    gs_longest_est = np.zeros((len(gs_event_lst),2))

    # Detection end in sample
    est_event_end = est_event_lst[:,0]+est_event_lst[:,1]
    
    # For each GS event, look for the ED match if any
    for gs_evt_i in range(len(gs_event_lst)):
        # If there is a detection during the gs event
        gs_start_i = gs_event_lst[gs_evt_i,0]
        gs_end_i = gs_start_i + gs_event_lst[gs_evt_i,1]
        if sum(est_bin_events[gs_start_i:gs_end_i])>0:
            # for a detection D to intersect with an GS event E
            #   D_end >= E_start && D_start =< E_end
            # detection index which intercept the gs event
            est_intersect = (est_event_end >= gs_start_i) & \
                (est_event_lst[:,0] <= gs_end_i)
            # Find the max duration of grouped events
                # all muscular events included in the current GS event are grouped
                # to sum the total duration
            cur_est_df = df_event_est[est_intersect]
            event_name_lst = cur_est_df['name']
            unique_name = event_name_lst.unique()
            dur_all = []
            for i_name in unique_name:
                # Sum the duration for each event type
                dur_all.append(cur_est_df[cur_est_df['name']==i_name].duration_sec.sum())
            # gs_longest_est is used to select the right event name
            # the first occurrence of the event is selected (even if the sum of all durations is used)
            longest_evt_name = unique_name[np.argmax(dur_all)]
            longest_evt_index = cur_est_df[cur_est_df.name==longest_evt_name].first_valid_index()
            # Store the longest detection, its index and its duration
            gs_longest_est[gs_evt_i,0] = longest_evt_index  
            gs_longest_est[gs_evt_i,1] = np.max(dur_all)
           
        else:
            gs_longest_est[gs_evt_i,:] = np.NaN

    return gs_longest_est

        
def _jaccord_index(event, detection):
    """
    Compute the jaccord index for the event and the detection.
    event and detection are a list of 2 values, the start and the end in samples.
    """
    # Pad the binary event to cover both length
    min_start = min((event[0],detection[0]))
    max_end = max((event[1],detection[1]))
    event = np.asarray(event)-min_start
    detection = np.asarray(detection)-min_start
    evt_pad = np.zeros(max_end-min_start)
    evt_pad[event[0]:event[1]]=1        
    det_pad = np.zeros(max_end-min_start)
    det_pad[detection[0]:detection[1]]=1

    # Compute the intersection between event and detection
    intersect = sum(evt_pad == det_pad)
    # Compute the union of the event and detection
    union = len(evt_pad)
    # Return the jaccord index  
    return intersect/union


def performance_by_sample(df_event_gs, df_event_est, fs, gs_event_label=None, \
        est_event_label=None):
    """
    Compute the performance by sample of estimated events against the 
    gold standard events.  The sampling frequency specifies time domain resolution
    to evaluate the detection.  Ideally, the fs used to detect the events should 
    be provided.  If the Gold standard detection was not made with the same fs
    than the estimated events ones, the lowest fs should be provided.
    
    Parameters
    -----------
    df_event_gs : Pandas DataFrame ['group','name', 'start_sec', 'duration_sec','channels']
        Gold standard events list
    df_event_est : Pandas DataFrame ['group','name', 'start_sec', 'duration_sec','channels']
        Estimated events list
    fs          : float
        Sampling frequency used to detect events.
    gs_event_label : string, optional
        Event label to extract from the gs data frame, if None, all the events
        are extracted.
    est_event_label : string, optional
        Event label to extract from the estimated data frame, if None, all the events
        are extracted.     
       
    Returns
    -----------    
    fn : float
        False negative (event not detected)
    fp : float 
        False positive (wrong detection)
    tp : float
        True positive (event detected)
    tn : float
        True positive (correct non-detection)
    precision : float
        TP / (TP + FP) (proportion of valid detection)
    recall : float
        TP / (TP + FN) (proportion of events found) 
    f1 : float
        2 * (Precision  * Recall) / (Precision  + Recall) 
      (harmonic mean of precision and recall)
    kappa : float
        conservative agreement because the expected agreement is removed from the score
    Usage
    -----------
    fn, fp, tp, tn, precision, recall, f1, kappa, specificity, npv, accuracy\
         = performance_by_sample(df_event_gs, df_event_est, gs_event_label, est_event_label)
    """    
    # Gold standard : Convert the events dataframe into a binary events vector
    gs_event_lst, gs_bin_events = evt_df_to_bin(df_event_gs, fs, \
                                    event_label=gs_event_label)
    # Estimated event : Convert the events dataframe into a binary events vector
    est_event_lst, est_bin_events = evt_df_to_bin(df_event_est, fs, \
                                    event_label=est_event_label)
    # Compute and return the performance
    return _perf_by_sample_on_bin(gs_bin_events, est_bin_events)


def evt_df_to_bin(df_event, fs, event_label=None):
    """
    Convert the events dataframe (name, start and duration) into a event list
    and a binary event vector of samples where 0 means no events and 1 means a event.     

    Parameters
    -----------
    df_event : Pandas DataFrame ['group','name', 'start_sec', 'duration_sec','channels']
        Events list
    fs          : float
        Sampling frequency used to detect events.
    event_label : string, optional
        Event label to extract from the data frame, if None, all the events
        are extracted.   

    Returns
    -----------    
    event_lst : list
        Numerical values of the events listed as start(sample) and duration(sample)
    bin_events : array
        Binary events vector, 0 means no events and 1 means a event. 

    Usage
    -----------
    event_lst, bin_events = evt_df_to_bin(df_event, fs, event_label)
    """
    # Extract the specific event label
    if event_label != None:
        df_event = df_event[df_event.name == event_label]
        
    if df_event.empty:
        bin_events = np.zeros(1)
        event_lst = []
    else:
        # Extract the start and duration in sec
        event_lst = df_event[['start_sec','duration_sec']].values
        # Convert the event listed as start and duration into binary event vector
        bin_events = evt_lst_to_bin(event_lst, fs)
        bin_events = bin_events.astype(int)
        # Extract the start and duration in sample
        event_lst_sample = (event_lst * fs).astype(float)
        event_lst = np.round(event_lst_sample)
        
    return event_lst, bin_events


def _perf_by_sample_on_bin(gs_bin_events, est_bin_events):
    """
    Compute the performance by samples of estimated events against the gold 
    standard events from binary event vectors.
    """
    
    # Ensure we have np.arrays, get outdtype
    gs_bin_events = np.asarray(gs_bin_events)
    est_bin_events = np.asarray(est_bin_events)
         
    # zeros pad to have the same length
    npads = len(gs_bin_events)-len(est_bin_events)
    if npads<0:
        gs_bin_events = np.pad(gs_bin_events, (0, abs(npads)), 'constant', constant_values=(0, 0))
    elif npads>0:
        est_bin_events = np.pad(est_bin_events, (0, npads), 'constant', constant_values=(0, 0))
    
    # Calculate FN, FP, TN and TP
    fn = int(np.sum( (gs_bin_events==1) & (est_bin_events==0) ))
    fp = int(np.sum( (gs_bin_events==0) & (est_bin_events==1) ))
    tp = int(np.sum( (gs_bin_events==1) & (est_bin_events==1) ))
    tn = int(np.sum( (gs_bin_events==0) & (est_bin_events==0) ))
    
    # Performance metrics
    precision, recall, f1, kappa, specificity, npv, ppv, accuracy = \
        compute_performance_from_stats(fn, fp, tp, tn)
    
    return fn, fp, tp, tn, precision, recall, f1, kappa, specificity, npv, ppv, accuracy


def compute_performance_from_stats(fn, fp, tp, tn):
    """
    Compute recall, precision, f1-score and kappa scores based on 
    False Negative (fn), False Positive (fp), True Positive (tp) and True Negative (tn). 
    """
    if tp==0:
        precision=0
        recall=0
        ppv=0
    else:
        # Performance metrics
        precision = round(tp/(tp+fp),ndigits=2)
        recall = round(tp/(tp+fn),ndigits=2) # Sensitivity, Hit Rate
        ppv = round(tp/(tp+fp),ndigits=2)
    if precision==0 and recall==0:
        f1 = 0
    else:
        f1 = round(2 * (precision * recall) / (precision + recall),ndigits=2)
    # Kappa
        # Wiki scale
        # values < 0 as indicating no agreement and 
        # 0–0.20 as slight, 
        # 0.21–0.40 as fair, 
        # 0.41–0.60 as moderate, 
        # 0.61–0.80 as substantial, and 
        # 0.81–1 as almost perfect agreement.    
    kappa = (2 * (tp*tn - fn*fp))/((tp + fp)*(fp + tn) + (tp + fn)*(fn + tn))
    kappa = round(kappa,ndigits=2)

    if tn==0:
        specificity = 0
        npv = 0
    else:
        specificity = round(tn/(tn+fp),ndigits=2)
        npv = round(tn/(tn+fn),ndigits=2)
    
    accuracy = round((tp+tn)/(tp+tn+fp+fn),ndigits=2)

    return precision, recall, f1, kappa, specificity, npv, ppv, accuracy


def evt_lst_to_bin(events_sec, fs):
    """
    Convert the events list (start and duration) into a binary vector of samples, 
    0 means no events and 1 means a event. 
    
    Parameters
    -----------
        events_sec : array like 2 dimensions
            list of start events and duration in seconds
        fs : sampling frequency (Hz)
    Returns
    -----------    
        bin_event_array : array
            events detection in samples, 0 means no events and 1 means a event. 
    """
    # Ensure we have np.arrays, get outdtype
    events_sec = np.asarray(events_sec)
    
    if len(events_sec)>0:
        # extract the last event to compute the minimum number of samples needed 
        # to generate the array
        nsamples = int(np.round( (events_sec[-1,0]+events_sec[-1,1]) *fs ))
        # Preallocation
        bin_event_array = np.zeros(nsamples)
        for evt_i in range(len(events_sec)):
            start_i = int(np.round(events_sec[evt_i,0]*fs))
            end_i = start_i + int(np.round(events_sec[evt_i,1]*fs))
            bin_event_array[start_i:end_i]=1
    else:
        bin_event_array = 0 
    
    return bin_event_array


def bin_evt_to_lst(bin_event_array):
    """
    Convert the events array into a list of events with start and duration in samples.
    The array must contain only 0 and 1, 0 means no events and 1 means a event. 
    
    Parameters
    -----------
        bin_event_array : array
            events detection in samples, 0 means no events and 1 means a event.     
    Returns
    -----------    
        events : numpy array of 2 dimensions
            start events and duration of events in samples
    """    
    # Ensure we have np.arrays, get outdtype
    bin_event_array = np.asarray(bin_event_array)    
    
    # Convert to integer (especially when it is an array of np.bool)
    bin_event_array = bin_event_array.astype(int) 
    
    if bin_event_array.size>1:
        # Make sure bin_event_array includes only 0 or 1
        if ( (np.sum(bin_event_array == 0) + np.sum(bin_event_array == 1)) != len(bin_event_array) ):
            raise ValueError('bin_event_array must includes only 0 or 1')
        
        # Find the edges
        if len(bin_event_array)>1:
            edge = bin_event_array[0:-1]-bin_event_array[1:]
            start_evt = np.asarray(np.where(edge==-1)[0]) + 1
            end_evt = np.asarray(np.where(edge==1)[0])
            
            # Add a start if the event array begins with during an event
            if bin_event_array[0]==1:
                start_evt = np.concatenate( ([0], start_evt) )
            # Add a end if the event array ends during an event
            if bin_event_array[-1]==1:
                end_evt = np.concatenate( (end_evt, [len(bin_event_array)-1]) )
                
            # Duration
            dur_evt = end_evt+1 - start_evt
            
            # Create an np.array of 2 dimensions
            events = np.zeros((len(start_evt),2))
            events[:,0] = start_evt
            events[:,1] = dur_evt
            # Convert the sample index into np.int64
            events = np.round(events).astype(int)
            #events = np.floor(events).astype(int)

    elif bin_event_array==1:
        # Create an np.array of 2 dimensions
        events = np.zeros((1,2))
        events[:,0] = 0
        events[:,1] = 1
    else:
        events = np.zeros((1,2))
    
    return events
    
    

def bin_evt_to_lst_sec(bin_event_array, fs):
    """
    Convert the events array into a list of events with start and duration in sec.
    
    Parameters
    -----------
        bin_event_array : array
            events detection in samples, 0 means no events and 1 means a event.    
        fs : sampling frequency (Hz)
 
    Returns
    -----------    
        events : numpy array of 2 dimensions
            start events and duration of events in second
    """      
    return bin_evt_to_lst(bin_event_array) / fs

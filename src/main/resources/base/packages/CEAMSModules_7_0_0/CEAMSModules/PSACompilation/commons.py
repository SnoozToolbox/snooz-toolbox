"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

import numpy as np
from commons.NodeRuntimeException import NodeRuntimeException

def get_attribute(dicts, attr_to_get, attr_to_test=None, value_to_test=None):
    """
    Get or Group in a list the desired attribute in the list of dicts

    Parameters
    -----------
        dicts : a list of dict
        attr_to_get : string, the desired attribute i.e. "psd"., None to get a list of dicts
        attr_to_test : string, attribute to evaluate. i.e. "chan_label". 
                If None, just the desired attribute is get from list.
        value_to_test : string, condition to test. i.e. "EEG F3"

    Returns
    -----------    
        attribute_list : a list of attribute or the list of the selected dicts

    Usage
    -----------
        To extract the list of channels from the dicts:
            channel_list = get_attribute(PSD, 'chan_label')
        To extract the list of sample_rate from the dicts:
            fs_list = get_attribute(PSD, 'sample_rate')
        To extract the list of psd data that the 'chan_label' is 'EEG F3':
            dict_chan = = get_attribute(PSD, 'psd', 'chan_label', 'EEG F3')
        To extract the list of dicts that the 'chan_label' is 'EEG F3':
        #   ex) psd_lst = get_attribute(PSD, None, 'chan_label', 'EEG F3')
        elif (not group_by == None) and (attr == None) and (value_to_test == None):
            condition = np.vstack([getattr(signal, group_by) for signal in signals])
            unq_condition = np.unique(condition)
            attribute_list = np.array([[signal for signal in signals if getattr(signal, group_by) == cond] for cond in unq_condition])
    """
    if attr_to_test == None and not attr_to_get == None:
        attribute_list = np.array([item_list.get(attr_to_get) for item_list in dicts])
    elif (not attr_to_get == None) and (not attr_to_test == None) and (not value_to_test == None):
        attribute_list = np.vstack([item_list.get(attr_to_get) for item_list in dicts if item_list.get(attr_to_test)==value_to_test])
    elif (attr_to_get == None) and (not attr_to_test == None) and (not value_to_test == None):
        attribute_list = [item_list for item_list in dicts if item_list.get(attr_to_test)==value_to_test]
    else:
        attribute_list = dicts
    return attribute_list


# Extract the channel information
def get_channel_info(PSD, channel):
    fs_chan = get_attribute(PSD, 'sample_rate', 'chan_label', channel)
    channel_info_param = {}
    channel_info_param['channel_label']=channel
    channel_info_param['channel_fs']=fs_chan[0][0]
    fs_chan = fs_chan[0][0]
    return channel_info_param, fs_chan


# To select the artefact events according to artefact groups and names.
# Generate the artefact info dict to write. 
def get_PSD_info(identifier, PSD, channel):
    # Make sure there are only one window definition for the current channel of the current recording
    fft_win_length_s = np.unique(get_attribute(PSD, 'win_len', 'chan_label', channel))
    fft_step_length_s = np.unique(get_attribute(PSD, 'win_step', 'chan_label', channel))
    if len(fft_win_length_s)>1:
        raise NodeRuntimeException(identifier, "win_len", \
            f"PSACompilation : FFTs computed on different windows length definition")
    if len(fft_step_length_s)>1:
        raise NodeRuntimeException(identifier, "win_step", \
            f"PSACompilation : FFTs computed on different step windows definition")
    # Extract the PSD definition
    PSD_info_params={}
    PSD_info_params['fft_win_sec'] = fft_win_length_s[0]
    PSD_info_params['fft_step_sec'] = fft_step_length_s[0]
    return PSD_info_params


# Extract psd for the current channel
def get_PSD_attribute_chan(identifier, PSD, channel, extract_data=False):
    # Extract psd for the current channel
    freq_bin_chan = get_attribute(PSD, 'freq_bins', 'chan_label', channel)
    psd_start_time = get_attribute(PSD, 'start_time', 'chan_label', channel)
    psd_end_time = get_attribute(PSD, 'end_time', 'chan_label', channel)
    if extract_data:
        psd_chan = get_attribute(PSD, 'psd', 'chan_label', channel)

    # Make sure the frequency bins are unique though the recording
    freq_bin_temp = freq_bin_chan[0]
    freq_bin_unique = np.unique(freq_bin_chan)
    if len(freq_bin_temp)==len(freq_bin_unique):
        if not (freq_bin_temp==freq_bin_unique).all():
            raise NodeRuntimeException(identifier, "freq_bins", \
                f"PSACompilation : the freq_bins are not unique through the recording")
    else:
        raise NodeRuntimeException(identifier, "freq_bins", \
            f"PSACompilation : the freq_bins are not unique through the recording")
    psd_start_time = psd_start_time.flatten()
    psd_end_time = psd_end_time.flatten()
    if extract_data:
        return freq_bin_unique, psd_start_time, psd_end_time, psd_chan
    else:
        return freq_bin_unique, psd_start_time, psd_end_time


# Extract psd for the current channel
def get_PSD_attribute_chan_stage(identifier, PSD, channel, sleep_stages):
    """
    Parameters
    -----------
        PSD : list of dicts
        channel : str
        sleep_stages : pd.DataFrame
            list of sleep stages
    Return
    -----------
        freq_bin_chan is an [1 x n_freq_bins] 
          frequency bins for the PSD.
        psd_start_time is an [1 x n_fft_wins] 
          The start time of each fft window.
        psd_stage is [1 x n_fft_wins]
          The sleep stage of each fft window.
        psd_data is an [n_fft_wins x n_freq_bins] 
          The PSD data of each fft window.
    """
    # Extract psd for the current channel
    #
        # If the PSD is run on the whole recording
        #  psd_start_time.shape = (1,1)
        #  psd_chan.shape = (n_fft_win, n_freq_bins)
        #  sleep_stages.shape = (n_epochs, 1)

        # If the PSD is run on splitted epochs
        #  psd_start_time.shape = (n_epochs, 1)
        #  psd_chan.shape = (n_fft_win, n_freq_bins)
        #  sleep_stages.shape = (n_epochs, 1)

    freq_bin_chan = get_attribute(PSD, 'freq_bins', 'chan_label', channel)
    psd_start_time = get_attribute(PSD, 'start_time', 'chan_label', channel)
    psd_end_time = get_attribute(PSD, 'end_time', 'chan_label', channel)

    if len(psd_start_time)==len(sleep_stages):
        psd_splitted = True
    else:
        psd_splitted = False

    # Make sure the frequency bins are unique through the recording
    freq_bin_temp = freq_bin_chan[0]
    freq_bin_unique = np.unique(freq_bin_chan)
    if len(freq_bin_temp)==len(freq_bin_unique):
        if not (freq_bin_temp==freq_bin_unique).all():
            raise NodeRuntimeException(identifier, "freq_bins", \
                f"PSACompilation : the freq_bins are not unique through the recording")
    else:
        raise NodeRuntimeException(identifier, "freq_bins", \
            f"PSACompilation : the freq_bins are not unique through the recording")
    
    # If the freq_bin is unique, the fft_win and fft_step are also unique
    fft_len_s = np.unique(get_attribute(PSD, 'win_len', 'chan_label', channel))[0]
    fft_step_s = np.unique(get_attribute(PSD, 'win_step', 'chan_label', channel))[0]

    # Convert the psd_start_time and psd_end_time array into float 
    #   (to allow the rouding when they are integer)
    #   (important to locate events with non integer sampling rate)
    psd_start_time = psd_start_time.flatten()
    psd_end_time = psd_end_time.flatten()
    psd_start_time = psd_start_time.astype(float)
    psd_start_time = np.around(psd_start_time, 2)
    psd_end_time = psd_end_time.astype(float)
    psd_end_time = np.around(psd_end_time, 2)

    # Extract the sleep stages information
    stage_start_all = sleep_stages['start_sec'].to_numpy()
    stage_start_all = stage_start_all.astype(float)
    stage_start_all = np.around(stage_start_all, 2)
    stage_duration_all = sleep_stages['duration_sec'].to_numpy()
    stage_duration_all = stage_duration_all.astype(float)
    stage_duration_all = np.around(stage_duration_all, 2)
    stage_name_all = sleep_stages['name'].to_numpy()

    # Generate the start time and the stage for each fft window
    if psd_splitted: # When the STFT has been run on data splittted in epochs
        psd_values_chan = get_attribute(PSD, 'psd', 'chan_label', channel)
        psd_stage = []
        for start_time, end_time in zip(psd_start_time, psd_end_time):
            stage_sel_arr = (stage_start_all<end_time) & ((stage_start_all+stage_duration_all)>start_time)
            if any(stage_sel_arr):
                cur_stage = stage_name_all[stage_sel_arr]
                psd_stage.append(cur_stage[0])
            else:
                psd_stage.append(np.nan)
        # Repeat the start time and stage for each fft window of the same epoch
        n_epochs = len(psd_start_time)
        n_fft_wins = len(psd_values_chan)
        n_fft_epoch = n_fft_wins/n_epochs
        psd_start = np.repeat(psd_start_time, n_fft_epoch)
        psd_stage = np.repeat(stage_name_all, n_fft_epoch)

    else: # When the STFT has been run on the whole recording
        psd_chan_lst = get_attribute(PSD, None, 'chan_label', channel)
        n_signals = len(psd_chan_lst)
        psd_stage = np.empty(0)
        psd_values_chan = np.empty(0)
        psd_start = np.empty(0)
        # The user usually select specific sleep stages, so the psd data will be truncated
        for stage, stage_start, stage_dur in zip(stage_name_all, stage_start_all, stage_duration_all):
            # For each continuous bout
            for i in range(n_signals): # important for discontinuity
                # Extract the psd values data for the current stage
                psd_values_current, psd_start_current = extract_psd_from_event(\
                    psd_chan_lst[i]['psd'], psd_start_time[i], psd_end_time[i],\
                         fft_step_s, fft_len_s, stage_start, stage_dur)
                # Make the psd_start_current (6,) into 2D array (6,1)
                psd_start_current = np.reshape(psd_start_current, (psd_start_current.shape[0], 1))
                # If found in the current bout add it to the list
                if len(psd_values_current)>0:
                    # Repeat the stage for each fft window
                    psd_stage_current = np.repeat(stage, psd_values_current.shape[0])
                    psd_stage_current = np.reshape(psd_stage_current, (psd_stage_current.shape[0], 1))
                    # Vertical concatenation of the psd values
                    psd_values_chan = np.vstack((psd_values_chan, psd_values_current)) if len(psd_values_chan)>0 else psd_values_current
                    psd_start = np.vstack((psd_start, psd_start_current)) if len(psd_start)>0 else psd_start_current
                    psd_stage = np.vstack((psd_stage, psd_stage_current)) if len(psd_stage)>0 else psd_stage_current

    return freq_bin_unique, psd_start, psd_stage, psd_values_chan


def extract_psd_from_event(psd_data, psd_start, psd_end, fft_win_step_s, fft_win_len_s, event_start, event_dur):
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
    if (event_start < psd_start) and ((event_start + event_dur) > psd_start):
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
    psd_data_sel = psd_data[first_fft_win:first_fft_win+n_fft_win,:] # the last fft window
    psd_start_sel = [psd_start_sel_s + (i-1)*fft_win_step_s for i in range(1, n_fft_win+1)]
    # Round the start time to the nearest second with 2 decimals
    psd_start_sel = np.round(np.array(psd_start_sel), 2)
    return psd_data_sel, psd_start_sel


# Compute the freq bins indexes for each mini band
def get_miniband_index(identifier, freq_bin_chan, mini_bandwidth, first_freq, last_freq, fs_chan):
    # Define the spectral band of each miniband
    # Compute the freq bins to average for each mini band
    # the upper limit is not included as [min, max[

    # ex 1 ) start=20 Hz, band=10 Hz, max=50 Hz
    # 20-30; 30-40, 40-50
    # ex 2 ) start=0.6 Hz, band=1 Hz, max =30 Hz
    # 0.6-1; 1-2; 2-3, 3-4, ...29-30
    # ex 3 ) start=0.6 Hz, band=0.5Hz, max=30 Hz
    # 0.6-1;  1-1.5; 1.5-2; 2-2.5....29.5-30.     
    
    # Min value between nyquist, last frequency bin of the fft and the last freq asked by the user.
    freq_max = min([freq_bin_chan[-1], last_freq, fs_chan/2])
    # Max between the first freq asked by the user and the min value of the freq bin of the fft.
    freq_min = max([freq_bin_chan[0],first_freq])
    cur_end = freq_min
    miniband_index = np.empty((0,0))

    # To make sure the floating point does not give to much precision 
    #   (it causes problem when finding the right freq bins)
    mini_bandwidth_precision = int(np.log10(mini_bandwidth))+1

    while cur_end < freq_max:
        start_bin = cur_end
        if (start_bin/mini_bandwidth).is_integer():
            if (start_bin + mini_bandwidth)<freq_max:
                cur_end = round(start_bin + mini_bandwidth, mini_bandwidth_precision)
            else:
                cur_end = freq_max
        else:
            if start_bin<mini_bandwidth:
                cur_end = round(start_bin + (mini_bandwidth-start_bin), mini_bandwidth_precision)
            else:
                cur_end = round(start_bin + ((2*mini_bandwidth)-start_bin), mini_bandwidth_precision)

        # Find the indices of elements between start_bin and end_bin
        cur_index_list = np.where((freq_bin_chan >= start_bin) & (freq_bin_chan < cur_end))[0] # [min, max[
        if len(cur_index_list): 
            cur_idx_start_end = [cur_index_list[0], cur_index_list[-1]]
            if len(miniband_index):
                miniband_index = np.vstack((miniband_index, cur_idx_start_end))
            else:
                miniband_index = cur_idx_start_end
        else:
            if len(miniband_index)==0:
                raise NodeRuntimeException(identifier, "freq_bins", \
                    f"PSACompilation : the mini bands from {freq_min} to {last_freq} is not found in the frequency bins")
    return miniband_index
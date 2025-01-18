"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
import csv

def write_doc_file(filepath, N_HOURS, N_CYCLES):
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        docwriter = csv.writer(csvfile, delimiter='\t')

        doc = _get_doc(N_HOURS, N_CYCLES)

        for i, (k, v) in enumerate(doc.items()):
            row_name = excel_column_name(i+1)
            docwriter.writerow([row_name,k,v])

def excel_column_name(number):
    column_name = ""
    while number > 0:
        remainder = (number - 1) % 26  # Subtract 1 to account for 0-based indexing
        column_name = chr(65 + remainder) + column_name  # 65 is the ASCII code for 'A'
        number = (number - 1) // 26
    return column_name

def _get_doc(N_HOURS, N_CYCLES):
    general_dict = \
    {
        'filename' : 'PSG filename',
        'id1'      : 'subject identification',
        'cyc_def_option':'Method used to split the sleep period in sleep cycles, it defines the criteria. I.e. : "Minimum criteria"  "Aeschbach 1993"  "Feinberg 1979"',
        'cyc_def_include_soremp':'Include a REM sleep periods (REMP) that occur within 15 minutes of sleep onset.',
        'cyc_def_include_last_incomplete':'Include the last sleep cycle even if the NREM period (NREMP) or REMP does not meet the minimum duration criteria.',
        'cyc_def_rem_min':'Minimum length without R stage to end the REMP.',
        'cyc_def_first_nrem_min':'Minimum length of the first NREMP in minutes.',
        'cyc_def_mid_last_nrem_min':'Minimum length of the middle and last NREMP in minutes.',
        'cyc_def_last_nrem_valid_min':'Minimum length of the NREMP in minutes to validate the last sleep cycle.',
        'cyc_def_first_rem_min':'Minimum length of the first REMP in minutes.',
        'cyc_def_mid_rem_min':'Minimum length of the middle REMP in minutes.',
        'cyc_def_last_rem_min':'Minimum length of the last REMP in minutes.',
        'cyc_def_move_end_rem':'Move the end of the REMP to the start of the following NREMP, eliminating the temporal "gap" between 2 cycles.',
        'cyc_def_sleep_stages':'List of valid stages used to define the sleep cycles:  "N1, N2, N3, R" or "N2, N3, R"',
        'artefact_group_name_list' : 'List of groups and names of the artefact excluded from the Power Spectral Analysis',
        'channel_label' : 'The label of the channel.',
        'channel_fs' : 'The sampling rate (Hz) of the channel.',
        'channel_artefact_count' : 'The number of artefacts marked on the channel (i.e. number of events).',
        'fft_win_sec': 'The window length in sec used to perform the FFT.',
        'fft_step_sec': 'The step in sec between each start point of the window used for the FFT.',
        'freq_low_Hz' : 'The low frequency (Hz) of the mini band.',
        'freq_high_Hz' : 'The high frequency (Hz) of the mini band.'
    }
    total_len_dict = \
    {
        'total_W_fft_win_count' : 'Total - The number of fft windows in awake.',
        'total_W_fft_win_valid_count' : 'Total - The number of valid fft windows in awake.',
        'total_N1_fft_win_count' : 'Total - The number of fft windows in N1.',
        'total_N1_fft_win_valid_count' : 'Total - The number of valid fft windows in N1.',
        'total_N2_fft_win_count' : 'Total - The number of fft windows in N2.',
        'total_N2_fft_win_valid_count' : 'Total - The number of valid fft windows in N2.',
        'total_N3_fft_win_count' : 'Total - The number of fft windows in N3.',
        'total_N3_fft_win_valid_count' : 'Total - The number of valid fft windows in N3.',
        'total_NREM_fft_win_count' : 'Total - The number of fft windows in NREM.',
        'total_NREM_fft_win_valid_count' : 'Total - The number of valid fft windows in NREM.',
        'total_R_fft_win_count' : 'Total - The number of fft windows in R.',
        'total_R_fft_win_valid_count' : 'Total - The number of valid fft windows in R.',
        'total_Unscored_fft_win_count' : 'Total - The number of fft windows unscored.',
        'total_Unscored_fft_win_valid_count' : 'Total - The number of valid fft windows unscored.',
        'total_fft_win_count' : 'Total - The total number of fft windows.',
        'total_fft_win_valid_count' : 'Total - The total number of valid fft windows.'
    }

    hour_len_dict = {}
    for i_hour in range(N_HOURS):
        current_hour_len_dict = \
        {
            f'hour{i_hour+1}_W_fft_win_count' : f'Hour {i_hour+1} - The number of valid fft windows in awake.',
            f'hour{i_hour+1}_W_fft_win_valid_count' : f'Hour {i_hour+1} - The number of valid fft windows in awake.',
            f'hour{i_hour+1}_N1_fft_win_count' : f'Hour {i_hour+1} - The number of valid fft windows in N1.',
            f'hour{i_hour+1}_N1_fft_win_valid_count' : f'Hour {i_hour+1} - The number of valid fft windows in N1.',
            f'hour{i_hour+1}_N2_fft_win_count' : f'Hour {i_hour+1} - The number of valid fft windows in N2.',
            f'hour{i_hour+1}_N2_fft_win_valid_count' : f'Hour {i_hour+1} - The number of valid fft windows in N2.',
            f'hour{i_hour+1}_N3_fft_win_count' : f'Hour {i_hour+1} - The number of valid fft windows in N3.',
            f'hour{i_hour+1}_N3_fft_win_valid_count' : f'Hour {i_hour+1} - The number of valid fft windows in N3.',
            f'hour{i_hour+1}_NREM_fft_win_count' : f'Hour {i_hour+1} - The number of valid fft windows in NREM.',
            f'hour{i_hour+1}_NREM_fft_win_valid_count' : f'Hour {i_hour+1} - The number ofhour1 valid fft windows in NREM.',
            f'hour{i_hour+1}_R_fft_win_count' : f'Hour {i_hour+1} - The number of valid fft windows in rem.',
            f'hour{i_hour+1}_R_fft_win_valid_count' : f'Hour {i_hour+1} - The number of valid fft windows in rem.',
            f'hour{i_hour+1}_Unscored_fft_win_count' : f'Hour {i_hour+1} - The number of valid fft windows unscored.',
            f'hour{i_hour+1}_Unscored_fft_win_valid_count' : f'Hour {i_hour+1} - The number of valid fft windows unscored.',
            f'hour{i_hour+1}_fft_win_count' : f'Hour {i_hour+1} - The total number of valid fft windows.',
            f'hour{i_hour+1}_fft_win_valid_count' : f'Hour {i_hour+1} - The total number of valid fft windows.'
        }
        hour_len_dict = hour_len_dict | current_hour_len_dict

    cyc_len_dict = {}
    for i_cycle in range(N_CYCLES):
        current_cycle_len_dict = \
        {        
        f'cyc{i_cycle+1}_length_min' : f'Cycle {i_cycle+1} - Duration of the cycle 1 in minutes.',
        f'cyc{i_cycle+1}_W_fft_win_count' : f'Cycle {i_cycle+1} - The number of valid fft windows in awake.',
        f'cyc{i_cycle+1}_W_fft_win_valid_count' : f'Cycle {i_cycle+1} - The number of valid fft windows in awake.',
        f'cyc{i_cycle+1}_N1_fft_win_count' : f'Cycle {i_cycle+1} - The number of valid fft windows in N1.',
        f'cyc{i_cycle+1}_N1_fft_win_valid_count' : f'Cycle {i_cycle+1} - The number of valid fft windows in N1.',
        f'cyc{i_cycle+1}_N2_fft_win_count' : f'Cycle {i_cycle+1} - The number of valid fft windows in N2.',
        f'cyc{i_cycle+1}_N2_fft_win_valid_count' : f'Cycle {i_cycle+1} - The number of valid fft windows in N2.',
        f'cyc{i_cycle+1}_N3_fft_win_count' : f'Cycle {i_cycle+1} - The number of valid fft windows in N3.',
        f'cyc{i_cycle+1}_N3_fft_win_valid_count' : f'Cycle {i_cycle+1} - The number of valid fft windows in N3.',
        f'cyc{i_cycle+1}_NREM_fft_win_count' : f'Cycle {i_cycle+1} - The number of valid fft windows in NREM.',
        f'cyc{i_cycle+1}_NREM_fft_win_valid_count' : f'Cycle {i_cycle+1} - The number of valid fft windows in NREM.',
        f'cyc{i_cycle+1}_R_fft_win_count' : f'Cycle {i_cycle+1} - The number of valid fft windows in rem.',
        f'cyc{i_cycle+1}_R_fft_win_valid_count' : f'Cycle {i_cycle+1} - The number of valid fft windows in rem.',
        f'cyc{i_cycle+1}_Unscored_fft_win_count' : f'Cycle {i_cycle+1} - The number of valid fft windows unscored.',
        f'cyc{i_cycle+1}_Unscored_fft_win_valid_count' : f'Cycle {i_cycle+1} - The number of valid fft windows unscored.',
        f'cyc{i_cycle+1}_fft_win_count' : f'Cycle {i_cycle+1} - The total number of valid fft windows.',
        f'cyc{i_cycle+1}_fft_win_valid_count' : f'Cycle {i_cycle+1} - The total number of valid fft windows.'
        }
        cyc_len_dict = cyc_len_dict | current_cycle_len_dict

    total_act_dict = \
        {
            'total_act' : 'Total - The total spectral power (uV^2)',
            'total_W_act' : 'Total - The total spectral power (uV^2) in awake.',
            'total_N1_act' : 'Total - The total spectral power (uV^2) in N1.',
            'total_N2_act' : 'Total - The total spectral power (uV^2) in N2.',
            'total_N3_act' : 'Total - The total spectral power (uV^2) in N3.',
            'total_NREM_act' : 'Total - The total spectral power (uV^2) in NREM.',
            'total_R_act' : 'Total - The total spectral power (uV^2) in rem.',
            'total_Unscored_act' : 'Total - The total spectral power (uV^2) unscored.'
        }

    hour_act_dict = {}
    for i_hour in range(N_HOURS):
        current_hour_act_dict = \
        {
            f'hour{i_hour+1}_act' : f'Hour {i_hour+1} - The spectral power (uV^2)', 
            f'hour{i_hour+1}_W_act' : f'Hour {i_hour+1} - The spectral power (uV^2) in awake.',
            f'hour{i_hour+1}_N1_act' : f'Hour {i_hour+1} - The spectral power (uV^2) in N1.',
            f'hour{i_hour+1}_N2_act' : f'Hour {i_hour+1} - The spectral power (uV^2) in N2.',
            f'hour{i_hour+1}_N3_act' : f'Hour {i_hour+1} - The spectral power (uV^2) in N3.',
            f'hour{i_hour+1}_NREM_act' : f'Hour {i_hour+1} - The spectral power (uV^2) in NREM.',
            f'hour{i_hour+1}_R_act' : f'Hour {i_hour+1} - The spectral power (uV^2) in rem.',
            f'hour{i_hour+1}_Unscored_act' : f'Hour {i_hour+1} - The spectral power (uV^2) unscored.'
        }
        hour_act_dict = hour_act_dict | current_hour_act_dict

    cyc_act_dict = {}
    for i_cycle in range(N_CYCLES):
        current_cycle_act_dict = \
        {  
            f'cyc{i_cycle+1}_act' : f'Cycle {i_cycle+1} - The spectral power (uV^2)', 
            f'cyc{i_cycle+1}_W_act' : f'Cycle {i_cycle+1} - The spectral power (uV^2) in awake.',
            f'cyc{i_cycle+1}_N1_act' : f'Cycle {i_cycle+1} - The spectral power (uV^2) in N1.',
            f'cyc{i_cycle+1}_N2_act' : f'Cycle {i_cycle+1} - The spectral power (uV^2) in N2.',
            f'cyc{i_cycle+1}_N3_act' : f'Cycle {i_cycle+1} - The spectral power (uV^2) in N3.',
            f'cyc{i_cycle+1}_NREM_act' : f'Cycle {i_cycle+1} - The spectral power (uV^2) in NREM.',
            f'cyc{i_cycle+1}_R_act' : f'Cycle {i_cycle+1} - The spectral power (uV^2) in rem.',
            f'cyc{i_cycle+1}_Unscored_act' : f'Cycle {i_cycle+1} - The spectral power (uV^2) unscored.'
        }
        cyc_act_dict = cyc_act_dict | current_cycle_act_dict

    return general_dict | total_len_dict | total_act_dict | hour_len_dict | hour_act_dict | cyc_len_dict | cyc_act_dict
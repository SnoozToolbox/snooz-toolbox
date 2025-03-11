"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
import csv

def write_doc_file(filepath, N_CYCLE):
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        docwriter = csv.writer(csvfile, delimiter='\t')

        doc = _get_doc(N_CYCLE)

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


def _get_doc(N_CYCLE):

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
            'cyc_def_sleep_stages':'List of valid stages used to define the sleep cycles:  "N1, N2, N3, R" or "N2, N3, R"'
    }

    # not included yet.. 
    # 'detect_in_cycle' : 'Flag to detect slow wave in sleep cycles only.',
    detector_dict = \
    {    
            'stage_sel' :       'Sleep stages selection to detect slow waves in.',
            'detect_excl_remp' : 'Flag to exclude rem period from the slow wave detection.',
            'sw_event_name' :   'Slow wave event name (specific to the detection algorithm).',
            'filt_low_Hz' :     'Low frequency of the bandpass filter (Hz).',
            'filt_high_Hz' :    'High frequency of the bandpass filter (Hz).',
            'min_amp_pkpk_uV' : 'Minimum peak-to-peak amplitude (uV).',
            'min_neg_amp_uV' :  'Minimum negative amplitude (uV).', 
            'min_neg_ms' :  'Minimum duration of negative part of the slow wave (ms).',
            'max_neg_ms' :  'Maximum duration of negative part of the slow wave (ms).',
            'min_pos_ms' :  'Minimum duration of positive part of the slow wave (ms).',
            'max_pos_ms' :  'Maximum duration of positive part of the slow wave (ms).'
    }

    channel_dict = \
    {            
            'artefact_group_name' : 'List of groups and names of the artifact excluded from the detection',
            'chan_label' : 'The label of the channel.',
            'chan_fs' : 'The sampling rate (Hz) of the channel.'
    }

    sleep_car_dict = \
    {
            'cyc_count' : 'Number of sleep cycles.',
            'recording_min' : 'Recording duration (min) from lights off to lights on.',
            'sleep_period_min' : 'Total period for detection - Duration (min) of the sleep period.'
    }

    # The valid duration can change across channels because of the artifact detection
    total_dict = \
    {  
            'total_N1_valid_min' : 'Valid (no artifact) period for detection - Valid duration (min) of the sleep period in N1 stage minus the REM periods if excluded.',
            'total_N2_valid_min' : 'Valid (no artifact) period for detection - Valid duration (min) of the sleep period in N2 stage minus the REM periods if excluded.',
            'total_N3_valid_min' : 'Valid (no artifact) period for detection - Valid duration (min) of the sleep period in N3 stage minus the REM periods if excluded.',
            'total_R_valid_min' : 'Valid (no artifact) period for detection - Valid duration (min) of the sleep period in REM stage.',
            'total_valid_min' : 'Valid (no artifact) period for detection - Valid duration (min) of the sleep stage selected minus thoses included in REM periods if remps are excluded.',

            'total_N1_sw_count' : 'Total - SW count in N1 stage.',
            'total_N2_sw_count' : 'Total - SW count in N2 stage.',
            'total_N3_sw_count' : 'Total - SW count in N3 stage.',
            'total_R_sw_count' : 'Total - SW count in REM stage.',
            'total_sw_count' : 'Total - SW count in all stages.',

            'total_N1_sw_sec' : 'Total - Average slow wave duration (s) in N1 stage.',
            'total_N2_sw_sec' : 'Total - Average slow wave duration (s) in N2 stage.',
            'total_N3_sw_sec' : 'Total - Average slow wave duration (s) in N3 stage.',
            'total_R_sw_sec' : 'Total - Average slow wave duration (s) in REM stage.',
            'total_sw_sec' : 'Total - Average slow wave duration (s)',

            'total_N1_pkpk_amp_uV' : 'Total - Average slow wave peak-to-peak amplitude (uV) in N1 stage.',
            'total_N2_pkpk_amp_uV' : 'Total - Average slow wave peak-to-peak amplitude (uV) in N2 stage.',
            'total_N3_pkpk_amp_uV' : 'Total - Average slow wave peak-to-peak amplitude (uV) in N3 stage.',
            'total_R_pkpk_amp_uV' : 'Total - Average slow wave peak-to-peak amplitude (uV) in REM stage.',
            'total_pkpk_amp_uV' : 'Total - Average slow wave peak-to-peak amplitude (uV)',

            'total_N1_freq_Hz' : 'Total - Slow wave frequency (Hz) (inverse of the duration) in N1 stage.',
            'total_N2_freq_Hz' : 'Total - Slow wave frequency (Hz) (inverse of the duration) in N2 stage.',
            'total_N3_freq_Hz' : 'Total - Slow wave frequency (Hz) (inverse of the duration) in N3 stage.',
            'total_R_freq_Hz' : 'Total - Slow wave frequency (Hz) (inverse of the duration) in REM stage.',
            'total_freq_Hz' : 'Total - Slow wave frequency (Hz) (inverse of the duration).',

            'total_N1_neg_amp_uV' : 'Total - Average slow wave negative peak amplitude (uV) in N1 stage.',
            'total_N2_neg_amp_uV' : 'Total - Average slow wave negative peak amplitude (uV) in N2 stage.',
            'total_N3_neg_amp_uV' : 'Total - Average slow wave negative peak amplitude (uV) in N3 stage.',
            'total_R_neg_amp_uV' : 'Total - Average slow wave negative peak amplitude (uV) in REM stage.',
            'total_neg_amp_uV' : 'Total - Average slow wave negative peak amplitude (uV).',

            'total_N1_neg_sec' : 'Total - Average slow wave negative duration (ms) in N1 stage.',
            'total_N2_neg_sec' : 'Total - Average slow wave negative duration (ms) in N2 stage.',
            'total_N3_neg_sec' : 'Total - Average slow wave negative duration (ms) in N3 stage.',
            'total_R_neg_sec' : 'Total - Average slow wave negative duration (ms) in REM stage.',
            'total_neg_sec' : 'Total - Average slow wave negative duration (ms)',

            'total_N1_pos_sec' : 'Total - Average slow wave positive duration (ms) in N1 stage.',
            'total_N2_pos_sec' : 'Total - Average slow wave positive duration (ms) in N2 stage.',
            'total_N3_pos_sec' : 'Total - Average slow wave positive duration (ms) in N3 stage.',
            'total_R_pos_sec' : 'Total - Average slow wave positive duration (ms) in REM stage.',
            'total_pos_sec' : 'Total -  Average slow wave positive duration (ms)',

            'total_N1_slope_0_min' : 'Total - Average slow wave slope (uV/s) from 0 crossing to the min of the negative component in N1 stage.',
            'total_N2_slope_0_min' : 'Total - Average slow wave slope (uV/s) from 0 crossing to the min of the negative component in N2 stage.',
            'total_N3_slope_0_min' : 'Total - Average slow wave slope (uV/s) from 0 crossing to the min of the negative component in N3 stage.',
            'total_R_slope_0_min' : 'Total - Average slow wave slope (uV/s) from 0 crossing to the min of the negative component in REM stage.',
            'total_slope_0_min' : 'Total -  Average slow wave slope (uV/s) from 0 crossing to the min of the negative component.',

            'total_N1_slope_min_max' : 'Total - Average slow wave slope (uV/s) from min to the max in N1 stage.',
            'total_N2_slope_min_max' : 'Total - Average slow wave slope (uV/s) from min to the max in N2 stage.',
            'total_N3_slope_min_max' : 'Total - Average slow wave slope (uV/s) from min to the max in N3 stage.',
            'total_R_slope_min_max' : 'Total - Average slow wave slope (uV/s) from min to the max in REM stage.',
            'total_slope_min_max' : 'Total -  Average slow wave slope (uV/s) from min to the max.',

            'total_N1_slope_max_0' : 'Total - Average slow wave slope (uV/s) from max of positive to the 0 crossing in N1 stage.',
            'total_N2_slope_max_0' : 'Total - Average slow wave slope (uV/s) from max of positive to the 0 crossing in N2 stage.',
            'total_N3_slope_max_0' : 'Total - Average slow wave slope (uV/s) from max of positive to the 0 crossing in N3 stage.',
            'total_R_slope_max_0' : 'Total - Average slow wave slope (uV/s) from max of positive to the 0 crossing in REM stage.',
            'total_slope_max_0' : 'Total -  Average slow wave slope (uV/s) from max of positive to the 0 crossing.',

            'total_N1_trans_freq_Hz' : 'Total -  Average slow wave transition frequency (Hz) in N1 stage.',
            'total_N2_trans_freq_Hz' : 'Total -  Average slow wave transition frequency (Hz) in N2 stage.',
            'total_N3_trans_freq_Hz' : 'Total -  Average slow wave transition frequency (Hz) in N3 stage.',
            'total_R_trans_freq_Hz' : 'Total -  Average slow wave transition frequency (Hz) in REM stage.',
            'total_trans_freq_Hz' : 'Total -   Average slow wave transition frequency (Hz)'
    }

    cycle_dict = {}
    for i_cycle in range(N_CYCLE):
        current_cycle_dict = \
            {
            f'cyc{i_cycle+1}_valid_min' : f'Cycle {i_cycle+1} - Valid (no artifact) duration (min) available for detection minus the REM periods if excluded.',
            f'cyc{i_cycle+1}_N1_valid_min' : f'Cycle {i_cycle+1} - Valid (no artifact) duration (min) in N1 stage available for detection minus the REM periods if excluded.',
            f'cyc{i_cycle+1}_N2_valid_min' : f'Cycle {i_cycle+1} - Valid (no artifact) duration (min) in N2 stage available for detection minus the REM periods if excluded.',
            f'cyc{i_cycle+1}_N3_valid_min' : f'Cycle {i_cycle+1} - Valid (no artifact) duration (min) in N3 stage available for detection minus the REM periods if excluded.',
            f'cyc{i_cycle+1}_R_valid_min' : f'Cycle {i_cycle+1} - Valid (no artifact) duration (min) in REM stage available for detection.',
            f'cyc{i_cycle+1}_min' : f'Cycle {i_cycle+1} duration (min) minus the REM periods if excluded.',

            f'cyc{i_cycle+1}_N1_sw_count' : f'Cycle {i_cycle+1} - Slow wave count in N1 stage.',
            f'cyc{i_cycle+1}_N2_sw_count' : f'Cycle {i_cycle+1} - Slow wave count in N2 stage.',
            f'cyc{i_cycle+1}_N3_sw_count' : f'Cycle {i_cycle+1} - Slow wave count in N3 stage.',
            f'cyc{i_cycle+1}_R_sw_count' : f'Cycle {i_cycle+1} - Slow wave count in REM stage.',
            f'cyc{i_cycle+1}_sw_count' : f'Cycle {i_cycle+1} - Slow wave count in all stages.',

            f'cyc{i_cycle+1}_N1_sw_sec' : f'Cycle {i_cycle+1} - Average slow wave duration (s) in N1 stage.',
            f'cyc{i_cycle+1}_N2_sw_sec' : f'Cycle {i_cycle+1} - Average slow wave duration (s) in N2 stage.',
            f'cyc{i_cycle+1}_N3_sw_sec' : f'Cycle {i_cycle+1} - Average slow wave duration (s) in N3 stage.',
            f'cyc{i_cycle+1}_R_sw_sec' : f'Cycle {i_cycle+1} - Average slow wave duration (s) in REM stage.',
            f'cyc{i_cycle+1}_sw_sec' : f'Cycle {i_cycle+1} - Average slow wave duration (s)',

            f'cyc{i_cycle+1}_N1_pkpk_amp_uV' : f'Cycle {i_cycle+1} - Average slow wave peak-to-peak amplitude (uV) in N1 stage.',
            f'cyc{i_cycle+1}_N2_pkpk_amp_uV' : f'Cycle {i_cycle+1} - Average slow wave peak-to-peak amplitude (uV) in N2 stage.',
            f'cyc{i_cycle+1}_N3_pkpk_amp_uV' : f'Cycle {i_cycle+1} - Average slow wave peak-to-peak amplitude (uV) in N3 stage.',
            f'cyc{i_cycle+1}_R_pkpk_amp_uV' : f'Cycle {i_cycle+1} - Average slow wave peak-to-peak amplitude (uV) in REM stage.',
            f'cyc{i_cycle+1}_pkpk_amp_uV' : f'Cycle {i_cycle+1} - Average slow wave peak-to-peak amplitude (uV)',

            f'cyc{i_cycle+1}_N1_freq_Hz' : f'Cycle {i_cycle+1} - Slow wave frequency (Hz) (inverse of the duration) in N1 stage.',
            f'cyc{i_cycle+1}_N2_freq_Hz' : f'Cycle {i_cycle+1} - Slow wave frequency (Hz) (inverse of the duration) in N2 stage.',
            f'cyc{i_cycle+1}_N3_freq_Hz' : f'Cycle {i_cycle+1} - Slow wave frequency (Hz) (inverse of the duration) in N3 stage.',
            f'cyc{i_cycle+1}_R_freq_Hz' : f'Cycle {i_cycle+1} - Slow wave frequency (Hz) (inverse of the duration) in REM stage.',
            f'cyc{i_cycle+1}_freq_Hz' : f'Cycle {i_cycle+1} - Slow wave frequency (Hz) (inverse of the duration).',

            f'cyc{i_cycle+1}_N1_neg_amp_uV' : f'Cycle {i_cycle+1} - Average slow wave negative peak amplitude (uV) in N1 stage.',
            f'cyc{i_cycle+1}_N2_neg_amp_uV' : f'Cycle {i_cycle+1} - Average slow wave negative peak amplitude (uV) in N2 stage.',
            f'cyc{i_cycle+1}_N3_neg_amp_uV' : f'Cycle {i_cycle+1} - Average slow wave negative peak amplitude (uV) in N3 stage.',
            f'cyc{i_cycle+1}_R_neg_amp_uV' : f'Cycle {i_cycle+1} - Average slow wave negative peak amplitude (uV) in REM stage.',
            f'cyc{i_cycle+1}_neg_amp_uV' : f'Cycle {i_cycle+1} - Average slow wave negative peak amplitude (uV).',

            f'cyc{i_cycle+1}_N1_neg_sec' : f'Cycle {i_cycle+1} - Average slow wave negative duration (ms) in N1 stage.',
            f'cyc{i_cycle+1}_N2_neg_sec' : f'Cycle {i_cycle+1} - Average slow wave negative duration (ms) in N2 stage.',
            f'cyc{i_cycle+1}_N3_neg_sec' : f'Cycle {i_cycle+1} - Average slow wave negative duration (ms) in N3 stage.',
            f'cyc{i_cycle+1}_R_neg_sec' : f'Cycle {i_cycle+1} - Average slow wave negative duration (ms) in REM stage.',
            f'cyc{i_cycle+1}_neg_sec' : f'Cycle {i_cycle+1} - Average slow wave negative duration (ms)',

            f'cyc{i_cycle+1}_N1_pos_sec' : f'Cycle {i_cycle+1} - Average slow wave positive duration (ms) in N1 stage.',
            f'cyc{i_cycle+1}_N2_pos_sec' : f'Cycle {i_cycle+1} - Average slow wave positive duration (ms) in N2 stage.',
            f'cyc{i_cycle+1}_N3_pos_sec' : f'Cycle {i_cycle+1} - Average slow wave positive duration (ms) in N3 stage.',
            f'cyc{i_cycle+1}_R_pos_sec' : f'Cycle {i_cycle+1} - Average slow wave positive duration (ms) in REM stage.',
            f'cyc{i_cycle+1}_pos_sec' : f'Cycle {i_cycle+1} -  Average slow wave positive duration (ms)',

            f'cyc{i_cycle+1}_N1_slope_0_min' : f'Cycle {i_cycle+1} - Average slow wave slope (uV/s) from 0 crossing to the min of the negative component in N1 stage.',
            f'cyc{i_cycle+1}_N2_slope_0_min' : f'Cycle {i_cycle+1} - Average slow wave slope (uV/s) from 0 crossing to the min of the negative component in N2 stage.',
            f'cyc{i_cycle+1}_N3_slope_0_min' : f'Cycle {i_cycle+1} - Average slow wave slope (uV/s) from 0 crossing to the min of the negative component in N3 stage.',
            f'cyc{i_cycle+1}_R_slope_0_min' : f'Cycle {i_cycle+1} - Average slow wave slope (uV/s) from 0 crossing to the min of the negative component in REM stage.',
            f'cyc{i_cycle+1}_slope_0_min' : f'Cycle {i_cycle+1} -  Average slow wave slope (uV/s) from 0 crossing to the min of the negative component.',

            f'cyc{i_cycle+1}_N1_slope_min_max' : f'Cycle {i_cycle+1} - Average slow wave slope (uV/s) from min to the max in N1 stage.',
            f'cyc{i_cycle+1}_N2_slope_min_max' : f'Cycle {i_cycle+1} - Average slow wave slope (uV/s) from min to the max in N2 stage.',
            f'cyc{i_cycle+1}_N3_slope_min_max' : f'Cycle {i_cycle+1} - Average slow wave slope (uV/s) from min to the max in N3 stage.',
            f'cyc{i_cycle+1}_R_slope_min_max' : f'Cycle {i_cycle+1} - Average slow wave slope (uV/s) from min to the max in REM stage.',
            f'cyc{i_cycle+1}_slope_min_max' : f'Cycle {i_cycle+1} -  Average slow wave slope (uV/s) from min to the max.',

            f'cyc{i_cycle+1}_N1_slope_max_0' : f'Cycle {i_cycle+1} - Average slow wave slope (uV/s) from max of positive to the 0 crossing in N1 stage.',
            f'cyc{i_cycle+1}_N2_slope_max_0' : f'Cycle {i_cycle+1} - Average slow wave slope (uV/s) from max of positive to the 0 crossing in N2 stage.',
            f'cyc{i_cycle+1}_N3_slope_max_0' : f'Cycle {i_cycle+1} - Average slow wave slope (uV/s) from max of positive to the 0 crossing in N3 stage.',
            f'cyc{i_cycle+1}_R_slope_max_0' : f'Cycle {i_cycle+1} - Average slow wave slope (uV/s) from max of positive to the 0 crossing in REM stage.',
            f'cyc{i_cycle+1}_slope_max_0' : f'Cycle {i_cycle+1} -  Average slow wave slope (uV/s) from max of positive to the 0 crossing.',

            f'cyc{i_cycle+1}_N1_trans_freq_Hz' : f'Cycle {i_cycle+1} -  Average slow wave transition frequency (Hz) in N1 stage.',
            f'cyc{i_cycle+1}_N2_trans_freq_Hz' : f'Cycle {i_cycle+1} -  Average slow wave transition frequency (Hz) in N2 stage.',
            f'cyc{i_cycle+1}_N3_trans_freq_Hz' : f'Cycle {i_cycle+1} -  Average slow wave transition frequency (Hz) in N3 stage.',
            f'cyc{i_cycle+1}_R_trans_freq_Hz' : f'Cycle {i_cycle+1} -  Average slow wave transition frequency (Hz) in REM stage.',
            f'cyc{i_cycle+1}_trans_freq_Hz' : f'Cycle {i_cycle+1} -   Average slow wave transition frequency (Hz)'
            }
        cycle_dict = cycle_dict | current_cycle_dict
    
    complete_dict = general_dict | detector_dict | channel_dict | sleep_car_dict | total_dict | cycle_dict
    return complete_dict

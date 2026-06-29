"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
import csv

def write_doc_file(filepath, N_CYCLE, N_DIVISION, n_dist):
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        docwriter = csv.writer(csvfile, delimiter='\t')

        doc = _get_doc(N_CYCLE, N_DIVISION, n_dist)

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


def _get_doc(N_CYCLE, N_DIVISION, n_dist):

    general_dict = \
    {
            'filename' : 'PSG filename',
            'chan_label' : 'Channel label',
            'recording_min' : 'Recording duration (min) from lights off to lights on.',
            'sleep_period_min' : 'Total period for detection - Duration (min) of the sleep period.'
    }

    # The valid duration can change across channels because of the artifact detection
    total_dict = {}
    for i_cat in range(n_dist):
        current_total_dict = \
            {  
            f'cat{i_cat+1}_sw_count' : f'Category{i_cat+1} - The number of slow wave events.',
            f'cat{i_cat+1}_sw_density' : f'Category{i_cat+1} - Slow wave density per minute.',
            f'cat{i_cat+1}_pkpk_amp_uV' : f'Category{i_cat+1} - Average slow wave peak-to-peak amplitude (uV)',
            f'cat{i_cat+1}_duration_sec' : f'Category{i_cat+1} - Average slow wave duration (s)',
            f'cat{i_cat+1}_freq_Hz' : f'Category{i_cat+1} - Slow wave frequency (Hz) (inverse of the duration).',
            f'cat{i_cat+1}_neg_amp_uV' : f'Category{i_cat+1} - Average slow wave negative peak amplitude (uV).',
            f'cat{i_cat+1}_neg_sec' : f'Category{i_cat+1} - Average slow wave negative duration (ms)',
            f'cat{i_cat+1}_pos_sec' : f'Category{i_cat+1} -  Average slow wave positive duration (ms)',
            f'cat{i_cat+1}_slope_0_min' : f'Category{i_cat+1} -  Average slow wave slope (uV/s) from 0 crossing to the min of the negative component.',
            f'cat{i_cat+1}_slope_min_max' : f'Category{i_cat+1} -  Average slow wave slope (uV/s) from min to the max.',
            f'cat{i_cat+1}_slope_max_0' : f'Category{i_cat+1} -  Average slow wave slope (uV/s) from max of positive to the 0 crossing.',
            f'cat{i_cat+1}_trans_freq_Hz' : f'Category{i_cat+1} -   Average slow wave transition frequency (Hz)'
            }
        total_dict = total_dict | current_total_dict

    cycle_dict = {}
    for i_cycle in range(N_CYCLE):
        for i_cat in range(n_dist):
            current_cycle_dict = \
                {
                f'cat{i_cat+1}_cyc{i_cycle+1}_sw_count' : f'Category{i_cat+1} - Cycle {i_cycle+1} - The number of slow wave events.',
                f'cat{i_cat+1}_cyc{i_cycle+1}_sw_density' : f'Category{i_cat+1} - Cycle {i_cycle+1} - Slow wave density per minute.',
                f'cat{i_cat+1}_cyc{i_cycle+1}_pkpk_amp_uV' : f'Category{i_cat+1} - Cycle {i_cycle+1} - Average slow wave peak-to-peak amplitude (uV)',
                f'cat{i_cat+1}_cyc{i_cycle+1}_duration_sec' : f'Category{i_cat+1} - Cycle {i_cycle+1} - Average slow wave duration (s)',
                f'cat{i_cat+1}_cyc{i_cycle+1}_freq_Hz' : f'Category{i_cat+1} - Cycle {i_cycle+1} - Slow wave frequency (Hz) (inverse of the duration).',
                f'cat{i_cat+1}_cyc{i_cycle+1}_neg_amp_uV' : f'Category{i_cat+1} - Cycle {i_cycle+1} - Average slow wave negative peak amplitude (uV).',
                f'cat{i_cat+1}_cyc{i_cycle+1}_neg_sec' : f'Category{i_cat+1} - Cycle {i_cycle+1} - Average slow wave negative duration (ms)',
                f'cat{i_cat+1}_cyc{i_cycle+1}_pos_sec' : f'Category{i_cat+1} - Cycle {i_cycle+1} -  Average slow wave positive duration (ms)',
                f'cat{i_cat+1}_cyc{i_cycle+1}_slope_0_min' : f'Category{i_cat+1} - Cycle {i_cycle+1} -  Average slow wave slope (uV/s) from 0 crossing to the min of the negative component.',
                f'cat{i_cat+1}_cyc{i_cycle+1}_slope_min_max' : f'Category{i_cat+1} - Cycle {i_cycle+1} -  Average slow wave slope (uV/s) from min to the max.',
                f'cat{i_cat+1}_cyc{i_cycle+1}_slope_max_0' : f'Category{i_cat+1} - Cycle {i_cycle+1} -  Average slow wave slope (uV/s) from max of positive to the 0 crossing.',
                f'cat{i_cat+1}_cyc{i_cycle+1}_trans_freq_Hz' : f'Category{i_cat+1} - Cycle {i_cycle+1} -   Average slow wave transition frequency (Hz)'
                }
            cycle_dict = cycle_dict | current_cycle_dict
    
    div_dict = {}
    for i_div in range(N_DIVISION):
        for i_cat in range(n_dist):
            current_div_dict = \
                {
                f'cat{i_cat+1}_div{i_div+1}_out{N_DIVISION}_sw_count' : f'Category{i_cat+1} - Division {i_div+1} out of {N_DIVISION} - The number of slow wave events.',
                f'cat{i_cat+1}_div{i_div+1}_out{N_DIVISION}_sw_density' : f'Category{i_cat+1} - Division {i_div+1} out of {N_DIVISION} - Slow wave density per minute.',
                f'cat{i_cat+1}_div{i_div+1}_out{N_DIVISION}_pkpk_amp_uV' : f'Category{i_cat+1} - Division {i_div+1} out of {N_DIVISION} -Average slow wave peak-to-peak amplitude (uV)',
                f'cat{i_cat+1}_div{i_div+1}_out{N_DIVISION}_duration_sec' : f'Category{i_cat+1} - Division {i_div+1} out of {N_DIVISION} -Average slow wave duration (s)',
                f'cat{i_cat+1}_div{i_div+1}_out{N_DIVISION}_freq_Hz' : f'Category{i_cat+1} - Division {i_div+1} out of {N_DIVISION} -Slow wave frequency (Hz) (inverse of the duration).',
                f'cat{i_cat+1}_div{i_div+1}_out{N_DIVISION}_neg_amp_uV' : f'Category{i_cat+1} - Division {i_div+1} out of {N_DIVISION} -Average slow wave negative peak amplitude (uV).',
                f'cat{i_cat+1}_div{i_div+1}_out{N_DIVISION}_neg_sec' : f'Category{i_cat+1} - Division {i_div+1} out of {N_DIVISION} -Average slow wave negative duration (ms)',
                f'cat{i_cat+1}_div{i_div+1}_out{N_DIVISION}_pos_sec' : f'Category{i_cat+1} - Division {i_div+1} out of {N_DIVISION} - Average slow wave positive duration (ms)',
                f'cat{i_cat+1}_div{i_div+1}_out{N_DIVISION}_slope_0_min' : f'Category{i_cat+1} - Division {i_div+1} out of {N_DIVISION} - Average slow wave slope (uV/s) from 0 crossing to the min of the negative component.',
                f'cat{i_cat+1}_div{i_div+1}_out{N_DIVISION}_slope_min_max' : f'Category{i_cat+1} - Division {i_div+1} out of {N_DIVISION} - Average slow wave slope (uV/s) from min to the max.',
                f'cat{i_cat+1}_div{i_div+1}_out{N_DIVISION}_slope_max_0' : f'Category{i_cat+1} - Division {i_div+1} out of {N_DIVISION} - Average slow wave slope (uV/s) from max of positive to the 0 crossing.',
                f'cat{i_cat+1}_div{i_div+1}_out{N_DIVISION}_trans_freq_Hz' : f'Category{i_cat+1} - Division {i_div+1} out of {N_DIVISION} -  Average slow wave transition frequency (Hz)'
                }
            div_dict = div_dict | current_div_dict    

    complete_dict = general_dict | total_dict | cycle_dict | div_dict
    return complete_dict

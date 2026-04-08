"""
© 2025 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
import csv

def write_doc_file(filepath, N_CYCLE, N_HOURS=0):
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        docwriter = csv.writer(csvfile, delimiter='\t')

        doc = _get_doc(N_CYCLE, N_HOURS)

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


def _get_doc(N_CYCLE, N_HOURS=0):

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

    detector_dict = \
    {    
            'stage_sel' :       'Sleep stages selection to detect REMs in.',
            'rems_event_name' :   'REMs event name (specific to the detection algorithm).'
    }

    channel_dict = \
    {            
            'chan_label' : 'The label of the channel.',
            'chan_fs' : 'The sampling rate (Hz) of the channel.'
    }

    sleep_car_dict = \
    {
            'cyc_count' : 'Number of sleep cycles.',
            'recording_min' : 'Recording duration (min) from lights off to lights on.',
            'sleep_period_min' : 'Total period for detection - Duration (min) of the sleep period.'
    }

    # The valid duration represents the duration available for detection
    # REMs only occur in REM sleep stage (R)
    total_dict = \
    {  
            'total_R_valid_min' : 'Valid (no artifact) period for detection - Valid duration (min) of the sleep period in REM stage.',

            'total_R_rems_count' : 'Total - REMs count in REM stage.',

            'total_R_rems_sec' : 'Total - Average REMs duration (s) in REM stage.',

            'total_R_amplitude_uV' : 'Total - Average REMs amplitude (uV) in REM stage.',

            'total_R_rems_density' : 'Total - REMs density (count/epoch) in REM stage. Epoch duration is 30 seconds.'

    }

    cycle_dict = {}
    for i_cycle in range(N_CYCLE):
        current_cycle_dict = \
            {
            f'cyc{i_cycle+1}_R_valid_min' : f'Cycle {i_cycle+1} - Valid (no artifact) duration (min) in REM stage available for detection.',
            f'cyc{i_cycle+1}_min' : f'Cycle {i_cycle+1} duration (min).',

            f'cyc{i_cycle+1}_R_rems_count' : f'Cycle {i_cycle+1} - REMs count in REM stage.',

            f'cyc{i_cycle+1}_R_rems_sec' : f'Cycle {i_cycle+1} - Average REMs duration (s) in REM stage.',

            f'cyc{i_cycle+1}_R_amplitude_uV' : f'Cycle {i_cycle+1} - Average REMs amplitude (uV) in REM stage.',

            f'cyc{i_cycle+1}_R_rems_density' : f'Cycle {i_cycle+1} - REMs density (count/epoch) in REM stage. Epoch duration is 30 seconds.'
            }
        cycle_dict = cycle_dict | current_cycle_dict
    
    # Add variance of densities across cycles
    cycle_dict['rems_density_var'] = 'Variance of REMs density across all sleep cycles.'
    
    # Add clock hour documentation
    clock_hour_dict = {}
    for i_hour in range(N_HOURS):
        current_hour_dict = \
            {
            f'clock_h{i_hour+1}_R_valid_min' : f'Hour {i_hour+1} - Valid (no artifact) duration (min) in REM stage available for detection.',
            f'clock_h{i_hour+1}_min' : f'Hour {i_hour+1} duration (min).',

            f'clock_h{i_hour+1}_R_rems_count' : f'Hour {i_hour+1} - REMs count in REM stage.',

            f'clock_h{i_hour+1}_R_rems_sec' : f'Hour {i_hour+1} - Average REMs duration (s) in REM stage.',

            f'clock_h{i_hour+1}_R_amplitude_uV' : f'Hour {i_hour+1} - Average REMs amplitude (µV) in REM stage.',

            f'clock_h{i_hour+1}_R_rems_density' : f'Hour {i_hour+1} - REMs density (count/epoch) in REM stage. Epoch duration is 30 seconds.'
            }
        clock_hour_dict = clock_hour_dict | current_hour_dict
    
    # Add variance of densities across clock hours
    clock_hour_dict['clock_h_rems_density_var'] = 'Variance of REMs density across all clock hours.'
    
    # Add stage hour documentation
    stage_hour_dict = {}
    for i_hour in range(N_HOURS):
        current_stage_hour_dict = \
            {
            f'stage_h{i_hour+1}_R_valid_min' : f'Stage Hour {i_hour+1} - Valid (no artifact) duration (min) in REM stage available for detection.',
            f'stage_h{i_hour+1}_min' : f'Stage Hour {i_hour+1} duration (min).',

            f'stage_h{i_hour+1}_R_rems_count' : f'Stage Hour {i_hour+1} - REMs count in REM stage.',

            f'stage_h{i_hour+1}_R_rems_sec' : f'Stage Hour {i_hour+1} - Average REMs duration (s) in REM stage.',

            f'stage_h{i_hour+1}_R_amplitude_uV' : f'Stage Hour {i_hour+1} - Average REMs amplitude (µV) in REM stage.',

            f'stage_h{i_hour+1}_R_rems_density' : f'Stage Hour {i_hour+1} - REMs density (count/epoch) in REM stage. Epoch duration is 30 seconds.'
            }
        stage_hour_dict = stage_hour_dict | current_stage_hour_dict
    
    # Add variance of densities across stage hours
    stage_hour_dict['stage_h_rems_density_var'] = 'Variance of REMs density across all stage hours.'
    
    complete_dict = general_dict | detector_dict | channel_dict | sleep_car_dict | total_dict | cycle_dict | clock_hour_dict | stage_hour_dict
    return complete_dict


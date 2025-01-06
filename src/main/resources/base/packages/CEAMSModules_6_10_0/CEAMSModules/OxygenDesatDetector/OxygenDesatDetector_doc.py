"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
import csv

def write_doc_file(filepath, N_CYCLE, stage_stats_labels, values_below):
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        docwriter = csv.writer(csvfile, delimiter='\t')

        doc = _get_doc(N_CYCLE, stage_stats_labels, values_below)

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


def _get_doc(N_CYCLE, stage_stats_labels, values_below):
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
            'sleep_cycle_count' : 'Number of sleep cycles',

            'desaturation_drop_percent' : 'Drop level (%) for the oxygen desaturation "3 or 4"',
            'max_slope_drop_sec' : 'The maximum duration (s) during which the oxygen level is dropping "120 or 20"',
            'min_hold_drop_sec' : 'Minimum duration (s) during which the oxygen level drop is maintained "10 or 5"',     

            'invalid_events' : 'Group and name annotation labels removed from the oxygen saturation analysis',
            'chan_label' : 'The label of the oxygen channel used for the anlysis',
            'chan_fs' : 'The sampling rate (Hz) of the oxygen channel used for the anlysis'
    }

    total_dict = \
    {            
            'total_invalid_min' : 'Invalid duration for oxygen saturation analysis (min).',
            'total_valid_min' : 'Valid (no invalid section) duration for oxygen saturation analysis (min) from lights off to lights on.',
            'total_saturation_avg' : 'The average value of the oxygen saturation (%) during lights off (the recording).',
            'total_saturation_std' : 'The standard deviation value of the oxygen saturation (%) during lights off (the recording).',
            'total_saturation_min' : 'The minimum value of the oxygen saturation (%) during lights off (the recording).',
            'total_saturation_max' : 'The maximum value of the oxygen saturation (%) during lights off (the recording).'
    }
    total_threshold_dict = {}
    for val in values_below:
        total_threshold_dict[f"total_below_{val}_min"] = f"The time spent (min) with an oxygen saturation under {val} % during the recording."
        
    third_dict = {}
    third_val = [1, 2, 3]
    for val in third_val:
        if val==1:
            label = "first"
        elif val==2:
            label = "second"
        else:
            label = "last"
        third_dict[f'third{val}_saturation_avg'] = f"The average value of the oxygen saturation (%) for the {label} third of the recording."
        third_dict[f'third{val}_saturation_std'] = f"The standard deviation value of the oxygen saturation (%) for the {label} third of the recording."
        third_dict[f'third{val}_saturation_min'] = f"The minimum value of the oxygen saturation (%) for the {label} third of the recording."
        third_dict[f'third{val}_saturation_max'] = f"The maximum value of the oxygen saturation (%) for the {label} third of the recording."

    half_dict = {}
    half_val = [1, 2]
    for val in half_val:
        if val==1:
            label = "first"
        else :
            label = "last"
        half_dict[f'half{val}_saturation_avg'] = f"The average value of the oxygen saturation (%) for the {label} half of the recording."
        half_dict[f'half{val}_saturation_std'] = f"The standard deviation value of the oxygen saturation (%) for the {label} half of the recording."
        half_dict[f'half{val}_saturation_min'] = f"The minimum value of the oxygen saturation (%) for the {label} half of the recording."
        half_dict[f'half{val}_saturation_max'] = f"The maximum value of the oxygen saturation (%) for the {label} half of the recording."

    stage_dict = {}
    for stage in stage_stats_labels:
        stage_dict[f'{stage}_saturation_avg'] = f"The average value of the oxygen saturation (%) for the {stage} stages during lights off."
        stage_dict[f'{stage}_saturation_std'] = f"The standard deviation value of the oxygen saturation (%) for the {stage} stages during lights off."
        stage_dict[f'{stage}_saturation_min'] = f"The minimum value of the oxygen saturation (%) for the {stage} stages during lights off."
        stage_dict[f'{stage}_saturation_max'] = f"The maximum value of the oxygen saturation (%) for the {stage} stages during lights off."
        for val in values_below:
            stage_dict[f"{stage}_below_{val}_min"] = f"The time spent (min) with an oxygen saturation under {val} % in stage {stage}."

    cycle_dict = {}
    for i_cycle in range(N_CYCLE):
        current_cycle_dict = \
            {
            f'cyc{i_cycle+1}_saturation_avg' : f'Cycle {i_cycle+1} - The average value of the oxygen saturation (%).',
            f'cyc{i_cycle+1}_saturation_std' : f'Cycle {i_cycle+1} - The standard deviation value of the oxygen saturation (%).',
            f'cyc{i_cycle+1}_saturation_min' : f'Cycle {i_cycle+1} - The minimum value of the oxygen saturation (%).',
            f'cyc{i_cycle+1}_saturation_max' : f'Cycle {i_cycle+1} - The maximum value of the oxygen saturation (%).'
            }

        cycle_dict = cycle_dict | current_cycle_dict

    desat_dict = \
    {            
            'desat_count' : 'The number of oxygen desaturation from lights off to lights on in asleep stages only.',
            'desat_avg_sec' : 'The average duration in sec of the oxygen desaturation events occuring in asleep stages.',
            'desat_std_sec' : 'The standard deviation value of the duration in sec of the oxygen desaturation events occuring in asleep stages.',
            'desat_med_sec' : 'The median value of the duration in sec of the oxygen desaturation events occuring in asleep stages.',
            'desat_sleep_percent' : 'The percentage of time spent in desaturation during the asleep stages.',
            'desat_ODI' : 'The Oxygen Desaturation Index (ODI) : number of desaturation per sleep hour.'
    }
    # temporal_link_dict = \
    #     {
    #         'desat_start_before_count' : 'The number of desaturations that start before the beginning of the arousal.',
    #         'desat_start_before_delay_sec' : 'Arousal starts before desaturation- The average delay between arousal and the beginning of the desaturation in sec.',
    #         'desat_end_before_count' : 'The number of desaturations that end before the beginning of the arousal.',
    #         'desat_end_before_delay_sec' : 'Desaturation ends before arousal - The average delay between desaturations and the beginning of the arousal in sec.', 
    #         'arousal_start_before_count' : 'The number of arousals that start before the beginning of the desaturation.',
    #         'arousal_start_before_delay_sec' : 'Arousal starts before desaturation- The average delay between arousal and the beginning of the desaturation in sec.',
    #         'arousal_end_before_count' : 'The number of arousals that end before the beginning of the desaturation.',
    #         'arousal_end_before_delay_sec' : 'Arousal ends before desaturation- The average delay between arousal and the beginning of the desaturation in sec.'
    #     }


    # Ajouter les tiers
    complete_dict = general_dict | total_dict | total_threshold_dict | third_dict | half_dict | stage_dict | cycle_dict | desat_dict #| temporal_link_dict
    return complete_dict

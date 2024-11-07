"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
import csv

def write_doc_file(filepath, N_CYCLES):
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        docwriter = csv.writer(csvfile, delimiter='\t')
        doc = _get_doc(N_CYCLES)
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


def _get_doc(N_CYCLES):

    general_dict = \
    {        
        'filename':'The name of the file analysed in this report.',
        'id1':'First ID',
        'id2':'Second ID',
        'first_name':'First name',
        'last_name':'Last name',
        'sex':'The sex (M, F, X)',
        'birthdate':'The birthdate of the subject, yyyy-mm-dd',
        'creation_date':'The creation date of the analysed file, yyyy-mm-dd',
        'age':'The age of the subject (Integer value)',
        'height':'The height of the subject in meters or inches.',
        'weight':'The weight of the subject in kg or lbs',
        'bmi':'Body Mass Index (kg/m²)',
        'waistline':'Waist size meters or inches.',
        'height_unit':'Unit used for the height. Possible values are: "meters/feets"',
        'weight_unit':'Unit used for the weight. Possible values are: "kg/lbs"',
        'waistline_unit':'Unit used for the waistline. Possible values are: "cm/inches"',
        'cyc_def_option':'Method used to split the sleep period in sleep cycles. The values are defined in the following "cyc_def..." parameters.  Possible values are:  "Minimum criteria"  "Aeschbach 1993"  "Feinberg 1979"  "Mice"',
        'cyc_def_include_soremp':'Include a REM sleep periods (REMP) that occur within 15 minutes of sleep onset.',
        'cyc_def_include_last_incomplete':'Include the last sleep cycle even if the NREM period (NREMP) or REMP does not meet the minimum duration criteria.',
        'cyc_def_rem_min':'Minimum duration without R stage to end the REM period.',
        'cyc_def_first_nrem_min':'Minimum duration of the first NREMP in minutes.',
        'cyc_def_mid_last_nrem_min':'Minimum duration of the middle and last NREMP in minutes.',
        'cyc_def_last_nrem_valid_min':'Minimum duration of the NREMP in minutes to validate the last sleep cycle.',
        'cyc_def_first_rem_min':'Minimum duration of the first REM period in minutes.',
        'cyc_def_mid_rem_min':'Minimum duration of the middle REM period in minutes',
        'cyc_def_last_rem_min':'Minimum duration of the last REM period in minutes',
        'cyc_def_move_end_rem':'Move the end of the REM period to the start of the following NREM period, eliminating the temporal "gap" between 2 cycles.',
        'cyc_def_sleep_stages':'List of valid stages used to define the sleep cycles:  "N1, N2, N3, R" or "N2, N3, R"',
        'epoch_sec':'Duration of an epoch in seconds, usually 30 seconds.',
        'first_epoch_time_win':'The timestamp of the first epoch.',
        'last_epoch_time_win':'The timestamp of the last epoch.',
        'record_min':'Duration of the whole record in minutes.',
        'sleep_latency_used_in_this_report_min':'The sleep latency value used to compute all statistics in the report.',
        'sleep_latency_aasm_min':'The sleep latency based on the valid sleep stages from the AASM (1,2,3,REM)',
        'sleep_latency_aeschbach_min':'The sleep latency based on the valid sleep stages from Aeschbach rules: (2,3,REM)',
        'sleep_latency_floyd_min':'The sleep latency based on the valid sleep stages from Feinberg rules: (2,3,REM)',
        'persistant_sleep_latency_min':'Persistant sleep is defined as 10 minutes of continious sleep stages. The latency is the time it takes from the beginning of the hypnogram (assumed to be the lights off) to the beginning of the 10 minutes period.',
        'sleep_latency_N1_min':'Latencies for stage N1 and N2 are base on the beginning of the of the hypnogram (scored_stages).',
        'sleep_latency_N2_min':'Latencies for stage N1 and N2 are base on the beginning of the of the hypnogram (scored_stages).',
        'sleep_latency_N3_min':'Latency of the stage N3 is based on the sleep latency.',
        'sleep_latency_R_min':'Latency of the stage REM is based on the sleep latency.',
        'total_W_count':'Number of epoch in wake during the sleep period.',
        'wake_1min_count':'Number of period of 1 minute of wake during the sleep period.',
        'wake_2min_count':'Number of period of 2 minutes of wake during the sleep period.',
        'wake_3min_count':'Number of period of 3 minutes of wake during the sleep period.',
        'wake_4min_count':'Number of period of 4 minutes of wake during the sleep period.',
        'wake_5min_count':'Number of period of 5 minutes of wake during the sleep period.',
        'total_W_min':'Total time spend in wake stage during the sleep period in minutes',
        'total_sleep_min':'The total sleep is defined as: sleep_period_min - total_W_min - (Movement duration) - Unscored_min.',
        'last_wake_min':'Duration of the last wake period of the sleep period in minutes.',
        'sleep_efficiency_percent':'Defined as the time spend in a sleep stage over the duration of the sleep period.',
        'sleep_period_min':'Duration of the sleep period defined as the time between the sleep onset and the last sleep stage (N1,N2,N3,R) in minutes.',
        'Unscored_min':'Time spent in an unscored stage during the sleep period in minutes.',
        'third1_W_min':'Time spent in wake during the first third of the sleep period in minutes.',
        'third1_N1_min':'Time spent in N1 during the first third of the sleep period in minutes.',
        'third1_N2_min':'Time spent in N2 during the first third of the sleep period in minutes.',
        'third1_N3_min':'Time spent in N3 during the first third of the sleep period in minutes.',
        'third1_R_min':'Time spent in REM stage during the first third of the sleep period in minutes.',
        'third1_Unscored_min':'Time spent in Unscored stage during the first third of the sleep period in minutes.',
        'third1_N1N2N3_min':'Time spent in NREM stages during the first third of the sleep period in minutes.',
        'third1_sleep_min':'Time spent in a sleep stage (N1,N2,N3,R) during the first third of the sleep period in minutes.',
        'third2_W_min':'Time spent in wake during the first third of the sleep period in minutes.',
        'third2_N1_min':'Time spent in N1 during the second third of the sleep period in minutes.',
        'third2_N2_min':'Time spent in N2 during the second third of the sleep period in minutes.',
        'third2_N3_min':'Time spent in N3 during the second third of the sleep period in minutes.',
        'third2_R_min':'Time spent in REM stage during the second third of the sleep period in minutes.',
        'third2_Unscored_min':'Time spent in Unscored stage during the second third of the sleep period in minutes.',
        'third2_N1N2N3_min':'Time spent in NREM stages during the second third of the sleep period in minutes.',
        'third2_sleep_min':'Time spent in a sleep stage (N1,N2,N3,R) during the second third of the sleep period in minutes.',
        'third3_W_min':'Time spent in wake during the first third of the sleep period in minutes.',
        'third3_N1_min':'Time spent in N1 during the second third of the sleep period in minutes.',
        'third3_N2_min':'Time spent in N2 during the second third of the sleep period in minutes.',
        'third3_N3_min':'Time spent in N3 during the second third of the sleep period in minutes.',
        'third3_R_min':'Time spent in REM stage during the second third of the sleep period in minutes.',
        'third3_Unscored_min':'Time spent in Unscored stage during the second third of the sleep period in minutes.',
        'third3_N1N2N3_min':'Time spent in NREM stages during the second third of the sleep period in minutes.',
        'third3_sleep_min':'Time spent in a sleep stage (N1,N2,N3,R) during the second third of the sleep period in minutes.',
        'half1_W_min':'Time spent in wake during the first half of the sleep period in minutes.',
        'half1_N1_min':'Time spent in N1 during the second half of the sleep period in minutes.',
        'half1_N2_min':'Time spent in N2 during the second half of the sleep period in minutes.',
        'half1_N3_min':'Time spent in N3 during the second half of the sleep period in minutes.',
        'half1_R_min':'Time spent in REM stage during the second half of the sleep period in minutes.',
        'half1_Unscored_min':'Time spent in Unscored stage during the second half of the sleep period in minutes.',
        'half1_N1N2N3_min':'Time spent in NREM stages during the second half of the sleep period in minutes.',
        'half1_sleep_min':'Time spent in a sleep stage (N1,N2,N3,R) during the second half of the sleep period in minutes.',
        'half2_W_min':'Time spent in wake during the first half of the sleep period in minutes.',
        'half2_N1_min':'Time spent in N1 during the second half of the sleep period in minutes.',
        'half2_N2_min':'Time spent in N2 during the second half of the sleep period in minutes.',
        'half2_N3_min':'Time spent in N3 during the second half of the sleep period in minutes.',
        'half2_R_min':'Time spent in REM stage during the second half of the sleep period in minutes.',
        'half2_Unscored_min':'Time spent in Unscored stage during the second half of the sleep period in minutes.',
        'half2_N1N2N3_min':'Time spent in NREM stages during the second half of the sleep period in minutes.',
        'half2_sleep_min':'Time spent in a sleep stage (N1,N2,N3,R) during the second half of the sleep period in minutes.',
        'total_W_min':'Total time spent in wake during the first half of the sleep period in minutes.',
        'total_N1_min':'Total time spent in N1 during the second half of the sleep period in minutes.',
        'total_N2_min':'Total time spent in N2 during the second half of the sleep period in minutes.',
        'total_N3_min':'Total time spent in N3 during the second half of the sleep period in minutes.',
        'total_R_min':'Total time spent in REM stage during the second half of the sleep period in minutes.',
        'total_Unscored_min':'Total time spent in Unscored stage during the second half of the sleep period in minutes.',
        'total_N1N2N3_min':'Total time spent in NREM stages during the second half of the sleep period in minutes.',
        'total_sleep_min':'Total time spent in a sleep stage (N1,N2,N3,R) during the second half of the sleep period in minutes.',
        'third1_W_percent':'Percentage of time spent in a wake stage during the first third of the sleep period.',
        'third1_N1_percent':'Percentage of time spent in N1 stage during the first third of the sleep period.',
        'third1_N2_percent':'Percentage of time spent in N2 stage during the first third of the sleep period.',
        'third1_N3_percent':'Percentage of time spent in N3 stage during the first third of the sleep period.',
        'third1_R_percent':'Percentage of time spent in REM stage during the first third of the sleep period.',
        'third1_Unscored_percent':'Percentage of time spent in an unscored stage during the first third of the sleep period.',
        'third1_N1N2N3_percent':'Percentage of time spent in NREM stages during the first third of the sleep period.',
        'third1_sleep_percent':'Percentage of time spent in a sleep stage (N1,N2,N3,R) during the first third of the sleep period.',
        'third2_W_percent':'Percentage of time spent in a wake stage during the second third of the sleep period.',
        'third2_N1_percent':'Percentage of time spent in N1 stage during the second third of the sleep period.',
        'third2_N2_percent':'Percentage of time spent in N2 stage during the second third of the sleep period.',
        'third2_N3_percent':'Percentage of time spent in N3 stage during the second third of the sleep period.',
        'third2_R_percent':'Percentage of time spent in REM stage during the second third of the sleep period.',
        'third2_Unscored_percent':'Percentage of time spent in an unscored stage during the second third of the sleep period.',
        'third2_N1N2N3_percent':'Percentage of time spent in NREM stages during the second third of the sleep period.',
        'third2_sleep_percent':'Percentage of time spent in a sleep stage (N1,N2,N3,R) during the second third of the sleep period.',
        'third3_W_percent':'Percentage of time spent in a wake stage during the last third of the sleep period.',
        'third3_N1_percent':'Percentage of time spent in N1 stage during the last third of the sleep period.',
        'third3_N2_percent':'Percentage of time spent in N2 stage during the last third of the sleep period.',
        'third3_N3_percent':'Percentage of time spent in N3 stage during the last third of the sleep period.',
        'third3_R_percent':'Percentage of time spent in REM stage during the last third of the sleep period.',
        'third3_Unscored_percent':'Percentage of time spent in an unscored stage during the last third of the sleep period.',
        'third3_N1N2N3_percent':'Percentage of time spent in NREM stages during the last third of the sleep period.',
        'third3_sleep_percent':'Percentage of time spent in a sleep stage (N1,N2,N3,R) during the last third of the sleep period.',
        'half1_W_percent':'Percentage of time spent in a wake stage during the first half of the sleep period.',
        'half1_N1_percent':'Percentage of time spent in N1 stage during the first half of the sleep period.',
        'half1_N2_percent':'Percentage of time spent in N2 stage during the first half of the sleep period.',
        'half1_N3_percent':'Percentage of time spent in N3 stage during the first half of the sleep period.',
        'half1_R_percent':'Percentage of time spent in REM stage during the first half of the sleep period.',
        'half1_Unscored_percent':'Percentage of time spent in an unscored stage during the first half of the sleep period.',
        'half1_N1N2N3_percent':'Percentage of time spent in NREM stages during the first half of the sleep period.',
        'half1_sleep_percent':'Percentage of time spent in a sleep stage (N1,N2,N3,R) during the first half of the sleep period.',
        'half2_W_percent':'Percentage of time spent in a wake stage during the second half of the sleep period.',
        'half2_N1_percent':'Percentage of time spent in N1 stage during the second half of the sleep period.',
        'half2_N2_percent':'Percentage of time spent in N2 stage during the second half of the sleep period.',
        'half2_N3_percent':'Percentage of time spent in N3 stage during the second half of the sleep period.',
        'half2_R_percent':'Percentage of time spent in REM stage during the second half of the sleep period.',
        'half2_Unscored_percent':'Percentage of time spent in an unscored stage during the second half of the sleep period.',
        'half2_N1N2N3_percent':'Percentage of time spent in NREM stages during the second half of the sleep period.',
        'half2_sleep_percent':'Percentage of time spent in a sleep stage (N1,N2,N3,R) during the second half of the sleep period.',
        'total_W_percent':'Percentage of time spent in a wake stage during the sleep period.',
        'total_N1_percent':'Percentage of time spent in N1 stage during the sleep period.',
        'total_N2_percent':'Percentage of time spent in N2 stage during the sleep period.',
        'total_N3_percent':'Percentage of time spent in N3 stage during the sleep period.',
        'total_R_percent':'Percentage of time spent in REM stage during the sleep period.',
        'total_Unscored_percent':'Percentage of time spent in an unscored stage during the sleep period.',
        'total_N1N2N3_percent':'Percentage of time spent in NREM stages during the sleep period.',
        'total_sleep_percent':'Percentage of time spent in a sleep stage (N1,N2,N3, REM) during the sleep period.',
        'third1_W_percent':'The percentage of the total Wake stage spent during the first third of the sleep period.',
        'third1_N1_percent':'The percentage of the total N1 stage spent during the first third of the sleep period.',
        'third1_N2_percent':'The percentage of the total N2 stage spent during the first third of the sleep period.',
        'third1_N3_percent':'The percentage of the total N3 stage spent during the first third of the sleep period.',
        'third1_R_percent':'The percentage of the total R stage spent during the first third of the sleep period.',
        'third1_Unscored_percent':'The percentage of the total Unscored stage spent during the first third of the sleep period.',
        'third1_N1N2N3_percent':'The percentage of the total NREM stages spent during the first third of the sleep period.',
        'third2_W_percent':'The percentage of the total Wake stage spent during the second third of the sleep period.',
        'third2_N1_percent':'The percentage of the total N1 stage spent during the second third of the sleep period.',
        'third2_N2_percent':'The percentage of the total N2 stage spent during the second third of the sleep period.',
        'third2_N3_percent':'The percentage of the total N3 stage spent during the second third of the sleep period.',
        'third2_R_percent':'The percentage of the total R stage spent during the second third of the sleep period.',
        'third2_Unscored_percent':'The percentage of the total Unscored stage spent during the second third of the sleep period.',
        'third2_N1N2N3_percent':'The percentage of the total NREM stages spent during the second third of the sleep period.',
        'third3_W_percent':'The percentage of the total Wake stage spent during the last third of the sleep period.',
        'third3_N1_percent':'The percentage of the total N1 stage spent during the last third of the sleep period.',
        'third3_N2_percent':'The percentage of the total N2 stage spent during the last third of the sleep period.',
        'third3_N3_percent':'The percentage of the total N3 stage spent during the last third of the sleep period.',
        'third3_R_percent':'The percentage of the total R stage spent during the last third of the sleep period.',
        'third3_Unscored_percent':'The percentage of the total Unscored stage spent during the last third of the sleep period.',
        'third3_N1N2N3_percent':'The percentage of the total NREM stages spent during the last third of the sleep period.',
        'half1_W_percent':'The percentage of the total Wake stage spent during the first half of the sleep period.',
        'half1_N1_percent':'The percentage of the total N1 stage spent during the first half of the sleep period.',
        'half1_N2_percent':'The percentage of the total N2 stage spent during the first half of the sleep period.',
        'half1_N3_percent':'The percentage of the total N3 stage spent during the first half of the sleep period.',
        'half1_R_percent':'The percentage of the total R stage spent during the first half of the sleep period.',
        'half1_Unscored_percent':'The percentage of the total Unscored stage spent during the first half of the sleep period.',
        'half1_N1N2N3_percent':'The percentage of the total NREM stages spent during the first half of the sleep period.',
        'half2_W_percent':'The percentage of the total Wake stage spent during the second half of the sleep period.',
        'half2_N1_percent':'The percentage of the total N1 stage spent during the second half of the sleep period.',
        'half2_N2_percent':'The percentage of the total N2 stage spent during the second half of the sleep period.',
        'half2_N3_percent':'The percentage of the total N3 stage spent during the second half of the sleep period.',
        'half2_R_percent':'The percentage of the total R stage spent during the second half of the sleep period.',
        'half2_Unscored_percent':'The percentage of the total Unscored stage spent during the second half of the sleep period.',
        'half2_N1N2N3_percent':'The percentage of the total NREM stages spent during the second half of the sleep period.',
        'sleep_cycle_count':'Number of sleep cycles detected based on the sleep cycle parameters used.'
    }


    cyc_len_dict = {}
    for i_cycle in range(N_CYCLES):
        current_cycle_len_dict = \
        {        
        f'cyc{i_cycle+1}_nrem_min' : f'Cycle {i_cycle+1} - Time spend in NREM period during the first cycle.',
        f'cyc{i_cycle+1}_R_min' : f'Cycle {i_cycle+1} - Time spend in REM stage during the first cycle.',
        f'cyc{i_cycle+1}_min' : f'Cycle {i_cycle+1} - Duration of the first cycle',
        }
        cyc_len_dict = cyc_len_dict | current_cycle_len_dict


    rem_total_dict = \
    { 
        'rem_intervals_mean':'Mean of intervals between REM periods.',
        'rem_total_R_min':'Total time spend in REM stage during all REM periods in minutes.',
        'rem_total_N1N2N3_min':'Total time spend in NREM stages during all REM periods in minutes.',
        'rem_total_W_min':'Total time spend in wake stage during all REM periods in minutes.',
        'rem_total_Unscored_min':'Total time spend in unscored stage during all REM periods in minutes.',
        'rem_total_time_min':'Total time spend all REM periods in minutes.',
        'rem_fragmentation_count':'Number of REM fragments. A continious sequence of REM stages count as one fragment.',
        'rem_R_efficiency_percent':'Ratio of time spent in a REM stage during all REM periods.',
        'rem_count':'Number of REM periods.',
        'rem1_interval_min':'Delay between the sleep onset and the first REM period in minutes.',
        'rem1_R_min':'Time spent in REM stage during the REM period in minutes.',
        'rem1_N1N2N3_min':'Time spent in a NREM stages during the REM period in minutes.',
        'rem1_W_min':'Time spent in wake stage during the REM period in minutes.',
        'rem1_Unscored_min':'Time spent in unscored stage during the REM period in minutes.',
        'rem1_min':'Duration of the REM period in minutes.',
        'rem1_fragmentation_count':'Fragmentation count during the REM period. A continious sequence of REM stages count as one fragment.',
        'rem1_efficiency_percent':'Percent of time spend in REM stage during the REM period.'
    }


    rem_dict = {}
    for i_cycle in range(N_CYCLES-1):
        current_rem_dict = \
    {        
        f'rem{i_cycle+2}_interval_min' : f'REM {i_cycle+2} - Time interval in minutes between the beginning of a REM period and the beginning of the previous REM period.',
        f'rem{i_cycle+2}_R_min' : f'REM {i_cycle+2} - Time spent in REM stage during the REM period in minutes.',
        f'rem{i_cycle+2}_N1N2N3_min' : f'REM {i_cycle+2} - Time spent in a NREM stages during the REM period in minutes.',
        f'rem{i_cycle+2}_W_min' : f'REM {i_cycle+2} - Time spent in wake stage during the REM period in minutes.',
        f'rem{i_cycle+2}_Unscored_min' : f'REM {i_cycle+2} - Time spent in unscored stage during the REM period in minutes.',
        f'rem{i_cycle+2}_min' : f'REM {i_cycle+2} - Duration of the REM period in minutes.',
        f'rem{i_cycle+2}_fragmentation_count' : f'REM {i_cycle+2} - Fragmentation count during the REM period. A continious sequence of REM stages count as one fragment.',
        f'rem{i_cycle+2}_efficiency_percent' : f'REM {i_cycle+2} - Percent of time spend in REM stage during the REM period.',
    }
        rem_dict = rem_dict | current_rem_dict


    transition_dict = \
    {
        'W_to_N1_count':'Count of transition between two stages during the whole recording.',
        'W_to_N2_count':'Count of transition between two stages during the whole recording.',
        'W_to_N3_count':'Count of transition between two stages during the whole recording.',
        'W_to_R_count':'Count of transition between two stages during the whole recording.',
        'W_to_Unscored_count':'Count of transition between two stages during the whole recording.',
        'W_to_any_count':'Count of transition between two stages during the whole recording.',
        'N1_to_W_count':'Count of transition between two stages during the whole recording.',
        'N1_to_N2_count':'Count of transition between two stages during the whole recording.',
        'N1_to_N3_count':'Count of transition between two stages during the whole recording.',
        'N1_to_R_count':'Count of transition between two stages during the whole recording.',
        'N1_to_Unscored_count':'Count of transition between two stages during the whole recording.',
        'N1_to_any_count':'Count of transition between two stages during the whole recording.',
        'N2_to_W_count':'Count of transition between two stages during the whole recording.',
        'N2_to_N1_count':'Count of transition between two stages during the whole recording.',
        'N2_to_N3_count':'Count of transition between two stages during the whole recording.',
        'N2_to_R_count':'Count of transition between two stages during the whole recording.',
        'N2_to_Unscored_count':'Count of transition between two stages during the whole recording.',
        'N2_to_any_count':'Count of transition between two stages during the whole recording.',
        'N3_to_W_count':'Count of transition between two stages during the whole recording.',
        'N3_to_N1_count':'Count of transition between two stages during the whole recording.',
        'N3_to_N2_count':'Count of transition between two stages during the whole recording.',
        'N3_to_R_count':'Count of transition between two stages during the whole recording.',
        'N3_to_Unscored_count':'Count of transition between two stages during the whole recording.',
        'N3_to_any_count':'Count of transition between two stages during the whole recording.',
        'R_to_W_count':'Count of transition between two stages during the whole recording.',
        'R_to_N1_count':'Count of transition between two stages during the whole recording.',
        'R_to_N2_count':'Count of transition between two stages during the whole recording.',
        'R_to_N3_count':'Count of transition between two stages during the whole recording.',
        'R_to_Unscored_count':'Count of transition between two stages during the whole recording.',
        'R_to_any_count':'Count of transition between two stages during the whole recording.',
        'Unscored_to_W_count':'Count of transition between two stages during the whole recording.',
        'Unscored_to_N1_count':'Count of transition between two stages during the whole recording.',
        'Unscored_to_N2_count':'Count of transition between two stages during the whole recording.',
        'Unscored_to_N3_count':'Count of transition between two stages during the whole recording.',
        'Unscored_to_R_count':'Count of transition between two stages during the whole recording.',
        'Unscored_to_any_count':'Count of transition between two stages during the whole recording.',
        'any_to_any_count':'Total count of all transitions between any two stages.'
    }

    # Concatenate all the dictionaries
    stats_dict = general_dict | cyc_len_dict | rem_total_dict | rem_dict | transition_dict

    return stats_dict
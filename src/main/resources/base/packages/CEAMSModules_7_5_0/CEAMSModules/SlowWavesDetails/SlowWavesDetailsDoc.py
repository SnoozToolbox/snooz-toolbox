"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
import csv
import re

def write_slow_wave_characteristics_info_file(filepath):
    """
    Write info file for slow wave characteristics TSV file.
    Describes each column in the slow wave characteristics export.
    """
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        docwriter = csv.writer(csvfile, delimiter='\t')

        doc = _get_slow_wave_characteristics_doc()

        for i, (k, v) in enumerate(doc.items()):
            row_name = excel_column_name(i+1)
            docwriter.writerow([row_name, k, v])


def write_doc_file(filepath, N_CYCLE, N_HOURS=0, unscored=False):
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        docwriter = csv.writer(csvfile, delimiter='\t')

        doc = _get_doc(N_CYCLE, N_HOURS, unscored)

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


def _get_slow_wave_characteristics_doc():
    """
    Get documentation dictionary for individual slow wave characteristics.
    """
    slow_wave_char_dict = {
        'group': 'Event group (slow wave)',
        'name': 'Slow wave event name (specific to the detection algorithm)',
        'cycle': 'Sleep cycle number (1-based) during which the slow wave occurred (NaN for unscored)',
        'stage': 'Sleep stage during which the slow wave occurred (1=N1, 2=N2, 3=N3, 5=REM, 9=Unscored)',
        'start_sec': 'Slow wave start time (s)',
        'duration_sec': 'Slow wave total duration (s)',
        'channels': 'Channel label(s) where the slow wave was detected',
        'pkpk_amp_uV': 'Slow wave peak-to-peak amplitude (uV)',
        'freq_Hz': 'Slow wave frequency (Hz), inverse of the duration',
        'neg_amp_uV': 'Slow wave negative amplitude (uV)',
        'neg_sec': 'Slow wave negative half-wave duration (s)',
        'neg_peak_sec': 'Duration (s) from slow wave onset to the negative peak',
        'pos_sec': 'Slow wave positive half-wave duration (s)',
        'pos_peak_sec': 'Duration (s) from slow wave onset to the positive peak',
        'slope_0_min': 'Slope from slow wave onset to the negative peak (uV/s)',
        'slope_min_max': 'Slope from the negative peak to the positive peak (uV/s)',
        'slope_max_0': 'Slope from the positive peak to the end of the slow wave (uV/s)',
        'trans_freq_Hz': 'Transition frequency (Hz), calculated as the inverse of twice the duration between the negative and positive peaks. Formula: 1/(2*(pos_peak_sec-neg_peak_sec))',
    }
    return slow_wave_char_dict


def _get_doc(N_CYCLE, N_HOURS=0, unscored=False):

    identification_dict = \
    {
            'filename' : 'PSG filename',
            'id1'      : 'subject identification'
    }

    def_cycle_dict = \
    {
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

    stage_definitions = (
        ('N1', 'N1 stage'),
        ('N2', 'N2 stage'),
        ('N3', 'N3 stage'),
        ('N2N3', 'N2 and N3 stage'),
        ('NREM', 'NREM stage (N1, N2, N3)'),
        ('R', 'REM stage'),
    )

    total_stage_dict = {}
    for stage_name, stage_definition in stage_definitions:
        rem_exclusion = '.' if stage_name == 'R' else ' minus the REM periods if excluded.'
        total_stage_dict |= {
            f'total_{stage_name}_valid_min': f'Valid (no artifact) period for detection - Valid duration (min) of the sleep period in {stage_definition}{rem_exclusion}',
            f'total_{stage_name}_sw_count': f'Total - SW count in {stage_definition}.',
            f'total_{stage_name}_sw_sec': f'Total - Average slow wave duration (s) in {stage_definition}.',
            f'total_{stage_name}_pkpk_amp_uV': f'Total - Average slow wave peak-to-peak amplitude (uV) in {stage_definition}.',
            f'total_{stage_name}_freq_Hz': f'Total - Slow wave frequency (Hz) (inverse of the duration) in {stage_definition}.',
            f'total_{stage_name}_neg_amp_uV': f'Total - Average slow wave negative peak amplitude (uV) in {stage_definition}.',
            f'total_{stage_name}_neg_sec': f'Total - Average slow wave negative duration (s) in {stage_definition}.',
            f'total_{stage_name}_neg_peak_sec': f'Total - Average slow wave duration (s) from onset to the negative peak in {stage_definition}.',
            f'total_{stage_name}_pos_sec': f'Total - Average slow wave positive duration (s) in {stage_definition}.',
            f'total_{stage_name}_pos_peak_sec': f'Total - Average slow wave duration (s) from onset to the positive peak in {stage_definition}.',
            f'total_{stage_name}_slope_0_min': f'Total - Average slow wave slope (uV/s) from 0 crossing to the min of the negative component in {stage_definition}.',
            f'total_{stage_name}_slope_min_max': f'Total - Average slow wave slope (uV/s) from min to the max in {stage_definition}.',
            f'total_{stage_name}_slope_max_0': f'Total - Average slow wave slope (uV/s) from max of positive to the 0 crossing in {stage_definition}.',
            f'total_{stage_name}_trans_freq_Hz': f'Total -  Average slow wave transition frequency (Hz) in {stage_definition}.',
            f'total_{stage_name}_sw_density': f'Total - Slow wave density (count/min) in {stage_definition}.',
        }

    # The valid duration can change across channels because of the artifact detection
    total_dict = total_stage_dict | \
    {
            'total_valid_min' : 'Valid (no artifact) period for detection - Valid duration (min) of the sleep stage selected minus thoses included in REM periods if remps are excluded.',

            'total_sw_count' : 'Total - SW count in all stages.',
            'total_sw_sec' : 'Total - Average slow wave duration (s)',
            'total_pkpk_amp_uV' : 'Total - Average slow wave peak-to-peak amplitude (uV)',
            'total_freq_Hz' : 'Total - Slow wave frequency (Hz) (inverse of the duration).',
            'total_neg_amp_uV' : 'Total - Average slow wave negative peak amplitude (uV).',
            'total_neg_sec' : 'Total - Average slow wave negative duration (s)',
            'total_neg_peak_sec' : 'Total - Average slow wave duration (s) from onset to the negative peak',
            'total_pos_sec' : 'Total -  Average slow wave positive duration (s)',
            'total_pos_peak_sec' : 'Total - Average slow wave duration (s) from onset to the positive peak',
            'total_slope_0_min' : 'Total -  Average slow wave slope (uV/s) from 0 crossing to the min of the negative component.',
            'total_slope_min_max' : 'Total -  Average slow wave slope (uV/s) from min to the max.',
            'total_slope_max_0' : 'Total -  Average slow wave slope (uV/s) from max of positive to the 0 crossing.',
            'total_trans_freq_Hz' : 'Total -   Average slow wave transition frequency (Hz)',
            'total_sw_density' : 'Total - Slow wave density (count/min)'
    }

    cycle_dict = {}
    for i_cycle in range(N_CYCLE):
        current_cycle_dict = {
            f'cyc{i_cycle+1}_valid_min' : f'Cycle {i_cycle+1} - Valid (no artifact) duration (min) available for detection minus the REM periods if excluded.',
            f'cyc{i_cycle+1}_min' : f'Cycle {i_cycle+1} duration (min) minus the REM periods if excluded.',
            f'cyc{i_cycle+1}_sw_count' : f'Cycle {i_cycle+1} - Slow wave count in all stages.',
            f'cyc{i_cycle+1}_sw_sec' : f'Cycle {i_cycle+1} - Average slow wave duration (s)',
            f'cyc{i_cycle+1}_pkpk_amp_uV' : f'Cycle {i_cycle+1} - Average slow wave peak-to-peak amplitude (uV)',
            f'cyc{i_cycle+1}_freq_Hz' : f'Cycle {i_cycle+1} - Slow wave frequency (Hz) (inverse of the duration).',
            f'cyc{i_cycle+1}_neg_amp_uV' : f'Cycle {i_cycle+1} - Average slow wave negative peak amplitude (uV).',
            f'cyc{i_cycle+1}_neg_sec' : f'Cycle {i_cycle+1} - Average slow wave negative duration (s)',
            f'cyc{i_cycle+1}_neg_peak_sec' : f'Cycle {i_cycle+1} - Average slow wave duration (s) from onset to the negative peak',
            f'cyc{i_cycle+1}_pos_sec' : f'Cycle {i_cycle+1} -  Average slow wave positive duration (s)',
            f'cyc{i_cycle+1}_pos_peak_sec' : f'Cycle {i_cycle+1} - Average slow wave duration (s) from onset to the positive peak',
            f'cyc{i_cycle+1}_slope_0_min' : f'Cycle {i_cycle+1} -  Average slow wave slope (uV/s) from 0 crossing to the min of the negative component.',
            f'cyc{i_cycle+1}_slope_min_max' : f'Cycle {i_cycle+1} -  Average slow wave slope (uV/s) from min to the max.',
            f'cyc{i_cycle+1}_slope_max_0' : f'Cycle {i_cycle+1} -  Average slow wave slope (uV/s) from max of positive to the 0 crossing.',
            f'cyc{i_cycle+1}_trans_freq_Hz' : f'Cycle {i_cycle+1} -   Average slow wave transition frequency (Hz)',
            f'cyc{i_cycle+1}_sw_density' : f'Cycle {i_cycle+1} - Slow wave density (count/min)'
        }
        for stage_name, stage_definition in stage_definitions:
            rem_exclusion = '.' if stage_name == 'R' else ' minus the REM periods if excluded.'
            current_cycle_dict |= {
                f'cyc{i_cycle+1}_{stage_name}_valid_min': f'Cycle {i_cycle+1} - Valid (no artifact) duration (min) in {stage_definition} available for detection{rem_exclusion}',
                f'cyc{i_cycle+1}_{stage_name}_sw_count': f'Cycle {i_cycle+1} - Slow wave count in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_sw_sec': f'Cycle {i_cycle+1} - Average slow wave duration (s) in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_pkpk_amp_uV': f'Cycle {i_cycle+1} - Average slow wave peak-to-peak amplitude (uV) in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_freq_Hz': f'Cycle {i_cycle+1} - Slow wave frequency (Hz) (inverse of the duration) in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_neg_amp_uV': f'Cycle {i_cycle+1} - Average slow wave negative peak amplitude (uV) in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_neg_sec': f'Cycle {i_cycle+1} - Average slow wave negative duration (s) in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_neg_peak_sec': f'Cycle {i_cycle+1} - Average slow wave duration (s) from onset to the negative peak in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_pos_sec': f'Cycle {i_cycle+1} - Average slow wave positive duration (s) in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_pos_peak_sec': f'Cycle {i_cycle+1} - Average slow wave duration (s) from onset to the positive peak in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_slope_0_min': f'Cycle {i_cycle+1} - Average slow wave slope (uV/s) from 0 crossing to the min of the negative component in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_slope_min_max': f'Cycle {i_cycle+1} - Average slow wave slope (uV/s) from min to the max in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_slope_max_0': f'Cycle {i_cycle+1} - Average slow wave slope (uV/s) from max of positive to the 0 crossing in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_trans_freq_Hz': f'Cycle {i_cycle+1} -  Average slow wave transition frequency (Hz) in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_sw_density': f'Cycle {i_cycle+1} - Slow wave density (count/min) in {stage_definition}.',
            }
        cycle_dict = cycle_dict | current_cycle_dict
    
    # Add clock hour documentation
    clock_hour_dict = {}
    for i_hour in range(N_HOURS):
        current_hour_dict = {
            f'clock_h{i_hour+1}_valid_min' : f'Hour {i_hour+1} - Valid (no artifact) duration (min) available for detection minus the REM periods if excluded.',
            f'clock_h{i_hour+1}_min' : f'Hour {i_hour+1} duration (min) minus the REM periods if excluded.',
            f'clock_h{i_hour+1}_sw_count' : f'Hour {i_hour+1} - Slow wave count in all stages.',
            f'clock_h{i_hour+1}_sw_sec' : f'Hour {i_hour+1} - Average slow wave duration (s) in all stages.',
            f'clock_h{i_hour+1}_pkpk_amp_uV' : f'Hour {i_hour+1} - Average slow wave peak-to-peak amplitude (µV) in all stages.',
            f'clock_h{i_hour+1}_freq_Hz' : f'Hour {i_hour+1} - Average slow wave frequency (Hz) in all stages.',
            f'clock_h{i_hour+1}_neg_amp_uV' : f'Hour {i_hour+1} - Average slow wave negative amplitude (µV) in all stages.',
            f'clock_h{i_hour+1}_neg_sec' : f'Hour {i_hour+1} - Average slow wave negative duration (s) in all stages.',
            f'clock_h{i_hour+1}_neg_peak_sec' : f'Hour {i_hour+1} - Average slow wave duration (s) from onset to the negative peak in all stages.',
            f'clock_h{i_hour+1}_pos_sec' : f'Hour {i_hour+1} - Average slow wave positive duration (s) in all stages.',
            f'clock_h{i_hour+1}_pos_peak_sec' : f'Hour {i_hour+1} - Average slow wave duration (s) from onset to the positive peak in all stages.',
            f'clock_h{i_hour+1}_slope_0_min' : f'Hour {i_hour+1} - Average slow wave slope (uV/s) from 0 to min of negative in all stages.',
            f'clock_h{i_hour+1}_slope_min_max' : f'Hour {i_hour+1} - Average slow wave slope (uV/s) from min of negative to max of positive in all stages.',
            f'clock_h{i_hour+1}_slope_max_0' : f'Hour {i_hour+1} - Average slow wave slope (uV/s) from max of positive to the 0 crossing in all stages.',
            f'clock_h{i_hour+1}_trans_freq_Hz' : f'Hour {i_hour+1} - Average slow wave transition frequency (Hz) in all stages.',
            f'clock_h{i_hour+1}_sw_density' : f'Hour {i_hour+1} - Slow wave density (count/min)'
        }
        for stage_name, stage_definition in stage_definitions:
            rem_exclusion = '.' if stage_name == 'R' else ' minus the REM periods if excluded.'
            current_hour_dict |= {
                f'clock_h{i_hour+1}_{stage_name}_valid_min': f'Hour {i_hour+1} - Valid (no artifact) duration (min) in {stage_definition} available for detection{rem_exclusion}',
                f'clock_h{i_hour+1}_{stage_name}_sw_count': f'Hour {i_hour+1} - Slow wave count in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_sw_sec': f'Hour {i_hour+1} - Average slow wave duration (s) in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_pkpk_amp_uV': f'Hour {i_hour+1} - Average slow wave peak-to-peak amplitude (µV) in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_freq_Hz': f'Hour {i_hour+1} - Average slow wave frequency (Hz) in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_neg_amp_uV': f'Hour {i_hour+1} - Average slow wave negative amplitude (µV) in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_neg_sec': f'Hour {i_hour+1} - Average slow wave negative duration (s) in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_neg_peak_sec': f'Hour {i_hour+1} - Average slow wave duration (s) from onset to the negative peak in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_pos_sec': f'Hour {i_hour+1} - Average slow wave positive duration (s) in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_pos_peak_sec': f'Hour {i_hour+1} - Average slow wave duration (s) from onset to the positive peak in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_slope_0_min': f'Hour {i_hour+1} - Average slow wave slope (uV/s) from 0 to min of negative in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_slope_min_max': f'Hour {i_hour+1} - Average slow wave slope (uV/s) from min of negative to max of positive in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_slope_max_0': f'Hour {i_hour+1} - Average slow wave slope (uV/s) from max of positive to the 0 crossing in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_trans_freq_Hz': f'Hour {i_hour+1} - Average slow wave transition frequency (Hz) in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_sw_density': f'Hour {i_hour+1} - Slow wave density (count/min) in {stage_definition}.',
            }
        clock_hour_dict = clock_hour_dict | current_hour_dict
    
    # Add stage hour documentation
    stage_hour_dict = {}
    for i_hour in range(N_HOURS):
        current_stage_hour_dict = {
            f'stage_h{i_hour+1}_min' : f'Stage Hour {i_hour+1} duration (min) minus the REM periods if excluded.',
            f'stage_h{i_hour+1}_sw_count' : f'Stage Hour {i_hour+1} - Slow wave count in all stages.',
            f'stage_h{i_hour+1}_sw_sec' : f'Stage Hour {i_hour+1} - Average slow wave duration (s) in all stages.',
            f'stage_h{i_hour+1}_pkpk_amp_uV' : f'Stage Hour {i_hour+1} - Average slow wave peak-to-peak amplitude (µV) in all stages.',
            f'stage_h{i_hour+1}_freq_Hz' : f'Stage Hour {i_hour+1} - Average slow wave frequency (Hz) in all stages.',
            f'stage_h{i_hour+1}_neg_amp_uV' : f'Stage Hour {i_hour+1} - Average slow wave negative amplitude (µV) in all stages.',
            f'stage_h{i_hour+1}_neg_sec' : f'Stage Hour {i_hour+1} - Average slow wave negative duration (s) in all stages.',
            f'stage_h{i_hour+1}_neg_peak_sec' : f'Stage Hour {i_hour+1} - Average slow wave duration (s) from onset to the negative peak in all stages.',
            f'stage_h{i_hour+1}_pos_sec' : f'Stage Hour {i_hour+1} - Average slow wave positive duration (s) in all stages.',
            f'stage_h{i_hour+1}_pos_peak_sec' : f'Stage Hour {i_hour+1} - Average slow wave duration (s) from onset to the positive peak in all stages.',
            f'stage_h{i_hour+1}_slope_0_min' : f'Stage Hour {i_hour+1} - Average slow wave slope (uV/s) from 0 to min of negative in all stages.',
            f'stage_h{i_hour+1}_slope_min_max' : f'Stage Hour {i_hour+1} - Average slow wave slope (uV/s) from min of negative to max of positive in all stages.',
            f'stage_h{i_hour+1}_slope_max_0' : f'Stage Hour {i_hour+1} - Average slow wave slope (uV/s) from max of positive to the 0 crossing in all stages.',
            f'stage_h{i_hour+1}_trans_freq_Hz' : f'Stage Hour {i_hour+1} - Average slow wave transition frequency (Hz) in all stages.',
            f'stage_h{i_hour+1}_sw_density' : f'Stage Hour {i_hour+1} - Slow wave density (count/min) in all stages.'
        }
        for stage_name, stage_definition in stage_definitions:
            rem_exclusion = '.' if stage_name == 'R' else ' minus the REM periods if excluded.'
            current_stage_hour_dict |= {
                f'stage_h{i_hour+1}_{stage_name}_valid_min': f'Stage Hour {i_hour+1} - Valid (no artifact) duration (min) in {stage_definition} available for detection{rem_exclusion}',
                f'stage_h{i_hour+1}_{stage_name}_sw_count': f'Stage Hour {i_hour+1} - Slow wave count in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_sw_sec': f'Stage Hour {i_hour+1} - Average slow wave duration (s) in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_pkpk_amp_uV': f'Stage Hour {i_hour+1} - Average slow wave peak-to-peak amplitude (µV) in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_freq_Hz': f'Stage Hour {i_hour+1} - Average slow wave frequency (Hz) in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_neg_amp_uV': f'Stage Hour {i_hour+1} - Average slow wave negative amplitude (µV) in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_neg_sec': f'Stage Hour {i_hour+1} - Average slow wave negative duration (s) in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_neg_peak_sec': f'Stage Hour {i_hour+1} - Average slow wave duration (s) from onset to the negative peak in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_pos_sec': f'Stage Hour {i_hour+1} - Average slow wave positive duration (s) in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_pos_peak_sec': f'Stage Hour {i_hour+1} - Average slow wave duration (s) from onset to the positive peak in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_slope_0_min': f'Stage Hour {i_hour+1} - Average slow wave slope (uV/s) from 0 to min of negative in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_slope_min_max': f'Stage Hour {i_hour+1} - Average slow wave slope (uV/s) from min of negative to max of positive in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_slope_max_0': f'Stage Hour {i_hour+1} - Average slow wave slope (uV/s) from max of positive to the 0 crossing in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_trans_freq_Hz': f'Stage Hour {i_hour+1} - Average slow wave transition frequency (Hz) in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_sw_density': f'Stage Hour {i_hour+1} - Slow wave density (count/min) in {stage_definition}.',
            }
        stage_hour_dict = stage_hour_dict | current_stage_hour_dict
    
    # Unscored data have no sleep stage/cycle: keep only the stage-agnostic stats
    if unscored:
        stage_pattern = re.compile(r'^total_(N1|N2|N3|N2N3|NREM|R)_')
        total_generic_dict = {k: v for k, v in total_dict.items() if not stage_pattern.match(k)}

        clock_stage_pattern = re.compile(r'^clock_h\d+_(N1|N2|N3|N2N3|NREM|R)_')
        clock_h_generic_dict = {k: v for k, v in clock_hour_dict.items() if not clock_stage_pattern.match(k)}

        complete_dict = identification_dict | detector_dict | channel_dict | total_generic_dict | clock_h_generic_dict
        return complete_dict

    complete_dict = identification_dict | def_cycle_dict | detector_dict | channel_dict | sleep_car_dict | total_dict | cycle_dict | clock_hour_dict | stage_hour_dict
    return complete_dict

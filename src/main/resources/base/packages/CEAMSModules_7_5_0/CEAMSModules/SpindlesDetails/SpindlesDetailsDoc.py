"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
import csv

def write_doc_file(filepath, N_CYCLE, spindle_event_name, N_HOURS=0):
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        docwriter = csv.writer(csvfile, delimiter='\t')

        doc = _get_doc(N_CYCLE, spindle_event_name, N_HOURS)

        for i, (k, v) in enumerate(doc.items()):
            row_name = excel_column_name(i+1)
            docwriter.writerow([row_name,k,v])


def write_spindle_characteristics_info_file(filepath):
    """
    Write info file for spindle characteristics TSV file.
    Describes each column in the spindle characteristics export.
    """
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        docwriter = csv.writer(csvfile, delimiter='\t')

        doc = _get_spindle_characteristics_doc()

        for i, (k, v) in enumerate(doc.items()):
            row_name = excel_column_name(i+1)
            docwriter.writerow([row_name, k, v])


def excel_column_name(number):
    column_name = ""
    while number > 0:
        remainder = (number - 1) % 26  # Subtract 1 to account for 0-based indexing
        column_name = chr(65 + remainder) + column_name  # 65 is the ASCII code for 'A'
        number = (number - 1) // 26
    return column_name


def _get_spindle_characteristics_doc():
    """
    Get documentation dictionary for individual spindle characteristics.
    """
    spindle_char_dict = {
        'group': 'Event group (spindle)',
        'name': 'Spindle event name (specific to the detection algorithm)',
        'start_sec': 'Spindle start time (s)',
        'duration_sec': 'Spindle total duration (s)',
        'channels': 'Channel label(s) where the spindle was detected',
        'stage': 'Sleep stage during which the spindle occurred (1=N1, 2=N2, 3=N3, 5=REM)',
        'cycle': 'Sleep cycle number (1-based) during which the spindle occurred',
        'dom_freq_Hz': 'Spindle dominant frequency (Hz), where spectral energy is maximum',
        'avg_freq_Hz': 'Spindle average frequency (Hz), counting peaks',
        'amp_pkpk_uV': 'Spindle peak-to-peak amplitude (uV)',
        'peak_sec': 'Duration (s) from spindle onset to the maximum peak-to-peak amplitude',
        'amp_rms_uV': 'Spindle Root Mean Square (RMS) amplitude (uV)',
        'rms_dur_uVsec': 'RMS Spindle Activity Index component: RMS amplitude x spindle duration (uV sec)',
    }
    return spindle_char_dict


def _get_doc(N_CYCLE, spindle_event_name, N_HOURS=0):
    general_dict_1 = \
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

            'min_sec' : 'Minimum duration of the spindle in sec.',
            'max_sec' : 'Maximum duration of the spindle in sec.',
            'sleep_stage_sel' : 'Sleep stages selection to detect spindles in.',
            'detect_in_cycle' : 'Flag to detect spindle in sleep cycles only.',
            'detect_exclude_remp' : 'Flag to exclude rem period from the spindle detection.'
    }
    
    if ('a4' in spindle_event_name.lower()) or ('martin' in spindle_event_name.lower()):
        algo_dict = \
        {
                'spindle_event_name' : 'Spindle event name (specific to the detection algorithm).',
                'threshold' : 'Threshold (percentile) specific to martin detector',
                'threshold_per_cycle' : 'Flag to compute a threshold for each sleep cycle.',
                'precision_on' : 'Flag to precise the onset and the duration of the spindle based on RMS sliding windows.',
        }
    elif ('a7' in spindle_event_name.lower()) or ('lacourse' in spindle_event_name.lower()):
        algo_dict = \
        {
                'spindle_event_name' : 'Spindle event name (specific to the detection algorithm).',
                'thresh_abs_sigma_pow_uv2': 'Threshold (uv2) for the absolute (mean squared) sigma power (log10)',
                'thresh_rel_sigma_pow_z': 'Threshold (z-score) for the relative sigma power (z(log10(PSA:11-16Hz/PSA:4.5-30Hz)))',
                'thresh_sigma_cov_z' : 'Threshold (z-score) for the sigma covariance between the broad band (EEGbf) and the sigma (EEGs) signal (z(log10(cov(EEGbf, EEGs))))',
                'thresh_sigma_cor_perc' : 'Threshold (percentile) for the sigma correlation between the broad band (EEGbf) and the sigma (EEGs) signal cov(EEGbf, EEGs)/(std(EEGbf)*std(EEGs))',
        }
    elif ('sumo' in spindle_event_name.lower()):
        algo_dict = \
        {
                'spindle_event_name' : 'Spindle event name (specific to the detection algorithm).',
        }
    general_dict_2 = \
    {
            'artefact_group_name_list' : 'List of groups and names of the artifact excluded from the spindle detection',

            'chan_label' : 'The label of the channel.',
            'chan_fs' : 'The sampling rate (Hz) of the channel.',

            'sleep_cycle_count' : 'Number of sleep cycles.'
    }
    # Concatenate dictionaries to create the general_dict
    general_dict = {**general_dict_1, **algo_dict, **general_dict_2}

    stage_definitions = (
        ('N1', 'N1 stage'),
        ('N2', 'N2 stage'),
        ('N3', 'N3 stage'),
        ('N2N3', 'N2 and N3 stage'),
        ('NREM', 'NREM stage (N1, N2, N3)'),
        ('R', 'REM stage'),
    )

    total_dict = \
    {
            'sleep_period_min' : 'Total period for detection - Duration (min) of the sleep period.',
            'total_valid_min' : 'Valid (no artifact) period for detection - Valid duration (min) of the sleep stage selected minus thoses included in REM periods if remps are excluded.',
            'total_spindle_count' : 'Total - Sleep spindle count in all stages.',
            'total_density' : 'Total - Spindle density (count/min)',
            'total_spindle_sec' : 'Total - Average spindle duration (s)',
            'total_dom_freq_Hz' : 'Total - Spindle dominant frequency (Hz) where spectral energy is maximum.',
            'total_avg_freq_Hz' : 'Total - Spindle average frequency (Hz) counting peaks.',
            'total_amp_pkpk_uV' : 'Total - Average peak-to-peak amplitude (uV)',
            'total_amp_rms_uV' : 'Total - Average rms (Root Mean Square) amplitude (uV)',
            'total_peak_sec' : 'Total - Average duration (s) from onset to the maximum peak-to-peak amplitude.',
            'total_RSAI_uVsec' : 'Total - RMS Spindle Activity Index (sum of RMS amplitude x spindle duration) in all stages (uV sec)'
    }

    total_stage_dict = {}
    for stage_name, stage_definition in stage_definitions:
        rem_exclusion = '.' if stage_name == 'R' else ' minus the REM periods if excluded.'
        total_stage_dict |= {
            f'total_{stage_name}_valid_min': f'Valid (no artifact) period for detection - Valid duration (min) of the sleep period in {stage_definition}{rem_exclusion}',
            f'total_{stage_name}_spindle_count': f'Total - Sleep spindle count in {stage_definition}.',
            f'total_{stage_name}_density': f'Total - Spindle density (count/min) in {stage_definition}.',
            f'total_{stage_name}_spindle_sec': f'Total - Average spindle duration (s) in {stage_definition}.',
            f'total_{stage_name}_dom_freq_Hz': f'Total - Spindle dominant frequency (Hz) where spectral energy is maximum in {stage_definition}.',
            f'total_{stage_name}_avg_freq_Hz': f'Total - Spindle average frequency (Hz) counting peaks in {stage_definition}.',
            f'total_{stage_name}_amp_pkpk_uV': f'Total - Average peak-to-peak amplitude (uV) in {stage_definition}.',
            f'total_{stage_name}_amp_rms_uV': f'Total - Average rms amplitude (uV) in {stage_definition}.',
            f'total_{stage_name}_peak_sec': f'Total - Average duration (s) from onset to the maximum peak-to-peak amplitude in {stage_definition}.',
            f'total_{stage_name}_RSAI_uVsec': f'Total - RMS Spindle Activity Index (sum of RMS amplitude x spindle duration) in {stage_definition} (uV sec).',
        }


    total_dict |= total_stage_dict
    cycle_dict = {}
    for i_cycle in range(N_CYCLE):
        current_cycle_dict = {
            f'cyc{i_cycle+1}_valid_min': f'Cycle {i_cycle+1} - Valid (no artifact) duration (min) available for detection minus the REM periods if excluded.',
            f'cyc{i_cycle+1}_min': f'Cycle {i_cycle+1} duration (min) minus the REM periods if excluded.',
        }
        for stage_name, stage_definition in stage_definitions:
            rem_exclusion = '.' if stage_name == 'R' else ' available for detection minus the REM periods if excluded.'
            current_cycle_dict |= {
                f'cyc{i_cycle+1}_{stage_name}_valid_min': f'Cycle {i_cycle+1} - Valid (no artifact) duration (min) in {stage_definition}{rem_exclusion}',
                f'cyc{i_cycle+1}_{stage_name}_spindle_count': f'Cycle {i_cycle+1} - Sleep spindle count in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_density': f'Cycle {i_cycle+1} - Spindle density (count/min) in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_spindle_sec': f'Cycle {i_cycle+1} - Average spindle duration (s) in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_dom_freq_Hz': f'Cycle {i_cycle+1} - Spindle dominant frequency (Hz) where spectral energy is maximum in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_avg_freq_Hz': f'Cycle {i_cycle+1} - Spindle average frequency (Hz) counting peaks in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_amp_pkpk_uV': f'Cycle {i_cycle+1} - Average peak-to-peak amplitude (uV) in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_amp_rms_uV': f'Cycle {i_cycle+1} - Average rms amplitude (uV) in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_peak_sec': f'Cycle {i_cycle+1} - Average duration (s) from onset to the maximum peak-to-peak amplitude in {stage_definition}.',
                f'cyc{i_cycle+1}_{stage_name}_RSAI_uVsec': f'Cycle {i_cycle+1} - RMS Spindle Activity Index (sum of RMS amplitude x spindle duration) in {stage_definition} (uV sec).',
            }
        current_cycle_dict |= {
            f'cyc{i_cycle+1}_spindle_count': f'Cycle {i_cycle+1} - Sleep spindle count in all stages.',
            f'cyc{i_cycle+1}_density': f'Cycle {i_cycle+1} - Spindle density (count/min) in all stages.',
            f'cyc{i_cycle+1}_spindle_sec': f'Cycle {i_cycle+1} - Average spindle duration (s) in all stages.',
            f'cyc{i_cycle+1}_dom_freq_Hz': f'Cycle {i_cycle+1} - Spindle dominant frequency (Hz) where spectral energy is maximum in all stages.',
            f'cyc{i_cycle+1}_avg_freq_Hz': f'Cycle {i_cycle+1} - Spindle average frequency (Hz) counting peaks in all stages.',
            f'cyc{i_cycle+1}_amp_pkpk_uV': f'Cycle {i_cycle+1} - Average peak-to-peak amplitude (uV) in all stages',
            f'cyc{i_cycle+1}_amp_rms_uV': f'Cycle {i_cycle+1} - Average rms (Root Mean Square) amplitude (uV) in all stages',
            f'cyc{i_cycle+1}_peak_sec': f'Cycle {i_cycle+1} - Average duration (s) from onset to the maximum peak-to-peak amplitude in all stages',
            f'cyc{i_cycle+1}_RSAI_uVsec': f'Cycle {i_cycle+1} - RMS Spindle Activity Index (sum of RMS amplitude x spindle duration) in all stages (uV sec)',
        }
        cycle_dict = cycle_dict | current_cycle_dict
    
    clock_hour_dict = {}
    for i_hour in range(N_HOURS):
        current_hour_dict = {
            f'clock_h{i_hour+1}_valid_min': f'Hour {i_hour+1} - Valid (no artifact) duration (min) available for detection minus the REM periods if excluded.',
            f'clock_h{i_hour+1}_min': f'Hour {i_hour+1} duration (min) minus the REM periods if excluded.',
        }
        for stage_name, stage_definition in stage_definitions:
            rem_exclusion = '.' if stage_name == 'R' else ' available for detection minus the REM periods if excluded.'
            current_hour_dict |= {
                f'clock_h{i_hour+1}_{stage_name}_valid_min': f'Hour {i_hour+1} - Valid (no artifact) duration (min) in {stage_definition}{rem_exclusion}',
                f'clock_h{i_hour+1}_{stage_name}_spindle_count': f'Hour {i_hour+1} - Sleep spindle count in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_density': f'Hour {i_hour+1} - Spindle density (count/min) in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_spindle_sec': f'Hour {i_hour+1} - Average spindle duration (s) in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_dom_freq_Hz': f'Hour {i_hour+1} - Spindle dominant frequency (Hz) where spectral energy is maximum in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_avg_freq_Hz': f'Hour {i_hour+1} - Spindle average frequency (Hz) counting peaks in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_amp_pkpk_uV': f'Hour {i_hour+1} - Average peak-to-peak amplitude (uV) in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_amp_rms_uV': f'Hour {i_hour+1} - Average rms amplitude (uV) in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_peak_sec': f'Hour {i_hour+1} - Average duration (s) from onset to the maximum peak-to-peak amplitude in {stage_definition}.',
                f'clock_h{i_hour+1}_{stage_name}_RSAI_uVsec': f'Hour {i_hour+1} - RMS Spindle Activity Index (sum of RMS amplitude x spindle duration) in {stage_definition} (uV sec).',
            }
        current_hour_dict |= {
            f'clock_h{i_hour+1}_spindle_count': f'Hour {i_hour+1} - Sleep spindle count in all stages.',
            f'clock_h{i_hour+1}_density': f'Hour {i_hour+1} - Spindle density (count/min) in all stages.',
            f'clock_h{i_hour+1}_spindle_sec': f'Hour {i_hour+1} - Average spindle duration (s) in all stages.',
            f'clock_h{i_hour+1}_dom_freq_Hz': f'Hour {i_hour+1} - Spindle dominant frequency (Hz) where spectral energy is maximum in all stages.',
            f'clock_h{i_hour+1}_avg_freq_Hz': f'Hour {i_hour+1} - Spindle average frequency (Hz) counting peaks in all stages.',
            f'clock_h{i_hour+1}_amp_pkpk_uV': f'Hour {i_hour+1} - Average peak-to-peak amplitude (uV) in all stages',
            f'clock_h{i_hour+1}_amp_rms_uV': f'Hour {i_hour+1} - Average rms (Root Mean Square) amplitude (uV) in all stages',
            f'clock_h{i_hour+1}_peak_sec': f'Hour {i_hour+1} - Average duration (s) from onset to the maximum peak-to-peak amplitude in all stages',
            f'clock_h{i_hour+1}_RSAI_uVsec': f'Hour {i_hour+1} - RMS Spindle Activity Index (sum of RMS amplitude x spindle duration) in all stages (uV sec)',
        }
        clock_hour_dict = clock_hour_dict | current_hour_dict
    # Add stage hour documentation
    stage_hour_dict = {}
    for i_hour in range(N_HOURS):
        current_stage_hour_dict = {
            f'stage_h{i_hour+1}_min': f'Stage Hour {i_hour+1} duration (min) minus the REM periods if excluded.',
        }
        for stage_name, stage_definition in stage_definitions:
            rem_exclusion = '.' if stage_name == 'R' else ' available for detection minus the REM periods if excluded.'
            current_stage_hour_dict |= {
                f'stage_h{i_hour+1}_{stage_name}_valid_min': f'Stage Hour {i_hour+1} - Valid (no artifact) duration (min) in {stage_definition}{rem_exclusion}',
                f'stage_h{i_hour+1}_{stage_name}_spindle_count': f'Stage Hour {i_hour+1} - Sleep spindle count in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_density': f'Stage Hour {i_hour+1} - Spindle density (count/min) in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_spindle_sec': f'Stage Hour {i_hour+1} - Average spindle duration (s) in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_dom_freq_Hz': f'Stage Hour {i_hour+1} - Spindle dominant frequency (Hz) where spectral energy is maximum in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_avg_freq_Hz': f'Stage Hour {i_hour+1} - Spindle average frequency (Hz) counting peaks in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_amp_pkpk_uV': f'Stage Hour {i_hour+1} - Average peak-to-peak amplitude (uV) in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_amp_rms_uV': f'Stage Hour {i_hour+1} - Average rms amplitude (uV) in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_peak_sec': f'Stage Hour {i_hour+1} - Average duration (s) from onset to the maximum peak-to-peak amplitude in {stage_definition}.',
                f'stage_h{i_hour+1}_{stage_name}_RSAI_uVsec': f'Stage Hour {i_hour+1} - RMS Spindle Activity Index (sum of RMS amplitude x spindle duration) in {stage_definition} (uV sec).',
            }
        current_stage_hour_dict |= {
            f'stage_h{i_hour+1}_spindle_count': f'Stage Hour {i_hour+1} - Sleep spindle count in all stages.',
            f'stage_h{i_hour+1}_density': f'Stage Hour {i_hour+1} - Spindle density (count/min) in all stages.',
            f'stage_h{i_hour+1}_spindle_sec': f'Stage Hour {i_hour+1} - Average spindle duration (s) in all stages.',
            f'stage_h{i_hour+1}_dom_freq_Hz': f'Stage Hour {i_hour+1} - Spindle dominant frequency (Hz) where spectral energy is maximum in all stages.',
            f'stage_h{i_hour+1}_avg_freq_Hz': f'Stage Hour {i_hour+1} - Spindle average frequency (Hz) counting peaks in all stages.',
            f'stage_h{i_hour+1}_amp_pkpk_uV': f'Stage Hour {i_hour+1} - Average peak-to-peak amplitude (uV) in all stages',
            f'stage_h{i_hour+1}_amp_rms_uV': f'Stage Hour {i_hour+1} - Average rms (Root Mean Square) amplitude (uV) in all stages',
            f'stage_h{i_hour+1}_peak_sec': f'Stage Hour {i_hour+1} - Average duration (s) from onset to the maximum peak-to-peak amplitude in all stages',
            f'stage_h{i_hour+1}_RSAI_uVsec': f'Stage Hour {i_hour+1} - RMS Spindle Activity Index (sum of RMS amplitude x spindle duration) in all stages (uV sec)',
        }
        stage_hour_dict = stage_hour_dict | current_stage_hour_dict
    
    complete_dict = general_dict | total_dict | cycle_dict | clock_hour_dict | stage_hour_dict
    return complete_dict

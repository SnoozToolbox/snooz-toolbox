"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
import csv

def write_doc_file(filepath, N_CYCLE, spindle_event_name):
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        docwriter = csv.writer(csvfile, delimiter='\t')

        doc = _get_doc(N_CYCLE, spindle_event_name)

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


def _get_doc(N_CYCLE, spindle_event_name):
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
    general_dict_2 = \
    {
            'artefact_group_name_list' : 'List of groups and names of the artifact excluded from the spindle detection',

            'chan_label' : 'The label of the channel.',
            'chan_fs' : 'The sampling rate (Hz) of the channel.',

            'sleep_cycle_count' : 'Number of sleep cycles.'
    }
    # Concatenate dictionaries to create the general_dict
    general_dict = {**general_dict_1, **algo_dict, **general_dict_2}

    total_dict = \
    {            # The valid duration can change across channels because of the artifact detection
            'sleep_period_min' : 'Total period for detection - Duration (min) of the sleep period.',
            'total_N1_valid_min' : 'Valid (no artifact) period for detection - Valid duration (min) of the sleep period in N1 stage minus the REM periods if excluded.',
            'total_N2_valid_min' : 'Valid (no artifact) period for detection - Valid duration (min) of the sleep period in N2 stage minus the REM periods if excluded.',
            'total_N3_valid_min' : 'Valid (no artifact) period for detection - Valid duration (min) of the sleep period in N3 stage minus the REM periods if excluded.',
            'total_R_valid_min' : 'Valid (no artifact) period for detection - Valid duration (min) of the sleep period in REM stage.',
            'total_valid_min' : 'Valid (no artifact) period for detection - Valid duration (min) of the sleep stage selected minus thoses included in REM periods if remps are excluded.',

            'total_N1_spindle_count' : 'Total - Sleep spindle count in N1 stage.',
            'total_N2_spindle_count' : 'Total - Sleep spindle count in N2 stage.',
            'total_N3_spindle_count' : 'Total - Sleep spindle count in N3 stage.',
            'total_R_spindle_count' : 'Total - Sleep spindle count in REM stage.',
            'total_spindle_count' : 'Total - Sleep spindle count in all stages.',

            'total_N1_density' : 'Total - Spindle density (count/min) in N1 stage.',
            'total_N2_density' : 'Total - Spindle density (count/min) in N2 stage.',
            'total_N3_density' : 'Total - Spindle density (count/min) in N3 stage.',
            'total_R_density' : 'Total - Spindle density (count/min) in REM stage.',
            'total_density' : 'Total - Spindle density (count/min)',
            
            'total_N1_spindle_sec' : 'Total - Average spindle duration (s) in N1 stage.',
            'total_N2_spindle_sec' : 'Total - Average spindle duration (s) in N2 stage.',
            'total_N3_spindle_sec' : 'Total - Average spindle duration (s) in N3 stage.',
            'total_R_spindle_sec' : 'Total - Average spindle duration (s) in REM stage.',
            'total_spindle_sec' : 'Total - Average spindle duration (s)',

            'total_N1_dom_freq_Hz' : 'Total - Spindle dominant frequency (Hz) where spectral energy is maximum in N1 stage.',
            'total_N2_dom_freq_Hz' : 'Total - Spindle dominant frequency (Hz) where spectral energy is maximum in N2 stage.',
            'total_N3_dom_freq_Hz' : 'Total - Spindle dominant frequency (Hz) where spectral energy is maximum in N3 stage.',
            'total_R_dom_freq_Hz' : 'Total - Spindle dominant frequency (Hz) where spectral energy is maximum in REM stage.',
            'total_dom_freq_Hz' : 'Total - Spindle dominant frequency (Hz) where spectral energy is maximum.',

            'total_N1_avg_freq_Hz' : 'Total - Spindle average frequency (Hz) counting peaks in N1 stage.',
            'total_N2_avg_freq_Hz' : 'Total - Spindle average frequency (Hz) counting peaks in N2 stage.',
            'total_N3_avg_freq_Hz' : 'Total - Spindle average frequency (Hz) counting peaks in N3 stage.',
            'total_R_avg_freq_Hz' : 'Total - Spindle average frequency (Hz) counting peaks in REM stage.',
            'total_avg_freq_Hz' : 'Total - Spindle average frequency (Hz) counting peaks.',

            'total_N1_amp_pkpk_uV' : 'Total - Average peak-to-peak amplitude (µV) in N1 stage.',
            'total_N2_amp_pkpk_uV' : 'Total - Average peak-to-peak amplitude (µV) in N2 stage.',
            'total_N3_amp_pkpk_uV' : 'Total - Average peak-to-peak amplitude (µV) in N3 stage.',
            'total_R_amp_pkpk_uV' : 'Total - Average peak-to-peak amplitude (µV) in REM stage.',
            'total_amp_pkpk_uV' : 'Total - Average peak-to-peak amplitude (µV)',

            'total_N1_amp_rms_uV' : 'Total - Average rms amplitude (µV) in N1 stage.',
            'total_N2_amp_rms_uV' : 'Total - Average rms amplitude (µV) in N2 stage.',
            'total_N3_amp_rms_uV' : 'Total - Average rms amplitude (µV) in N3 stage.',
            'total_R_amp_rms_uV' : 'Total - Average rms amplitude (µV) in REM stage.',
            'total_amp_rms_uV' : 'Total - Average rms (Root Mean Square) amplitude (µV)'}
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

            f'cyc{i_cycle+1}_N1_spindle_count' : f'Cycle {i_cycle+1} - Sleep spindle count in N1 stage.',
            f'cyc{i_cycle+1}_N2_spindle_count' : f'Cycle {i_cycle+1} - Sleep spindle count in N2 stage.',
            f'cyc{i_cycle+1}_N3_spindle_count' : f'Cycle {i_cycle+1} - Sleep spindle count in N3 stage.',
            f'cyc{i_cycle+1}_R_spindle_count' : f'Cycle {i_cycle+1} - Sleep spindle count in REM stage.',
            f'cyc{i_cycle+1}_spindle_count' : f'Cycle {i_cycle+1} - Sleep spindle count in all stages.',

            f'cyc{i_cycle+1}_N1_density' : f'Cycle {i_cycle+1} - Spindle density (count/min) in N1 stage.',
            f'cyc{i_cycle+1}_N2_density' : f'Cycle {i_cycle+1} - Spindle density (count/min) in N2 stage.',
            f'cyc{i_cycle+1}_N3_density' : f'Cycle {i_cycle+1} - Spindle density (count/min) in N3 stage.',
            f'cyc{i_cycle+1}_R_density' : f'Cycle {i_cycle+1} - Spindle density (count/min) in REM stage.',
            f'cyc{i_cycle+1}_density' : f'Cycle {i_cycle+1} - Spindle density (count/min) in all stages.',
            
            f'cyc{i_cycle+1}_N1_spindle_sec' : f'Cycle {i_cycle+1} - Average spindle duration (s) in N1 stage.',
            f'cyc{i_cycle+1}_N2_spindle_sec' : f'Cycle {i_cycle+1} - Average spindle duration (s) in N2 stage.',
            f'cyc{i_cycle+1}_N3_spindle_sec' : f'Cycle {i_cycle+1} - Average spindle duration (s) in N3 stage.',
            f'cyc{i_cycle+1}_R_spindle_sec' : f'Cycle {i_cycle+1} - Average spindle duration (s) in REM stage.',
            f'cyc{i_cycle+1}_spindle_sec' : f'Cycle {i_cycle+1} - Average spindle duration (s) in all stages.',

            f'cyc{i_cycle+1}_N1_dom_freq_Hz' : f'Cycle {i_cycle+1} - Spindle dominant frequency (Hz) where spectral energy is maximum in N1 stage.',
            f'cyc{i_cycle+1}_N2_dom_freq_Hz' : f'Cycle {i_cycle+1} - Spindle dominant frequency (Hz) where spectral energy is maximum in N2 stage.',
            f'cyc{i_cycle+1}_N3_dom_freq_Hz' : f'Cycle {i_cycle+1} - Spindle dominant frequency (Hz) where spectral energy is maximum in N3 stage.',
            f'cyc{i_cycle+1}_R_dom_freq_Hz' : f'Cycle {i_cycle+1} - Spindle dominant frequency (Hz) where spectral energy is maximum in REM stage.',
            f'cyc{i_cycle+1}_dom_freq_Hz' : f'Cycle {i_cycle+1} - Spindle dominant frequency (Hz) where spectral energy is maximum in all stages.',

            f'cyc{i_cycle+1}_N1_avg_freq_Hz' : f'Cycle {i_cycle+1} - Spindle average frequency (Hz) counting peaks in N1 stage.',
            f'cyc{i_cycle+1}_N2_avg_freq_Hz' : f'Cycle {i_cycle+1} - Spindle average frequency (Hz) counting peaks in N2 stage.',
            f'cyc{i_cycle+1}_N3_avg_freq_Hz' : f'Cycle {i_cycle+1} - Spindle average frequency (Hz) counting peaks in N3 stage.',
            f'cyc{i_cycle+1}_R_avg_freq_Hz' : f'Cycle {i_cycle+1} - Spindle average frequency (Hz) counting peaks in REM stage.',
            f'cyc{i_cycle+1}_avg_freq_Hz' : f'Cycle {i_cycle+1} - Spindle average frequency (Hz) counting peaks in all stages.',            

            f'cyc{i_cycle+1}_N1_amp_pkpk_uV' : f'Cycle {i_cycle+1} - Average peak-to-peak amplitude (µV) in N1 stage.',
            f'cyc{i_cycle+1}_N2_amp_pkpk_uV' : f'Cycle {i_cycle+1} - Average peak-to-peak amplitude (µV) in N2 stage.',
            f'cyc{i_cycle+1}_N3_amp_pkpk_uV' : f'Cycle {i_cycle+1} - Average peak-to-peak amplitude (µV) in N3 stage.',
            f'cyc{i_cycle+1}_R_amp_pkpk_uV' : f'Cycle {i_cycle+1} - Average peak-to-peak amplitude (µV) in REM stage.',
            f'cyc{i_cycle+1}_amp_pkpk_uV' : f'Cycle {i_cycle+1} - Average peak-to-peak amplitude (µV) in all stages',

            f'cyc{i_cycle+1}_N1_amp_rms_uV' : f'Cycle {i_cycle+1} - Average rms amplitude (µV) in N1 stage.',
            f'cyc{i_cycle+1}_N2_amp_rms_uV' : f'Cycle {i_cycle+1} - Average rms amplitude (µV) in N2 stage.',
            f'cyc{i_cycle+1}_N3_amp_rms_uV' : f'Cycle {i_cycle+1} - Average rms amplitude (µV) in N3 stage.',
            f'cyc{i_cycle+1}_R_amp_rms_uV' : f'Cycle {i_cycle+1} - Average rms amplitude (µV) in REM stage.',
            f'cyc{i_cycle+1}_amp_rms_uV' : f'Cycle {i_cycle+1} - Average rms (Root Mean Square) amplitude (µV) in all stages'}
        cycle_dict = cycle_dict | current_cycle_dict
    complete_dict = general_dict | total_dict | cycle_dict
    return complete_dict

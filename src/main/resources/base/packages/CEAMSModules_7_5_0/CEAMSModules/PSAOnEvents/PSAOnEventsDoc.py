"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
import csv

def write_doc_file(filepath, N_HOURS=0, N_CYCLES=0, event_names=None, include_total=True):
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        docwriter = csv.writer(csvfile, delimiter='\t')

        doc = _get_doc(N_HOURS, N_CYCLES, event_names, include_total)

        for i, (k, v) in enumerate(doc.items()):
            docwriter.writerow([k,v])

def _get_doc(N_HOURS=0, N_CYCLES=0, event_names=None, include_total=True):
    if event_names is None:
        event_names = ['annot1', 'annot2', 'annotx']
    else:
        event_names = list(event_names)

    general_dict = {
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
            'artifact_group_name_list' : 'List of groups and names of the artefact excluded from the Power Spectral Analysis',
            'channel_label' : 'The label of the channel.',
            'channel_fs' : 'The sampling rate (Hz) of the channel.',
            'channel_artefact_count' : 'The number of artefacts marked on the channel (i.e. number of events).',
            'fft_win_sec': 'The actual FFT window length in seconds after rounding to whole samples. Annotation durations are compared using the same sample rounding at each channel sampling rate.',
            'fft_step_sec': 'The step in sec between each start point of the window used for the FFT.',
            'freq_low_Hz' : 'The low frequency (Hz) of the mini band.',
            'freq_high_Hz' : 'The high frequency (Hz) of the mini band.',
    }

    total_dict = {}
    if include_total:
        total_dict['total_fft_win_count'] = 'The number of fft windows in selected annotations.'
        total_dict['total_fft_win_valid_count'] = 'The number of valid fft windows in selected annotations.'
        for event_name in event_names:
            total_dict[f'total_{event_name}_fft_win_count'] = \
                f'The number of fft windows in selected annotation {event_name}.'
            total_dict[f'total_{event_name}_fft_win_valid_count'] = \
                f'The number of valid fft windows in selected annotation {event_name}.'
        total_dict['total_act'] = 'The total spectral power (uV^2)'
        for event_name in event_names:
            total_dict[f'total_{event_name}_act'] = \
                f'The spectral power (uV^2) in selected annotation {event_name}.'

    clock_hour_dict = {}
    for i_hour in range(N_HOURS):
        label = f'clock_h{i_hour+1}'
        clock_hour_dict[f'{label}_fft_win_count'] = \
            f'Clock Hour {i_hour+1} - The number of fft windows in selected annotations.'
        clock_hour_dict[f'{label}_fft_win_valid_count'] = \
            f'Clock Hour {i_hour+1} - The number of valid fft windows in selected annotations.'
        for event_name in event_names:
            clock_hour_dict[f'{label}_{event_name}_fft_win_count'] = \
                f'Clock Hour {i_hour+1} - The number of fft windows in selected annotation {event_name}.'
            clock_hour_dict[f'{label}_{event_name}_fft_win_valid_count'] = \
                f'Clock Hour {i_hour+1} - The number of valid fft windows in selected annotation {event_name}.'
        clock_hour_dict[f'{label}_act'] = \
            f'Clock Hour {i_hour+1} - The spectral power (uV^2).'
        for event_name in event_names:
            clock_hour_dict[f'{label}_{event_name}_act'] = \
                f'Clock Hour {i_hour+1} - The spectral power (uV^2) in selected annotation {event_name}.'

    cyc_dict = {}
    for i_cycle in range(N_CYCLES):
        label = f'cyc{i_cycle+1}'
        cyc_dict[f'{label}_length_min'] = \
            f'Cycle {i_cycle+1} - Duration of the cycle in minutes.'
        cyc_dict[f'{label}_fft_win_count'] = \
            f'Cycle {i_cycle+1} - The number of fft windows in selected annotations.'
        cyc_dict[f'{label}_fft_win_valid_count'] = \
            f'Cycle {i_cycle+1} - The number of valid fft windows in selected annotations.'
        for event_name in event_names:
            cyc_dict[f'{label}_{event_name}_fft_win_count'] = \
                f'Cycle {i_cycle+1} - The number of fft windows in selected annotation {event_name}.'
            cyc_dict[f'{label}_{event_name}_fft_win_valid_count'] = \
                f'Cycle {i_cycle+1} - The number of valid fft windows in selected annotation {event_name}.'
        cyc_dict[f'{label}_act'] = \
            f'Cycle {i_cycle+1} - The spectral power (uV^2).'
        for event_name in event_names:
            cyc_dict[f'{label}_{event_name}_act'] = \
                f'Cycle {i_cycle+1} - The spectral power (uV^2) in selected annotation {event_name}.'

    return general_dict | total_dict | clock_hour_dict | cyc_dict

"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
import csv

def write_doc_file(filepath):
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        docwriter = csv.writer(csvfile, delimiter='\t')

        doc = _get_doc()

        for i, (k, v) in enumerate(doc.items()):
            docwriter.writerow([k,v])

def _get_doc():
    return {
            'filename' : 'PSG filename',
            'id1'      : 'subject identification',
            'artefact_group_name_list' : 'List of groups and names of the artefact excluded from the Power Spectral Analysis',
            'channel_label' : 'The label of the channel.',
            'channel_fs' : 'The sampling rate (Hz) of the channel.',
            'channel_artefact_count' : 'The number of artefacts marked on the channel (i.e. number of events).',
            'fft_win_sec': 'The window length in sec used to perform the FFT.',
            'fft_step_sec': 'The step in sec between each start point of the window used for the FFT.',
            'fft_win_count' : 'The number of fft windows in selected annotations.',
            'fft_win_valid_count' : 'The number of valid fft windows in selected annotations.',           
            'fft_win_annot1_count' : 'The number of fft windows in selected annotation 1.',
            'fft_win_valid_annot1_count' : 'The number of valid fft windows in selected annotation 1.',
            'fft_win_annot2_count' : 'The number of fft windows in in selected annotation 2.',
            'fft_win_valid_annot2_count' : 'The number of valid fft windows in selected annotation 2.',
            'fft_win_annotx_count' : 'The number of fft windows in selected annotation x.',
            'fft_win_valid_annotx_count' : 'The number of valid fft windows in selected annotation x.',
            'freq_low_Hz' : 'The low frequency (Hz) of the mini band.',
            'freq_high_Hz' : 'The high frequency (Hz) of the mini band.',
            'act_total' : 'The total spectral power (uV^2)',
            'act_annot1' : 'The spectral power (uV^2) in selected annotation 1.',
            'act_annot2' : 'The spectral power (uV^2) in selected annotation 2.',
            'act_annotx' : 'The spectral power (uV^2) selected annotation x.'
    }
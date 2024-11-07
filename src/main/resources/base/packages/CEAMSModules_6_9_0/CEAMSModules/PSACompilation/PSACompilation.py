"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    PSACompilation
    Class to analyse and report the PSD output. 
    Average the PSD per channel, stage, cycle, hour...
    Append all subjects in the same output file.
"""
import numpy as np
import os
import pandas as pd

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

from CEAMSModules.PSGReader import commons
from CEAMSModules.SleepReport import SleepReport
from CEAMSModules.PSACompilation.PSACompilationDoc import write_doc_file, _get_doc
from CEAMSModules.PSACompilation import commons as PSA

DEBUG = False

class PSACompilation(SciNode):
    """
    Class to analyse and report the PSD output. 
    Average the PSD per channel, stage, cycle, hour...
    Append all subjects in the same output file.

    Inputs:
        "subject_info": dict
            filename : Recording filename without path and extension.
            id1 : Identification 1
            id2 : Identification 2
            first_name : first name of the subject recorded
            last_name : last name of the subject recorded
            sex :
            ...
        "PSD":  list of dicts
            psd : power (µV^2)
            freq_bins : frequency bins (Hz)
            win_len : windows length (s)
            win_step : windows step (s)
            sample_rate : sampling rate of the original signal (Hz)
            chan_label : channel label
        "events": Pandas Dataframe ['group','name','start_sec','duration_sec','channels']
            List of events.
        "sleep_stages": Pandas Dataframe ['group','name','start_sec','duration_sec','channels']
            List of sleep stages that match the PSD input. Sleep stages selected to analyse the spectral power.
        "mini_bandwidth" : float
            The bandwidth of eah mini band division (Hz)
        "first_freq" : float
            The minimum (first) frequency analyzed.
        "last_freq" : float
            The maximum (last) frequency analysed.
            ! Warning : the last frequency is limited to fs/2
        "dist_total" : bool
            True to write the total spectral activity.
        "dist_hour" : bool
            True to write the spectral activity per hour.
        "dist_cycle" : bool
            True to write the spectral activity per cycle.        
        "parameters_cycle" : String (dict converted into a string)
            "{
                'defined_option':'Minimum Criteria'
                'Include_SOREMP' : '1'
                'Include_last_incompl' : '1'
                'Include_all_incompl: : '1'
                'dur_ends_REMP' = '15'
                'NREM_min_len_first':'0'
                'NREM_min_len_mid_last':'15'
                'NREM_min_len_val_last':'0'
                'REM_min_len_first':'0'
                'REM_min_len_mid':'0'
                'REM_min_len_last':'0'
                'mv_end_REMP':'0'
                'sleep_stages':'N1, N2, N3, N4, R'
                'details': '<p>Adjust options based on minimum criteria.</p>
            }"
        "artefact_group": String
            Event group to ignore, each group is separated by a comma. 
        "artefact_name": String
            Event name to ignore, each name is separated by a comma.
        "cycle_labelled" :  pandas DataFrame
            List of NREM and REM periods (columns=['group','name','start_sec','duration_sec','channels'])
            where the group is the recording filename.
        "report_constants": dict
            Constants used in the report (N_HOURS, N_CYCLES)        
        "filename" : string
            Path and filename to write the output.

    Outputs:
        Outputs are written in the file defined by the input filename

    """

    def __init__(self, **kwargs):
        """ Initialize module PSACompilation """
        super().__init__(**kwargs)
        if DEBUG: print('PSACompilation.__init__')

        # Input plugs
        InputPlug('subject_info',self)
        InputPlug('PSD',self)
        InputPlug('events',self)
        InputPlug('sleep_stages',self)
        InputPlug('mini_bandwidth',self)
        InputPlug('first_freq',self)
        InputPlug('last_freq',self)
        InputPlug('dist_total',self)
        InputPlug('dist_hour',self)
        InputPlug('dist_cycle',self)
        InputPlug('parameters_cycle',self)
        InputPlug('artefact_group',self)
        InputPlug('artefact_name',self)
        InputPlug('cycle_labelled',self)        
        InputPlug('report_constants',self)
        InputPlug('filename',self)
        
        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 

        # Define the sleep stage to analyse
        self.sleep_stage_to_stats = [ ['0'], ['1'], ['2'], ['3'], ['1', '2', '3'], ['5'], ['9'] ]
        self.stage_stats_labels = [ 'W', 'N1', 'N2', 'N3', 'NREM', 'R', 'Unscored'] 

        # Dict to accumulate the act per stage, hour and cycle.
        self.PSD_act_param = {}
        self.PSD_avg_per_stage = {}
    

    def compute(self, subject_info, PSD, sleep_stages, events, mini_bandwidth, first_freq, last_freq, dist_total, \
        dist_hour, dist_cycle, parameters_cycle, artefact_group, artefact_name, cycle_labelled, report_constants, filename):
        """
        Inputs:
            "subject_info": dict
                filename : Recording filename without path and extension.
                id1 : Identification 1
                id2 : Identification 2
                first_name : first name of the subject recorded
                last_name : last name of the subject recorded
                sex :
                ...
            "PSD":  list of dicts
                psd : power (µV^2)
                freq_bins : frequency bins (Hz)
                win_len : windows length (s)
                win_step : windows step (s)
                sample_rate : sampling rate of the original signal (Hz)
                chan_label : channel label
            "events": Pandas Dataframe ['group','name','start_sec','duration_sec','channels']
                List of events.
            "sleep_stages": Pandas Dataframe ['group','name','start_sec','duration_sec','channels']
                List of sleep stages and sleep cycles. 
            "mini_bandwidth" : float
                The bandwidth of eah mini band division (Hz)
            "first_freq" : float
                The minimum (first) frequency analyzed.
            "last_freq" : float
                The maximum (last) frequency analysed.
                ! Warning : the last frequency is limited to fs/2
            "dist_total" : bool
                True to write the total spectral activity.
            "dist_hour" : bool
                True to write the spectral activity per hour.
            "dist_cycle" : bool
                True to write the spectral activity per cycle.        
            "parameters_cycle" : String (dict converted into a string)
                "{
                    'defined_option':'Minimum Criteria'
                    'Include_SOREMP' : '1'
                    'Include_last_incompl' : '1'
                    'Include_all_incompl: : '1'
                    'dur_ends_REMP' = '15'
                    'NREM_min_len_first':'0'
                    'NREM_min_len_mid_last':'15'
                    'NREM_min_len_val_last':'0'
                    'REM_min_len_first':'0'
                    'REM_min_len_mid':'0'
                    'REM_min_len_last':'0'
                    'mv_end_REMP':'0'
                    'sleep_stages':'N1, N2, N3, N4, R'
                    'details': '<p>Adjust options based on minimum criteria.</p>
                }"
            "artefact_group": String
                Event group to reset signal, each group is separated by a comma, as a pattern occurrence.
            "artefact_name": String
                Event name to reset signal, each name is separated by a comma, as a pattern occurrence.
            "cycle_labelled" :  pandas DataFrame
                List of NREM and REM periods (columns=['group','name','start_sec','duration_sec','channels'])
                where the group is the recording filename.
            "report_constants": dict
                Constants used in the report (N_HOURS, N_CYCLES)   
            "filename" : string
                Path and filename to write the output.

        Outputs:
            Outputs are written in the file defined by the input filename
            

        """
        # Input Type verification
        if not isinstance(PSD,list):
            raise NodeInputException(self.identifier, "PSA", \
                f"PSACompilation input of wrong type. Expected: <class 'list'> received: {type(PSD)}")   

        if not isinstance(sleep_stages,pd.DataFrame):
            raise NodeInputException(self.identifier, "sleep_stages", \
                f"PSACompilation input of wrong type. Expected: <class 'pd.DataFrame'> received: {type(sleep_stages)}")

        if type(parameters_cycle) != dict:
            raise NodeInputException(self.identifier, "parameters_cycle", \
                f"PSACompilation input of wrong type. Expected: <class 'dict'> received: {type(parameters_cycle)}")

        if (not isinstance(cycle_labelled, pd.DataFrame)) or len(cycle_labelled)==0:
            raise NodeInputException(self.identifier, "cycle_labelled", \
                f"PSACompilation input of wrong type or empty. Expected: <class 'pd.DataFrame'> received: {type(cycle_labelled)}")            
        try:
            mini_bandwidth = float(mini_bandwidth)
        except ValueError:
            raise NodeInputException(self.identifier, "mini_bandwidth", \
                f"PSACompilation input of wrong type or empty. Expected: str of float") 
        try:
            first_freq = float(first_freq)
        except ValueError:
            raise NodeInputException(self.identifier, "first_freq", \
                f"PSACompilation input of wrong type or empty. Expected: str of float") 
        try:
            last_freq = float(last_freq)
        except ValueError:
            raise NodeInputException(self.identifier, "last_freq", \
                f"PSACompilation input of wrong type or empty. Expected: str of float") 

        if isinstance(report_constants,str) and report_constants == '':
            raise NodeInputException(self.identifier, "report_constants", \
                "PSACompilation report_constants parameter must be set.")
        elif isinstance(report_constants,str):
            report_constants = eval(report_constants)
        if isinstance(report_constants,dict) == False:
            raise NodeInputException(self.identifier, "report_constants",\
                "PSACompilation report_constants expected type is dict and received type is " + str(type(report_constants)))   
        self.N_HOURS = int(float(report_constants['N_HOURS']))
        self.N_CYCLES = int(float(report_constants['N_CYCLES']))

        if (not isinstance(filename,str)) or (isinstance(filename,str) and len(filename)==0):
            raise NodeInputException(self.identifier, "filename", \
                f"PSACompilation input of wrong type. Expected: <class str> received: {type(filename)}") 

        # Extract PSG information, Filename of the PSG recording and Sleep cycle parameters  
        
        # Extract subject info
        subject_info_params = {"filename": subject_info['filename']}
        if (subject_info['id1'] is not None) and len(subject_info['id1'].strip())>0:
            subject_info_params['id1'] = subject_info['id1']
        elif (subject_info['id2'] is not None) and len(subject_info['id2'].strip())>0:
            subject_info_params['id1'] = subject_info['id2']
        else:
            subject_info_params['id1'] = subject_info['id1']

        cycle_info_param = SleepReport.get_sleep_cycle_parameters(self,parameters_cycle)    

        # Select the artefact from events
        artefact_info_param, art_selected = \
            self.get_artefact_info(artefact_group, artefact_name, events.copy())

        # Extract the unique channel list
        channels_list = np.unique(PSA.get_attribute(PSD, 'chan_label'))
        # The channels are grouped in the PSA cohort file
        report_df = []
        for channel in channels_list:

            # Extract the sampling rate of the current channel
            channel_info_param, fs_chan = PSA.get_channel_info(PSD, channel)

            # Compute the number of artefacts for the current channel and selected sleep stage
            channel_info_param['channel_artefact_count'] = \
                self.get_n_artefact_sel(art_selected, channel, sleep_stages)        

            # Extract the fft length and step
            PSD_info_params = PSA.get_PSD_info(self.identifier, PSD, channel)

            # Extract the PSD property for the current channel
            #   freq_bin_chan is an [1 x n_freq_bins] (because it is unique across the recording)
            #   psd_start_time is an [1 x n_fft_wins] (a start time for each fft window)
            #   psd_stage is [1 x n_fft_wins] (the sleep stage for each fft window)
            #   psd_data is an [n_fft_wins x n_freq_bins] (the PSD data for each fft window)
            freq_bin_chan, psd_start_time, psd_stage, psd_data = \
                PSA.get_PSD_attribute_chan_stage(self.identifier, PSD, channel, sleep_stages)

            # To avoid too many decimal in the frequency bins
            freq_bin_space = np.average(np.diff(freq_bin_chan))
            # This works only for frequency bins < 1
            if freq_bin_space<1:
                precision_space = int(abs(np.log10(freq_bin_space)))+2
                freq_bin_chan = np.round(freq_bin_chan,precision_space)

            miniband_indices = PSA.get_miniband_index(self.identifier, freq_bin_chan, mini_bandwidth, first_freq, last_freq, fs_chan)
            # The frequency band definded as [min, max[ (i.e. 0-3.8 Hz) are written in the report as 0-4 Hz
            PSD_freq_params = {}
            PSD_freq_params['freq_low_Hz'] = [freq_bin_chan[miniband_index[0]] for miniband_index in miniband_indices]
            PSD_freq_params['freq_high_Hz'] = [freq_bin_chan[miniband_index[1]+1] for miniband_index in miniband_indices] 

            # --------------------------------------------------------------------------
            # Compute the total and the valid number of fft windows and 
            # average the activity across windows through the recording 
            # for each sleep stage defined by sleep_stage_to_stats. 
            # --------------------------------------------------------------------------
            # Compute :
                # self.PSD_act_param : dict
                    #     n_fft_win : total number of fft windows
                    #     n_fft_win_valid : number of valid fft windows
                    #     for each sleep stage
                    #         i.e. total_n_fft_win_W, total_n_fft_win_valid_W, total_n_fft_win_N1 ...
                # self.PSD_avg_per_stage : dict
                #   psd data average through the recording for each stage
                #     total_act : narray [1 x n_freq_bins]
                #     for each sleep stage
                #         i.e. total_act_W, total_act_N1 ...
            if int(dist_total)==1:
                my_label = 'total'
                PSD_avg_total, PSD_avg_per_stage = self.compute_fft_win_div(psd_data, psd_stage, my_label)

                self.PSD_act_param[f"total_act"] = \
                    [np.nansum(PSD_avg_total[miniband_index[0]:miniband_index[1]+1]) for miniband_index in miniband_indices]

                for i, stage_label in enumerate(self.stage_stats_labels):
                    if (self.PSD_act_param[f'total_{stage_label}_fft_win_count']>0):
                        # The fft normalisation is made to integrate (sum) through frequency bins
                        self.PSD_act_param[f"total_{stage_label}_act"] = \
                            [np.nansum(PSD_avg_per_stage[i][miniband_index[0]:miniband_index[1]+1]) for miniband_index in miniband_indices]
                    else:
                        self.PSD_act_param[f"total_{stage_label}_act"] = np.array([np.NaN]*len(miniband_indices)) 

            # PSD data per hour
            if int(dist_hour)==1: 
                my_label = 'hour'
                for cur_div in range(self.N_HOURS):
                    # Verify if the cycle is valid (at least the start of the first cycle)
                    if isinstance(cycle_labelled.iloc[0]['start_sec'],float):
                        # Extract the psd_stage and psd_start_time for the current hour
                        start_hour = cycle_labelled.iloc[0]['start_sec']+cur_div*3600
                        end_hour = start_hour+3600
                        #psd_start_div = psd_start_time[(psd_start_time<end_hour) & (psd_start_time>=start_hour)]
                        psd_stage_div = [psd_stage[i] for i in np.where( (psd_start_time<end_hour) & (psd_start_time>=start_hour))[0]]   
                        psd_data_div = [data for (start_time, data) in zip(psd_start_time, psd_data) if ((start_time<end_hour) & (start_time>=start_hour))]
                    else:
                        psd_data_div = []
                        psd_stage_div = []
                    
                    # self.PSD_avg_per_stage : dict
                    #   psd data average through the recording for each stage and hour
                    #     hour1_act : narray [1 x n_freq_bins]
                    #     for each sleep stage
                    #         i.e. hour1_act_W, hour1_act_N1 ...
                    PSD_avg_hour, PSD_stage_avg_hour = self.compute_fft_win_div(psd_data_div, psd_stage_div, f'{my_label}{cur_div+1}')

                    if self.PSD_act_param[f'hour{cur_div+1}_fft_win_count']>0:
                        self.PSD_act_param[f"hour{cur_div+1}_act"] = \
                            [np.nansum(PSD_avg_hour[miniband_index[0]:miniband_index[1]+1]) for miniband_index in miniband_indices]
                    else:
                        self.PSD_act_param[f"hour{cur_div+1}_act"] = np.array([np.NaN]*len(miniband_indices))               
                    for i, stage_label in enumerate(self.stage_stats_labels):
                        if (self.PSD_act_param[f'hour{cur_div+1}_{stage_label}_fft_win_count']>0):
                            # The fft normalisation is made to integrate (sum) through frequency bins
                            self.PSD_act_param[f"hour{cur_div+1}_{stage_label}_act"] = \
                                [np.nansum(PSD_stage_avg_hour[i][miniband_index[0]:miniband_index[1]+1]) for miniband_index in miniband_indices]
                        else:
                            self.PSD_act_param[f"hour{cur_div+1}_{stage_label}_act"] = np.array([np.NaN]*len(miniband_indices))  

            # PSD data per sleep cycle
            if int(dist_cycle)==1:
                my_label = 'cyc'
                for cur_div in range(self.N_CYCLES):
                    # Verify if the cycle is valid (at least the start of the first cycle)
                    if isinstance(cycle_labelled.iloc[0]['start_sec'],float):
                        # Extract the psd_stage and psd_start_time for the current cycle
                        if (cur_div*2)<len(cycle_labelled):
                            start_cycle = cycle_labelled.iloc[cur_div*2]['start_sec']
                        else:
                            start_cycle = cycle_labelled.iloc[-1]['start_sec']+cycle_labelled.iloc[-1]['duration_sec']
                        if (cur_div*2+1)<len(cycle_labelled):
                            end_cycle = cycle_labelled.iloc[cur_div*2+1]['start_sec']+cycle_labelled.iloc[cur_div*2+1]['duration_sec']
                        else:
                            end_cycle = cycle_labelled.iloc[-1]['start_sec']+cycle_labelled.iloc[-1]['duration_sec']
                        #psd_start_div = psd_start_time[(psd_start_time<end_cycle) & (psd_start_time>=start_cycle)]
                        psd_stage_div = [psd_stage[i] for i in np.where( (psd_start_time<end_cycle) & (psd_start_time>=start_cycle))[0]]
                        psd_data_div = [data for (start_time, data) in zip(psd_start_time, psd_data) if ((start_time<end_cycle) & (start_time>=start_cycle))]
                    else:
                        psd_start_div = []
                        psd_stage_div = []                        
                    # Add the cycle duration to the stats
                    self.PSD_act_param[f'{my_label}{cur_div+1}_length_min'] = (end_cycle-start_cycle)/60

                    # self.PSD_avg_per_stage : dict
                    #   psd data average through the recording for each stage and cycle
                    #     cycle1_act : narray [1 x n_freq_bins]
                    #     for each sleep stage
                    #         i.e. cycle1_act_W, cycle1_act_N1 ...
                    PSD_avg_cycle, PSD_stage_avg_cycle = self.compute_fft_win_div(psd_data_div, psd_stage_div, f'{my_label}{cur_div+1}')

                    if self.PSD_act_param[f'cyc{cur_div+1}_fft_win_count']>0:
                        self.PSD_act_param[f"cyc{cur_div+1}_act"] = \
                            [np.nansum(PSD_avg_cycle[miniband_index[0]:miniband_index[1]+1]) for miniband_index in miniband_indices]
                    else:
                        self.PSD_act_param[f"cyc{cur_div+1}_act"] = np.array([np.NaN]*len(miniband_indices))               
                    for i, stage_label in enumerate(self.stage_stats_labels):
                        if (self.PSD_act_param[f'cyc{cur_div+1}_{stage_label}_fft_win_count']>0):
                            # The fft normalisation is made to integrate (sum) through frequency bins
                            self.PSD_act_param[f"cyc{cur_div+1}_{stage_label}_act"] = \
                                [np.nansum(PSD_stage_avg_cycle[i][miniband_index[0]:miniband_index[1]+1]) for miniband_index in miniband_indices]
                        else:
                            self.PSD_act_param[f"cyc{cur_div+1}_{stage_label}_act"] = np.array([np.NaN]*len(miniband_indices))       

            # --------------------------------------------------------------------------
            # Organize data to Write the file
            # --------------------------------------------------------------------------
            # Construction of the pandas dataframe that will be used to create the CSV file
            # There is a new line for each channel and mini band
            header_dict = subject_info_params | cycle_info_param | artefact_info_param | channel_info_param | PSD_info_params 
            header_df = pd.DataFrame.from_records([header_dict])
            mini_band_hdr_df = pd.DataFrame([header_df.values[0]] * len(miniband_indices), columns=header_df.columns)
            mini_band_dict = PSD_freq_params | self.PSD_act_param
            mini_band_df = pd.DataFrame.from_dict(mini_band_dict)
            cur_chan_report_df = pd.concat([mini_band_hdr_df, mini_band_df], axis=1) # Add the columns for the mini band info

            if len(report_df):
                report_df = pd.concat([report_df, cur_chan_report_df], axis=0) # Add the rows for the current channel to the total report
            else:
                report_df = cur_chan_report_df


        # Order columns as the doc file
        if dist_hour and dist_cycle:
            out_columns = list(_get_doc(self.N_HOURS, self.N_CYCLES).keys())
        elif dist_hour:
            out_columns = list(_get_doc(self.N_HOURS, 0).keys())
        elif dist_cycle:
            out_columns = list(_get_doc(0, self.N_CYCLES).keys())
        else:
            out_columns = list(_get_doc(0, 0).keys())
        report_df = report_df[out_columns]

        # Write the current report for the current subject into the tsv file
        write_header = not os.path.exists(filename)
        try: 
            report_df.to_csv(path_or_buf=filename, sep='\t', \
                index=False, mode='a', header=write_header, encoding="utf_8")
        except:
            raise NodeRuntimeException(self.identifier, "PSA", f"ERROR : Snooz can not write in the file {filename}. Check if the drive is accessible and ensure the file is not already open.")               

        # To write the info text file to describe the variable names
        if write_header:
            # Write the documentation file
            file_name, file_extension = os.path.splitext(filename)
            doc_filepath = file_name+"_info"+file_extension
            if not os.path.exists(doc_filepath):
                try:
                    write_doc_file(doc_filepath, self.N_HOURS, self.N_CYCLES)
                    # Log message for the Logs tab
                    self._log_manager.log(self.identifier, f"The file {doc_filepath} has been created.")
                except:
                    raise NodeRuntimeException(self.identifier, "PSA", f"ERROR : Snooz can not write in the file {doc_filepath}. Check if the drive is accessible and ensure the file is not already open.")    
        return {
        }


    # To select the artefact events according to artefact groups and names.
    # Generate the artefact info dict to write. 
    def get_artefact_info(self, artefact_group, artefact_name, events):
        # Select the group and name
        art_selected = pd.DataFrame(columns=['group','name','start_sec','duration_sec','channels'])
        if isinstance(artefact_group,str) and len(artefact_group)>0:
            art_group_lst = artefact_group.split(',')
        else:
            art_group_lst = []
        if isinstance(artefact_name,str) and len(artefact_name)>0:
            art_name_lst = artefact_name.split(',')
        else:
            art_name_lst = []
        if len(art_group_lst)==len(art_name_lst):
            for i, group_cur in enumerate(art_group_lst):
                cur_selection = events.loc[ (events.group.str.contains(group_cur, regex=False)) \
                    & (events.name.str.contains(art_name_lst[i], regex=False)), :]
                art_selected = pd.concat([art_selected,cur_selection])
        elif len(art_group_lst)>0 and len(art_name_lst)==0:
            for group_cur in art_group_lst:
                group_selected = events.loc[events.group.str.contains(group_cur, regex=False), :]
                art_selected = pd.concat([art_selected,group_selected])
        elif len(art_name_lst)>0 and len(art_group_lst)==0:
            for name_cur in art_name_lst:
                name_selected = events.loc[events.name.str.contains(name_cur, regex=False), :]
                art_selected = pd.concat([art_selected,name_selected])
        else:
            raise NodeInputException(self.identifier, "artefact_group", \
                f"PSACompilation input of wrong size. If both group and name are defined they need to be the same length, group length:\
                     {len(art_group_lst)} and name length: {len(art_name_lst)}") 
        artefact_info_param = {}
        artefact_info_param['artefact_group_name_list']=''
        for i_art, group in enumerate(art_group_lst):
            temp = '('+str(i_art)+')'+"group:"+group+" name:"+art_name_lst[i_art]+' '
            artefact_info_param['artefact_group_name_list']=artefact_info_param['artefact_group_name_list']+temp

        return artefact_info_param, art_selected


    # Get the sleep stage of each psd start of the selected epoch
    def get_sleep_stage(self, psd_start_time, psd_end_time, sleep_stages):
        stage_start_all = sleep_stages['start_sec'].to_numpy()
        # Convert the stage_start_all array into float (to allow the rouding when they are integer)
        stage_start_all = stage_start_all.astype(float)
        # Round the stage_start_all array to 2 decimals (important to locate events with non integer sampling rate)
        stage_start_all = np.around(stage_start_all, 2)
        stage_end_all = stage_start_all+sleep_stages['duration_sec'].to_numpy()
        stage_end_all = stage_end_all.astype(float)
        stage_end_all = np.around(stage_end_all, 2)
        stage_name_all = sleep_stages['name'].to_numpy()
        psd_start_time = psd_start_time.astype(float)
        psd_start_time = np.around(psd_start_time, 2)
        psd_end_time = psd_end_time.astype(float)
        psd_end_time = np.around(psd_end_time, 2)
        psd_stage = []
        for start_time, end_time in zip(psd_start_time, psd_end_time):
            stage_sel_arr = (stage_start_all<end_time) & (stage_end_all>start_time)
            if any(stage_sel_arr):
                cur_stage = stage_name_all[stage_sel_arr]
                psd_stage.append(cur_stage[0])
            else:
                psd_stage.append(np.nan)
        return psd_stage


    def compute_fft_win_div(self, psd_data, psd_stage, label_stat_div):
        """
            Compute the total and the valid number of fft windows for each sleep stage
            defined by sleep_stage_to_stats. Return also the PSD data averaged per sleep stages.

            Inputs:
                psd_data: array 
                    data of each fft window
                psd_stage : list
                    stage of each fft window
                label_stat_div : str
                    String to label the stats per division (.i.e. total, )

            compute:
                self.PSD_avg_per_stage : dict
                    total_act : narray [1 x n_freq_bins]
                    for each sleep stage
                        i.e. total_act_W, total_act_N1 ...
            return : 
                PSD_avg_total : array
                    the total average PSD (len of the fequency bins)
                PSD_avg_per_stage : list
                    the average PSD per sleep stage (len of the fequency bins)

        """
        # sleep_stage_to_stats : list
        #     Each item is a list of sleep stages to compute the event stats
        # stage_stats_label : list of string
        #     Each item is a string to label the stats variable

        # Compute the number of valid fft windows for each sleep stage
        

        PSD_avg_per_stage = []
        psd_data_tot = np.empty([0,0])
        for i_list, cur_stage_list in enumerate(self.sleep_stage_to_stats):
            # Extract current data (FAST)
            psd_data_cur_stage = [data for (stage, data) in zip(psd_stage, psd_data) if stage in cur_stage_list]

            # Compute the number of valid fft windows and average datat (FAST)
            if len(psd_data_cur_stage):
                # Accumulate act and n fft for the total
                if len(cur_stage_list)==1: # grouped stages are not accumulated to avoid the count the same stage twice
                    if len(psd_data_tot)>0:
                        psd_data_tot = np.vstack((psd_data_tot,psd_data_cur_stage))
                    else:
                        psd_data_tot = psd_data_cur_stage
                # Compute the total number of valid fft windows (find out if there is a nan for each window)
                n_nan_fft_win = np.sum(np.isnan(np.sum(psd_data_cur_stage, axis=1)))
                div_n_fft_win = len(psd_data_cur_stage)
                div_n_fft_win_valid = div_n_fft_win-n_nan_fft_win
            else:
                # Compute the total number of valid fft windows
                div_n_fft_win = 0
                div_n_fft_win_valid = 0                

            # Compute the total number of valid fft windows
            n_fft_win_label = f"{label_stat_div}_{self.stage_stats_labels[i_list]}_fft_win_count"
            n_fft_valid_label = f"{label_stat_div}_{self.stage_stats_labels[i_list]}_fft_win_valid_count"
            self.PSD_act_param[n_fft_win_label] = div_n_fft_win
            self.PSD_act_param[n_fft_valid_label] = div_n_fft_win_valid
            # Average the activity through the recording
            #self.PSD_avg_per_stage[f"{label_stat_div}_{self.stage_stats_labels[i_list]}_act"] = np.nanmean(psd_data_cur_stage,axis=0)
            PSD_avg_per_stage.append(np.nanmean(psd_data_cur_stage,axis=0))

        # Compute the total number of valid fft windows (find out if there is a nan for each window)
        n_nan_fft_win = np.sum(np.isnan(np.sum(psd_data_tot, axis=1)))
        tot_n_fft_win = len(psd_data_tot)
        tot_n_fft_win_valid = tot_n_fft_win-n_nan_fft_win

        self.PSD_act_param[f'{label_stat_div}_fft_win_count'] = tot_n_fft_win
        self.PSD_act_param[f'{label_stat_div}_fft_win_valid_count'] = tot_n_fft_win_valid
        # Average the activity through the recording
        self.PSD_avg_per_stage[f'{label_stat_div}_act']= np.nanmean(psd_data_tot,axis=0)
        PSD_avg_total = np.nanmean(psd_data_tot,axis=0)

        return PSD_avg_total, PSD_avg_per_stage

    # Compute the number of artefacts for the current channel and selected sleep stage
    def get_n_artefact_sel(self, art_selected, channel, sleep_stages):
        # Extract sleep stage info
        stage_start_all = sleep_stages['start_sec'].to_numpy()
        # Convert the stage_start_all array into float (to allow the rouding when they are integer)
        stage_start_all = stage_start_all.astype(float)
        # Round the stage_start_all array to 2 decimals (important to locate events with non integer sampling rate)
        stage_start_all = np.around(stage_start_all, decimals=2)
        stage_end_all = stage_start_all+sleep_stages['duration_sec'].to_numpy()
        stage_end_all = stage_end_all.astype(float)
        stage_end_all = np.around(stage_end_all, decimals=2)
        # Extract artefact for the current channel
        art_channel_arr = art_selected['channels'].to_numpy()
        art_start_arr = art_selected['start_sec'].to_numpy()
        art_start_arr = np.around(art_start_arr, decimals=2)
        art_dur_arr = art_selected['duration_sec'].to_numpy()
        art_dur_arr = np.around(art_dur_arr, decimals=2)
        # Compute the number of artefacts for the selected sleep stages
        n_arts = 0
        for start, dur, chan in zip(art_start_arr, art_dur_arr, art_channel_arr):
            if channel == chan:
                if any( (stage_start_all<(start+dur)) & (stage_end_all>start) ):
                    n_arts += 1
                # This value is more similar to "Compilation de l'activite spectrale"
                # if any( (stage_start_all<=start) & (stage_end_all>=(start+dur)) ):
                #    n_arts += 1
        return n_arts
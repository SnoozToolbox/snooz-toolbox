"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    SlowWavesDetails
    To average slow wave events characteristics such as duration, amplitude, frequency and so on per stage and sleep cycle.
"""
import numpy as np
import os
import pandas as pd

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

from CEAMSModules.PSGReader import commons
from CEAMSModules.PSGReader.SignalModel import SignalModel
from CEAMSModules.SleepReport import SleepReport
from CEAMSModules.SlowWavesDetails.SlowWavesDetailsDoc import write_doc_file
from CEAMSModules.SlowWavesDetails.SlowWavesDetailsDoc import _get_doc
from CEAMSModules.SpindlesDetails.SpindlesDetails import SpindlesDetails as EventsDetails

DEBUG = False

class SlowWavesDetails(SciNode):
    """
    To average slow wave events characteristics such as duration, amplitude, frequency and so on per stage and sleep cycle.

    Inputs:
        "recording_path" : string
            The recording path.
        "subject_info": dict
            filename : Recording filename without path and extension.
            id1 : Identification 1
            id2 : Identification 2
            first_name : first name of the subject recorded
            last_name : last name of the subject recorded
            sex :
            ...
        "signals": a list of SignalModel
            Each item of the list is a SignalModel object as described below:
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the sampling rate of the signal
                signal.channel : current channel label
                signal.start_time : The start time of the signal in sec
                signal.end_time : The end time of the signal in sec
                (for more info : look into common/SignalModel)
        "sw_events_details": Pandas DataFrame
            Slow wave events defined as (columns=['group', 'name', 'start_sec','pkpk_amp_uV','neg_amp_uV','neg_sec','pos_sec','Pap_raw','Neg_raw','mfr','trans_freq_Hz', 'channels'])
        "artifact_events": Pandas DataFrame
            Artifact events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
            Artifacts are forced to zeros for the detection (with a tukey window)
        "sleep_cycle_param": Dict
            Options used to define the cycles
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
        "stages_cycles": Pandas DataFrame
            Events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
            The sleep stage group has to be commons.sleep_stage_group "stage" and 
            the sleep cycle group has to be commons.sleep_cycle_group "cycle".
        "slow_wave_det_param": Dict
            stage_sel : Sleep stages selection to detect slow waves in.
            detect_excl_remp : Flag to exclude rem period from the spindle detection.
            sw_event_name : String label of the event name
            filt_low_hz : Low frequency bandpass filter (Hz)
            filt_high_hz : High frequency bandpass filter (Hz)
            min_amp_pk-pk_uV  : minimum peak-to-peak amplitude (uV)
            min_neg_amp_uV : minimum negative amplitude (uV)
            min_dur_neg_ms : minimum duration of negative part of the slow wave (ms)
            max_dur_neg_ms : maximum duration of negative part of the slow wave (ms)
            min_dur_pos_ms : minimum duration of positive part of the slow wave (ms)
            max_dur_pos_ms : maximum duration of positive part of the slow wave (ms)
        "report_constants": dict
            Constants used in the report (N_HOURS, N_CYCLES)   
        "cohort_filename": string
            Path and filename to save the slow wave characteristics for the cohort. 
        "export_slow_wave": bool or string
            True : generate a file per subject of the characteristics of each slow wave.
    
    Outputs:
        None
        
    """
    def __init__(self, **kwargs):
        """ Initialize module SlowWavesDetails """
        super().__init__(**kwargs)
        if DEBUG: print('SlowWavesDetails.__init__')

        # Input plugs
        InputPlug('recording_path',self)
        InputPlug('subject_info',self)
        InputPlug('signals',self)
        InputPlug('sw_events_details',self)
        InputPlug('artifact_events',self)
        InputPlug('sleep_cycle_param',self)
        InputPlug('stages_cycles',self)
        InputPlug('slow_wave_det_param',self)
        InputPlug('report_constants',self)
        InputPlug('cohort_filename',self)
        InputPlug('export_slow_wave',self)
        
        # Init module variables
        self.stage_stats_labels = ['N1', 'N2', 'N3', 'R']
        #self.N_CYCLES = 8

        # A master module allows the process to be reexcuted multiple time.
        self._is_master = False 

        self.sw_columns = ['group','name','cycle','stage','start_sec','duration_sec','pkpk_amp_uV', 'freq_Hz',\
            'neg_amp_uV', 'neg_sec', 'pos_sec','slope_0_min','slope_min_max','slope_max_0','trans_freq_Hz','channels']
        self.sw_characteristics = ['duration_sec','pkpk_amp_uV', 'freq_Hz','neg_amp_uV', 'neg_sec', 'pos_sec',\
            'slope_0_min','slope_min_max','slope_max_0','trans_freq_Hz']
    

    def compute(self, recording_path, subject_info, signals, sw_events_details, artifact_events, \
        sleep_cycle_param, stages_cycles, slow_wave_det_param, report_constants, cohort_filename, export_slow_wave):
        """
        To average slow wave events characteristics such as duration, amplitude, frequency and so on per stage and sleep cycle.

        Inputs:
            "recording_path" : string
                The recording path.
            "subject_info": dict
                filename : Recording filename without path and extension.
                id1 : Identification 1
                id2 : Identification 2
                first_name : first name of the subject recorded
                last_name : last name of the subject recorded
                sex :
                ...
            "signals": a list of SignalModel
                Each item of the list is a SignalModel object as described below:
                    signal.samples : The actual signal data as numpy list
                    signal.sample_rate : the sampling rate of the signal
                    signal.channel : current channel label
                    signal.start_time : The start time of the signal in sec
                    signal.end_time : The end time of the signal in sec
                    (for more info : look into common/SignalModel)
            "sw_events_details": Pandas DataFrame
                Slow wave events defined as (columns=['group', 'name', 'start_sec','pkpk_amp_uV','neg_amp_uV','neg_sec','pos_sec','Pap_raw','Neg_raw','mfr','trans_freq_Hz', 'channels'])
            "artifact_events": Pandas DataFrame
                Artifact events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
                Artifacts are forced to zeros for the detection (with a tukey window)
            "sleep_cycle_param": Dict
                Options used to define the cycles
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
            "stages_cycles": Pandas DataFrame
                Spindle events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
                The sleep stage group has to be commons.sleep_stage_group (stage) and 
                the sleep cycle group has to be commons.sleep_cycle_group (cycle)
            "slow_wave_det_param": Dict
                stage_sel : Sleep stages selection to detect slow waves in.
                detect_excl_remp : Flag to exclude rem period from the spindle detection.
                sw_event_name : String label of the event name
                filt_low_hz : Low frequency bandpass filter (Hz)
                filt_high_hz : High frequency bandpass filter (Hz)
                min_amp_pk-pk_uV  : minimum peak-to-peak amplitude (uV)
                min_neg_amp_uV : minimum negative amplitude (uV)
                min_dur_neg_ms : minimum duration of negative part of the slow wave (ms)
                max_dur_neg_ms : maximum duration of negative part of the slow wave (ms)
                min_dur_pos_ms : minimum duration of positive part of the slow wave (ms)
                max_dur_pos_ms : maximum duration of positive part of the slow wave (ms)
            "report_constants": dict
                Constants used in the report (N_HOURS, N_CYCLES)   
            "cohort_filename": string
                Path and filename to save the slow wave characteristics for the cohort. 
            "export_slow_wave": bool or string
                True : generate a file per subject of the characteristics of each slow wave.
        """
        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if isinstance(export_slow_wave, str):
            export_slow_wave = eval(export_slow_wave)
        if not isinstance(export_slow_wave, bool):
            raise NodeInputException(self.identifier, "recording_path", \
                f"SlowWavesDetails the type of the input is {type(export_slow_wave)} and bool is expected.")            
        if recording_path=='':
            raise NodeInputException(self.identifier, "recording_path", \
                f"SlowWavesDetails this input is empty, it needs to identify the recording to analyze.")
        if subject_info=='':
            raise NodeInputException(self.identifier, "subject_info", \
                f"SlowWavesDetails this input is empty, it needs to identify the subject recorded.")
        if cohort_filename=='' and not export_slow_wave:
            raise NodeInputException(self.identifier, "cohort_filename", \
                f"SlowWavesDetails has nothing to generate, 'cohort_filename' is empty and 'export_slow_wave' is False")    
        if isinstance(signals, str) and signals=='':
            raise NodeInputException(self.identifier, "signals", \
                f"SlowWavesDetails this input is empty, no signals no details.")              
        if isinstance(sw_events_details, str) and sw_events_details=='':
            raise NodeInputException(self.identifier, "sw_events_details", \
                f"SlowWavesDetails this input is empty, no sw_events_details no details.")     
        if isinstance(stages_cycles, str) and stages_cycles=='':
            raise NodeInputException(self.identifier, "stages_cycles", \
                f"SlowWavesDetails this input is empty")    
        if isinstance(sleep_cycle_param, str) and sleep_cycle_param=='':
            raise NodeInputException(self.identifier, "sleep_cycle_param", \
                f"SlowWavesDetails this input is empty")  
        if isinstance(slow_wave_det_param, str) and slow_wave_det_param=='':
            raise NodeInputException(self.identifier, "slow_wave_det_param", \
                f"SlowWavesDetails this input is empty")  

        if len(signals)==0:
            raise NodeRuntimeException(self.identifier, "signals", \
                f"SlowWavesDetails this input is empty, no signals no details.")       

        if isinstance(report_constants,str) and report_constants == '':
            raise NodeInputException(self.identifier, "report_constants", \
                "SlowWavesDetails report_constants parameter must be set.")
        elif isinstance(report_constants,str):
            report_constants = eval(report_constants)
        if isinstance(report_constants,dict) == False:
            raise NodeInputException(self.identifier, "report_constants",\
                "SlowWavesDetails report_constants expected type is dict and received type is " + str(type(report_constants)))   
        self.N_CYCLES = int(float(report_constants['N_CYCLES']))

        # To convert string to dict
        if isinstance(sleep_cycle_param, str):
            sleep_cycle_param = eval(sleep_cycle_param)
        if isinstance(slow_wave_det_param, str):
            slow_wave_det_param = eval(slow_wave_det_param)

        # Extract subject info
        subject_info_params = {"filename": subject_info['filename']}
        if (subject_info['id1'] is not None) and len(subject_info['id1'].strip())>0:
            subject_info_params['id1'] = subject_info['id1']
        elif (subject_info['id2'] is not None) and len(subject_info['id2'].strip())>0:
            subject_info_params['id1'] = subject_info['id2']
        else:
            subject_info_params['id1'] = subject_info['id1']
        #-----------------------------------------------------------------------------------
        # Define the sw parameters
        #-----------------------------------------------------------------------------------
        sw_det_param = slow_wave_det_param

        #-----------------------------------------------------------------------------------
        # Sleep stages and cyles extraction
        #-----------------------------------------------------------------------------------        
        # Extract sleep cycle parameters
        cycle_info_param = SleepReport.get_sleep_cycle_parameters(self, sleep_cycle_param)    
        sleep_cycles_df = stages_cycles[stages_cycles['group']==commons.sleep_cycle_group].copy()
        sleep_cycles_df.reset_index(inplace=True, drop=True)
        sleep_cycle_count = {}
        sleep_cycle_count['cyc_count']=len(sleep_cycles_df) # 'Number of sleep cycles.',

        # Extract sleep stage info
        sleep_stage_df = stages_cycles[stages_cycles['group']==commons.sleep_stages_group].copy()
        sleep_stage_df.reset_index(inplace=True, drop=True)      
        # Keep stage from the first awake or sleep until the last awake or sleep
        sleep_stage_df['name'] = sleep_stage_df['name'].apply(int)
        index_valid = sleep_stage_df[sleep_stage_df['name']<8].index
        stage_rec_df = sleep_stage_df.loc[index_valid[0]:index_valid[-1]]
        stage_rec_df.reset_index(inplace=True, drop=True)
        recording_lights_off = stage_rec_df['start_sec'].values[0]
        recording_lights_on = stage_rec_df['start_sec'].values[-1]+stage_rec_df['duration_sec'].values[-1]

        # Edit the cycle number 
        cycle_cnt = 1
        for index, row in sleep_cycles_df.iterrows():
            sleep_cycles_df.loc[index,'name']=cycle_cnt
            cycle_cnt = cycle_cnt+1

        # Exclude sleep stage before Sleep Onset
        # Exclude sleep stage after the end of the last cycle
        stage_in_cycle_df = EventsDetails.exlude_stages_before_SO_after_awake(EventsDetails, sleep_cycles_df, sleep_stage_df)

        # Cycle events
        cycle_starts = sleep_cycles_df['start_sec'].values
        cycle_durations = sleep_cycles_df['duration_sec'].values

        # Compute duration (min)
        sleep_onset_sec = cycle_starts[0]
        end_sleep_sec = cycle_starts[-1]+cycle_durations[-1] #TODO make sure we dont have to recompute end_sleep_sec without REMP
        
        # Remove REMP if excluded? no! It matches with Gaetan if we let it like this
        # 'Total period for detection - Duration (min) of the sleep period.'
        sleep_cycle_count['sleep_period_min'] = (end_sleep_sec - sleep_onset_sec)/60
        sleep_cycle_count['recording_min'] = (recording_lights_on - recording_lights_off)/60

        # Exclude REMPs if exluded
        if slow_wave_det_param['detect_excl_remp']==1:
            stage_in_cycle_df, sleep_cycles_df = EventsDetails.exclude_remps(EventsDetails, stages_cycles, sleep_cycles_df, stage_in_cycle_df)

        if export_slow_wave: 
            # Extract sleep stages selected by the user from stage_in_cycle_df
            # Create a list from string separated by comma
            sleep_stage_sel_list = slow_wave_det_param['stage_sel'].split(',')
            # Convert the list to integer
            sleep_stage_sel_list = [int(i) for i in sleep_stage_sel_list]
            stage_detection_df = stage_in_cycle_df[stage_in_cycle_df['name'].isin(sleep_stage_sel_list)]  
            # In a folder at the cohort level
            if len(cohort_filename)>0:
                # Extract folder of the file
                folder_cohort = os.path.dirname(cohort_filename)
                # Make directory specific for spindles characteristics
                folder_sw_stage = os.path.join(folder_cohort, 'slow_wave_sleep_stages')
                if not os.path.isdir(folder_sw_stage):
                    os.makedirs(folder_sw_stage)
                sw_stage_filename = os.path.join(folder_sw_stage,subject_info['filename'])
                sw_stage_filename = sw_stage_filename+'_'+slow_wave_det_param["sw_event_name"]+'_'+'stages'+'.tsv'
                # Write the stage_detection_df dataframe into the sw_stage_filename file
                stage_detection_df.to_csv(sw_stage_filename, sep='\t', index=False, header=True)

        # For each spindle events add its sleep stage and cycle
        # Need to have "start_sec" and "duration_sec" to use add_stage_cycle_to_spindle_df
        sw_events_details = EventsDetails.add_stage_cycle_to_spindle_df(EventsDetails, sw_events_details, stage_in_cycle_df, sleep_cycles_df)

        #-----------------------------------------------------------------------------------
        # Extract artifact group and name to save the info parameters
        #-----------------------------------------------------------------------------------
        artifact_info_param = {}
        group_name_artifact = artifact_events[['group','name']]
        group_name_artifact = group_name_artifact.drop_duplicates()
        group_name_artifact.reset_index(inplace=True, drop=True)
        artifact_info_param['artefact_group_name'] = ''
        for index, row in group_name_artifact.iterrows():
            temp = '('+str(index)+')'+"group:"+row['group']+" name:"+row['name']+' '
            artifact_info_param['artefact_group_name']=artifact_info_param['artefact_group_name']+temp

        #-----------------------------------------------------------------------------------
        # Compute and organize characteristics
        #----------------------------------------------------------------------------------_
        
        channels_list = np.unique(SignalModel.get_attribute(signals, 'channel', 'channel'))
        # Define the dataframe to save
        cohort_characteristics_df = []
        sw_characteristics_df = pd.DataFrame()
        for channel in channels_list:

            # Define the channel info
            fs_chan = SignalModel.get_attribute(signals, 'sample_rate', 'channel', channel)[0][0] 
            channel_info_param = {}
            channel_info_param['chan_label']=channel
            channel_info_param['chan_fs']=fs_chan
            # Organize data for the output (GENERAL)
            cur_chan_general_dict = subject_info_params | cycle_info_param | sw_det_param | artifact_info_param | channel_info_param | sleep_cycle_count     

            # Select artifact for the current channel
            #   Artifact events have been cleanup to have a single channel as a string
            artifact_cur_chan_df = artifact_events[artifact_events['channels']==channel]    

            # Select sw events for the current channel
            sw_cur_chan_df = sw_events_details[sw_events_details['channels']==channel].copy() # dataFrame
            sw_cur_chan_df.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')  
            sw_cur_chan_df.reset_index(inplace=True, drop=True)

            # Manage slow wave event, reset the index
            sw_cur_chan_df = sw_cur_chan_df.reset_index(drop=True)
            # Add the frequency is 1/total duration.
            sw_cur_chan_df['freq_Hz'] = 1/sw_cur_chan_df['duration_sec'].values
            # Order columns as expected in the doc
            sw_cur_chan_sort = sw_cur_chan_df[self.sw_columns]

            # ---------------------------------------------------------------------------------------------------------
            # Compute the stats for total
            # ---------------------------------------------------------------------------------------------------------
            label_stats = 'total'
            tot_stats = self.compute_tot_stats_per_stage(sw_cur_chan_sort, artifact_cur_chan_df, stage_in_cycle_df, \
                commons.sleep_stages_name, sw_det_param['stage_sel'], label_stats, self.stage_stats_labels)

            # ---------------------------------------------------------------------------------------------------------
            # Compute the stats for cycle
            # ---------------------------------------------------------------------------------------------------------
            label_stats = 'cyc'
            cyc_stats = self.compute_cyc_stats_per_stage(sw_cur_chan_sort, artifact_cur_chan_df, stage_in_cycle_df, sleep_cycles_df,\
                commons.sleep_stages_name, sw_det_param['stage_sel'], label_stats, self.stage_stats_labels)

            # Organize data to write the cohort spindle report
            # Construction of the pandas dataframe that will be used to create the TSV file
            # There is a new line for each channel and mini band
            cur_chan_dict = cur_chan_general_dict | tot_stats | cyc_stats
            cur_chan_df = pd.DataFrame.from_records([cur_chan_dict])

            # --------------------------------------------------------------------------
            # Organize data to Write the file
            # --------------------------------------------------------------------------
            if len(cohort_characteristics_df):
                cohort_characteristics_df = pd.concat([cohort_characteristics_df, cur_chan_df])
            else:
                cohort_characteristics_df = cur_chan_df
            # Organize data to write the slow wave characteristics
            if export_slow_wave:
                if len(sw_characteristics_df)==0:
                    sw_characteristics_df = sw_cur_chan_sort
                else:
                    sw_characteristics_df = pd.concat([sw_characteristics_df, sw_cur_chan_sort],ignore_index=True)

        #----------------------------------------------------------------------------
        # Slow wave characteristics TSV file
        #----------------------------------------------------------------------------
        if export_slow_wave:
            if len(sw_characteristics_df)>0:
                # We need to link the sw characteristics file with the PSG recording
                subject_id = subject_info['filename'] 
                # In a folder at the cohort level
                if len(cohort_filename)>0:
                    # Extract folder of the file
                    folder_cohort = os.path.dirname(cohort_filename)
                    # Make directory specific for spindles characteristics
                    folder_sw_char = os.path.join(folder_cohort, 'slow_wave_characteristics')
                    if not os.path.isdir(folder_sw_char):
                        os.makedirs(folder_sw_char)
                    sw_char_filename = os.path.join(folder_sw_char,subject_id)
                    sw_char_filename = sw_char_filename+'_'+slow_wave_det_param["sw_event_name"]+'.tsv'
                # In the subject folder
                else:
                    # Extract folder of the file
                    folder_subject = os.path.dirname(recording_path)
                    sw_char_filename = os.path.join(folder_subject,subject_id)
                    sw_char_filename = sw_char_filename+'_'+slow_wave_det_param["sw_event_name"]+'.tsv'
                # Sort from start_time (events are ordered per channel) and remove index for the output text file
                sw_characteristics_df = sw_characteristics_df.sort_values(by=['start_sec'])
                sw_characteristics_df = sw_characteristics_df.reset_index(drop=True) # do not add an index column
                try : 
                    sw_characteristics_df.to_csv(path_or_buf=sw_char_filename, sep='\t', index=False, index_label='False', mode='w', header=True, encoding="utf_8")
                    # Log message for the Logs tab
                    self._log_manager.log(self.identifier, f"Slow wave characteristics from {subject_info['filename']} has been generated.")
                except :
                    error_message = f"Snooz can not write in the file {sw_char_filename}."+\
                        f" Check if the drive is accessible and ensure the file is not already open."
                    raise NodeRuntimeException(self.identifier, "SlowWavesDetails", error_message)
            else:
                # Log message for the Logs tab
                self._log_manager.log(self.identifier, f"No slow wave for {subject_info['filename']}.")

        #----------------------------------------------------------------------------
        # Cohort TSV file
        #----------------------------------------------------------------------------
        if len(cohort_filename)>0:
            # Write the current report for the current subject into the cohort tsv file
            write_header = not os.path.exists(cohort_filename)
            # Order columns as the doc file
            out_columns = list(_get_doc(self.N_CYCLES).keys())
            cohort_characteristics_df = cohort_characteristics_df[out_columns]
            try : 
                cohort_characteristics_df.to_csv(path_or_buf=cohort_filename, sep='\t', \
                    index=False, index_label='False', mode='a', header=write_header, encoding="utf_8")
            except :
                error_message = f"Snooz can not write in the file {cohort_filename}."+\
                    f" Check if the drive is accessible and ensure the file is not already open."
                raise NodeRuntimeException(self.identifier, "SlowWavesDetails", error_message)            

            # To write the info text file to describe the variable names
            if write_header:
                # Write the documentation file
                file_name, file_extension = os.path.splitext(cohort_filename)
                doc_filepath = file_name+"_info"+file_extension
                if not os.path.exists(doc_filepath):
                    write_doc_file(doc_filepath, self.N_CYCLES)
                    # Log message for the Logs tab
                    self._log_manager.log(self.identifier, f"The file {doc_filepath} has been created.")

            # Log message for the Logs tab
            self._log_manager.log(self.identifier, f"{subject_info['filename']} is added to {cohort_filename}.")

        return {
        }


    def compute_tot_stats_per_stage(self, sw_cur_chan_sort, artifact_cur_chan_df, stage_in_cycle_df, sleep_stages_name, stage_sel, label_stats, stage_stats_labels):
        # Compute valid duration (min)
        #   Return a dict as valid_dur[f'{label_stats}_valid_min_{stage}']
        valid_dur = EventsDetails.compute_valid_dur_min(EventsDetails, artifact_cur_chan_df, stage_in_cycle_df, sleep_stages_name, stage_sel, label_stats, stage_stats_labels)

        # Extract characteristics to average
        sw_cur_chan_tot = sw_cur_chan_sort[self.sw_characteristics]
        # Format the sw_cur_chan_stage dataframe values into float
        sw_cur_chan_tot = sw_cur_chan_tot.applymap(float)        
        mean_char_series = sw_cur_chan_tot.mean(axis=0, skipna=True, numeric_only=True)
        mean_char_series = mean_char_series.round(decimals=2)
        mean_char_tot = mean_char_series.to_dict()
        # Rename keys
        mean_tot = {}
        sw_count_tot = {f'{label_stats}_sw_count':len(sw_cur_chan_tot)}
        for key, value in mean_char_tot.items():
            if key=='duration_sec':
                mean_tot[f'{label_stats}_sw_sec'] = value
            else:
                mean_tot[f'{label_stats}_{key}'] = value                
        # Average characteristique per stage
        mean_stage = {}
        sw_count_stage = {}
        for stage in stage_stats_labels:
#            if sleep_stages_name[stage] in stage_sel:
            # Extract sw for the current stage
            sw_cur_chan_stage = sw_cur_chan_sort[sw_cur_chan_sort['stage']==int(sleep_stages_name[stage])]
            sw_cur_chan_stage = sw_cur_chan_stage[self.sw_characteristics]
            # Format the sw_cur_chan_stage dataframe values into float
            sw_cur_chan_stage = sw_cur_chan_stage.applymap(float)
            # Compute the number of detection per stage
            n_sw = len(sw_cur_chan_stage)
            sw_count_stage[f'{label_stats}_{stage}_sw_count'] = n_sw
            # Average the characteristiques for the current recording and stage
            mean_char_series = sw_cur_chan_stage.mean(axis=0, skipna=True, numeric_only=True)
            mean_char_series = mean_char_series.round(decimals=2)
            mean_char_stage = mean_char_series.to_dict()
            # Rename keys of the dict with all the stats and all the stages
            if n_sw==0:
                for key in self.sw_characteristics:
                    if key=='duration_sec':
                        mean_stage[f'{label_stats}_{stage}_sw_sec'] = np.NaN 
                    else:
                        mean_stage[f'{label_stats}_{stage}_{key}'] = np.NaN      
            else:
                for key, value in mean_char_stage.items():
                    if key=='duration_sec':
                        mean_stage[f'{label_stats}_{stage}_sw_sec'] = value
                    else:
                        mean_stage[f'{label_stats}_{stage}_{key}'] = value              
        tot_stats =  valid_dur | sw_count_stage | mean_stage | sw_count_tot | mean_tot
        return tot_stats


    def compute_cyc_stats_per_stage(self, sw_cur_chan_sort, artifact_cur_chan_df, stage_in_cycle_df, \
        sleep_cycles_df, sleep_stages_name, stage_sel, label_stats, stage_stats_labels):

        # SW events
        sw_start_times = sw_cur_chan_sort['start_sec'].to_numpy().astype(float)   # numpy array
        sw_duration_times = sw_cur_chan_sort['duration_sec'].to_numpy().astype(float)  # numpy array
        sw_end_times = sw_start_times+sw_duration_times        

        # Stage events
        stage_starts = stage_in_cycle_df['start_sec'].values
        stage_durations = stage_in_cycle_df['duration_sec'].values
        stage_ends = stage_starts+stage_durations  

        # Cycle events
        cycle_starts = sleep_cycles_df['start_sec'].values
        cycle_durations = sleep_cycles_df['duration_sec'].values
        cycle_ends = cycle_starts+cycle_durations

        # Stage columns labels
        stage_col_label = stage_in_cycle_df.columns

        valid_dur= {}
        rec_dur = {}
        sw_count_cyc = {}
        mean_cyc = {}
        mean_stage = {}
        sw_count_stage = {}
        # For each sleep cycle
        for i_cycle in range(self.N_CYCLES):
            cycle_label = label_stats+str(i_cycle+1)
            
            # If the cycle exist
            if len(cycle_durations)>i_cycle:
                # Select the stages from the current cycle
                i_cycle_start = cycle_starts[i_cycle]
                i_cycle_end = cycle_ends[i_cycle]
                stages_bool = (stage_starts>=i_cycle_start) & (stage_ends<=i_cycle_end)
                stages_i_sel = np.nonzero(stages_bool)[0]
                stage_sel_df = stage_in_cycle_df.iloc[stages_i_sel]

                # Select the sw from the current cycle
                sw_bool = (sw_start_times>=i_cycle_start) & (sw_end_times<=i_cycle_end)
                slow_wave_sel_i = np.nonzero(sw_bool)[0]
                sw_sel_df = sw_cur_chan_sort.iloc[slow_wave_sel_i]
            else:
                stage_sel_df = pd.DataFrame(columns=stage_col_label)
                sw_sel_df = pd.DataFrame(columns=self.sw_columns)

            # Extract characteristics to average
            sw_sel_to_mean = sw_sel_df[self.sw_characteristics]
            # Format the sw_cur_chan_stage dataframe values into float
            sw_sel_to_mean = sw_sel_to_mean.applymap(float)

            if len(cycle_durations)>i_cycle:
                # Compute duration (min)
                rec_dur[f'{cycle_label}_min'] = cycle_durations[i_cycle]/60
            else:
                rec_dur[f'{cycle_label}_min'] = 0

            # Compute valid duration (min)
            #   For each sleep stage included in stage_sel_df, compute the duration without artifact (valid_min).
            valid_dur_cur = EventsDetails.compute_valid_dur_min(EventsDetails, artifact_cur_chan_df, stage_sel_df, \
                commons.sleep_stages_name, stage_sel, cycle_label, self.stage_stats_labels)
            # Accumulate for each cycle
            valid_dur = valid_dur | valid_dur_cur
            # Compute the number of detection per cycle
            n_sw = len(sw_sel_to_mean)
            sw_count_cyc[f'{cycle_label}_sw_count'] = n_sw
            # Average characteristique for the current cycle
            mean_char_series = sw_sel_to_mean.mean(axis=0, skipna=True, numeric_only=True)
            mean_char_series = mean_char_series.round(decimals=2)
            mean_char_tot = mean_char_series.to_dict()
            if n_sw==0:
                for key in self.sw_characteristics:
                    if key=='duration_sec':
                        mean_cyc[f'{cycle_label}_sw_sec'] = np.NaN 
                    else:
                        mean_cyc[f'{cycle_label}_{key}'] = np.NaN          
            else:
                for key, value in mean_char_tot.items():
                    if key=='duration_sec':
                        mean_cyc[f'{cycle_label}_sw_sec'] = value
                    else:
                        mean_cyc[f'{cycle_label}_{key}'] = value          

            # Average characteristique per stage
            for stage in stage_stats_labels:
                #if sleep_stages_name[stage] in stage_sel:
                # Extract sw for the current stage
                sw_cur_chan_stage = sw_sel_df[sw_cur_chan_sort['stage']==int(sleep_stages_name[stage])]
                sw_cur_to_mean = sw_cur_chan_stage[self.sw_characteristics]
                # Format the sw_cur_chan_stage dataframe values into float
                sw_cur_to_mean = sw_cur_to_mean.applymap(float)

                # Compute the number of detection per stage
                n_sw = len(sw_cur_chan_stage)
                sw_count_stage[f'{cycle_label}_{stage}_sw_count'] = n_sw

                # Average the characteristiques for the current recording and stage
                mean_char_series = sw_cur_to_mean.mean(axis=0, skipna=True, numeric_only=True)
                mean_char_series = mean_char_series.round(decimals=2)
                mean_char_stage = mean_char_series.to_dict()
                # Rename keys of the dict with all the stats and all the stages
                if n_sw==0:
                    for key in self.sw_characteristics:
                        if key=='duration_sec':
                            mean_stage[f'{cycle_label}_{stage}_sw_sec'] = np.NaN
                        else:
                            mean_stage[f'{cycle_label}_{stage}_{key}'] = np.NaN                        
                else:
                    for key, value in mean_char_stage.items():
                        if key=='duration_sec':
                            mean_stage[f'{cycle_label}_{stage}_sw_sec'] = value
                        else:
                            mean_stage[f'{cycle_label}_{stage}_{key}'] = value

            cyc_stats =  valid_dur | rec_dur | sw_count_stage | mean_stage | sw_count_cyc | mean_cyc
        return cyc_stats
"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    SpindlesDetails
    To compute events characteristics such as duration, amplitude, frequency and so on.
"""

import numpy as np
import os
import pandas as pd
from scipy import signal as sci_signal
from scipy import fft as sp_fft

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

from CEAMSModules.PSGReader.SignalModel import SignalModel
from CEAMSModules.PSGReader import commons
from CEAMSModules.SleepReport import SleepReport
from CEAMSModules.SpindlesDetails.SpindlesDetailsDoc import write_doc_file
from CEAMSModules.SpindlesDetails.SpindlesDetailsDoc import _get_doc
from CEAMSModules.SignalsFromEvents.SignalsFromEvents import SignalsFromEvents

DEBUG = False

class SpindlesDetails(SciNode):
    """
    To compute events characteristics such as duration, amplitude, frequency and so on.

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
        "spindle_events": Pandas DataFrame
            Spindle events defined as (columns=['group', 'name','start_sec','duration_sec','channels'])   
            The group has to be commons.sleep_spindle_group (spindle)
        "stages_cycles": Pandas DataFrame
            Spindle events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
            The sleep stage group has to be commons.sleep_stage_group (stage) and 
            the sleep cycle group has to be commons.sleep_cycle_group (cycle)
        "artifact_events" : Pandas DataFrame
            Artifact events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
            Artifacts that disable the spindle detection.
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
        "spindle_gen_param": Dict
            Options used to detect spindles
            "{
                'min_duration': 0.5
                'max_duration': 2.5
                'sleep_stage_sel' : [2,3]
                'in_cycle: : 1
                'exclude_nremp' : 0
                'exclude_remp' : 1
            }
        "spindle_sel_param": Dict
            Options specific to the det selected    
            "{
                -> Martin a4    
                    'spindle_name' : a4
                    'threshold' : 0.95
                    'threshold_per_cycle' : 1
                    'precision_on' : 1
                -> Lacourse A7
                    'spindle_name' : a7
                    'thresh_abs_sigma_pow_uv2' : 1.25
                    'thresh_rel_sigma_pow_z' : 1.6
                    'thresh_sigma_cov_z' : 1.3
                    'thresh_sigma_cor_perc' : 69               
            }"
        "report_constants": dict
            Constants used in the report (N_HOURS, N_CYCLES)   
        "cohort_filename": String
            Path and filename to save the spindle characteristics for the cohort. 
        "export_spindles" : bool
            True : generate a file per subject of the characteristics of each spindle.
            
    Outputs:
        Nothing since the spindle events details are saved in the cohort_filename.
        
    """
    def __init__(self, **kwargs):
        """ Initialize module SpindlesDetails """
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')

        # Input plugs
        InputPlug('recording_path',self)
        InputPlug('subject_info',self)
        InputPlug('signals',self)
        InputPlug('spindle_events',self)
        InputPlug('stages_cycles',self)
        InputPlug('artifact_events',self)
        InputPlug('sleep_cycle_param',self)
        InputPlug('spindle_gen_param',self)
        InputPlug('spindle_sel_param',self)
        InputPlug('report_constants',self)
        InputPlug('cohort_filename',self)
        InputPlug('export_spindles',self)

        # Init module variables
        self.stage_stats_labels = ['N1', 'N2', 'N3', 'R']

        # A master module allows the process to be reexcuted multiple time.
        self._is_master = False 
    
    
    def compute(self, recording_path, subject_info, signals, spindle_events, stages_cycles, artifact_events, \
        sleep_cycle_param, spindle_gen_param, spindle_sel_param, report_constants, cohort_filename, export_spindles):
        """
        To compute events characteristics such as duration, amplitude, frequency and so on.

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
            "spindle_events": Pandas DataFrame
                Spindle events defined as (columns=['group', 'name','start_sec','duration_sec','channels'])   
                The group has to be commons.sleep_spindle_group (spindle)
            "stages_cycles": Pandas DataFrame
                Spindle events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
                The sleep stage group has to be commons.sleep_stage_group (stage) and 
                the sleep cycle group has to be commons.sleep_cycle_group (cycle)
            "artifact_events" : Pandas DataFrame
                Artifact events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
                Artifacts that disable the spindle detection.
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
            "spindle_gen_param": Dict
                Options used to detect spindles
                "{
                    'min_duration': 0.5
                    'max_duration': 2.5
                    'sleep_stage_sel' : [2,3]
                    'in_cycle: : 1
                    'exclude_nremp' : 0
                    'exclude_remp' : 1
                }
            "spindle_sel_param": Dict
                Options specific to the det selected    
                "{
                    -> Martin a4    
                        'spindle_name' : a4
                        'threshold' : 0.95
                        'threshold_per_cycle' : 1
                        'precision_on' : 1
                    -> Lacourse A7
                        'spindle_name' : a7
                        'thresh_abs_sigma_pow_uv2' : 1.25
                        'thresh_rel_sigma_pow_z' : 1.6
                        'thresh_sigma_cov_z' : 1.3
                        'thresh_sigma_cor_perc' : 69               
                }"
            "report_constants": dict
                Constants used in the report (N_HOURS, N_CYCLES)   
            "cohort_filename": String
                Path and filename to save the spindle characteristics for the cohort. 
            "export_spindles" : bool
                True : generate a file per subject of the characteristics of each spindle.
                
        Outputs:
            Nothing since the spindle events details are saved in the cohort_filename.
            """
        if isinstance(export_spindles, str):
            export_spindles = eval(export_spindles)

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if recording_path=='':
            raise NodeInputException(self.identifier, "recording_path", \
                f"SpindlesDetails this input is empty, it needs to identify the recording to analyze.")
        if subject_info=='':
            raise NodeInputException(self.identifier, "subject_info", \
                f"SpindlesDetails this input is empty, it needs to identify the subject recorded.")
        if cohort_filename=='' and not export_spindles:
            raise NodeInputException(self.identifier, "cohort_filename", \
                f"SpindlesDetails has nothing to generate, 'cohort_filename' is empty and 'export_spindles' is False")    
        if isinstance(signals, str) and signals=='':
            raise NodeInputException(self.identifier, "signals", \
                f"SpindlesDetails this input is empty, no signals no details.")              
        if isinstance(spindle_events, str) and spindle_events=='':
            raise NodeInputException(self.identifier, "spindle_events", \
                f"SpindlesDetails this input is empty, no spindle_events no details.")     
        if isinstance(stages_cycles, str) and stages_cycles=='':
            raise NodeInputException(self.identifier, "stages_cycles", \
                f"SpindlesDetails this input is empty")    
        if isinstance(sleep_cycle_param, str) and sleep_cycle_param=='':
            raise NodeInputException(self.identifier, "sleep_cycle_param", \
                f"SpindlesDetails this input is empty")  
        if isinstance(spindle_gen_param, str) and spindle_gen_param=='':
            raise NodeInputException(self.identifier, "spindle_gen_param", \
                f"SpindlesDetails this input is empty")  
        if isinstance(spindle_sel_param, str) and spindle_sel_param=='':
            raise NodeInputException(self.identifier, "spindle_sel_param", \
                f"SpindlesDetails this input is empty")  

        if isinstance(report_constants,str) and report_constants == '':
            raise NodeInputException(self.identifier, "report_constants", \
                "SpindlesDetails report_constants parameter must be set.")
        elif isinstance(report_constants,str):
            report_constants = eval(report_constants)
        if isinstance(report_constants,dict) == False:
            raise NodeInputException(self.identifier, "report_constants",\
                "SpindlesDetails report_constants expected type is dict and received type is " +\
                    str(type(report_constants)))   
        self.N_HOURS = int(float(report_constants['N_HOURS']))
        self.N_CYCLES = int(float(report_constants['N_CYCLES']))

        # Raise NodeRuntimeException if there is a critical error during runtime. 
        # This exception will stop and skip the current process but will not stop the following
        # iterations if a master node is not done.
        # Once the master node is completed, a dialog will appear to show all NodeRuntimeException to the user.
        if len(signals)==0:
            raise NodeRuntimeException(self.identifier, "signals", \
                f"SpindlesDetails this input is empty, no signals no details.")              

        # To convert string to dict
        if isinstance(sleep_cycle_param, str):
            sleep_cycle_param = eval(sleep_cycle_param)
        if isinstance(spindle_gen_param, str):
            spindle_gen_param = eval(spindle_gen_param)
        if isinstance(spindle_sel_param, str):
            spindle_sel_param = eval(spindle_sel_param)

        # Extract subject info
        subject_info_params = {"filename": subject_info['filename']}
        if (subject_info['id1'] is not None) and len(subject_info['id1'].strip())>0:
            subject_info_params['id1'] = subject_info['id1']
        elif (subject_info['id2'] is not None) and len(subject_info['id2'].strip())>0:
            subject_info_params['id1'] = subject_info['id2']
        else:
            subject_info_params['id1'] = subject_info['id1']

        #-----------------------------------------------------------------------------------
        # Define the general spindle parameters
        #-----------------------------------------------------------------------------------
        gen_spindle_param = {}
        gen_spindle_param['min_sec'] = spindle_gen_param['min_duration'] # 'Minimum duration of the spindle in sec.',
        gen_spindle_param['max_sec'] = spindle_gen_param['max_duration']  # 'Maximum duration of the spindle in sec.',
        gen_spindle_param['sleep_stage_sel'] = spindle_gen_param['sleep_stage_sel']  # 'Sleep stages selection to detect spindles in.',
        gen_spindle_param['detect_in_cycle'] = spindle_gen_param['in_cycle']  # 'Flag to detect spindle in sleep cycles only.',
        gen_spindle_param['detect_exclude_remp'] = spindle_gen_param['exclude_remp']  # 'Flag to exclude rem period from the spindle detection.',    

        #-----------------------------------------------------------------------------------
        # Define the spindle parameter specific to the algorythm detection
        #-----------------------------------------------------------------------------------
        sel_spindle_param = {}
        # TODO adapt the code when other algorythms will be impletemented - maybe look at the spindle_name
        sel_spindle_param['spindle_event_name'] = spindle_sel_param['spindle_name'] #'Spindle event name (specific to the det,ection algorithm).',
        if ('a4' in sel_spindle_param['spindle_event_name'].lower()) or ('martin' in sel_spindle_param['spindle_event_name'].lower()):
            sel_spindle_param['threshold'] = spindle_sel_param['threshold'] #'Threshold (percentile) specific to martin detector',
            sel_spindle_param['threshold_per_cycle']= spindle_sel_param['threshold_per_cycle'] #'Flag to compute a threshold for each sleep cycle.',
            sel_spindle_param['precision_on']= spindle_sel_param['precision_on'] #'Flag to precise the onset and the duration of the spindle based on RMS sliding windows.',
        elif ('a7' in sel_spindle_param['spindle_event_name'].lower()) or ('lacourse' in sel_spindle_param['spindle_event_name'].lower()):
            sel_spindle_param['thresh_abs_sigma_pow_uv2'] = spindle_sel_param['thresh_abs_sigma_pow_uv2']
            sel_spindle_param['thresh_rel_sigma_pow_z'] = spindle_sel_param['thresh_rel_sigma_pow_z']
            sel_spindle_param['thresh_sigma_cov_z'] = spindle_sel_param['thresh_sigma_cov_z']
            sel_spindle_param['thresh_sigma_cor_perc'] = spindle_sel_param['thresh_sigma_cor_perc']        
        else:
            raise NodeRuntimeException(self.identifier, "spindle_sel_param", \
                f"SpindlesDetails The event label name for the spindles needs to include a4/a7 or martin/lacourse.") 
        sleep_stage_sel = gen_spindle_param['sleep_stage_sel']
        
        #-----------------------------------------------------------------------------------
        # Sleep stages and cyles extraction
        #-----------------------------------------------------------------------------------        
        # Select spindle event based on the spindle_name
        spindle_events = spindle_events[spindle_events['name']==spindle_sel_param['spindle_name']]

        # Extract sleep cycle parameters
        cycle_info_param = SleepReport.get_sleep_cycle_parameters(self, sleep_cycle_param)           
        sleep_cycles_df = stages_cycles[stages_cycles['group']==commons.sleep_cycle_group]
        sleep_cycles_df.reset_index(inplace=True, drop=True)
        sleep_cycle_count = {}
        sleep_cycle_count['sleep_cycle_count']=len(sleep_cycles_df) # 'Number of sleep cycles.',

        # Extract sleep stage info
        sleep_stage_df = stages_cycles[stages_cycles['group']==commons.sleep_stages_group].copy()
        sleep_stage_df.reset_index(inplace=True, drop=True)
        sleep_stage_df['name'] = sleep_stage_df['name'].apply(int)

        # Edit the cycle number 
        cycle_cnt = 0
        for index, row in sleep_cycles_df.iterrows():
            sleep_cycles_df.loc[index,'name']=cycle_cnt
            cycle_cnt = cycle_cnt+1

        # Exclude sleep stage before Sleep Onset
        # Exclude sleep stage after the end of the last cycle
        stage_in_cycle_df = self.exlude_stages_before_SO_after_awake(sleep_cycles_df, sleep_stage_df)

        # Exclude REMPs if exluded
        if spindle_gen_param['exclude_remp']==1:
            stage_in_cycle_df, sleep_cycles_df = self.exclude_remps(stages_cycles, sleep_cycles_df, stage_in_cycle_df)

        # TODO add if density per division of night if requested.
        # Extract sleep stages selected by the user from stage_in_cycle_df
        #stage_detection_df = stage_in_cycle_df[stage_in_cycle_df['name'].isin(sleep_stage_sel)]

        channels_list = np.unique(SignalModel.get_attribute(signals, 'channel', 'channel'))

        # For each spindle events add its sleep stage and cycle
        spindle_events = self.add_stage_cycle_to_spindle_df(spindle_events, stage_in_cycle_df, sleep_cycles_df)

        #-----------------------------------------------------------------------------------
        # Extract artifact group and name to save the info parameters
        #-----------------------------------------------------------------------------------
        artifact_info_param = {}
        group_name_artifact = artifact_events[['group','name']]
        group_name_artifact = group_name_artifact.drop_duplicates()
        group_name_artifact.reset_index(inplace=True, drop=True)
        artifact_info_param['artefact_group_name_list'] = ''
        for index, row in group_name_artifact.iterrows():
            temp = '('+str(index)+')'+"group:"+row['group']+" name:"+row['name']+' '
            artifact_info_param['artefact_group_name_list']=artifact_info_param['artefact_group_name_list']+temp

        #-----------------------------------------------------------------------------------
        # Compute and organize characteristics
        #-----------------------------------------------------------------------------------
        # Define the dataframe to save
        cohort_characteristics_df = []
        spindle_characteristics_df = pd.DataFrame()
        for channel in channels_list:

            # Define the channel info
            fs_chan = SignalModel.get_attribute(signals, 'sample_rate', 'channel', channel)[0][0] 
            channel_info_param = {}
            channel_info_param['chan_label']=channel
            channel_info_param['chan_fs']=fs_chan
            # Organize data for the output (GENERAL)
            cur_chan_general_dict = subject_info_params | cycle_info_param | gen_spindle_param | \
                sel_spindle_param | artifact_info_param | channel_info_param | sleep_cycle_count

            # Select spindles events for the current channel
            spindle_cur_chan_df = spindle_events[spindle_events['channels']==channel].copy() # dataFrame
            spindle_cur_chan_df.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')  
            spindle_cur_chan_df.reset_index(inplace=True, drop=True)

            # Extract the signal filtered in sigma of each spindle
            #   signals_spindle_cur_chan : list of samples
            #       each item is the signal filtered in sigma.
            #       each item is a spindle
            signals_spindle_cur_chan, spindle_cur_chan_df = \
                self.extract_sigma_signal_from_spindles(signals, fs_chan, channel, spindle_cur_chan_df)

            # Extract artifact for the current channel
            #   Artifact events have been cleanup to have a single channel as a string
            artifact_cur_chan_df = artifact_events[artifact_events['channels']==channel] 

            #-----------------------------------------------------------------------------------
            # Compute characteristics for each spindle (long to process so we do it only once)
            #-----------------------------------------------------------------------------------
            # Compute the dominant frequency of the signal.
            #   Frequency with the maximum energy between 11-16 Hz, found using 5s zero-padded fft
            dom_freq = self.compute_char_dom_freq( signals_spindle_cur_chan, fs_chan)
            spindle_cur_chan_df['dom_freq_Hz'] = dom_freq

            # Compute the average frequency of the signal counting peaks.
            #   Find positive peaks, average the duration between positive peaks, freq (Hz) = 1/avg_distance
            avg_freq = self.compute_char_avg_freq(signals_spindle_cur_chan, fs_chan)
            spindle_cur_chan_df['avg_freq_Hz'] = avg_freq

            # Compute the amplitude_pk-pk of the signal during the spindle
            pk_amp = self.compute_char_amp_pk_pk(signals_spindle_cur_chan)
            spindle_cur_chan_df['amp_pkpk_uV'] = pk_amp

            # Compute the amplitude rms of the signal during the spindle
            #   Compute RMS (Root Mean Squared) value of each spindle.
            rms_amp = self.compute_char_amp_rms(signals_spindle_cur_chan)
            spindle_cur_chan_df['amp_rms_uV'] = rms_amp

            #-----------------------------------------------------------------------------------
            # TOTAL statistics from the spindle events
            #-----------------------------------------------------------------------------------
            label_stats = 'total'

            # Compute duration (min)
            sleep_onset_sec = sleep_cycles_df['start_sec'].values[0]
            end_sleep_sec = sleep_cycles_df['start_sec'].values[-1]+sleep_cycles_df['duration_sec'].values[-1]
            # Remove REMP if excluded? no! It matches with Gaetan if we let it like this
            tot_rec_dur_stats = {'sleep_period_min': (end_sleep_sec - sleep_onset_sec)/60}
    
            # Compute valid duration (min)
            #   Return a dict as valid_dur[f'{label_stats}_valid_min_{stage}']
            tot_valid_dur_stats = self.compute_valid_dur_min(artifact_cur_chan_df, stage_in_cycle_df, \
                commons.sleep_stages_name, sleep_stage_sel, label_stats, self.stage_stats_labels)

            # Compute the spindle count, density, duration and all the characteristics per stage
            tot_ss_stats = self.compute_stats_spindle_gen_char(tot_valid_dur_stats, \
                spindle_cur_chan_df, sleep_stage_sel, label_stats)

            # Organize data for the output
            total_stats =  tot_rec_dur_stats | tot_valid_dur_stats | tot_ss_stats

            #-----------------------------------------------------------------------------------
            # CYCLE statistics from the spindle events
            #-----------------------------------------------------------------------------------
            label_stats = 'cyc'
            cycle_stats = self.compute_stats_for_cycles(spindle_cur_chan_df, sleep_cycles_df, \
                stage_in_cycle_df, artifact_cur_chan_df, sleep_stage_sel, label_stats)      

            # --------------------------------------------------------------------------
            # Organize data to Write the file
            # --------------------------------------------------------------------------
            # Organize data to write the spindle characteristics
            if export_spindles:
                spindle_cur_chan_df = spindle_cur_chan_df.reset_index(drop=True)
                if len(spindle_characteristics_df)==0:
                    spindle_characteristics_df = spindle_cur_chan_df
                else:
                    spindle_characteristics_df = pd.concat([spindle_characteristics_df, spindle_cur_chan_df],ignore_index=True)
            # Organize data to write the cohort spindle report
            # Construction of the pandas dataframe that will be used to create the TSV file
            # There is a new line for each channel and mini band
            cur_chan_dict = cur_chan_general_dict | total_stats | cycle_stats
            cur_chan_df = pd.DataFrame.from_records([cur_chan_dict])
            if len(cohort_characteristics_df):
                cohort_characteristics_df = pd.concat([cohort_characteristics_df, cur_chan_df])
            else:
                cohort_characteristics_df = cur_chan_df

        #----------------------------------------------------------------------------
        # Cohort TSV file
        #----------------------------------------------------------------------------
        if len(cohort_filename)>0:
            # Write the current report for the current subject into the cohort tsv file
            write_header = not os.path.exists(cohort_filename)
            # Order columns as the doc file
            out_columns = list(_get_doc(self.N_CYCLES, sel_spindle_param['spindle_event_name']).keys())

            cohort_characteristics_df = cohort_characteristics_df[out_columns]
            try : 
                cohort_characteristics_df.to_csv(path_or_buf=cohort_filename, sep='\t', \
                    index=False, index_label='False', mode='a', header=write_header, encoding="utf_8")
            except :
                error_message = f"Snooz can not write in the file {cohort_filename}."+\
                    f" Check if the drive is accessible and ensure the file is not already open."
                raise NodeRuntimeException(self.identifier, "SpindlesDetails", error_message)      

            # To write the info text file to describe the variable names
            if write_header:
                # Write the documentation file
                file_name, file_extension = os.path.splitext(cohort_filename)
                doc_filepath = file_name+"_info"+file_extension
                if not os.path.exists(doc_filepath):
                    write_doc_file(doc_filepath, self.N_CYCLES, sel_spindle_param['spindle_event_name'])
                    # Log message for the Logs tab
                    self._log_manager.log(self.identifier, f"The file {doc_filepath} has been created.")

            # Log message for the Logs tab
            self._log_manager.log(self.identifier, f"{subject_info['filename']} is added to {cohort_filename}.")
        
        #----------------------------------------------------------------------------
        # Spindle characteristics TSV file
        #----------------------------------------------------------------------------
        if export_spindles:
            if len(spindle_characteristics_df)>0:
                # We need to link the sw characteristics file with the PSG recording
                subject_id = subject_info['filename'] 
                # In a folder at the cohort level
                if len(cohort_filename)>0:
                    # Extract folder of the file
                    folder_cohort = os.path.dirname(cohort_filename)
                    # Make directory specific for spindles characteristics
                    folder_ss_char = os.path.join(folder_cohort, 'spindles_characteristics')
                    if not os.path.isdir(folder_ss_char):
                        os.makedirs(folder_ss_char)
                    ss_char_filename = os.path.join(folder_ss_char,subject_id)
                    ss_char_filename = ss_char_filename+'_'+spindle_sel_param['spindle_name']+'.tsv'
                # In the subject folder
                else:
                    # Extract folder of the file
                    folder_subject = os.path.dirname(recording_path)
                    ss_char_filename = os.path.join(folder_subject,subject_id)
                    ss_char_filename = ss_char_filename+'_'+spindle_sel_param['spindle_name']+'.tsv'
                # Sort from start_time (events are ordered per channel) and remove index for the output text file
                spindle_characteristics_df = spindle_characteristics_df.sort_values(by=['start_sec'])
                spindle_characteristics_df = spindle_characteristics_df.reset_index(drop=True) # do not add an index column
                try : 
                    spindle_characteristics_df.to_csv(path_or_buf=ss_char_filename, sep='\t', index=False, index_label='False', mode='w', header=True, encoding="utf_8")
                    # Log message for the Logs tab
                    self._log_manager.log(self.identifier, f"Spindles characteristics from {subject_info['filename']} has been generated.")
                except :
                    error_message = f"Snooz can not write in the file {ss_char_filename}."+\
                        f" Check if the drive is accessible and ensure the file is not already open."
                    raise NodeRuntimeException(self.identifier, "SpindlesDetails", error_message)  
            else:
                # Log message for the Logs tab
                self._log_manager.log(self.identifier, f"No spindles for {subject_info['filename']}.")

        return {
        }


    
    def add_stage_cycle_to_spindle_df(self, spindle_events, stage_in_cycle_df, sleep_cycle_df):
        """""
        Add the sleep stage to the spindle_events in a new column named 'stage'.

        Parameters
        -----------
            spindle_events     : Pandas DataFrame
                spindle events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
            stage_in_cycle_df   : Pandas DataFrame
                Sleep stage events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
            sleep_cycle_df      : Pandas DataFrame
                Sleep cycle events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
                The group is cycle and the name is from 0 to last cycle number.
            
        Returns
        -----------  
            spindle_events  : Pandas DataFrame
                spindle events defined as (columns=['group', 'name','start_sec','duration_sec','channels', 'stage', 'cycle])        
        """""
        # Extract stage info
        stage_start_all = stage_in_cycle_df['start_sec'].to_numpy()
        stage_start_all = np.round(stage_start_all,2) # without precision, the event could be labelled with the wrong stage
        stage_end_all = stage_start_all+stage_in_cycle_df['duration_sec'].to_numpy()
        stage_end_all = np.round(stage_end_all,2)
        stage_name_all = stage_in_cycle_df['name'].to_numpy()

        # Extract cycle info
        cycle_start_all = sleep_cycle_df['start_sec'].to_numpy()
        cycle_start_all = np.round(cycle_start_all,2)
        cycle_end_all = cycle_start_all+sleep_cycle_df['duration_sec'].to_numpy()
        cycle_end_all = np.round(cycle_end_all,2)
        cycle_name_all = sleep_cycle_df['name'].to_numpy()

        ss_start_time = spindle_events['start_sec'].to_numpy()
        ss_stage = []
        ss_cycle = []
        for start_time in ss_start_time:
            # We select the stage where the spindle starts
            stage_sel_arr = (stage_start_all<=start_time) & (stage_end_all>start_time)
            cycle_sel_arr = (cycle_start_all<=start_time) & (cycle_end_all>start_time)
            if any(stage_sel_arr):
                cur_stage = stage_name_all[stage_sel_arr]
                ss_stage.append(cur_stage[0])
            else:
                ss_stage.append(np.nan)
            if any(cycle_sel_arr):
                cur_cycle = cycle_name_all[cycle_sel_arr]
                ss_cycle.append(cur_cycle[0])
            else:
                ss_cycle.append(np.nan)
        spindle_events['stage'] = ss_stage 
        spindle_events['cycle'] = ss_cycle
        spindle_events = spindle_events.sort_values(by=['start_sec'])
        spindle_events = spindle_events.reset_index(drop=True)
        return spindle_events

    
    def compute_stats_spindle_gen_char(self, valid_dur, spindle_cur_chan_df, sleep_stage_sel, label_stats):
        """""
        Compute the general spindle characteristics such as count, density and average duration 
        for all spindles in spindle_cur_chan_df.

        Parameters
        -----------
            spindle_cur_chan_df : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels', 'stage', 'cycle']) 
                The spindle events
            sleep_stage_sel     : list of string
                List of sleep stage number selected (ex. ['2', '3'])
            label_stats : string
                The label of the statistics to export. I.e. : 'total', 'cycle1', 'cycle2', ...
        Returns
        -----------  
            spindle_stats   : dict
                with keys: 
                    f'{label_stats}_ss_count_{stage}'
                    f'{label_stats}_density_min_{stage}'
                    f'{label_stats}_sec_{stage}'
                    f'{label_stats}_dom_freq_Hz_{stage}'
                        ...
        """""
        ss_count = {}
        density_min = {}
        duration_s = {}
        dom_freq_Hz = {}
        avg_freq_Hz = {}
        amp_pkpk_uV = {}
        amp_rms_uV = {}
        ss_count_total = 0
        duration_s_all = []
        dom_freq_Hz_all = []
        avg_freq_Hz_all = []
        amp_pkpk_uV_all = []
        amp_rms_uV_all = []
        for stage in self.stage_stats_labels:
            # If selected
            if commons.sleep_stages_name[stage] in sleep_stage_sel:
                
                # Count the number of spindle for the current stage
                spindle_cur_stage = spindle_cur_chan_df[spindle_cur_chan_df['stage']==int(commons.sleep_stages_name[stage])]
                ss_count_cur_stage = len(spindle_cur_stage)
                ss_count_total = ss_count_total + ss_count_cur_stage
                if valid_dur[f'{label_stats}_{stage}_valid_min']>0:
                    ss_count[f'{label_stats}_{stage}_spindle_count'] = ss_count_cur_stage
                else:
                    ss_count[f'{label_stats}_{stage}_spindle_count'] = np.nan
                # Compute the density
                if valid_dur[f'{label_stats}_{stage}_valid_min']>0:
                    density_min[f'{label_stats}_{stage}_density'] = ss_count_cur_stage/valid_dur[f'{label_stats}_{stage}_valid_min']
                else:
                    density_min[f'{label_stats}_{stage}_density'] = np.nan

                if ss_count_cur_stage>0:
                    duration_s[f'{label_stats}_{stage}_spindle_sec'] = spindle_cur_stage['duration_sec'].sum()/ss_count_cur_stage
                    dom_freq_Hz[f'{label_stats}_{stage}_dom_freq_Hz'] = spindle_cur_stage['dom_freq_Hz'].sum()/ss_count_cur_stage
                    avg_freq_Hz[f'{label_stats}_{stage}_avg_freq_Hz'] = spindle_cur_stage['avg_freq_Hz'].sum()/ss_count_cur_stage
                    amp_pkpk_uV[f'{label_stats}_{stage}_amp_pkpk_uV'] = spindle_cur_stage['amp_pkpk_uV'].sum()/ss_count_cur_stage
                    amp_rms_uV[f'{label_stats}_{stage}_amp_rms_uV'] = spindle_cur_stage['amp_rms_uV'].sum()/ss_count_cur_stage
                else:
                    duration_s[f'{label_stats}_{stage}_spindle_sec'] = np.NaN
                    dom_freq_Hz[f'{label_stats}_{stage}_dom_freq_Hz'] = np.NaN
                    avg_freq_Hz[f'{label_stats}_{stage}_avg_freq_Hz'] = np.NaN
                    avg_freq_Hz[f'{label_stats}_{stage}_amp_pkpk_uV'] = np.NaN
                    amp_rms_uV[f'{label_stats}_{stage}_amp_rms_uV'] = np.NaN

                if len(duration_s_all)==0:
                    duration_s_all = spindle_cur_stage['duration_sec'].values
                else:
                    duration_s_all = np.concatenate((duration_s_all,spindle_cur_stage['duration_sec'].values), axis=0)

                if len(dom_freq_Hz_all)==0:
                    dom_freq_Hz_all = spindle_cur_stage['dom_freq_Hz'].values
                else:
                    dom_freq_Hz_all = np.concatenate((dom_freq_Hz_all,spindle_cur_stage['dom_freq_Hz'].values), axis=0)

                if len(avg_freq_Hz_all)==0:
                    avg_freq_Hz_all = spindle_cur_stage['avg_freq_Hz'].values
                else:
                    avg_freq_Hz_all = np.concatenate((avg_freq_Hz_all,spindle_cur_stage['avg_freq_Hz'].values), axis=0)

                if len(amp_pkpk_uV_all)==0:
                    amp_pkpk_uV_all = spindle_cur_stage['amp_pkpk_uV'].values
                else:
                    amp_pkpk_uV_all = np.concatenate((amp_pkpk_uV_all,spindle_cur_stage['amp_pkpk_uV'].values), axis=0)

                if len(amp_rms_uV_all)==0:
                    amp_rms_uV_all = spindle_cur_stage['amp_rms_uV'].values
                else:
                    amp_rms_uV_all = np.concatenate((amp_rms_uV_all,spindle_cur_stage['amp_rms_uV'].values), axis=0)
            else:
                ss_count[f'{label_stats}_{stage}_spindle_count'] = np.NaN
                density_min[f'{label_stats}_{stage}_density'] = np.NaN
                duration_s[f'{label_stats}_{stage}_spindle_sec'] = np.NaN
                dom_freq_Hz[f'{label_stats}_{stage}_dom_freq_Hz'] = np.NaN
                avg_freq_Hz[f'{label_stats}_{stage}_avg_freq_Hz'] = np.NaN
                amp_pkpk_uV[f'{label_stats}_{stage}_amp_pkpk_uV'] = np.NaN
                amp_rms_uV[f'{label_stats}_{stage}_amp_rms_uV'] = np.NaN

        # Total stats on the accumulated data
        ss_count[f'{label_stats}_spindle_count'] = ss_count_total
        if valid_dur[f'{label_stats}_valid_min']>0:
            density_min[f'{label_stats}_density'] = ss_count_total/valid_dur[f'{label_stats}_valid_min']
        else:
            density_min[f'{label_stats}_density'] = np.NaN
        duration_s[f'{label_stats}_spindle_sec'] = np.mean(duration_s_all)
        dom_freq_Hz[f'{label_stats}_dom_freq_Hz'] = np.mean(dom_freq_Hz_all)
        avg_freq_Hz[f'{label_stats}_avg_freq_Hz'] = np.mean(avg_freq_Hz_all)
        amp_pkpk_uV[f'{label_stats}_amp_pkpk_uV'] = np.mean(amp_pkpk_uV_all)
        amp_rms_uV[f'{label_stats}_amp_rms_uV'] = np.mean(amp_rms_uV_all)

        spindle_stats = ss_count | density_min | duration_s | dom_freq_Hz | avg_freq_Hz | amp_pkpk_uV | amp_rms_uV
        return spindle_stats


    def compute_valid_dur_min(self, art_cur_chan_df, stage_in_cycle_df, sleep_stages_name, sleep_stage_sel, label_stats, stage_stats_labels):
        """""
        For each sleep stage included in stage_in_cycle_df, compute the duration without artifact (valid_min).

        Parameters
        -----------
            art_cur_chan_df     : Pandas DataFrame
                Artifact events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
                Artifacts that disable the spindle detection, artifact are selected for the current channel.
            stage_in_cycle_df   : Pandas DataFrame
                Sleep stage events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
            sleep_stages_name   : dict
                Dict of sleep stage label to number (commons.sleep_stages_name)
            sleep_stage_sel     : list of string
                List of sleep stage number selected (ex. ['2', '3']) 
            label_stats         : string
                The label of the stats to compute. I.e. 'total' or 'cycle'
            stage_stats_labels : list of string
                List of label to use for the stages.
                ex. ['N1', 'N2', 'N3', 'R']
        Returns
        -----------  
            valid_dur  : dict
                Dict of valid duration in min.
        """""
        # Manage sleep stage
        stage_start_in_cycle = stage_in_cycle_df['start_sec'].to_numpy()
        #stage_start_in_cycle = np.around(stage_start_in_cycle)
        stage_dur_in_cycle = stage_in_cycle_df['duration_sec'].to_numpy()
        #stage_dur_in_cycle = np.around(stage_dur_in_cycle)        
        stage_end_in_cycle = stage_start_in_cycle+stage_dur_in_cycle
        stage_label_in_cycle = stage_in_cycle_df['name'].to_numpy()
        stage_label_in_cycle = stage_label_in_cycle.astype(int)

        # Manage artifact
        # Extract artifact for the current channel
        art_start_np = art_cur_chan_df['start_sec'].to_numpy()
        #art_start_np = np.around(art_start_np)
        art_dur_np = art_cur_chan_df['duration_sec'].to_numpy()
        #art_dur_np = np.around(art_dur_np)
        art_end_np = art_start_np + art_dur_np  

        valid_dur = {}
        valid_dur_sec = 0
        invalid_dur_sec = 0
        for stage in stage_stats_labels:
            inv_dur_sec_cur_stage = 0
            if sleep_stages_name[stage] in sleep_stage_sel:
                stage_sel = stage_label_in_cycle==int(sleep_stages_name[stage])
                stage_start_cur = stage_start_in_cycle[stage_sel]
                stage_dur_cur = stage_dur_in_cycle[stage_sel]
                stage_end_cur = stage_end_in_cycle[stage_sel]
                i_stage = 0
                # For all epochs from the current sleep stage
                for start_epoch, end_epoch in zip(stage_start_cur, stage_end_cur):
                    if any((art_start_np<end_epoch) & (art_end_np>start_epoch)):

                        # To compute the invalide duration because of artifact (defined by art_start_np, 
                        # art_dur_np, art_end_np) for the current epoch defined by start_epoch and end_epoch.
                        # Each value of the numpy array (art_start_np, art_dur_np, art_end_np) corresponds to an artifact.

                        inv_dur_sec_cur_epoch = 0
                        # Manage the artifacts that start before the sleep onset, end after SO but before the end of the last cycle
                            # The duration is the difference between the end of the artifact and the SO
                        art_dur_before_SO = art_end_np[(art_start_np < start_epoch) & (art_end_np > start_epoch) & (art_end_np < end_epoch )]-start_epoch
                        inv_dur_sec_cur_epoch = inv_dur_sec_cur_epoch + art_dur_before_SO.sum()
                        # Manage the artifacts that start after the sleep onset but end before the end of the last cycle
                            # The duration is the sum of the duration of all the artifacts
                        art_sel_in_cycles = (art_start_np >= start_epoch) & (art_end_np <= end_epoch)
                        inv_dur_sec_cur_epoch = inv_dur_sec_cur_epoch + art_dur_np[art_sel_in_cycles].sum()
                        # Manage the artifact that end after the end of the last cycle, but start after the start_epoch
                            # The duration is the difference between the end of the last cycle and the artifact start
                        art_sel_after_last_cycle = (art_start_np < end_epoch) & (art_end_np > end_epoch) & (art_start_np >= start_epoch)
                        art_dur_after_last_cycle = end_epoch-art_start_np[art_sel_after_last_cycle]
                        inv_dur_sec_cur_epoch = inv_dur_sec_cur_epoch + art_dur_after_last_cycle.sum()
                        # Manage the artifact that start before the SO and end after the last cycle.
                        art_sel_all_time = (art_start_np < start_epoch) & (art_end_np > end_epoch)
                        if any(art_sel_all_time):
                            inv_dur_sec_cur_epoch = inv_dur_sec_cur_epoch + end_epoch-start_epoch
                    else:
                        inv_dur_sec_cur_epoch=0
                    inv_dur_sec_cur_stage = inv_dur_sec_cur_stage + inv_dur_sec_cur_epoch
                    i_stage = i_stage +1 
                # Compute the valid duration for the current stage
                valid_dur[f'{label_stats}_{stage}_valid_min'] = (stage_dur_cur.sum()-inv_dur_sec_cur_stage)/60
                # Compute the total valid duration
                valid_dur_sec = valid_dur_sec + (stage_dur_cur.sum()-inv_dur_sec_cur_stage)
                invalid_dur_sec = invalid_dur_sec + inv_dur_sec_cur_stage
            else:
                valid_dur[f'{label_stats}_{stage}_valid_min'] = 0
        # for now does not match with Gaetan, just add valid time
        valid_dur[f'{label_stats}_valid_min'] = valid_dur_sec/60
        return valid_dur


    def _filter_signals_in_sigma(self,signals_cur_chan, fs_chan):
        """""
            Filter the list of SignalModel.samples in the sigma band.
            Return a list of SignalModel bandpass filtered in sigma.

            Parameters
            -----------
                signals_cur_chan : list of SignalModel               
            Returns
            -----------  
                signals_sigma  : list of SignalModel           
                    Signal bandpass filtered in sigma
        """""        
        order=10
        low_freq = 11
        high_freq = 16
        signals_sigma = []
        for i, signal_model in enumerate(signals_cur_chan):
            order_filtfilt = int(order)/2
            sos = sci_signal.butter(int(order_filtfilt), [low_freq,high_freq],btype='bandpass', output='sos', fs=fs_chan)
            filtered_signal = sci_signal.sosfiltfilt(sos, signal_model.samples)
            # Clone the signal object and set it back into the dictionary
            s = signal_model.clone(clone_samples=False)
            s.samples = filtered_signal
            s.is_modified = True
            signals_sigma.append(s)
        return signals_sigma


    def _open_dialog_fig_filtered_spindle(self, signals_cur_chan, signals_sigma, fs_chan, ss_start_times, ss_dur_times, signal_sel, ss_start, ss_dur, spindle_i):
        """""
            Debug function to open figure in a dialog. This funciton display the original spindle (mean removed) 
            and the filtered spindle in sigma band.
        """""
        from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
        from matplotlib.figure import Figure
        from PySide2.QtWidgets import QDialog, QVBoxLayout

        # Extract and define the new extracted channel_cur
        signal_cur = SignalsFromEvents.extract_events_from_signal(SignalsFromEvents, signals_cur_chan[signal_sel], ss_start, ss_dur)
        sigma_cur = SignalsFromEvents.extract_events_from_signal(SignalsFromEvents, signals_sigma[signal_sel], ss_start, ss_dur)

        dialog = QDialog()
        fig = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvas(fig)
        time = np.arange(ss_start_times[spindle_i],ss_start_times[spindle_i]+ss_dur_times[spindle_i],1/fs_chan)
        ax = fig.add_subplot(111)
        ax.plot(time,signal_cur.samples-np.mean(signal_cur.samples),'k')
        #ax.title.set_text('raw signal')
        ax.plot(time,sigma_cur.samples, 'r')
        #ax.title.set_text('signal 11-16 Hz')
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        dialog.setLayout(layout)
        dialog.exec_()


    def _open_dialog_fig_psa_spindle(self, freq_bins, fft_result_win, freq_max_energy):
        """""
            Debug function to open figure in a dialog. This funciton display the spectre and the frequency 
            with the highest energy in the sigma band.
        """""
        from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
        from matplotlib.figure import Figure
        from PySide2.QtWidgets import QDialog, QVBoxLayout
        dialog = QDialog()
        fig = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.plot(freq_bins,abs(fft_result_win),'k')
        ax.axvline(x = freq_max_energy, color = 'r')
        #ax.text(freq_max_energy,max(abs(fft_result_win_sigma)),'X',color='r',horizontalalignment='center')
        ax.set_xlim(5.0,20.0)
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        dialog.setLayout(layout)
        dialog.exec_()


    def compute_char_dom_freq(self, signals_spindle_cur_chan, fs_chan):
        """""
            Compute the dominant frequency of each signal included in signals_spindle_cur_chan.
            Frequency with the maximum energy between 11-16 Hz, found using 5s zero-padded fft

            Parameters
            -----------
                signals_spindle_cur_chan : list of array
                    Each item is the samples of a spindle
                fs_chan : float
                    Sampling frequency (Hz)

            Returns
            -----------  
                list_dom_freq  : list       
                    Dominant frequency for each spindle event.
        """""
        low_freq = 11
        high_freq = 16
        list_dom_freq = []
        win_len_sec = 5
        nsample_fft = int(win_len_sec*fs_chan)
        # A loop on each event
        for ss_signal in signals_spindle_cur_chan:
            # Pad around signal
            nsample_signal = len(ss_signal)
            npads = nsample_fft - nsample_signal
            if npads<0: # Spindle are always shorter than 5 s
                    raise NodeRuntimeException(self.identifier, "spindle_events", \
                    f"SpindlesDetails spindle event longer than {win_len_sec} s")
            else:
                ss_signal_pad = np.pad(ss_signal,(int(npads/2),int(npads-int(npads/2))))
            # Calculate the number of frequency bins (= number of cols in the output)
            freq_bins = sp_fft.rfftfreq(nsample_fft, 1./fs_chan)     
            # Perform the one sided right fft 
            fft_result_win = sp_fft.rfft(ss_signal_pad, n=nsample_fft, axis=0)        
            fft_result_win_sigma = fft_result_win[(freq_bins>=low_freq) & (freq_bins<=high_freq)]
            fft_freq_sigma = freq_bins[(freq_bins>=low_freq) & (freq_bins<=high_freq)]
            freq_i = np.argmax(abs(fft_result_win_sigma))
            freq_max_energy = fft_freq_sigma[freq_i]
            list_dom_freq.append(freq_max_energy)

            # # Open figure to debug, need to add a breakpoint at the code self._open_dialog_fig_psa_spindle
            # self._open_dialog_fig_psa_spindle(freq_bins, fft_result_win, freq_max_energy)

        return list_dom_freq


    def compute_char_avg_freq(self, signals_spindle_cur_chan, fs_chan):
        """""
            Compute the average frequency of each signal included in signals_spindle_cur_chan.
            Frequency with the maximum energy between 11-16 Hz, found using 5s zero-padded fft

            Parameters
            -----------
                signals_spindle_cur_chan : list of array
                    Each item is the samples of a spindle
                fs_chan : float
                    Sampling frequency (Hz)
            Returns
            -----------  
                avg_freq  : dict       
                    keys depend on the label_stats : ex) total_avg_freq_Hz, total_avg_freq_Hz_N2, total_avg_freq_N3
                spindle_cur_chan_df : Pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels', 'stage', 'cycle', 'avg_freq_Hz']) 
                    List of spindles with the average frequency added.
        """""            
        # A loop on each event
        list_avg_freq = []
        for ss_signal in signals_spindle_cur_chan:
            # Find positive peaks
            peaks, _ = sci_signal.find_peaks(ss_signal)
            # average the duration between positive peaks
            time = np.arange(0,len(ss_signal)/fs_chan,1/fs_chan)
            # freq (Hz) = 1/avg_distance
            avg_freq_Hz = 1/np.mean(np.diff(time[peaks])) 
            list_avg_freq.append(avg_freq_Hz)
        return list_avg_freq

    

    def compute_char_amp_pk_pk(self, signals_spindle_cur_chan):
        """""
            Compute the amplitude peak-to-peak of the signal.
            Using scipy.signal.find_peaks, find positive peaks, find negative peaks, merge and sort (by position time)
            and compute max diff between consecutive peak.

            Parameters
            -----------
                signals_spindle_cur_chan : list of array
                    Each item is the samples of a spindle
            Returns
            -----------  
                list_pk_amp : list       
                    Amplitude peak-to-peak for each spindle event.
        """""  
        # A loop on each event
        list_pk_amp = []
        for ss_signal in signals_spindle_cur_chan:
            # Find positive peaks
            pos_peaks, _ = sci_signal.find_peaks(ss_signal)
            # Find negative peaks
            neg_peaks, _ = sci_signal.find_peaks(ss_signal*-1)
            # merge and sort (by position time)
            all_peaks = np.sort(np.concatenate([pos_peaks,neg_peaks]))
            pk_amp = np.max(np.abs(np.diff(ss_signal[all_peaks])))
            # Accumulate Total for the cohort file
            list_pk_amp.append(pk_amp)      
        return list_pk_amp


    def compute_char_amp_rms(self, signals_spindle_cur_chan):
        """""
            Compute the amplitude rms (Root Means Squared) of the signal.

            Parameters
            -----------
                signals_spindle_cur_chan : list of array
                    Each item is the samples of a spindle
            Returns
            -----------  
                list_rms_amp  : list       
                    Rms amplitude for each spindle event.
        """"" 
        # A loop on each event
        list_rms_amp = []
        for ss_signal in signals_spindle_cur_chan:
            # square the data
            ss_signal_p2 = np.power(ss_signal, 2)
            # Compute the average of each window
            ss_signal_p2_avg = np.nanmean(ss_signal_p2, axis=0)
            # Compute squared root
            ss_signal_p2_avg_sqrt = np.sqrt(ss_signal_p2_avg)
            # Accumulate Total for the cohort file
            list_rms_amp.append(ss_signal_p2_avg_sqrt)                  
        return list_rms_amp


    def extract_sigma_signal_from_spindles(self, signals, fs_chan, channel, spindle_cur_chan_df):
        """""
            Extract signal filtered in sigma for each spindles for the channel in the input.

            Parameters
            -----------
                signals             : List of SignalModel
                    List of all signals (all channels)
                fs_chan             : float
                    Sampling frequency (Hz) of the selected channel.
                channel             : string
                    Label of the selected channel
                spindle_cur_chan_df : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])  
                    List of spindles.

            Returns
            -----------  
                signals_spindle_cur_chan : list of numpy array
                    The samples of each spindle (filtered in sigma)
                spindle_cur_chan_df : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])  
                    List of spindles.

        """""

        ss_start_times = spindle_cur_chan_df['start_sec'].to_numpy().astype(float)   # numpy array
        ss_dur_times = spindle_cur_chan_df['duration_sec'].to_numpy().astype(float)  # numpy array

        # Extract signals for the current channel as list of SignalModel
        signals_cur_chan = SignalModel.get_attribute(signals, None, 'channel', channel).tolist()
        # Extract start_time of the signals for the current channel as numpy array
        signals_starttime = SignalModel.get_attribute(signals_cur_chan, 'start_time', 'start_time').flatten()
        # Extract end_time of the signals for the current channel as numpy array
        signals_endtime = SignalModel.get_attribute(signals_cur_chan, 'end_time', 'end_time').flatten()
        
        # The signal is already filtered in sigma
        # To avoid border effect on each spindle, we filtter the whole signal
        # Filter 11-16 Hz all the signals
        # signals_sigma = self._filter_signals_in_sigma(signals_cur_chan, fs_chan)

        # Extract signal from the list of spindle filtered in sigma
        # Create my list of slice signals
        signals_spindle_cur_chan = []
        spindle_index_to_drop = []
        spindle_i = 0
        for ss_start, ss_dur in zip(ss_start_times, ss_dur_times):
            # Find in within signal the spindle is included
            ss_start_in_signal = signals_starttime<(ss_start+ss_dur)
            ss_end_in_signal = signals_endtime>ss_start
            ss_sel_in_signal = ss_start_in_signal & ss_end_in_signal
            # Only one signal should include the spindle since the signals are splitted in continuous bouts (not stages)
            if sum(ss_sel_in_signal)==1:
                signal_sel = np.nonzero(ss_sel_in_signal)[0][0]
                # Extract and define the new extracted channel_cur
                sigma_cur = SignalsFromEvents.extract_events_from_signal(SignalsFromEvents, signals_cur_chan[signal_sel], ss_start, ss_dur)
                signals_spindle_cur_chan.append(sigma_cur.samples)
                # Open figure to debug, need to add a breakpoint at the code self._open_dialog_fig_filtered_spindle
                # self._open_dialog_fig_filtered_spindle(signals_cur_chan, signals_sigma, fs_chan, ss_start_times, \
                #     ss_dur_times, signal_sel, ss_start, ss_dur, spindle_i)
            elif sum(ss_sel_in_signal)==0:
                # Log message for the Logs tab
                self._log_manager.log(self.identifier, f"SpindlesDetails spindle event not included in the signals")
                spindle_index_to_drop.append(spindle_i)
            elif sum(ss_sel_in_signal)>1:
                raise NodeRuntimeException(self.identifier, "signals", \
                    f"SpindlesDetails spindle included in many signals")                
            spindle_i = spindle_i +1
        # Drop spindles from the official list to compute stats
        # Can happen when we analyze spindles (without detecting them from the current pipeline)
        if len(spindle_index_to_drop)>0:
            spindle_cur_chan_df.drop(spindle_index_to_drop, inplace=True)
        return signals_spindle_cur_chan, spindle_cur_chan_df


    def exlude_stages_before_SO_after_awake(self, sleep_cycles_df, sleep_stage_df):
        """""
            Exclude sleep stage before Sleep Onset
            Exclude sleep stage after the end of the last cycle

            Parameters
            -----------
                sleep_cycles_df             : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])  
                    List of cycles.
                sleep_stage_df              : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])  
                    List of sleep stages
            Returns
            -----------  
                stage_in_cycle_df : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels']) 

        """""
        onlyCycle = pd.DataFrame(columns=['group','name','start_sec','duration_sec','channels'])
        # Keep any stage inside cycle
        for index, row in sleep_cycles_df.iterrows():
            idx_start = sleep_stage_df[sleep_stage_df.start_sec>=row.start_sec].index
            idx_stop = sleep_stage_df[ (sleep_stage_df.start_sec+sleep_stage_df.duration_sec) <= (row.start_sec+row.duration_sec)].index
            idx_in_cycle = idx_start.intersection(idx_stop)
            onlyCycle = pd.concat([onlyCycle,sleep_stage_df.loc[idx_in_cycle]])
        stage_in_cycle_df = onlyCycle   
        stage_in_cycle_df.reset_index(inplace=True, drop=True) 
        return stage_in_cycle_df


    def exclude_remps(self, stages_cycles, sleep_cycles_df, stage_in_cycle_df):
        """""
            Exclude sleep stages during the remps.
            Remove the remps from the cycles, reduce the duration of each cycle with a remps.

            Parameters
            -----------
                stages_cycles              : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels']) 
                    List of stages, cycles, nremps and remps.
                sleep_cycles_df            : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])  
                    List of cycles.
                stage_in_cycle_df          : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])  
                    List of sleep stages included in the cycles.
            Returns
            -----------  
                stage_in_cycle_df           : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels']) 
                    List of stages without the stages in remps.
                sleep_cycles_df             : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels']) 
                    List of cycles with the duration corrected to remove the remps.
        """""
        remps_df = stages_cycles[stages_cycles['group']==commons.rem_period_group]
        remps_df.reset_index(inplace=True, drop=True) 
        for index, row in remps_df.iterrows():
            idx_start = stage_in_cycle_df[stage_in_cycle_df.start_sec>=row.start_sec].index
            idx_stop = stage_in_cycle_df[ (stage_in_cycle_df.start_sec+stage_in_cycle_df.duration_sec) <= (row.start_sec+row.duration_sec)].index
            idx_in_remps = idx_start.intersection(idx_stop) 
            stage_in_cycle_df.drop(idx_in_remps, inplace=True)
            # Remove the remps from the cyvle, reduce the duration of the cycle
            sleep_cycles_df.loc[index, 'duration_sec'] = sleep_cycles_df.loc[index, 'duration_sec']-row['duration_sec']
        return stage_in_cycle_df, sleep_cycles_df


    def compute_stats_for_cycles(self, spindle_cur_chan_df, sleep_cycles_df, \
        stage_in_cycle_df, artifact_cur_chan_df, sleep_stage_sel, label_stats):
        """""
            Compute statistics for each cycle

            Parameters
            -----------
                spindle_cur_chan_df : pandas DataFrame 
                    spindle events including the characteristics
                sleep_cycles_df     : pandas DataFrame
                    sleep cycles list
                stage_in_cycle_df   : pandas DataFrame
                    List of sleep stages included in the cycles.
                artifact_cur_chan_df : pandas DataFrame
                    List of artifacts events
                sleep_stage_sel     : list
                    List of sleep stage number selected (ex. ['2', '3'])
                label_stats         : str
                    The label of the statistics to export. I.e. : 'cyc', ...

            Returns
            -----------  
                stats   : dict
                    List of statistics for each cycle.
        """""
        # Spindle events
        ss_start_times = spindle_cur_chan_df['start_sec'].to_numpy().astype(float)   # numpy array
        ss_dur_times = spindle_cur_chan_df['duration_sec'].to_numpy().astype(float)  # numpy array
        ss_end_times = ss_start_times+ss_dur_times

        # Cycle events
        cycle_starts = sleep_cycles_df['start_sec'].values
        cycle_durations = sleep_cycles_df['duration_sec'].values
        cycle_ends = cycle_starts+cycle_durations

        # Stage events
        stage_starts = stage_in_cycle_df['start_sec'].values
        stage_durations = stage_in_cycle_df['duration_sec'].values
        stage_ends = stage_starts+stage_durations    

        # For each sleep cycle
        cyc_valid_dur_stats = {}
        cyc_ss_stats = {}
        cyc_rec_dur_stats = {}
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

                # Select the spindles from the current cycle
                spindle_bool = (ss_start_times>=i_cycle_start) & (ss_end_times<=i_cycle_end)
                spindle_sel_i = np.nonzero(spindle_bool)[0]
                # To know in which sleep stage the spindle occurs
                spindle_sel_df = spindle_cur_chan_df.iloc[spindle_sel_i] 

                # Compute duration (min)
                cyc_rec_dur_stats[f'{cycle_label}_min'] = cycle_durations[i_cycle]/60

                # Compute valid duration (min)
                #   For each sleep stage included in stage_sel_df, compute the duration without artifact (valid_min).
                valid_dur_stats_cur = self.compute_valid_dur_min(artifact_cur_chan_df, stage_sel_df, \
                    commons.sleep_stages_name, sleep_stage_sel, cycle_label, self.stage_stats_labels)
                cyc_valid_dur_stats = cyc_valid_dur_stats | valid_dur_stats_cur

                # Compute the spindle count, density, duration and all the characteristics per stage
                ss_stats_cur = self.compute_stats_spindle_gen_char(valid_dur_stats_cur, spindle_sel_df, sleep_stage_sel, cycle_label)
                cyc_ss_stats = cyc_ss_stats | ss_stats_cur
        
            else:
                cyc_rec_dur_stats[f'{cycle_label}_min'] = 0
                cyc_valid_dur_stats[f'{cycle_label}_valid_min']=np.NaN
                cyc_ss_stats[f'{cycle_label}_spindle_count']=np.NaN
                cyc_ss_stats[f'{cycle_label}_density']=np.NaN
                cyc_ss_stats[f'{cycle_label}_spindle_sec']=np.NaN
                cyc_ss_stats[f'{cycle_label}_dom_freq_Hz']=np.NaN
                cyc_ss_stats[f'{cycle_label}_avg_freq_Hz']=np.NaN
                cyc_ss_stats[f'{cycle_label}_amp_pkpk_uV']=np.NaN
                cyc_ss_stats[f'{cycle_label}_amp_rms_uV']=np.NaN
                for stage in self.stage_stats_labels:
                    cyc_valid_dur_stats[f'{cycle_label}_{stage}_valid_min']=np.NaN
                    cyc_ss_stats[f'{cycle_label}_{stage}_spindle_count']=np.NaN
                    cyc_ss_stats[f'{cycle_label}_{stage}_density']=np.NaN
                    cyc_ss_stats[f'{cycle_label}_{stage}_spindle_sec']=np.NaN
                    cyc_ss_stats[f'{cycle_label}_{stage}_dom_freq_Hz']=np.NaN
                    cyc_ss_stats[f'{cycle_label}_{stage}_avg_freq_Hz']=np.NaN
                    cyc_ss_stats[f'{cycle_label}_{stage}_amp_pkpk_uV']=np.NaN
                    cyc_ss_stats[f'{cycle_label}_{stage}_amp_rms_uV']=np.NaN    

        # Organize data for the output
        return cyc_rec_dur_stats | cyc_valid_dur_stats | cyc_ss_stats
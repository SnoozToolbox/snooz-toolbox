"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    OxygenDesatDetector
    A Class to analyze the oxygen channel, detect oxygen desaturations and export oxygen saturation report.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.switch_backend('agg')  # turn off gui
import numpy as np
import os.path
import pandas as pd
import scipy.signal as scipysignal
from scipy.interpolate import interp1d

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

from CEAMSModules.EventTemporalLink import EventTemporalLink
from CEAMSModules.EventReader import manage_events
from CEAMSModules.PSACompilation import PSACompilation
from CEAMSModules.PSGReader.SignalModel import SignalModel
from CEAMSModules.PSGReader import commons
from CEAMSModules.SleepReport import SleepReport

from CEAMSModules.OxygenDesatDetector.OxygenDesatDetector_doc import write_doc_file
from CEAMSModules.OxygenDesatDetector.OxygenDesatDetector_doc import _get_doc

DEBUG = False

class OxygenDesatDetector(SciNode):
    """
    A Class to analyze the oxygen channel, detect oxygen desaturations and export oxygen saturation report.
    To copy the previous software, the oxygen saturation channel is downsampled to 1 Hz.

    Inputs:
        "artifact_group": String
            The group label of the invalid section annotation for the oxy chan analysis.
        "artifact_name": String
            The name label of the invalid section annotation for the oxy chan analysis.
        "arousal_group": String
            The group label of the arousal annotations for temporal link analysis.
            (Obsolete, the feature was removed 2024-01-30, not robust)
        "arousal_name": String
            The name label of the arousal annotations for temporal link analysis.
            (Obsolete, the feature was removed 2024-01-30, not robust)
        "signals": a list of SignalModel
            Each item of the list is a SignalModel object as described below:
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the sampling rate of the signal
                signal.channel : current channel label
                signal.start_time : The start time of the signal in sec
                signal.end_time : The end time of the signal in sec
                (for more info : look into common/SignalModel)
        "events": pandas DataFrame
            df of events with field
            'group': Group of events this event is part of (String)
            'name': Name of the event (String)
            'start_sec': Starting time of the event in sec (Float)
            'duration_sec': Duration of the event in sec (Float)
            'channels' : Channel where the event occures (String)
            (within Snooz channels is a string of a single channel or [] for all channels)
        "stages_cycles": Pandas Dataframe ['group','name','start_sec','duration_sec','channels']
            Events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
            The sleep stage group has to be commons.sleep_stage_group "stage" and 
            the sleep cycle group has to be commons.sleep_cycle_group "cycle".            
        "subject_info": dict
            filename : Recording filename without path and extension.
            id1 : Identification 1
            id2 : Identification 2
            first_name : first name of the subject recorded
            last_name : last name of the subject recorded
            sex :
            ...
        "parameters_oxy": dict
            'desaturation_drop_percent' : 'Drop level (%) for the oxygen desaturation "3 or 4"',
            'max_slope_drop_sec' : 'The maximum duration (s) during which the oxygen level is dropping "120 or 20"',
            'min_hold_drop_sec' : 'Minimum duration (s) during which the oxygen level drop is maintained "10 or 5"',

        "parameters_cycle": Dict
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
        "report_constants": dict
            Constants used in the report (N_HOURS, N_CYCLES)  
        "cohort_filename": String
            Path and filename to save the oxygen saturation report for the cohort. 
        "picture_dir" : String
            Directory path to save the oxygen saturation graph picture.
            One graph per recording (1 picture per discontinuity).

    Outputs:
        desat_events : pandas DataFrame
            df of events with field
            'group': Group of events this event is part of (String)
            'name': Name of the event (String)
            'start_sec': Starting time of the event in sec (Float)
            'duration_sec': Duration of the event in sec (Float)
            'channels' : Channel where the event occures (String)
            (within Snooz channels is a string of a single channel or [] for all channels)
        
    """
    def __init__(self, **kwargs):
        """ Initialize module OxygenDesatDetector """
        super().__init__(**kwargs)
        if DEBUG: print('OxygenDesatDetector.__init__')

        # Input plugs
        InputPlug('artifact_group',self)
        InputPlug('artifact_name',self)
        InputPlug('arousal_group',self)
        InputPlug('arousal_name',self)
        InputPlug('signals',self)
        InputPlug('events',self)
        InputPlug('stages_cycles',self)
        InputPlug('subject_info',self)
        InputPlug('parameters_oxy',self)
        InputPlug('parameters_cycle',self)
        InputPlug('report_constants',self)
        InputPlug('cohort_filename',self)
        InputPlug('picture_dir',self)
        
        # Output plugs
        OutputPlug('desat_events',self)

        # A master module allows the process to be reexcuted multiple time.
        self._is_master = False 

        # Init module variables
        self.stage_stats_labels =   ['N1',   'N2',   'N3',   'R',    'W',    'NREM',             'N2N3',         'SLEEP']
        self.stage_stats_list =     [['N1'], ['N2'], ['N3'], ['R'], ['W'],   ['N1', 'N2', 'N3'], ['N2', 'N3'], ['N1', 'N2', 'N3', 'R', 'W']]
        self.values_below = [96, 94, 92, 90, 88, 85, 80, 75, 70, 60]
    

    def compute(self, artifact_group, artifact_name, arousal_group, arousal_name, \
        signals, events, stages_cycles, subject_info, parameters_oxy, parameters_cycle,\
             report_constants, cohort_filename, picture_dir):
        """
        To analyze the oxygen channel, detect oxygen desaturations and export oxygen saturation report.

        Inputs:
            "artifact_group": String
                The group label of the invalid section annotation for the oxy chan analysis.
            "artifact_name": String
                The name label of the invalid section annotation for the oxy chan analysis.
            "arousal_group": String
                The group label of the arousal annotations for temporal link analysis.
            "arousal_name": String
                The name label of the arousal annotations for temporal link analysis.
            "signals": a list of SignalModel
                Each item of the list is a SignalModel object as described below:
                    signal.samples : The actual signal data as numpy list
                    signal.sample_rate : the sampling rate of the signal
                    signal.channel : current channel label
                    signal.start_time : The start time of the signal in sec
                    signal.end_time : The end time of the signal in sec
                    (for more info : look into common/SignalModel)
            "events": pandas DataFrame
                df of events with field
                'group': Group of events this event is part of (String)
                'name': Name of the event (String)
                'start_sec': Starting time of the event in sec (Float)
                'duration_sec': Duration of the event in sec (Float)
                'channels' : Channel where the event occures (String)
                (within Snooz channels is a string of a single channel or [] for all channels)
            "stages_cycles": Pandas Dataframe ['group','name','start_sec','duration_sec','channels']
                Events defined as (columns=['group', 'name','start_sec','duration_sec','channels']) 
                The sleep stage group has to be commons.sleep_stage_group "stage" and 
                the sleep cycle group has to be commons.sleep_cycle_group "cycle".            
            "subject_info": dict
                filename : Recording filename without path and extension.
                id1 : Identification 1
                id2 : Identification 2
                first_name : first name of the subject recorded
                last_name : last name of the subject recorded
                sex :
                ...
            "parameters_oxy": dict
                'desaturation_drop_percent' : 'Drop level (%) for the oxygen desaturation "3 or 4"',
                'max_slope_drop_sec' : 'The maximum duration (s) during which the oxygen level is dropping "120 or 20"',
                'min_hold_drop_sec' : 'Minimum duration (s) during which the oxygen level drop is maintained "10 or 5"',
                'window_link_sec' : 'The window length (s) to compute the temporal link between desaturations and arousals',
                'arousal_min_sec' : 'The minimum length (s) of the arousal events kept',
                'arousal_max_sec' : 'The maximum length (s) of the arousal events kept',

            "parameters_cycle": Dict
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
            "report_constants": dict
                Constants used in the report (N_HOURS, N_CYCLES)  
            "cohort_filename": String
                Path and filename to save the oxygen saturation report for the cohort. 
            "picture_dir" : String
                Directory path to save the oxygen saturation graph picture.
                One graph per recording (1 picture per discontinuity).
        Outputs:

        """
        self.clear_cache()

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if subject_info=='':
            raise NodeInputException(self.identifier, "subject_info", \
                f"OxygenDesatDetector this input is empty, it needs to identify the subject recorded.")
        if cohort_filename=='':
            raise NodeInputException(self.identifier, "cohort_filename", \
                f"OxygenDesatDetector has nothing to generate, 'cohort_filename' is empty")    
        if isinstance(signals, str) and signals=='':
            raise NodeInputException(self.identifier, "signals", \
                f"OxygenDesatDetector this input is empty, no signals no Oxygen Saturation Report.")         
        if isinstance(stages_cycles, str) and stages_cycles=='':
            raise NodeInputException(self.identifier, "stages_cycles", \
                f"OxygenDesatDetector this input is empty")    
        if isinstance(parameters_cycle, str) and parameters_cycle=='':
            raise NodeInputException(self.identifier, "parameters_cycle", \
                f"OxygenDesatDetector this input is empty")  
        if isinstance(parameters_oxy, str) and parameters_oxy=='':
            raise NodeInputException(self.identifier, "parameters_oxy", \
                f"OxygenDesatDetector this input is empty")  
        if isinstance(events, str) and events=='':
            raise NodeInputException(self.identifier, "events", \
                f"OxygenDesatDetector this input is empty, events is not connected.")    

        # Convert string into dicts
        if isinstance(parameters_cycle, str):
            parameters_cycle = eval(parameters_cycle)
        if isinstance(parameters_oxy, str):
            parameters_oxy = eval(parameters_oxy)

        if isinstance(report_constants,str) and report_constants == '':
            raise NodeInputException(self.identifier, "report_constants", \
                "OxygenDesatDetector report_constants parameter must be set.")
        elif isinstance(report_constants,str):
            report_constants = eval(report_constants)
        if isinstance(report_constants,dict) == False:
            raise NodeInputException(self.identifier, "report_constants",\
                "OxygenDesatDetector report_constants expected type is dict and received type is " \
                    + str(type(report_constants)))   
        self.N_CYCLES = int(float(report_constants['N_CYCLES']))

        #------------------------------------------------------------------------------
        # Header parameters
        # subject info, sleep cycle parameters, desaturation parameters
        #------------------------------------------------------------------------------
        subject_info_params = \
        {
            "filename":subject_info['filename'],
            "id1": subject_info['id1']
            }
        cycle_info_param = SleepReport.get_sleep_cycle_parameters(self,parameters_cycle)

        # Extract cycle
        sleep_cycles_df = stages_cycles[stages_cycles['group']==commons.sleep_cycle_group]
        sleep_cycles_df.reset_index(inplace=True, drop=True)
        sleep_cycle_count = {}
        sleep_cycle_count['sleep_cycle_count']=len(sleep_cycles_df) # 'Number of sleep cycles.',

        desaturation_param = parameters_oxy
        # Select the invalid sections events (self is required for the self.identifier)
        invalid_section_param, invalid_events = \
            PSACompilation.get_artefact_info(self, artifact_group, artifact_name, events.copy())
        invalid_section_param['invalid_events'] = invalid_section_param.pop('artefact_group_name_list')

        # Extract sleep stages
        sleep_stage_df = stages_cycles[stages_cycles['group']==commons.sleep_stages_group]
        sleep_stage_df.reset_index(inplace=True, drop=True)

        # Keep stages from the first sleep stage (1-5) to the last sleep stage (1-5) to define the sleep period
        sleep_stage_df.loc[:, 'name'] = sleep_stage_df['name'].apply(int)
        index_sleep = sleep_stage_df[(sleep_stage_df['name']>=1) & (sleep_stage_df['name']<=5)].index
        stage_sleep_period_df = sleep_stage_df.loc[index_sleep[0]:index_sleep[-1]]
        stage_sleep_period_df.reset_index(inplace=True, drop=True)

        channels_list = np.unique(SignalModel.get_attribute(signals, 'channel', 'channel'))
        if len(channels_list)>1:
            raise NodeRuntimeException(self.identifier, "signals", \
                f"OxygenDesatDetector more than one channels were selected for {subject_info['filename']}.")
        
        #----------------------------------------------------------------------
        # Define the channel info
        #----------------------------------------------------------------------
        channel = channels_list[0]
        fs_chan = SignalModel.get_attribute(signals, 'sample_rate', 'channel', channel)[0][0] 
        channel_info_param = {}
        channel_info_param['chan_label']=channel
        channel_info_param['chan_fs']=fs_chan

        #----------------------------------------------------------------------
        # Oxygen channel saturation variables
        # Minimum, maximum and average oxygen saturation per thirds, halves, sleep cycles and sleep stages.
        #----------------------------------------------------------------------

        # Extract samples for the sleep period
        data_stats, data_starts = self.extract_signal_data_for_sleep_period(stage_sleep_period_df, signals)

        # Detect artifact 
        #   data_clean is the raw signal with short artifacts interpolated and long artifact forced to NaN
        artifact_events = []
        data_clean, artifact_det_lst, data_gradient = self.detect_artifact_SpO2(data_stats, data_starts, fs_chan)
        artifact_events += [('SpO2', 'art_SpO2', start_sec, duration_sec, '') # Add back channel
                         for start_sec, duration_sec in artifact_det_lst]
        # Convert artifact_events to dataframe
        artifact_events_df = manage_events.create_event_dataframe(data=artifact_events)
        # Add artifact events to invalid events
        invalid_events = pd.concat([invalid_events, artifact_events_df], ignore_index=True)

        # Compute stats for the sleep period
        #----------------------------------------------------------------------
        total_stats = self.compute_total_stats_saturation(\
            stage_sleep_period_df, data_clean, data_starts, \
                subject_info, fs_chan, picture_dir, invalid_events)

        # Compute stats for thirds
        #----------------------------------------------------------------------
        n_divisions = 3
        section_label = 'third'
        third_stats = self.compute_division_stats_saturation(\
            n_divisions, section_label, stage_sleep_period_df, data_clean, data_starts, fs_chan)

        # Compute stats for halves
        #----------------------------------------------------------------------
        n_divisions = 2
        section_label = 'half'
        half_stats = self.compute_division_stats_saturation(\
            n_divisions, section_label, stage_sleep_period_df, data_clean, data_starts, fs_chan)

        # Compute stats for stages
        #----------------------------------------------------------------------       
        stage_stats = self.compute_stages_stats_saturation(\
            stage_sleep_period_df, data_clean, data_starts, fs_chan)

        # Compute stats for cycles
        #----------------------------------------------------------------------       
        cycle_stats = self.compute_cycles_stats_saturation(\
            sleep_cycles_df,  data_clean, data_starts, fs_chan)

        # Detect desaturation 
        #----------------------------------------------------------------------
            # "parameters_oxy": dict
            # 'desaturation_drop_percent' : 'Drop level (%) for the oxygen desaturation "3 or 4"',
            # 'max_slope_drop_sec' : 'The maximum duration (s) during which the oxygen level is dropping "180 or 20"',
            # 'min_hold_drop_sec' : 'Minimum duration (s) during which the oxygen level drop is maintained "10 or 5"',
        desat_df, plateau_df, data_lpf_list, data_hpf_list, data_dev_list, lmax_indices_list, lmin_indices_list = \
            self.detect_desaturation_ABOSA(data_starts, data_clean, fs_chan, channel, parameters_oxy)
        
        # Detect recovery
        #----------------------------------------------------------------------
        recovery_df = self.detect_recovery_ABOSA(desat_df, data_starts, data_clean, data_dev_list, fs_chan, channel, parameters_oxy)

        desat_recovery_df = pd.concat([desat_df, recovery_df], ignore_index=True)

        # Save the list of desaturation events detected and their characteristics
        #----------------------------------------------------------------------
        if len(picture_dir)>0:
            file_events_name = os.path.join(picture_dir, f"{subject_info['filename']}_oxygen_saturation_events.tsv")
            pd.DataFrame.to_csv(desat_recovery_df, path_or_buf=file_events_name, sep='\t', index=False, encoding="utf_8")
            
        # Compute desaturation stats
        #----------------------------------------------------------------------
        desat_stats = self.compute_desat_stats(desat_df, total_stats, stage_sleep_period_df)
        recovery_stats = self.compute_recovery_stats(recovery_df, total_stats, stage_sleep_period_df)
        # TotalSev_integrated = Total Severity of desaturation and recovery events. Total event area (desaturation+recovery) is calculated by integrating from the start of desaturation to the end of recovery. 
        severity_integrated = {"total_severity": desat_recovery_df['area_percent_sec'].sum()/(total_stats['total_valid_min']*60)}

        # Remove desaturation features not included in the Snooz annotations
        # Keep ['group', 'name', 'start_sec', 'duration_sec', 'channels']
        desat_recovery_df = desat_recovery_df[['group', 'name', 'start_sec', 'duration_sec', 'channels']]

        # Add invalid sections to desaturation events
        desat_recovery_df = pd.concat([desat_recovery_df, invalid_events], ignore_index=True)

        if DEBUG:
            cache = {}
            if len(data_lpf_list)>1:
                # Find the longuest signal
                len_data = [len(data) for data in data_lpf_list]
                index_longuest = np.argmax(len_data)
                data_lpf_list = [data_lpf_list[index_longuest]]
            else:
                index_longuest = 0
            if len(data_lpf_list)>0:
                # Create a SignalModel for the raw data and the filtered data
                signal_raw = signals[index_longuest].clone(clone_samples=False)
                signal_lpf = signals[index_longuest].clone(clone_samples=False)
                signal_hpf = signals[index_longuest].clone(clone_samples=False)
                #signal_squared = signals[index_longuest].clone(clone_samples=False)
                signal_raw.samples = data_stats[index_longuest]
                signal_raw.start_time = data_starts[index_longuest]
                signal_lpf.samples = data_lpf_list[index_longuest]
                #signal_lpf.samples = data_gradient[index_longuest]
                signal_lpf.start_time = data_starts[index_longuest]
                signal_lpf.channel = signal_raw.channel+'_lpf'
                #signal_lpf.channel = signal_raw.channel+'_art'
                signal_hpf.samples = data_dev_list[index_longuest]
                signal_hpf.start_time = data_starts[index_longuest]
                signal_hpf.channel = signal_raw.channel+'_grad'
                cache['signal_raw'] = signal_raw
                cache['signal_lpf'] = signal_lpf
                cache['signal_hpf'] = signal_hpf

                cache['desat_df'] = desat_recovery_df
                cache['plateau_df'] = plateau_df
                cache['lmax_sec'] = lmax_indices_list[index_longuest]/fs_chan + data_starts[index_longuest]
                cache['lmin_sec'] = lmin_indices_list[index_longuest]/fs_chan + data_starts[index_longuest]
                self._cache_manager.write_mem_cache(self.identifier, cache)

        # Temporal links between desaturation and arousal
        # Removed 2024-01-30
        #   - Does not look robust
        #   - We dont know who asked for it
        #----------------------------------------------------------------------        
        # # Select arousals
        # arousal_section_param, arousal_events = \
        #     PSACompilation.get_artefact_info(self, arousal_group, arousal_name, events.copy())
        # # Select arousals between min and max duration
        # arousals_selected = arousal_events[arousal_events['duration_sec']>=parameters_oxy['arousal_min_sec']]
        # arousals_selected = arousals_selected[arousals_selected['duration_sec']<=parameters_oxy['arousal_max_sec']]

        # # Compute temporal links
        # temporal_stats, link_event_df = self.compute_temporal_link_stats(\
        #     desat_df, arousals_selected, parameters_oxy['window_link_sec'], channel)

        # --------------------------------------------------------------------------
        # Organize data to Write the file
        # --------------------------------------------------------------------------
        # Construction of the pandas dataframe that will be used to create the CSV file
        # There is a new line for each channel and mini band
        output = subject_info_params | cycle_info_param | desaturation_param | invalid_section_param | \
            channel_info_param | sleep_cycle_count | total_stats | third_stats | half_stats | \
                stage_stats | cycle_stats | desat_stats | recovery_stats | severity_integrated #| temporal_stats
        report_df = pd.DataFrame.from_records([output])

        # Write the current report for the current subject into the cohort tsv file
        write_header = not os.path.exists(cohort_filename)
        # Order columns as the doc file
        out_columns = list(_get_doc(self.N_CYCLES, self.stage_stats_labels, self.values_below).keys())
        # Re order the columns and make sure they all exist
        report_df = report_df[out_columns]
        try : 
            report_df.to_csv(path_or_buf=cohort_filename, sep='\t', \
                index=False, index_label='False', mode='a', header=write_header, encoding="utf_8")
        except :
            error_message = f"Snooz can not write in the file {cohort_filename}."+\
                f" Check if the drive is accessible and ensure the file is not already open."
            raise NodeRuntimeException(self.identifier, "OxygenDesatDetector", error_message)      

        # To write the info text file to describe the variable names
        if write_header:
            # Write the documentation file
            file_name, file_extension = os.path.splitext(cohort_filename)
            doc_filepath = file_name+"_info"+file_extension
            if not os.path.exists(doc_filepath):
                write_doc_file(doc_filepath, self.N_CYCLES, self.stage_stats_labels, self.values_below)
                # Log message for the Logs tab
                self._log_manager.log(self.identifier, f"The file {doc_filepath} has been created.")

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, f"{subject_info['filename']} has been append to {cohort_filename}")
        
        return {
            'desat_events' : desat_recovery_df
        }


    def _plot_oxygen_saturation(self, data_to_plot, fs_chan, fig_name, data_starts, invalid_events):

        figure, ax = plt.subplots()
        figure.set_size_inches(25, 5)
        ax.clear()
        ymin = np.nanmin(data_to_plot)
        new_fs = fs_chan
        data_2_plot_end = len(data_to_plot)/new_fs+data_starts
        time = np.arange(data_starts, data_2_plot_end, 1/new_fs)
        # the sampling rate can be non integer,
        # we have to make sure that the time vector has the same length as the data to plot
        min_lenght = min(len(time), len(data_to_plot))
        time = time[:min_lenght]
        data_to_plot = data_to_plot[:min_lenght]
        ax.plot(time, data_to_plot,'-k', linewidth=1)
        
        # Add invalid section
        invalid_start_time = invalid_events['start_sec'].to_numpy()
        invalid_duration = invalid_events['duration_sec'].to_numpy()
        invalid_end = invalid_start_time + invalid_duration
        for inval_start, inval_end in zip(invalid_start_time, invalid_end):
            # If the invalid section starts during the data_to_plot
            if (inval_start >= data_starts) and (inval_start < data_2_plot_end):
                cur_invalid_start = inval_start
            # If the invalid section starts before the data_to_plot
            elif inval_start < data_starts:
                cur_invalid_start = data_starts
            else:
                cur_invalid_start = None
            # If the invalid section ends during the data_2_plot
            if (inval_end > data_starts) and (inval_end <= data_2_plot_end):
                cur_invalid_end = inval_end
            elif inval_end > data_2_plot_end:
                cur_invalid_end = data_2_plot_end
            else:
                cur_invalid_end = None
            if (cur_invalid_start is not None) and (cur_invalid_end is not None):
                ax.broken_barh([(cur_invalid_start, cur_invalid_end-cur_invalid_start)], (ymin, 100-ymin), facecolors='tab:red')

        ax.set_xlim(data_starts,len(data_to_plot)/new_fs-data_starts)
        ax.set_ylim(ymin,100)
        xticks_hour = np.arange(int(np.floor(min(time)/3600)),int(np.ceil(max(time)/3600)), 0.5)
        ax.set_xticks(xticks_hour*3600)
        ax.set_xticklabels(xticks_hour)
        ax.set_xlabel("Time (h)")
        ax.set_ylabel("Saturation (%)")
        ax.set_title("Oxygen Saturation")
        ax.grid(visible=True, which='both', axis='both')

        if not '.' in fig_name:
            fig_name = fig_name + '.pdf'
        try: 
            figure.savefig(fig_name)
        except :
            raise NodeRuntimeException(self.identifier, "OxygenDesatDetector", \
                f"ERROR : Snooz can not save the picture {fig_name}. "+\
                f"Check if the drive is accessible and ensure the file is not already open.")                           

    def compute_division_stats_saturation(self, n_divisions, section_label, stage_sleep_period_df, data_clean, data_starts, fs):
        """""
            Compute the statistics (mean, std, max and min) of the oxygen saturation for the requested division.
            n_divisions can be 3 or 2.

            Parameters
            -----------
                n_divisions                 : int
                    Number of divisions.
                section_label               : string
                    Label of the division.
                stage_sleep_period_df                : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])  
                    List of sleep stages from lights off to lights on.
                signals                     : list of SignalModel
                    The list of SignalModel from the whole recording, will be truncated in this fonction.
            Returns
            -----------  
                stats_dict                  : dict
                    Keys are adapted to the division such as
                    stats_dict["third1_saturation_avg"]
                    stats_dict["half2_saturation_min"]

        """""
        # For dividing a number into (almost) equal whole numbers
        # Remainers are added in the first division first
            # 15 epochs divided by 3 => [5, 5, 5]
            # 14 epochs divided by 3 => [5, 5, 4]
            # 13 epochs divided by 3 => [5, 4, 4]
            # 12 epochs divided by 3 => [4, 4, 4]
        n_epochs = len(stage_sleep_period_df)
        n_epoch_div = [n_epochs // n_divisions + (1 if x < n_epochs % n_divisions else 0)  for x in range (n_divisions)]
        # Create a list of indexes to select the epochs in each division
        # Select the portion of the recording, row integer (NOT label), the end point is excluded with the .iloc
        index_div = []
        index_tmp = 0
        for div in range(n_divisions):
            cur_start = index_tmp
            cur_stop = cur_start+n_epoch_div[div]
            index_div.append([cur_start,cur_stop]) # integer index then last is exclusive
            index_tmp = cur_stop
        stats_dict = {}
        section_val = 1
        for index_start, index_stop in index_div:
            start = stage_sleep_period_df.iloc[index_start]['start_sec']
            end = stage_sleep_period_df.iloc[index_stop-1]['start_sec']+ stage_sleep_period_df.iloc[index_stop-1]['duration_sec']
            dur = end - start
            signals_third = []
            for samples, data_start in zip(data_clean, data_starts):
                # Because of the discontinuity
                # we have to verify if the signal includes at least partially the events
                # Look for the Right windows time
                if (data_start<(start+dur)) and ((data_start+len(samples)/fs)>start): 
                    # Extract samples for the current division
                    channel_cur_samples = self.extract_samples_from_array(samples, data_start, start, dur, fs)
                    signals_third.append(channel_cur_samples)

            # Flat signals into an array
            data_array = np.empty(0)
            for i_bout, samples in enumerate(signals_third):
                if len(data_array)==0:
                    data_array = samples
                else:
                    data_array = np.concatenate((data_array, samples), axis=0)

            # Clean-up invalid values
            #data_array = np.round(data_array,0) # to copy Gaetan
            data_array[data_array>100]=np.nan
            data_array[data_array<=0]=np.nan
            stats_dict[f"{section_label}{section_val}_saturation_avg"] = np.nanmean(data_array)
            stats_dict[f"{section_label}{section_val}_saturation_std"] = np.nanstd(data_array)
            # stats_dict[f"{section_label}{section_val}_saturation_min"] = np.round(np.nanmin(data_array),0)
            # stats_dict[f"{section_label}{section_val}_saturation_max"] = np.round(np.nanmax(data_array),0)     
            stats_dict[f"{section_label}{section_val}_saturation_min"] = np.nanmin(data_array)
            stats_dict[f"{section_label}{section_val}_saturation_max"] = np.nanmax(data_array)     
            section_val = section_val + 1
        return stats_dict


    def extract_samples_from_events(self, signal, start, dur):
        """
        Parameters :
            signal : SignalModel object
                signal with channel, samples, sample_rate...
            start : float
                start time in sec of the signal
            dur : float
                duration in sec of the signal
        Return : 
            samples :numpy array
                all samples linked to the event specified by start and dur

        """
        channel_cur = signal.clone(clone_samples=False)
        # Because of the discontinuity, the signal can start with an offset (second section)
        signal_start_samples = int(signal.start_time * channel_cur.sample_rate)
        channel_cur.start_time = start
        channel_cur.duration = dur
        channel_cur.end_time = start + dur
        first_sample = int(start * channel_cur.sample_rate)
        last_sample = int(channel_cur.end_time * channel_cur.sample_rate)
        channel_cur_samples = signal.samples[first_sample-signal_start_samples:last_sample-signal_start_samples]
        return channel_cur_samples
    

    def extract_signal_data_for_sleep_period(self, stage_sleep_period_df, signals):
        """
        Extract signal data and start times for the sleep period, handling discontinuities.

        Parameters :
            stage_sleep_period_df : pandas DataFrame
                Sleep stages from lights off to lights on.
            signals : list of SignalModel
                List of SignalModel objects from the whole recording.

        Return : 
            data_stats : list of numpy array
                Oxygen saturation values (cleaned: >100 or <=0 set to NaN) for each continuous section.
            data_starts : list of float
                Start time in sec of each continuous section (more than one when there are discontinuities).
        """
        start = stage_sleep_period_df['start_sec'].values[0]
        end = stage_sleep_period_df['start_sec'].values[-1] + stage_sleep_period_df['duration_sec'].values[-1]
        dur = end - start
        data_stats = []
        data_starts = []
        for signal in signals:
            # Because of the discontinuity
            # we have to verify if the signal includes at least partially the events
            # Look for the Right windows time
            if (signal.start_time < (start + dur)) and ((signal.start_time + signal.duration) > start):
                cur_start = signal.start_time if start <= signal.start_time else start
                cur_end = end if end <= signal.end_time else signal.end_time
                # Extract and define the new extracted channel_cur
                channel_cur = self.extract_samples_from_events(signal, cur_start, cur_end - cur_start)
                # Clean-up invalid values
                # channel_cur[channel_cur > 100] = np.nan
                # channel_cur[channel_cur <= 0] = np.nan
                data_starts.append(cur_start)
                data_stats.append(channel_cur)
        return data_stats, data_starts


    def extract_samples_from_array(self, samples, data_start, start, dur, fs):
        """
        Extract samples from a numpy array for a given time window.

        Parameters :
            samples : numpy array
                Signal samples.
            data_start : float
                Start time in sec of the signal array.
            start : float
                Start time in sec of the window to extract.
            dur : float
                Duration in sec of the window to extract.
            fs : float
                Sampling rate in Hz.

        Return : 
            extracted_samples : numpy array
                Samples within the specified time window.
        """
        signal_start_samples = int(data_start * fs)
        end_time = start + dur
        first_sample = int(start * fs)
        last_sample = int(end_time * fs)
        # Add verification to avoid negative indexing
        if first_sample - signal_start_samples < 0:
            first_sample = signal_start_samples
        # Add verification to avoid exceeding array length
        if last_sample - signal_start_samples > len(samples):
            last_sample = len(samples) + signal_start_samples
        extracted_samples = samples[first_sample - signal_start_samples:last_sample - signal_start_samples]
        return extracted_samples


    def compute_total_stats_saturation(self, stage_sleep_period_df, data_clean, data_starts, subject_info, fs_chan, picture_dir, invalid_events):
        """
        Parameters :
            stage_sleep_period_df : pandas DataFrame
                Sleep stages from lights off to lights on.
            signal : SignalModel object
                signal with channel, samples, sample_rate...
            subject_info : dict
                filename : Recording filename without path and extension.
                id1 : Identification 1
                ...
            fs_chan : float
                sampling rate of the channel
            picture_dir : string
                path of the folder to save the saturation picture (can be empty)
            invalid_events : pandas DataFrame
                Events of the invalid section of the oxygen saturation.
        Return : 
            total_stats : dict
                statistics fot the total recording.
                saturation_avg, std, min and max.
            data_stats : numpy array
                oxygen saturation integer values from 1 to 100% 
            data_starts : list
                start in sec of each continuous section (more than one when there are discontinuities)
        """    
        # Compute duration of sleep period for stats
        sleep_period_start_sec = stage_sleep_period_df['start_sec'].values[0]
        sleep_period_end_sec = stage_sleep_period_df['start_sec'].values[-1] + stage_sleep_period_df['duration_sec'].values[-1]
        sleep_period_dur_sec = sleep_period_end_sec - sleep_period_start_sec

        # Generate and save the oxygen saturation graph
        if len(picture_dir)>0:
            for i_bout, samples in enumerate(data_clean):
                fig_name = os.path.join(picture_dir, f"{subject_info['filename']}_oxygen_saturation_graph{i_bout}.pdf")
                self._plot_oxygen_saturation(samples, fs_chan, fig_name, data_starts[i_bout], invalid_events)

        # Flat signals into an array (discontinuity handling)
        data_array = np.empty(0)
        for i_bout, samples in enumerate(data_clean):
            if data_array.size == 0:
                data_array = samples
            else:
                data_array = np.concatenate((data_array, samples), axis=0)

        total_stats = {}
        total_stats["sleep_period_min"] = sleep_period_dur_sec/60
        total_stats["total_valid_min"] = (len(data_array)-np.isnan(data_array).sum())/fs_chan/60
        total_stats["total_invalid_min"]  = np.isnan(data_array).sum()/fs_chan/60
        total_stats["total_saturation_avg"] = np.nanmean(data_array)
        total_stats["total_saturation_std"] = np.nanstd(data_array)
        total_stats["total_saturation_min"] = np.nanmin(data_array)
        total_stats["total_saturation_max"] = np.nanmax(data_array)
        for val in self.values_below:
            total_stats[f"total_below_{val}_percent"] = ((data_array<val).sum()/fs_chan)/(total_stats["total_valid_min"]*60)*100
        return total_stats


    def compute_stages_stats_saturation(self, stage_sleep_period_df, data_clean, data_starts, fs_chan):
        """
        Parameters :
            stage_sleep_period_df : pandas DataFrame
                Sleep stages from lights off to lights on.
            data_clean : list of numpy arrays   
                signal with channel, samples, sample_rate...
            data_starts : list
                start in sec of each continuous section (more than one when there are discontinuities)
            fs_chan : float
                sampling rate of the channel
        Return : 
            stage_dict : dict
                statistics fot the stages.
                Saturation_avg, std, min and max for each stage.
                Duration in min for saturation under different thresholds.
        """    
        stage_start_times = stage_sleep_period_df['start_sec'].to_numpy().astype(float)
        stage_duration_times = stage_sleep_period_df['duration_sec'].to_numpy().astype(float)
        stage_name = stage_sleep_period_df['name'].apply(str).to_numpy()

        stage_dict = {}
        for stage_label, stage_list in zip(self.stage_stats_labels, self.stage_stats_list):
            stage_mask = np.zeros(stage_name.shape, dtype=bool)
            for stage_code in stage_list:
                stage_mask = stage_mask | (stage_name == commons.sleep_stages_name[stage_code])

            if not np.any(stage_mask):
                stage_dict[f'{stage_label}_saturation_avg'] = np.nan
                stage_dict[f'{stage_label}_saturation_std'] = np.nan
                stage_dict[f'{stage_label}_saturation_min'] = np.nan
                stage_dict[f'{stage_label}_saturation_max'] = np.nan
                for val in self.values_below:
                    stage_dict[f"{stage_label}_below_{val}_percent"] = np.nan
                continue

            start_masked = stage_start_times[stage_mask]
            dur_masked = stage_duration_times[stage_mask]

            # Incremental accumulation avoids building large temporary arrays.
            valid_count = 0
            sum_values = 0.0
            sum_squares = 0.0
            min_value = np.inf
            max_value = -np.inf
            below_counts = {val: 0 for val in self.values_below}

            for start, dur in zip(start_masked, dur_masked):
                end = start + dur
                expected_samples = int(round(dur * fs_chan, 0))

                epoch_segments = []
                for samples, start_signal in zip(data_clean, data_starts):
                    end_signal = start_signal + len(samples) / fs_chan
                    if (start_signal < end) and (end_signal > start):
                        epoch_segments.append(
                            self.extract_samples_from_array(samples, start_signal, start, dur, fs_chan)
                        )

                if len(epoch_segments) == 0:
                    epoch_samples = np.empty(0)
                elif len(epoch_segments) == 1:
                    epoch_samples = epoch_segments[0]
                else:
                    epoch_samples = np.concatenate(epoch_segments, axis=0)

                # Keep the old behavior: pad missing samples with NaN for incomplete epochs.
                if expected_samples > len(epoch_samples):
                    epoch_samples = np.pad(
                        epoch_samples,
                        (0, expected_samples - len(epoch_samples)),
                        constant_values=(0, np.nan)
                    )

                valid_mask = ~np.isnan(epoch_samples)
                if not np.any(valid_mask):
                    continue

                valid_samples = epoch_samples[valid_mask]
                valid_count += valid_samples.size
                sum_values += np.sum(valid_samples)
                sum_squares += np.sum(valid_samples * valid_samples)
                min_value = min(min_value, np.min(valid_samples))
                max_value = max(max_value, np.max(valid_samples))
                for val in self.values_below:
                    below_counts[val] += np.sum(valid_samples < val)

            if valid_count == 0:
                stage_dict[f'{stage_label}_saturation_avg'] = np.nan
                stage_dict[f'{stage_label}_saturation_std'] = np.nan
                stage_dict[f'{stage_label}_saturation_min'] = np.nan
                stage_dict[f'{stage_label}_saturation_max'] = np.nan
                for val in self.values_below:
                    stage_dict[f"{stage_label}_below_{val}_percent"] = np.nan
                continue

            mean_value = sum_values / valid_count
            variance_value = (sum_squares / valid_count) - (mean_value * mean_value)
            variance_value = max(0.0, variance_value)

            stage_dict[f'{stage_label}_saturation_avg'] = mean_value
            stage_dict[f'{stage_label}_saturation_std'] = np.sqrt(variance_value)
            stage_dict[f'{stage_label}_saturation_min'] = min_value
            stage_dict[f'{stage_label}_saturation_max'] = max_value
            for val in self.values_below:
                stage_dict[f"{stage_label}_below_{val}_percent"] = (below_counts[val] / valid_count) * 100

        return stage_dict


    def compute_cycles_stats_saturation(self, sleep_cycles_df, data_clean, data_starts, fs_chan):
        """
        Parameters :
            sleep_cycles_df : pandas DataFrame
                Sleep cycles 
            signal : SignalModel object
                signal with channel, samples, sample_rate...
        Return : 
            cyc_dict : dict
                statistics fot the cycles.
                Saturation_avg, std, min and max for each stage.
        """    
        cyc_dict = {}
        for i_cyc in range(self.N_CYCLES):
            # Extract samples for each cycle
            if len(sleep_cycles_df)>i_cyc:
                start = sleep_cycles_df.iloc[i_cyc]['start_sec']
                end = sleep_cycles_df.iloc[i_cyc]['start_sec']+sleep_cycles_df.iloc[i_cyc]['duration_sec']
                dur = end - start
                signals_cyc = []
                for samples, data_start in zip(data_clean, data_starts):
                    # Because of the discontinuity
                    # we have to verify if the signal includes at least partially the events
                    # Look for the Right windows time
                    if (data_start<(start+dur)) and ((data_start+len(samples)/fs_chan)>start): 
                        # Extract and define the new extracted channel_cur
                        channel_cur = self.extract_samples_from_array(samples, data_start, start, dur, fs_chan)
                        signals_cyc.append(channel_cur)
                
                # Flat signals into an array
                data_stats = np.empty(0)
                for i_bout, samples in enumerate(signals_cyc):
                    if data_stats.size == 0:
                        data_stats = samples
                    else:
                        data_stats = np.concatenate((data_stats, samples), axis=0)

                #data_stats = np.round(data_stats,0) # to copy Gaétan   
                # Clean-up invalid values
                # data_stats[data_stats>100]=np.nan
                # data_stats[data_stats<=0]=np.nan        
                cyc_dict[f'cyc{i_cyc+1}_saturation_avg'] = np.nanmean(data_stats)
                cyc_dict[f'cyc{i_cyc+1}_saturation_std'] = np.nanstd(data_stats)
                cyc_dict[f'cyc{i_cyc+1}_saturation_min'] = np.nanmin(data_stats)
                cyc_dict[f'cyc{i_cyc+1}_saturation_max'] = np.nanmax(data_stats)
            else:
                cyc_dict[f'cyc{i_cyc+1}_saturation_avg'] = np.nan
                cyc_dict[f'cyc{i_cyc+1}_saturation_std'] = np.nan
                cyc_dict[f'cyc{i_cyc+1}_saturation_min'] = np.nan
                cyc_dict[f'cyc{i_cyc+1}_saturation_max'] = np.nan
        return cyc_dict


    def convert_sec_to_HHMMSS(self, time_sec):
        HH = (np.floor(time_sec/3600)).astype(int)
        MM = ( np.floor( (time_sec-HH*3600) / 60 )).astype(int)
        SS = np.around( (time_sec-HH*3600 - MM*60).astype(np.double),decimals=2,out=None)
        # return the time as HH:MM:SS
        return f"{HH}:{MM}:{SS}"

    def compute_desaturation_area(self, signal, data_start, start_sec, duration_sec, fs_chan):
        """
        Compute the area of a desaturation event.
        
        The area is calculated as the integral of the drop below the baseline (starting SpO2 value)
        over the duration of the event. The result is in %-seconds.
        
        Parameters:
            signal : numpy array
                SpO2 signal samples.
            data_start : float
                Start time in seconds of the signal array.
            start_sec : float
                Start time in seconds of the desaturation event.
            duration_sec : float
                Duration in seconds of the desaturation event.
            fs_chan : float
                Sampling frequency in Hz.
        
        Returns:
            area : float
                Area of the desaturation event in %-seconds.
        """
        # Extract samples for the desaturation event
        event_samples = self.extract_samples_from_array(signal, data_start, start_sec, duration_sec, fs_chan)
        
        if len(event_samples) == 0 or np.all(np.isnan(event_samples)):
            return np.nan
        
        # Baseline is the first valid sample (start of desaturation = max SpO2 before drop)
        baseline = event_samples[0] if not np.isnan(event_samples[0]) else np.nanmax(event_samples)
        
        # Compute the drop below baseline for each sample
        drop_below_baseline = baseline - event_samples
        drop_below_baseline = np.clip(drop_below_baseline, 0, None)  # Only count positive drops
        
        # Compute the area using trapezoidal integration
        # Each sample represents 1/fs_chan seconds
        dt = 1.0 / fs_chan
        area = np.nansum(drop_below_baseline) * dt
        
        return area


    def compute_recovery_area(self, signal, data_start, start_sec, duration_sec, fs_chan):
        """
        Compute the area of a recovery event.

        The area is calculated as the integral of the rise above the baseline
        (recovery start value) over the duration of the event. The result is in
        %-seconds.

        Parameters:
            signal : numpy array
                SpO2 signal samples.
            data_start : float
                Start time in seconds of the signal array.
            start_sec : float
                Start time in seconds of the recovery event.
            duration_sec : float
                Duration in seconds of the recovery event.
            fs_chan : float
                Sampling frequency in Hz.

        Returns:
            area : float
                Area of the recovery event in %-seconds.
        """
        # Extract samples for the recovery event
        event_samples = self.extract_samples_from_array(signal, data_start, start_sec, duration_sec, fs_chan)

        if len(event_samples) == 0 or np.all(np.isnan(event_samples)):
            return np.nan

        # Baseline is the last valid sample at recovery start
        baseline = event_samples[-1] if not np.isnan(event_samples[-1]) else np.nanmax(event_samples)

        # Compute drop below baseline for each sample
        drop_below_baseline = baseline - event_samples
        drop_below_baseline = np.clip(drop_below_baseline, 0, None)  # Only count positive drops

        # Compute area using sample duration
        dt = 1.0 / fs_chan
        area = np.nansum(drop_below_baseline) * dt

        return area


    def resolve_overlapping_desaturations(self, desat_events):
        """
        Resolve overlapping desaturation events by keeping the one with the steepest fall rate.
        
        Parameters:
            desat_events : list of tuples
                List of (start_sec, duration_sec, fall_rate) tuples.
        
        Returns:
            resolved_events : list of tuples
                List of non-overlapping (start_sec, duration_sec, fall_rate) tuples.
        """
        if len(desat_events) == 0:
            return desat_events
        
        # Sort events by start time
        sorted_events = sorted(desat_events, key=lambda x: x[0])
        
        resolved_events = []
        i = 0
        while i < len(sorted_events):
            current_start, current_dur, current_rate, current_drop = sorted_events[i]
            current_end = current_start + current_dur
            
            # Find all overlapping events
            overlapping = [(i, current_start, current_dur, current_rate, current_drop)]
            j = i + 1
            while j < len(sorted_events):
                next_start, next_dur, next_rate, next_drop = sorted_events[j]
                next_end = next_start + next_dur
                
                # Check for overlap: events overlap if next starts before current ends
                if next_start < current_end:
                    overlapping.append((j, next_start, next_dur, next_rate, next_drop))
                    # Update current_end to include the new event's range
                    current_end = max(current_end, next_end)
                    j += 1
                else:
                    break
            
            # Select the event with the steepest fall rate (most negative, closest to -4)
            best_event = min(overlapping, key=lambda x: x[3])  # x[3] is fall_rate
            resolved_events.append((best_event[1], best_event[2], best_event[3], best_event[4]))
            
            if DEBUG and len(overlapping) > 1:
                print(f"Resolved {len(overlapping)} overlapping desaturations:")
                for idx, start, dur, rate, drop in overlapping:
                    marker = " <-- KEPT" if (start, dur, rate, drop) == (best_event[1], best_event[2], best_event[3], best_event[4]) else ""
                    print(f"  start={start:.2f}s, duration={dur:.2f}s, fall_rate={rate:.3f}%/s{marker}, drop={drop:.3f}%")
            
            # Move to the next non-overlapping event
            i = overlapping[-1][0] + 1
        
        return resolved_events


    def resolve_overlapping_recoveries(self, recovery_events):
        """
        Resolve overlapping recovery events by keeping the one with the highest
        positive recovery slope.

        Parameters:
            recovery_events : list of tuples
                List of (start_sec, duration_sec, slope, rise) tuples.

        Returns:
            resolved_events : list of tuples
                List of non-overlapping (start_sec, duration_sec, slope, rise) tuples.
        """
        if len(recovery_events) == 0:
            return recovery_events

        # Sort events by start time
        sorted_events = sorted(recovery_events, key=lambda x: x[0])

        resolved_events = []
        i = 0
        while i < len(sorted_events):
            current_start, current_dur, current_slope, current_rise = sorted_events[i]
            current_end = current_start + current_dur

            # Find all overlapping events
            overlapping = [(i, current_start, current_dur, current_slope, current_rise)]
            j = i + 1
            while j < len(sorted_events):
                next_start, next_dur, next_slope, next_rise = sorted_events[j]
                next_end = next_start + next_dur

                # Check for overlap: events overlap if next starts before current ends
                if next_start < current_end:
                    overlapping.append((j, next_start, next_dur, next_slope, next_rise))
                    current_end = max(current_end, next_end)
                    j += 1
                else:
                    break

            # Select event with highest positive slope
            best_event = max(overlapping, key=lambda x: x[3])  # x[3] is slope
            resolved_events.append((best_event[1], best_event[2], best_event[3], best_event[4]))

            if DEBUG and len(overlapping) > 1:
                print(f"Resolved {len(overlapping)} overlapping recoveries:")
                for idx, start, dur, slope, rise in overlapping:
                    marker = " <-- KEPT" if (start, dur, slope, rise) == (best_event[1], best_event[2], best_event[3], best_event[4]) else ""
                    print(f"  start={start:.2f}s, duration={dur:.2f}s, rise={rise:.3f}%, slope={slope:.3f}%/s{marker}")

            # Move to the next non-overlapping event
            i = overlapping[-1][0] + 1

        return resolved_events

    def detect_desaturation_ABOSA(self, data_starts, data_stats, fs_chan, channel, parameters_oxy):
        """
        Detect desaturation as described in ABOSA [1].

        Parameters :
            data_stats : list of numpy array
                oxygen saturation integer values from 1 to 100% (cleaned)
            data_starts : list
                start in sec of each continuous section (more than one when there are discontinuities)
            fs_chan     : float
                Sampling frequency (Hz).
            channel     : string
                Channel label.
            parameters_oxy: dict
                'desaturation_drop_percent' : 'Drop level (%) for the oxygen desaturation "3 or 4"',
                'max_slope_drop_sec' : 'The maximum duration (s) during which the oxygen level is dropping "120 or 20"',
                'min_hold_drop_sec' : 'Minimum duration (s) during which the oxygen level drop is maintained "10 or 5"',
            asleep_stages_df : pandas DataFrame
                Asleep stages from lights off to lights on.

        Return : 
            desat_df : pandas DataFrame
                df of events with field
                'group': Group of events this event is part of (String)
                'name': Name of the event (String)
                'start_sec': Starting time of the event in sec (Float)
                'duration_sec': Duration of the event in sec (Float)
                'channels' : Channel where the event occures (String)
            signal_lpf_list : list of numpy array
                low pass filtered oxygen saturation signals (the trend) for debug purpose.
            

        Reference : 
            [1] Karhu, T., Leppänen, T., Töyräs, J., Oksenberg, A., Myllymaa, S., & Nikkonen, S. (2022).
            ABOSA - Freely available automatic blood oxygen saturation signal analysis software: 
            Structure and validation. Computer Methods and Programs in Biomedicine, 226, 107120. 
            https://doi.org/10.1016/j.cmpb.2022.107120
        """   
        data_lpf_list = []
        data_hpf_list = []
        data_dev_list = []
        all_desat_events = []
        plateau_lst = []
        lmin_indices_list = []
        lmax_indices_list = []        

        #---------------------
        # ABOSA parameters
        #---------------------
        # Avg fall rate limits to consider for the whole desaturation event
        # The deeptest slope
        desat_event_slope_steep_limit = -4.0  # % per second
        # The least steep
        desat_event_slope_shallow_limit = -0.05  # % per second
        # peak detection parameters
        min_peak_distance_sec = 5 
        min_peak_prominence = 1
        # Filter order for lowpass (finding peaks) and highpass (fall rate) filtering
        order = 4 # ABOSA
        frequency_cutoff = 0.1 #same as the paper
        # Adjust Lmax and all Lmin candidates for plateau on the filtered signal
        min_plateau_duration_sec = 20  # Strategy different than ABOSA
        # Steepest accepted slope during 1 sec 
        desat_event_slope_steepest_1sec = -6.0  # % per second

        for i, signal in enumerate(data_stats):
            valid_mask = ~np.isnan(signal)
            if not np.any(valid_mask):
                continue

            # Low pass filter the signal to get the trend in order to detect local min and max
            signal_lpf = self.filter_nan_filtfilt(signal, order, fs_chan, frequency_cutoff, 'low')

            # Plateau detection
            signal_rounded = np.round(signal_lpf, 0)
            signal_derivative = np.gradient(signal_rounded) * fs_chan

            # High-pass filter the signal at 0.1 Hz (which is already low-pass filtered to 0.1 Hz)
            signal_hpf = self.filter_nan_filtfilt(signal_lpf, order, fs_chan, frequency_cutoff , 'high')

            # Step 1: Locate potential endpoints (Lmin)
            min_peak_distance_samples = int(min_peak_distance_sec * fs_chan)
            lmin_indices = self.detect_local_min(
                signal, signal_lpf, fs_chan, 
                min_peak_distance_samples, min_peak_prominence, 
                data_starts[i]
            )
            lmin_indices_list.append(lmin_indices)

            # Step 2: Locate potential starting points (Lmax)
            # lmax_indices (numpy array) : Indices of local maximums filtered for too low maximums.
            # lmax_indices_org (numpy array) : Indices of local maximums in the original signal.
            lmax_indices, lmax_indices_org = self.detect_local_max(
                signal, signal_lpf, fs_chan, 
                min_peak_distance_samples, min_peak_prominence, 
                data_starts[i]
            )
            lmax_indices_list.append(lmax_indices_org)

            # Step 3: Validate and match Lmax-Lmin pairs
            for lmax_idx in lmax_indices:
                lmax_time = data_starts[i] + lmax_idx / fs_chan
                lmax_val = signal[lmax_idx]
                
                # discard lmax without lmin
                #   The maximum duration of a desaturation event is limited to 180 s.
                #   The potential Lmax-Lmin pair cannot go through another Lmax.
                lmin_list = self.discard_lmax_without_lmin(
                    signal, lmin_indices, lmax_indices, lmax_idx, lmax_time, lmax_val,
                    data_starts[i], fs_chan, 
                    parameters_oxy['max_slope_drop_sec'], 
                    parameters_oxy['desaturation_drop_percent']
                )
                if lmin_list is None:
                    continue
                if DEBUG and len(lmin_list) > 1:
                    print(f"{len(lmin_list)} Lmins for current Lmax at {lmax_time:.2f}s")
                
                # Process all Lmin candidates through adjustments and validation
                for lmin_idx, lmin_time, lmin_val, drop in lmin_list:

                    # Adjust Lmax for fall rate
                    # The Lmax is shifted forward to a point where the fall starts using the low pass filtered signal.
                    # The high pass filtered signal is used to verify abrupt transition
                    adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, signal_squared = \
                        self.adjust_lmax_for_fall_rate(signal_lpf, signal_hpf, lmax_idx, lmin_idx, \
                                                       data_starts[i], fs_chan, desat_event_slope_shallow_limit)
                    
                    # Adjust Lmax and all Lmin candidates at least 20 s plateau
                    adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, \
                        adjusted_lmin_idx, adjusted_lmin_time, adjusted_lmin_val, plateau = \
                        self.adjust_for_rounded_plateau(
                            signal_rounded, signal_derivative, \
                            adjusted_lmax_idx, adjusted_lmax_val, 
                            lmin_idx, lmin_time, lmin_val,
                            data_starts[i], fs_chan, 
                            min_plateau_duration_sec
                        )
                    if len(plateau) > 0:
                        plateau_lst.extend(plateau)

                    if adjusted_lmax_time >= adjusted_lmin_time:
                        if DEBUG:
                            print(f"Lmax at {adjusted_lmax_time:.2f}s is after Lmin at {adjusted_lmin_time:.2f}s after plateau adjustment")
                        break

                    # Skip desaturation events that include artifacts
                    if any(np.isnan(signal[adjusted_lmax_idx:adjusted_lmin_idx + 1])):
                        if DEBUG:
                            print(f"Skipping desaturation event from {adjusted_lmax_time:.2f}s to {adjusted_lmin_time:.2f}s due to artifact (NaN values in signal)")
                        continue

                    # Adjust Lmax for fall rate
                    # The Lmax is shifted forward to a point where the fall starts using the low pass filtered signal.
                    # The high pass filtered signal is used to verify abrupt transition
                    adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, signal_squared = \
                        self.adjust_lmax_for_fall_rate(signal_lpf, signal_hpf, adjusted_lmax_idx, adjusted_lmin_idx, \
                                                       data_starts[i], fs_chan, desat_event_slope_shallow_limit)
                                        
                    # Correct Lmax locations by finding actual maximum within 5s window on raw signal
                    adjusted_lmax_idx = self.correct_single_peak_index_in_window(
                        signal, adjusted_lmax_idx, window_s=5, fs_chan=fs_chan, find_max=True)
                    adjusted_lmax_time = data_starts[i] + adjusted_lmax_idx / fs_chan
                    adjusted_lmax_val = signal[adjusted_lmax_idx]

                    # Correct Lmin locations by finding actual minimum within 5s window on raw signal
                    adjusted_lmin_idx = self.correct_single_peak_index_in_window(
                        signal, adjusted_lmin_idx, window_s=5, fs_chan=fs_chan, find_max=False)
                    adjusted_lmin_time = data_starts[i] + adjusted_lmin_idx / fs_chan
                    adjusted_lmin_val = signal[adjusted_lmin_idx]

                    # Recalculate drop after adjustments
                    drop = adjusted_lmax_val - adjusted_lmin_val
                    duration = adjusted_lmin_time - adjusted_lmax_time
                    
                    # Calculate average fall rate (%/s)
                    avg_fall_rate = -drop / duration if duration > 0 else 0

                    # Keep only events without disconnections during the desaturation event
                    # A disconnection is a drop with a slope steeper than desat_event_slope_steepest_1sec %/s for 1 second
                    # Use a sliding window of 1 sec (step of 0.5 sec) to detect steep slopes across the entire event
                    window_samples = int(fs_chan)        # 1 sec window
                    step_samples = max(1, int(0.5 * fs_chan))    # 0.5 sec step
                    end_idx = min(adjusted_lmin_idx, len(signal) - 1)
                    segment = signal[adjusted_lmax_idx:end_idx + 1]
                    if len(segment) > window_samples:
                        # Compute fall rate for all windows at once using vectorized indexing
                        win_starts = np.arange(0, len(segment) - window_samples, step_samples)
                        fall_rates = segment[win_starts] - segment[win_starts + window_samples]
                        has_steep_spike = bool(np.any(fall_rates <= desat_event_slope_steepest_1sec))
                    else:
                        has_steep_spike = False
                    
                    # Validate drop threshold, duration and fall rate limits
                    if ((drop >= parameters_oxy['desaturation_drop_percent']) and 
                        (duration >= parameters_oxy['min_hold_drop_sec']) and
                        (desat_event_slope_steep_limit <= avg_fall_rate <= desat_event_slope_shallow_limit) and
                        (not has_steep_spike)):  # No steep drop detected within any 1s window:
                        # Valid desaturation event with the avg_fall_rate to filter overlapping later
                        all_desat_events.append((adjusted_lmax_time, duration, avg_fall_rate, drop))
                    else:
                        if DEBUG:
                            print(f"  Invalid desaturation: start={adjusted_lmax_time:.2f}s, "
                                  f"duration={duration:.2f}s, drop={drop:.1f}%, "
                                  f"fall_rate={avg_fall_rate:.3f}%/s")

            # Debug output for the result view
            if DEBUG: 
                data_lpf_list.append(signal_lpf)
                data_hpf_list.append(signal_squared)
            data_dev_list.append(signal_derivative)

        # Resolve overlapping desaturations by keeping events with steepest fall rate
        all_desat_events = self.resolve_overlapping_desaturations(all_desat_events)

        # Compute the area under the desaturation events for further analysis
        desat_areas = []
        for start_sec, duration_sec, slope, depth in all_desat_events:
            # Find which signal segment contains this event
            area = np.nan
            for samples, data_start in zip(data_stats, data_starts):
                signal_end = data_start + len(samples) / fs_chan
                # Check if the event is within this signal segment
                if start_sec >= data_start and start_sec < signal_end:
                    area = self.compute_desaturation_area(samples, data_start, start_sec, duration_sec, fs_chan)
                    break
            desat_areas.append(area)

        # Create output dataframe
        # desat_events = [('SpO2', 'desat_SpO2', start_sec, duration_sec, channel) 
        #                 for start_sec, duration_sec in all_desat_events]
        desat_events = [('SpO2', 'desat_SpO2', start_sec, duration_sec, '', slope, depth)
                        for start_sec, duration_sec, slope, depth in all_desat_events]

        # plateau_events = [('SpO2', 'plateau_SpO2', start_sec, duration_sec, channel) 
        #                   for start_sec, duration_sec in plateau_lst]
        plateau_events = [('SpO2', 'plateau_SpO2', start_sec, duration_sec, '') 
                          for start_sec, duration_sec in plateau_lst]
        if DEBUG:
            print(f"\n{len(desat_events)} desat events\n")
            print(f"\n{len(plateau_events)} plateau events\n")
            for i in range(len(data_stats)):
                print(f"{len(lmax_indices_list[i])} possible max\n")
                print(f"{len(lmin_indices_list[i])} possible min\n")

        desat_df = pd.DataFrame(data=desat_events, columns=['group', 'name', 'start_sec', 'duration_sec', 'channels', 'slope', 'depth'])
        # Add the desaturation features to compute stats
        desat_df['area_percent_sec'] = desat_areas
        plateau_df = manage_events.create_event_dataframe(data=plateau_events)
  
        return desat_df, plateau_df, data_lpf_list, data_hpf_list, data_dev_list, lmax_indices_list, lmin_indices_list


    def detect_recovery_ABOSA(self, desat_df, data_starts, data_stats, data_dev_list, fs_chan, channel, parameters_oxy):
        """
        Detect recovery events following desaturation events as described in ABOSA.

        For each desaturation end time (Lmin), the recovery event starts at the Lmin
        and ends at the next local maximum (Lmax) found in the signal.

        Parameters:
            desat_df : pandas DataFrame
                Dataframe of desaturation events with at least 'start_sec' and
                'duration_sec' columns.
            data_starts : list
                Start time in seconds of each continuous signal section.
            data_stats : list of numpy array
                Cleaned oxygen saturation signal for each continuous section.
            fs_chan : float
                Sampling frequency (Hz).
            channel : string
                Channel label.
            parameters_oxy : dict
                'desaturation_drop_percent' : Drop level (%) for the oxygen desaturation.

        Returns:
            recovery_df : pandas DataFrame
                df of events with columns:
                'group': 'SpO2'
                'name': 'recovery_SpO2'
                'start_sec': Start time of the recovery (= desaturation end time).
                'duration_sec': Duration of the recovery in seconds.
                'channels': Channel label.
        """
        MIN_RECOVERY_DURATION_SEC = 3.0  # Minimum duration for a valid recovery event
        all_recovery_events = []

        # Parameters matching detect_desaturation_ABOSA
        min_peak_distance_sec = 5
        min_peak_prominence = 1
        order = 4
        frequency_cutoff = 0.1
        min_recovery_rise_percent = 2.0
        min_recovery_slope_percent_per_sec = 0.05

        for i, signal in enumerate(data_stats):
            if not np.any(~np.isnan(signal)):
                continue

            data_start = data_starts[i]
            signal_end = data_start + len(signal) / fs_chan
            data_derivative = data_dev_list[i]

            # Low-pass filter to detect local maxima (recovery endpoints)
            signal_lpf = self.filter_nan_filtfilt(signal, order, fs_chan, frequency_cutoff, 'low')
            # High-pass filter the signal at 0.1 Hz (which is already low-pass filtered to 0.1 Hz)
            signal_hpf = self.filter_nan_filtfilt(signal_lpf, order, fs_chan, frequency_cutoff, 'high')
            min_peak_distance_samples = int(min_peak_distance_sec * fs_chan)
            lmax_indices, _ = self.detect_local_max(
                signal, signal_lpf, fs_chan,
                min_peak_distance_samples, min_peak_prominence,
                data_start
            )

            # For each desaturation event, find the next local maximum (Lmax) after the desaturation end (Lmin) 
            # and validate the recovery based on rise and slope criteria.
            for desat_event_i, desat_event in desat_df.iterrows():
                desat_end_time = desat_event['start_sec'] + desat_event['duration_sec']
                desat_duration = desat_event['duration_sec']

                # Keep only desaturation ends that fall within this signal segment
                if desat_end_time < data_start or desat_end_time >= signal_end:
                    continue
                desat_end_idx = int((desat_end_time - data_start) * fs_chan)
                recovery_start_value = signal[desat_end_idx]
                if np.isnan(recovery_start_value): # artifact at the start of recovery - skip
                    continue
                # Select all Lmax candidates for the current recovery event (after the curent desaturation end)
                #   and before the next desaturation start if there is one
                next_lmax = lmax_indices[lmax_indices > desat_end_idx]
                next_desat = desat_df.iloc[desat_event_i + 1] if desat_event_i + 1 < len(desat_df) else None
                if next_desat is not None:
                    next_desat_end_idx = int((next_desat['start_sec'] - data_start) * fs_chan) if next_desat is not None else None
                    next_lmax = next_lmax[next_lmax <= next_desat_end_idx]
                if len(next_lmax) == 0:
                    break  # No Lmax remains in this segment for any later desaturation either

                # Allowed recovery duration: 120 s or 2x desaturation duration, 
                # the minimum of the two
                max_recovery_duration_sec = max(120.0, 2.0 * desat_duration)
                recovery_selected = False
                for recovery_lmax_idx in next_lmax:

                    # Move recovery end backward to the sample just after the last derivative change
                    # find the first derivative change points starting from the recovery_lmax_idx and going backward
                    derivative_change_points = np.where(np.diff(np.sign(data_derivative)) != 0)[0]
                    derivative_change_points = derivative_change_points[derivative_change_points <= recovery_lmax_idx]
                    if len(derivative_change_points) > 0:
                        rec_lmax_idx_shifted = derivative_change_points[-1] + 1
                    else:
                        rec_lmax_idx_shifted = recovery_lmax_idx  # No derivative change point found, the recovery end does not change

                    # Correct Lmax locations by finding actual maximum within 2s window
                    lmax_indice_real = self.correct_single_peak_index_in_window(
                        signal, rec_lmax_idx_shifted, window_s=2, fs_chan=fs_chan, find_max=True
                    )
                    if lmax_indice_real is not None:
                        rec_lmax_idx_shifted = lmax_indice_real

                    rec_lmax_time = data_start + rec_lmax_idx_shifted / fs_chan
                    rec_lmax_val = signal[rec_lmax_idx_shifted]
                    recovery_duration = rec_lmax_time - desat_end_time
                    if recovery_duration <= MIN_RECOVERY_DURATION_SEC:
                        if DEBUG:
                            desat_end_time_formatted = f"{int(desat_end_time // 3600):02d}:{int((desat_end_time % 3600) // 60):02d}:{int(desat_end_time % 60):02d}"
                            print(f"No valid recovery for {desat_end_time_formatted} because of short recovery duration ({recovery_duration:.2f}s)")
                        continue
                    # evaluate recovery duration
                    if recovery_duration > max_recovery_duration_sec:
                        if DEBUG:
                            desat_end_time_formatted = f"{int(desat_end_time // 3600):02d}:{int((desat_end_time % 3600) // 60):02d}:{int(desat_end_time % 60):02d}"
                            print(f"No valid recovery for {desat_end_time_formatted} because of long recovery duration ({recovery_duration:.2f}s)")
                        break

                    # Skip recovery candidates that contain artifacts.
                    if np.any(np.isnan(signal[desat_end_idx:rec_lmax_idx_shifted + 1])):
                        if DEBUG:
                            desat_end_time_formatted = f"{int(desat_end_time // 3600):02d}:{int((desat_end_time % 3600) // 60):02d}:{int(desat_end_time % 60):02d}"
                            print(f"No valid recovery for {desat_end_time_formatted} because of artifacts in the signal")
                        continue

                    # Evaluate recovery rise and slope
                    recovery_rise = rec_lmax_val - recovery_start_value
                    recovery_slope = recovery_rise / recovery_duration if recovery_duration > 0 else 0.0
                    if (recovery_rise >= min_recovery_rise_percent) and \
                       (recovery_slope >= min_recovery_slope_percent_per_sec):
                        all_recovery_events.append((desat_end_time, recovery_duration, recovery_slope, recovery_rise))
                        recovery_selected = True
                    else:
                        if DEBUG:
                            desat_end_time_formatted = f"{int(desat_end_time // 3600):02d}:{int((desat_end_time % 3600) // 60):02d}:{int(desat_end_time % 60):02d}"
                            print(f"No valid recovery for {desat_end_time_formatted} because of recovery_rise ({recovery_rise:.2f}%) or recovery_slope ({recovery_slope:.2f}%/s)")                
                        #break no break since we resolve overlapping recoveries later

        all_recovery_events = self.resolve_overlapping_recoveries(all_recovery_events)
        # Compute the area under the recovery events for further analysis
        recovery_areas = []
        for start_sec, duration_sec, slope, rise in all_recovery_events:
            # Find which signal segment contains this event
            area = np.nan
            for samples, data_start in zip(data_stats, data_starts): # usually only one signal since edf does not support discontinuities.
                signal_end = data_start + len(samples) / fs_chan
                # Check if the event is within this signal segment
                if start_sec >= data_start and start_sec < signal_end:
                    area = self.compute_recovery_area(samples, data_start, start_sec, duration_sec, fs_chan)
                    break
            recovery_areas.append(area)

        recovery_events = [('SpO2', 'recovery_SpO2', start_sec, duration_sec, channel, slope, rise)
                   for start_sec, duration_sec, slope, rise in all_recovery_events]
        recovery_df = pd.DataFrame(data=recovery_events,
            columns=['group', 'name', 'start_sec', 'duration_sec', 'channels', 'slope', 'depth'])
        recovery_df['area_percent_sec'] = recovery_areas
        return recovery_df


    def filter_nan_filtfilt(self, signal, order, fs_chan, cutoff_freq, type='low'):
        # We expect to have NaN values in chunk (if any)
        #   so we filter the signal (without nan values) even if it could have border effects
        #   and we reconstruct the filtered signal with the original NaN values.
        non_nan_indices = np.where(~np.isnan(signal))[0]
        if len(non_nan_indices) > 0:
            # reshape the i_nan_samples (x,1) to (x,)
            non_nan_indices = np.squeeze(non_nan_indices)
            samples_without_nan = signal[non_nan_indices]
            order_filtfilt = int(order)/2
            sos = scipysignal.butter(int(order_filtfilt), cutoff_freq,\
                btype=type, output='sos', fs=fs_chan)
            samples_filtered = scipysignal.sosfiltfilt(\
                sos, samples_without_nan).copy() # .copy() is a hack to make 
                                        # recording the EDF with pyedflib much
                                        # much much faster
            filtered_signal = np.empty_like(signal) 
            filtered_signal.fill(np.nan)
            filtered_signal[non_nan_indices] = samples_filtered
        else: # The whole signal is NaN - no filter applied
            filtered_signal = np.empty_like(signal)
            filtered_signal.fill(np.nan)
        return filtered_signal


    def detect_artifact_SpO2(self, sraw, data_starts, fs_chan):
        """
        Detect major artifacts from oxygen saturation signal.
        
        First, major artifacts are detected from the signal (SRaw) by filtering 
        the SRaw signal with 4th order Butterworth high-pass filter with a 1 Hz cutoff. 
        Next, the filtered signal is squared. Values >30 in the squared signal, 
        and values <50% and >100% in the SRaw signal are counted as artifacts. 
        Adjacent artifact points are grouped into a single artifact, and artifacts 
        are extended by one second in both directions to add a safety margin. 
        However, artifacts with a duration of ≤5 s are linearly interpolated.
        
        Parameters:
        - sraw: Raw signal array (may contain NaNs)
        - data_start: Start time of the signal in seconds
        - fs_chan: Sampling rate in Hz
        
        Returns:
        - cleaned_signal: Signal with short artifacts interpolated
        - artifact_events: List of (start_sec, duration_sec) tuples for artifacts >5s
        """
        # List of constants
        filter_order = 8 # The author uses order 4 with filtfilt but did not divide the order by 2
        threshold_squared = 30 # ABOSA 30
        lower_bound = 50
        upper_bound = 100
        art_buffer_sec = 1.0 # Extend each artifact by 1 second in both directions
        linear_art_sec = 5.0 # Interpolate artifacts with duration ≤ 5 seconds

        # We cannot use the ABOSA strategy when the sampling frequency is low (e.g. 1 Hz) - we use fs/3 as cutoff in this case
        cutoff_freq = min(1.0, fs_chan / 3.0) 

        data_cleaned = []
        data_gradient = []
        for samples, data_start in zip(sraw, data_starts):
            # 1. Identify artifact points directly from raw signal first
            # This avoids filter edge effects
            artifact_mask = np.zeros(len(samples), dtype=bool)
            artifact_mask |= (samples < lower_bound)
            artifact_mask |= (samples > upper_bound)
            artifact_mask |= np.isnan(samples)
            
            # 2. Apply 4th order Butterworth high-pass filter (1 Hz cutoff) on valid samples only
            filtered_signal = self.filter_nan_filtfilt(samples, filter_order, fs_chan, cutoff_freq, 'high')
            
            # 3. Square the filtered signal
            squared_signal = filtered_signal ** 2
            
            # 4. Add high-frequency artifacts (rapid changes)
            artifact_mask |= (squared_signal > threshold_squared)
            
            # 5. Group adjacent artifacts and extend by 1 second
            diff = np.diff(np.concatenate([[0], artifact_mask.astype(int), [0]]))
            starts = np.where(diff == 1)[0]
            ends = np.where(diff == -1)[0]
            
            # Extend each artifact by 1 second in both directions
            # Note: 'start' is the first artifact sample, 'end' is one past the last artifact sample
            extension_samples = int(fs_chan * art_buffer_sec)
            extended_mask = np.zeros(len(samples), dtype=bool)
            
            for start, end in zip(starts, ends):
                # Apply symmetric buffer: 1s before start and 1s after the last artifact sample
                extended_start = max(0, start - extension_samples)
                extended_end = min(len(samples), end + extension_samples)
                extended_mask[extended_start:extended_end] = True
            
            # Re-identify artifact regions after extension
            diff = np.diff(np.concatenate([[0], extended_mask.astype(int), [0]]))
            starts = np.where(diff == 1)[0]
            ends = np.where(diff == -1)[0]
            
            # 6. Interpolate artifacts with duration ≤ 5 seconds
            cleaned_signal = samples.copy()
            threshold_samples = int(fs_chan * linear_art_sec)
            artifact_events = []
            
            for start, end in zip(starts, ends):
                # start is first artifact sample, end is first non-artifact sample
                duration = end - start
                
                if duration <= threshold_samples:
                    # Linear interpolation for short artifacts
                    if start > 0 and end < len(samples):
                        x = [start - 1, end]
                        y = [samples[start - 1], samples[end]]
                        
                        # If the slope of the interpolation is too steep, we can skip the interpolation and keep it as artifact (NaN)
                        slope = abs((y[1] - y[0]) / ((x[1] - x[0])/fs_chan))  # Slope in % per second
                        if slope > np.sqrt(threshold_squared):
                            start_sec = (start / fs_chan) + data_start
                            duration_sec = duration / fs_chan
                            artifact_events.append((start_sec, duration_sec))
                            cleaned_signal[start:end] = np.nan
                            continue
                        
                        interpolator = interp1d(x, y, kind='linear')
                        cleaned_signal[start:end] = interpolator(np.arange(start, end))
                    
                    # Mark as non-artifact after interpolation
                    extended_mask[start:end] = False
                else:
                    # Keep artifacts longer than 5s
                    start_sec = (start / fs_chan) + data_start
                    duration_sec = duration / fs_chan
                    artifact_events.append((start_sec, duration_sec))
                    # Mark these samples as NaN in cleaned signal
                    cleaned_signal[start:end] = np.nan

            data_cleaned.append(cleaned_signal)
            data_gradient.append(squared_signal)
        
        return data_cleaned, artifact_events, data_gradient


    def correct_peak_indices_in_window(self, signal, peak_indices, window_s, fs_chan, find_max=True):
        """
        Correct peak locations by finding actual extrema in the original signal within a time window.
        Vectorized implementation for better performance.
        
        Parameters:
            signal : numpy array
                Original SpO2 signal.
            peak_indices : numpy array or list
                Indices of peaks to correct.
            window_s : float
                Window duration in seconds (centered on each peak).
            fs_chan : float
                Sampling frequency (Hz).
            find_max : bool
                If True, find maximum within window; if False, find minimum.
        
        Returns:
            corrected_indices : numpy array
                Corrected indices of peaks in the original signal.
        """
        peak_indices = np.asarray(peak_indices)
        if len(peak_indices) == 0:
            return np.array([], dtype=int)
        
        half_window_samples = int((window_s / 2) * fs_chan)
        signal_len = len(signal)
        
        # Vectorized window bounds calculation
        window_starts = np.maximum(0, peak_indices - half_window_samples)
        window_ends = np.minimum(signal_len, peak_indices + half_window_samples)
        
        corrected_indices = np.empty(len(peak_indices), dtype=int)
        valid_mask = np.ones(len(peak_indices), dtype=bool)
        
        for i, (ws, we) in enumerate(zip(window_starts, window_ends)):
            window_signal = signal[ws:we]
            if len(window_signal) > 0 and not np.all(np.isnan(window_signal)):
                if find_max:
                    corrected_indices[i] = ws + np.nanargmax(window_signal)
                else:
                    corrected_indices[i] = ws + np.nanargmin(window_signal)
            else:
                valid_mask[i] = False
        
        return corrected_indices[valid_mask]


    def correct_single_peak_index_in_window(self, signal, peak_idx, window_s, fs_chan, find_max=True):
        """
        Correct a single peak location by finding the actual extremum in the original
        signal within a centered time window.

        Parameters:
            signal : numpy array
                Original SpO2 signal.
            peak_idx : int
                Index of the peak to correct.
            window_s : float
                Window duration in seconds (centered on peak_idx).
            fs_chan : float
                Sampling frequency (Hz).
            find_max : bool
                If True, find maximum within window; if False, find minimum.

        Returns:
            corrected_idx : int or None
                Corrected index, or None if the window contains only NaN values.
        """
        half_window_samples = int((window_s / 2) * fs_chan)
        ws = max(0, peak_idx - half_window_samples)
        we = min(len(signal), peak_idx + half_window_samples)
        window_signal = signal[ws:we]
        if len(window_signal) == 0 or np.all(np.isnan(window_signal)):
            return None
        if find_max:
            return ws + np.nanargmax(window_signal)
        return ws + np.nanargmin(window_signal)


    def detect_local_min(self, signal, signal_lpf, fs_chan, min_peak_distance_samples, min_peak_prominence, data_start):
        """
        Detect local minimums from the low-pass filtered signal and correct their location
        by finding the actual minimum in the original signal within a 10s window.
        
        Parameters:
            signal : numpy array
                Original SpO2 signal.
            signal_lpf : numpy array
                Low-pass filtered SpO2 signal for trend detection.
            fs_chan : float
                Sampling frequency (Hz).
            min_peak_distance_samples : int
                Minimum distance between peaks in samples.
            min_peak_prominence : float
                Minimum prominence for peak detection.
            data_start : float
                Start time in seconds of this signal section.
        
        Returns:
            lmin_indices_corrected : numpy array
                Corrected indices of local minimums in the original signal.
        """
        window_s = 10  # seconds window to identify the real minimum
        half_window_samples = int((window_s / 2) * fs_chan)
        
        # Invert the signal to find minimums using find_peaks
        inverted_signal = -signal_lpf
        
        # Find local minimums (peaks in inverted signal)
        lmin_indices, lmin_properties = scipysignal.find_peaks(
            inverted_signal,
            distance=min_peak_distance_samples,
            prominence=min_peak_prominence
        )
        
        # Correct Lmin locations by finding actual minimum within 10s window
        lmin_indices_corrected = self.correct_peak_indices_in_window(
            signal, lmin_indices, window_s, fs_chan, find_max=False
        )
        
        if DEBUG:
            lmin_times_sec = data_start + lmin_indices_corrected / fs_chan
            lmin_values = signal[lmin_indices_corrected] if len(lmin_indices_corrected) > 0 else []
            print(f"Found {len(lmin_indices_corrected)} local minimums (corrected within {window_s}s window)\n")
            # for idx, (t, v) in enumerate(zip(lmin_times_sec, lmin_values)):
            #     print(f"  Lmin {idx}: time={t:.2f}s, value={v:.1f}%")
        
        return lmin_indices_corrected


    def detect_local_max(self, signal, signal_lpf, fs_chan, min_peak_distance_samples, min_peak_prominence, data_start):
        """
        Detect local maximums from the low-pass filtered signal and correct their location
        by finding the actual maximum in the original signal within a 5s window (to validate).

        If the difference is <3 percentage points between 2 consecutive Lmax, the first Lmax is removed.
        
        Parameters:
            signal : numpy array
                Original SpO2 signal.
            signal_lpf : numpy array
                Low-pass filtered SpO2 signal for trend detection.
            fs_chan : float
                Sampling frequency (Hz).
            min_peak_distance_samples : int
                Minimum distance between peaks in samples.
            min_peak_prominence : float
                Minimum prominence for peak detection.
            data_start : float
                Start time in seconds of this signal section.
        
        Returns:
            filtered_lmax_indices : numpy array
                Indices of local maximums filtered for too low maximums.
            lmax_indices_org : numpy array
                Indices of local maximums in the original signal.
        """
        window_s = 10  # seconds window to identify the real maximum
        min_drop_2_consecutive_max = 3  # minimum drop in SRaw values between two consecutive Lmaxs to consider both Lmaxs
        
        # Find local maximums using find_peaks on the filtered signal
        lmax_indices, lmax_properties = scipysignal.find_peaks(
            signal_lpf,
            distance=min_peak_distance_samples,
            prominence=min_peak_prominence
        )

        # Correct Lmax locations by finding actual maximum within 10s window
        lmax_indices_org = self.correct_peak_indices_in_window(
            signal, lmax_indices, window_s, fs_chan, find_max=True
        )

        # Lmaxvalues that are too low to potentially result in proper desaturation events are removed. 
        # This is done by checking the maximum difference in SRaw values between two adjacent Lmaxs: 
        # if the difference is <3 percentage points, the first Lmax is removed
        filtered_lmax_indices = []
        for i in range(len(lmax_indices_org)-1):
            current_lmax_idx = lmax_indices_org[i]
            next_lmax_idx = lmax_indices_org[i+1]
            signal_vals = signal[current_lmax_idx:next_lmax_idx]
            if len(signal_vals) > 1:
                current_lmax_val = np.nanmax(signal_vals)
                current_lmin_val = np.nanmin(signal_vals)
                if (current_lmax_val - current_lmin_val) >= min_drop_2_consecutive_max:
                    filtered_lmax_indices.append(current_lmax_idx)
            else:
                continue
        
        # Convert to numpy array for efficient operations (searchsorted, indexing)
        filtered_lmax_indices = np.array(filtered_lmax_indices, dtype=int)
        
        if DEBUG:
            lmax_times_sec = data_start + filtered_lmax_indices / fs_chan
            lmax_values = signal[filtered_lmax_indices] if len(filtered_lmax_indices) > 0 else []
            print(f"Found {len(filtered_lmax_indices)} local maximums (corrected within {window_s}s window)\n")
            # for idx, (t, v) in enumerate(zip(lmax_times_sec, lmax_values)):
            #     print(f"  Lmax {idx}: time={t:.2f}s, value={v:.1f}%")
        
        return filtered_lmax_indices, lmax_indices_org

    def discard_lmax_without_lmin(self, signal, lmin_indices, lmax_indices, lmax_idx, lmax_time, lmax_val, 
                                  data_start, fs_chan, max_slope_drop_sec, desaturation_drop_percent):
        """
        Find the best Lmin candidate for a given Lmax (lmax_idx).

        The maximum duration of a desaturation event is limited to 180 s.
        The potential Lmax-Lmin pair cannot go through another Lmax.
        
        Parameters:
            signal : numpy array
                Original SpO2 signal.
            lmin_indices : numpy array
                Indices of local minimums.
            lmax_indices : numpy array
                Indices of local maximums.
            lmax_idx : int
                Index of the current Lmax.
            lmax_time : float
                Time in seconds of the current Lmax.
            lmax_val : float
                Value of the current Lmax.
            data_start : float
                Start time in seconds of this signal section.
            fs_chan : float
                Sampling frequency (Hz).
            max_slope_drop_sec : float
                Maximum duration for the desaturation drop.
            desaturation_drop_percent : float
                Minimum drop percentage to be considered a desaturation.
        
        Returns:
            best_lmin : tuple or None
                (lmin_idx, lmin_time, lmin_val, drop) or None if no valid candidate.
        """
        max_end_time = lmax_time + max_slope_drop_sec
        candidate_lmins = []
        
        for lmin_idx in lmin_indices:
            lmin_time = data_start + lmin_idx / fs_chan
            
            # Lmin must be after Lmax and within max duration
            if lmin_time <= lmax_time or lmin_time > max_end_time:
                continue
            
            # Check if there's another Lmax between current Lmax and this Lmin
            # Use searchsorted for O(log n) lookup instead of np.where O(n)
            current_pos = np.searchsorted(lmax_indices, lmax_idx)
            if current_pos + 1 < len(lmax_indices):
                next_lmax_time = data_start + lmax_indices[current_pos + 1] / fs_chan
                if next_lmax_time < lmin_time:
                    continue
            
            lmin_val = signal[lmin_idx]
            drop = lmax_val - lmin_val
            
            # Reject if drop is less than minimum threshold
            if drop < desaturation_drop_percent:
                continue
            
            candidate_lmins.append((lmin_idx, lmin_time, lmin_val, drop))
        
        if not candidate_lmins:
            return None
        
        return candidate_lmins


    def adjust_lmax_for_fall_rate(self, signal, signal_hpf, lmax_idx, lmin_idx, data_start, fs_chan, desat_event_slope_shallow_limit=-0.05):
        """
        Shift Lmax forward to the next variation peak using the high-pass filtered signal 
        to identify the onset of the fall, accepting the shift only if the slope between 
        consecutive peaks is positive or not steeper than the negative fall-rate threshold.
        
        Parameters:
            signal : numpy array
                SpO2 signal (already low-pass filtered).
            signal_hpf : numpy array
                High-pass filtered SpO2 signal to identify peaks corresponding to rapid changes.
            lmax_idx : int
                Index of the current Lmax.
            lmin_idx : int
                Index of the matched Lmin.
            data_start : float
                Start time in seconds of this signal section.
            fs_chan : float
                Sampling frequency (Hz).
            desat_event_slope_shallow_limit : float
                Fall rate threshold in %/s (deepest fall rate to accept a shift).
        
        Returns:
            adjusted_lmax_idx : int
                Adjusted index of Lmax.
            adjusted_lmax_time : float
                Adjusted time of Lmax.
            adjusted_lmax_val : float
                Adjusted value of Lmax.
        """
        # Find maximum parameter
        min_peak_distance_sec = 1
        # seconds window to identify the real maximum for each peak
        if fs_chan <= 2:
            window_s = 2
        else:
            window_s = 1 
        # Square the high-pass filtered signal to enhance peaks (in both directions)
        signal_squared = signal_hpf ** 2
        
        # Detect peaks in the Squared signal - we are looking for the biggest drops
        min_peak_distance_samples = int(min_peak_distance_sec * fs_chan)  
        peaks, _ = scipysignal.find_peaks(
            signal_squared,
            distance=min_peak_distance_samples,
            #prominence=min_peak_prominence
        )
        
        # Find the next peak after lmax_idx
        adjusted_lmax_idx = lmax_idx
        next_peaks = peaks[peaks > lmax_idx]
        possible_peaks = next_peaks[next_peaks < lmin_idx]

        if len(possible_peaks) > 0:
            # Loop through all peaks before lmin_idx and keep shifting to better maxima
            for peak_idx in possible_peaks:
                    
                # Correct peak locations within 1s window
                lmax_corrected = self.correct_peak_indices_in_window(signal, [adjusted_lmax_idx], window_s=window_s, fs_chan=fs_chan)
                lmax_corrected = lmax_corrected[0]
                lmax_shifted = self.correct_peak_indices_in_window(signal, [peak_idx], window_s=window_s, fs_chan=fs_chan)
                lmax_shifted = lmax_shifted[0]
                
                duration_sec = (lmax_shifted - lmax_corrected) / fs_chan
                drop = signal[lmax_shifted] - signal[lmax_corrected]

                # Evaluate fall rate to ensure it's a valid shift
                fall_rate = drop / duration_sec if duration_sec > 0 else 0
                # For any positive fall rate or slow fall rate, we accept the shift
                if fall_rate >= desat_event_slope_shallow_limit:
                    adjusted_lmax_idx = lmax_shifted
                # If fall rate is too steep, keep current position and stop
                else:
                    break
        
        adjusted_lmax_time = data_start + adjusted_lmax_idx / fs_chan
        adjusted_lmax_val = signal[adjusted_lmax_idx]
        return adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, signal_squared
    

    # Obsolete
    def adjust_for_derivative_plateau(self, signal, signal_derivative, adjusted_lmax_idx, adjusted_lmax_val, lmin_idx, lmin_time, lmin_val, 
                           data_start, fs_chan, min_plateau_duration_sec, derivative_threshold, derivative_mean_threshold):
        """
        Adjust Lmax or Lmin if a flat plateau exists within the event.
        Plateau detection is based on the derivative of the signal:
        - Each sample must have |derivative| < derivative_threshold (rejects steep spikes)
        - The mean derivative over the plateau must have |mean| < derivative_mean_threshold (rejects constant slopes)
        
        This allows detection of plateaus with small oscillations around a mean value,
        while rejecting both steep transitions and constant drifts.
        
        Parameters:
            signal : numpy array
                Low-pass filtered SpO2 signal.
            adjusted_lmax_idx : int
                Current adjusted Lmax index.
            adjusted_lmax_val : float
                Current adjusted Lmax value.
            lmin_idx : int
                Current Lmin index.
            lmin_time : float
                Current Lmin time.
            lmin_val : float
                Current Lmin value.
            data_start : float
                Start time in seconds of this signal section.
            fs_chan : float
                Sampling frequency (Hz).
            min_plateau_duration_sec : float
                Minimum plateau duration in seconds (default 10s).
            derivative_threshold : float
                Maximum absolute derivative (%/sec) at each sample to be considered flat (default 0.01).
            derivative_mean_threshold : float
                Maximum absolute mean derivative (%/sec) over the plateau to reject constant slopes (default 0.01).
        
        Returns:
            adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, lmin_idx, lmin_time, lmin_val, plateau_list : tuple
                Adjusted values after plateau handling and list of all detected plateaus.
        """
        min_plateau_samples = int(min_plateau_duration_sec * fs_chan)
        plateau_list = []
        
        # Iterate to detect multiple plateaus
        while True:
            event_signal = signal[adjusted_lmax_idx:lmin_idx + 1]
            adjusted_lmax_time = data_start + adjusted_lmax_idx / fs_chan
            derivative = signal_derivative[adjusted_lmax_idx:lmin_idx + 1]
    
            # Stop if remaining duration is less than minimum plateau duration
            if len(event_signal) < min_plateau_samples:
                break
            
            # Step 1: Identify samples where individual derivative is below threshold
            # This rejects steep spikes (both positive and negative)
            flat_mask = np.abs(derivative) < derivative_threshold
            
            # Find contiguous flat regions based on individual derivative threshold
            diff = np.diff(np.concatenate([[0], flat_mask.astype(int), [0]]))
            starts = np.where(diff == 1)[0]
            ends = np.where(diff == -1)[0]
            
            # Step 2: For each candidate region, check if mean derivative is also low
            # This rejects constant slopes (e.g., steady decline)
            plateau_found = False
            best_plateau_start = 0
            best_plateau_end = 0
            for start, end in zip(starts, ends):
                if (end - start) >= min_plateau_samples:
                    # Compute mean derivative over this candidate region
                    mean_derivative = np.mean(derivative[start:end])
                    # Accept only if mean derivative is also low (rejects constant slopes)
                    if np.abs(mean_derivative) < derivative_mean_threshold:
                        best_plateau_start = start
                        best_plateau_end = end
                        plateau_found = True
                        break
            
            if not plateau_found:
                break
            
            # Store plateau information
            plateau_start_time = data_start + (adjusted_lmax_idx + best_plateau_start) / fs_chan
            plateau_duration = (best_plateau_end - best_plateau_start) / fs_chan
            plateau_list.append([plateau_start_time, plateau_duration])
            
            # Adjust Lmax or Lmin to maximize depth
            plateau_val = np.nanmean(event_signal[best_plateau_start:best_plateau_end])
            drop_before_plateau = adjusted_lmax_val - plateau_val
            drop_after_plateau = plateau_val - lmin_val
            
            if drop_before_plateau > drop_after_plateau:
                # Shift Lmin to start of plateau
                lmin_idx = adjusted_lmax_idx + best_plateau_start
                lmin_time = data_start + lmin_idx / fs_chan
                lmin_val = signal[lmin_idx]
            else:
                # Shift Lmax to end of plateau
                adjusted_lmax_idx = adjusted_lmax_idx + best_plateau_end
                adjusted_lmax_time = data_start + adjusted_lmax_idx / fs_chan
                adjusted_lmax_val = signal[adjusted_lmax_idx]
            
                # Make sure the current max on the low pass filtered signal is the maximum value until the Lmin candidate
                if lmin_idx - adjusted_lmax_idx > 1:
                    real_lmax_val = np.nanmax(signal[adjusted_lmax_idx:lmin_idx+1])
                    if real_lmax_val > adjusted_lmax_val:
                        # Update adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val to the real maximum on the low pass filtered signal
                        adjusted_lmax_idx = np.nanargmax(signal[adjusted_lmax_idx:lmin_idx+1]) + adjusted_lmax_idx
                        adjusted_lmax_time = data_start + adjusted_lmax_idx / fs_chan
                        adjusted_lmax_val = signal[adjusted_lmax_idx]

        return adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, lmin_idx, lmin_time, lmin_val, plateau_list
    

    def adjust_for_rounded_plateau(self, signal, signal_derivative, \
                        adjusted_lmax_idx, adjusted_lmax_val, lmin_idx, lmin_time, lmin_val, 
                        data_start, fs_chan, min_plateau_duration_sec):
        """
        Adjust Lmax or Lmin if a flat plateau exists within the event.
        Plateau detection is based on the derivative of the signal:
        - Each sample must have |derivative| < derivative_threshold (rejects steep spikes)
        - The mean derivative over the plateau must have |mean| < derivative_mean_threshold (rejects constant slopes)
        
        This allows detection of plateaus with small oscillations around a mean value,
        while rejecting both steep transitions and constant drifts.
        
        Parameters:
            signal : numpy array
                Low-pass filtered SpO2 signal.
            adjusted_lmax_idx : int
                Current adjusted Lmax index.
            adjusted_lmax_val : float
                Current adjusted Lmax value.
            lmin_idx : int
                Current Lmin index.
            lmin_time : float
                Current Lmin time.
            lmin_val : float
                Current Lmin value.
            data_start : float
                Start time in seconds of this signal section.
            fs_chan : float
                Sampling frequency (Hz).
            min_plateau_duration_sec : float
                Minimum plateau duration in seconds (default 10s).
            derivative_threshold : float
                Maximum absolute derivative (%/sec) at each sample to be considered flat (default 0.01).
            derivative_mean_threshold : float
                Maximum absolute mean derivative (%/sec) over the plateau to reject constant slopes (default 0.01).
        
        Returns:
            adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, lmin_idx, lmin_time, lmin_val, plateau_list : tuple
                Adjusted values after plateau handling and list of all detected plateaus.
        """
        min_plateau_samples = int(min_plateau_duration_sec * fs_chan)
        plateau_list = []
        
        # Iterate to detect multiple plateaus
        while True:
            event_signal = signal[adjusted_lmax_idx:lmin_idx + 1]
            adjusted_lmax_time = data_start + adjusted_lmax_idx / fs_chan
            derivative = signal_derivative[adjusted_lmax_idx:lmin_idx + 1]

            # Stop if remaining duration is less than minimum plateau duration
            if len(event_signal) < min_plateau_samples:
                break
            
            # Step 1: Find edges (transitions where derivative != 0)
            # Edges are where the rounded signal changes value
            edge_mask = derivative != 0
            edge_indices = np.where(edge_mask)[0]
            
            # Step 2: Calculate plateau durations between consecutive edges
            # A plateau is the flat region between two edges
            plateau_found = False
            best_plateau_start = 0
            best_plateau_end = 0
            
            if len(edge_indices) == 0:
                # No edges found - the entire region is a plateau
                if len(event_signal) >= min_plateau_samples:
                    best_plateau_start = 0
                    best_plateau_end = len(event_signal)
                    plateau_found = True
            else:
                # Check plateau from start to first edge
                if edge_indices[0] >= min_plateau_samples:
                    best_plateau_start = 0
                    best_plateau_end = edge_indices[0]
                    plateau_found = True
                
                # Check plateaus between consecutive edges
                if not plateau_found:
                    for i in range(len(edge_indices) - 1):
                        plateau_duration_samples = edge_indices[i + 1] - edge_indices[i] - 1
                        if plateau_duration_samples >= min_plateau_samples:
                            best_plateau_start = edge_indices[i] + 1
                            best_plateau_end = edge_indices[i + 1]
                            plateau_found = True
                            break
                
                # Check plateau from last edge to end
                if not plateau_found:
                    plateau_duration_samples = len(event_signal) - edge_indices[-1] - 1
                    if plateau_duration_samples >= min_plateau_samples:
                        best_plateau_start = edge_indices[-1] + 1
                        best_plateau_end = len(event_signal)
                        plateau_found = True
            
            if not plateau_found:
                break
            
            # Store plateau information
            plateau_start_time = data_start + (adjusted_lmax_idx + best_plateau_start) / fs_chan
            plateau_duration = (best_plateau_end - best_plateau_start) / fs_chan
            plateau_list.append([plateau_start_time, plateau_duration])
            
            # Adjust Lmax or Lmin to maximize depth
            plateau_val = np.nanmean(event_signal[best_plateau_start:best_plateau_end])
            drop_before_plateau = adjusted_lmax_val - plateau_val
            drop_after_plateau = plateau_val - lmin_val
            
            if drop_before_plateau > drop_after_plateau:
                # Shift Lmin to start of plateau
                lmin_idx = adjusted_lmax_idx + best_plateau_start
                lmin_time = data_start + lmin_idx / fs_chan
                lmin_val = signal[lmin_idx]
            else:
                # Shift Lmax to end of plateau
                adjusted_lmax_idx = adjusted_lmax_idx + best_plateau_end
                adjusted_lmax_time = data_start + adjusted_lmax_idx / fs_chan
                adjusted_lmax_val = signal[adjusted_lmax_idx]
            
                # Make sure the current max on the low pass filtered signal is the maximum value until the Lmin candidate
                if lmin_idx - adjusted_lmax_idx > 1:
                    real_lmax_val = np.nanmax(signal[adjusted_lmax_idx:lmin_idx+1])
                    if real_lmax_val > adjusted_lmax_val:
                        # Update adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val to the real maximum on the low pass filtered signal
                        adjusted_lmax_idx = np.nanargmax(signal[adjusted_lmax_idx:lmin_idx+1]) + adjusted_lmax_idx
                        adjusted_lmax_time = data_start + adjusted_lmax_idx / fs_chan
                        adjusted_lmax_val = signal[adjusted_lmax_idx]

        return adjusted_lmax_idx, adjusted_lmax_time, adjusted_lmax_val, lmin_idx, lmin_time, lmin_val, plateau_list


    def compute_desat_stats(self, desat_df, total_stats, stage_sleep_period_df):
        desat_stats = {}
        # The number of oxygen desaturation in the sleep period.
        desat_stats['desat_count'] = len(desat_df)
        # The Oxygen Desaturation Index (ODI) : number of desaturation per sleep hour.
        desat_stats['desat_ODI'] = len(desat_df)/((total_stats['total_valid_min'])/60)
        # Desaturation severity : The sum of areas under the desaturation events in percent*sec over the sleep period (sec).
        desat_stats['desat_severity'] = desat_df['area_percent_sec'].sum()/(total_stats['total_valid_min']*60)
        # The percentage of time spent in desaturation during the sleep period.
        desat_stats['desat_SP_percent'] = desat_df['duration_sec'].sum()/(total_stats['total_valid_min']*60)*100
        # The average duration in sec of the oxygen desaturation events in the sleep period.
        desat_stats['desat_dur_avg_sec'] = desat_df['duration_sec'].mean()
        # The median value of the duration in sec of the oxygen desaturation events in the sleep period.
        desat_stats['desat_dur_med_sec'] = desat_df['duration_sec'].median()
        # The average area under the desaturation events in percent*sec.
        desat_stats['desat_area_avg'] = desat_df['area_percent_sec'].mean()
        # The median area under the desaturation events in percent*sec.
        desat_stats['desat_area_med'] = desat_df['area_percent_sec'].median()
        # The average slope of the desaturation events in percent/sec.
        desat_stats['desat_slope_avg'] = desat_df['slope'].mean()
        # The median slope of the desaturation events in percent/sec.
        desat_stats['desat_slope_med'] = desat_df['slope'].median()
        # The average depth of the desaturation events in percent.
        desat_stats['desat_depth_avg'] = desat_df['depth'].mean()
        # The median depth of the desaturation events in percent.
        desat_stats['desat_depth_med'] = desat_df['depth'].median()

        return desat_stats

    def compute_recovery_stats(self, recovery_df, total_stats, stage_sleep_period_df):
        recovery_stats = {}
        # The number of oxygen recovery in the sleep period.
        recovery_stats['recovery_count'] = len(recovery_df)
        # The Recovery Index (RI) : number of recovery per sleep hour.
        recovery_stats['recovery_index'] = len(recovery_df)/((total_stats['total_valid_min'])/60)
        # Recovery severity : The sum of areas under the recovery events in percent*sec over the sleep period (sec).
        recovery_stats['recovery_severity'] = recovery_df['area_percent_sec'].sum()/(total_stats['total_valid_min']*60)        
        # The percentage of time spent in recovery during the sleep period.
        recovery_stats['recovery_SP_percent'] = recovery_df['duration_sec'].sum()/(total_stats['total_valid_min']*60)*100
        # The average duration in sec of the oxygen recovery events in the sleep period.
        recovery_stats['recovery_dur_avg_sec'] = recovery_df['duration_sec'].mean() 
        # The median value of the duration in sec of the oxygen recovery events in the sleep period.
        recovery_stats['recovery_dur_med_sec'] = recovery_df['duration_sec'].median()
        # The average area under the recovery events in percent*sec.
        recovery_stats['recovery_area_avg'] = recovery_df['area_percent_sec'].mean()
        # The median area under the recovery events in percent*sec.
        recovery_stats['recovery_area_med'] = recovery_df['area_percent_sec'].median()
        # The average slope of the recovery events in percent/sec.
        recovery_stats['recovery_slope_avg'] = recovery_df['slope'].mean()  
        # The median slope of the recovery events in percent/sec.
        recovery_stats['recovery_slope_med'] = recovery_df['slope'].median()
        # The average depth of the recovery events in percent.
        recovery_stats['recovery_depth_avg'] = recovery_df['depth'].mean()  
        # The median depth of the recovery events in percent.
        recovery_stats['recovery_depth_med'] = recovery_df['depth'].median()

        return recovery_stats

    
    def compute_temporal_link_stats(self, desat_df, arousals_selected, window_link_sec, channel):
        """
        Parameters :
            desat_df : pandas DataFrame
                desaturation events
                'group': Group of events this event is part of (String)
                'name': Name of the event (String)
                'start_sec': Starting time of the event in sec (Float)
                'duration_sec': Duration of the event in sec (Float)
                'channels' : Channel where the event occures (String)
            arousals_selected : pandas DataFrame
                arousals events in asleep stages and duration limits applied
            window_link_sec     : float
                The window length (s) to compute the temporal link between desaturations and arousals.
            channel     : string
                Channel label.
        Return : 
            temporal_stats : dict
                Dictionary of statistics
                'desat_start_before_count' : 'The number of desaturations that start before the beginning of the arousal.',
                'desat_start_before_delay_sec' : 'Arousal starts before desaturation- The average delay between arousal and the beginning of the desaturation in sec.',
                'desat_end_before_count' : 'The number of desaturations that end before the beginning of the arousal.',
                'desat_end_before_delay_sec' : 'Desaturation ends before arousal - The average delay between desaturations and the beginning of the arousal in sec.', 
                'arousal_start_before_count' : 'The number of arousals that start before the beginning of the desaturation.',
                'arousal_start_before_delay_sec' : 'Arousal starts before desaturation- The average delay between arousal and the beginning of the desaturation in sec.',
                'arousal_end_before_count' : 'The number of arousals that end before the beginning of the desaturation.',
                'arousal_end_before_delay_sec' : 'Arousal ends before desaturation- The average delay between arousal and the beginning of the desaturation in sec.'                
            link_event_df : pandas DataFrame
                Temporal link events.
        """           
        temporal_stats = {}
        
        # Desaturation first - start
        #---------------------------
        flat_list_delay, i_evt1_linked, i_evt2_unique = \
            EventTemporalLink.compute_delay_start(self, desat_df, arousals_selected, window_link_sec)
        # The number of desaturations that start before the beginning of the arousal.
        temporal_stats['desat_start_before_count'] = len(flat_list_delay)
        if len(flat_list_delay)>0:
            # Desaturation starts before arousal- The average delay between desaturation and the beginning of the arousal in sec.
            temporal_stats['desat_start_before_delay_sec'] = np.mean(flat_list_delay)
            link_start = []
            for i_link in range(len(i_evt1_linked)):
                start_sec = desat_df.loc[i_evt1_linked[i_link]]['start_sec']
                duration_sec = arousals_selected.loc[i_evt2_unique[i_link]]['start_sec']-start_sec
                link_start.append(['SpO2','SpO2_desat_start_link', start_sec, duration_sec, channel])
            link_desat_start_df = manage_events.create_event_dataframe(link_start)
        else:
            temporal_stats['desat_start_before_delay_sec'] = np.nan
            link_desat_start_df = manage_events.create_event_dataframe(None)

        # Desaturation first - end
        #---------------------------
        flat_list_delay, i_evt1_linked, i_evt2_unique = \
            EventTemporalLink.compute_delay_end(self, desat_df, arousals_selected, window_link_sec)
        # The number of desaturations that end before the beginning of the arousal.
        temporal_stats['desat_end_before_count'] = len(flat_list_delay)
        if len(flat_list_delay)>0:
            # Desaturation ends before arousal - The average delay between desaturations and the beginning of the arousal in sec.
            temporal_stats['desat_end_before_delay_sec'] = np.mean(flat_list_delay)
            link_start = []
            for i_link in range(len(i_evt1_linked)):
                start_sec = desat_df.loc[i_evt1_linked[i_link]]['start_sec']+desat_df.loc[i_evt1_linked[i_link]]['duration_sec']
                duration_sec = arousals_selected.loc[i_evt2_unique[i_link]]['start_sec']-start_sec
                link_start.append(['SpO2','SpO2_desat_end_link', start_sec, duration_sec, channel])
            link_desat_end_df = manage_events.create_event_dataframe(link_start)
        else:
            temporal_stats['desat_end_before_delay_sec'] = np.nan
            link_desat_end_df = manage_events.create_event_dataframe(None)

        # Arousal first - start
        #---------------------------
        flat_list_delay, i_evt1_linked, i_evt2_unique = \
            EventTemporalLink.compute_delay_start(self, arousals_selected, desat_df, window_link_sec)
        # The number of arousal that start before the beginning of the desaturation.
        temporal_stats['arousal_start_before_count'] = len(flat_list_delay)
        if len(flat_list_delay)>0:
            # Arousal starts before desaturation- The average delay between arousal and the beginning of the desaturation in sec.
            temporal_stats['arousal_start_before_delay_sec'] = np.mean(flat_list_delay)
            link_start = []
            for i_link in range(len(i_evt1_linked)):
                start_sec = arousals_selected.loc[i_evt1_linked[i_link]]['start_sec']
                duration_sec = desat_df.loc[i_evt2_unique[i_link]]['start_sec']-start_sec
                link_start.append(['SpO2','SpO2_arousal_start_link', start_sec, duration_sec, channel])
            link_arousal_start_df = manage_events.create_event_dataframe(link_start)
        else:
            temporal_stats['arousal_start_before_delay_sec'] = np.nan
            link_arousal_start_df = manage_events.create_event_dataframe(None)

        # Arousal first - end
        #---------------------------
        flat_list_delay, i_evt1_linked, i_evt2_unique = \
            EventTemporalLink.compute_delay_end(self, arousals_selected, desat_df, window_link_sec)
        # The number of arousal that end before the beginning of the desaturation.
        temporal_stats['arousal_end_before_count'] = len(flat_list_delay)
        if len(flat_list_delay)>0:
            # arousal ends before arousal - The average delay between arousal and the beginning of the desaturation in sec.
            temporal_stats['arousal_end_before_delay_sec'] = np.mean(flat_list_delay)        
            link_start = []
            for i_link in range(len(i_evt1_linked)):
                start_sec = arousals_selected.loc[i_evt1_linked[i_link]]['start_sec']+arousals_selected.loc[i_evt1_linked[i_link]]['duration_sec']
                duration_sec = desat_df.loc[i_evt2_unique[i_link]]['start_sec']-start_sec
                link_start.append(['SpO2','SpO2_arousal_end_link', start_sec, duration_sec, channel])
            link_arousal_end_df = manage_events.create_event_dataframe(link_start)
"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    OxygenDesatDetector
    A Class to analyze the oxygen channel, detect oxygen desaturations and export oxygen saturation report.
"""
import matplotlib.pyplot as plt
plt.switch_backend('agg')  # turn off gui
import numpy as np
import os.path
import pandas as pd
import scipy.signal as scipysignal

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
        self.stage_stats_labels = ['N1', 'N2', 'N3', 'R', 'W']
        self.N_CYCLES = 9
        self.values_below = [96, 94, 92, 90, 85, 80, 75, 70, 60]
        self.variability_tolerance = 2
    

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

        #----------------------------------------------------------------------
        # Header parameters
        # subject info, sleep cycle parameters, desaturation parameters
        #----------------------------------------------------------------------
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

        # Keep stage from the first awake or sleep until the last awake or sleep
        sleep_stage_df.loc[:, 'name'] = sleep_stage_df['name'].apply(int)
        index_valid = sleep_stage_df[sleep_stage_df['name']<8].index
        stage_rec_df = sleep_stage_df.loc[index_valid[0]:index_valid[-1]]
        stage_rec_df.reset_index(inplace=True, drop=True)

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

        # Compute stats for the whole recording from lights off to lights on
        #----------------------------------------------------------------------
        total_stats, data_stats, data_starts = self.compute_total_stats_saturation(\
            stage_rec_df, signals, subject_info, fs_chan, picture_dir, invalid_events)

        # Compute stats for thirds
        #----------------------------------------------------------------------
        n_divisions = 3
        section_label = 'third'
        third_stats = self.compute_division_stats_saturation(n_divisions, section_label, stage_rec_df, signals)

        # Compute stats for halves
        #----------------------------------------------------------------------
        n_divisions = 2
        section_label = 'half'
        half_stats = self.compute_division_stats_saturation(n_divisions, section_label, stage_rec_df, signals)

        # Compute stats for stages
        #----------------------------------------------------------------------       
        stage_stats = self.compute_stages_stats_saturation(stage_rec_df, signals, fs_chan)

        # Compute stats for cycles
        #----------------------------------------------------------------------       
        cycle_stats = self.compute_cycles_stats_saturation(sleep_cycles_df, signals)

        # Detect desaturation 
        #----------------------------------------------------------------------
            # "parameters_oxy": dict
            # 'desaturation_drop_percent' : 'Drop level (%) for the oxygen desaturation "3 or 4"',
            # 'max_slope_drop_sec' : 'The maximum duration (s) during which the oxygen level is dropping "120 or 20"',
            # 'min_hold_drop_sec' : 'Minimum duration (s) during which the oxygen level drop is maintained "10 or 5"',
        asleep_stages_df = stage_rec_df[((stage_rec_df['name']>0) & (stage_rec_df['name']<6))]
        desat_df = self.detect_desaturation(data_starts, data_stats, fs_chan, channel, parameters_oxy, asleep_stages_df)
        desat_stats = self.compute_desat_stats(desat_df, asleep_stages_df)

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
                stage_stats | cycle_stats | desat_stats #| temporal_stats
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
            'desat_events' : desat_df
        }


    def _plot_oxygen_saturation(self, data_to_plot, fs_chan, fig_name, data_starts, invalid_events):

        figure, ax = plt.subplots()
        figure.set_size_inches(25, 5)
        ax.clear()
        ymin = np.nanmin(data_to_plot)
        new_fs = fs_chan
        data_2_plot_end = len(data_to_plot)/new_fs+data_starts
        time = np.arange(data_starts, data_2_plot_end, 1/new_fs)
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

    
    def compute_division_stats_saturation(self, n_divisions, section_label, stage_rec_df, signals):
        """""
            Compute the statistics (mean, std, max and min) of the oxygen saturation for the requested division.
            n_divisions can be 3 or 2.

            Parameters
            -----------
                n_divisions                 : int
                    Number of divisions.
                section_label               : string
                    Label of the division.
                stage_rec_df                : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])  
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
        n_epochs = len(stage_rec_df)
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
            start = stage_rec_df.iloc[index_start]['start_sec']
            end = stage_rec_df.iloc[index_stop-1]['start_sec']+ stage_rec_df.iloc[index_stop-1]['duration_sec']
            dur = end - start
            signals_third = []
            for signal in signals:
                # Because of the discontinuity
                # we have to verify if the signal includes at least partially the events
                # Look for the Right windows time
                if (signal.start_time<(start+dur)) and ((signal.start_time+signal.duration)>start): 
                    # Extract and define the new extracted channel_cur
                    channel_cur = self.extract_samples_from_events(signal, start, dur)
                    signals_third.append(channel_cur)

            # Flat signals into an array
            data_array = np.empty(0)
            for i_bout, samples in enumerate(signals_third):
                data_array = np.concatenate((data_array, samples), axis=0)

            # Clean-up invalid values
            #data_array = np.round(data_array,0) # to copy Gaetan
            data_array[data_array>100]=np.nan
            data_array[data_array<=0]=np.nan
            stats_dict[f"{section_label}{section_val}_saturation_avg"] = np.nanmean(data_array)
            stats_dict[f"{section_label}{section_val}_saturation_std"] = np.nanstd(data_array)
            stats_dict[f"{section_label}{section_val}_saturation_min"] = np.round(np.nanmin(data_array),0)
            stats_dict[f"{section_label}{section_val}_saturation_max"] = np.round(np.nanmax(data_array),0)            
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


    def compute_total_stats_saturation(self, stage_rec_df, signals, subject_info, fs_chan, picture_dir, invalid_events):
        """
        Parameters :
            stage_rec_df : pandas DataFrame
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
        # Extract samples from lights off to lights on. 
        start = stage_rec_df['start_sec'].values[0]
        end = stage_rec_df['start_sec'].values[-1]+stage_rec_df['duration_sec'].values[-1]
        dur = end - start
        data_stats = []
        data_starts = []
        for signal in signals:
            # Because of the discontinuity
            # we have to verify if the signal includes at least partially the events
            # Look for the Right windows time
            if (signal.start_time<(start+dur)) and ((signal.start_time+signal.duration)>start): 
                cur_start = signal.start_time if start<=signal.start_time else start
                cur_end = end if end<=signal.end_time else signal.end_time
                # if start<=signal.start_time:
                #     cur_start = signal.start_time
                # else:
                #     cur_start = start
                # if end<=signal.end_time:
                #     cur_end = end
                # else:
                #     cur_end = signal.end_time
                #cur_dur = cur_end-cur_start
                # Extract and define the new extracted channel_cur
                channel_cur = self.extract_samples_from_events(signal, cur_start, cur_end-cur_start)
                # Clean-up invalid values
                #channel_cur = np.round(channel_cur,0) # to copy Gaétan
                channel_cur[channel_cur>100]=np.nan
                channel_cur[channel_cur<=0]=np.nan
                data_starts.append(cur_start)      
                data_stats.append(channel_cur)

        # Generate and save the oxygen saturation graph
        if len(picture_dir)>0:
            for i_bout, samples in enumerate(data_stats):
                fig_name = os.path.join(picture_dir, f"{subject_info['filename']}_oxygen_saturation{i_bout}.pdf")
                self._plot_oxygen_saturation(samples, fs_chan, fig_name, data_starts[i_bout], invalid_events)

        # Flat signals into an array
        data_array = np.empty(0)
        for i_bout, samples in enumerate(data_stats):
            data_array = np.concatenate((data_array, samples), axis=0)

        total_stats = {}
        total_stats["total_valid_min"] = (len(data_array)-np.isnan(data_array).sum())/fs_chan/60
        total_stats["total_invalid_min"]  = np.isnan(data_array).sum()/fs_chan/60
        total_stats["total_saturation_avg"] = np.nanmean(data_array)
        total_stats["total_saturation_std"] = np.nanstd(data_array)
        total_stats["total_saturation_min"] = np.round(np.nanmin(data_array),0)
        total_stats["total_saturation_max"] = np.round(np.nanmax(data_array),0)
        for val in self.values_below:
            total_stats[f"total_below_{val}_min"] = (data_array<val).sum()/fs_chan/60
        return total_stats, data_stats, data_starts


    def compute_stages_stats_saturation(self, stage_rec_df, signals, fs_chan):
        """
        Parameters :
            stage_rec_df : pandas DataFrame
                Sleep stages from lights off to lights on.
            signal : SignalModel object
                signal with channel, samples, sample_rate...
            fs_chan : float
                sampling rate of the channel
        Return : 
            stage_dict : dict
                statistics fot the stages.
                Saturation_avg, std, min and max for each stage.
                Duration in min for saturation under different thresholds.
        """    
        stage_start_times = stage_rec_df['start_sec'].to_numpy().astype(float)
        stage_duration_times = stage_rec_df['duration_sec'].to_numpy().astype(float)
        stage_name = stage_rec_df['name'].apply(str).to_numpy()

        stage_dict = {}
        for stage_label in self.stage_stats_labels:
            stage_mask = (stage_name==commons.sleep_stages_name[stage_label])
            start_masked = stage_start_times[stage_mask]
            dur_masked = stage_duration_times[stage_mask]
            if any(stage_mask):
                signals_from_stages = []
                for start, dur in zip(start_masked, dur_masked):
                    end = start + dur
                    for j, signal in enumerate(signals):
                        if (signal.start_time<(start+dur)) and ((signal.start_time+signal.duration)>start): 
                            # Extract and define the new extracted channel_cur
                            cur_start = signal.start_time if start<=signal.start_time else start
                            cur_end = end if end<=signal.end_time else signal.end_time
                            cur_samples = self.extract_samples_from_events(signal, cur_start, cur_end-cur_start)
                            # When the last epoch is not completed
                            if (len(cur_samples)/fs_chan) < dur:
                                n_miss_samples = int(round((dur-len(cur_samples)/fs_chan)*fs_chan,0))
                                cur_samples = np.pad(cur_samples, (0, n_miss_samples), constant_values=(0,np.nan))
                            signals_from_stages.append(cur_samples)

                # Flat signals into an array
                signals_cur_stage = np.empty(0)
                for i_bout, samples in enumerate(signals_from_stages):
                    signals_cur_stage = np.concatenate((signals_cur_stage, samples), axis=0)

                # Clean-up invalid values
                signals_cur_stage[signals_cur_stage>100]=np.nan
                signals_cur_stage[signals_cur_stage<=0]=np.nan
                stage_dict[f'{stage_label}_saturation_avg'] = np.nanmean(signals_cur_stage)
                stage_dict[f'{stage_label}_saturation_std'] = np.nanstd(signals_cur_stage)
                stage_dict[f'{stage_label}_saturation_min'] = np.round(np.nanmin(signals_cur_stage),0)
                stage_dict[f'{stage_label}_saturation_max'] = np.round(np.nanmax(signals_cur_stage),0)
                for val in self.values_below:
                    signals_flat = signals_cur_stage.flatten()
                    stage_dict[f"{stage_label}_below_{val}_min"] = (signals_flat<val).sum()/fs_chan/60
            else:
                stage_dict[f'{stage_label}_saturation_avg'] = np.nan
                stage_dict[f'{stage_label}_saturation_std'] = np.nan
                stage_dict[f'{stage_label}_saturation_min'] = np.nan
                stage_dict[f'{stage_label}_saturation_max'] = np.nan
                for val in self.values_below:
                    stage_dict[f"{stage_label}_below_{val}_min"] = np.nan                           
        return stage_dict


    def compute_cycles_stats_saturation(self, sleep_cycles_df, signals):
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
                for signal in signals:
                    # Because of the discontinuity
                    # we have to verify if the signal includes at least partially the events
                    # Look for the Right windows time
                    if (signal.start_time<(start+dur)) and ((signal.start_time+signal.duration)>start): 
                        # Extract and define the new extracted channel_cur
                        channel_cur = self.extract_samples_from_events(signal, start, dur)
                        signals_cyc.append(channel_cur)
                
                # Flat signals into an array
                data_stats = np.empty(0)
                for i_bout, samples in enumerate(signals_cyc):
                    data_stats = np.concatenate((data_stats, samples), axis=0)

                #data_stats = np.round(data_stats,0) # to copy Gaétan   
                # Clean-up invalid values
                data_stats[data_stats>100]=np.nan
                data_stats[data_stats<=0]=np.nan        
                cyc_dict[f'cyc{i_cyc+1}_saturation_avg'] = np.nanmean(data_stats)
                cyc_dict[f'cyc{i_cyc+1}_saturation_std'] = np.nanstd(data_stats)
                cyc_dict[f'cyc{i_cyc+1}_saturation_min'] = np.round(np.nanmin(data_stats),0)
                cyc_dict[f'cyc{i_cyc+1}_saturation_max'] = np.round(np.nanmax(data_stats),0)
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


    def detect_desaturation(self, data_starts, data_stats, fs_chan, channel, parameters_oxy, asleep_stages_df):
        """
        Parameters :
            data_stats : numpy array
                oxygen saturation integer values from 1 to 100% 
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
                'window_link_sec' : 'The window length (s) to compute the temporal link between desaturations and arousals',
                'arousal_min_sec' : 'The minimum length (s) of the arousal events kept',
                'arousal_max_sec' : 'The maximum length (s) of the arousal events kept',
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
        """   
        for i, signal in enumerate(data_stats):
            flag_end_min = False         
            desat_start_sec = data_starts[i]
            desat_start_val = data_stats[i][0]
            cur_min_val = 100
            cur_end_sec = 0
            cur_end_val = 100
            desat_drop_reached_flag = False
            desat_valid_flag = False
            desat_tab = []
            for j, sample in enumerate(signal):
                cur_sec = data_starts[i] + j/fs_chan

                # Manage the baseline to measure the saturation before the drop
                if not desat_drop_reached_flag:
                    # previous bsl is available
                    if j > (parameters_oxy["max_slope_drop_sec"]*fs_chan):
                        bsl_start = int(round(j-(parameters_oxy["max_slope_drop_sec"]*fs_chan)))
                    else:
                        bsl_start = 0
                    # Look for the max value to start the desaturation
                    if j-bsl_start > 0:
                        max_bsl_val = np.nanmax(signal[bsl_start:j])
                        i_max_val = [i for i, val in enumerate(signal[bsl_start:j]) if val==max_bsl_val]
                        if len(i_max_val)>1:
                            max_bsl_i = np.nanmax(i_max_val)
                        elif len(i_max_val)==1:
                            max_bsl_i = i_max_val[0]
                        else:
                            max_bsl_i=j # when all nan
                        max_bsl_sec = data_starts[i] + (bsl_start+max_bsl_i)/fs_chan
                    else:
                        max_bsl_val = sample
                        max_bsl_sec = cur_sec
                    desat_start_val = max_bsl_val
                    desat_start_sec = max_bsl_sec
                
                # Look for the minimum value to end the desaturation
                else:

                    if j-(bsl_start+max_bsl_i) > 0:
                        cur_min_val = np.nanmin(signal[bsl_start+max_bsl_i:j])
                    else:
                        cur_min_val = sample
                    # Find the last sec of the minimum value (real end of the desaturation)
                    i_min_val = [i for i, val in enumerate(signal[bsl_start+max_bsl_i:j]) if val==cur_min_val]
                    if len(i_min_val)>1:
                        min_desat_i = np.nanmax(i_min_val)
                    elif len(i_min_val)==1:
                        min_desat_i = i_min_val[0]
                    else:
                        min_desat_i=j # when all nan
                    cur_min_sec = data_starts[i] + (bsl_start+max_bsl_i+min_desat_i)/fs_chan

                # --------------------------------------------------------------
                # Evaluation of the desaturation status
                # --------------------------------------------------------------
                # Drop is enough -> we have a desaturation start!
                if (not desat_drop_reached_flag) and ((desat_start_val-cur_end_val) >= parameters_oxy["desaturation_drop_percent"]):
                    desat_drop_reached_flag = True
                    desat_reached_sec = cur_sec
                    if DEBUG:
                        print(f"desaturation drop (start={desat_start_val} and current={cur_end_val}) reached at {self.convert_sec_to_HHMMSS(desat_start_sec)}")
                
                # If the drop is maintained its a valid desaturation
                if desat_drop_reached_flag: 
                    # Drop is maintained enough
                    if not desat_valid_flag and ((cur_sec - desat_reached_sec) >= parameters_oxy["min_hold_drop_sec"]):
                        desat_valid_flag = True
   
                # --------------------------------------------------------------
                # Evaluation of the desaturation value
                # --------------------------------------------------------------
                # The value inscreased of more than 2%
                if (desat_drop_reached_flag and desat_valid_flag) and (sample > cur_min_val+(self.variability_tolerance/100*cur_min_val/100)*100):

                    # Make sure the desat_start_sec is not already included in a desaturation
                    #    before adding it into the desat_tab
                    if len(desat_tab)>0:
                        last_desat = desat_tab[-1]
                        if not ( (desat_start_sec>=last_desat[0]) and (desat_start_sec<(last_desat[0]+last_desat[1]))):
                            # Save the valid desaturation
                            if flag_end_min: # The end is at the last min value
                                desat_tab.append([desat_start_sec, cur_min_sec-desat_start_sec])
                            else: # The end is at the resaturation of 2%
                                desat_tab.append([desat_start_sec, cur_end_sec-desat_start_sec])
                    else:
                        # Save the valid desaturation
                        if flag_end_min: # The end is at the last min value
                            desat_tab.append([desat_start_sec, cur_min_sec-desat_start_sec])
                        else: # The end is at the resaturation of 2%
                            desat_tab.append([desat_start_sec, cur_end_sec-desat_start_sec])
                        
                    desat_drop_reached_flag = False
                    desat_valid_flag = False
                                        
                cur_end_sec = cur_sec
                cur_end_val = sample
        
        # Keep desat that start in asleep stages only
        start_time = asleep_stages_df['start_sec'].values
        end_time = start_time + asleep_stages_df['duration_sec'].values
        desat_kept = []
        for desat_start, desat_dur in desat_tab:
            if any( (start_time<=desat_start) & (end_time>=desat_start) ):
                desat_kept.append([desat_start, desat_dur])
        desat_events = [('SpO2', 'desat_SpO2', start_sec, duration_sec, channel) for start_sec, duration_sec in desat_kept]
        return manage_events.create_event_dataframe(data=desat_events)


    def compute_desat_stats(self, desat_df, asleep_stages_df):
        desat_stats = {}
        # The number of oxygen desaturation from lights off to lights on in asleep stages only.
        desat_stats['desat_count'] = len(desat_df)
        # The average duration in sec of the oxygen desaturation events occuring in asleep stages.
        desat_stats['desat_avg_sec'] = desat_df['duration_sec'].mean()
        # The std value of the duration in sec of the oxygen desaturation events occuring in asleep stages.
        desat_stats['desat_std_sec'] = desat_df['duration_sec'].std()
        # The median value of the duration in sec of the oxygen desaturation events occuring in asleep stages.
        desat_stats['desat_med_sec'] = desat_df['duration_sec'].median()
        # The percentage of time spent in desaturation during the asleep stages.
        desat_stats['desat_sleep_percent'] = desat_df['duration_sec'].sum()/asleep_stages_df['duration_sec'].sum()*100
        # The Oxygen Desaturation Index (ODI) : number of desaturation per sleep hour.
        desat_stats['desat_ODI'] = len(desat_df)/(asleep_stages_df['duration_sec'].sum()/3600)
        return desat_stats

    
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
        else:
            temporal_stats['arousal_end_before_delay_sec'] = np.nan       
            link_arousal_end_df = manage_events.create_event_dataframe(None)

        # Concatenate all new events
        link_event_df = pd.concat([link_desat_start_df, link_desat_end_df])
        link_event_df = pd.concat([link_event_df, link_arousal_start_df])
        link_event_df = pd.concat([link_event_df, link_arousal_end_df])
        return temporal_stats, link_event_df
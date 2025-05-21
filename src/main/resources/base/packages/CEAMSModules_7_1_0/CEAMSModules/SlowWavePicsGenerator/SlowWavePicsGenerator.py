"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    SlowWavePicsGenerator
    Class to generate pictures of slow wave events.
"""
import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Qtagg')  # Use non-GUI backend
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
#import matplotlib.pyplot as plt
from scipy import signal as scipy_signal

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

from CEAMSModules.PSGReader.SignalModel import SignalModel
from CEAMSModules.PSGReader.PSGReaderManager import PSGReaderManager
from CEAMSModules.SignalsFromEvents.SignalsFromEvents import SignalsFromEvents

DEBUG = True

class SlowWavePicsGenerator(SciNode):
    """
    Class to generate pictures of slow wave events.

    Parameters
    ----------
        "files": dict
            Keys are filenames. Each file contains a montage and a list of channel to process.
        "file_group": dict
            Keys are filenames. Values are the group label.
        "sw_char_folder": str
            Path to the folder containing the slow wave characteristics files.
        "sw_events_def" : dict
            Keys are filenames and values are group and name labels for sw events.
        "ROIs_def": dict
            Keys are ROI names and values are the channels list and the blank flag.
        "chans_ROIs_sel": dict
            Keys are channel labels or ROI names and values are the selection flag.
        "pics_param": dict
            Each key is a parameter to generate pictures.
            The default values are : 
                'cohort_avg': True,
                'cohort_sel': False,
                'subject_avg': False,
                'subject_sel': False,
                'show_sw_categories': False,
                'sw_aligment' : 'ZC',
                'display': "mean_std", # all, mean, mean_std
                'neg_up': False,
                'force_axis': False, # False or [xmin, xmax, ymin, ymax]
                'output_folder': '' 
        "colors_param": dict
            Each key is a parameter to generate pictures.
            The default values are : 
                'subjectavg': ['tab:blue', 'tab:red', 'tab:green', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'],
                'subjectsel': ['tab:blue', 'tab:red', 'tab:green', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'],
                'cohortavg': ['tab:blue', 'tab:red', 'tab:green', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'],

    Returns
    -------
        
    """
    def __init__(self, **kwargs):
        """ Initialize module SlowWavePicsGenerator """
        super().__init__(**kwargs)
        if DEBUG: print('SlowWavePicsGenerator.__init__')

        # Input plugs
        InputPlug('files',self)
        InputPlug('file_group',self)
        InputPlug('sw_char_folder',self)
        InputPlug('sw_events_def',self)
        InputPlug('ROIs_def',self)
        InputPlug('chans_ROIs_sel',self)
        InputPlug('pics_param',self)
        InputPlug('colors_param',self)
        # Output plugs
        
        # These properties are needed for the PSGReader plugin 
        # (we dont use the constructor because it is a Master node
        # so we cannot instance more than once)
        self._is_master = False 

        # We use the constructor of the PSGReaderManager
        # in order to initialize the readers 
        # (usually done in the constructor of the PSGReader)
        self._psg_reader_manager = PSGReaderManager()
        self._psg_reader_manager._init_readers()

        # Properties of the module
        self.filter_freqs = [0.16, 4.0] #To filter the signal in delta
        self.filter_order = 30
        self.fs_signal = 50 # Resample the signals
        # To display the pictures
        self.figsize = (6, 4) # in inches
        # Maximum time to plot in seconds
        self.max_time_to_plot = 5

        # Associate a linestyle to each SW categories
        self.linestyles = ['-', '--', '-.', ':','dotted'] # max 4 categories

        # Associate a color to each category
        #self.markers = ['|', '_','.', 'o', 'v', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd']
        # Associate a color to each channel
        #self.colors = ['tab:blue', 'tab:red', 'tab:green', 'tab:orange','tab:purple','tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
        #self.palette_labels = ["flare", "crest", "mako", "rocket", "viridis", "plasma", "inferno", "magma", "cividis", "turbo", "twilight"]
        #self.palette_labels = ["Blues", "Reds", "Greens", "Greys", "Oranges", "Purples"] # Un groupe pâle et l'autre foncé...
        #self.palette_labels = ["copper", "cool", "summer", "winter"] # max 4 categories

    def compute(self, files, file_group, sw_char_folder, sw_events_def, ROIs_def, chans_ROIs_sel, pics_param, colors_param):
        """
        Load signals, average SW signal event if needed and generate pictures of slow wave events.

        Parameters
        ----------
            "files": dict
                Keys are filenames. Each file contains a montage and a list of channel to process.
            "file_group": dict
                Keys are filenames. Values are the group label.
            "sw_char_folder": str
                Path to the folder containing the slow wave characteristics files.
            "sw_events_def" : dict
                Keys are filnames and values are group and name labels for sw events.
            "ROIs_def": dict
                Keys are ROI names and values are the channels list and the blank flag.
            "chans_ROIs_sel": dict
                Keys are channel labels or ROI names and values are the selection flag.
            "pics_param": dict
                Each key is a parameter to generate pictures.
                The default values are : 
                    'cohort_avg': True,
                    'cohort_sel': False,
                    'subject_avg': False,
                    'subject_sel': False,
                    'show_sw_categories': False,
                    'sw_aligment' : 'ZC',
                    'display': "mean_std", # all, mean, mean_std
                    'neg_up': False,
                    'force_axis': False, # False or [xmin, xmax, ymin, ymax]
                    'output_folder': ''      
            "colors_param": dict
                Each key is a parameter to generate pictures.
                The default values are : 
                    'subjectavg': ['tab:blue', 'tab:red', 'tab:green', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'],
                    'subjectsel': ['tab:blue', 'tab:red', 'tab:green', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'],
                    'cohortavg': ['tab:blue', 'tab:red', 'tab:green', 'tab:purple', 'tab:orange', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'],
                    
        Returns
        -------

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """

        if isinstance(sw_events_def, str) and not sw_events_def=='':
            sw_events_def = eval(sw_events_def)
        if not isinstance(sw_events_def, dict):
            raise NodeInputException(self.identifier, "sw_events_def", \
                f"SlowWavePicsGenerator : dict is expected for sw_events_def and it is {type(sw_events_def)}")

        if isinstance(chans_ROIs_sel, str) and not chans_ROIs_sel=='':
            chans_ROIs_sel = eval(chans_ROIs_sel)
        if not isinstance(chans_ROIs_sel, dict):
            raise NodeInputException(self.identifier, "chans_ROIs_sel", \
                f"SlowWavePicsGenerator : dict is expected for chans_ROIs_sel and it is {type(chans_ROIs_sel)}")

        if isinstance(ROIs_def, str) and not ROIs_def=='':
            ROIs_def = eval(ROIs_def)
        if not isinstance(ROIs_def, dict):
            raise NodeInputException(self.identifier, "ROIs_def", \
                f"SlowWavePicsGenerator : dict is expected for ROIs_def and it is {type(ROIs_def)}")

        if isinstance(pics_param, str) and not pics_param=='':
            pics_param = eval(pics_param)
        if not isinstance(pics_param, dict):
            raise NodeInputException(self.identifier, "pics_param", \
                f"SlowWavePicsGenerator : dict is expected for pics_param and it is {type(pics_param)}")

        if isinstance(file_group, str) and not file_group=='':
            file_group = eval(file_group)
        if not isinstance(file_group, dict):
            raise NodeInputException(self.identifier, "file_group", \
                f"SlowWavePicsGenerator : dict is expected for file_group and it is {type(file_group)}")

        if isinstance(colors_param, str) and not colors_param=='':
            colors_param = eval(colors_param)
        if not isinstance(colors_param, dict):
            raise NodeInputException(self.identifier, "colors_param", \
                f"SlowWavePicsGenerator : dict is expected for colors_param and it is {type(colors_param)}")

        # Dict to keep the average signal per channel
        signal_avg_per_chan = {} # the key is the channel label and the value is the average signal
        # the key is the group label and the value is the average signals or min/max valid index
        #   each subject is append (each subject represents all channels averaged)
        signal_avg_cohort = {}
        idx_min_cohort = {} 
        idx_max_cohort = {}
        n_cats = 1
        for file_name in files.keys():
            file_group_name = file_group[file_name]
            #--------------------------------------------------------------
            # Extract signals from the file
            #--------------------------------------------------------------
            if (not file_name==None) and ('montages' in files[file_name]):
                montages = list(files[file_name]['montages'].keys())
                for j in range(0, len(montages)):
                    montage = montages[j]
                    if files[file_name]['montages'][montage]['is_selected']:
                        channels = files[file_name]['montages'][montage]['channels']
                        selected_channels = [label for label in list(channels.keys()) if channels[label]['is_selected']]
                        montage_index = files[file_name]['montages'][montage]['montage_index']
            # Check if the file exist
            if(not os.path.isfile(file_name)):
                raise NodeRuntimeException(self.identifier, "files", \
                    f"SlowWavePicsGenerator file not found:{file_name}")
            # Try to open the file
            success = self._psg_reader_manager.open_file(file_name)
            if not success:
                raise NodeRuntimeException(self.identifier, "files", \
                    f"SlowWavePicsGenerator could not read file:{file_name}")
            if selected_channels is not None:
                signals = self._psg_reader_manager.get_signal_models(int(montage_index), selected_channels)
            # Close the file since the signals are saved
            self._psg_reader_manager.close_file()

            #--------------------------------------------------------------
            # Band-pass filter the signals 0.16-4 Hz
            #--------------------------------------------------------------
            order_filtfilt = int(self.filter_order)/2
            # For each signal in signals, apply the filter
            signals_delta = []
            for signal_model in signals:
                signal_delta = SignalModel.clone(signal_model, clone_samples=False)
                sos = scipy_signal.butter(int(order_filtfilt), self.filter_freqs,\
                    btype='bandpass', output='sos', fs=signal_model.sample_rate)
                signal_delta.samples = scipy_signal.sosfiltfilt(sos, signal_model.samples)
                signals_delta.append(signal_delta)

            #--------------------------------------------------------------
            # Downsample the signals "signals_delta" to 64 Hz
            #   so all channels have the same sample rate
            #--------------------------------------------------------------
            for signal_model in signals_delta:
                if signal_model.sample_rate < self.fs_signal:
                    raise NodeRuntimeException(self.identifier, "signals", \
                        f"SlowWavePicsGenerator signal sample rate too low:{signal_model.sample_rate}")
                original_length = len(signal_model.samples)
                final_length = int(round(original_length * self.fs_signal / signal_model.sample_rate))
                signal_model.samples = scipy_signal.resample(signal_model.samples, final_length)
                signal_model.sample_rate = self.fs_signal
                signal_model.duration = final_length / signal_model.sample_rate
                signal_model.end_time = signal_model.start_time + signal_model.duration

            #--------------------------------------------------------------
            # Extract slow wave characteristics
            #--------------------------------------------------------------
            # Open the slow wave characteristics file
            sw_label = sw_events_def[file_name]['name']
            base_name = os.path.basename(file_name)
            base_name = os.path.splitext(base_name)[0]+'_'+sw_label
            # Check if the file exist
            sw_char_filename = sw_char_folder+'/'+base_name+'.tsv'
            if(not os.path.isfile(sw_char_filename)):
                raise NodeRuntimeException(self.identifier, "files", \
                    f"SlowWavePicsGenerator file not found:{sw_char_filename}")  
            # Import events into df
            sw_char_subject = pd.read_csv(sw_char_filename, sep='\t', \
                header=0, engine='python', encoding = 'utf_8') 
            # Select the events
            if isinstance(sw_events_def[file_name]['group'],str):
                sw_char_subject_sw_sel = sw_char_subject[ \
                    (sw_char_subject['group']==sw_events_def[file_name]['group']) \
                & (sw_char_subject['name']==sw_events_def[file_name]['name']) ]
            elif isinstance(sw_events_def[file_name]['group'],list): 
                sw_char_subject_sw_sel = sw_char_subject[\
                    sw_char_subject['group'].isin(sw_events_def[file_name]['group']) \
                    & (sw_char_subject['name'].isin(sw_events_def[file_name]['name']))]

            #--------------------------------------------------------------
            # Generate the pictures
            #--------------------------------------------------------------
            signals_evt_all_chan = []
            sw_char_subject_all_chan = []
            chan_label_all_chan = []
            # For each channel in chans_ROIs_sel dict
            for ch in chans_ROIs_sel.keys():
                # if the channel is selected
                if chans_ROIs_sel[ch]:

                    # Extract the sw characterstics for the current channel or ROI.
                        # If the ROI has the blank option and at least one channel is missing None will be returned
                    sw_char_subject_ch_sel = self.extract_sw_char_ch(sw_char_subject_sw_sel, ch, ROIs_def)
                    if len(sw_char_subject_ch_sel)>0:
                        sw_char_subject_all_chan.append(sw_char_subject_ch_sel)
                    else:
                        self._log_manager.log(self.identifier, f"No slow wave characteristics for {file_name} channel {ch}.")
                        continue                        

                    # Select the signal for each event
                    if sw_char_subject_ch_sel is not None and len(sw_char_subject_ch_sel) > 0:
                        # Extract the unique list of channels from sw_char_subject_ch_sel
                        chan_list_cur_chan = sw_char_subject_ch_sel['channels'].unique().tolist()
                        # Extract the signal for each event
                        signals_evt_cur_chan = self.extract_signal_for_events_ch_roi(\
                            signals_delta, chan_list_cur_chan, sw_char_subject_ch_sel)
                        
                        if len(signals_evt_cur_chan) == 0:
                            self._log_manager.log(self.identifier, f"No signal for {file_name} channel {ch}.")
                            continue

                        # Generate the pictures
                        if "roi" in ch.lower():
                            # Keep as roi label all characters before [
                            chan_label = ch[:ch.index('[')]
                        else:
                            chan_label = ch
                        chan_label_all_chan.append(chan_label)

                        # **********************************************
                        # One figure for the current subject : one picture per channel or ROI
                        # **********************************************
                        if pics_param['subject_sel'] | pics_param['cohort_sel']:
                            # Save figure for a subject and a channel.
                            # This function display all the signals for the events included in event_cur_chan_df.
                            #   return the average signal for each category for the current channel and subject
                            if pics_param['subject_sel']:
                                fig_save = 'subject_sel'
                            else:
                                fig_save = False
                            signal_avg_per_chan_cat, min_x_idx, max_x_idx, max_cats = \
                                self._save_subject_chan_fig_sw(signals_evt_cur_chan, \
                                    sw_char_subject_ch_sel, pics_param, base_name, \
                                        chan_label, fig_save, colors_param['subject_sel'])
                            if chan_label in signal_avg_per_chan.keys():
                                signal_avg_per_chan[chan_label].append(\
                                    [signal_avg_per_chan_cat, min_x_idx, max_x_idx, file_group_name])
                            else:
                                signal_avg_per_chan[chan_label] = \
                                    [[signal_avg_per_chan_cat, min_x_idx, max_x_idx, file_group_name]]
                            if fig_save:
                                self._log_manager.log(self.identifier, \
                                    f"Images are generatef for the file {file_name} and channel\ROI {ch}.")

                            n_cats = max(n_cats, max_cats)

                        if pics_param['subject_avg'] | pics_param['cohort_avg']:
                            signals_evt_all_chan.append(signals_evt_cur_chan)

            # **********************************************
            # One figure for the current subject : one picture for all channels
            # **********************************************
            if pics_param['subject_avg'] | pics_param['cohort_avg']:
                # Function to save figure for a subject and a list of channels.
                # This function display all the signals_evt_all_chan for the events included in sw_char_subject_all_chan.
                #   return the average signal for each category for the current subject
                if pics_param['subject_avg']:
                    fig_save = 'subject_avg'
                else:
                    fig_save = False
                if len(chan_label_all_chan)>1:
                    colors = colors_param['subject_avg']
                else:
                    # If there is only one channel, differentiate the categories by color.
                    colors = colors_param['subject_sel']
                if (len(signals_evt_all_chan)>0) and (len(sw_char_subject_all_chan)>0):
                    # signal_avg_per_cat : numpy array
                    #     Average signal for each category for the current subject
                    # min_x_idx : int
                    #     Index of the minimum time on x axis for the current subject.
                    # max_x_idx : int
                    #     Index of the maximum time on x axis for the current subject.
                    # max_cat : int
                    #     The number of categories for the current subject
                    signal_avg_per_cat, min_x_idx, max_x_idx, max_cats = \
                        self._save_subject_chan_fig_sw(signals_evt_all_chan, sw_char_subject_all_chan, \
                            pics_param, base_name, chan_label_all_chan, fig_save, colors)

                    if fig_save:
                        self._log_manager.log(self.identifier, \
                            f"The image is generatef for the file {file_name} for all channels.")

                    n_cats = max(n_cats, max_cats)
                else:
                    # signal_avg_per_cat : numpy array
                    #     Average signal for each category for the current subject
                    # min_x_idx : int
                    #     Index of the minimum time on x axis for the current subject.
                    # max_x_idx : int
                    #     Index of the maximum time on x axis for the current subject.
                    # max_cat : int
                    #     The number of categories for the current subject
                    n_cats = 1
                    signal_avg_per_cat = np.empty(0)
                    min_x_idx = max_x_idx = 0

            # Accumulate data for one picture for all channels
            # Accumulate data for each sbject
            if pics_param['cohort_avg']:
                # To save figure for the cohort
                #   group_dict_avg : dict, where the key is the group label
                if file_group_name in signal_avg_cohort.keys():
                    # The signal averaged is appended only if it exist
                    if len(signal_avg_per_cat)>0:
                        signal_avg_cohort[file_group_name].append(signal_avg_per_cat)
                        idx_min_cohort[file_group_name].append(min_x_idx)
                        idx_max_cohort[file_group_name].append(max_x_idx)
                else:
                    # The signal averaged is appended only if it exist
                    if len(signal_avg_per_cat)>0:
                        signal_avg_cohort[file_group_name] = [signal_avg_per_cat]
                        idx_min_cohort[file_group_name] = [min_x_idx]
                        idx_max_cohort[file_group_name] = [max_x_idx]

        # -> all subjects are run

        # **********************************************
        # One figure for the cohort : one picture per channel
        # **********************************************
        if pics_param['cohort_sel']:
            # For each channel in chans_ROIs_sel dict
            for ch, sig_idx_grp in signal_avg_per_chan.items():
                # For each subject accumulate data
                # signal_avg is a numpy array of the number of groups
                #   Each item is a list of signals 
                # Need to be able to split the group (different plot on the same picture)
                signal_avg = {}
                idx_max = {}
                idx_min = {}
                for signal_avg_cur_sjt, idx_min_sjt, idx_max_sjt, group_cur_sjt in sig_idx_grp:
                    if not (group_cur_sjt in signal_avg.keys()):
                        if len(signal_avg_cur_sjt)>0:
                            signal_avg[group_cur_sjt] = [signal_avg_cur_sjt]
                            idx_max[group_cur_sjt] = [idx_max_sjt]
                            idx_min[group_cur_sjt] = [idx_min_sjt]
                    else:
                        if len(signal_avg_cur_sjt)>0:
                            signal_avg[group_cur_sjt].append(signal_avg_cur_sjt)
                            idx_max[group_cur_sjt].append(idx_max_sjt)
                            idx_min[group_cur_sjt].append(idx_min_sjt)
            
                # signal_avg : for the current channel -> one signal per subject,
                #  they need to be aligned together
                self._save_cohort_chan_fig_sw(signal_avg, idx_min, idx_max, \
                    pics_param, sw_label, ch, self.fs_signal, n_cats, colors_param['cohort'])

        # **********************************************
        # One figure for the cohort : one picture for all channels
        # **********************************************
        if pics_param['cohort_avg']:
            self._save_cohort_chan_fig_sw(signal_avg_cohort, idx_min_cohort, \
                idx_max_cohort, pics_param, sw_label, '', self.fs_signal, n_cats, colors_param['cohort'])

        return {
        }


    def extract_signal_for_events_ch_roi(self, signals, channels, event_cur_chan_df):
        """""
            Extract signal for each event in event_cur_chan_df for the list of channels.

            Parameters
            -----------
                signals             : List of SignalModel
                    List of all signals (all channels)
                channels             : string or list of string
                    Label of the selected channel
                event_cur_chan_df : pandas DataFrame (columns=['group', 'name','start_sec','duration_sec','channels'])  
                    List of events.

            Returns
            -----------  
                signals_evt_cur_chan : list of numpy array
                    The samples of each spindle (filtered in sigma)

        """""
        # For each channel in channels if channels is a list
        if isinstance(channels, str):
            channels = [channels]

        # Extract signal from the list of events
        signals_evt_cur_chan = []
        for channel in channels:
            # Extract the events for the current channel (important for ROIs)
            sel_channel_event_cur_chan_df = event_cur_chan_df[event_cur_chan_df['channels']==channel]
            evt_start_times = sel_channel_event_cur_chan_df['start_sec'].to_numpy().astype(float)   # numpy array
            evt_dur_times = sel_channel_event_cur_chan_df['duration_sec'].to_numpy().astype(float)  # numpy array
            # Extract signals for the current channel as list of SignalModel
            if SignalModel.get_attribute(signals, None, 'channel', channel) is not None :
                signals_cur_chan = SignalModel.get_attribute(signals, None, 'channel', channel).tolist()
                # Extract start_time of the signals for the current channel as numpy array
                signals_starttime = SignalModel.get_attribute(signals_cur_chan, 'start_time', 'start_time').flatten()
                # Extract end_time of the signals for the current channel as numpy array
                signals_endtime = SignalModel.get_attribute(signals_cur_chan, 'end_time', 'end_time').flatten()
            else:
                signals_cur_chan = []
                signals_starttime = []
                signals_endtime = []

            for evt_start, evt_dur in zip(evt_start_times, evt_dur_times):
                # Find in within signal the event is included
                evt_start_in_signal = signals_starttime < (evt_start+evt_dur)
                evt_end_in_signal = signals_endtime > evt_start
                evt_sel_in_signal = evt_start_in_signal & evt_end_in_signal
                # Only one signal should include the event since the signals are splitted in continuous bouts (not stages)
                if sum(evt_sel_in_signal)==1:
                    signal_sel = np.nonzero(evt_sel_in_signal)[0][0]
                    fs_signal = signals_cur_chan[signal_sel].sample_rate
                    evt_start_samples = int(np.round(evt_start*fs_signal))
                    evt_dur_samples = int(np.round(evt_dur*fs_signal))
                    # Extract and define the new extracted channel_cur
                    signal_evt_tmp = SignalsFromEvents.extract_events_from_signal(SignalsFromEvents, signals_cur_chan[signal_sel], evt_start_samples, evt_dur_samples)
                    signals_evt_cur_chan.append(signal_evt_tmp.samples)
                # elif sum(evt_sel_in_signal)==0:
                #     # Log message for the Logs tab, too many log message when the channel is missing.
                #     # self._log_manager.log(self.identifier, f"SlowWavePicsGenerator sw event not included in the signals")
                #     pass
                elif sum(evt_sel_in_signal)>1:
                    raise NodeRuntimeException(self.identifier, "signals", \
                        f"SlowWavePicsGenerator sw included in many signals")                
        return signals_evt_cur_chan


    # def _open_fig_sw(self, signals_evt_cur_chan, event_cur_chan_df):
    #     """""
    #         Debug function to open figure in a dialog. 
    #         This funciton display all the signals for the events included in event_cur_chan_df.
    #     """""
    #     from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
    #     from matplotlib.figure import Figure
    #     from PySide6.QtWidgets import QDialog, QVBoxLayout


    #     dialog = QDialog()
    #     fig = Figure(figsize=(self.figsize), dpi=100)
    #     canvas = FigureCanvas(fig)
    #     # Find the max duration of the events to prepare the time axis
    #     max_evt_dur = max(event_cur_chan_df['duration_sec'].values)
    #     longuest_evt = np.argmax(event_cur_chan_df['duration_sec'].values)
    #     n_samples = len(signals_evt_cur_chan[longuest_evt])
    #     fs_chan = n_samples/max_evt_dur
    #     time = np.arange(0,max_evt_dur,1/fs_chan)
    #     ax = fig.add_subplot(111)
    #     # For each signal in signals_evt_cur_chan
    #     for i, signal_cur in enumerate(signals_evt_cur_chan):
    #         signal_no_offset = signal_cur-np.mean(signal_cur)
    #         # Pad the end of the signal with nans
    #         signal_to_plot = np.concatenate((signal_no_offset, np.nan*np.ones(len(time)-len(signal_no_offset))))
    #         ax.plot(time,signal_to_plot,'k',alpha=0.1)
    #     ax.set_xlabel('time (s)')
    #     layout = QVBoxLayout()
    #     layout.addWidget(canvas)
    #     dialog.setLayout(layout)
    #     dialog.exec_()


    def _save_subject_chan_fig_sw(self, signals_evt_all_chan, event_all_chan_df, pics_param, base_name, chan_label, fig_save, colors):
        """""
            Function to save figure for a subject.
            This function display all the signals for the events included in event_all_chan_df.

            Parameters
            -----------
                signals_evt_all_chan : list of numpy array or list of list of numpy array
                    List of signals for the events included in event_all_chan_df
                event_all_chan_df : pandas dataframe or list of pandas dataframe
                    List of events for the current channel
                fig_name : str
                    Path to save the figure
                pics_param: dict
                    Each key is a parameter to generate pictures.
                    The default values are : 
                        'cohort_avg': True,
                        'cohort_sel': False,
                        'subject_avg': False,
                        'subject_sel': False,
                        'show_sw_categories': False,
                        'sw_aligment' : 'ZC',
                        'display': "mean_std", #"mean", "all", "mean_std"
                        'force_axis': False, # False or [xmin, xmax, ymin, ymax]
                        'output_folder': ''    
                chan_label : str or list of str
                    List of labels for the current channel
                fig_save : str or bool
                    The type (label) of figure to save. If false, the figure is not saved.
                colors : list of str
                    List of colors.
            Returns 
            -------
                signal_avg_per_cat : numpy array
                    Average signal for each category for the current subject
                min_x_idx : int
                    Index of the minimum time on x axis for the current subject.
                max_x_idx : int
                    Index of the maximum time on x axis for the current subject.
                max_cat : int
                    The number of categories for the current subject

        """""
        if fig_save:
            if 'subject' in fig_save:
                # Initialize the figure and canvas for plotting
                fig = Figure()
                fig.set_size_inches(self.figsize)
                fig.clear() # reset the hold on
                ax = fig.add_subplot()

        
        if isinstance(chan_label, str):
            signals_evt_all_chan = [signals_evt_all_chan]
            event_all_chan_df = [event_all_chan_df]
            chan_label = [chan_label]

        n_channels = len(signals_evt_all_chan)
        fs_chan = self.fs_signal
    
        # We align the signals to the time=0
        time = np.arange(-self.max_time_to_plot/2,self.max_time_to_plot/2,1/fs_chan)
        # Find the index of the time=0
        idx_time_0 = np.where(time>=0)[0][0]

        # For each channel compute the maximum index to delay the signals
        max_x_idx = 0
        min_x_idx = len(time)
        max_duration_pos = 0
        max_duration_tot = 0
        max_duration_neg = 0
        max_cat = 1
        idx_neg_peak_all_chan = []
        idx_pos_peak_all_chan = []
        idx_zc_all_chan = []
        for i_chan in range(n_channels):

            # Extract the signals for the current channel
            signals_evt_cur_chan = signals_evt_all_chan[i_chan]
            # Extract the events for the current channel
            event_cur_chan_df = event_all_chan_df[i_chan]

            # Extract the Zero Crossing time of each event
            zc_time_evts_cur_chan = event_cur_chan_df['neg_sec'].values # in seconds
            idx_zc_evts_cur_chan = np.round(zc_time_evts_cur_chan*fs_chan).astype(int) # index

            # Used to compute the first and last valid index (to limit the x-axis)
            max_dur_pos_cur_chan = max(event_cur_chan_df['pos_sec'].values)
            max_dur_tot_cur_chan = max(event_cur_chan_df['duration_sec'].values)
            max_dur_neg_cur_chan = max(event_cur_chan_df['neg_sec'].values)
            max_duration_pos = max(max_duration_pos, max_dur_pos_cur_chan)
            max_duration_tot = max(max_duration_tot, max_dur_tot_cur_chan)
            max_duration_neg = max(max_duration_neg, max_dur_neg_cur_chan)

            # When confirming the zero-crossing point, the delay is removed (nice!) but many events have the wrong delay (really bad!)
            #   so it is better to take the neg_sec value as zero-crossing point
            idx_zc_all_chan.append(idx_zc_evts_cur_chan)

            if pics_param['sw_aligment'] == 'NP':
                # Find the index of the negative peak (Not included in the slow wave characteristics events)
                idx_neg_peak = []
                for i_evt, signal_evt in enumerate(signals_evt_cur_chan):
                    idx_neg_peak.append(np.argmin(signal_evt[0:idx_zc_evts_cur_chan[i_evt]+1]))
                # Find the maximum index of all the negative peaks
                idx_neg_peak_all_chan.append(idx_neg_peak)

            elif pics_param['sw_aligment'] == 'PP':
                # Find the index of the positive peak in time (Not included in the slow wave characteristics events)
                idx_pos_peak = []
                for i_evt, signal_evt in enumerate(signals_evt_cur_chan):
                    cur_pos_peak_in_pos = np.argmax(signal_evt[idx_zc_evts_cur_chan[i_evt]-1:]).astype(int)
                    idx_pos_peak.append(cur_pos_peak_in_pos+idx_zc_evts_cur_chan[i_evt])
                # Find the maximum index of all the positive peaks
                idx_pos_peak_all_chan.append(idx_pos_peak)
            
            if 'category' in event_cur_chan_df.columns and pics_param['show_sw_categories']:
                # Find the maximum category number
                max_cat_cur_chan = max(event_cur_chan_df['category'].values)
            else: 
                max_cat_cur_chan = 1
            max_cat = max(max_cat, max_cat_cur_chan)

        # List of averaged signals, one item per slow wave category
        signal_avg_per_cat = np.empty(0)
        legend_labels = {}

        # # Define a color palette based on the n_cats and the number of channels
        # palette_list = []
        # if max_cat>1:
        #     for i_cat in range(max_cat):
        #         palette = sns.color_palette(self.palette_labels[i_cat], n_channels)
        #         palette_list.append(palette)
            
        # Create a list of sw category from 1 to max_cat
        sw_category = list(range(1,max_cat+1))
        # For each sw category display signal with a specific marker
        for i_cat in sw_category:
            #signal_accum_to_avg = np.empty((len(time),1))
            signal_accum_to_avg = np.empty(0)

            # For each channel display the signals
            for i_chan in range(n_channels):
                # Extract the signals for the current channel
                signals_evt_cur_chan = signals_evt_all_chan[i_chan]
                # Extract the events for the current channel
                event_cur_chan_df = event_all_chan_df[i_chan]

                # Extract the Zero Crossing time of each event
                if pics_param['sw_aligment'] == 'ZC':
                    idx_zc = idx_zc_all_chan[i_chan]

                # Extract the negative peak of the events for the current channel
                elif pics_param['sw_aligment'] == 'NP':
                    idx_neg_peak = idx_neg_peak_all_chan[i_chan]

                # Extract the Positive peak of the events for the current channel
                elif pics_param['sw_aligment'] == 'PP':
                    idx_pos_peak = idx_pos_peak_all_chan[i_chan]

                # Display the mean of the signals accross events and the std as shaded gray area
                if 'mean' in pics_param['display']:
                    signal_to_plot_cat = np.empty(0)
                    # For each signal in signals_evt_cur_chan
                    for i_evt, signal_cur in enumerate(signals_evt_cur_chan):
                        if ('category' not in event_cur_chan_df.columns) or \
                            ( (pics_param['show_sw_categories'] and ('category' in event_cur_chan_df.columns)) and (event_cur_chan_df['category'].values[i_evt] == i_cat) ) or \
                                (pics_param['show_sw_categories'] == False):
                            signal_cur_cat = signal_cur
                        else:
                            signal_cur_cat= None
                        if signal_cur_cat is not None:
                            if pics_param['sw_aligment'] == 'ZC':
                                # pad with zeros the beginning of the signal to move the zero-crossing of the event to the idx_max_neg_dur index
                                signal_pad_start = np.concatenate((np.zeros(idx_time_0-idx_zc[i_evt]), signal_cur_cat))
                                last_valid_idx = idx_time_0 + int(round(max_duration_pos*fs_chan))
                                first_valid_idx = idx_time_0 - int(round(max_duration_neg*fs_chan))

                            elif pics_param['sw_aligment'] == 'NP':
                                # pad with zeros the beginning of the signal to move the negative peak of the event to the idx_max_neg_peak index
                                signal_pad_start = np.concatenate((np.zeros(idx_time_0-idx_neg_peak[i_evt]), signal_cur_cat))
                                last_valid_idx = idx_time_0 + int(round(max_duration_tot*fs_chan))
                                first_valid_idx = idx_time_0 - int(round(max_duration_neg*fs_chan))

                            elif pics_param['sw_aligment'] == 'PP':
                                # pad with zeros the beginning of the signal to move the positive peak of the event to the idx_max_pos_peak index
                                signal_pad_start = np.concatenate((np.zeros(idx_time_0-idx_pos_peak[i_evt]), signal_cur_cat))
                                last_valid_idx = idx_time_0 + int(round(max_duration_pos*fs_chan))
                                first_valid_idx = idx_time_0 - int(round(max_duration_tot*fs_chan))

                            # Pad the end of the signal with zeros to match the length of the time axis (until 3 sec long)
                            signal_pad_end = np.concatenate((signal_pad_start, np.zeros(len(time)-len(signal_pad_start))))
                            # Reshape signal_to_plot to have 2D array of shape (n_samples, 1)
                            signal_to_plot = signal_pad_end.reshape(-1,1)
                            # concatenate the current signal to all signals for the current category and channel
                            #   in order to display the mean and std for the current subject
                            if len(signal_to_plot_cat) == 0:
                                signal_to_plot_cat = signal_to_plot
                            else:
                                signal_to_plot_cat = np.concatenate((signal_to_plot_cat, signal_to_plot), axis=1)
                            # Compute the max index valid for all the sw events
                            max_x_idx = max(last_valid_idx,max_x_idx)
                            min_x_idx = min(first_valid_idx,min_x_idx)
                           
                            # Concatenate signals for all channels and the current category
                            #   in order to output the mean for the current subject (for each category)
                            if len(signal_accum_to_avg)==0:
                                signal_accum_to_avg = signal_to_plot
                            else:
                                signal_accum_to_avg = np.concatenate((signal_accum_to_avg, signal_to_plot), axis=1)

                    # Display the mean of the signals accross events
                    signal_avg_chan_cat = np.nanmean(signal_to_plot_cat, axis=1)

                    if fig_save:
                        # Check if the label has already been added to the legend
                        if f'cat{i_cat}-{chan_label[i_chan]}' not in legend_labels:
                            # Plot the mean with a specific color and linestyle
                            # Multiple channels and multiple categories
                            if (max_cat>1 and n_channels>1):
                                #ax.plot(time, signal_avg_chan_cat, color=palette_list[i_cat-1][i_chan], linestyle=self.linestyles[i_cat-1], label=f'cat{i_cat}-{chan_label[i_chan]}')
                                ax.plot(time, signal_avg_chan_cat, color=colors[i_chan], linestyle=self.linestyles[i_cat-1], label=f'cat{i_cat}-{chan_label[i_chan]}')
                            # Only one channel to plot
                            elif max_cat>1:
                                ax.plot(time, signal_avg_chan_cat, color=colors[i_cat-1], label=f'cat{i_cat}-{chan_label[i_chan]}')
                            # Only one category to plot
                            else:
                                ax.plot(time, signal_avg_chan_cat, color=colors[i_chan], label=f'cat{i_cat}-{chan_label[i_chan]}')
                            # Add the label to the legend
                            legend_labels[f'cat{i_cat}-{chan_label[i_chan]}']=True
                        else:
                            # Plot the mean with a specific color and linestyle
                            # Multiple channels and multiple categories
                            if (max_cat>1 and n_channels>1):
                                #ax.plot(time, signal_avg_chan_cat, color=palette_list[i_cat-1][i_chan], linestyle=self.linestyles[i_cat-1], label=f'cat{i_cat}-{chan_label[i_chan]}')
                                ax.plot(time, signal_avg_chan_cat, color=colors[i_chan], linestyle=self.linestyles[i_cat-1])
                            # Only one channel to plot
                            elif max_cat>1:
                                ax.plot(time, signal_avg_chan_cat, color=colors[i_cat-1])
                            # Only one category to plot
                            else:
                                ax.plot(time, signal_avg_chan_cat, color=colors[i_chan])

                        if 'std' in pics_param['display']:
                            # Display the standard deviation of the signals accross events as shaded area
                            # Calculate the standard deviation of the signals
                            signal_to_plot_std = np.nanstd(signal_to_plot_cat, axis=1)
                            # Multiple channels and multiple categories
                            if (max_cat>1 and n_channels>1):
                                ax.fill_between(time, signal_avg_chan_cat - signal_to_plot_std, \
                                    signal_avg_chan_cat + signal_to_plot_std, color=colors[i_chan], linestyle=self.linestyles[i_cat-1], alpha=0.2) 
                            # Only one channel to plot
                            elif max_cat>1:
                                ax.fill_between(time, signal_avg_chan_cat - signal_to_plot_std, \
                                    signal_avg_chan_cat + signal_to_plot_std, color=colors[i_cat-1], alpha=0.2)
                            # Only one category to plot
                            else:
                                ax.fill_between(time, signal_avg_chan_cat - signal_to_plot_std, \
                                    signal_avg_chan_cat + signal_to_plot_std, color=colors[i_chan], alpha=0.2)                                                    

                # Display all signals accross events
                # Always only one channel
                else:
                    # For each signal in signals_evt_cur_chan
                    for i_evt, signal_cur in enumerate(signals_evt_cur_chan):
                        if ('category' not in event_cur_chan_df.columns) or \
                            ( (pics_param['show_sw_categories'] and ('category' in event_cur_chan_df.columns)) and (event_cur_chan_df['category'].values[i_evt] == i_cat) ) or \
                                (pics_param['show_sw_categories'] == False):
                            signal_cur_cat = signal_cur
                        else:
                            signal_cur_cat= None
                        if signal_cur_cat is not None:
                            if pics_param['sw_aligment'] == 'ZC':
                                # pad with zeros the beginning of the signal to move the zero-crossing of the event to the idx_max_neg_dur index
                                signal_pad_start = np.concatenate((np.nan*np.ones(idx_time_0-idx_zc[i_evt]), signal_cur_cat))
                                # Zero pad to compute properly the average (for the cohort data)
                                signal_zeros_pad_start = np.concatenate((np.zeros(idx_time_0-idx_zc[i_evt]), signal_cur_cat))
                                last_valid_idx = idx_time_0 + int(round(max_duration_pos*fs_chan))
                                first_valid_idx = idx_time_0 - int(round(max_duration_neg*fs_chan))

                            elif pics_param['sw_aligment'] == 'NP':
                                # pad with zeros the beginning of the signal to move the negative peak of the event to the idx_max_neg_peak index
                                signal_pad_start = np.concatenate((np.nan*np.ones(idx_time_0-idx_neg_peak[i_evt]), signal_cur_cat))
                                # Zero pad to compute properly the average (for the cohort data)
                                signal_zeros_pad_start = np.concatenate((np.zeros(idx_time_0-idx_neg_peak[i_evt]), signal_cur_cat))
                                last_valid_idx = idx_time_0 + int(round(max_duration_tot*fs_chan))
                                first_valid_idx = idx_time_0 - int(round(max_duration_neg*fs_chan))

                            elif pics_param['sw_aligment'] == 'PP':
                                # pad with zeros the beginning of the signal to move the positive peak of the event to the idx_max_pos_peak index
                                signal_pad_start = np.concatenate((np.nan*np.ones(idx_time_0-idx_pos_peak[i_evt]), signal_cur_cat))
                                # Zero pad to compute properly the average (for the cohort data)
                                signal_zeros_pad_start = np.concatenate((np.zeros(idx_time_0-idx_pos_peak[i_evt]), signal_cur_cat))
                                last_valid_idx = idx_time_0 + int(round(max_duration_pos*fs_chan))
                                first_valid_idx = idx_time_0 - int(round(max_duration_tot*fs_chan))

                            # Pad the end of the signal with zeros to match the length of the time axis (until 3 sec long)
                            signal_pad_end = np.concatenate((signal_pad_start, np.nan*np.ones(len(time)-len(signal_pad_start))))
                            # Zero pad to compute properly the average (for the cohort data)
                            signal_zero_pad_end = np.concatenate((signal_zeros_pad_start, np.zeros(len(time)-len(signal_zeros_pad_start))))

                            if (np.nanmax(signal_pad_end)>10000) and DEBUG:
                                print(f"i_event={i_evt}, cat{i_cat} max val={np.nanmax(signal_pad_end)}")
                            
                            if fig_save:
                                # Check if the label has already been added to the legend
                                if f'cat{i_cat}-{chan_label[i_chan]}' not in legend_labels:
                                    # Add the label to the legend
                                    legend_labels[f'cat{i_cat}-{chan_label[i_chan]}']=True
                                    ax.plot(time, signal_pad_end, color=colors[i_cat-1], alpha=0.5, label=f'cat{i_cat}-{chan_label[i_chan]}')
                                else:
                                    ax.plot(time, signal_pad_end, color=colors[i_cat-1],alpha=0.1)
                            # Compute the max index valid for all the sw events
                            max_x_idx = max(last_valid_idx,max_x_idx)
                            min_x_idx = min(first_valid_idx,min_x_idx)

                            # Concatenate signals for all channels and the current category
                            #   in order to output the mean for the current subject (for each category)
                            signal_to_plot = signal_zero_pad_end.reshape(-1,1)
                            if len(signal_accum_to_avg)==0:
                                signal_accum_to_avg = signal_to_plot
                            else:
                                signal_accum_to_avg = np.concatenate((signal_accum_to_avg, signal_to_plot), axis=1)
                
            # Average the signals for all channels and the current category
            #   in order to output the mean for the current subject (for each category)
            if len(signal_avg_per_cat)==0: # i_cat=0 (all channels have been processed)
                signal_avg_per_cat = np.nanmean(signal_accum_to_avg, axis=1)
                signal_avg_per_cat = signal_avg_per_cat.reshape(-1,1)
            else:
                signal_avg_temp = np.nanmean(signal_accum_to_avg, axis=1)
                # each new cat is concatened on the 2nd dimension
                signal_avg_per_cat = np.concatenate((signal_avg_per_cat, signal_avg_temp.reshape(-1,1)), axis=1) 

        # If the function is used to generate pictures
        if fig_save:
            if pics_param['subject_avg'] | pics_param['subject_sel']:
                fig_name = pics_param['output_folder']+'/'+base_name+'_'+pics_param['sw_aligment']
                if pics_param['subject_sel']:
                    fig_name = fig_name + '_' + chan_label[0]
                fig_name = fig_name + '_'+ pics_param['display']
                fig_name = fig_name + '.pdf'

                if pics_param['subject_sel']:
                    fig_title = base_name+ '_' + chan_label[0]
                if pics_param['subject_avg']:
                    fig_title = base_name

                if pics_param['force_axis']:
                    ax.set_xlim(pics_param['force_axis'][0], pics_param['force_axis'][1])
                    ax.set_ylim(pics_param['force_axis'][2], pics_param['force_axis'][3])
                else:
                    ax.set_xlim(time[min_x_idx],time[max_x_idx])

                if pics_param['neg_up']:
                    ax.invert_yaxis()

                ax.set_xlabel('Time (s)')
                ax.set_ylabel('Amplitude (uV)')
                if ('category' in event_cur_chan_df.columns) or n_channels>1:
                    ax.legend(loc='upper left')
                ax.grid(which='both', axis='both')
                ax.set_title(fig_title)
                try :
                    fig.savefig(fig_name)
                except:
                    raise NodeRuntimeException(self.identifier, "files", f"Error while saving figure {fig_name}, make sure it is not open")
                if DEBUG:
                    print(f"{fig_name} is saved")
                fig.clf()
            # close the figure
            #plt.close(fig)

        return signal_avg_per_cat, min_x_idx, max_x_idx, max_cat


    def extract_sw_char_ch(self, sw_char_subject_sw_sel, ch, ROIs_def):

        """""
            Extract the sw characterstics for the current channel or ROI.
            If the ROI has the blank option and at least one channel is missing None will be returned

            Parameters
            -----------
                sw_char_subject_sw_sel : pandas dataframe
                    List of events for the current subject
                ch : string
                    Label of the selected channel or ROI
                ROIs_def : dict
                    Definition of the ROIs (keys are ROI label and values are the channels list and the blank flag)
            Returns
            -----------  
                sw_char_subject_ch_sel : pandas dataframe
                    List of events for the current channel or ROI
        """""
        # Verify if it is an ROI
        if "roi" in ch.lower():
            # Select the events for all the channels included in the ROI
            chan_lst = ROIs_def[ch][0]
            blank_flag = ROIs_def[ch][1]
            # When the blank flag is set, all the channels must be present in the file
            miss_ch = False
            if blank_flag:
                for roi_ch in chan_lst:
                    cur_sel = sw_char_subject_sw_sel[sw_char_subject_sw_sel['channels']==roi_ch]
                    if len(cur_sel)==0:
                        miss_ch = True
            if blank_flag and miss_ch:
                sw_char_subject_ch_sel = None
            else:
                sw_char_subject_ch_sel = []
                for roi_ch in chan_lst:
                    if len(sw_char_subject_ch_sel)==0:
                        sw_char_subject_ch_sel = sw_char_subject_sw_sel[sw_char_subject_sw_sel['channels']==roi_ch]
                    else:
                        sw_char_subject_ch_sel = pd.concat([sw_char_subject_ch_sel, sw_char_subject_sw_sel[sw_char_subject_sw_sel['channels']==roi_ch]], ignore_index=True)
        else:
            sw_char_subject_ch_sel = sw_char_subject_sw_sel[sw_char_subject_sw_sel['channels']==ch]
        return sw_char_subject_ch_sel


    def _save_cohort_chan_fig_sw(self, signal_avg, idx_min, idx_max, pics_param, sw_label, chan_label, fs_chan, n_cats, colors):
        """""
            Save the cohort figure for the current channel or ROI

            Parameters
            -----------
                signal_avg : dict of list of numpy array
                    keys are the subject group and values are the average signal for the current channel or ROI
                    values are a list of number of sw categories
                idx_min : dict of float
                    keys are the subject group and values are the min index for the current subject or channel or ROI
                idx_max : dict of float
                    keys are the subject group and values are the max index for the current subject or channel or ROI
                pics_param : dict
                    keys are the parameter to generate pictures
                sw_label : string
                    Label of the slow wave event detected
                chan_label : string
                    Label of the selected channel or ROI (can be empty)
                fs_chan : float
                    Sampling frequency of the selected channel or ROI
                n_cats : int
                    Number of slow wave categories
            Returns
            -----------  
                None
        """""
        # Define the figure name
        if chan_label=='':
            fig_name = pics_param['output_folder']+'/'+sw_label+'_'+pics_param['sw_aligment']+'_' + pics_param['display']+'.pdf'
            fig_title = sw_label
        else:
            fig_name = pics_param['output_folder']+'/'+sw_label+'_'+chan_label+'_'+pics_param['sw_aligment']+'_' + pics_param['display']+'.pdf'
            fig_title = sw_label+'_'+chan_label

        # Create the figure
        fig = Figure()
        fig.set_size_inches(self.figsize)
        fig.clear() # reset the hold on
        ax = fig.add_subplot()
        legend_labels = {}

        time = np.arange(-self.max_time_to_plot/2,self.max_time_to_plot/2,1/fs_chan)

        # Create the unique list of keys of signal_avg
        group_list = list(set(signal_avg.keys()))
        # # Define a color palette based on the n_cats and the number of groups
        # palette_list = []
        # if n_cats>1:
        #     for i_cat in range(n_cats):
        #         palette = sns.color_palette(self.palette_labels[i_cat], len(group_list))
        #         palette_list.append(palette)

        # signal_to_plot_grp : dict of list of numpy array
        #         keys are the subject group and values are the average signal for the current channel or ROI
        #         values are a list of number of sw categories
        signal_to_plot_grp = {} 

        # For each group of the cohort
        for i_grp, cohort_group in enumerate(group_list):
            # For each subject
            n_subjects = len(signal_avg[cohort_group])
            for i_sjt in range(n_subjects):
                n_cats = signal_avg[cohort_group][i_sjt].shape[1]
                # For each sw category
                for i_cat in range(n_cats):
                    # Extract the average signal for each sw category
                    signal_cat_zero = signal_avg[cohort_group][i_sjt][:, i_cat]
                    # Replace the heading zeros with nans from the beginning to idx_min[cohort_group][i_sjt]
                    signal_cat_nan = signal_avg[cohort_group][i_sjt][:, i_cat].copy()
                    signal_cat_nan[:idx_min[cohort_group][i_sjt]] = np.nan
                    # Replace the tailing zeros with nans from the idx_max[cohort_group][i_sjt] to the end
                    signal_cat_nan[idx_max[cohort_group][i_sjt]:] = np.nan
                    # Reshape signal_to_plot to have 2D array of shape (n_samples, 1)
                    signal_to_plot = signal_cat_nan.reshape(-1,1)
                    signal_to_mean = signal_cat_zero.reshape(-1,1)
                    if 'mean' in pics_param['display']:
                        # concatenate the current signal to all signals
                        if cohort_group in signal_to_plot_grp.keys():
                            if f'cat{i_cat+1}' in signal_to_plot_grp[cohort_group].keys():
                                signal_to_plot_grp[cohort_group][f'cat{i_cat+1}'] = np.concatenate((signal_to_plot_grp[cohort_group][f'cat{i_cat+1}'], signal_to_mean), axis=1)
                            else:
                                signal_to_plot_grp[cohort_group][f'cat{i_cat+1}'] = signal_to_mean
                        else:
                            signal_to_plot_grp[cohort_group]={}
                            signal_to_plot_grp[cohort_group][f'cat{i_cat+1}'] = signal_to_mean
                    else:
                        # Check if the label has already been added to the legend
                        if f'cat{i_cat+1}-{cohort_group}' not in legend_labels:
                            # Add the label to the legend
                            legend_labels[f'cat{i_cat+1}-{cohort_group}']=True
                            # Plot the channels with a specific linestyle and the categories with a specific color
                            if n_cats>1:
                                ax.plot(time, signal_to_plot, color=colors[i_grp], linestyle=self.linestyles[i_cat], label=f'cat{i_cat+1}-{cohort_group}', alpha=0.5)
                            else:
                                ax.plot(time, signal_to_plot, color=colors[i_grp], label=f'cat{i_cat+1}-{cohort_group}', alpha=0.5)
                            #ax.plot(time, signal_to_plot, color=self.colors[i_cat*n_cats+i_grp], linestyle=self.linestyles[i_grp], label=f'cat{i_cat+1}-{cohort_group}', alpha=0.5)
                        else:
                            # Plot the channels with a specific linestyle and the categories with a specific color
                            #ax.plot(time, signal_to_plot, color=self.colors[i_cat], linestyle=self.linestyles[i_grp], alpha=0.5)
                            if n_cats>1:
                                #ax.plot(time, signal_to_plot, color=palette_list[i_cat][i_grp], alpha=0.5)
                                ax.plot(time, signal_to_plot, color=colors[i_grp], linestyle=self.linestyles[i_cat], alpha=0.5)
                            else:
                                ax.plot(time, signal_to_plot, color=colors[i_grp], alpha=0.5)
                            #ax.plot(time, signal_to_plot, color=self.colors[i_cat*n_cats+i_grp], linestyle=self.linestyles[i_grp], alpha=0.5)

        # Average signal to plot mean and gray area
        x_lim_max = 0
        x_lim_min = len(time)
        for i_grp, cohort_group in enumerate(group_list):
            for i_cat in range(n_cats):
                if 'mean' in pics_param['display']:
                    # Average the signals signal_to_plot_cat to get the mean signal
                    signal_to_plot_mean = np.nanmean(signal_to_plot_grp[cohort_group][f'cat{i_cat+1}'], axis=1)
                    # Compute the standard deviation
                    signal_to_plot_std = np.nanstd(signal_to_plot_grp[cohort_group][f'cat{i_cat+1}'], axis=1)
                    # Plot the channels with a specific linestyle and the categories with a specific color
                    #ax.plot(time, signal_to_plot_mean, color=self.colors[i_cat], linestyle=self.linestyles[i_grp], label=f'cat{i_cat+1}-{cohort_group}')
                    if n_cats>1:
                        ax.plot(time, signal_to_plot_mean, color=colors[i_grp],\
                         linestyle=self.linestyles[i_cat], label=f'cat{i_cat+1}-{cohort_group}')
                        if 'std' in pics_param['display']:
                            # Plot the channels with a specific linestyle and the categories with a specific color
                            # ax.fill_between(time, signal_to_plot_mean - signal_to_plot_std, signal_to_plot_mean + signal_to_plot_std,\
                            #     color=self.colors[i_cat], linestyle=self.linestyles[i_grp], alpha=0.3)
                            ax.fill_between(time, signal_to_plot_mean - signal_to_plot_std, \
                                signal_to_plot_mean + signal_to_plot_std, color=colors[i_grp], linestyle=self.linestyles[i_cat], alpha=0.3)
                    else:
                        ax.plot(time, signal_to_plot_mean, color=colors[i_grp], label=f'{cohort_group}')
                        if 'std' in pics_param['display']:
                            # Plot the channels with a specific linestyle and the categories with a specific color
                            # ax.fill_between(time, signal_to_plot_mean - signal_to_plot_std, signal_to_plot_mean + signal_to_plot_std,\
                            #     color=self.colors[i_cat], linestyle=self.linestyles[i_grp], alpha=0.3)
                            ax.fill_between(time, signal_to_plot_mean - signal_to_plot_std, \
                                signal_to_plot_mean + signal_to_plot_std, color=colors[i_grp], alpha=0.3)

        # Set the limits of the x axis
        x_lim_max = 0
        x_lim_min = len(time)-1
        for i_grp, cohort_group in enumerate(group_list):
            # For each subject
            n_subjects = len(signal_avg[cohort_group])
            for i_sjt in range(n_subjects):
                x_lim_max = max(idx_max[cohort_group][i_sjt],x_lim_max)
                x_lim_min = min(idx_min[cohort_group][i_sjt],x_lim_min)        

        if pics_param['force_axis']:
            ax.set_xlim(pics_param['force_axis'][0], pics_param['force_axis'][1])
            ax.set_ylim(pics_param['force_axis'][2], pics_param['force_axis'][3])
        else:
            ax.set_xlim(time[x_lim_min],time[x_lim_max])

        if pics_param['neg_up']:
            ax.invert_yaxis()

        ax.grid(which='both', axis='both')
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Amplitude (uV)')
        # set the legend to the upper left
        ax.legend(loc="upper left")
        ax.set_title(fig_title)
        if pics_param['cohort_avg'] | pics_param['cohort_sel']:
            try :
                fig.savefig(fig_name)
            except:
                raise NodeRuntimeException(self.identifier, "files", f"Error while saving figure {fig_name}, make sure it is not open")
            if DEBUG:
                print(f"{fig_name} is saved...")
            fig.clf()
        #plt.close(fig)
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Results viewer of the SpindleDetectorA7 plugin
"""
import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from qtpy import QtWidgets
from qtpy import QtGui

from widgets.WarningDialog import WarningDialog
from CEAMSModules.PSGReader.SignalModel import SignalModel
from CEAMSModules.SignalsFromEvents.Ui_SignalsFromEventsResultsView import Ui_SignalsFromEventsResultsView

class SpindleDetectorA7ResultsView(Ui_SignalsFromEventsResultsView, QtWidgets.QWidget):
    """
        SpindleDetectorA7ResultsView display the features extracted from the channel to detect spindles
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(SpindleDetectorA7ResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        self.disk_cache = {}

        # init UI
        self.setupUi(self)

        # Create the figure : https://matplotlib.org/2.1.2/api/axes_api.html
        self.figure = Figure(constrained_layout=False) #To use tight layout
        # Add the figure tool bar
        self.canvas = FigureCanvas(self.figure)
        toolbar = NavigationToolbar(self.canvas, self)    
        # Add the figure into the result_layout
        self.result_layout.addWidget(toolbar)
        self.result_layout.addWidget(self.canvas)   

        self._y_limits = None
        self._max_length_sec = 30


    def load_results(self):      

        # Clear the cache from the loaded file, usefull for the second run
        self.disk_cache = {}

        # Read result cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)

        if cache is not None:       
            # Get the data needed from the cache
            self.n_chan = cache['n_chan'] # maximum nb of channels
            self.signals = cache['signals']
            self.events = cache['events']
            if not isinstance(self.signals,list):
                self.signals = [self.signals]
            #self.signals_events = SignalModel.get_attribute(self.signals, None, 'start_time')
            # self.start_events = np.unique(SignalModel.get_attribute(self.signals, 'start_time', 'start_time'), axis=1)
            # self.duration_events = np.unique(SignalModel.get_attribute(self.signals, 'duration', 'start_time'), axis=1)

            # Split the signals to have 30 sec duration if the signal is longer than 30 sec
            self.signals_split = []
            for signal in self.signals:
                signal_split = signal.clone()
                signal_cur_start = signal_split.start_time
                signal_end = signal_split.start_time + signal.duration
                if signal.duration > self._max_length_sec:
                    while signal_cur_start < signal_end:
                        signal_split = signal.clone()
                        signal_split.duration = min(self._max_length_sec, signal_end - signal_cur_start)
                        signal_split.start_time = signal_cur_start
                        signal_split.end_time = signal_cur_start + signal_split.duration
                        offset_samples = round((signal_cur_start-signal.start_time)*signal.sample_rate)
                        signal_split.samples = signal.samples[offset_samples:offset_samples+round(signal_split.duration*signal.sample_rate)].copy()
                        self.signals_split.append(signal_split)
                        # Prepare for the next window
                        signal_cur_start = signal_split.end_time
                else:
                    signal_split.samples = signal.samples.copy()
                    self.signals_split.append(signal_split)

            # get_attribute(signals, attr, group_by, value_to_test=None):
            self.signals_events = SignalModel.get_attribute(self.signals_split, None, 'start_time')
            self.start_events = np.unique(SignalModel.get_attribute(self.signals_split, 'start_time', 'start_time'), axis=1)
            self.duration_events = np.unique(SignalModel.get_attribute(self.signals_split, 'duration', 'start_time'), axis=1)

            # Set first window
            self.index = 0
            self.prev_but.setEnabled(False)
            self.start = self.start_events[self.index][0]
            self.duration = self.duration_events[self.index][0]

            # extract events based on the self.start and self.duration
            # Define self.current_events
            self._get_events()

            # Create a list of SignalModel for all the channels with the selected start_sec from the event
            self.signal_event = self.signals_events[self.index]

            # Update event
            self._update_event_info()

            # Plot first signal
            self._plot_det_info()

            # Desable the button if its impossible to press the button another time.
            self.prev_but.setEnabled(False)
            if self.index + 1 > (len(self.signals_events) - 1):
                self.next_but.setEnabled(False)
            else:
                self.next_but.setEnabled(True)

        else:
            # When the cache is erased, dont show signals
            self.figure.clear()
            self.canvas.draw()

    def _update_event_info( self):

         # Fill info for first signal
        if self.duration>self._max_length_sec:
            self.duration_lineEdit.setText(str(self._max_length_sec))
        else:
            self.duration_lineEdit.setText(str(self.duration))
        self.event_index_lineEdit.setText(str(self.index))

        # Set the time elapsed
        nhour = int(self.start/3600)
        sec_tmp = self.start-nhour*3600
        nmin = int(sec_tmp/60)
        nsec = self.start-nhour*3600-nmin*60
        time_elapsed = "{0:02d}:{1:02d}:{2:0.2f}".format(nhour,nmin,nsec)
        self.time_lineedit.setText(time_elapsed)


    def on_event_index_changed( self):
        if int(self.event_index_lineEdit.text()) >= 0 and int(self.event_index_lineEdit.text()) <= (len(self.signals_events) - 1):
            self.index = int(self.event_index_lineEdit.text())
            self._on_navigate()
        else:
            self.event_index_lineEdit.setText(str(self.index))
            print("Error index outside of range")


    # Called when the user uncheck/check the checkBox_ylim_norm or finish editing the lineEdit_ylim_fixed
    def y_limits_change_slot(self):
        # The line edit is enabled if the checkBox_ylim_norm is not checked
        self.lineEdit_ylim_fixed.setEnabled(not self.checkBox_ylim_norm.isChecked())
        y_limits = self.lineEdit_ylim_fixed.text()
        # evaluate the string to be number only (no letters)
        try: 
            y_limits = float(y_limits)
            self._y_limits = y_limits
            self._plot_det_info()
        except:
            WarningDialog("Please enter a single number as y-axis limits (symmetric axis)")
            self.lineEdit_ylim_fixed.setText('')
            self._y_limits = None
        

    def _plot_det_info( self):
        """ 
        Plot eeg signal and detection info.
        use self.signal_event : Dictionnary of SignalModel
                A dictionary of channels with SignalModel with properties :
                name:          The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording

        """
        
        # Manage the figure
        self.figure.clear() # reset the hold on 

        #----------------------------------------------------------------------
        # Plot eeg signal
        n_chan = self.n_chan
        gs = self.figure.add_gridspec(n_chan, hspace=0)
        ax1 = gs.subplots(sharex=True, sharey=False)
        chan_sel = 0

        for signal in self.signal_event:
            fs = signal.sample_rate
            chan_name = signal.channel

            # Cannot plot too long vector 
            if self.duration > self._max_length_sec:
                duration = self._max_length_sec
                signal.samples = signal.samples[0:int(fs*duration)]
                #self.current_events = self.current_events[self.current_events['start_sec']<duration]
            else:
                duration = self.duration

            # Define the y-axis limits
            if (not self.checkBox_ylim_norm.isChecked()) and (self._y_limits is not None):
                ylim=[-self._y_limits,self._y_limits]
            else:
                ylim=[np.nanmin(signal.samples), np.nanmax(signal.samples)]

            # Add vertical lines for sec
            nsec = int(duration)
            for sec_i in range(nsec):
                if n_chan>1:
                    ax1[chan_sel].vlines(x=sec_i, ymin=ylim[0],ymax=ylim[1], linewidth=0.5, color='k', linestyles='--') 
                else:
                    ax1.vlines(x=sec_i, ymin=ylim[0],ymax=ylim[1], linewidth=0.5, color='k', linestyles='--')      

            # Add horizontal lines at zeros and the threshold if available
            if n_chan>1:
                ax1[chan_sel].hlines(y=0, xmin=0, xmax=duration, linewidth=0.5, color='k', linestyles='--')
                # Verify if there meta is defined as a dict with a key called 'threshold'
                if isinstance(signal.meta, dict) and 'threshold' in signal.meta.keys():
                    ax1[chan_sel].hlines(y=signal.meta['threshold'], xmin=0, xmax=duration, linewidth=0.5, color='r', linestyles='-')
            else:
                ax1.hlines(y=0, xmin=0, xmax=duration, linewidth=0.5, color='k', linestyles='--')
                # Verify if there meta is defined as a dict with a key called 'threshold'
                if isinstance(signal.meta, dict) and 'threshold' in signal.meta.keys():
                    ax1.hlines(y=signal.meta['threshold'], xmin=0, xmax=duration, linewidth=0.5, color='r', linestyles='-')

            # Plot the signals
            time_vect = np.linspace(0, duration, num = int(fs*duration))
            if n_chan>1:
                ax1[chan_sel].plot(time_vect, signal.samples[0:int(fs*duration)], 'b', linewidth=1, alpha=0.75)
            else:
                ax1.plot(time_vect, signal.samples[0:int(fs*duration)], 'b', linewidth=1, alpha=0.75)             

            # Plot the events as a rectangle from start_sec to start_sec+duration_sec
            if not self.current_events.empty:
                cur_chan_events = self.current_events[self.current_events['channels']==chan_name]
                for i in range(len(cur_chan_events)):
                    x_edge = cur_chan_events.iloc[i]['start_sec']
                    height = np.max([abs(np.array(ylim))])
                    width = cur_chan_events.iloc[i]['duration_sec']
                    if n_chan>1:
                        ax1[chan_sel].add_patch(plt.Rectangle((x_edge, -height), width, 2*height, color='g', alpha=0.3))
                    else:
                        ax1.add_patch(plt.Rectangle((x_edge, -height), width, 2*height, color='g', alpha=0.3))

            if n_chan>1:
                ax1[chan_sel].set_ylabel(chan_name, loc='center', rotation=0, labelpad=30)
                ax1[chan_sel].set_xlabel('time [s]')
                ax1[chan_sel].set_xlim((time_vect[0], time_vect[-1]))
                ax1[chan_sel].set_ylim(ylim)

                if not self.checkBox_display_y.isChecked():
                    # Turn off tick labels
                    ax1[chan_sel].set_yticklabels([])
            else:
                ax1.set_ylabel(chan_name, loc='center', rotation=0, labelpad=30)
                ax1.set_xlabel('time [s]')
                ax1.set_xlim((time_vect[0], time_vect[-1]))
                ax1.set_ylim(ylim)
                if not self.checkBox_display_y.isChecked():
                    # Turn off tick labels
                    ax1.set_yticklabels([])

            chan_sel += 1

        # Hide x labels and tick labels for all but bottom plot.
        if n_chan>1:
            for ax in ax1:
                ax.label_outer()

        # Add suptitle
        #self.figure.suptitle(signal.alias + ' From Events')
        # Redraw the figure, needed when the show button is pressed more than once
        self.canvas.draw()


    def on_next_button( self):
        """A slot called when >> button is pressed by the user.
        The user wants to display the following window.
        """  
        self._on_navigate(next_on=1)


    def on_prev_button( self):
        """A slot called when << button is pressed by the user.
        The user wants to display the previous window.
        """    
        self._on_navigate(next_on=-1)


    def _on_navigate(self, next_on=0):
        ''' Call when the user presses the >>, << or enter after editing the time.
        '''

        # Change index of event
        self.index = self.index + next_on
        self.start = self.start_events[self.index][0]
        self.duration = self.duration_events[self.index][0]

        # extract events based on the self.start and self.duration
        # Define self.current_events
        self._get_events()

        # Create a list of SignalModel for all the channels with the selected start_sec from the event
        self.signal_event = self.signals_events[self.index]       

        # Update event
        self._update_event_info()
        
        # Desable the button if its impossible to press the button another time.
        if self.index - 1 < 0:
            self.prev_but.setEnabled(False)
        else:
            self.prev_but.setEnabled(True)
        if self.index + 1 > (len(self.signals_events) - 1):
            self.next_but.setEnabled(False)
        else:
            self.next_but.setEnabled(True)

        # Plot eeg signal.
        self._plot_det_info()


    def update_y_axis_label_slot(self):
        # Plot eeg signal with the update checkbox to display or not y axis label.
        self._plot_det_info()


    # Extract MORs events that occur in the selected time window
    # Create a list of events self.MORs = columns=['group', 'start_sec', 'peak_sec', 'peak_amplitude', 'duration_sec','channels']
    def _get_events(self):
        events = self.events[(self.events['start_sec'] >= self.start) &\
             ( (self.events['start_sec']+self.events['duration_sec']) <= (self.start + self.duration))]
        offset_start = events['start_sec'] - self.start
        group = events['group'].values
        duration_sec = events['duration_sec'].values
        channels = events['channels'].values
        # Convert to pandas data frame
        self.current_events = pd.DataFrame({'group': group, 'start_sec': offset_start, \
                'duration_sec': duration_sec, 'channels': channels})
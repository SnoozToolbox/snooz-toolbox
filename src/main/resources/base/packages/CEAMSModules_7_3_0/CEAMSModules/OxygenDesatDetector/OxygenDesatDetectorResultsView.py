"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    Results viewer of the OxygenDesatDetector plugin
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

from CEAMSModules.EventReader import manage_events
from CEAMSModules.OxygenDesatDetector.Ui_OxygenDesatDetectorResultsView import Ui_OxygenDesatDetectorResultsView
from CEAMSModules.PSGReader.SignalModel import SignalModel


class OxygenDesatDetectorResultsView(Ui_OxygenDesatDetectorResultsView, QtWidgets.QWidget):
    """
        OxygenDesatDetectorResultsView nohting to show.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(OxygenDesatDetectorResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)

        self.disk_cache = {}

        # Create the figure : https://matplotlib.org/2.1.2/api/axes_api.html
        self.figure = Figure(constrained_layout=False) #To use tight layout
        # Add the figure tool bar
        self.canvas = FigureCanvas(self.figure)
        toolbar = NavigationToolbar(self.canvas, self)    
        # Add the figure into the result_layout
        self.result_layout.addWidget(toolbar)
        self.result_layout.addWidget(self.canvas)   

        self._y_limits = None


    def load_results(self):
        # Clear the cache from the loaded file, usefull for the second run
        self.disk_cache = {}

        # Read result cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)

        if cache is not None:       
            # Get the data needed from the cache
            self.signal_raw = cache['signal_raw']
            self.signal_lpf = cache['signal_lpf']
            self.signal_hpf = cache['signal_hpf']
            self.desat_df = cache['desat_df']
            self.plateau_df = cache['plateau_df']
            self.lmax_sec = cache['lmax_sec']
            self.lmin_sec = cache['lmin_sec']
            self.fs = self.signal_raw.sample_rate

            # Update the time elapsed based on the loaded data
            self._update_time_elapsed(self.signal_raw.start_time)
            # Init self.start_to_plot
            self.get_start_time_to_plot()

            # Set first window
            # Convert the text from the combobox to int
            self.duration = int(self.comboBox_duration.currentText())
            
            # Get the signals to plot
            self.get_signals()

            # Get the events to plot
            self.get_events()

            # Update event
            self._plot_det_info()
        else:
            # When the cache is erased, dont show signals
            self.figure.clear()
            self.canvas.draw()


    def _update_time_elapsed( self, start_time):
        # Set the time elapsed
        nhour = int(start_time/3600)
        sec_tmp = start_time-nhour*3600
        nmin = int(sec_tmp/60)
        nsec = start_time-nhour*3600-nmin*60
        time_elapsed = "{0:02d}:{1:02d}:{2:0.2f}".format(nhour,nmin,nsec)
        self.time_lineedit.setText(time_elapsed)

    def duration_change_slot(self):
        # Convert the text from the combobox to int
        self.duration = int(self.comboBox_duration.currentText())
        # Get the signals to plot
        self.get_signals()
        # Get the events to plot
        self.get_events()
        # Update plot
        self._plot_det_info()

    def time_elapsed_change_slot(self):
        self.get_start_time_to_plot()
        # Get the signals to plot
        self.get_signals()
        # Get the events to plot
        self.get_events()
        # Update plot
        self._plot_det_info()

    def get_start_time_to_plot(self):
        # Get the time elapsed from the lineedit
        time_text = self.time_lineedit.text()
        try:
            time_parts = time_text.split(':')
            if len(time_parts) == 3:
                nhour = int(time_parts[0])
                nmin = int(time_parts[1])
                nsec = float(time_parts[2])
                self.start_to_plot = nhour*3600 + nmin*60 + nsec
        except ValueError:
            self.start_to_plot = self.signal_raw.start_time

    def y_limits_change_slot(self):
        self._y_limits = int(self.lineEdit_ylim_fixed.text())
        self._plot_det_info()

    def y_limit_enable_slot(self):
        self.lineEdit_ylim_fixed.setEnabled(not self.checkBox_ylim_norm.isChecked())

    # called when the user check/uncheck "Display y axis"
    # it forces a redraw of the figure
    def y_label_slot(self):
        self._plot_det_info()
        
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
        n_chan = len(self.signals)
        gs = self.figure.add_gridspec(n_chan, hspace=0)
        ax1 = gs.subplots(sharex=True, sharey=False)
        chan_sel = 0

        for signal in self.signals:
            fs = signal.sample_rate
            chan_name = signal.channel

            # Define the y-axis limits
            if (not self.checkBox_ylim_norm.isChecked()) and (self._y_limits is not None):
                ylim=[self._y_limits,100]
            else:
                # compute the limits ignoring nan
                ylim = [np.nanmin(signal.samples), np.nanmax(signal.samples)]
                # If min and max are equal are nan, set default limits
                if np.isnan(ylim[0]) or np.isnan(ylim[1]):
                    ylim = [50, 100]

            duration = self.duration

            # Add vertical lines for sec for small durations
            if duration<=60:
                nsec = int(duration)
                for sec_i in range(nsec):
                    if n_chan>1:
                        ax1[chan_sel].vlines(x=sec_i, ymin=ylim[0],ymax=ylim[1], linewidth=0.5, color='k', linestyles='--') 
                    else:
                        ax1.vlines(x=sec_i, ymin=ylim[0],ymax=ylim[1], linewidth=0.5, color='k', linestyles='--')      

            # Add horizontal lines at zeros
            if n_chan>1:
                ax1[chan_sel].hlines(y=0, xmin=0, xmax=duration, linewidth=0.5, color='k', linestyles='--')
            else:
                ax1.hlines(y=0, xmin=0, xmax=duration, linewidth=0.5, color='k', linestyles='--')

            # Plot the signals
            time_vect = np.linspace(0, duration, num = int(fs*duration))
            if n_chan>1:
                ax1[chan_sel].plot(time_vect, signal.samples[0:int(fs*duration)], 'b', linewidth=1, alpha=0.75)
            else:
                ax1.plot(time_vect, signal.samples[0:int(fs*duration)], 'b', linewidth=1, alpha=0.75)             

            if n_chan>1:
                ax1[chan_sel].set_ylabel(chan_name, loc='center', rotation=0, labelpad=30)
                ax1[chan_sel].set_xlabel('time [s]')
                ax1[chan_sel].set_xlim((time_vect[0], time_vect[-1]))
                ax1[chan_sel].set_ylim(ylim)
                ax1[chan_sel].grid(True, which='major', linestyle='-', linewidth=1.0, alpha=0.8)
                ax1[chan_sel].grid(True, which='minor', linestyle='--', linewidth=0.5, alpha=0.4)
                ax1[chan_sel].minorticks_on()

                if not self.checkBox_display_y.isChecked():
                    # Turn off tick labels
                    ax1[chan_sel].set_yticklabels([])
            else:
                ax1.set_ylabel(chan_name, loc='center', rotation=0, labelpad=30)
                ax1.set_xlabel('time [s]')
                ax1.set_xlim((time_vect[0], time_vect[-1]))
                ax1.set_ylim(ylim)
                ax1.grid(True, which='major', linestyle='-', linewidth=1.0, alpha=0.8)
                ax1.grid(True, which='minor', linestyle='--', linewidth=0.5, alpha=0.4)
                ax1.minorticks_on()
                if not self.checkBox_display_y.isChecked():
                    # Turn off tick labels
                    ax1.set_yticklabels([])

            # Add rectangles for desaturation events or markers for min max
            for index, row in self.events.iterrows():
                event_start = row['start_sec']
                event_duration = row['duration_sec']
                event_start_to_plot = event_start - self.start_to_plot

                # Check if the event is within the plotted window
                if (event_start >= self.start_to_plot) and (event_start <= (self.start_to_plot + self.duration)):
                    if row['name']=='lmax_SpO2' or row['name']=='lmin_SpO2':
                        # Add red markers for lmax and blue markers for lmin
                        if row['name']=='lmax_SpO2':
                            color_marker='red'
                        else:
                            color_marker='blue'
                        if n_chan>1:
                            ax1[chan_sel].plot(event_start_to_plot, signal.samples[int(event_start_to_plot*fs)], \
                                    'o', color=color_marker, alpha=0.3, markersize=8)
                        else:
                            ax1.plot(event_start_to_plot, signal.samples[int(event_start_to_plot*fs)], \
                                     'o', color=color_marker, alpha=0.3, markersize=8)

                    else:
                        if row['name']=='desat_SpO2':
                            color_rec='green'
                        elif row['name']=='recovery_SpO2':
                            color_rec='blue'
                        elif row['name']=='plateau_SpO2':
                            color_rec='yellow'
                        elif row['name']=='art_SpO2':
                            color_rec='red' # artifact
                        if n_chan>1:
                            ax1[chan_sel].axvspan(event_start_to_plot, event_start_to_plot + event_duration, color=color_rec, alpha=0.3)
                        else:
                            ax1.axvspan(event_start_to_plot, event_start_to_plot + event_duration, color=color_rec, alpha=0.3)

            chan_sel += 1

        # Hide x labels and tick labels for all but bottom plot.
        if n_chan>1:
            for ax in ax1:
                ax.label_outer()

        # Add suptitle
        #self.figure.suptitle(signal.alias + ' From Events')
        # Redraw the figure, needed when the show button is pressed more than once
        self.canvas.draw()

    def get_signals(self):
        # Extract the samples to plot
        signal_raw = self.signal_raw.clone(clone_samples=True)
        signal_lpf = self.signal_lpf.clone(clone_samples=True)
        signal_hpf = self.signal_hpf.clone(clone_samples=True)
        start_samples = int(self.start_to_plot*self.fs) - int(self.signal_raw.start_time*self.fs)
        end_samples = int((self.start_to_plot - self.signal_raw.start_time + self.duration)*self.fs)
        
        if start_samples > signal_raw.samples.shape[0]:
            start_samples = signal_raw.samples.shape[0]
            self.start_to_plot = start_samples/self.fs
        if end_samples > signal_raw.samples.shape[0]:
            end_samples = signal_raw.samples.shape[0]
        
        # Create arrays filled with NaN
        n_samples = int(self.duration * self.fs)
        raw_filled = np.full(n_samples, np.nan)
        lpf_filled = np.full(n_samples, np.nan)
        hpf_filled = np.full(n_samples, np.nan)
        
        # Copy available samples into the NaN-filled arrays
        available_samples = end_samples - start_samples
        if available_samples > 0:
            raw_filled[:available_samples] = signal_raw.samples[start_samples:end_samples]
            lpf_filled[:available_samples] = signal_lpf.samples[start_samples:end_samples]
            hpf_filled[:available_samples] = signal_hpf.samples[start_samples:end_samples]
        
        signal_raw.samples = raw_filled
        signal_lpf.samples = lpf_filled
        signal_hpf.samples = hpf_filled
        
         # Store the signals to plot
        self.signals = [signal_raw, signal_lpf, signal_hpf]


    def get_events(self):
        # Extract the events from the dataframe that needed to be plotted
        # the set of events are from self.desat_df and self.plateau_df
        # Filter events based on the current time window

        # Create events for the maximum and minimum markers based on self.lmax_sec and self.lmin_sec
        lmax_events = []
        for lmax_time in self.lmax_sec:
            if lmax_time>=self.start_to_plot and lmax_time<=(self.start_to_plot + self.duration):
                lmax_events.append({'group': "SpO2", 'name':'lmax_SpO2', 'start_sec':lmax_time, 'duration_sec':0, 'channels':""})
        lmin_events = []
        for lmin_time in self.lmin_sec:
            if lmin_time>=self.start_to_plot and lmin_time<=(self.start_to_plot + self.duration):
                lmin_events.append({'group': "SpO2", 'name':'lmin_SpO2', 'start_sec':lmin_time, 'duration_sec':0, 'channels':""})
        # Create a dataframe for lmax and lmin events
        lmax_df = manage_events.create_event_dataframe(data=lmax_events)
        lmin_df = manage_events.create_event_dataframe(data=lmin_events)

        # Combine all the events into a single dataframe
        self.events = self.desat_df[self.desat_df['start_sec']>=self.start_to_plot]
        if len(self.plateau_df)>0:
            self.events = pd.concat([self.events,self.plateau_df[self.plateau_df['start_sec']>=self.start_to_plot]],ignore_index=True)
        self.events = self.events[self.events['start_sec']<=(self.start_to_plot + self.duration)]
        if len(lmax_df)>0:
            self.events = pd.concat([self.events,lmax_df],ignore_index=True)
        if len(lmin_df)>0:
            self.events = pd.concat([self.events,lmin_df],ignore_index=True)
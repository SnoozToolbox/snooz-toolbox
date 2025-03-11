"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the DetectionView plugin
"""

from typing import Text
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

from qtpy import QtWidgets

from CEAMSModules.DetectionView.Ui_DetectionViewResultsView import Ui_DetectionViewResultsView


class DetectionViewResultsView( Ui_DetectionViewResultsView, QtWidgets.QWidget):
    """
        DetectionViewResultsView display the EEG signal and detection information
         from SpeDetectionView into a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        
        super(DetectionViewResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager
        
        self.filename = ''
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
        

    def load_results(self):

        # Clear the cache from the loaded file, usefull for the second run
        self.disk_cache = {}

        # Read result cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)

        if cache is not None:            
            # Get the data needed from the cache
            time_elapsed = cache['time_elapsed']
            win_len_show = cache['win_len_show']
            signal_model = cache['signal_model'] 
            signal_i = cache['signal_i']
            n_signals_chan = cache['n_signals_chan']
            fs = signal_model.sample_rate
            events = cache['events']
            det_act_smp = cache['det_act_smp']
            if 'bsl_smp' in cache.keys():
                bsl_smp = cache['bsl_smp']
            else:
                bsl_smp = None
            threshold = cache['threshold']
            median_use = cache['median_use']
            self.filename = cache['filename']
            ts_extracted = signal_model.samples.copy()

            # Plot eeg signal and detection info.
            self._plot_det_info(time_elapsed, win_len_show, ts_extracted, \
                signal_model, events, det_act_smp, threshold, \
                    median_use, bsl_smp, event_name=None)

            # Make the file selection ready 
            self.filename_lineedit_2.setText(self.filename)
            self.time_lineedit.setText(time_elapsed)

            # Enable navigation button
            nhour, nmin, nsec = time_elapsed.split(':')
            winshow_start_sec = int(nhour) * 3600 + int(nmin) * 60 + float(nsec)
            # Desable the button if its impossible to press the button another time.
            if ((winshow_start_sec - win_len_show)<signal_model.start_time) and signal_i==0:
                self.prev_but.setEnabled(False)
            else:
                self.prev_but.setEnabled(True)
            if ((winshow_start_sec + win_len_show)>signal_model.end_time) and signal_i==(n_signals_chan-1):
                self.next_but.setEnabled(False)
            else:
                self.next_but.setEnabled(True)
        else:
            # When the cache is erased, dont show signals
            self.figure.clear()
            self.canvas.draw()


    def _plot_det_info( self, time_elapsed, win_len_show, ts_extracted, \
        signal_model, events, det_act_smp, threshold, median_use, bsl_smp=None,\
            event_name=None):
        """ 
        Plot eeg signal and detection info.

        Parameters
        -----------
            time_elapsed    : string "HH:MM:S.S"
                Time elapsed since the beginning of the recording to show.
            win_len_show    : double
                Window length in sec to show.
            ts_extracted     : ndarray
                Time series of the eeg chan to display
            signal_model     : SignalModel
                signal_model.sample_rate is the sampling rate of the signal.
                signal_model.name is the channel label.
            events          : Pandas DataFrame
                DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])   
            det_act_smp    : ndarray of length of ts_extracted
                Spectral power in the frequency bins from low_freq to high_freq. 
            threshold : double
                The threshold to detect events.
            median_use : bool
                The relative threshold is 'x times the baseline median' otherwise the 
                threshold is 'x times the baseline standard deviation'                
            bsl_smp     : ndarray of length of ts_extracted (or [2 x len(ts_extracted)])
                median_use==True : Median spectral power of the baseline window (low_freq to high_freq).
                median_use==False : Mean and standard deviation of the baseline spectral power 
                (low_freq to high_freq). row1: mean, row2: std.
            event_name      : string
                Event name of the current detector.  
                (optional, can be None if all events are displayed)

        @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)

        Log : 
            2021-04-27 : First release, klacourse
            2021-05-04 : Managed Fixed Spectral Detector, klacourse
            2022-03-31 : works with list of SignalModel (section of signals)

        """
        # Create the time vector to plot
        chan_sel = signal_model.channel
        fs = signal_model.sample_rate
        nhour, nmin, nsec = time_elapsed.split(':')
        winshow_start_sec = int(nhour) * 3600 + int(nmin) * 60 + float(nsec)
        time_vect = np.linspace(0, win_len_show, num = int(fs*win_len_show))

        # Manage the figure
        self.figure.clear() # reset the hold on 
        gs = self.figure.add_gridspec(5, 1)

        #----------------------------------------------------------------------
        # Plot eeg signal      
        ax1 = self.figure.add_subplot(gs[0:2])        
        ax1.plot(time_vect, ts_extracted, 'b', linewidth=1, alpha=0.75)
        # Add vertical lines for sec
        nsec = int(win_len_show)
        for sec_i in range(nsec):
            ax1.vlines(x=sec_i, ymin=-100, ymax=100, linewidth=0.5, color='b', linestyles='--')  

        # *** Add horizontal lines for events ***
        if len(events)>0:
            # for the current detector
            if event_name==None:
                for index, event in events.iterrows():
                    x_start_win = event['start_sec']-winshow_start_sec
                    y_start_win = x_start_win + event['duration_sec']
                    ax1.hlines(y=-90, xmin=x_start_win, xmax=y_start_win, linewidth=2.5, color='k') 
                ax1.set_title(chan_sel +' (start:'+time_elapsed+'; length: {0:0.2f} mins)'\
                    .format(win_len_show/60))
            # Extract the events_name when all previous event are saved
            else:
                # Display all previous events
                event_name_chan = event_name + '_' + chan_sel
                for index, event in events.iterrows():
                    x_start_win = event['start_sec']-winshow_start_sec
                    y_start_win = x_start_win + event['duration_sec']
                    if event['name']==event_name and chan_sel==event['channels']:
                        ax1.hlines(y=-90, xmin=x_start_win, xmax=y_start_win, linewidth=2.5, color='k') 
                    elif (event['group']=='artefact') and (chan_sel==event['channels']):
                        ax1.hlines(y=90, xmin=x_start_win, xmax=y_start_win, linewidth=2.5, color='r')   
                ax1.set_title(event_name + ' :' + chan_sel + ' (start:'+time_elapsed+'; length: {0:0.2f} mins)'\
                    .format(win_len_show/60))
        else:
            ax1.set_title(chan_sel +' (start:'+time_elapsed+'; length: {0:0.2f} mins)'\
                .format(win_len_show/60))            
        ax1.grid(True)
        ax1.set_ylabel('amplitude(µV)')
        ax1.set_xlim((time_vect[0], time_vect[-1]))  
        ax1.set_ylim((-100, 100)) 

        #----------------------------------------------------------------------
        # Plot detection info
        ax2 = self.figure.add_subplot(gs[2:4])
        ax2.plot(time_vect, det_act_smp, 'b', linewidth=2, alpha=0.75, label='current activity')
        if bsl_smp is not None:
            if median_use:
                ax2.plot(time_vect, np.squeeze(bsl_smp), 'k', linewidth=1.75, \
                    alpha=0.75, label='med baseline activity')
                ax2.plot(time_vect, np.squeeze(bsl_smp)*threshold, 'r', linewidth=1.5, \
                    alpha=0.75, label='adaptive treshold')
            else:
                # Since the data is z-score transformed, the bsl is always at z-score = 0
                # ax2.plot(time_vect, np.zeros(len(time_vect)), 'k', linewidth=1.75, alpha=0.75, \
                #     label='mean baseline activity')
                ax2.plot(time_vect, np.ones(len(time_vect))*threshold, 'r', \
                linewidth=1.5, alpha=0.75, label='adaptive treshold')
                # Plot the threshold value µV^2 : bsl mean + treshold * bsl STD
                # Plot threshold value on the right axis
                # twin object for two different y-axis on the sample plot
                ax22=ax2.twinx() 
                # make a plot with different y-axis using second axis object
                ax22.plot(time_vect, bsl_smp[0,:] + bsl_smp[1,:]*threshold, 'g',\
                    linewidth=1.75, alpha=0.75, label='threshold value(µV²)')
                ax22.set_ylabel('threshold value(µV²)')
                ax22.yaxis.label.set_color('green')
        else:
            ax2.plot(time_vect, np.ones(len(time_vect))*threshold, 'r', \
                linewidth=1.5, alpha=0.75, label='fixed treshold')            
        
        # Add vertical lines for sec
        for sec_i in range(nsec):
            if median_use:
                ax2.vlines(x=sec_i, ymin=0, ymax=np.nanmax(np.squeeze(bsl_smp)*threshold)*1.1, \
                    linewidth=0.5, color='b', linestyles='--')
            else:
                ax2.vlines(x=sec_i, ymin=-0.1, ymax=threshold*1.1, linewidth=0.5, \
                    color='b', linestyles='--')
        ax2.set_xlim((time_vect[0], time_vect[-1]))

        self.figure.text(0.2, 0.55, 'Detection : ', color='black', fontsize='small')
        if bsl_smp is not None:
            if median_use:
                ax2.set_ylim((0, np.nanmax(bsl_smp*threshold)*1.1))
                ax2.set_ylabel('power(µV²)')
                self.figure.text(0.325, 0.55, 'Current Activity', color='blue', fontsize='small')
                self.figure.text(0.5, 0.55, 'median baseline', color='black', fontsize='small')
                self.figure.text(0.7, 0.55, 'treshold', color='red', fontsize='small')
            else:
                ax2.set_ylim((-0.1, threshold*1.1))
                ax2.set_ylabel('power(z-score)')
                self.figure.text(0.325, 0.55, 'z-score activity', color='blue', fontsize='small')
                self.figure.text(0.5, 0.55, 'z-score treshold', color='red', fontsize='small')
                self.figure.text(0.655, 0.55, 'treshold value (right)', color='green', fontsize='small')      
        else:
            self.figure.text(0.325, 0.55, 'Current Activity', color='blue', fontsize='small')
            self.figure.text(0.655, 0.55, 'fixed treshold', color='red', fontsize='small')
            ax2.set_ylim((0, threshold*1.1))
            ax2.set_ylabel('power(µV²)')
        
        # General plot init
        #ax2.legend()
        ax2.grid(True)
        ax2.set_xlabel('time(s)')


        #----------------------------------------------------------------------
        # Plot histogram info
        ax3 = self.figure.add_subplot(gs[4])
        hist_count, hist_bin, _ = ax3.hist(det_act_smp, range=(np.nanmin(det_act_smp),\
                     np.nanmax(det_act_smp)), bins=100)
        # Choose bins to show the threshold
        if bsl_smp is not None:
            if median_use:             
                ax3.vlines(x=np.nanmax(bsl_smp*threshold), ymin=0, \
                    ymax=hist_count.max(), linewidth=0.5, \
                        color='r', linestyles='-')
                ax3.vlines(x=np.nanmin(bsl_smp*threshold), ymin=0, \
                    ymax=hist_count.max(), \
                    linewidth=0.5, color='r', linestyles='-')
            else:
                ax3.vlines(x=threshold, ymin=-0.1, ymax=hist_count.max(), linewidth=0.5, \
                    color='r', linestyles='-')                
        else:
            ax3.vlines(x=threshold, ymin=0, ymax=hist_count.max(), linewidth=0.5, \
                color='r', linestyles='-') 
        ax3.set_title('Histogram of detection info')

        # needed when tight_layout cannot make axes height small enough to accommodate all axes decorations
        self.canvas.draw()
        self.figure.tight_layout()
        # Redraw the figure, needed when the show button is pressed more than once
        self.canvas.draw()


    def _get_time_elapsed_sec( self ):
        time_elapsed = self.time_lineedit.text()
        nhour, nmin, nsec = time_elapsed.split(':')
        return int(nhour) * 3600 + int(nmin) * 60 + float(nsec)


    def on_choose_button( self):
        """Choose button is pressed by the user.
        Open a file. Ask the user for a Python file.
        """
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 
            'Open detection information from a python file', 
            None, 
            'Python (*.npy)')
        if filename != '':
            self.filename_lineedit_2.setText(filename)
            try:
                # Load the python file
                self.disk_cache = np.load(filename,allow_pickle='TRUE').item()
                self.filename = filename
                self.on_show_button()
            except (ValueError) as e:  
                print("Error when reading {} : {}".format(filename,e) )
                self.disk_cache = {}
                self.filename = ''
        else:
            print('No file selected')


    def on_show_button( self):
        ''' A slot called when the user presses enter after editing the time.
        '''
        self._on_navigate(next_on=0)


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

        # When the process has been run and filename points to 
        # the python file saved during the run
        if len(self.disk_cache)==0:
            self.disk_cache = np.load(self.filename,allow_pickle='TRUE').item()
        # Add a reference to few item on the cache dict
        signals_chan = self.disk_cache['signal_model']

        fs = signals_chan[0].sample_rate
        threshold = self.disk_cache['threshold']
        median_use = self.disk_cache['median_use']

        # Compute the new time elapsed
        try: 
            winshow_start_sec = self._get_time_elapsed_sec()
        except (ValueError) as e:  
            print("Error when reading time_elapsed : {}".format(e) )
        # Get the time window length to show.
        win_len_show = float(self.win_len_lineEdit.text())
        if next_on==1:
            winshow_start_sec = winshow_start_sec + win_len_show
        elif next_on==-1:
            winshow_start_sec = winshow_start_sec - win_len_show
        
        # Find the item from the list where the data starts
        signal_chan_start = None
        signal_i = None
        for i, signal in enumerate(signals_chan):
            # The first signal that end after the asked time
            if signal.end_time>winshow_start_sec:
                # If the user wants a previous window : allow to jump to the previous signal
                if next_on==-1 and i>0 and signal.start_time>winshow_start_sec:
                    signal_i = i-1
                else:
                    signal_i = i
                signal_chan_start = signals_chan[signal_i]
                break

        if not signal_chan_start == None:
            threshold_extracted = threshold[signal_i]
            computed_start = signal_chan_start.start_time
            smp_start_i = int((winshow_start_sec-computed_start) * fs)
            # If the window starts before the current signal, show the beginning
            if smp_start_i<0:
                smp_start_i = 0
                winshow_start_sec = signal_chan_start.start_time
                nmin, nsec = divmod(winshow_start_sec, 60)
                nhour, nmin = divmod(nmin, 60)
                time_elapsed = f'{int(nhour):02d}:{int(nmin):02d}:{int(nsec):02d}'
            # If the windows starts after the current signal, show the end
            elif smp_start_i>=len(signal_chan_start.samples):
                smp_start_i = int((signal_chan_start.duration - win_len_show) * fs)
                winshow_start_sec = signal_chan_start.end_time - win_len_show
                nmin, nsec = divmod(winshow_start_sec, 60)
                nhour, nmin = divmod(nmin, 60)
                time_elapsed = f'{int(nhour):02d}:{int(nmin):02d}:{int(nsec):02d}'
            smp_stop_i = smp_start_i + int(win_len_show * fs)            
            # time elapsed is included in the recording
            if winshow_start_sec<signal_chan_start.end_time\
                and (winshow_start_sec + win_len_show)>=signal_chan_start.start_time:
                # Desable the button if its impossible to press the button another time.
                if ((winshow_start_sec - win_len_show)<signal_chan_start.start_time) and signal_i==0:
                    self.prev_but.setEnabled(False)
                else:
                    self.prev_but.setEnabled(True)
                if ((winshow_start_sec+win_len_show)>signal_chan_start.end_time) and (signal_i==(len(signals_chan)-1)):
                    self.next_but.setEnabled(False)
                else:
                    self.next_but.setEnabled(True)
                # Set the time elapsed
                nhour = int(winshow_start_sec/3600)
                sec_tmp = winshow_start_sec-nhour*3600
                nmin = int(sec_tmp/60)
                nsec = winshow_start_sec-nhour*3600-nmin*60
                time_elapsed = "{0:02d}:{1:02d}:{2:0.2f}".format(nhour,nmin,nsec)
                self.time_lineedit.setText(time_elapsed)

                # Extract data
                smp_start_i = int((winshow_start_sec-signal_chan_start.start_time) * fs)
                smp_stop_i = smp_start_i + int(win_len_show * fs)
                # Pad with nans if the window to display 
                #   ends after the actual recording
                #   or starts before 0
                nanpad = 0
                if smp_start_i < 0:
                    nanpad = abs(smp_start_i)
                    smp_start_i = 0
                elif smp_stop_i > len(signal_chan_start.samples):
                    nanpad = smp_stop_i-len(signal_chan_start.samples)
                    smp_stop_i = len(signal_chan_start.samples)
                
                # Copy info from the cache
                ts_samples = signal_chan_start.samples.copy()
                det_act_smp = self.disk_cache['det_act_smp'].copy()
                det_act_smp = det_act_smp[signal_i]
                if 'bsl_smp' in self.disk_cache.keys():
                    bsl_smp = self.disk_cache['bsl_smp'].copy()
                else:
                    bsl_smp = None
                # Fill an nan array
                nan_array = np.empty(nanpad)
                nan_array[:] = np.nan
                if smp_start_i==0:
                    ts_extracted = np.concatenate((nan_array, ts_samples[smp_start_i:smp_stop_i]),axis=0)
                    det_smp_extracted = np.concatenate((nan_array, det_act_smp[smp_start_i:smp_stop_i]),axis=0)
                    if bsl_smp is not None:
                        nan_array = np.empty((bsl_smp.shape[0],nanpad))
                        bsl_smp_extracted = np.concatenate((nan_array, bsl_smp[:,smp_start_i:smp_stop_i]),axis=-1)
                    else:
                        bsl_smp_extracted = None
                else:
                    ts_extracted = np.concatenate((ts_samples[smp_start_i:smp_stop_i],nan_array),axis=0)
                    det_smp_extracted = np.concatenate((det_act_smp[smp_start_i:smp_stop_i],nan_array),axis=0)
                    if bsl_smp is not None:
                        nan_array = np.empty((bsl_smp.shape[0],nanpad))
                        bsl_smp_extracted = np.concatenate((bsl_smp[:,smp_start_i:smp_stop_i],nan_array),axis=-1)
                    else:
                        bsl_smp_extracted = None                    
                
                # Extract events
                #   event starts before the end of the window showed (winshow_offset_sec+win_len_show)
                #   event ends after the start of the window showed (winshow_offset_sec) and 
                events = self.disk_cache['events']
                if len(events):
                    new_df_events = events[(events.start_sec < (winshow_start_sec+win_len_show))\
                                            & ((events.start_sec+events.duration_sec) > winshow_start_sec)]
                else:
                    new_df_events = ''
                
                event_name = self.disk_cache['event_name']
                # when the window ends before the time serie, the detection can ends before the time serie
                # to avoid that problem the detection could be regenerated from 
                #   det_smp_extracted and bsl_smp_extracted (with the threshold)

                # -----------------------------------------------------------------
                # Plot eeg signal and detection info.
                # -----------------------------------------------------------------
                self._plot_det_info( self.time_lineedit.text(), win_len_show, \
                    ts_extracted, signal_chan_start, new_df_events, det_smp_extracted, \
                        threshold_extracted, median_use, bsl_smp_extracted, event_name)
            else:
                print("Time elapsed asked is outside the EDF recording")
                if winshow_start_sec>=(len(signal_chan_start.samples)/fs):
                    self.next_but.setEnabled(False)
                if winshow_start_sec<=0:
                    self.prev_but.setEnabled(False)
        else:
            print("Time elapsed asked is outside the EDF recording")
            self.next_but.setEnabled(False)
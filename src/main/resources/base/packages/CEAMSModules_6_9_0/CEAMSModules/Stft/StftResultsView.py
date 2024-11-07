"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the Stft plugin
"""

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.ticker as mticker
import numpy as np

from qtpy import QtWidgets
from qtpy import QtGui

from CEAMSModules.Stft.plot_helper import draw_spectogram
from CEAMSModules.Stft.Ui_StftResultsView import Ui_StftResultsView

class StftResultsView( Ui_StftResultsView, QtWidgets.QWidget):
    """
        StftView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(StftResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)

        # To manage the disk cache to navigate through epochs
        self.filename = []
        self.disk_cache = {}

        # To manage the figure on the layout result_layout
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        toolbar = NavigationToolbar(self.canvas, self)
        # set the layout
        self.result_layout.addWidget(toolbar)
        self.result_layout.addWidget(self.canvas)
    

    def load_results(self):
        # Read result cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)

        if cache is not None:
            # Get the data needed in the spectogram
            win_len = cache['win_len']
            win_step = cache['win_step_sec']
            psd = cache['psd']
            freq_bins = cache['freq_bins']
            self.filename = cache['filename']

            # Call the display function
            self._plot_resultsView(psd, win_len, win_step, 0, psd.shape[0], freq_bins)

            # Make the file selection ready 
            self.filename_lineEdit.setText(self.filename)
            self.time_lineEdit.setText("00:00:00")
            # Init the window length with the real signal length
            # It makes sens when the user uncheck box to keep the same signal view
            length_sec = psd.shape[0]*win_step+(win_len-win_step)
            self.length_lineEdit.setText(str(length_sec))
            # Make the navigate button ready
            self.next_pb.setEnabled(True)
            self.previous_pb.setEnabled(False)
        else:
            self.figure.clear() # reset the hold on 
            # Redraw the figure, needed when the show button is pressed more than once
            self.canvas.draw()            


    def on_choose(self):
        """Choose button is pressed by the user.
        Open a file. Ask the user for a Python file.
        """
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 
            'Open detection information from a python file', 
            None, 
            'Python (*.npy)')
        if filename != '':
            self.filename_lineEdit.setText(filename)
            try:
                # Load the python file
                self.disk_cache = np.load(filename,allow_pickle='TRUE').item()
                self.filename = filename
            except (ValueError) as e:  
                print("Error when reading {} : {}".format(filename,e) )
                self.disk_cache = {}
                self.filename = ''
        else:
            print('No file selected')


    def on_previous(self):
        """<< button is pressed by the user.
        The user wants to display the previous window.
        """    
        self._on_navigate(move=-1)


    def on_next(self):
        """>> button is pressed by the user.
        The user wants to display the next window.
        """    
        self._on_navigate(move=1)


    def on_time_changed(self):
        """When the user press "enter" after writing a time
        """    
        self._on_navigate(move=0)


    def on_plot_cb(self):
        """When the user check or uncheck the "show <30 Hz" or the "log scale"
        """    
        self._on_navigate(move=0)


    "Function to draw the spectogram and STFT mean"
    def _on_navigate(self, move=0):
        
        # When the process has been run and filename points to 
        # the python file saved during the run
        if len(self.disk_cache)==0:
            if not self.filename=='':
                self.disk_cache = np.load(self.filename,allow_pickle='TRUE').item()
            else:
                war_message = "WARNING : StftResultsView - no file saved"
                print(war_message)                
        
        if len(self.disk_cache)>0:
            # Get the data needed in the spectogram
            # references on dict
            win_len = self.disk_cache['win_len']
            win_step_sec = self.disk_cache['win_step_sec']
            psd = self.disk_cache['psd']
            freq_bins = self.disk_cache['freq_bins']
            self.filename = self.disk_cache['filename']    
            fs = self.disk_cache['sample_rate']

            try: 
                winshow_start_sec = self._get_time_elapsed_sec()
            except (ValueError) as e:  
                print("Error when reading time_elapsed : {}".format(e) )
            if move==1:
                winshow_start_sec = winshow_start_sec + float(self.length_lineEdit.text())
            elif move==-1:
                winshow_start_sec = winshow_start_sec - float(self.length_lineEdit.text())
            
            # time elapsed is included in the recording
            if winshow_start_sec<=(np.shape(psd)[0]*win_step_sec-win_len) and winshow_start_sec>=0:
                # Desable the button if its impossible to press the button another time.
                if winshow_start_sec - float(self.length_lineEdit.text())<0:
                    self.previous_pb.setEnabled(False)
                else:
                    self.previous_pb.setEnabled(True)
                if winshow_start_sec+float(self.length_lineEdit.text())>(np.shape(psd)[0]*win_step_sec-win_len):
                    self.next_pb.setEnabled(False)
                else:
                    self.next_pb.setEnabled(True)

                # Extract time window asked
                winshow_start_win = int(winshow_start_sec/win_step_sec)
                if float(self.length_lineEdit.text())<win_len:
                    print('Window length to show {} is shorter than the STFT window length {}'\
                        .format(self.length_lineEdit.text(), win_len))
                    self.length_lineEdit.setText(win_len)

                winshow_len_win = int(float(self.length_lineEdit.text())/win_step_sec)
                # Set the time elapsed of the real start based on the window step resolution
                self._set_time_elapsed_sec( winshow_start_win*win_step_sec )

                # Call the display function
                self._plot_resultsView(psd, win_len, win_step_sec, winshow_start_win, \
                    winshow_len_win, freq_bins)

            else:
                if winshow_start_sec>=(np.shape(psd)[1]/fs):
                    self.next_pb.setEnabled(False)
                if winshow_start_sec<=0:
                    self.previous_pb.setEnabled(False)     
                

    def _get_time_elapsed_sec( self ):
        time_elapsed = self.time_lineEdit.text()
        nhour, nmin, nsec = time_elapsed.split(':')
        return int(nhour) * 3600 + int(nmin) * 60 + float(nsec)


    def _set_time_elapsed_sec( self, winshow_start_sec ):
        nhour = int(winshow_start_sec/3600)
        sec_tmp = winshow_start_sec-nhour*3600
        nmin = int(sec_tmp/60)
        nsec = winshow_start_sec-nhour*3600-nmin*60
        time_elapsed = "{0:02d}:{1:02d}:{2:0.2f}".format(nhour,nmin,nsec)
        self.time_lineEdit.setText(time_elapsed)


    def _plot_resultsView(self, psd, win_len, win_step_sec, winshow_start_win, \
        winshow_len_win, freq_bins):
        
        #-----------------
        # Manage figure
        #-----------------
        # reset the hold on needed to erase the color bar
        self.figure.clear() 
        # create an axis
        ax = self.figure.add_subplot(121)
        # discards the old graph
        ax.clear()
        #-----------------
        # Extract data
        #-----------------
        # psd : ndarray [fft_win_count x 0-fs/2 Hz]
        psd_extract = psd[winshow_start_win:winshow_start_win+winshow_len_win,:].copy()
        # Flip it so X axis is the time and Y is the frequencies
        psd_extract = np.transpose(psd_extract) # A view is returned whenever possible.
        #-----------------
        # Plot data
        #-----------------
        # Manage the figure
        # Modify the plot based on the checkbox
        if self.log_cb.isChecked():
            scale="log"
            if self.zoom_cb.isChecked():
                ylim = (1, min(30,freq_bins[-1]))
            else:
                ylim = (1, min(65,freq_bins[-1]))
        else:
            scale="linear"
            if self.zoom_cb.isChecked():
                ylim = (0.5, min(30,freq_bins[-1]))
            else:
                ylim = (0.5, min(65,freq_bins[-1]))     
        
        draw_spectogram(ax, psd_extract, freq_bins, win_len, win_step_sec, \
            scale, ylim, show_colorbar=True, fig=self.figure)

        # Draw the STFT mean (spectral density)
        ax2 = self.figure.add_subplot(122)
        ax2.clear()
        ax2.plot(freq_bins, np.mean(psd_extract, axis=1))
        ax2.set_yscale(scale)
        if self.log_cb.isChecked():
            ax2.set_ylim((1, max(np.mean(psd_extract, axis=1))))
        else:
            ax2.set_ylim((0, max(np.mean(psd_extract, axis=1))))
        if self.zoom_cb.isChecked():
            ax2.set_xlim((0, min(30,freq_bins[-1])))
        else:
            ax2.set_xlim((0, min(65,freq_bins[-1])))
        ax2.set_xlabel('Hz')
        ax2.set_title(f'STFT Mean')
        
        # refresh canvas
        self.figure.tight_layout()
        self.canvas.draw()
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the SpectralDetector plugin
"""

import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.patches as patches
import matplotlib.ticker as mticker
import numpy as np

from qtpy import QtWidgets
from qtpy import QtGui

from CEAMSModules.Stft.plot_helper import draw_spectogram
from CEAMSModules.AmplitudeVarDetector.Ui_AmplitudeVarDetectorResultsView import Ui_AmplitudeVarDetectorResultsView


class AmplitudeVarDetectorResultsView( Ui_AmplitudeVarDetectorResultsView, QtWidgets.QWidget):
    """
        AmplitudeVarDetectorView display the amplitude of the whole night into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(AmplitudeVarDetectorResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)

        # Manage the figure on the result_layout from UI
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        toolbar = NavigationToolbar(self.canvas, self)

        # set the layout
        self.result_layout.addWidget(toolbar)
        self.result_layout.addWidget(self.canvas)


    def load_results(self):

        # create an axis
        ax = self.figure.add_subplot(111)
        # discards the old graph
        ax.clear()

        # Read result cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)

        if cache is not None:

            # Get the data needed in the spectogram
            signal = cache['signal']
            fs = cache['fs']
            
            # Create the time vector in hour
            time_vect = np.arange(start=0, stop=len(signal)/fs, step=1/fs)

            # Plot the detection activity
            ax.plot(time_vect, signal)

            # Events are already filtered for the current detector
            df_event = cache['events']

            # Draw a rectangle for each event detected. The rectangles are limited
            # by the start time and the duration of the event on the X axis
            # and the lower frequency and higher frequency of the detection on the
            # y axis.            
            for index, event in df_event.iterrows():
                x = event.start_sec
                w = event.duration_sec
                rect = patches.Rectangle(
                    (x,0), w, np.nanmax(signal)*1.1,
                    linewidth=1,
                    edgecolor='r',
                    facecolor='r',
                    alpha = 0.5)
                ax.add_patch(rect)
            
            # Plot a horizontal line for the threshold
            #ax.hlines(y=threshold_val, xmin=time_vect[0], xmax=time_vect[-1], linewidth=1, color='r')

            # The tick label strings are not populated until a draw method has been called.
            self.canvas.draw()

            # Format the X axis ticker from secondes to time (HH:MM:SS format)
            def fmtsec(x,pos):
                hours = int(x / 60 / 60)
                mins = int((x - hours*60*60) / 60)
                seconds = x % 60
                return "{:02d}:{:02d}:{:02.1f}".format(hours,mins,seconds)
            ax.xaxis.set_major_formatter(mticker.FuncFormatter(fmtsec))

            formatter = mticker.ScalarFormatter()
            formatter.set_scientific(False)
            ax.yaxis.set_major_formatter(formatter)
            ax.yaxis.set_minor_formatter(formatter)
            ax.tick_params(axis='y', which='minor', labelsize=8)
            ax.set_xlabel('Time (HH:MM:SS)')

            ax.set_ylabel('Amplitude µV')
            ax.set_title('Amplitude detection')

        self.canvas.draw()
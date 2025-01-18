"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the WindowsToSamples plugin
"""

from qtpy import QtWidgets

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.ticker as mticker
import numpy as np

from CEAMSModules.WindowsToSamples.Ui_WindowsToSamplesResultsView import Ui_WindowsToSamplesResultsView

class WindowsToSamplesResultsView( Ui_WindowsToSamplesResultsView, QtWidgets.QWidget):
    """
        WindowsToSamplesResultsView nohting to show.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(WindowsToSamplesResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)

        # Init figure
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        toolbar = NavigationToolbar(self.canvas, self)

        # set the layout
        self.result_layout.addWidget(toolbar)
        self.result_layout.addWidget(self.canvas)


    def load_results(self):
        # Load the cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)
        if cache is not None:
            self.figure.clear() # reset the hold on 

            signal = cache['samples_values']
            channel_name = cache['channel']
            sample_rate = cache['sample_rate']

            signal_length = len(signal) # time series
            x_time = np.linspace(0, signal_length/sample_rate, num=signal_length)

            # create an axis
            self.ax1 = self.figure.add_subplot(1,1,1)
            # Plot windows values converted into the samples domain
            self.ax1.plot(x_time, signal, color=[0.25, 0.25, 0.25], linewidth=1)
            self.ax1.grid(True)
            self.ax1.set_title(channel_name)
            self.ax1.set_ylabel('Amplitude')
            self.ax1.set_xlabel('Time(s)')      
               
            # Redraw the figure, needed when the show button is pressed more than once
            self.canvas.draw()
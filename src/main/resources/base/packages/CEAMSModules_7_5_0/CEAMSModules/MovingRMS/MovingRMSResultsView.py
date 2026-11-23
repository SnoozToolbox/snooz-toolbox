"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the MovingRMS plugin
"""

from qtpy import QtWidgets

import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.ticker as mticker
import numpy as np

from CEAMSModules.MovingRMS.Ui_MovingRMSResultsView import Ui_MovingRMSResultsView

class MovingRMSResultsView( Ui_MovingRMSResultsView, QtWidgets.QWidget):
    """
        MovingRMSResultsView nohting to show.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(MovingRMSResultsView, self).__init__(*args, **kwargs)
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

            samples = cache['in_signal']
            moving_RMS_values = cache['moving_RMS_values']
            channel_name = cache['channel']
            sample_rate = cache['sample_rate']
            win_step_sec = cache['win_step_sec']

            signal_length = len(samples)
            x_time = np.linspace(0, signal_length/sample_rate, num=signal_length)

            # create an axis
            self.ax1 = self.figure.add_subplot(2,1,1)
            # Plot signal
            self.ax1.plot(x_time, samples,  label='signal', 
                                            color=[0.25, 0.25, 0.25], 
                                            linewidth=1)
            self.ax1.grid(True)
            self.ax1.set_title(channel_name)
            self.ax1.set_ylabel('Amplitude(µV)')

            # Convert a by-window information to by-sample information to match the signal
            if win_step_sec != 0:
                nsample_step = win_step_sec*sample_rate
                if not nsample_step.is_integer():
                    win_step_sec = int(round(nsample_step))/sample_rate
                nsample_step = int(round(win_step_sec*sample_rate))
                reps = np.ones(moving_RMS_values.shape[0],dtype=int) * nsample_step
                moving_RMS_smp = np.repeat(moving_RMS_values, reps)
            else:
                moving_RMS_smp = moving_RMS_values

            # Different length when the last window is incomplete
            # I think the best way is to duplicate the last info
            if len(samples) > len(moving_RMS_smp):
                values_2_pad = np.ones(len(samples)-len(moving_RMS_smp))*moving_RMS_smp[-1]
                moving_RMS_smp = np.concatenate((moving_RMS_smp,values_2_pad))        

            # Plot moving RMS
            self.ax2 = self.figure.add_subplot(2,1,2)                                          
            x_time = np.linspace(0, signal_length/sample_rate, num=signal_length)
            self.ax2.plot(x_time, moving_RMS_smp,  label='RMS', 
                                            color=[0.25, 0.25, 0.25], 
                                            linewidth=1)
            self.ax2.grid(True)
            self.ax2.set_ylabel('RMS')
            self.ax2.set_xlabel('Time(s)')        
            # Redraw the figure, needed when the show button is pressed more than once
            self.canvas.draw()
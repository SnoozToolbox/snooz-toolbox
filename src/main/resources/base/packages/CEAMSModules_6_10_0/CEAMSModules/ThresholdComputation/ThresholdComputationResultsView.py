"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the ThresholdComputation plugin
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

from CEAMSModules.ThresholdComputation.Ui_ThresholdComputationResultsView import Ui_ThresholdComputationResultsView

class ThresholdComputationResultsView( Ui_ThresholdComputationResultsView, QtWidgets.QWidget):
    """
        ThresholdComputationResultsView nohting to show.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(ThresholdComputationResultsView, self).__init__(*args, **kwargs)
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

        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)
        if cache is not None:
            self.figure.clear() # reset the hold on 

            samples = cache['sample']
            channel_name = cache['channel_label']
            threshold_metric = cache['threshold_metric']
            threshold_definition = cache['threshold_definition']
            threshold_value = cache['threshold_value']

            # create an axis
            self.ax1 = self.figure.add_subplot(1,1,1)
            # the histogram of the data
            self.ax1.hist(samples, 50, density=True, facecolor='b', alpha=0.75)
            self.ax1.axvline(x=threshold_value, ymin=0, ymax=1, color='r')
            self.ax1.grid(True)
            self.ax1.set_title(channel_name + ": " +  str(threshold_definition) + " " + threshold_metric)
            self.ax1.set_ylabel('density probability')
            self.ax1.set_xlabel('Value')

            # Redraw the figure, needed when the show button is pressed more than once
            self.canvas.draw()        


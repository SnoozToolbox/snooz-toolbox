"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the Resample plugin
"""

import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

from qtpy import QtWidgets
from qtpy import QtGui

from CEAMSModules.Resample.Ui_ResampleResultsView import Ui_ResampleResultsView

class ResampleResultsView( Ui_ResampleResultsView, QtWidgets.QWidget):
    """
        ResampleView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(ResampleResultsView, self).__init__(*args, **kwargs)
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
        self.signal_layout.addWidget(toolbar)
        self.signal_layout.addWidget(self.canvas)

        # create an axis
        self.ax = self.figure.add_subplot(111)

    def load_results(self):
        # discards the old graph
        self.ax.clear()

        # Read result cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)

        if cache is not None:
            fs = cache['input_sample_rate']
            x = np.linspace(0, 30, num=int(30*fs))
            self.ax.plot(x, cache['input_signal'],   label='Input signal',
                                                color=[0.25, 0.25, 0.25],
                                                linewidth=1)

            fs = cache['output_sample_rate']
            x = np.linspace(0, 30, num=int(30*fs))
            self.ax.plot(x, cache['output_signal'],  label='Output signal',
                                                color=[0.8500, 0.3250, 0.0980],
                                                linewidth=1)
            
            self.ax.set_xlabel('Seconds')
            self.ax.set_ylabel('µV')
            self.ax.set_ylim((-100, 100))
            self.ax.set_title(cache['channel'])
            self.ax.legend()
            self.ax.grid()

        # refresh canvas
        self.canvas.draw()
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the Hypnogram plugin

    A hypnogram is a form of polysomnography; it is a graph that represents the 
    stages of sleep as a function of time.

    Takes sleep stages and sleep cycles in parameter. A sleep cycle is 
    defined as a period of NREM sleep followed by a period of REM sleep.

"""
from ..PSGReader import commons

import matplotlib
from numpy import ceil
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
import math
import numpy as np

from qtpy import QtWidgets

from CEAMSModules.Hypnogram.Ui_HypnogramResultsView import Ui_HypnogramResultsView
from CEAMSModules.Hypnogram.Hypnogram import Hypnogram

class HypnogramResultsView( Ui_HypnogramResultsView, QtWidgets.QWidget):
    """
        HypnogramResultsView displays an hypnogram based on the stages in input
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(HypnogramResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self) 

        self.figure = Figure(constrained_layout=False)
        self.hypno_ax = self.figure.add_subplot(111)
        self.hypno_ax.clear()

        # Add the figure tool bar
        self.canvas = FigureCanvas(self.figure)
        toolbar = NavigationToolbar(self.canvas, self)
        self.verticalLayout.addWidget(toolbar)
        self.verticalLayout.addWidget(self.canvas)


    def load_results(self):
        self.cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)

        if self.cache is not None:
            sleep_stages = self.cache['sleep_stages']
            epoch_len = self.cache['epoch_len_sec']
            sleep_cycles = self.cache['sleep_cycles']

            # Plot Hypnogram
            if sleep_stages is not None:
                Hypnogram.plot_hypnogram(self, sleep_stages, sleep_cycles, epoch_len=epoch_len)
            self.canvas.draw()
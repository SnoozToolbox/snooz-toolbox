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
from CEAMSModules.SpectralDetector.Ui_SpectralDetectorResultsView import Ui_SpectralDetectorResultsView


class SpectralDetectorResultsView( Ui_SpectralDetectorResultsView, QtWidgets.QWidget):
    """
        SpectralDetectorView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(SpectralDetectorResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)

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
            # reset the hold on needed to erase the color bar
            self.figure.clear() 

            # create an axis
            ax = self.figure.add_subplot(111)

            # discards the old graph
            ax.clear()

            # Get the data needed in the spectogram
            win_len = cache['psd_data']['win_len']
            win_step = cache['psd_data']['win_step']
            psd = cache['psd_data']['psd']
            freq_bins = cache['psd_data']['freq_bins']

            # Flip it so X axis is the time and Y is the frequencies
            psd = np.transpose(psd)
            
            draw_spectogram(ax, psd, freq_bins, win_len, win_step, scale='log', \
                show_colorbar=True, fig=self.figure)

            # Draw a rectangle for each event detected. The rectangles are limited
            # by the start time and the duration of the event on the X axis
            # and the lower frequency and higher frequency of the detection on the
            # y axis.
            for (index, row) in cache['detections'].iterrows(): # First 2 columns are [index] and [event name]
                x = row['start_sec']
                y = cache['low_freq']
                w = row['duration_sec']
                h = cache['high_freq'] - cache['low_freq']
                rect = patches.Rectangle(
                    (x,y),
                    w,h,
                    linewidth=1,
                    edgecolor='r',
                    facecolor='none')
                ax.add_patch(rect)
        else:
            # When the cache is erased, dont show signals
            self.figure.clear()
            self.canvas.draw()
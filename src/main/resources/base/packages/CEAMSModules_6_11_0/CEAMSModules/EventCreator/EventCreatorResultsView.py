"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the EventCreator plugin
"""

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

from qtpy import QtWidgets
from qtpy import QtGui

from CEAMSModules.EventCreator.Ui_EventCreatorResultsView import Ui_EventCreatorResultsView

class EventCreatorResultsView( Ui_EventCreatorResultsView, QtWidgets.QWidget):
    """
        EventCreatorView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(EventCreatorResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)

    def load_results(self):
        pass
"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the SignalFromEvent plugin
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

from CEAMSModules.PSGReader.SignalModel import SignalModel
from CEAMSModules.MutualInfo.Ui_MutualInfoResultsView import Ui_MutualInfoResultsView

class MutualInfoResultsView( Ui_MutualInfoResultsView, QtWidgets.QWidget):
   """
      MutualInfoView display the epochs list read
   """
   def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
      super(MutualInfoResultsView, self).__init__(*args, **kwargs)
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
         self.scores = cache['scores']
         self.n_chan = cache['n_chan']
         self.scores_events = SignalModel.get_attribute(self.scores, None, 'start_time')
         self.start_events = np.unique(SignalModel.get_attribute(self.scores, 'start_time', 'start_time'), axis=1)
         self.duration_events = np.unique(SignalModel.get_attribute(self.scores, 'duration', 'start_time'), axis=1)

         # Set first window
         self.index = 0
         self.prev_but.setEnabled(False)
         self.score = self.scores_events[self.index]
         self.start = self.start_events[self.index][0]
         self.duration = self.duration_events[self.index][0]

         # Update event
         self._update_event_info()

         # Scatter plot
         self._scatter_score(self.score)

         
      else:
         # When the cache is erased, dont show signals
         self.figure.clear()
         self.canvas.draw()

   def _update_event_info( self):

      # Fill info for first signal
      if self.duration>30:
         self.duration_lineEdit.setText(str(30))
      else:
         self.duration_lineEdit.setText(str(self.duration))
      self.event_index_lineEdit.setText(str(self.index))

      # Set the time elapsed
      nhour = int(self.start/3600)
      sec_tmp = self.start-nhour*3600
      nmin = int(sec_tmp/60)
      nsec = self.start-nhour*3600-nmin*60
      time_elapsed = "{0:02d}:{1:02d}:{2:0.2f}".format(nhour,nmin,nsec)
      self.time_lineedit.setText(time_elapsed)

   def on_event_index_changed( self):
      if int(self.event_index_lineEdit.text()) >= 0 and int(self.event_index_lineEdit.text()) <= (len(self.scores_events) - 1):
         self.index = int(self.event_index_lineEdit.text())
         self._on_navigate()
      else:
         self.event_index_lineEdit.setText(str(self.index))
         print("Error index outside of range")

   def _scatter_score( self, scores):
      """ 
      Plot scores from mutual information.

      Parameters
      -----------
         scores    : List
               List of all the mutual information score by epoch and by event

      """
      
      # Manage the figure
      self.figure.clear() # reset the hold on 

      #----------------------------------------------------------------------
      # Scatter plot
      ax = self.figure.add_subplot(1, 1, 1)
      y_vect = np.array([score.meta['mutual_info'] for score in scores])
      x_vect = range(scores.shape[0])
      ax.scatter(x_vect, y_vect, alpha=0.8, edgecolors='none', s=30)

      # Add title
      self.figure.suptitle('Mutual Info Score by event')

      ax.set_xticks(x_vect)
      ax.grid(True)
      ax.set_xlabel('Signal number')
      ax.set_ylabel('Mutual info score')
      #ax.legend(loc='center right', bbox_to_anchor=(1.12, 0.5))

      # Redraw the figure, needed when the show button is pressed more than once
      self.canvas.draw()

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

      # Change index of event
      self.index = self.index + next_on
      self.score = self.scores_events[self.index]
      self.start = self.start_events[self.index][0]
      self.duration = self.duration_events[self.index][0]

      # Update event
      self._update_event_info()
      
      # Desable the button if its impossible to press the button another time.
      if self.index - 1 < 0:
         self.prev_but.setEnabled(False)
      else:
         self.prev_but.setEnabled(True)
      if self.index + 1 > (len(self.scores_events) - 1):
         self.next_but.setEnabled(False)
      else:
         self.next_but.setEnabled(True)

      # Scatter plot
         self._scatter_score(self.score)

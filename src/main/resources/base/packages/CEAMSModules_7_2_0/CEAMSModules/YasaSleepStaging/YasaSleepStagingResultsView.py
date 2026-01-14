"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.

    Results viewer of the YasaSleepStaging plugin
"""

import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.gridspec as gridspec
import numpy as np
from qtpy import QtWidgets

from CEAMSModules.YasaSleepStaging.Ui_YasaSleepStagingResultsView import Ui_YasaSleepStagingResultsView
from sklearn.metrics import confusion_matrix
import seaborn as sns
from sklearn.calibration import calibration_curve

class YasaSleepStagingResultsView(Ui_YasaSleepStagingResultsView, QtWidgets.QWidget):
    """
        YasaSleepStagingResultsView.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(YasaSleepStagingResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)
        # Init figure
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        toolbar = NavigationToolbar(self.canvas, self)
        self.ACC = QtWidgets.QLabel()
        self.Confidence = QtWidgets.QLabel()
        self.Kappa = QtWidgets.QLabel()
                
        # set the layout
        self.result_layout.addWidget(toolbar)
        self.result_layout.addWidget(self.canvas)
        self.result_layout.addWidget(self.ACC)
        self.result_layout.addWidget(self.Confidence)
        self.result_layout.addWidget(self.Kappa)

    def load_results(self):

        self.figure.clear() # reset the hold on 
        self.figure.set_size_inches(15,4)
         # Read result cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)
        
        if cache is not None:
            # call accuracy
            Accuracy = cache['Accuracy']
            # call avg_confidence
            AvgConfidence = cache['Avg_Confidence']
            # call kappa
            Kappa = cache['kappa']
            # Create a new label widget to display the accuracy
            self.ACC.setText(f"Accuracy: {Accuracy:.2f}%")
            self.Confidence.setText(f"Avg Confidence: {AvgConfidence:.2f}%")
            self.Kappa.setText(f"Kappa: {Kappa:.2f}")
            ### Plot the hypnogram
            # Define the layout for the plots
            gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])  # Three equal-height plots
            
            #confidence = cache['y_pred_new'].proba.max(axis=1)
            #print(confidence)
            # Adjust the layout to make each subplot bigger
            gs.update(wspace=0.4, hspace=0.6)
            # First subplot - Hypnogram
            ax1 = self.figure.add_subplot(gs[0])
            ax1 = cache['labels_new'].plot_hypnogram(fill_color="gainsboro", ax=ax1)
            ax1.set_title('Expert Annotated Hypnogram')
            ax1.set_xlabel('Time (h)')
            ax1.set_ylabel('Sleep stage')
            ax1.grid()

            # Second subplot - Estimated Hypnogram
            ax2 = self.figure.add_subplot(gs[2])
            ax2 = cache['y_pred_new'].plot_hypnogram(fill_color="blue", ax=ax2)
            ax2.set_title('Estimated Hypnogram')
            ax2.set_xlabel('Time (h)')
            ax2.set_ylabel('Sleep stage')
            ax2.grid()

            # Compute confusion matrix
            y_true = cache['labels_new'].hypno.values
            y_pred = cache['y_pred_new'].hypno.values
            class_labels = ['WAKE', 'N1', 'N2', 'N3', 'REM']
            cm = confusion_matrix(y_true, y_pred, labels=class_labels)
            cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
            # Set the labels for the confusion matrix
            tick_marks = np.arange(len(class_labels))
            # Third subplot - Confusion Matrix
            ax3 = self.figure.add_subplot(gs[1])
            sns.heatmap(cm_normalized, annot=True, fmt='.2f', cmap='Blues', ax=ax3)
            ax3.set_title('Confusion Matrix')
            ax3.set_xlabel('Predicted')
            ax3.set_ylabel('True')
            ax3.set_xticks(tick_marks)
            ax3.set_xticklabels(class_labels)
            ax3.set_yticks(tick_marks)
            ax3.set_yticklabels(class_labels)
            # Save the figure to a PDF file
            '''file_name = cache['file_name']
            if isinstance(file_name, str) and (len(file_name)>0):
                if not '.' in file_name:
                    file_name = file_name + '.pdf'
            self.figure.savefig(file_name, format='pdf')'''

            '''# Fourth subplot - Calibration Curve
            ax4 = self.figure.add_subplot(gs[3])
            y_prob = cache['sls'].predict_proba()
            y_prob = y_prob.iloc[cache['first_wake']:cache['last_wake']+1]
            prob_true, prob_pred = calibration_curve(y_true, y_prob[:, 1], n_bins=10) 
               
            ax4.plot(prob_pred, prob_true, marker='o')
            ax4.set_title('Calibration Curve')
            ax4.set_xlabel('Mean predicted probability')
            ax4.set_ylabel('Fraction of positives')
            ax4.legend()
            ax4.grid()'''

            # Adjust layout to add more space between subplots
            self.figure.tight_layout(pad=10.0)
        # refresh canvas
        self.canvas.draw()
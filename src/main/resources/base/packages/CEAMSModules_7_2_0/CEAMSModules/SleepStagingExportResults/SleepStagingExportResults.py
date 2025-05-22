"""
@ Valorisation Recherche HSCM, Société en Commandite – 2025
See the file LICENCE for full license details.

    SleepStagingExportResults
    A Flowpipe node that handles the export and visualization of sleep staging results,
    including saving metrics to TSV files and generating PDF reports with hypnograms
    and confusion matrices.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import pandas as pd
import os

import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.gridspec as gridspec
from sklearn.metrics import confusion_matrix
import seaborn as sns
import numpy as np

DEBUG = False

class SleepStagingExportResults(SciNode):
    """
    Processes and visualizes sleep staging results including:
    - Saving performance metrics (accuracy, kappa, confidence) to TSV files
    - Generating PDF reports with comparative hypnograms and confusion matrices

    Parameters
    ----------
        ResultsDataframe: pd.DataFrame
            DataFrame containing sleep staging metrics (accuracy, kappa, confidence)
        info: list
            List containing [ground_truth_hypnogram, predicted_hypnogram, file_path]
        SavedDestination: str
            Directory path where results should be saved
        Checkbox: bool
            Flag indicating whether to save results (True) or skip (False)

    Returns
    -------
        ExportResults: str or None
            Path to the generated TSV file if saved, None otherwise
    """
    def __init__(self, **kwargs):
        """ Initialize module SleepStagingExportResults """
        super().__init__(**kwargs)
        if DEBUG: print('SleepStagingExportResults.__init__')

        # Input plugs
        InputPlug('ResultsDataframe', self)
        InputPlug('info', self)
        InputPlug('SavedDestination', self)
        InputPlug('Checkbox', self)

        # Output plugs
        OutputPlug('ExportResults', self)

        # Initialize the figure and canvas for plotting
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # A master module allows the process to be reexcuted multiple time.
        self._is_master = False
        self.AccuracyList = []

    def compute(self, ResultsDataframe, info, SavedDestination, Checkbox):
        """
        Processes sleep staging results by:
        1. Saving metrics to a cumulative TSV file when Checkbox is True
        2. Generating visualization PDF with:
           - Ground truth vs predicted hypnograms
           - Normalized confusion matrix
           - Accuracy/Kappa/Confidence metrics

        Parameters
        ----------
            ResultsDataframe: pd.DataFrame
                Contains columns: ['Accuracy', 'Average Confidence', 'kappa']
            info: list
                [ground_truth_labels, predicted_labels, source_file_path]
            SavedDestination: str
                Valid directory path for output files
            Checkbox: bool
                Control whether to save results

        Returns
        -------
            ExportResults: str or None
                Path to the generated TSV file if saved, None otherwise

        Raises
        ------
            NodeInputException
                If inputs are invalid (wrong types, missing data)
            NodeRuntimeException
                If file operations or visualizations fail
        """
        # Validate inputs
        if not isinstance(ResultsDataframe, pd.DataFrame):
            raise NodeInputException(self.identifier, "ResultsDataframe", "Input must be a pandas DataFrame")
        if not isinstance(info, list) or len(info) != 3:
            raise NodeInputException(self.identifier, "info", "Info must be a list of [ground_truth, predicted, file_path]")
        if not os.path.isdir(SavedDestination) and Checkbox:
            raise NodeInputException(self.identifier, "SavedDestination", "Output directory does not exist")
        

        if Checkbox:
            # Define file path (change extension to .tsv)
            export_results_file_path = SavedDestination + 'YASA_sleep_staging_metrics_cohort_report.tsv'  # TSV file
            # Check if file exists, if not create it with headers
            if not os.path.exists(export_results_file_path):
                pd.DataFrame().to_csv(export_results_file_path, sep='\t', index=False)  # TSV creation

            # Load existing data
            try:
                export_results_df = pd.read_csv(export_results_file_path, sep='\t')  # Read TSV
            except (pd.errors.EmptyDataError, FileNotFoundError):
                export_results_df = pd.DataFrame()

            # Append new data
            export_results_df = pd.concat([export_results_df, ResultsDataframe], ignore_index=True)

            # Save updated data back to TSV file
            export_results_df.to_csv(export_results_file_path, sep='\t', index=False)  # Save as TSV


            #NOTE: Plot the hypnogram and confusion matrix and save to a PDF file
            self.figure.clear() # reset the hold on
            self.figure.set_size_inches(15,4)
            ### Plot the hypnogram
            # Define the layout for the plots
            gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])  # Three equal-height plots
            
            #confidence = cache['y_pred_new'].proba.max(axis=1)
            #print(confidence)
            # Adjust the layout to make each subplot bigger
            gs.update(wspace=0.4, hspace=0.6)
            # First subplot - Hypnogram
            labels_new = info[0]
            ax1 = self.figure.add_subplot(gs[0])
            ax1 = labels_new.plot_hypnogram(fill_color="gainsboro", ax=ax1)
            ax1.set_title('Expert Annotated Hypnogram')
            ax1.set_xlabel('Time (h)')
            ax1.set_ylabel('Sleep stage')
            ax1.grid()

            # Second subplot - Estimated Hypnogram
            y_pred_new = info[1]
            ax2 = self.figure.add_subplot(gs[2])
            ax2 = y_pred_new.plot_hypnogram(fill_color="blue", ax=ax2)
            ax2.set_title('Estimated Hypnogram')
            ax2.set_xlabel('Time (h)')
            ax2.set_ylabel('Sleep stage')
            ax2.grid()

            # Compute confusion matrix
            y_true = labels_new.hypno.values
            y_pred = y_pred_new.hypno.values
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
            # Fourth subplot - Accuracy and Average Confidence
            ax4 = self.figure.add_subplot(gs[3])
            ax4.axis('off')
            # Add accuracy and average confidence text next to the subplots
            ax4.text(0.5, 0.5, f"Accuracy: {ResultsDataframe['Accuracy'].iloc[0]:.2f}%", transform=ax4.transAxes, fontsize=12, verticalalignment='center', horizontalalignment='center')
            ax4.text(0.5, 0.3, f"Avg Confidence: {ResultsDataframe['Average Confidence'].iloc[0]:.2f}%", transform=ax4.transAxes, fontsize=12, verticalalignment='center', horizontalalignment='center')
            ax4.text(0.5, 0.1, f"Kappa: {ResultsDataframe['kappa'].iloc[0]:.2f}", transform=ax4.transAxes, fontsize=12, verticalalignment='center', horizontalalignment='center')
                                # Adjust layout to add more space between subplots
            self.figure.tight_layout(pad=10.0)

                    # Save the figure to a PDF file
            filename = os.path.basename(info[2])
            name_without_extension = os.path.splitext(filename)[0]
            file_name = SavedDestination + name_without_extension
            file_name = file_name + '.pdf'
            self.figure.savefig(file_name, format='pdf')

            # refresh canvas
            self.canvas.draw()
            # Return the path to the updated Excel file
        else:
            export_results_file_path = None

        return {
            'ExportResults': export_results_file_path
        }

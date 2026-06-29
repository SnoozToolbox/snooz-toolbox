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

# Conditionally import matplotlib based on headless mode
import config
if config.HEADLESS_MODE:
    # Use Agg backend in headless mode (no GUI required, perfect for PDF generation)
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib.figure import Figure
else:
    # Use QtAgg backend in GUI mode
    import matplotlib
    matplotlib.use('QtAgg')
    from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
    from matplotlib.figure import Figure

import matplotlib.pyplot as plt
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
        # Canvas is only needed in GUI mode (for interactive display)
        # In headless mode, we can still save figures to PDF without canvas
        if not config.HEADLESS_MODE:
            self.canvas = FigureCanvas(self.figure)
        else:
            self.canvas = None

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
        if not isinstance(info, list) or len(info) != 6:
            raise NodeInputException(self.identifier, "info", "Info must be a list of [ground_truth, predicted, file_path, proba_list, confidence, names]")
        if not os.path.isdir(SavedDestination) and Checkbox:
            raise NodeInputException(self.identifier, "SavedDestination", "Output directory does not exist")
        
        # plot the hypnodensity figure for both cases: validation and prediction
        stage_colors = {
            'N1': "#88cee6",
            'N2': "#1A7CCCFF",
            'N3': '#00008B',
            'R': 'purple',
            'W': 'gold'}
        names = info[5]
        n = len(names)
        cols = 2
        rows = (n + cols - 1) // cols
        self.fig, axes = plt.subplots(rows, cols, figsize=(14, rows * 4))
        self.fig.suptitle('Hypnodensity Plots', fontsize=20)
        axes = axes.flatten()
        for i, name in enumerate(names):
            proba = info[3][i]
            if i == len(names) - 1:
                # change the proba to a new one which has the confidence of the majority vote
                max_stages = proba.idxmax(axis=1)
                for j, stage in enumerate(max_stages):
                    proba.loc[j, stage] = info[4][j]
                # Normalize the probabilities to ensure they sum to 1 across each row
                proba = proba.div(proba.sum(axis=1), axis=0)
                proba.plot(kind="area", stacked=True, alpha=0.8, ax=axes[i], color=[stage_colors[stage] for stage in proba.columns])
                axes[i].set_title(name)
                axes[i].set_xlabel("Time (30-sec epoch)")
                axes[i].set_ylabel("Probability")
                axes[i].legend(loc='center left', bbox_to_anchor=(1.22, 0.5), borderaxespad=0, fontsize=17)
            else:
                proba.plot(kind="area", stacked=True, alpha=0.8, ax=axes[i], color=[stage_colors[stage] for stage in proba.columns])
                axes[i].set_title(name)
                axes[i].set_xlabel("Time (30-sec epoch)")
                axes[i].set_ylabel("Probability")
                axes[i].legend().remove()
                #axes[i].legend(loc='center left', bbox_to_anchor=(1.02, 0.5), borderaxespad=0)

        # Hide any unused axes
        for k in range(len(names), len(axes)):
            self.fig.delaxes(axes[k])
        self.fig.tight_layout()

        if Checkbox:
            # Save the hypnodensity figure to a PDF file
            filename = os.path.basename(info[2])
            name_without_extension = os.path.splitext(filename)[0]
            hypno_file_name = SavedDestination + name_without_extension + '_hypnodensity_plot.pdf'
            self.fig.savefig(hypno_file_name, format='pdf')

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
            self.figure.set_size_inches(10, 6)  # Set aspect ratio
            ### Plot the hypnogram
            # Define the layout for the plots
            gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])  # Three equal-height plots
            
            #confidence = cache['y_pred_new'].proba.max(axis=1)
            #print(confidence)
            # Adjust the layout to make each subplot bigger
            gs.update(wspace=0.01, hspace=0.4)
            # First subplot - Hypnogram
            labels_new = info[0]
            ax1 = self.figure.add_subplot(gs[0])
            ax1 = labels_new.plot_hypnogram(fill_color="gainsboro", ax=ax1)
            ax1.set_title('Expert Annotated Hypnogram', fontsize=12, fontweight='bold')
            ax1.set_xlabel('Time (h)')
            ax1.set_ylabel('Sleep stage')
            ax1.grid()

            # Second subplot - Estimated Hypnogram
            y_pred_new = info[1]
            ax2 = self.figure.add_subplot(gs[2])
            ax2 = y_pred_new.plot_hypnogram(fill_color="blue", ax=ax2)
            ax2.set_title('Estimated Hypnogram', fontsize=12, fontweight='bold')
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
            # Create heatmap with improved readability
            heatmap = sns.heatmap(cm_normalized, annot=True, fmt='.1f',
                                cmap='Blues', ax=ax3, cbar=True,
                                annot_kws={"size": 10, "weight": "regular"},
                                square=True, linewidths=0.6, linecolor='white')
            ax3.set_title('Confusion Matrix (%)', fontsize=12, fontweight='bold')
            ax3.set_xlabel('Predicted Label', fontsize=10)
            ax3.set_ylabel('True Label', fontsize=10)
            ax3.set_xticks(tick_marks)
            ax3.set_xticklabels(class_labels, fontsize=9, rotation=45, ha='right')
            ax3.set_yticks(tick_marks)
            ax3.set_yticklabels(class_labels, fontsize=9, rotation=0)

            # Improve colorbar
            cbar = heatmap.collections[0].colorbar
            cbar.set_label('Percentage (%)', fontsize=8)
            # Fourth subplot - Accuracy and Average Confidence
            ax4 = self.figure.add_subplot(gs[3])
            ax4.axis('off')
            # Add accuracy and average confidence text next to the subplots
            ax4.text(0.5, 0.5, f"Accuracy: {ResultsDataframe['Accuracy'].iloc[0]:.2f}%", transform=ax4.transAxes, fontsize=12, verticalalignment='center', horizontalalignment='center', fontweight='bold')
            ax4.text(0.5, 0.3, f"Avg Confidence: {ResultsDataframe['Average Confidence'].iloc[0]:.2f}%", transform=ax4.transAxes, fontsize=12, verticalalignment='center', horizontalalignment='center', fontweight='bold')
            ax4.text(0.5, 0.1, f"Kappa: {ResultsDataframe['kappa'].iloc[0]:.2f}", transform=ax4.transAxes, fontsize=12, verticalalignment='center', horizontalalignment='center', fontweight='bold')
                                # Adjust layout to add more space between subplots
            self.figure.tight_layout(pad=10.0)

            # Save the figure to a PDF file
            file_name = SavedDestination + name_without_extension + '.pdf'
            self.figure.savefig(file_name, format='pdf')

            # refresh canvas (only in GUI mode)
            if self.canvas is not None:
                self.canvas.draw()
            # Return the path to the updated Excel file
        else:
            export_results_file_path = None
            # Save the figure to a PDF file
            filename = info[2]
            #name_without_extension = os.path.splitext(filename)[0]
            hypno_file_name = filename + '_hypnodensity_plot.pdf'
            self.fig.savefig(hypno_file_name, format='pdf')


        return {
            'ExportResults': export_results_file_path
        }

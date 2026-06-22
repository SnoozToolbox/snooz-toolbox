"""EEG visualization components"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from .constants import *

class EEGVisualizer:
    """Handles EEG plotting and visualization"""
    
    def __init__(self, parent_widget):
        self.parent = parent_widget
        self.mne_plot_select_chs = None
        self.canvas_select_chs = None
        self.marked_bad_chs = []

    def cleanup(self):
        """Clean up EEG visualizer resources"""
        # Close MNE plot windows
        if self.mne_plot_select_chs:
            try:
                if hasattr(self.mne_plot_select_chs, 'close'):
                    self.mne_plot_select_chs.close()
                elif hasattr(self.mne_plot_select_chs, 'fig'):
                    import matplotlib.pyplot as plt
                    plt.close(self.mne_plot_select_chs.fig)
            except Exception:
                pass
            self.mne_plot_select_chs = None
        
        # Clear canvas
        self.canvas_select_chs = None
        
        # Clear marked channels
        self.marked_bad_chs.clear()

    def setup_visualization(self, raw_eeg, duration):
        """Setup EEG visualization with correct time scaling"""
        # Choose appropriate raw data for display
        if duration > SLEEP_RECORDING_THRESHOLD_SEC:
            # Use decimated version for long recordings
            if hasattr(self.parent.data_processor, 'raw_eeg_display'):
                display_raw = self.parent.data_processor.raw_eeg_display
            else:
                display_raw = raw_eeg
            # Show entire recording for sleep data
            plot_duration = duration
            plot_scales = PLOT_SCALES_SLEEP
        else:
            display_raw = raw_eeg
            plot_duration = PLOT_COMA_DURATION_SEC
            plot_scales = PLOT_SCALES_COMA

        # Set measurement date to avoid time offset issues
        display_raw.set_meas_date(0)
        
        self.mne_plot_select_chs = display_raw.plot(
            bad_color='red', 
            n_channels=DEFAULT_N_CHANNELS, 
            duration=plot_duration, 
            scalings=plot_scales, 
            show=False, 
            time_format='clock'
        )

        self.canvas_select_chs = FigureCanvas(self.mne_plot_select_chs.canvas.figure)
        self.canvas_select_chs.setFocusPolicy(Qt.StrongFocus)
        self.canvas_select_chs.setFocus()

        placeholder2 = self.parent.findChild(QWidget, "figure_placeholder2")
        self._setup_canvas_in_placeholder(placeholder2, self.canvas_select_chs)

        self.parent.NextButton2.setVisible(True)
        self.parent.textEdit_2.setVisible(True)
        self.parent.desc_label22.setVisible(True)
        self.parent.NextButton2.setEnabled(True)

    def get_bad_channels(self):
        """Get list of bad channels marked by user"""
        if self.mne_plot_select_chs:
            return self.mne_plot_select_chs.mne.info['bads']
        return []

    def _setup_canvas_in_placeholder(self, placeholder, canvas):
        """Setup canvas widget in placeholder"""
        if placeholder.layout():
            while placeholder.layout().count():
                child = placeholder.layout().takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            layout = placeholder.layout()
        else:
            layout = QVBoxLayout(placeholder)
        
        layout.addWidget(canvas)
        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        canvas.setSizePolicy(size_policy)
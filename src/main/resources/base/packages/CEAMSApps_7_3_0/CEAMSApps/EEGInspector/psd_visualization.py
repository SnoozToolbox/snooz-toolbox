"""PSD visualization components"""

from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from .constants import PSD_FMAX_HZ

class PSDVisualizer:
    """Handles PSD plotting and visualization"""
    
    def __init__(self, parent_widget):
        self.parent = parent_widget
        self.psd_plot = None
        self.canvas_psd = None

    def cleanup(self):
        """Clean up PSD visualizer resources"""
        # Close PSD plot
        if self.psd_plot:
            try:
                if hasattr(self.psd_plot, 'close'):
                    self.psd_plot.close()
                elif hasattr(self.psd_plot, 'fig'):
                    import matplotlib.pyplot as plt
                    plt.close(self.psd_plot.fig)
            except Exception:
                pass
            self.psd_plot = None
        
        # Clear canvas
        if self.canvas_psd:
            try:
                self.canvas_psd.deleteLater()
            except Exception:
                pass
            self.canvas_psd = None

    def setup_psd_plot(self, epochs, cutoff_freq):
        """Setup PSD visualization"""
        if not epochs:
            return

        # Plot Power Spectral Density
        max_freq_to_plot = min(PSD_FMAX_HZ, cutoff_freq)
        self.psd_plot = epochs.plot_psd(fmax=PSD_FMAX_HZ, exclude=['VREF'], show=False)
        self.canvas_psd = FigureCanvas(self.psd_plot.canvas.figure)

        # Setup canvas in placeholder
        placeholder4 = self.parent.findChild(QWidget, "figure_placeholder4")
        self._setup_canvas_in_placeholder(placeholder4, self.canvas_psd)

    def _setup_canvas_in_placeholder(self, placeholder, canvas):
        """Setup canvas widget in placeholder"""
        if placeholder.layout() is None:
            layout = QVBoxLayout()
            placeholder.setLayout(layout)
        else:
            layout = placeholder.layout()
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        layout.addWidget(canvas)
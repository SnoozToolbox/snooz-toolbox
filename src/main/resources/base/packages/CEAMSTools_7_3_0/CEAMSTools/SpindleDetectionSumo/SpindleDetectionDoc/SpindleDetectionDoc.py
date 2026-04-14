"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.
"""
"""
    SpindleDetectionDoc
    Description of the tool to detect spindles with the SUMO algorithm.
"""

from qtpy import QtWidgets
from qtpy.QtGui import QPixmap
import base64

from .Ui_SpindleDetectionDoc import Ui_SpindleDetectionDoc
from commons.BaseStepView import BaseStepView

class SpindleDetectionDoc( BaseStepView,  Ui_SpindleDetectionDoc, QtWidgets.QWidget):
    """
        SpindleDetectionDoc
        Description of the tool to detect spindles with the SUMO algorithm.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # init UI
        self.setupUi(self)
        self._load_embedded_pixmap()

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass

    def _load_embedded_pixmap(self):
        """Load the embedded base64 image data into the QLabel."""
        from .spindle_image_data import SPINDLE_IMAGE_BASE64
        
        # Decode base64 data to bytes
        image_bytes = base64.b64decode(SPINDLE_IMAGE_BASE64)
        
        # Create QPixmap from bytes
        pixmap = QPixmap()
        pixmap.loadFromData(image_bytes)
        self.spindle_image.setPixmap(pixmap)
"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
import base64
from qtpy.QtGui import QPixmap
"""
    SpindleDetectionDoc
    TODO CLASS DESCRIPTION
"""

from qtpy import QtWidgets

from CEAMSTools.SpindleDetectionMartin.SpindleDetectionDoc.Ui_SpindleDetectionDoc import Ui_SpindleDetectionDoc
from commons.BaseStepView import BaseStepView

class SpindleDetectionDoc( BaseStepView,  Ui_SpindleDetectionDoc, QtWidgets.QWidget):
    """
        SpindleDetectionDoc
        TODO CLASS DESCRIPTION
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        self._load_embedded_image()

    def _load_embedded_image(self):
        """Load the embedded base64 image data into spindle_image."""
        from .art_image_data import E0004_B1_01_05_0001_SMP303751_RES80_IMAGE_BASE64
        
        image_bytes = base64.b64decode(E0004_B1_01_05_0001_SMP303751_RES80_IMAGE_BASE64)
        pixmap = QPixmap()
        pixmap.loadFromData(image_bytes)
        self.spindle_image.setPixmap(pixmap)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass

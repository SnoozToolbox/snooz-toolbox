"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Settings viewer of the Intro plugin
"""

from qtpy import QtWidgets
from qtpy.QtGui import QPixmap
import base64

from CEAMSTools.DetectArtifacts.ArtIntroStepPL.Ui_ArtIntroStepPL import Ui_ArtIntroStepPL
from commons.BaseStepView import BaseStepView

class ArtIntroStepPL( BaseStepView,  Ui_ArtIntroStepPL, QtWidgets.QWidget):
    """
        ArtIntroStepPL displays the a few examples of artifact and describes the tool.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        self._load_embedded_images()

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass

    def _load_embedded_images(self):
        """Load the embedded base64 image data into the QLabel widgets."""
        from .art_image_data import (
            AMPLITUDE_IMAGE_BASE64,
            BURST_NOISE_IMAGE_BASE64,
            PERSISTENT_NOISE_IMAGE_BASE64,
            POWER_LINE_IMAGE_BASE64,
            BSL_VAR_IMAGE_BASE64,
            MUSCULAR_IMAGE_BASE64
        )
        
        # Map labels to their corresponding base64 image data
        image_mappings = {
            self.label_6: AMPLITUDE_IMAGE_BASE64,
            self.label_8: BURST_NOISE_IMAGE_BASE64,
            self.label_5: PERSISTENT_NOISE_IMAGE_BASE64,
            self.label_9: POWER_LINE_IMAGE_BASE64,
            self.label_10: BSL_VAR_IMAGE_BASE64,
            self.label_11: MUSCULAR_IMAGE_BASE64
        }
        
        # Load each image into its corresponding label
        for label, base64_data in image_mappings.items():
            image_bytes = base64.b64decode(base64_data)
            pixmap = QPixmap()
            pixmap.loadFromData(image_bytes)
            label.setPixmap(pixmap)
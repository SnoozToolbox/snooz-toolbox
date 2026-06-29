#! /usr/bin/env python3
"""
    SSWCIntroStep
    Settings viewer of the Intro plugin for the Slow Wave Classifier tool
"""
import base64
from qtpy.QtGui import QPixmap

from qtpy import QtWidgets

from CEAMSTools.SlowWaveClassification.SSWCIntroStep.Ui_SSWCIntroStep import Ui_SSWCIntroStep
from commons.BaseStepView import BaseStepView

class SSWCIntroStep( BaseStepView,  Ui_SSWCIntroStep, QtWidgets.QWidget):
    """
        SSWCIntroStep
        Displays the functionnalities of the slow wave classifier.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        self._load_embedded_image()

    def _load_embedded_image(self):
        """Load the embedded base64 image data into image_hist."""
        from .art_image_data import TRANSITION_FREQUENCY_IMAGE_BASE64
        
        image_bytes = base64.b64decode(TRANSITION_FREQUENCY_IMAGE_BASE64)
        pixmap = QPixmap()
        pixmap.loadFromData(image_bytes)
        self.image_hist.setPixmap(pixmap)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass

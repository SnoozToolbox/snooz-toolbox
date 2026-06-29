#! /usr/bin/env python3
"""
    SSWDIntroStep
    Settings viewer of the intro plugin for the Slow Wave Detector tool
"""
import base64
from qtpy.QtGui import QPixmap

from qtpy import QtWidgets

from CEAMSTools.SlowWaveDetection.SSWDIntroStep.Ui_SSWDIntroStep import Ui_SSWDIntroStep
from commons.BaseStepView import BaseStepView

class SSWDIntroStep( BaseStepView,  Ui_SSWDIntroStep, QtWidgets.QWidget):
    """
        IntrSSWDIntroStepoStep
        Displays the functionnalities of the slow wave detector.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)
        self._load_embedded_image()

    def _load_embedded_image(self):
        """Load the embedded base64 image data into label."""
        from .art_image_data import ONDE_LENTE_UI_SMALL_IMAGE_BASE64
        
        image_bytes = base64.b64decode(ONDE_LENTE_UI_SMALL_IMAGE_BASE64)
        pixmap = QPixmap()
        pixmap.loadFromData(image_bytes)
        self.label.setPixmap(pixmap)

    def load_settings(self):
        pass

    def on_apply_settings(self):
        pass

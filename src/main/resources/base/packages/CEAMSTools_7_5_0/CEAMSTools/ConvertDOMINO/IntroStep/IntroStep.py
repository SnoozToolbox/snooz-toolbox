#! /usr/bin/env python3
"""
    IntroStep
    To provide information to the user, how to use the tool.
    Only one text edit read only.
"""

from qtpy import QtWidgets

from CEAMSTools.ConvertDOMINO.IntroStep.Ui_IntroStep import Ui_IntroStep
from commons.BaseStepView import BaseStepView

class IntroStep(BaseStepView, Ui_IntroStep, QtWidgets.QWidget):
    """
        IntroStep
        To provide information to the user, how to use the tool.
        Only one text edit read only.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # init UI
        self.setupUi(self)

        
    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        pass


    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        pass


    def on_apply_settings(self):
        pass

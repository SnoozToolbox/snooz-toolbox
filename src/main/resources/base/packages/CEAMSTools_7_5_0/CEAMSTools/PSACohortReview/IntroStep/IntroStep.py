#! /usr/bin/env python3
"""
    IntroStep
    TODO CLASS DESCRIPTION
"""

from qtpy import QtWidgets

from CEAMSTools.PSACohortReview.IntroStep.Ui_IntroStep import Ui_IntroStep
from commons.BaseStepView import BaseStepView

class IntroStep(BaseStepView, Ui_IntroStep, QtWidgets.QWidget):
    """
        IntroStep
        TODO CLASS DESCRIPTION
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # If necessary, init the context. The context is a memory space shared by 
        # all steps of a tool. It is used to share and notice other steps whenever
        # the value in it changes. It's very useful when the parameter within a step
        # must have an impact in another step.
        #self._context_manager["context_IntroStep"] = {"the_data_I_want_to_share":"some_data"}
        
    def load_settings(self):
        # Load settings is called after the constructor of all steps has been executed.
        # From this point on, you can assume that all context has been set correctly.
        pass

    def on_topic_update(self, topic, message, sender):
        # Whenever a value is updated within the context, all steps receives a 
        # self._context_manager.topic message and can then act on it.
        #if topic == self._context_manager.topic:

            # The message will be the KEY of the value that's been updated inside the context.
            # If it's the one you are looking for, we can then take the updated value and use it.
            #if message == "context_some_other_step":
                #updated_value = self._context_manager["context_some_other_step"]
        pass
    

    def on_apply_settings(self):
        pass

"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    This plugin pass a value (which can be a constant, a dictionary or a list) to the next node.

    Inputs:
        signals
        sampling_rate

    Ouputs:
        signals

"""

from scipy import signal

from flowpipe import SciNode, InputPlug, OutputPlug

DEBUG = False

class Constant(SciNode):
    """
        Transmit a constant value

        Inputs:
            Constant: The constant value to transmit to the next node

        Ouputs:
            Constant: The constant value transmitted to the next node
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('Constant.__init__')
        InputPlug('constant', self)
        OutputPlug('constant', self)

    def subscribe_topics(self):
        pass

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'Constant.on_topic_update {topic}:{message}')

    def compute(self, constant):
        """
            Inputs:
                Constant: The constant value to transmit to the next node

            Ouputs:
                Constant: The constant value transmitted to the next node
        """
        if DEBUG: print('Constant.compute')
        
        # Log message for the Logs tab
        if DEBUG : 
            self._log_manager.log(self.identifier, f"{constant} in process...")    

        return {
            'constant': constant
        }
        
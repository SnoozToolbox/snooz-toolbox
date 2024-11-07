"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    This plugin extract only the signals with a specific Alias.

    Parameters
    -----------
        signals: A list of SignalModel
            The original list of signals to filter;
        alias:   String
            The alias of the signals to extract

    Returns
    -----------  
        signals: A list of SignalModel
            Signals using the alias defined in the input
        channels_name : A list of string 
            The list of channels linked to the input alias
"""

from scipy import signal

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException

DEBUG = False

class AliasSignals(SciNode):
    """
        This plugin extract only the signals with a specific Alias.

        Parameters
        -----------
            signals: A list of SignalModel
                The original list of signals to filter;
            alias:   String
                The alias of the signals to extract

        Returns
        -----------  
            signals: A list of SignalModel
                Signals using the alias defined in the input
            channels_name : A list of string 
                The list of channels linked to the input alias

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('AliasSignals.__init__')
        InputPlug('signals', self)
        InputPlug('alias', self)
        OutputPlug('signals', self)
        OutputPlug('channels_name', self)

    def subscribe_topics(self):
        pass

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'AliasSignals.on_topic_update {topic}:{message}')

    def compute(self, signals, alias):
        """
            Extract only the signals with a specific Alias.

            Parameters
            -----------
                signals: A list of SignalModel
                    The original list of signals to filter;
                alias:   String
                    The alias of the signals to extract

            Returns
            -----------  
                signals: A list of SignalModel
                    Signals using the alias defined in the input
                channels_name : A list of string 
                    The list of channels linked to the input alias
        """
        if DEBUG: print('AliasSignals.compute')

        if not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"AliasSignals input of wrong type. Expected: <class 'list'> received: {type(signals)}")

        output_signals = []
        channels_name = []
        
        # Only keep signals that matches the Alias
        for i, signal_model in enumerate(signals):
            if signal_model.alias == alias:
                # Copy the signal to avoid problems when referencing objects.
                alias_signal = signal_model.clone(clone_samples=True)
                output_signals.append(alias_signal)
                channels_name.append(signal_model.channel)

        return {
            'signals': output_signals,
            'channels_name' : channels_name
        }
        
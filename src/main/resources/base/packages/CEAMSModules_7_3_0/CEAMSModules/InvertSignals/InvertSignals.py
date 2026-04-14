"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    InvertSignals
    Class the invert signals.
    Useful to analyse the signals positive down as the sleep techs are usually exploring the EEG signals.
"""
import numpy as np

import config
from flowpipe.ActivationState import ActivationState
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from CEAMSModules.PSGReader.SignalModel import SignalModel

DEBUG = False

class InvertSignals(SciNode):
    """
    Class the invert signals.
    Useful to analyse the signals positive down as the sleep techs are usually exploring the EEG signals.

    Parameters
    ----------
        signals: List of SignalModel
            List of signal with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original
        
    Returns
    -------
        signals: List of SignalModel (inverted)
            List of signal with dictionary of channels with SignalModel with 
            properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original
        
        
    """
    def __init__(self, **kwargs):
        """ Initialize module InvertSignals """
        super().__init__(**kwargs)
        if DEBUG: print('InvertSignals.__init__')

        # Input plugs
        InputPlug('signals',self)
        # Output plugs
        OutputPlug('signals',self)
        self._is_master = False 
    

    def compute(self, signals):
        """
        Class the invert signals.
        Useful to analyse the signals positive down as the sleep techs are usually exploring the EEG signals.

        Parameters
        ----------
            signals: List of SignalModel
                List of signal with dictionary of channels with SignalModel with 
                properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original
            
        Returns
        -------
            signals: List of SignalModel (inverted)
                List of signal with dictionary of channels with SignalModel with 
                properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original
            
        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        if DEBUG: print('InvertSignals.compute')        
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None        

        if isinstance(signals,str) and signals=='':
            raise NodeInputException(self.identifier, "signals", f"InvertSignals this input is not connected.")
        elif not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"InvertSignals input of wrong type. Expected: <class 'list'> received: {type(signals)}")     

        # It is possible to bypass the inversion by passing the input signals directly
        # to the output signals without any modification
        if self.activation_state == ActivationState.BYPASS:
            return {
                'signals': signals
            }

        # Get list of channels in signals
        channel_lst = np.unique(SignalModel.get_attribute(signals, 'channel', None))
        new_signals = []
        for signal in signals:
            new_signal = signal.clone(clone_samples=True)
            new_signal.samples = -new_signal.samples
            new_signal.is_modified = True # Set the flag as modified otherwise it wont be written in the edf
            new_signals.append(new_signal)

        # Write the cache
        cache = {}
        if config.is_dev: # Avoid save of the recording when not developping
            cache['n_chan'] = len(channel_lst)
            cache['signals'] = new_signals
            self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'signals': new_signals
        }
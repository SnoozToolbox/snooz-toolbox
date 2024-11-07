"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    Insert samples from event dataframe inside a signals.

    Parameters
    -----------     
        signals : List
            List of SignalModel with properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original

        signals_events : List
            List of SignalModel with properties :
            These channels are SignalModel with properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original 

    Returns
    ----------- 
        new_signals: List
            List of SignalModel with properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original

"""

from flowpipe import SciNode, InputPlug, OutputPlug
from CEAMSModules.PSGReader.SignalModel import SignalModel
from commons.NodeInputException import NodeInputException

from math import *
import numpy as np


DEBUG = False

class ReplaceEventInSignals(SciNode):
    """
        Insert samples from event dataframe inside a signals.

        Parameters
        -----------     
            signals : List
                   List of SignalModel with properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original

            signals_events : List
                List of signals from events with dictionary of channels. 
                These channels are SignalModel with properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original 

        Returns
        ----------- 
            new_signals: signals : List
                   List of SignalModel with properties :
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
        super().__init__(**kwargs)
        if DEBUG: print('ReplaceEventInSignals.__init__')
        self._filename = None
        InputPlug('signals', self)
        InputPlug('signals_events', self)
        OutputPlug('new_signals', self)

    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass

    def compute(self, signals, signals_events):
        """
            Insert samples from event dataframe inside a signals.

            Parameters
            -----------     
                signals : List
                   List of SignalModel with properties :
                        name:           The name of the channel
                        samples:        The samples of the signal
                        alias:          The alias of the channel
                        sample_rate:    The sample rate of the signal
                        start_time:     The start time of the recording
                        montage_index:  The index of the montage used for this signal
                        is_modified:    Value caracterizing if the signal as been modify 
                                        from the original

                signals_events : List
                    List of SignalModel that have been modify. 
                    These channels are SignalModel with properties :
                        name:           The name of the channel
                        samples:        The samples of the signal
                        alias:          The alias of the channel
                        sample_rate:    The sample rate of the signal
                        start_time:     The start time of the recording
                        montage_index:  The index of the montage used for this signal
                        is_modified:    Value caracterizing if the signal as been modify 
                                        from the original 

            Returns
            ----------- 
                new_signals: List
                    List of SignalModel with properties :
                        name:           The name of the channel
                        samples:        The samples of the signal
                        alias:          The alias of the channel
                        sample_rate:    The sample rate of the signal
                        start_time:     The start time of the recording
                        montage_index:  The index of the montage used for this signal
                        is_modified:    Value caracterizing if the signal as been modify 
                                        from the original
        """

        if DEBUG: print('ReplaceEventInSignals.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None  

        # Verify inputs
        if isinstance(signals,str) and signals=='':
            err_message = "ERROR: signals not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals", \
                f"ReplaceEventInSignals this input is not connected.")
        if not isinstance(signals,list):
            err_message = "ERROR: signals unexpected type"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals", \
                f"ReplaceEventInSignals input of wrong type. Expected: <class 'list'> received: {type(signals)}")
        elif isinstance(signals, list) and len(signals)==0:
            return {'new_signals': []}
        
        if isinstance(signals_events,str) and signals_events=='':
            err_message = "ERROR: signals_events not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals_events", \
                f"ReplaceEventInSignals this input is not connected.")
        if not isinstance(signals_events,list):
            err_message = "ERROR: signals_events unexpected type"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals_events", \
                f"ReplaceEventInSignals input of wrong type. Expected: <class 'list'> received: {type(signals_events)}")
        elif isinstance(signals_events, list) and len(signals_events)==0:
            return {'new_signals': []}

        # The copy of the original signals
        new_signals = [signal.clone(clone_samples=True) for signal in signals]
        # List of SignalModel (the modified one) ordered (grouped) per chan (3 dimensions)
        signal_chan = SignalModel.get_attribute(signals_events, None, 'channel')
        # Unique list of channels modified
        chans = np.unique(SignalModel.get_attribute(signals_events, 'channel', 'channel'))
        # total number of channels in the original signals
        n_tot_chan = np.unique(SignalModel.get_attribute(signals, 'channel', 'channel'))
        
        # For every original signals (probably an item per channel for the whole night)
        for signal in new_signals:
            signal.is_modified = True
            # Index of the current channel if modified
            idx = np.where(signal.channel == chans)[0]
            if len(idx) != 0:
                # For every signal_event for the current channel
                for signal_event in signal_chan[idx[0]]:
                    start = int(signal_event.start_time * signal_event.sample_rate)
                    end = int(signal_event.end_time * signal_event.sample_rate)
                    # Overwrite the original samples with the modified ones
                    signal.samples[start:end] = signal_event.samples
        
        # Write the cache
        cache = {}
        cache['n_chan'] = len(n_tot_chan)
        cache['signals'] = new_signals
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {'new_signals': new_signals}
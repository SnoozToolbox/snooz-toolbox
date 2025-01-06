"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Find the mutual information between two lists of signals.
    Parameters
    -----------
        signals1: List of SignalModel 
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
        signals2: List of SignalModel 
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
    -----------    
        mutual_info : List of SignalModel 
            List of mutual info score for each window in each index of the list

"""

from flowpipe import SciNode, InputPlug, OutputPlug
from CEAMSModules.PSGReader.SignalModel import SignalModel
from sklearn.metrics import mutual_info_score
import numpy as np
from tqdm import tqdm
from commons.NodeInputException import NodeInputException

DEBUG = False

class MutualInfo(SciNode):
    """
        Find the mutual information between two lists of signals.
        Parameters
        -----------
            signals1: List of SignalModel
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
            signals2: List of SignalModel
                List of signal with dictionary of channels with SignalModel with 
                properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                                    from the original

        Returns
        -----------    
            mutual_info : List of SignalModel
                List of mutual info score for each window in each index of the list
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('MutualInfo.__init__')
        self._filename = None
        InputPlug('signals1', self)
        InputPlug('signals2', self)  
        OutputPlug('mutual_info', self)


    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass


    def compute(self, signals1, signals2):
        """
            Find the mutual information between two lists of signals.
            Parameters
            -----------
                signals1: List of SignalModel
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
                signals2: List of SignalModel
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
            -----------    
                mutual_info : List of SignalModel
                    List of mutual info score for each window in each index of the list
        """

        if DEBUG: print('MutualInfo.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None             

        # Verify inputs
        if isinstance(signals1,str) and signals1=='':
            err_message = "ERROR: signals not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals1", \
                f"MutualInfo this input is not connected.")
        if not isinstance(signals1,list):
            err_message = "ERROR: signals unexpected type"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals1", \
                f"MutualInfo input of wrong type. Expected: <class 'list'> received: {type(signals1)}")
        elif isinstance(signals1, list) and len(signals1)==0:
            return {'mutual_info': []}
        if isinstance(signals2,str) and signals2=='':
            err_message = "ERROR: signals not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals2", \
                f"MutualInfo this input is not connected.")
        if not isinstance(signals2,list):
            err_message = "ERROR: signals unexpected type"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals2", \
                f"MutualInfo input of wrong type. Expected: <class 'list'> received: {type(signals2)}")
        elif isinstance(signals2, list) and len(signals2)==0:
            return {'mutual_info': []}

        # Sort List of SignalModel per start_time
        signals1_event = SignalModel.get_attribute(signals1, None, 'start_time')
        signals2_event = SignalModel.get_attribute(signals2, None, 'start_time')

        # Create a list of SignalModel copied from signals1
        mutual_info = [signal.clone(clone_samples=True) for signal in signals1] 
        mutual_info = SignalModel.get_attribute(mutual_info, None, 'start_time')

        for signal1, signal2, mi in zip(signals1_event, signals2_event, mutual_info):
            # Extract samples
            samples1 = SignalModel.get_attribute(signal1, 'samples', None)
            samples2 = SignalModel.get_attribute(signal2, 'samples', None)
                
            # Make sure signals have the same number of samples
            if not samples1.shape[1] == samples2.shape[1]:
                err_message = "ERROR: Signals with different numbers of samples"
                self._log_manager.log(self.identifier, err_message)
                print('MutualInfo ' + err_message)
                return {'mutual_info': []}

            # Compute mutual information for each combination
            combine_signals = [[x,y] for x in samples1 for y in samples2]
            mutual_info_event = [mutual_info_score(combine_signal[0], combine_signal[1], contingency=None) for combine_signal in combine_signals]
            # Save answer in new SignalModel with both signal in samples and mutual info in meta
            for sig_mut, mut_inf in zip(mi, mutual_info_event):
                sig_mut.meta['mutual_info'] = mut_inf

        mutual_info = mutual_info.flatten()
        # Write the cache
        cache = {}
        cache['scores'] = mutual_info
        cache['n_chan'] = SignalModel.get_attribute(mutual_info, 'channel', 'start_time').shape[1]
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {'mutual_info': mutual_info}
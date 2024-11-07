"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    Reconstruct Signal from ICA components. 

    Parameters
    -----------     
        signals : List
            List of signals put in IcaComponents with dictionary of channels. 
            These channels are SignalModel with properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original

        components : List
            List of componants with dictionary of channels. These channels are
            SignalModel with properties :
                name:           The name of the channel
                samples:        The samples of the signal
                alias:          The alias of the channel
                sample_rate:    The sample rate of the signal
                start_time:     The start time of the recording
                montage_index:  The index of the montage used for this signal
                is_modified:    Value caracterizing if the signal as been modify 
                                from the original
            
        epochs_to_process : pandas DataFrame
            df of epochs with field 
            'group': Group of events this event is part of (String)
            'name': Name of the event (String)
            'start_sec': Starting time of the event in sec (Float)
            'duration_sec': Duration of the event in sec (Float)
            'channels' : Channel where the event occures (String)

    Returns
    ----------- 
        signals_reconstruct: List
            List of componants with dictionary of channels. These channels are 
            SignalModel with properties :
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
from sklearn import decomposition
from tqdm import tqdm


DEBUG = False

class IcaRestore(SciNode):
    """
        Reconstruct Signal from ICA components. 

        Parameters
        -----------     
            signals : List
                List of signals put in IcaComponents with dictionary of channels. 
                These channels are SignalModel with properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original

            components : List
                List of componants with dictionary of channels. These channels are
                SignalModel with properties :
                    name:           The name of the channel
                    samples:        The samples of the signal
                    alias:          The alias of the channel
                    sample_rate:    The sample rate of the signal
                    start_time:     The start time of the recording
                    montage_index:  The index of the montage used for this signal
                    is_modified:    Value caracterizing if the signal as been modify 
                                    from the original
                
            epochs_to_process : pandas DataFrame
                df of epochs with field 
                'group': Group of events this event is part of (String)
                'name': Name of the event (String)
                'start_sec': Starting time of the event in sec (Float)
                'duration_sec': Duration of the event in sec (Float)
                'channels' : Channel where the event occures (String)

        Returns
        ----------- 
            signals_reconstruct: List
                List of componants with dictionary of channels. These channels are 
                SignalModel with properties :
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
        if DEBUG: print('IcaRestore.__init__')
        self._filename = None
        InputPlug('signals', self)
        InputPlug('components', self)
        InputPlug('epochs_to_process', self)
        OutputPlug('signals_reconstruct', self)


    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass

    def compute(self, signals, components, epochs_to_process):
        """
            Reconstruct Signal from ICA components. 

            Parameters
            -----------     
                signals : List
                    List of signals put in IcaComponents with dictionary of channels. 
                    These channels are SignalModel with properties :
                        name:           The name of the channel
                        samples:        The samples of the signal
                        alias:          The alias of the channel
                        sample_rate:    The sample rate of the signal
                        start_time:     The start time of the recording
                        montage_index:  The index of the montage used for this signal
                        is_modified:    Value caracterizing if the signal as been modify 
                                        from the original

                components : List
                    List of componants with dictionary of channels. These channels are
                    SignalModel with properties :
                        name:           The name of the channel
                        samples:        The samples of the signal
                        alias:          The alias of the channel
                        sample_rate:    The sample rate of the signal
                        start_time:     The start time of the recording
                        montage_index:  The index of the montage used for this signal
                        is_modified:    Value caracterizing if the signal as been modify 
                                        from the original
                    
                epochs_to_process : pandas DataFrame
                    df of epochs with field 
                    'group': Group of events this event is part of (String)
                    'name': Name of the event (String)
                    'start_sec': Starting time of the event in sec (Float)
                    'duration_sec': Duration of the event in sec (Float)
                    'channels' : Channel where the event occures (String)

            Returns
            ----------- 
                signals_reconstruct: List
                    List of componants with dictionary of channels. These channels are 
                    SignalModel with properties :
                    name:           The name of the channel
                        samples:        The samples of the signal
                        alias:          The alias of the channel
                        sample_rate:    The sample rate of the signal
                        start_time:     The start time of the recording
                        montage_index:  The index of the montage used for this signal
                        is_modified:    Value caracterizing if the signal as been modify 
                                        from the original

        """

        if DEBUG: print('IcaRestore.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None  

        # Verify inputs
        if isinstance(signals,str) and signals=='':
            err_message = "ERROR: signals not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals", \
                f"SignalsFromEvents this input is not connected.")
        if not isinstance(signals,list):
            err_message = "ERROR: signals unexpected type"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals", \
                f"SignalsFromEvents input of wrong type. Expected: <class 'list'> received: {type(signals)}")
        elif isinstance(signals, list) and len(signals)==0:
            return {'signals_reconstruct': []}
        
        if isinstance(components,str) and components=='':
            err_message = "ERROR: components not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "components", \
                f"SignalsFromEvents this input is not connected.")
        if not isinstance(components,list):
            err_message = "ERROR: components unexpected type"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "components", \
                f"SignalsFromEvents input of wrong type. Expected: <class 'list'> received: {type(components)}")
        elif isinstance(components, list) and len(components)==0:
            return {'signals_reconstruct': []}

        if isinstance(epochs_to_process, str) and epochs_to_process == '':
            err_message = "ERROR: epochs_to_process not connected"
            self._log_manager.log(self.identifier, err_message)
            return {'signals_reconstruct': []}

        components_events = SignalModel.get_attribute(components, None, 'start_time')        
        signals_reconstruct = [signal.clone(clone_samples=True) for signal in signals]
        signals_reconstruct = SignalModel.get_attribute(signals_reconstruct, None, 'start_time')

        for signal, component in zip(signals_reconstruct, components_events):
            if signal[0].start_time in np.array(epochs_to_process.start_sec):
                samples_cmp_events = SignalModel.get_attribute(component, 'samples', None)
                # Reconstruct signal from infomax ICA decomposition
                if isinstance(component[0].meta['transformer'],np.ndarray):
                    # mixer = [n_channels, n_components]
                    mixer = component[0].meta['transformer']
                    # Apply inverse transform to reconstruct signal without the components attenuated
                    reconstruct_cmp = np.dot(mixer, np.vstack(samples_cmp_events))
                # Reconstruct signal from fastICA decomposition
                elif isinstance(component[0].meta['transformer'],decomposition._fastica.FastICA):
                    # inverse_transform 
                    #   input : X_data as array-like of shape (n_samples, n_components)
                    #   returns : X_new as ndarray of shape (n_samples, n_features)
                    X_data = np.transpose(np.vstack(samples_cmp_events))
                    X_new = component[0].meta['transformer'].inverse_transform(X_data)
                    reconstruct_cmp = np.transpose(X_new)
                else:
                    raise NodeInputException(self.identifier, "components", \
                        f"Components input of wrong type. Expected: <class 'numpy.ndarray'> or <class 'sklearn.decomposition._fastica.FastICA'> received: {type(component[0].meta['transformer'])}")
                for i, chan in enumerate(signal):
                    chan.samples = reconstruct_cmp[i,:]
                    chan.is_modified = True
                    chan.meta['transformer'] = component[0].meta['transformer']
        
        signals_reconstruct = list(np.hstack(signals_reconstruct))
        channel_events = SignalModel.get_attribute(signals_reconstruct, 'channel', 'start_time')

        # Write the cache
        cache = {}
        cache['n_chan'] = len(channel_events[0])
        cache['signals'] = signals_reconstruct
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {'signals_reconstruct': signals_reconstruct}

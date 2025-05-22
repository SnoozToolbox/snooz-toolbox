"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Create a list of dictionnaries with the channels (each of them are 
    SignalModel) from specific epochs during a recording. Each signal is 
    rescale according to a specific approach.
    Parameters
    -----------
        signals : List
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
        scaling_approach : String
            String of the desired scaling approach to rescale signals.
        parameters : Dict
            Dictionnary of all the parameters associated with the scaling 
            approach.

    Returns
    -----------    
        signals_rescale : List
            List of Dict containing channel with SignalModel where the signal
            have been rescale.
"""

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from CEAMSModules.PSGReader.SignalModel import SignalModel
from sklearn.preprocessing import MinMaxScaler, StandardScaler, KBinsDiscretizer
import numpy as np
import pandas as pd

DEBUG = False

class RescaleSignal(SciNode):
    """
        Create a list of dictionnaries with the channels (each of them are 
        SignalModel) from specific epochs during a recording. Each signal is 
        rescale according to a specific approach.
        Parameters
        -----------
            signals : List
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
            scaling_approach : String
                String of the desired scaling approach to rescale signals.
            parameters : Dict
                Dictionnary of all the parameters associated with the scaling 
                approach.

        Returns
        -----------    
            signals_rescale : List
                List of Dict containing channel with SignalModel where the signal
                have been rescale.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('RescaleSignal.__init__')
        self._filename = None
        InputPlug('signals', self)
        InputPlug('scaling_approach', self)
        InputPlug('parameters', self)     
        OutputPlug('signals_rescale', self)


    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass


    def compute(self, signals, scaling_approach, parameters):
        """
            Create a list of dictionnaries with the channels (each of them are 
            SignalModel) from specific epochs during a recording. Each signal is 
            rescale according to a specific approach.
            Parameters
            -----------
                signals : List
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
                scaling_approach : String
                    String of the desired scaling approach to rescale signals.
                parameters : Dict
                    Dictionnary of all the parameters associated with the scaling 
                    approach.

            Returns
            -----------    
                signals_rescale : List
                    List of Dict containing channel with SignalModel where the signal
                    have been rescale.
        """

        if DEBUG: print('RescaleSignal.compute')
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
            return {'signals_rescale': []}

        # Initialize new signals
        signals_rescale = [signal.clone(clone_samples=False) for signal in signals]
        samples_events = np.transpose(SignalModel.get_attribute(signals, 'samples', None))

        if scaling_approach == 'Normalization':
            feature_range = (parameters['min'], parameters['max'])
            copy_para = parameters['copy']
            clip = parameters['clip']
            scaler = MinMaxScaler(feature_range=feature_range, copy=copy_para, clip=clip)
            rescale = np.transpose(scaler.fit_transform(samples_events, y=None))

        elif scaling_approach == 'Standardization':
            copy_para = parameters['copy']
            with_mean = parameters['with_mean']
            with_std = parameters['with_std']
            scaler = StandardScaler(copy=copy_para, with_mean=with_mean, with_std=with_std)
            rescale = np.transpose(scaler.fit_transform(samples_events, y=None))
        
        elif scaling_approach == 'Discretization':
            n_bins = parameters['n_bins']
            encode = parameters['encode']
            strategy = parameters['strategy']
            dtype = parameters['dtype']
            scaler = KBinsDiscretizer(n_bins=n_bins, encode=encode, strategy=strategy, dtype=dtype)
            rescale = np.transpose(scaler.fit_transform(samples_events, y=None))

        # Extract signal from each event
        for i, signal in enumerate(signals_rescale):
            signal.samples = rescale[i,:]

        # Write the cache
        cache = {}
        cache['signals'] = signals_rescale
        cache['n_chan'] = SignalModel.get_attribute(signals_rescale, 'channel', 'start_time').shape[1]

        self._cache_manager.write_mem_cache(self.identifier, cache)
        return {'signals_rescale': signals_rescale}
    
    

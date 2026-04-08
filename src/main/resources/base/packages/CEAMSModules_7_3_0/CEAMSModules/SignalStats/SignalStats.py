"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    SignalStats
    Compute the mean and standard deviation of the input signals per epoch, per channel.
    For each epoch (each item in the `SignalModel` list), the module calculates the mean and standard deviation.
    The module accepts NaN values in the signals and will ignore them in the calculations.

"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import numpy as np

DEBUG = False

class SignalStats(SciNode):
    """
    Compute the mean and standard deviation of the input signals per epoch, per channel.
    For each epoch (each item in the `SignalModel` list), the module calculates the mean and standard deviation.
    The module accepts NaN values in the signals and will ignore them in the calculations.

    Parameters
    ----------
        signals : List of SignalModel
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
        stats: dict
        A dictionary containing statistical properties of the signals.
        - 'mean': List of mean values computed from the input signals.
        - 'std': List of standard deviation values computed from the input signals.    
    """

    def __init__(self, **kwargs):
        """ Initialize module SignalStats """
        super().__init__(**kwargs)
        if DEBUG: print('SignalStats.__init__')

        # Input plugs
        InputPlug('signals',self)
        

        # Output plugs
        OutputPlug('stats',self)
        

        # Init module variables
        self.this_is_an_example_you_can_delete_it = 0

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, signals):
        """
        Compute the mean and standard deviation of the input signals per epoch, per channel.
        For each epoch (each item in the `SignalModel` list), the module calculates the mean and standard deviation.
        The module accepts NaN values in the signals and will ignore them in the calculations.

        Parameters
        ----------
            signals : List of SignalModel
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
            stats: dict
            A dictionary containing statistical properties of the signals.
            - 'mean': List of mean values computed from the input signals.
            - 'std': List of standard deviation values computed from the input signals.
        
            
        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """

        if DEBUG: 
            print('SignalStats.compute')

        if isinstance(signals, str) and signals=='':
            raise NodeInputException(self.identifier, "signals", \
                f"SignalStats this input is empty, no signals no spindles.")   

        # Calculate mean and std of signal epochs 
        mean = [np.nanmean(x.samples) for x in signals]
        std = [np.nanstd(x.samples) for x in signals]

        # Write to the cache to use the data in the resultTab
        # cache = {}
        # cache['this_is_a_key'] = 42
        # self._cache_manager.write_mem_cache(self.identifier, cache)

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module does nothing.")

        return {
            'stats': {
                'mean': mean,
                'std': std
            }
        }
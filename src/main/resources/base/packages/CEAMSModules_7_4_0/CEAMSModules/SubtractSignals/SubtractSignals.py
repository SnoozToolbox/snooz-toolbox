"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Subtract signals from a specific channel from the signals of a list of channels.
    This module can be used to reformat a montage.
    For example, to reformat C3-CLE to C3-A2, the input channel is [C3-CLE], and the channel to subtract is [A2-CLE].
    To rename properly the channel, the new channel name can be provided.
"""
import numpy as np
import pandas as pd

import config
from flowpipe import SciNode, InputPlug, OutputPlug
from flowpipe.ActivationState import ActivationState
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from CEAMSModules.PSGReader.SignalModel import SignalModel

DEBUG = False

class SubtractSignals(SciNode):
    """"
    Subtract a signal to others.

    Parameters
    -----------
        signals: List
            List of SignalModel and their informations
            Properties:
                samples:np.array
                    List of samples
                start_time:float 
                    Start time in seconds of the signal in relation to the beginning 
                    of the recording.
                end_time:float
                    End time in seconds of the signal in relation to the beginning 
                    of the recording.
                duration:float
                    Duration in seconds of the signal.
                sample_rate:float
                    Sampling rate of the signal
                channel:str
                    Name of the channel
                alias:str
                    Channel alias.
                meta:dict
                    Optional information about this signal
                is_modified:bool
                    Has the signal been modified or not.
        channel: String or List of strings (usually the output of Alias Signals)
            A string with the name of the initial channels. Can be multiple split with ";"
        channel_to_sub: String or a list of strings
            A string with the name of the channel to Subtract
        new_channel_name : String (let empty to use the default channel name)
            To rename the new Subtracted channel.
            Valid only when a single channel is Subtracted.
            
    Returns
    -----------    
        new_signal: List
            List of SignalModel and their informations
            Properties:
                samples:np.array
                    List of samples
                start_time:float 
                    Start time in seconds of the signal in relation to the beginning 
                    of the recording.
                end_time:float
                    End time in seconds of the signal in relation to the beginning 
                    of the recording.
                duration:float
                    Duration in seconds of the signal.
                sample_rate:float
                    Sampling rate of the signal
                channel:str
                    Name of the channel
                alias:str
                    Channel alias.
                meta:dict
                    Optional information about this signal
                is_modified:bool
                    Has the signal been modified or not.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('SubtractSignals.__init__')
        self._filename = None
        InputPlug('signals', self)
        InputPlug('channel', self)
        InputPlug('channel_to_sub', self)       
        InputPlug('new_channel_name', self)       
        OutputPlug('new_signals', self)


    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass


    def compute(self, signals, channel, channel_to_sub, new_channel_name):
        """"
            Subtract a signal to others.

            Parameters
            -----------
                signals: List
                    List of SignalModel and their informations
                    Properties:
                        samples:np.array
                            List of samples
                        start_time:float 
                            Start time in seconds of the signal in relation to the beginning 
                            of the recording.
                        end_time:float
                            End time in seconds of the signal in relation to the beginning 
                            of the recording.
                        duration:float
                            Duration in seconds of the signal.
                        sample_rate:float
                            Sampling rate of the signal
                        channel:str
                            Name of the channel
                        alias:str
                            Channel alias.
                        meta:dict
                            Optional information about this signal
                        is_modified:bool
                            Has the signal been modified or not.
                channel: String or List of strings (usually the output of Alias Signals)
                    A string with the name of the initial channels. Can be multiple split with ";"
                channel_to_sub: String or a list of strings
                    A string with the name of the channel to Subtract
                new_channel_name : String (let empty to use the default channel name)
                    To rename the new Subtracted channel.
                    Valid only when a single channel is Subtracted.
                    
            Returns
            -----------    
                new_signal: List
                    List of SignalModel and their informations
                    Properties:
                        samples:np.array
                            List of samples
                        start_time:float 
                            Start time in seconds of the signal in relation to the beginning 
                            of the recording.
                        end_time:float
                            End time in seconds of the signal in relation to the beginning 
                            of the recording.
                        duration:float
                            Duration in seconds of the signal.
                        sample_rate:float
                            Sampling rate of the signal
                        channel:str
                            Name of the channel
                        alias:str
                            Channel alias.
                        meta:dict
                            Optional information about this signal
                        is_modified:bool
                            Has the signal been modified or not.
            """

        if DEBUG: print('SubtractSignals.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None        

        if isinstance(signals,str) and signals=='':
            raise NodeInputException(self.identifier, "signals", f"SubtractSignals this input is not connected.")
        elif not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"SubtractSignals input of wrong type. Expected: <class 'list'> received: {type(signals)}")     

        # It is possible to bypass the filter by passing the input signals directly
        # to the output signals without any modification
        if self.activation_state == ActivationState.BYPASS:
            return {
                'signals': signals
            }

        # When channels are not specified
        if channel=='':   
            err_message = " ERROR: channels are not defined, the Subtraction is not done, the signals input is forward to the output."
            self._log_manager.log(self.identifier, err_message)
            return {'new_signals': signals}
        if channel_to_sub=='':   
            err_message = " ERROR: channel_to_sub are not defined, the Subtraction is not done, the signals input is forward to the output."
            self._log_manager.log(self.identifier, err_message)
            return {'new_signals': signals}

        # Get list of channels in signals
        channel_lst = np.unique(SignalModel.get_attribute(signals, 'channel', None))
        # Make sure the channels in channel and channel_to_sub (if any) are in channel_lst
        if isinstance(channel, str):
            channel = [channel]
        if isinstance(channel_to_sub, str):
            channel_to_sub = [channel_to_sub]
        if isinstance(channel, list):
            channel = [c for c in channel if c in channel_lst]
        if isinstance(channel_to_sub, list):
            channel_to_sub = [c for c in channel_to_sub if c in channel_lst]

        if len(channel)==0:
            raise NodeRuntimeException(self.identifier, "channel", \
                f"channels are empty or not found in the signals, the current subject is skipped.") 
        if len(channel_to_sub)>1:
            raise NodeRuntimeException(self.identifier, "channel_to_sub", \
                f"More than one channel_to_sub, the current subject is skipped.")             

        if isinstance(new_channel_name, list): 
            if len(new_channel_name)>1:
                err_message = " ERROR: new_channel_name is a list multiple names are not allowed, the default name is used."
                self._log_manager.log(self.identifier, err_message)
                new_channel_name = ''
            else:
                new_channel_name = new_channel_name[0]

        #---------------------------------------------------------------------------
        # Extract the signals from each channel
        #---------------------------------------------------------------------------
        new_signals = []
        for cur_channel in channel:
            signal_chan_1 = SignalModel.get_attribute(signals, None, 'channel', value_to_test=cur_channel)
            if len(channel_to_sub)==0:
                for signal_1 in signal_chan_1:
                    new_signals.append(signal_1)
            else:
                signal_chan_2 = SignalModel.get_attribute(signals, None, 'channel', value_to_test=channel_to_sub[0])
                for signal_1, signal2 in zip(signal_chan_1, signal_chan_2):
                    # Test for sampling rate and duration with the shape
                    if signal_1.samples.shape != signal2.samples.shape:
                        err_message = "ERROR: The signals have different shapes"
                        self._log_manager.log(self.identifier, err_message)
                        return {'new_signals': ''}        
                    else:
                        # Clone the signal from signal1 to have a valid strat_time, duration and so on...
                        new_signal = signal_1.clone(clone_samples=True)
                        # Subtract
                        new_signal.samples = new_signal.samples - signal2.samples
                        new_signal.is_modified = True # Set the flag as modified otherwise it wont be written in the edf
                        # Rename the channel if possible
                        if len(new_channel_name) > 0:
                            new_signal.channel = new_channel_name
                        else:
                            #new_signal.channel = new_signal.channel + ' - ' + signal_chan_1.channel
                            new_signal.channel = new_signal.channel + ' - ' + signal2.channel
                        
                        new_signals.append(new_signal)                   

        # Write the cache
        cache = {}
        if config.is_dev: # Avoid save of the recording when not developping
            cache['n_chan'] = len(channel)
            cache['signals'] = new_signals
            self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'new_signals': new_signals
        }


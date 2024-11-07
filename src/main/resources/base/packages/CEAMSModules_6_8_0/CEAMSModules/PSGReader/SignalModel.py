"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    The model of a signal. Contains the signal and its informations

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
DEBUG = False
import numpy as np

class SignalModel:
    """
        The model of a signal. Contains the signal and its informations

        Properties:
        -----------
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
        montage_index:int
            Which montage is this signal from.
            
    """
    def __init__(self):
        self.samples = np.empty(0)
        self.start_time = float(0)
        self.end_time = float(0)
        self.duration = float(0)
        self.sample_rate = float(0)
        self.channel = ''
        self.alias = ''
        self.meta = {}
        self.is_modified = False
        self.montage_index = 0

    def clone(self, clone_samples=False):
        new_signal = SignalModel()

        if clone_samples:
            new_signal.samples = self.samples.copy()

        new_signal.start_time = self.start_time
        new_signal.end_time = self.end_time
        new_signal.duration = self.duration
        new_signal.sample_rate = self.sample_rate
        new_signal.channel = self.channel
        new_signal.alias = self.alias
        new_signal.meta = self.meta.copy()
        new_signal.is_modified = self.is_modified
        new_signal.montage_index = self.montage_index

        return new_signal

    def get_attribute(signals, attr, group_by, value_to_test=None):
        """
        Get or Group in a list the desired attribute in the list of SignalModel
        * To use get_attribute(signals, 'samples', 'channel', 'c3') all the samples must have the same dimension.

        Parameters
        -----------
            signals : a list of SignalModel
            attr : The desired attribute. If None, will return the list of SignalModel (signals)
            group_by : Attribute to group by. If None, just the desired 
                       attribute is get from list [String]
            value_to_test : Select the attr with the value_to_test

        Returns
        -----------    
            attribute_list : a list of attribute
        """
        # Extract one attribute and convert it in an array
        #   ex) samples1 = SignalModel.get_attribute(signals, 'samples', None)
        if (not attr == None) and (group_by == None) and (value_to_test == None):
            try :
                attribute_list = np.array([getattr(signal, attr) for signal in signals])
            except :
                # When the shape cannot be converted into an numpy array, keep it in list
                attribute_list = [getattr(signal, attr) for signal in signals]
        # Group the list of dict (SignalModel) by the attribute group_by and convert it in an array
        #   ex) signals_events = SignalModel.get_attribute(signals, None, 'start_time')
        elif (not group_by == None) and (attr == None) and (value_to_test == None):
            condition = np.vstack([getattr(signal, group_by) for signal in signals])
            unq_condition = np.unique(condition)
            attribute_list = np.array([[signal for signal in signals if getattr(signal, group_by) == cond] for cond in unq_condition])
        elif (not group_by == None) and (attr == None) and (not value_to_test == None):
            condition = np.vstack([getattr(signal, group_by) for signal in signals])
            unq_condition = np.unique(condition)
            attribute_list = np.array([[signal for signal in signals if getattr(signal, group_by) == cond] for cond in unq_condition])
            for i in range(len(attribute_list)):
                if getattr(attribute_list[i][0],group_by)==value_to_test:
                    return attribute_list[i]
            return None
        # No modification
        elif (group_by == None) and (attr == None) and (value_to_test == None):
            attribute_list = signals
        # Extract the unique values of an attribute
        #   start_events = np.unique(SignalModel.get_attribute(signals, 'start_time', 'start_time'), axis=1)
        elif (not attr == None) and (not group_by == None) and (value_to_test == None):
            condition = np.vstack([getattr(signal, group_by) for signal in signals])
            unq_condition = np.unique(condition)
            attribute_list = np.array([[getattr(signal, attr) for signal in signals if getattr(signal, group_by) == cond] for cond in unq_condition])
        # Extract the only attr that match the value_to_test
        #   ex) fs_chan = SignalModel.get_attribute(signals, 'sample_rate', 'chan_label', channel)
        else:
            attribute_list = np.array([[ getattr(signal, attr) for signal in signals if getattr(signal, group_by) == value_to_test ] ])
        return attribute_list


    def is_vectorizable(signals, same_events):
        """
        Check if list of objects can be vectorize

        Parameters
        -----------
            signals : A list of SignalModel
            same_events : Bool if all signalModel in list should be from a same event

        Returns
        -----------    
            vectorizable : Bool
        """
        samples_len = np.vstack([len(signal.samples) for signal in signals])
        if same_events:
            start_times = np.vstack([signal.start_time for signal in signals])
            duration_times = np.vstack([signal.duration for signal in signals])
            vectorizable = np.all(start_times == start_times[0]) and np.all(duration_times == duration_times[0]) and np.all(samples_len == samples_len[0])
        else:
            vectorizable = np.all(samples_len == samples_len[0])

        return vectorizable

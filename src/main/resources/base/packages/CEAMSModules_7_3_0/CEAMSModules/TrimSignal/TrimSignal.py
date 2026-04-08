"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    TrimSignal
    TODO CLASS DESCRIPTION
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from flowpipe.ActivationState import ActivationState
import pandas as pd
import copy
DEBUG = False

class TrimSignal(SciNode):
    """
    TODO CLASS DESCRIPTION

    Parameters
    ----------
        signals: TODO TYPE
            TODO DESCRIPTION
        events: TODO TYPE
            TODO DESCRIPTION
        start_sec: TODO TYPE
            TODO DESCRIPTION
        duration_sec: TODO TYPE
            TODO DESCRIPTION
        reset_time: TODO TYPE
            TODO DESCRIPTION
        

    Returns
    -------
        signals: TODO TYPE
            TODO DESCRIPTION
        events: TODO TYPE
            TODO DESCRIPTION
        
    """
    def __init__(self, **kwargs):
        """ Initialize module TrimSignal """
        super().__init__(**kwargs)
        if DEBUG: print('TrimSignal.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('events',self)
        InputPlug('start_sec',self)
        InputPlug('duration_sec',self)
        InputPlug('reset_time',self)
        

        # Output plugs
        OutputPlug('signals',self)
        OutputPlug('events',self)
        

        # Init module variables
        self.this_is_an_example_you_can_delete_it = 0

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, signals, events, start_sec, duration_sec, reset_time=True):
        """
        TODO DESCRIPTION

        Parameters
        ----------
            signals: TODO TYPE
                TODO DESCRIPTION
            events: TODO TYPE
                TODO DESCRIPTION
            start_sec: TODO TYPE
                TODO DESCRIPTION
            duration_sec: TODO TYPE
                TODO DESCRIPTION
            reset_time: TODO TYPE
                TODO DESCRIPTION
            

        Returns
        -------
            signals: TODO TYPE
                TODO DESCRIPTION
            events: TODO TYPE
                TODO DESCRIPTION
            

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """

        # Code examples

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        # raise NodeInputException(self.identifier, "my_input", \
        #        f"TrimSignal this input is wrong.")

        # Raise NodeRuntimeException if there is a critical error during runtime. 
        # This will usually be a user error, a file that can't be read due to security reason,
        # a parameter that is out of bound, etc. This exception will stop and skip the current
        # process but will not stop the followin iterations if a master node is not done.
        # Once the master node is completed, a dialog will appear to show all NodeRuntimeException
        # to the user.
        #
        # Set the iteration_identifier if this module is a master node.
        # This will be used to identify the problematic iteration if a runtime exception occurs
        # in any module during this process. For example, a master node that reads one file at a 
        # could set the identifier to the name of the file.
        # self.iteration_identifier = current_filename
        #
        # Iteration count and counter are used to show a progress bar in percent.
        # Update these when creating a master node to properly show the progress 
        # for each iteration. This is optional and can be ignored but it's a good practice
        # to do for your users.
        #self.iteration_count = the total amout of iteration to make
        #self.iteration_counter = the current iteration number

        #
        # Raise the runtime exception
        # raise NodeRuntimeException(self.identifier, "files", \
        #        f"Some file could not be open.")

        #
        #

        # Write to the cache to use the data in the resultTab
        # cache = {}
        # cache['this_is_a_key'] = 42
        # self._cache_manager.write_mem_cache(self.identifier, cache)

        # Log message for the Logs tab


        # --- 1) INPUT CHECKS ---
        if not isinstance(signals, list):
            raise NodeInputException(self.identifier, "signals",
                f"Expected list of SignalModel, got {type(signals)}")
        if not isinstance(reset_time, bool):
            raise NodeInputException(self.identifier, "reset_time",
                f"Expected boolean, got {type(reset_time)}")
        if not signals:
            raise NodeInputException(self.identifier, "signals",
                "Input signal list is empty.")
        if not isinstance(events, pd.DataFrame):
            raise NodeInputException(self.identifier, "events",
                f"Expected pandas.DataFrame, got {type(events)}")
        
        # It is possible to bypass the module by passing the input signals directly
        # to the output signals without any modification
        if self.activation_state == ActivationState.BYPASS:
            return {
                'signals': signals,
                'events' : events
            }    
 

        
        try:
            start_sec = float(start_sec)
            duration_sec = float(duration_sec)
        except Exception as e:
            raise NodeInputException(self.identifier, "start_sec/duration_sec",
                f"Could not convert start_sec or duration_sec to float: {e}")
        
        self._log_manager.log(self.identifier, "This module Trimmed signals and events based on input start_sec and duration_sec.")

        initial_start_time = signals[0].start_time
        initial_end_time = signals[0].end_time
        if start_sec < initial_start_time:
            raise NodeInputException(self.identifier, "start_sec",
                "start_sec must be greater than or equal to signal's start time.")
        if duration_sec < 0:
            raise NodeInputException(self.identifier, "duration_sec",
                "duration_sec must be non-negative.")
        if (start_sec + duration_sec) > initial_end_time:
            raise NodeInputException(self.identifier, "duration_sec",
                "start_sec plus duration_sec must be less than or equal to the signal's end time.")


        # --- 2) PROCESSING ---
        
        trimmed_signals = []
        for signal in signals:
            trimmed_signal = copy.deepcopy(signal)
            trimmed_signal.start_time = 0.0 if reset_time else start_sec
            trimmed_signal.end_time = (start_sec + duration_sec - start_sec) if reset_time else (start_sec + duration_sec)
            trimmed_signal.duration = duration_sec
            trimmed_signal.is_modified = True
            start_sample_idx = int((start_sec-signal.start_time) * trimmed_signal.sample_rate)
            duration_sampls = int(duration_sec * trimmed_signal.sample_rate)
            
            trimmed_signal.samples = trimmed_signal.samples[start_sample_idx : start_sample_idx + duration_sampls]
            trimmed_signals.append(trimmed_signal)


        trimmed_events = events[((events['start_sec']+events['duration_sec']) > start_sec) & ((events['start_sec']) < (start_sec + duration_sec))].copy().reset_index(drop=True) 
        
        # Calculate the end times in a temporary variable
        end_times = trimmed_events['start_sec'] + trimmed_events['duration_sec']

        # Calculate the new clipped start and end times (still absolute)
        clipped_starts = trimmed_events['start_sec'].clip(lower=start_sec)
        clipped_ends = end_times.clip(upper=(start_sec + duration_sec))

        # Update the DataFrame columns directly
        #    New Duration = Clipped End - Clipped Start
        trimmed_events['duration_sec'] = clipped_ends - clipped_starts

        #  New Start = Clipped Start - Window Start (shifting to relative time)
        trimmed_events['start_sec'] = clipped_starts - start_sec if reset_time else clipped_starts

        return {
            'signals': trimmed_signals,
            'events': trimmed_events
        }


"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

TrimSignal
----------
Trim continuous/discontinuous signal segments and their associated events to a
time window defined by `start_sec` and `duration_sec`.

- Signals are cropped in sample space for each channel/segment.
- Events are filtered to keep only overlapping events, then clipped to window bounds.
- If `reset_time=True`, output times are shifted so the trimmed window starts at 0.
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
    Trim a list of SignalModel objects and an events table to a target time window.

    Parameters
    ----------
        signals: list[SignalModel]
            Input signal segments to crop. Each element is expected to provide
            at least: `samples`, `sample_rate`, `start_time`, `end_time`, and `duration`.
        events: pandas.DataFrame
            Event annotations with at least `start_sec` and `duration_sec` columns.
        start_sec: float | str
            Absolute start time (in seconds) of the trimming window.
        duration_sec: float | str
            Duration (in seconds) of the trimming window.
        reset_time: bool
            If True, output signal/event times are shifted so trimmed data starts at 0.
            If False, absolute timeline is preserved.

    Returns
    -------
        signals: list[SignalModel]
            Deep-copied and trimmed signals, with updated timing metadata.
        events: pandas.DataFrame
            Events overlapping the trimming window, clipped to boundaries and optionally
            time-shifted depending on `reset_time`.
    """
    def __init__(self, **kwargs):
        """Initialize TrimSignal node input/output plugs."""
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
    
    
    def compute(self, signals, events, start_sec, duration_sec, reset_time=True):
        """
        Trim signals and events to a time window.

        Parameters
        ----------
            signals: list[SignalModel]
                Input signal segments to trim.
            events: pandas.DataFrame
                Input events table containing `start_sec` and `duration_sec`.
            start_sec: float | str
                Start time of trimming window in seconds.
            duration_sec: float | str
                Length of trimming window in seconds.
            reset_time: bool
                Whether to shift output timeline to start at 0.

        Returns
        -------
            signals: list[SignalModel]
                Trimmed signal list.
            events: pandas.DataFrame
                Trimmed/clipped event table.

        Raises
        ------
            NodeInputException
                If input types are invalid, required values are missing, or requested
                trim window is out of bounds.
            NodeRuntimeException
                Reserved for runtime failures during processing.
        """

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


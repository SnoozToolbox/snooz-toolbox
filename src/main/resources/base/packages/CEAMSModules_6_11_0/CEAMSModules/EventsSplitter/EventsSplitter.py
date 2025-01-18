"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    EventsSplitter
    Class to split too long events.
    A max_length_s=30 sec means that events longer than 30s are split into multiple events with a maximum duration of 30s each.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from flowpipe.ActivationState import ActivationState
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException


import pandas as pd
import numpy as np

DEBUG = False

class EventsSplitter(SciNode):
    """
    Class to split too long events.

    Inputs:
        "events": Pandas DataFrame
            DataFrame events to split (columns=['group','name','start_sec','duration_sec','channels'])  
        "max_length_s": str or float
            Event maximum length or longest duration before a split is performed. 
            I.e. max_length_s=30 sec means that events longer than 30s are split into multiple events with a maximum duration of 30s each.
    Outputs:
        "splitted_events": Pandas DataFrame
            DataFrame of splitted events (columns=['group','name','start_sec','duration_sec','channels'])  
        
    """
    def __init__(self, **kwargs):
        """ Initialize module EventsSplitter """
        super().__init__(**kwargs)
        if DEBUG: print('EventsSplitter.__init__')

        # Input plugs
        InputPlug('events',self)
        InputPlug('max_length_s',self)
        # Output plugs
        OutputPlug('splitted_events',self)
        
        # There can only be 1 master module per process.
        self._is_master = False 
    

    def compute(self, events, max_length_s):
        """
        Class to split too long events.

        Inputs:
            "events": Pandas DataFrame
                DataFrame events to split (columns=['group','name','start_sec','duration_sec','channels'])  
            "max_length_s": str or float
                Event maximum length or longest duration before a split is performed. 
                I.e. max_length_s=30 sec means that events longer than 30s are split into multiple events with a maximum duration of 30s each.
        Outputs:
            "splitted_events": Pandas DataFrame
                DataFrame of splitted events (columns=['group','name','start_sec','duration_sec','channels'])  
            
        """

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if isinstance(events, str) and events=='':
            raise NodeInputException(self.identifier, "events", f"EventsSplitter, events has to be connected.")
        if isinstance(max_length_s, str) and max_length_s=='':
            raise NodeInputException(self.identifier, "max_length_s", f"EventsSplitter, max_length_s has to be connected.")

        if not isinstance(events,pd.DataFrame):
            raise NodeInputException(self.identifier, "events", f"EventsSplitter, unexpected type, need pd.DataFrame and it is {type(events)}.")
        try :
            max_length_s = float(max_length_s)
        except : 
            raise NodeInputException(self.identifier, "max_length_s", f"EventsSplitter, unexpected type, need a str of float and it is {type(max_length_s)}.")

        # It is possible to bypass the "DiscardEvents" by passing the input events directly
        # to the output events without any modification
        if self.activation_state == ActivationState.BYPASS:
            return {
                'splitted_events': events
            }             

        if len(events)>0:

            # Round the duration of events (especially for stellate cases)
            duration_sec = events['duration_sec'].to_numpy().astype(float)
            duration_sec = np.around(duration_sec, decimals=2)
            events.loc[:,'duration_sec']=duration_sec.astype(float)

            # Accumulate all the short events (no modification)
            events_out = events[(duration_sec <= max_length_s)]

            # For each too long events, split it
            event_too_long = events[(duration_sec > max_length_s)]
            for index, row in event_too_long.iterrows():
                n_events = int(row['duration_sec']/max_length_s)
                last_duration = row['duration_sec']%max_length_s
                split_event = [(row['group'], row['name'], row['start_sec']+i_evt*max_length_s, max_length_s, row['channels']) for i_evt in range(n_events)]
                if last_duration>0:
                    split_event.append((row['group'], row['name'], row['start_sec']+n_events*max_length_s, last_duration, row['channels']))
                # Create a pandas dataframe of events (each row is an event)
                events_split_df = pd.DataFrame(split_event, columns=['group','name','start_sec','duration_sec','channels']) 
                events_out = pd.concat([events_out,events_split_df])

            # Reset index
            events_out.reset_index(inplace=True, drop=True)
            # Sort events based on the start_sec
            events_out.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')

        # Write to the cache to use the data in the resultTab
        cache = {}
        cache['events'] = events_out
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'splitted_events': events_out
        }
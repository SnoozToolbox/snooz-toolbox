"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    DefineEventGroup
    Define groups to events. 
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

import numpy as np
import pandas as pd

DEBUG = False

class DefineEventGroup(SciNode):
    """
    Define groups to events. 

    Inputs:
        "events": Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
            Lits of events (could miss the group column) 
        "groups": dict
            Group dictionary. Each item is an event name and the value is the group to add or modify.

    Outputs:
        "events": Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
            Lits of events with the added or modified group.
        
    """
    def __init__(self, **kwargs):
        """ Initialize module DefineEventGroup """
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')

        # Input plugs
        InputPlug('events',self)
        InputPlug('groups',self)
        # Output plugs
        OutputPlug('events',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    

    def compute(self, events,groups):
        """
        Define groups to events. 

        Inputs:
            "events": Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
                Lits of events (could miss the group column) 
            "groups": dict
                Group dictionary. Each item is an event name and the value is the group to add or modify.

        Outputs:
            "events": Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
                Lits of events with the added or modified group.
            
        """
        if not isinstance(events, pd.DataFrame):
            raise NodeInputException(self.identifier, "events", \
                f"DefineEventGroup : expected type is pd.DataFrame and the type is {type(events)}.")
        if not isinstance(groups,dict):
            raise NodeInputException(self.identifier, "groups", \
                f"DefineEventGroup : expected type is dict and the type is {type(groups)}.")            

        if not ('group' in events):
            events['group'] = ''
        for event_name, event_group in groups.items():
            # Modify the group based on the dictionary group
            events.loc[events['name'] ==event_name, 'group'] = event_group

        events = events[['group','name','start_sec','duration_sec','channels']]
        # Write the cache
        cache = {}
        cache['events'] = events
        self._cache_manager.write_mem_cache(self.identifier, cache)

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module does nothing.")

        return {
            'events': events
        }
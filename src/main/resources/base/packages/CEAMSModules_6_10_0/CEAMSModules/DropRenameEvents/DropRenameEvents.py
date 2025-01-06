"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    DropRenameEvents
    To drop events and/or rename events group and/or name.
    The effect is only on the events dataframe (not the file saved on the disk).
"""
import pandas as pd
import numpy as np

from flowpipe import SciNode, InputPlug, OutputPlug, ActivationState
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from CEAMSModules.EventReader import manage_events

DEBUG = False

class DropRenameEvents(SciNode):
    """
    To drop events and/or rename events group and/or name.
    
    We suppose that the output file has already all the events.
    We want to rename some events (events_to_rename), so new_events is only the new set of events renamed
    (all untouched events are not included in new_events). 
    We also want to drop some events (events_to_drop_in). 
    Warning : the renamed events are added as new_events, so we need to drop the original (not renamed) events. 
    The output "events_to_drop_out" also include the original events that has been renamed.

    Inputs:
        "events": pandas DataFrame columns=['group','name','start_sec','duration_sec','channels']
            Original list of events.
        "events_to_drop_in": list of tuple
            Events group and name to remove from the file.
            ex. [('group1', 'name1') 
                ('group2', 'name2')]
        "events_to_rename": list of tuple
            Events group and name to remove from the file.
            ex. [('group1_ori', 'name1_ori', 'group1_new', 'name1_new')
                ('group2_ori', 'name2_ori', 'group2_new', 'name2_new')]

    Outputs:
        "new_events": pandas DataFrame columns=['group','name','start_sec','duration_sec','channels']
            Modified list of events (renamed and dropped if apply).
        "events_to_drop_out" : list of tuple
            Events group and name to remove from the file.
            ex. [('group1', 'name1') 
                ('group2', 'name2')]
        
    """
    def __init__(self, **kwargs):
        """ Initialize module DropRenameEvents """
        super().__init__(**kwargs)
        if DEBUG: print('DropRenameEvents.__init__')

        # Input plugs
        InputPlug('events',self)
        InputPlug('events_to_drop_in',self)
        InputPlug('events_to_rename',self)

        # Output plugs
        OutputPlug('new_events',self)
        OutputPlug('events_to_drop_out',self)
        
        # Init module variables
        # self.this_is_an_example_you_can_delete_it = 0
        self._is_master = False 
    

    def compute(self, events, events_to_drop_in, events_to_rename):
        """
        To drop events and/or rename events group and/or name.

        Inputs:
            "events": pandas DataFrame columns=['group','name','start_sec','duration_sec','channels']
                Original list of events.
            "events_to_drop_in": tuples of n events to remove.
                Events group and name to remove from the file.
                ex. (('group1', 'name1') 
                    ('group2', 'name2'))
            "events_to_rename": tuples of n events to rename.
                Events group and name to remove from the file.
                ex. (('group1_ori', 'name1_ori', 'group1_new', 'name1_new')
                    ('group2_ori', 'name2_ori', 'group2_new', 'name2_new'))

        Outputs:
            "new_events": pandas DataFrame columns=['group','name','start_sec','duration_sec','channels']
                Modified list of events (renamed and dropped if apply).
            "events_to_drop_out" : list of tuple
                Events group and name to remove from the file.
                ex. [('group1', 'name1') 
                    ('group2', 'name2')]
            
        """

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if not isinstance(events, pd.DataFrame):
            raise NodeInputException(self.identifier, "events", \
                f"DropRenameEvents this input is {type(events)} and a pd.DataFrame is expected.")
        if isinstance(events_to_drop_in,str) and not events_to_drop_in=='':
            events_to_drop_in = eval(events_to_drop_in)
        if not isinstance(events_to_drop_in, list):
            raise NodeInputException(self.identifier, "events_to_drop_in", \
                f"DropRenameEvents this input is {type(events_to_drop_in)} and a list of tuple is expected.")            
        if isinstance(events_to_rename,str) and not events_to_rename=='':
            events_to_rename = eval(events_to_rename)
        if not isinstance(events_to_rename, list):
            raise NodeInputException(self.identifier, "events_to_rename", \
                f"DropRenameEvents this input is {type(events_to_rename)} and a list of tuple is expected.")      

        # Raise NodeRuntimeException if there is a critical error during runtime. 
        # This exception will stop and skip the current
        # process but will not stop the followin iterations if a master node is not done.
        # raise NodeRuntimeException(self.identifier, "files", \
        #        f"Some file could not be open.")

        # It is possible to bypass the DropRenameEventsplugin by passing 
        # the input events directly to the output events
        if self.activation_state == ActivationState.BYPASS:
            return {'new_events': manage_events.create_event_dataframe(None),
                    'events_to_drop_out' : events_to_drop_in}

        # Convert string to tuple if apply
        if isinstance(events_to_drop_in, str) and len(events_to_drop_in)>0:
            events_to_drop_in = eval(events_to_drop_in)
        if isinstance(events_to_rename, str) and len(events_to_rename)>0:
            events_to_rename = eval(events_to_rename)
            
        # If theirs are no modifications to apply, nothing to do 
        if (len(events_to_drop_in)==0) and (len(events_to_rename)==0):
            return {'new_events': manage_events.create_event_dataframe(None),
                    'events_to_drop_out' : manage_events.create_event_dataframe(None)}

        # Rename the events for each combinason of group-name to remove                
        if len(events_to_rename)>0:
            new_events = manage_events.create_event_dataframe(None)
            index_to_ren_all = []
            for group_ori, name_ori, group_new, name_new in events_to_rename: 
                index_to_ren = events[(events['group']==group_ori) & (events['name']==name_ori)].index.to_list()
                index_to_ren_all.append(index_to_ren)
                new_events_to_ren = events.loc[index_to_ren].copy()
                if len(new_events_to_ren)>0:
                    list_group = [group_new] * len(index_to_ren)
                    list_name = [name_new] * len(index_to_ren)
                    new_events_to_ren.loc[index_to_ren, "group"] = list_group
                    new_events_to_ren.loc[index_to_ren, "name"] = list_name
                    # Reset index and sort events based on the start_sec
                    new_events_to_ren.reset_index(inplace=True, drop=True)
                    new_events_to_ren.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')
                else:
                    self._log_manager.log(self.identifier, f"Events {group_ori}-{name_ori} to rename are not found")
                new_events = pd.concat([new_events, new_events_to_ren])
        else:
            new_events = manage_events.create_event_dataframe(None)

        # We have to drop renamed events
        #   because they are now in the new_events
        # Add the original group/name of the renamed events in the events to drop.
        events_to_drop_out_all = events_to_drop_in
        if len(events_to_rename)>0:
            index_to_ren_all_flat = [item for sublist in index_to_ren_all for item in sublist]
            ori_events_renamed = events.loc[index_to_ren_all_flat, ['group', 'name']]
            ori_events_renamed.drop_duplicates(inplace=True,ignore_index=True)
            for index, event in ori_events_renamed.iterrows():
                events_to_drop_out_all.append((event['group'], event['name']))
                
        # Drop duplicates in case renamed events were also dropped events
        events_to_drop_out = []
        for group, name in events_to_drop_out_all:
            if not ((group, name) in events_to_drop_out):
                events_to_drop_out.append((group, name))
            
        # Write to the cache to use the data in the resultTab
        cache = {}
        cache['events'] = new_events
        self._cache_manager.write_mem_cache(self.identifier, cache)

        # Log message for the Logs tab
        # self._log_manager.log(self.identifier, "This module does nothing.")

        return {
            'new_events': new_events,
            'events_to_drop_out' : events_to_drop_out
        }
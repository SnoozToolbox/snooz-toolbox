"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    DiscardEvents
    To discard too long, too short or events that occur during artefacts.
"""
from CEAMSModules.EventReader import manage_events
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from flowpipe.ActivationState import ActivationState

import numpy as np
import pandas as pd

DEBUG = False

class DiscardEvents(SciNode):
    """
    To discard too long, too short or events that occur during artefacts.

    Parameters
    -----------
        "events": : Pandas DataFrame
            DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])  
        "event_group" : String
            Event group to filter (discard too long, short).
        "event_name" : String
            Event name to filter (discard too long, short).
        "min_len_sec": float
            Mimimum length accepted, shorter events are discared.
        "max_len_sec": float
            Maximum length accepted, longer events are discared.
        "artefact_free": bool
            '1' : discard events that occur during an artefact.
            '0' : keep all events
        "artefact_group": String
            Events to considered as artefact.
            The user can define a single group (and let the name blank) or a single name (and let the group blank).
            If group and name are defined, they must be defined in pairs.
            Each group should be separated by a comma. The group works as a pattern matching.  
        "artefact_name": String
            Events to considered as artefact.
            Each name should be separated by a comma. The name works as a pattern matching.
    Returns
    -----------  
        "events": : Pandas DataFrame
            DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])     
        
    """
    def __init__(self, **kwargs):
        """ Initialize module DiscardEvents """
        super().__init__(**kwargs)
        if DEBUG: print('DiscardEvents.__init__')

        # Input plugs
        InputPlug('events',self)
        InputPlug('event_group',self)
        InputPlug('event_name',self)
        InputPlug('min_len_sec',self)
        InputPlug('max_len_sec',self)
        InputPlug('artefact_free',self)
        InputPlug('artefact_group',self)
        InputPlug('artefact_name',self)
        
        # Output plugs
        OutputPlug('events',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    

    def compute(self, events, event_group, event_name, min_len_sec, max_len_sec, artefact_free, artefact_group, artefact_name):
        """
        To discard too long, too short or events that occur during artefacts.

        Parameters
        -----------
            "events": : Pandas DataFrame
                DataFrame events (columns=['group','name','start_sec','duration_sec','channels']) 
            "event_group" : String
                Event group to filter (discard too long, short)
            "event_name" : String
                Event name to filter (discard too long, short)
            "min_len_sec": float
                Mimimum length accepted, shorter events are discared.
            "max_len_sec": float
                Maximum length accepted, longer events are discared.
            "artefact_free": bool
                '1' : discard events that occur during an artefact.
                '0' : keep all events
            "artefact_group": String
                Events to considered as artefact.
                The user can define a single group (and let the name blank) or a single name (and let the group blank).
                If group and name are defined, they must be defined in pairs.
                Each group should be separated by a comma. The group works as a pattern matching.  
            "artefact_name": String
                Events to considered as artefact.
                Each name should be separated by a comma. The name works as a pattern matching.
        Returns
        -----------  
            "events": : Pandas DataFrame
                DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])     
            
        """
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None    

        # It is possible to bypass the "DiscardEvents" by passing the input events directly
        # to the output events without any modification
        if self.activation_state == ActivationState.BYPASS:
            return {
                'events': events
            }        

        if not isinstance(events,pd.DataFrame):
            raise NodeInputException(self.identifier, "events", \
                f"DiscardEvents input of wrong type. Expected: <class 'pd.DataFrame'> received: {type(events)}")                    

        # To discard too long and too short events
        min_len_sec = float(min_len_sec)
        max_len_sec = float(max_len_sec)

        # Apply group and name selection. The user can define a single group or a single name. 
        # If group and name are defined, they must be defined in pairs.
        if len(events)>0:
            if isinstance(event_group,str) and len(event_group)>0:
                event_group_lst = event_group.split(',')
            else:
                event_group_lst = []
            if isinstance(event_name,str) and len(event_name)>0:
                event_name_lst = event_name.split(',')
            else:
                event_name_lst = []
            
            # Select the event to evaluate
            group_event_to_select = events['group'].values
            name_event_to_select = events['name'].values
            events_out = manage_events.create_event_dataframe(None)
            if len(event_group_lst)==len(event_name_lst):
                for i, group_cur in enumerate(event_group_lst):
                    mask_group = group_event_to_select==group_cur
                    mask_name = name_event_to_select==event_name_lst[i]
                    mask_tot = mask_group & mask_name
                    events_cur = pd.DataFrame(events.values[mask_tot], events.index[mask_tot], events.columns)
                    events_out = pd.concat([events_out,events_cur])
            elif len(event_group_lst)>0 and len(event_name_lst)==0:
                for group_cur in event_group_lst:
                    mask_group = group_event_to_select==group_cur
                    events_cur = pd.DataFrame(events.values[mask_group], events.index[mask_group], events.columns)
                    events_out = pd.concat([events_out,events_cur])
            elif len(event_name_lst)>0 and len(event_group_lst)==0:
                for name_cur in event_name_lst:
                    mask_name = name_event_to_select==name_cur
                    events_cur = pd.DataFrame(events.values[mask_name], events.index[mask_name], events.columns)
                    events_out = pd.concat([events_out,events_cur])
            else:
                raise NodeInputException(self.identifier, "artefact_group", \
                    f"DiscardEvents input of wrong size. If both group and name are defined they need to be the same length, group length:\
                         {len(event_group_lst)} and name length: {len(event_name_lst)}")

            # To discard too long and too short events
            # Round the event duration to 2 decimals because the duration limit are also 2 decimal precise
            duration_sec = events_out['duration_sec'].to_numpy().astype(float).copy()
            duration_sec = np.around(duration_sec, decimals=2)
            #events_out.loc[:,'duration_sec']=duration_sec.astype(float) # We want to keep the original length
            events_out = events_out.drop(events_out[(duration_sec > max_len_sec) | (duration_sec < min_len_sec)].index)
            # Reset index
            events_out.reset_index(inplace=True, drop=True)
            # Sort events based on the start_sec
            events_out.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')

            # To discard events that occur during artefact
            # Select the artefact
            # Apply group and name selection. The user can define a single group or a single name. 
            # If group and name are defined, they must be defined in pairs.
            if artefact_free=='1':
                art_selected = pd.DataFrame(columns=['group','name','start_sec','duration_sec','channels'])
                if isinstance(artefact_group,str) and len(artefact_group)>0:
                    art_group_lst = artefact_group.split(',')
                else:
                    art_group_lst = []
                if isinstance(artefact_name,str) and len(artefact_name)>0:
                    art_name_lst = artefact_name.split(',')
                else:
                    art_name_lst = []
                if len(art_group_lst)==len(art_name_lst):
                    for i, group_cur in enumerate(art_group_lst):
                        cur_selection = events[ (events['group']==group_cur) & (events['name']==art_name_lst[i])]
                        art_selected = pd.concat([art_selected,cur_selection])
                elif len(art_group_lst)>0 and len(art_name_lst)==0:
                    for group_cur in art_group_lst:
                        group_selected = events[events['group']==group_cur]
                        art_selected = pd.concat([art_selected,group_selected])
                elif len(art_name_lst)>0 and len(art_group_lst)==0:
                    for name_cur in art_name_lst:
                        name_selected = events[events['name']==name_cur]
                        art_selected = pd.concat([art_selected,name_selected])
                else:
                    raise NodeInputException(self.identifier, "event_group", \
                        f"DiscardEvents input of wrong size. If both group and name are defined they need to be the same length, group length:\
                             {len(art_group_lst)} and name length: {len(art_name_lst)}") 
                # Reset index
                art_selected.reset_index(inplace=True, drop=True)
                # Sort events based on the start_sec
                art_selected.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')

                # events_out includes spindles (valid length)
                # art_selected includes selected artefact that drops spindles

                # We need to drop spindles that occur during art_selected
                # for each event, evaluate for artefact
                event_sel_to_drop = []
                for event_sel in range(len(events_out)):
                    cur_event = events_out.loc[event_sel]
                    art_cur_chan = art_selected[art_selected.channels==cur_event.channels]
                    if len(art_cur_chan)>0:
                        art_start = art_cur_chan['start_sec'].to_numpy().astype(float)
                        art_dur = art_cur_chan['duration_sec'].to_numpy().astype(float)
                        # If there is at least one artefact that : 
                        #   start before the end of the spindle AND stop after the start of the spindle.
                        if any( (art_start<= (cur_event.start_sec + cur_event.duration_sec)) & ((art_start+art_dur)>=cur_event.start_sec) ):
                            # Save the spindle index to drop
                            event_sel_to_drop.append(event_sel)             
                # Drop the spindles
                events_out = events_out.drop(event_sel_to_drop)
                # Reset index
                events_out.reset_index(inplace=True, drop=True)
                # Sort events based on the start_sec
                events_out.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')
        else:
            events_out = events
        # Write the cache to see event 
        cache = {}
        cache['events'] = events_out
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'events': events_out
        }
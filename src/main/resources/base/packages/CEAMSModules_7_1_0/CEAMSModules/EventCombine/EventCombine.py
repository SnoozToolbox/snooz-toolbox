"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    This plugin combines two lists of events, with or without selection.
    The union and intersection behavior are performed per channels (only events on the same channel are combined).
    ! Except when events are filtered for a sepcific channel (channel1_name or channel2_name are initialized).
      In this case the combined events is forced to be on the channel from events1
    The append behavior is perform on all events (event without channel), dataframe are simply concatenated (row wise).

    Append behavior :
        -All events are added row wise in the events output.
        (could have duplicated events)
    Union behavior (per channel) : 
        -without new event name : events1 and events2 are append to the new list of events
        -with a new event name : events1 and events2 are merge (no more concurrent events)
        and all the new events are renamed with the new event name.
    Union non-concurrent behavior (per channel) :
        -without new event name : events1 and events2 are merge (no more concurrent events)
        and renamed as the event with the longest duration within the new combined event.
        If an event occures more than onces within the combined event, 
        the total duration of all the occurrences are considered.
            Ex: high freq artefact (1), electrode pop (2) and muscular artefact (3) 
            occur all partially in the same time (they are concurrent).
            event1:  -1111-----
            event2:  --2---2---
            event3:  ---333333-
            combine: -33333333-  
        *When 2 events have the same duration the first one in the list is taken
        -with a new event name : events1 and events2 are merge (no more concurrent events)
        and all the new events are renamed with the new event name.
    Intersection behavior (per channel): 
        Only concurrent events, events1 and event2 have to occur simultaneously.
        -without new event name : event1 name is taken
        -with a new event name : combined events are rename with the new event name.

    Notes 
    ----------
    The events1 has to be connected as a pandas dataframe.
    The events1 or events2 may be empty (except for the append).
    If the events are filtered by channel, events1 can be filtered for only one channel
    and events2 can be filtered for only one channel.

    Parameters
    -----------
        events1 : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            The first list of events
        event1_name : String
            The name of the first event to combine
        events2 : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            The second list of events
        event2_name : String
            The name of the second event to combine.
        channel1_name : String or list of string
            The channel name to extract events1 or the channel name saved in a list.
        channel2_name : String or list of string
            The channel name to extract events1 or the channel name saved in a list.
        behavior : String
            Select how to combine events : union (all events) or 
                intersection (concurrent events only).
        new_event_group : string
            The group of the created (combined) list of events.
        new_event_name : String
            The name of the created (combined) list of events.
        new_event_chan : String
            The name of the created (combined) list of events.

    Returns
    -----------  
        events  : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            The new events list created.   

    @author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)
"""
from CEAMSModules.EventReader import manage_events
from CEAMSModules.EventCompare import performance as perf
from commons.NodeInputException import NodeInputException
from flowpipe import SciNode, InputPlug, OutputPlug

import numpy as np
import pandas as pd
import datetime as dt

DEBUG = False

class EventCombine(SciNode):

    """
        This class combines two lists of events, with or without selection.

        Parameters
        -----------
            events1 : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                The first list of events
            event1_name : String
                The name of the first event to combine
            events2 : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                The second list of events
            event2_name : String
                The name of the second event to combine.
            channel1_name : String or list of string
                The channel name to extract events1 or the channel name saved in a list.
            channel2_name : String or list of string
                The channel name to extract events1 or the channel name saved in a list.
            behavior : String
                Select how to combine events : union (all events) or 
                    intersection (concurrent events only).
            new_event_group : String
                The group of the created (combined) list of events.
            new_event_name : String
                The name of the created (combined) list of events.
            new_event_chan : String
                The name of the created (combined) list of events.
        Returns
        -----------  
            events  : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                The new events list created.   
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('EventCombine.__init__')
        InputPlug('events1', self)
        InputPlug('event1_name', self)
        InputPlug('events2', self)
        InputPlug('event2_name', self)
        InputPlug('channel1_name', self)
        InputPlug('channel2_name', self)
        InputPlug('behavior', self)
        InputPlug('new_event_group', self)
        InputPlug('new_event_name', self)
        InputPlug('new_event_chan', self)
        OutputPlug('events', self)

    def __del__(self):
        if DEBUG: print('EventCombine.__del__')

    def subscribe_topics(self):
        pass

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'EventCombine.on_topic_update {topic}:{message}')

    def compute(self, events1, event1_name, events2, event2_name, channel1_name,\
         channel2_name, behavior, new_event_group, new_event_name, new_event_chan):
        """
            This function combines two lists of events, with ot without selection.

            Parameters
            -----------
                events1 : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                    The first list of events
                event1_name : String
                    The name of the first event to combine
                events2 : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                    The second list of events
                event2_name : String
                    The name of the second event to combine.
                channel1_name : String or list of string
                    The channel name to extract events1 or the channel name saved in a list.
                channel2_name : String or list of string
                    The channel name to extract events1 or the channel name saved in a list.
                behavior : String
                    Select how to combine events : union (all events) or 
                        intersection (concurrent events only).
                new_event_group : String
                    The group of the created (combined) list of events.
                new_event_name : String
                    The name of the created (combined) list of events.
                new_event_chan : String
                    The name of the created (combined) list of events.
            Returns
            -----------  
                events  : Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                    The new events list created.   
        """
        if DEBUG: print('EventCombine.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None        

        if isinstance(events1, pd.DataFrame):
            events1 = events1.copy() # otherwise following instance of events are also modified
            # If the user wants to filter for a specific event name
            if len(event1_name)>0:
                events1 = events1[events1.name==event1_name]

            if isinstance(events2, pd.DataFrame):
                events2 = events2.copy() # otherwise followinf instance of events are also modified
                # If the user wants to filter for a specific event name
                if len(event2_name)>0:
                    events2 = events2[events2.name==event2_name]                

            # Simply append both dataframes events
            if behavior == "append":

                if ((len(new_event_group)>0) & (len(new_event_name)==0)) or \
                    ((len(new_event_group)==0) & (len(new_event_name)>0)):
                    err_message = "To modify events the new event group and the new event name are madatory"
                    print("ERROR : EventCombine, " +  err_message)
                    self._log_manager.log(self.identifier, err_message)
                    # Exit
                    return {
                        'events': ''
                    } 

                events_df = manage_events.create_event_dataframe(None)
                # Append events
                if isinstance(events1, pd.DataFrame) and isinstance(events2, pd.DataFrame):
                    events_df = pd.concat([events1,events2],ignore_index=True)
                elif isinstance(events1, pd.DataFrame):
                    events_df = events1
                elif isinstance(events2, pd.DataFrame):
                    events_df = events1
                else:
                    raise NodeInputException(self.identifier, "events", \
                        f"EventCombine : events1 or events2 must be connected to append events")                    
                # Sort events based on the start_sec
                events_df.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')

                # If user want to modify the combined events
                if (len(new_event_group)>0) and (len(new_event_group)>0):
                    events_df.loc[:,'group']=new_event_group
                    events_df.loc[:,'name']=new_event_name
                if len(new_event_chan)>0:
                    events_df.loc[:,'channels']=new_event_chan

                # Write the cache
                cache = {}
                cache['events'] = events_df
                self._cache_manager.write_mem_cache(self.identifier, cache)

                # Output the new list of events
                return {
                    'events': events_df
                } 
            else:
                # Drop any event without channel information
                # Probably not event, but sleep stages
                events1_chan = events1.dropna(axis=0, how='any', inplace=False)
                events1_chan.reset_index(inplace=True, drop=True)
                channel1_lst = pd.unique(events1_chan.channels)

                if isinstance(events2, pd.DataFrame):
                    # Drop any event without channel information
                    # Probably not event, but sleep stages
                    events2_chan = events2.dropna(axis=0, how='any', inplace=False)
                    events2_chan.reset_index(inplace=True, drop=True)
        else:
            print("ERROR : EventCombine, Events1 is not connected")
            err_message = "ERROR : Events1 is not connected"
            self._log_manager.log(self.identifier, err_message)
            # Exit
            return {
                'events': ''
            } 

        if ((len(new_event_group)>0) & (len(new_event_name)==0)) or \
            ((len(new_event_group)==0) & (len(new_event_name)>0)):
            err_message = "To modify events the new event group and the new event name are madatory"
            print("ERROR : EventCombine, " +  err_message)
            self._log_manager.log(self.identifier, err_message)
            # Exit
            return {
                'events': ''
            } 

        if isinstance(channel2_name, list):
            if len(channel2_name)==0:
                channel2_name = ''
            elif len(channel2_name)>1:
                err_message = "channel2_name should have only one channel, only the first one is taken {}".format(channel2_name[0])
                self._log_manager.log(self.identifier, err_message)
                channel2_name = channel2_name[0]
            else:
                channel2_name = channel2_name[0]

        # If the user wants to filter for a specific channel only
        if isinstance(channel1_name, str) and len(channel1_name)>0:
            channel_lst = [channel1_name]
        elif isinstance(channel1_name, list):
            channel_lst = channel1_name
        # Channels are not filtered in events1
        elif isinstance(events2, pd.DataFrame):
            channel2_lst = pd.unique(events2_chan.channels)
            # Create the master list of unique channels
            channel_lst = [item for sublist in [channel1_lst,channel2_lst] for item in sublist]
            channel_lst = list(set(channel_lst))
        else:
            channel_lst = channel1_lst

        # Loop accross all channels
        events_df = manage_events.create_event_dataframe(None)
        for i_chan in channel_lst:
            # Filter for the current channel
            events1_chan_cur = events1_chan[events1_chan['channels']==i_chan]
            # Reset index of the events
            events1_chan_cur.reset_index(inplace=True, drop=True)

            if isinstance(events2, pd.DataFrame):
                # If the user wants to filter for a specific event name           
                if len(channel2_name)>0:
                    events2_chan_cur = events2_chan[events2_chan['channels']==channel2_name]
                else:
                    events2_chan_cur = events2_chan[events2_chan['channels']==i_chan]
                # Reset index of the events
                events2_chan_cur.reset_index(inplace=True, drop=True)
                
                # Evaluate if there is only one name of events (artifact rejection)
                unique_name = np.unique(np.concatenate((events1_chan_cur['name'].unique(), events2_chan_cur['name'].unique())))
                unique_group = np.unique(np.concatenate((events1_chan_cur['group'].unique(), events2_chan_cur['group'].unique())))
            else:
                # Evaluate if there is only one name of events (artifact rejection)
                unique_name = events1_chan_cur['name'].unique()
                unique_group = events1_chan_cur['group'].unique()

            # Add both events (with or without concurrent)
            if 'union' in behavior:
                # Create the combined list of events
                events_cur = pd.DataFrame(columns=['group','name','start_sec','duration_sec','channels']) 
                # Append events    
                events_cur = pd.concat([events_cur,events1_chan_cur],ignore_index=True) 
                if isinstance(events2, pd.DataFrame):
                    events_cur = pd.concat([events_cur,events2_chan_cur],ignore_index=True) 
                # Reset index of the events
                events_cur.reset_index(inplace=True, drop=True)
                # Convert data frame events into binary vector and event list
                # This event_list does not have event_name yet, its only the combinaison
                (event_list, bin_event_cur) = perf.evt_df_to_bin(events_cur, fs=256)

            # Keep detection that are concurrent only
            elif 'intersection' in behavior and isinstance(events2, pd.DataFrame):
                #if event1_name=='' or event2_name=='':
                    # print("WARNING : EventCombine, Intersection of non selected events")
                    # war_message = "WARNING : Intersection of non selected events"
                    # self._log_manager.log(self.identifier, war_message)

                # Convert events into binary vector
                (event_list1, bin_event1_cur) = perf.evt_df_to_bin(events1_chan_cur, fs=256)
                (event_list2, bin_event2_cur) = perf.evt_df_to_bin(events2_chan_cur, fs=256)

                # pad length
                len_diff = len(bin_event1_cur) - len(bin_event2_cur)
                bin_event1_cur = np.expand_dims(bin_event1_cur, axis=1)
                bin_event2_cur = np.expand_dims(bin_event2_cur, axis=1)
                if len_diff>0:
                    bin_event2_cur = np.concatenate((bin_event2_cur,np.zeros((len_diff,1))),axis=0)
                elif len_diff<0:
                    bin_event1_cur = np.concatenate((bin_event1_cur,np.zeros((abs(len_diff),1))),axis=0)
                # AND operator between binary vector to keep only concurrent events
                bin_event_cur = np.where(bin_event1_cur==bin_event2_cur,bin_event1_cur,0)
            else:
                print("ERROR : EventCombine, Intersection but events2 is not connected")
                war_message = "ERROR : Intersection but events2 is not connected"
                self._log_manager.log(self.identifier, war_message) 
                return {
                    'events': ''
                }                        

            # Combined events, the master list of events
            # Convert the binary vector into list of events in second
            event_list_sec = perf.bin_evt_to_lst_sec(bin_event_cur, fs=256)
            # Convert the binary vector into list of events in samples
            event_list_smp = perf.bin_evt_to_lst(bin_event_cur)

            # ------------------------------------------------------------------
            # Add the name event to the created list
            # ------------------------------------------------------------------
            
            # Rename the combined events with the new event name if available
            if (len(new_event_group)>0) & (len(new_event_name)>0):
                # Modify the channel if new_event_chan is available
                if len(new_event_chan)>0:
                    events = [(new_event_group, new_event_name, start, dur, new_event_chan) \
                        for start, dur in event_list_sec]
                else:
                    events = [(new_event_group, new_event_name, start, dur, i_chan) \
                        for start, dur in event_list_sec]
                # Create a pandas dataframe of events (each row is an event)
                events_df_cur = pd.DataFrame(events, columns=['group','name','start_sec','duration_sec','channels']) 
                if DEBUG:
                    war_message = "Combined events have been renamed"
                    print("WARNING " + "EventCombine " + war_message)
                    self._log_manager.log(self.identifier, war_message) 

            elif len(unique_name)==1 and len(unique_group)==1: # Unique name
                events = [(unique_group[0], unique_name[0], start, dur, i_chan) \
                    for start, dur in event_list_sec]
                events_df_cur = pd.DataFrame(events, columns=['group','name','start_sec','duration_sec','channels']) 

            # Event name are preserved (select the right one)
            elif (('concurrent' in behavior) or ('intersection' in behavior)) and not (len(unique_name)==1 and len(unique_group)==1):
                # The name of the event with the longest duration is taken 
                # when 2 or more events overlap each others.
                # longest_evt : nparray [n gs events x 2]
                #   0: longest etimated event index
                #   1: duration 

                # event_list_smp : non concurrent events listed as start(sample) and duration(sample)
                # bin_event_cur : binary vector of non concurrent events 
                # events1_chan_cur : pandas dataframe of events1
                # longest_evt1 may contains NaN values if the non concurrent event is events2
                if len(events1_chan_cur)>0:
                    longest_evt1 = perf.compute_longest_est(\
                        event_list_smp, bin_event_cur, events1_chan_cur, fs=256)
                else:
                    longest_evt1 = np.zeros((len(event_list_smp),2))
                    longest_evt1[:] = np.NaN
                if isinstance(events2, pd.DataFrame) and len(events2_chan_cur)>0:
                    longest_evt2 = perf.compute_longest_est(\
                        event_list_smp, bin_event_cur, events2_chan_cur, fs=256)
                else:
                    longest_evt2 = np.zeros((len(event_list_smp),2))
                    longest_evt2[:] = np.NaN                    
                
                # Look for the biggest intersection between event1 and event2
                events_lst = []
                for i_evt_comb in range(len(longest_evt1)):
                    if isinstance(events2, pd.DataFrame):
                        if np.nanargmax((longest_evt1[i_evt_comb,1],\
                            longest_evt2[i_evt_comb,1])) == 0:
                            event_name = events1_chan_cur.name[longest_evt1[i_evt_comb,0]]
                            event_group = events1_chan_cur.group[longest_evt1[i_evt_comb,0]]
                        elif np.nanargmax((longest_evt1[i_evt_comb,1],\
                            longest_evt2[i_evt_comb,1])) == 1:
                            event_name = events2_chan_cur.name[longest_evt2[i_evt_comb,0]]
                            event_group = events2_chan_cur.group[longest_evt2[i_evt_comb,0]]
                        else:
                            war_message = "Combine events without concurrent does not work"
                            self._log_manager.log(self.identifier, war_message) 
                    else:
                        event_name = events1_chan_cur.name[longest_evt1[i_evt_comb,0]]
                        event_group = events1_chan_cur.group[longest_evt1[i_evt_comb,0]]
                    # Modify the channel if new_event_chan is available
                    if len(new_event_chan)>0:
                        channel_name = new_event_chan
                    else:
                        channel_name = i_chan
                    # Append the modified combined events for the current channel
                    events_lst.append([event_group,event_name,event_list_sec[i_evt_comb,0].tolist(),\
                        event_list_sec[i_evt_comb,1].tolist(),channel_name])

                # Convert event list into pandas DataFrame
                events_df_cur = pd.DataFrame(data=events_lst,columns=[\
                    'group','name','start_sec','duration_sec','channels'])          

            # No new event name (union or intersection)
            else:
                # All the events (union) are taken
                events_df_cur = events_cur
            
            # Append the events across all channels
            events_df = pd.concat([events_df,events_df_cur],ignore_index=True)

        # Sort events based on the start_sec
        events_df.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')

        # Write the cache
        cache = {}
        cache['events'] = events_df
        self._cache_manager.write_mem_cache(self.identifier, cache)

        # Output the new list of events
        return {
            'events': events_df
        } 


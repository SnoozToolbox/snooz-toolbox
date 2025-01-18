"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Select (filter) events from specific sleep stages.
    I.e. useful to select spindles occuring in NREM sleep stage.

    Parameters
    -----------
        events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            Events to select based on the sleep stages.
        sleep_stages: pandas DataFrame
            Sleep stages used to select events.
        stages_selection: String
            A string of each sleep stage separeted by a comma with the same 
            valid values as sleep_stages. Example : '1,4,5,7'
        group_selection : String
            The group event to select. Can have many group separated by a comma.
        name_selection : String
            The name event to select. Can have many name separated by a comma.
            
    Returns
    -----------    
        events_selected : pandas DataFrame
            Events selected from specific sleep stages (stages_selection).
        sleep_stages_selected : pandas DataFrame
            Sleep stages selected from specific sleep stages (stages_selection).
"""

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeRuntimeException import NodeRuntimeException
from CEAMSModules.EventCompare import performance as perf
from ..PSGReader import commons
import numpy as np
import pandas as pd


DEBUG = False

class FilterEvents(SciNode):
    """
    Select (filter) events from specific sleep stages.

    Parameters
    -----------
        events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            Events to select based on the sleep stages.
        sleep_stages: pandas DataFrame
            Sleep stages used to select events.
        stages_selection: String
            A string of each sleep stage separeted by a comma with the same 
            valid values as sleep_stages. Example : '1,4,5,7'
        group_selection : String
            The group event to select. Can have many group separated by a comma.
        name_selection : String
            The name event to select. Can have many name separated by a comma.
    Returns
    -----------    
        events_selected : pandas DataFrame
            Events selected from specific sleep stages (stages_selection).
        sleep_stages_selected : andas DataFrame
            Sleep stages selected from specific sleep stages (stages_selection).
"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('FilterEvents.__init__')
        self._filename = None
        InputPlug('events', self)
        InputPlug('sleep_stages', self)
        InputPlug('stages_selection', self)      
        InputPlug('group_selection', self)  
        InputPlug('name_selection', self)   
        OutputPlug('events_selected', self)
        OutputPlug('sleep_stages_selected', self)
    

    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass


    def compute(self, events, sleep_stages, stages_selection, group_selection, name_selection):
        """
        Select (filter) events from specific sleep stages.

        Parameters
        -----------
            events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                Events to select based on the sleep stages.
            sleep_stages: pandas DataFrame
                Sleep stages used to select events.
            stages_selection: String
                A string of each sleep stage separeted by a comma with the same 
                valid values as sleep_stages. Example : '1,4,5,7'
            group_selection : String
                The group event to select. Can have many group separated by a comma.
            name_selection : String
                The name event to select. Can have many name separated by a comma.               
    Returns
    -----------    
        events_selected : pandas DataFrame
            Events selected from specific sleep stages (stages_selection).
        sleep_stages_selected : andas DataFrame
            Sleep stages selected from specific sleep stages (stages_selection).
        """

        if DEBUG: print('FilterEvents.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None             

        # Sleep stage selection
        # if sleep_stages is empty, the events can still be filtered from name or group
        if isinstance(sleep_stages, str) and sleep_stages == '':
            err_message = "WARNING: sleep_stages not connected"
            self._log_manager.log(self.identifier, err_message)
            selected_sleep_stage = pd.DataFrame(data=None,columns=['group','name','start_sec','duration_sec','channels'])

            if len(stages_selection)>0:
                raise NodeRuntimeException(self.identifier, "sleep_stages", \
                    f"FilterEvents : sleep_stages is not connected and there is a sleep stage selection{stages_selection}")                

            # If there are no selection of evens neither sleep stage selection, the events_selected is empty
            if (group_selection=='' or group_selection==None) and (name_selection=='' or group_selection==None):
                events_selected = pd.DataFrame(data=None,columns=['group','name','start_sec','duration_sec','channels'])
                err_message = "WARNING: events are not selected"
                self._log_manager.log(self.identifier, err_message)                
                # Write the cache
                cache = {}
                cache['events'] = events_selected
                self._cache_manager.write_mem_cache(self.identifier, cache)
                return {
                    'events_selected': events_selected,
                    'sleep_stages_selected': selected_sleep_stage
                }           
        else:
            # Prepare the sleep stage pandas DataFrame
            # Convert the possible int into string
            sleep_stages.loc[:,'name'] = sleep_stages.loc[:,'name'].apply(str).copy()
            selected_sleep_stage = sleep_stages.copy()
            # Find all events that occur during the selected sleep stages
            if isinstance(stages_selection, str) and len(stages_selection)>0:
                selected_sleep_stage = pd.DataFrame(data=None,columns=['group','name','start_sec','duration_sec','channels'])
                # split list to keep only chosen stage
                stages = list(stages_selection.split(","))            
                for stage in stages:
                    current_sleep_stage = sleep_stages[sleep_stages['group']==commons.sleep_stages_group]
                    current_sleep_stage = current_sleep_stage[current_sleep_stage['name']==stage]
                    selected_sleep_stage = pd.concat([selected_sleep_stage,current_sleep_stage],ignore_index=True)
                    #selected_sleep_stage = selected_sleep_stage.append(current_sleep_stage)
                selected_sleep_stage.sort_values(by=['start_sec'], inplace=True)

        # Events selection
        # if events is empty, the Sleep stages can still be filtered from the sleep stage selection
        if isinstance(events, str) and events == '':
            err_message = "WARNING: events not connected"
            self._log_manager.log(self.identifier, err_message)
            events_selected = pd.DataFrame(data=None,columns=['group','name','start_sec','duration_sec','channels'])
        else:
            # It is important to make a copy otherwise other instance of events
            # will also be modified.
            events_selected = events.copy()

        # Apply group and/or name selection
        # Find all events with a group defined by the user
        if len(events_selected)>0:
            # A group or a name is defined for a selection
            if (isinstance(group_selection,str) and len(group_selection)>0) or (isinstance(name_selection,str) and len(name_selection)>0) :
                # More than a single group is defined
                if (isinstance(group_selection,str) and len(group_selection)>0) and len(group_selection.split(','))>1:
                    # The same number of names and groups are defined
                    if (isinstance(name_selection,str) and len(name_selection)>0) and (len(group_selection.split(','))==len(name_selection.split(','))): 
                        events_groups_name = pd.DataFrame(data=None,columns=['group','name','start_sec','duration_sec','channels'])
                        for i, group in enumerate(group_selection.split(',')):
                            tmp = events_selected[(events_selected['group']==group) & (events_selected['name']==name_selection.split(',')[i])]
                            events_groups_name = pd.concat([events_groups_name, tmp])
                        events_selected = events_groups_name
                    else:
                        raise NodeRuntimeException(self.identifier, "group_selection", \
                            f"FilterEvents : the number of groups must match the number of names")
                # More than a single name
                elif (isinstance(name_selection,str) and len(name_selection)>0) and len(name_selection.split(','))>1:
                    raise NodeRuntimeException(self.identifier, "group_selection", \
                        f"FilterEvents : the number of groups must match the number of names")
                else:
                    # A single group
                    if (isinstance(group_selection,str) and len(group_selection)>0):
                        events_selected = events_selected[events_selected['group']==group_selection]
                    # A single name
                    if (isinstance(name_selection,str) and len(name_selection)>0):
                        events_selected = events_selected[events_selected['name']==name_selection]

        # Apply stage selection
        # If epochs have been filtered out because of the stage selection
        if len(selected_sleep_stage)<len(sleep_stages): # maybe not true because the sleep_stages could have been filtered outside the plugin.
            # select_events_from_stages(self, selected_sleep_stage, events_selected)
            events_selected = self.select_events_from_stages(selected_sleep_stage, events_selected)

        # Write the cache
        cache = {}
        cache['events'] = events_selected
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'events_selected': events_selected,
            'sleep_stages_selected': selected_sleep_stage
        }     
    

    def select_events_from_stages(self, selected_sleep_stage, events_selected):
        local_fs = 100

        ## Verify if the event have duration
        # duration_times = events_selected['duration_sec'].to_numpy().astype(float)
        ## if len(np.unique(duration_times))==1:
        #     #new_min_dur = 1/local_fs # one sample with the local sampling rate
        #     print("patch!!! slow wave")
        #     new_min_dur=0.5
        #     duration_times = np.ones((len(duration_times),1))*new_min_dur
        #     events_selected['duration_sec']=duration_times

        events_filtered = pd.DataFrame(data=None,columns=['group','name','start_sec','duration_sec','channels'])
        # Find out if the event occur during a selected sleep stages
        [selected_stage_lst, selected_stage_bin] = perf.evt_df_to_bin(selected_sleep_stage, local_fs)
        events_selected = events_selected.reset_index(drop=True)  # make sure indexes pair with number of rows         
        for index, event in events_selected.iterrows():
            # Create a binary vector to represent the event
            event_bin_vect = np.ones(int(np.round(event['duration_sec']*local_fs)))
            event_start_sample = int(np.round(event['start_sec']*local_fs))
            # Find out if at least a part of the event occur during a valid sleep stage
            if any(selected_stage_bin[event_start_sample:event_start_sample+len(event_bin_vect)]):
                # Adjust events filtered if they are not totally included in valid sleep stage
                valid_event_vect = (selected_stage_bin[event_start_sample:event_start_sample+len(event_bin_vect)])
                valid_event_lst = perf.bin_evt_to_lst_sec(valid_event_vect, local_fs)
                valid_event_df = pd.DataFrame(data=None,columns=['group','name','start_sec','duration_sec','channels'])
                for valid_event_start, valid_event_dur in valid_event_lst:
                    current_event = pd.DataFrame(data=None,columns=['group','name','start_sec','duration_sec','channels'])
                    current_event.at[0,'group'] = event["group"]
                    current_event.at[0,'name'] = event["name"]
                    current_event.at[0,'start_sec'] = valid_event_start+event["start_sec"]
                    current_event.at[0,'duration_sec'] = valid_event_dur
                    current_event.at[0,'channels'] = event["channels"]
                    valid_event_df = pd.concat([valid_event_df,current_event],ignore_index=True)
                events_filtered = pd.concat([events_filtered,valid_event_df],ignore_index=True)     
        return events_filtered
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Create a list of event from specific sleep stages during a recording.

    Parameters
    -----------
        epoch_len: double
            The epoch length in second (only required for sleep_stages as array)
        sleep_stages: array or pandas DataFrame
            A sleep stage per epoch (an array of stages from 0-9). Valid values are :
                0 = Wake
                1 = Stage 1
                2 = Stage 2
                3 = Stage 3
                4 = Stage 4
                5 = REM
                6 = Movement time
                7 = Technical time
                9 = undetermined
            pandas DataFrame of events with field
                'group': Group of events this event is part of (String)
                'name': Name of the event (String)
                'start_sec': Starting time of the event in sec (Float)
                'duration_sec': Duration of the event in sec (Float)
                'channels' : Channel where the event occures (String)
        stages: string
            A string of each sleep stage separeted by a comma with the same 
            valid values as sleep_stages. Example : '1,4,5,7'
        merge_events : String 
            '1' to merge selected continuous events, 0 to let them in epochs.
        new_event_name : string (optional)
            To rename selected event. The original name is kept if let blank.
        exclude_NREMP : String
            '1' to exclude nrem period from the sleep_stage_events
            '0' to keep all selected stages
        exclude_REMP : String
            '1' to exclude rem period from the sleep_stage_events
            '0' to keep all selected stages
        in_cycle : String
            '1' to keep only events inluded in the sleep cycles.
            '0' do not use sleep cycles information. 
    Returns
    -----------    
        sleep_stage_events   : pandas DataFrame
            List of events from specific stages
"""
from CEAMSModules.EventCompare import performance as perf
from CEAMSModules.EventReader.manage_events import create_event_dataframe
from commons.NodeInputException import NodeInputException
from flowpipe import SciNode, InputPlug, OutputPlug
from ..PSGReader import commons

import numpy as np
import pandas as pd

DEBUG = False

class SleepStageEvents(SciNode):
    """
    Create a list of event from specific sleep stages during a recording.

    Parameters
    -----------
        epoch_len: double
            The epoch length in second (only required for sleep_stages as array)
        sleep_stages: array or pandas DataFrame
            A sleep stage per epoch (an array of stages from 0-9). Valid values are :
                0 = Wake
                1 = Stage 1
                2 = Stage 2
                3 = Stage 3
                4 = Stage 4
                5 = REM
                6 = Movement time
                7 = Technical time
                9 = undetermined
            pandas DataFrame of events with field
                'group': Group of events this event is part of (String)
                'name': Name of the event (String)
                'start_sec': Starting time of the event in sec (Float)
                'duration_sec': Duration of the event in sec (Float)
                'channels' : Channel where the event occures (String)
        stages: string
            A string of each sleep stage separeted by a comma with the same 
            valid values as sleep_stages. Example : '1,4,5,7'
        merge_events : String 
            1 to merge selected continuous events, 0 to let them in epochs.
        new_event_name : string (optional)
            To rename selected event. The original name is kept if let blank.
        exclude_NREMP : String
            '1' to exclude nrem period from the sleep_stage_events
            '0' to keep all selected stages
        exclude_REMP : String
            '1' to exclude rem period from the sleep_stage_events
            '0' to keep all selected stages
        in_cycle : String
            '1' to keep only events inluded in the sleep cycles.
            '0' do not use sleep cycles information.             
    Returns
    -----------    
        sleep_stage_events   : pandas DataFrame
            List of events from specific stages
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('SleepStageEvents.__init__')
        self._filename = None
        InputPlug('epoch_len', self)
        InputPlug('sleep_stages', self)
        InputPlug('stages', self)       
        InputPlug('merge_events', self)
        InputPlug('new_event_name', self)   
        InputPlug('exclude_nremp', self)     
        InputPlug('exclude_remp', self)  
        InputPlug('in_cycle', self)  
        OutputPlug('sleep_stage_events', self)
        #self.columns = create_event_dataframe(None).columns
        self.MAX_GAP_BWT_EVENTS = 0.1


    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass


    def compute(self, epoch_len, sleep_stages, stages, merge_events, \
        new_event_name, exclude_nremp, exclude_remp, in_cycle):
        """
        Create a list of event from specific sleep stages during a recording.

        Parameters
        -----------
            epoch_len: double
                The epoch length in second (only required for sleep_stages as array)
            sleep_stages: array or pandas DataFrame
                A sleep stage per epoch (an array of stages from 0-9). Valid values are :
                    0 = Wake
                    1 = Stage 1
                    2 = Stage 2
                    3 = Stage 3
                    4 = Stage 4
                    5 = REM
                    6 = Movement time
                    7 = Technical time
                    9 = undetermined
                pandas DataFrame of events with field
                    'group': Group of events this event is part of (String)
                    'name': Name of the event (String)
                    'start_sec': Starting time of the event in sec (Float)
                    'duration_sec': Duration of the event in sec (Float)
                    'channels' : Channel where the event occures (String)
            stages: string
                A string of each sleep stage separeted by a comma with the same 
                valid values as sleep_stages. Example : '1,4,5,7'
            merge_events : string 
                '1' to merge selected continuous events, 0 to let them in epochs.
            new_event_name : string (optional)
                To rename selected event. The original name is kept if let blank.
            exclude_NREMP : String
                '1' to exclude nrem period from the sleep_stage_events
                '0' to keep all selected stages
            exclude_REMP : String
                '1' to exclude rem period from the sleep_stage_events
                '0' to keep all selected stages
            in_cycle : String
                '1' to keep only events inluded in the sleep cycles.
                '0' do not use sleep cycles information. 
        Returns
        -----------    
            sleep_stage_events   : pandas DataFrame
                List of events from specific stages
        """

        if DEBUG: print('SleepStageEvents.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None             

        # Verify inputs
        if isinstance(sleep_stages, str) and sleep_stages == '':
            err_message = "ERROR: signals not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "sleep_stages", \
                f"SleepStageEvents this input is not connected.")
        elif not isinstance(sleep_stages, pd.DataFrame) :
            if isinstance(epoch_len, str) and epoch_len == '':
                err_message = "ERROR: epoch_len not connected"
                self._log_manager.log(self.identifier, err_message)
                raise NodeInputException(self.identifier, "epoch_len", \
                    f"SleepStageEvents this input is not connected.")
        if len(sleep_stages)==0:
            err_message = "WARNING: sleep_stages is empty"
            self._log_manager.log(self.identifier, err_message) 
            return {
                'sleep_stage_events': create_event_dataframe(None)
            }              

        # Because of the non integer sampling rate 
        # we round all start and duration to 0.x precision
        #sleep_stages = sleep_stages.round(2) # It is now managed by looking at the difference higher than 0.1 s

        # Depending of how the input plugin are defined (tool, interface or node)
        # the type of the input can be integer, string or bool
        # so, it could be 1, '1', True, 'True'
        # Type cast the input as bool
        if isinstance(merge_events, str):
            merge_events = bool(eval(merge_events))
        else:
            merge_events = bool(merge_events)
        if isinstance(exclude_nremp, str):
            exclude_nremp = bool(eval(exclude_nremp))
        else:
            exclude_nremp = bool(exclude_nremp)
        if isinstance(exclude_remp, str):
            exclude_remp = bool(eval(exclude_remp))
        else:
            exclude_remp = bool(exclude_remp)
        if isinstance(in_cycle, str):
            in_cycle = bool(eval(in_cycle))
        else:
            in_cycle = bool(in_cycle)

        # To exclude nrem period
        if exclude_nremp==True:
            if isinstance(sleep_stages,pd.DataFrame): 
                # Extract rem period
                nremp_df = sleep_stages[ sleep_stages.group==commons.nrem_period_group]
                nremp_df.reset_index(drop=True,inplace=True)
            else:
                err_message = "ERROR: impossible to exclude NREMP wthout the sleep cycles information"
                self._log_manager.log(self.identifier, err_message)
                raise NodeInputException(self.identifier, "exclude_nremp", \
                    f"SleepStageEvents exclude_nremp=1 and the sleep cycles information is missing.")     

        # To exclude rem period
        if exclude_remp==True:
            if isinstance(sleep_stages,pd.DataFrame): 
                # Extract rem period
                remp_df = sleep_stages[sleep_stages.group==commons.rem_period_group]
                remp_df.reset_index(drop=True,inplace=True)
            else:
                err_message = "ERROR: impossible to exclude REMP wthout the sleep cycles information"
                self._log_manager.log(self.identifier, err_message)
                raise NodeInputException(self.identifier, "exclude_remp", \
                    f"SleepStageEvents exclude_remp=1 and the sleep cycles information is missing.")    

        # To use data included in cycle only
        if in_cycle==True:
            if isinstance(sleep_stages,pd.DataFrame): 
                # Extract rem period
                cycle_df = sleep_stages[sleep_stages.group==commons.sleep_cycle_group]
                cycle_df.reset_index(drop=True,inplace=True)
                # Round epoch length (for non integer sampling rate)
                #cycle_df = cycle_df.round({'duration_sec':0})
            else:
                err_message = "ERROR: impossible to use sleep cycle information"
                self._log_manager.log(self.identifier, err_message)
                raise NodeInputException(self.identifier, "in_cycle", \
                    f"SleepStageEvents in_cycle=1 and the sleep cycles information is missing.")            

        # Select or create events from the selected sleep stages
        stages = list(stages.split(","))  # split list to keep only chosen stage
        if len(stages)==0:
            stages = commons.valid_stage
            log_message = "WARNING: stages was empty, so it has been set to commons.valid_stage"
            self._log_manager.log(self.identifier, log_message)            

        events_df = create_event_dataframe(None)
        for stage in stages:
            # If sleep_stages is an array (from xml)
            if isinstance(sleep_stages,np.ndarray) or isinstance(sleep_stages,list):
                events_index = np.where(sleep_stages == int(stage))[0]
                # Rename event name is needed
                if len(new_event_name)>0:
                    event_name = new_event_name
                else :#
                    event_name = stage
                events = [('stage', event_name, index * epoch_len, epoch_len, '') for index in events_index]
                # Create a pandas events_df of events (each row is an event)
                stage_df = create_event_dataframe(events)
                events_df = pd.concat( [events_df, stage_df])
            # If sleep_stages is a DataFrame event list
            elif isinstance(sleep_stages,pd.DataFrame):  
                stage_df = sleep_stages[sleep_stages.group==commons.sleep_stages_group]  
                stage_df = stage_df[stage_df.name==stage]
                # Rename event name if needed
                if len(new_event_name)>0:
                    stage_df.name = new_event_name
                # Concatenate all the stages
                events_df = pd.concat( [events_df, stage_df])
        events_df.reset_index(drop=True,inplace=True)

        # To exclude signals outside cycle
        if in_cycle==True: 
            # It is possible to have a subject without cycle especially if uncomplete cycles are not included
            onlyCycle = create_event_dataframe(None)                
            if len(cycle_df)>0:
                # Keep any stage inside cycle
                for index, row in cycle_df.iterrows():
                    idx_start = events_df[events_df.start_sec<(row.start_sec+row.duration_sec)].index
                    idx_stop = events_df[ (events_df.start_sec+events_df.duration_sec) > (row.start_sec)].index
                    idx_in_cycle = idx_start.intersection(idx_stop)
                    onlyCycle = pd.concat([onlyCycle,events_df.loc[idx_in_cycle]])
            events_df = onlyCycle 
            events_df.reset_index(drop=True,inplace=True)   

        # To exclude nrem period
        if exclude_nremp==True:
            if len(nremp_df)>0:
                no_nremp = events_df
                # Exclude any stage during rem period
                for index, row in nremp_df.iterrows():
                    idx_start = no_nremp[no_nremp.start_sec<(row.start_sec+row.duration_sec)].index
                    idx_stop = no_nremp[ (no_nremp.start_sec+no_nremp.duration_sec) > (row.start_sec)].index
                    idx_drop_remp = idx_start.intersection(idx_stop)
                    no_nremp = no_nremp.drop(idx_drop_remp)
                events_df = no_nremp
                events_df.reset_index(drop=True,inplace=True)

        # To exclude rem period
        if exclude_remp==True:
            if len(remp_df)>0:
                no_remp = events_df
                # Exclude any stage during rem period
                for index, row in remp_df.iterrows():
                    idx_start = no_remp[no_remp.start_sec<(row.start_sec+row.duration_sec)].index
                    idx_stop = no_remp[ (no_remp.start_sec+no_remp.duration_sec) > (row.start_sec)].index
                    idx_drop_no_remp = idx_start.intersection(idx_stop)
                    no_remp = no_remp.drop(idx_drop_no_remp)
                events_df = no_remp 
                events_df.reset_index(drop=True,inplace=True)          

        # Format events_df event list
        events_df = events_df.sort_values(by=['start_sec'])
        events_df = events_df.reset_index(drop=True)

        # Merge selected continuous events
        if merge_events == True:

            # Compute the difference between consecutive events, so the difference 
            # between the end of an event and the start of the next event
            start_event = events_df.start_sec.values
            duration_event = events_df.duration_sec.values

            if len(start_event) > 0:
                # If the difference is less than 0.1, merge the events
                current_event = np.array([start_event[0],duration_event[0]])
                events_lst_merge = []
                for i_start, i_dur in zip(start_event[1:],duration_event[1:]):
                    # Calculate the gap between the current event and the next
                    gap = i_start - (current_event[0] + current_event[1])
                    # if the difference is less than 0.1
                    # increase the duration of the current event by i_dur+abs(diff)
                    if abs(gap) < self.MAX_GAP_BWT_EVENTS:
                        current_event[1] = current_event[1] + i_dur + gap
                    else:
                        # Append the current event to the merged list and start a new event
                        events_lst_merge.append(current_event)
                        current_event = [i_start, i_dur]
                # Append the last event
                events_lst_merge.append(current_event)
                
                if len(new_event_name)>0:
                    event_name = new_event_name
                else:
                    event_name = "merge_event"
                events = [('stage', event_name, start_sec, duration_sec, "") \
                    for start_sec, duration_sec in events_lst_merge]
                # Create a pandas events_df of events (each row is an event)
                merge_df = create_event_dataframe(events)
                merge_df = merge_df.sort_values(by=['start_sec'])
                merge_df = merge_df.reset_index(drop=True)
                events_df = merge_df

        # It is important to make a copy otherwise other instance of events
        # will also be modified.
        events_to_write = events_df.copy()
        if len(events_to_write)==0:
            err_message = "ERROR: sleep stage events is empty"
            self._log_manager.log(self.identifier, err_message)            

        # Write the cache
        cache = {}
        cache['events'] = events_to_write
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'sleep_stage_events': events_to_write
        }      

    

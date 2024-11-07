"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Compute the sleep cycles.
    Creates and appends events with group: "cycles" and name: "cycle number" ex.1.

    Cycle definition:
    The cycle starts with a nrem period.
    The nrem period ends with a rem stage.
    The rem period ends when there is 15 mins without a rem stage.
    The end of the rem period is updated to the last rem stage or 
    the start of the following nrem period.

    Parameters
    -----------
        events_in : pandas DataFrame
            List of events to rename (columns=['group','name','start_sec','duration_sec','channels']).
        parameters : String (dict converted into a string)
            "{
                'defined_option':'Minimum Criteria'
                'Include_SOREMP' : '1'
                'Include_last_incompl' : '1'
                'Include_all_incompl: : '1'
                'dur_ends_REMP' = '15'
                'NREM_min_len_first':'0'
                'NREM_min_len_mid_last':'15'
                'NREM_min_len_val_last':'0'
                'REM_min_len_first':'0'
                'REM_min_len_mid':'0'
                'REM_min_len_last':'0'
                'mv_end_REMP':'0'
                'sleep_stages':'N1, N2, N3, R'
                'details': '<p>Adjust options based on minimum criteria.</p>
            }"
        label : string
            Label to identify the current recording
    Returns
    -----------    
        events_out : pandas DataFrame
            List of events (columns=['group','name','start_sec','duration_sec','channels'])
        parameters_cycle : Dict
            Options used to define the cycles
            "{
                'defined_option':'Minimum Criteria'
                'Include_SOREMP' : '1'
                'Include_last_incompl' : '1'
                'Include_all_incompl: : '1'
                'dur_ends_REMP' = '15'
                'NREM_min_len_first':'0'
                'NREM_min_len_mid_last':'15'
                'NREM_min_len_val_last':'0'
                'REM_min_len_first':'0'
                'REM_min_len_mid':'0'
                'REM_min_len_last':'0'
                'mv_end_REMP':'0'
                'sleep_stages':'N1, N2, N3, R'
                'details': '<p>Adjust options based on minimum criteria.</p>
            }"
        sleep_cycles_epoch : list
            The list of sleep cycle in epoch (one cycle per row).
            Epoch start and end are inclusive and start to 0.
            [((NREM start, NREM stop),(REM start, REM stop))\
            ((NREM start, NREM stop),(REM start, REM stop))\
            ...]
        REM_period_epoch : list
            The list of REM period in epoch (one cycle per row).
            Epoch start and end are inclusive and start to 0.
            [(REM start, REM stop))\
            ((REM start, REM stop))\
            ...]
        cycle_labelled :  pandas DataFrame
            List of NREM and REM periods (columns=['group','name','start_sec','duration_sec','channels'])
            where the group is the input label. 
"""

from flowpipe import SciNode, InputPlug, OutputPlug
import numpy as np
import pandas as pd

from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from ..PSGReader import commons
from CEAMSModules.EventCompare import performance as perf


DEBUG = False

class SleepCyclesDelimiter(SciNode):
    """
    Compute the sleep cycles.
    Creates and appends events with group: "cycles" and name: "cycle number" ex.1.

    Cycle definition:
    The cycle starts with a nrem period.
    The nrem period ends with a rem stage.
    The rem period ends when there is 15 mins without a rem stage.
    The end of the rem period is updated to the last rem stage or 
    the start of the following nrem period.

    Parameters
    -----------
        events_in : pandas DataFrame
            List of events to rename (columns=['group','name','start_sec','duration_sec','channels']).
        parameters : String (dict converted into a string)
            "{
                'defined_option':'Minimum Criteria'
                'Include_SOREMP' : '1'
                'Include_last_incompl' : '1'
                'Include_all_incompl: : '1'
                'dur_ends_REMP' : '15'
                'NREM_min_len_first':'0'
                'NREM_min_len_mid_last':'15'
                'NREM_min_len_val_last':'0'
                'REM_min_len_first':'0'
                'REM_min_len_mid':'0'
                'REM_min_len_last':'0'
                'mv_end_REMP':'0'
                'sleep_stages':'N1, N2, N3, R'
                'details': '<p>Adjust options based on minimum criteria.</p>
            }"
        label : string
            Label to identify the current recording
    Returns
    -----------    
        events_out : pandas DataFrame
            List of events (columns=['group','name','start_sec','duration_sec','channels'])
        parameters_cycle : Dict
            Options used to define the cycles
            "{
                'defined_option':'Minimum Criteria'
                'Include_SOREMP' : '1'
                'Include_last_incompl' : '1'
                'Include_all_incompl: : '1'
                'dur_ends_REMP' : '15'
                'NREM_min_len_first':'0'
                'NREM_min_len_mid_last':'15'
                'NREM_min_len_val_last':'0'
                'REM_min_len_first':'0'
                'REM_min_len_mid':'0'
                'REM_min_len_last':'0'
                'mv_end_REMP':'0'
                'sleep_stages':'N1, N2, N3, R'
                'details': '<p>Adjust options based on minimum criteria.</p>
            }"
        sleep_cycles_epoch : list
            The list of sleep cycle in epoch (one cycle per row).
            Epoch start and end are inclusive and start to 0.
            [((NREM start, NREM stop),(REM start, REM stop))\
            ((NREM start, NREM stop),(REM start, REM stop))\
            ...]
        REM_period_epoch : list
            The list of REM period in epoch (one cycle per row).
            Epoch start and end are inclusive and start to 0.
            [(REM start, REM stop))\
            ((REM start, REM stop))\
            ...]
        cycle_labelled :  pandas DataFrame
            List of NREM and REM periods (columns=['group','name','start_sec','duration_sec','channels'])
            where the group is the input label. 
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('SleepCyclesDelimiter.__init__')
        self._filename = None
        InputPlug('events_in', self)
        InputPlug('parameters', self)     
        InputPlug('label', self)
        OutputPlug('events_out', self)
        OutputPlug('events_cycles', self)
        OutputPlug('parameters_cycle', self)
        OutputPlug('sleep_cycles_epoch', self)
        OutputPlug('REM_period_epoch', self)
        OutputPlug('cycle_labelled', self)


    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass


    def compute(self, events_in, parameters, label):
        """
        Compute the sleep cycles.
        Creates and appends events with group: "cycles" and name: "cycle number" ex.1.

        Cycle definition:
        The cycle starts with a nrem period.
        The nrem period ends with a rem stage.
        The rem period ends when there is 15 mins without a rem stage.
        The end of the rem period is updated to the last rem stage or 
        the start of the following nrem period.

        Parameters
        -----------
            events_in : pandas DataFrame
                List of events to rename (columns=['group','name','start_sec','duration_sec','channels']).
            parameters : String (dict converted into a string)
                "{
                    'defined_option':'Minimum Criteria'
                    'Include_SOREMP' : '1'
                    'Include_last_incompl' : '1'
                    'Include_all_incompl: : '1'
                    'dur_ends_REMP' : '15'
                    'NREM_min_len_first':'0'
                    'NREM_min_len_mid_last':'15'
                    'NREM_min_len_val_last':'0'
                    'REM_min_len_first':'0'
                    'REM_min_len_mid':'0'
                    'REM_min_len_last':'0'
                    'mv_end_REMP':'0'
                    'sleep_stages':'N1, N2, N3, R'
                    'details': '<p>Adjust options based on minimum criteria.</p>
                }"
            label : string
                Label to identify the current recording
        Returns
        -----------    
            events_out : pandas DataFrame
                List of events (columns=['group','name','start_sec','duration_sec','channels'])
            parameters_cycle : Dict
                Options used to define the cycles
                "{
                    'defined_option':'Minimum Criteria'
                    'Include_SOREMP' : '1'
                    'Include_last_incompl' : '1'
                    'Include_all_incompl: : '1'
                    'dur_ends_REMP' : '15'
                    'NREM_min_len_first':'0'
                    'NREM_min_len_mid_last':'15'
                    'NREM_min_len_val_last':'0'
                    'REM_min_len_first':'0'
                    'REM_min_len_mid':'0'
                    'REM_min_len_last':'0'
                    'mv_end_REMP':'0'
                    'sleep_stages':'N1, N2, N3, R'
                    'details': '<p>Adjust options based on minimum criteria.</p>
                }"
            sleep_cycles_epoch : list
                The list of sleep cycle in epoch (one cycle per row).
                Epoch start and end are inclusive and start to 0.
                [((NREM start, NREM stop),(REM start, REM stop))\
                ((NREM start, NREM stop),(REM start, REM stop))\
                ...]
            REM_period_epoch : list
                The list of REM period in epoch (one cycle per row).
                Epoch start and end are inclusive and start to 0.
                [(REM start, REM stop))\
                ((REM start, REM stop))\
                ...]
            cycle_labelled :  pandas DataFrame
                List of NREM and REM periods (columns=['group','name','start_sec','duration_sec','channels'])
                where the group is the input label. 
    """

        if DEBUG: print('SleepCyclesDelimiter.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None

        # Convert the String into a dictionary
        parameters_dict = eval(parameters)

        # Verify inputs
        if isinstance(events_in, str) and events_in == '':
            raise NodeInputException(self.identifier, "events_in", \
                "SleepCyclesDelimiter events_in parameter must be set.")

        if isinstance(events_in, pd.DataFrame) and len(events_in) == 0:
            war_message = "WARNING : events_in parameter is empty."
            self._log_manager.log(self.identifier, war_message)
            #raise NodeInputException(self.identifier, "events_in", \
                #"SleepCyclesDelimiter events_in parameter is empty.")

        # It is important to make a copy otherwise other instance of events
        # will also be modified.
        events_out = events_in.copy()

        cycle_labelled = pd.DataFrame(columns=['group','name','start_sec','duration_sec','channels'])
        cycle_labelled.loc[0,'group']=label

        # Extract all sleep stages from the events list
        sleep_stage_events = events_out[events_out['group']==commons.sleep_stages_group]
        sleep_stage_events['name'] = sleep_stage_events['name'].apply(str)

        # Warning when there is no sleep stage scoring
        if sleep_stage_events.empty:
            war_message = "WARNING : events_in parameter does not include sleep stage scoring."
            self._log_manager.log(self.identifier, war_message)
            # Write the cache
            cache = {}
            cache['events'] = events_out
            self._cache_manager.write_mem_cache(self.identifier, cache)
            return {
                'parameters_cycle' : parameters_dict,
                'events_out': events_out,
                'sleep_cycles_epoch' : [],
                'REM_period_epoch' : [],
                'cycle_labelled' : cycle_labelled,
            }  

        sleep_stage_events.reset_index(drop=True,inplace=True)
        epoch_length_sec = np.round(sleep_stage_events['duration_sec'][0])

        # drop stages until the first epoch scored 'wake,N1,N2,N3,R'
            # sleep_stage_scored : dataframe
            #     Sleep stage list (columns=['group','name','start_sec','duration_sec','channels'])
            #     without the stages before the lights out.
            #     Every events before the first awake or sleep stages are dropped.        
            #   Interval between first epoch scored and 'sleep_stages'
            #   If 'sleep_stages' is the first epoch the SO is 0.
            #   The N1 stage is added because the sleep latency can exclude the N1
        sleep_stage_scored = self._drop_until_first_epoch(sleep_stage_events, 'W,N1,N2,N3,R')
        if len(sleep_stage_scored)==0:
            war_message = "WARNING : events_in parameter must include the sleep stages."
            self._log_manager.log(self.identifier, war_message)
            # Write the cache
            cache = {}
            cache['events'] = events_out
            self._cache_manager.write_mem_cache(self.identifier, cache)
            return {
                'parameters_cycle' : parameters_dict,
                'events_out': events_out,
                'sleep_cycles_epoch' : [],
                'REM_period_epoch' : [],
                'cycle_labelled' : cycle_labelled,
            }  

        # Find the first occurrence of asleep stage
        asleep_events_df, first_stage_scored_idx, last_stage_scored_idx = \
            self._select_stage(sleep_stage_scored, parameters_dict['sleep_stages'])
        if not asleep_events_df.empty:
            first_asleep_event = asleep_events_df.iloc[0]
            last_asleep_event = asleep_events_df.iloc[-1]
            sleep_stage_scored = sleep_stage_scored.loc[first_stage_scored_idx:last_stage_scored_idx]
            # pas même indice extraire les stades scoré -> "loc" for indexes and "iloc" for integer row!
            # iloc -> start : step : stop (stop is the last index you dont want where the stop applied)
            # loc -> start : step : stop (stop is the last index you want)
        else:
            war_message = "WARNING : events_in parameter does not include any sleep stages."
            self._log_manager.log(self.identifier, war_message)
            # Write the cache
            cache = {}
            cache['events'] = events_out
            self._cache_manager.write_mem_cache(self.identifier, cache)

            return {
                'parameters_cycle' : parameters_dict,
                'events_out': events_out,
                'sleep_cycles_epoch' : [],
                'REM_period_epoch' : [],
                'cycle_labelled' : cycle_labelled,
            }           

        #----------------------------------------------------------------------
        # Compute the sleep cycles
        #----------------------------------------------------------------------
        # Compute end of the REM periods
        remper_end_lst = self._compute_rem_period_end(sleep_stage_scored,\
            parameters_dict['sleep_stages'], float(parameters_dict['dur_ends_REMP']), \
                float(parameters_dict['NREM_min_len_val_last']))

        # Compute start of the NREM and REM periods
        # REM end periods are updated in case the recording ends in NREM
        # Remove the use of nrem_rem_df
        # nremper_start_lst, remper_start_lst, remper_end_lst = \
        #     self._compute_period_start(first_asleep_event, last_asleep_event, \
        #         nrem_rem_df, remper_end_lst, parameters_dict)  
        nremper_start_lst, remper_start_lst, remper_end_lst = \
            self._compute_period_start(first_asleep_event, last_asleep_event, \
                sleep_stage_scored, remper_end_lst, parameters_dict)                    

        #--------------------------------------------
        # Adjust the end of the rem period if required
        #--------------------------------------------
        if int(parameters_dict['mv_end_REMP'])==1:
            # The last REMP end is moved if there is an extra NREMP
            if len(nremper_start_lst)>len(remper_end_lst):
                for cycle_i in range(len(remper_end_lst)):
                    remper_end_lst[cycle_i] = nremper_start_lst[cycle_i+1]                
            else:
                for cycle_i in range(len(remper_end_lst)-1):
                    remper_end_lst[cycle_i] = nremper_start_lst[cycle_i+1]
    
        #-------------------------------------------
        # Manage Fusion
        #-------------------------------------------
            # Perform fusion on REMP.
            # A too short REMP joins the preceding REMP.
        nremper_start_lst, remper_start_lst, remper_end_lst = \
            self._REMP_fusion(parameters_dict, nremper_start_lst, remper_start_lst, remper_end_lst)

        #----------------------------------------------------------------------
        # Define each REMP including incomplete period
        #----------------------------------------------------------------------
        # REM period definition in epoch
        # start and end are inclusive and start to 0
        # [(REM start, REM stop))\
        # (REM start, REM stop))\
        # ...]
        rem_def = []
        if len(remper_start_lst)>0:
            remper_start_epoch = np.round((remper_start_lst-sleep_stage_events.start_sec[0]) / epoch_length_sec)
            remper_end_epoch = np.round((remper_end_lst-sleep_stage_events.start_sec[0]) / epoch_length_sec)
        for cycle_i, start_sec_remp in enumerate(remper_end_lst):
            rem_def.append([(int(remper_start_epoch[cycle_i]),int(remper_end_epoch[cycle_i])-1)])

        #-------------------------------------------
        # Manage incomplete cycle.
        #-------------------------------------------
        # Evaluate (mark or discard) incomplete cycles.
        # SOREMP and last complete cycles are evaluated. 
        # Last cycles are discarded if parameters_dict[Include_last_incompl]==0.
        # The first cycle is kept even in SOREMP but marked as incomplete.
        # No fusion on incomplete cycle
        cycle_complete, nremper_start_lst, remper_start_lst, remper_end_lst = \
            self._incomplete_cycle_evaluation(\
                parameters_dict, nremper_start_lst, remper_start_lst, remper_end_lst)

        # TODO Miss the metadata

        #----------------------------------------------------------------------
        # Create an dataframe event for each NREM and REM period.
        #----------------------------------------------------------------------
        if len(nremper_start_lst)==0:
            nrem_cycle_event = []
            rem_cycle_event = []
            cycle_event = []
        elif len(remper_end_lst)==0:
            nremper_dur = remper_start_lst[0] - nremper_start_lst[0]
            #nremper_dur = nrem_rem_df['duration_sec'][0]
            nrem_cycle_event = [[commons.nrem_period_group, commons.nrem_period_group, nremper_start_lst[0], nremper_dur, '']]
            cycle_event = [[commons.sleep_cycle_group, commons.sleep_cycle_group, nremper_start_lst[0], nremper_dur, '']]
        else:            
            nrem_cycle_event = []
            rem_cycle_event = []
            cycle_event = []
            for cycle_i, start_sec_remp in enumerate(remper_end_lst):
                nremper_dur = remper_start_lst[cycle_i]-nremper_start_lst[cycle_i]
                nrem_cycle_event.append([commons.nrem_period_group, commons.nrem_period_group, nremper_start_lst[cycle_i], nremper_dur, ''])
                remper_dur = remper_end_lst[cycle_i]-remper_start_lst[cycle_i]
                rem_cycle_event.append([commons.rem_period_group, commons.rem_period_group, remper_start_lst[cycle_i], remper_dur, ''])
                cycle_dur = (remper_start_lst[cycle_i]+remper_dur)-nremper_start_lst[cycle_i]
                cycle_event.append([commons.sleep_cycle_group, commons.sleep_cycle_group, nremper_start_lst[cycle_i], cycle_dur, ''])
        
            # The last REMP can be missing (when the last NREMP is < NREM_min_len_val_last)
            # In that case the cycle is always incomplete, but can be showed
            if len(remper_end_lst)<len(cycle_complete):
                #last_nrem_end = int(nrem_rem_df['duration_sec'].iloc[-1])+int(nrem_rem_df['start_sec'].iloc[-1])
                # remove the use of the nrem_rem_df
                last_nrem_end = sleep_stage_scored['start_sec'].values[-1]+sleep_stage_scored['duration_sec'].values[-1]
                nremper_dur = last_nrem_end-nremper_start_lst[-1]
                nrem_cycle_event.append([commons.nrem_period_group, commons.nrem_period_group, nremper_start_lst[-1], nremper_dur, ''])
                cycle_event.append([commons.sleep_cycle_group, commons.sleep_cycle_group, nremper_start_lst[-1], nremper_dur, ''])

        cycle_event_df = pd.DataFrame(data=nrem_cycle_event,columns=['group','name','start_sec','duration_sec','channels'])
        if len(remper_end_lst)>0:
            cycle_event_df = pd.concat([cycle_event_df,pd.DataFrame(\
                data=rem_cycle_event, columns=['group','name','start_sec','duration_sec','channels'])])
        cycle_event_df = pd.concat([cycle_event_df,pd.DataFrame(\
                data=cycle_event, columns=['group','name','start_sec','duration_sec','channels'])])
        
        #events_out = events_out.append(cycle_event_df)
        events_out = pd.concat([events_out, cycle_event_df])
        events_out.sort_values(by=['start_sec'],inplace=True)
        events_out = events_out.reset_index(drop=True)     

        # Concatenate the group and name
        if len(nrem_cycle_event)>0: # To avoid to loose the group
            nrem_cycle_event_label = [[label, j[1], j[2], j[3], j[4]] for j in nrem_cycle_event]
            cycle_labelled = pd.DataFrame(data=nrem_cycle_event_label,columns=['group','name','start_sec','duration_sec','channels'])
        if len(rem_cycle_event)>0: # To avoid to loose the group
            rem_cycle_event_label = [[label, j[1], j[2], j[3], j[4]] for j in rem_cycle_event]
            cycle_labelled = pd.concat([cycle_labelled,pd.DataFrame(\
                data=rem_cycle_event_label, columns=['group','name','start_sec','duration_sec','channels'])])
        cycle_labelled.sort_values(by=['start_sec'],inplace=True)
        cycle_labelled = cycle_labelled.reset_index(drop=True)     

        #----------------------------------------------------------------------
        # Define each rem and rem period per epoch
        #----------------------------------------------------------------------
        # NREM-REM cycle definition in epoch
        # start and end are inclusive and start to 0
        # [((NREM start, NREM stop),(REM start, REM stop))\
        # ((NREM start, NREM stop),(REM start, REM stop))\
        # ...]
        cycle_def = []
        if len(nremper_start_lst)>0:
            nremper_start_epoch = np.round((nremper_start_lst-sleep_stage_events.start_sec[0]) / epoch_length_sec)
            if len(remper_start_lst)==0:
                # remove the use of the nrem_rem_df
                #remper_start_lst = [nrem_rem_df['start_sec'][0] + nrem_rem_df['duration_sec'][0]]
                remper_start_lst = [sleep_stage_scored['start_sec'].values[-1]+sleep_stage_scored['duration_sec'].values[-1]]
                remper_end_lst = remper_start_lst
                remper_start_epoch = [np.round((remper_start_lst-sleep_stage_events.start_sec[0]) / epoch_length_sec)]
                remper_end_epoch = [np.round((remper_end_lst-sleep_stage_events.start_sec[0]) / epoch_length_sec)]                 
            else:
                remper_start_epoch = np.round((remper_start_lst-sleep_stage_events.start_sec[0]) / epoch_length_sec)
                remper_end_epoch = np.round((remper_end_lst-sleep_stage_events.start_sec[0]) / epoch_length_sec)

            for cycle_i, start_sec_remp in enumerate(remper_end_lst):
                cycle_def.append([(int(nremper_start_epoch[cycle_i]),int(remper_start_epoch[cycle_i])-1),\
                    (int(remper_start_epoch[cycle_i]),int(remper_end_epoch[cycle_i])-1),int(cycle_complete[cycle_i])])

            # The last REMP can be missing (when the last NREMP is < NREM_min_len_val_last)
            # In that case the cycle is always incomplete, but can be showed
            if len(remper_end_lst)<len(cycle_complete):
                nremper_start_epoch = np.round((nremper_start_lst[-1]-sleep_stage_events.start_sec[0]) / epoch_length_sec)
                # remove the use of the nrem_rem_df
                #last_nrem_end = int(nrem_rem_df['duration_sec'].iloc[-1])+int(nrem_rem_df['start_sec'].iloc[-1])-sleep_stage_events.start_sec[0]
                last_nrem_end = int(sleep_stage_scored['start_sec'].values[-1]+sleep_stage_scored['duration_sec'].values[-1])
                last_nrem_end_epoch = np.round((last_nrem_end-sleep_stage_events.start_sec[0]) / epoch_length_sec)
                cycle_def.append([(int(nremper_start_epoch),int(last_nrem_end_epoch)-1),\
                    (int(last_nrem_end_epoch),int(last_nrem_end_epoch)-1),int(cycle_complete[cycle_i])])

        # Write the cache
        cache = {}
        cache['events'] = events_out
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'parameters_cycle' : parameters_dict,
            'events_out': events_out,
            'sleep_cycles_epoch' : cycle_def,
            'REM_period_epoch' : rem_def,
            'cycle_labelled' : cycle_labelled,
        }  


    def _compute_rem_period_end(self, sleep_stages_df, NREM_stages, dur_ends_REMP_min, NREM_min_len_val_last):
        """
        To compute the list of rem period end.

        Parameters
        -----------
            nrem_rem_df : dataframe columns=['name','start_sec','duration_sec']
                List of nrem and rem events sorted with the start_sec. 
            dur_ends_REMP_min : integer
                Duration in minutes without REM that ends the REM period.
        Returns
        -----------                
            remper_end_lst : list
                List of end of REM period.
        """
        # TODO revise this !!!
        # it is possible to have 2 consecutive REM bouts (without nrem bout between i.e. only awake)
        remper_end_lst = []
        current_nor_dur = 0
        possible_REM_period = 0
        rem_end = sleep_stages_df['start_sec'].values[0]
        nrem_dur = 0
        nrem_start = 0
        for index, row in sleep_stages_df.iterrows():
            if row["name"] == commons.sleep_stages_name['R']:
                rem_end = row['start_sec'] + row['duration_sec']
                possible_REM_period = 1
                current_nor_dur = 0
                nrem_dur = 0
                nrem_start = 0
            elif ((row["name"] in commons.nremp_stages_without_n1)) or \
                ((row["name"] in commons.nremp_stages_with_n1) and ('N1' in NREM_stages)):
                current_nor_dur = row['start_sec'] + row['duration_sec'] - rem_end
                if nrem_start==0:
                    nrem_start = row['start_sec']
                nrem_dur = row['start_sec'] + row['duration_sec'] - nrem_start
            else:
                current_nor_dur = row['start_sec'] + row['duration_sec'] - rem_end
            if round(current_nor_dur) >= (dur_ends_REMP_min*60): # The round is needed for non integer fs
                if possible_REM_period==1:
                    remper_end_lst.append(rem_end)
                possible_REM_period = 0
        # remove duplicates
        remper_end_lst = list(set(remper_end_lst))
        remper_end_lst.sort()
        # Adjust for the last REM period
        if possible_REM_period==1:
            # If the recording ends in REMP
            if current_nor_dur==0:
                remper_end_lst.append(rem_end)
            # If the recording ends in NREMP but its duration is shorter than 15 min
            # the last REMP end has not been append
            else:
                remper_end_lst.append(rem_end)
                # If the last NREMP is long enough to create a new cycle
                # Create an empty REMP: the last REMP 
                # (which is duration > 0 will be considered a middle cycle and not the last cycle)
                # nrem_dur is the duration of the last NREMP 
                #   NREMP starts at the first nrem stage and ends at the last nrem stage
                #   NREMP can include awake
                if nrem_dur/60 >= NREM_min_len_val_last:
                    rem_end_artificial = row['start_sec'] + row['duration_sec']
                    remper_end_lst.append(rem_end_artificial)
        # Recording ends in NREMP
        else:
            # If the last NREMP is long enough to create a new cycle
            # Create an empty REMP: the last REMP 
            # (which is duration > 0 will be considered a middle cycle and not the last cycle)
            if nrem_dur/60 >= NREM_min_len_val_last:
                rem_end_artificial = row['start_sec'] + row['duration_sec']
                remper_end_lst.append(rem_end_artificial)
        return remper_end_lst


    # def _compute_period_start(self, first_asleep_event, last_asleep_event, \
    #     nrem_rem_df, remper_end_lst, parameters_dict):
    def _compute_period_start(self, first_asleep_event, last_asleep_event, \
        sleep_stage_scored, remper_end_lst, parameters_dict):
        """
        To compute the list of nrem and rem period start.

        Parameters
        -----------
            first_asleep_event : dataframe (columns=['group','name','start_sec','duration_sec','channels'])
                The event linked to the sleep onset.
            last_asleep_event : dataframe (columns=['group','name','start_sec','duration_sec','channels'])
                The sleep last event.
            sleep_stage_scored : dataframe (columns=['group','name','start_sec','duration_sec','channels'])
                List of sleep stage from first to last asleep. 
            remper_end_lst : list
                List of end of REM period.
            parameters_dict : dict
                Dictionary of parameters linked to the NREMP duration.
                NREM_min_len_first
                NREM_min_len_mid_last
                NREM_min_len_val_last

        Returns
        -----------                
            nremper_start_lst : list
                List of start of NREM period.
            remper_start_lst : list
                List of start of REM period.
            remper_end_lst : list
                List of end of REM period.
        """            
        nremper_start_lst = []
        remper_start_lst = []
        # First cycle generaly starts with a NREM stage except when the subject goes directly in REM
        if 'N1' in parameters_dict['sleep_stages'] :
            nrem_start_sec = first_asleep_event['start_sec'] if first_asleep_event['name'] in commons.nremp_stages_with_n1 else None
        else:
            nrem_start_sec = first_asleep_event['start_sec'] if first_asleep_event['name'] in commons.nremp_stages_without_n1 else None
        if not nrem_start_sec==None :
            nremper_start_lst.append(nrem_start_sec)
        rem_extract = sleep_stage_scored[sleep_stage_scored['name']==commons.sleep_stages_name['R']]
        rem_extract.reset_index(drop=True,inplace=True)
        if not nrem_start_sec==None:
            first_rem_epoch_i = rem_extract[rem_extract['start_sec']>nrem_start_sec].first_valid_index()
        else:
            first_rem_epoch_i = rem_extract.first_valid_index()
            nrem_start_sec = rem_extract.loc[first_rem_epoch_i]['start_sec']
            nremper_start_lst.append(nrem_start_sec)
        if first_rem_epoch_i==None:
            war_message = "WARNING : events_in parameter does not include any R stages."
            self._log_manager.log(self.identifier, war_message)
            return nremper_start_lst, remper_end_lst, remper_end_lst
        #remper_start_lst.append(rem_extract.iloc[first_rem_epoch_i].start_sec)
        remper_start_lst.append(rem_extract.loc[first_rem_epoch_i].start_sec)
        # For each additional cycle
        for remper_end in remper_end_lst:
            # nrem
            cur_nrem_rem_df = sleep_stage_scored[sleep_stage_scored.start_sec>=remper_end]
            if not cur_nrem_rem_df.empty:
                cur_nrem_rem_df.reset_index(drop=True,inplace=True)
                #first_nrem_epoch_i = cur_nrem_rem_df[cur_nrem_rem_df['name']=='nrem'].first_valid_index() 
                if 'N1' in parameters_dict['sleep_stages']:
                    NREM_event_df, first_ori_idx, last_ori_idx = \
                        self._select_stage(cur_nrem_rem_df, 'N1,N2,N3')
                else:
                    NREM_event_df, first_ori_idx, last_ori_idx = \
                        self._select_stage(cur_nrem_rem_df, 'N2,N3')
                first_nrem_epoch_i = first_ori_idx
                first_rem_epoch_i = cur_nrem_rem_df[cur_nrem_rem_df['name']==commons.sleep_stages_name['R']].first_valid_index()
            else:
                first_nrem_epoch_i = None
                first_rem_epoch_i = None
            if not first_rem_epoch_i == None:
                #rem_start_sec = cur_nrem_rem_df.iloc[first_rem_epoch_i].start_sec
                rem_start_sec = cur_nrem_rem_df.loc[first_rem_epoch_i].start_sec
            if not first_nrem_epoch_i == None:
                #nrem_start_sec = cur_nrem_rem_df.iloc[first_nrem_epoch_i].start_sec
                nrem_start_sec = cur_nrem_rem_df.loc[first_nrem_epoch_i].start_sec
                if not first_rem_epoch_i == None:
                    # if any which one is first (REMP or NREMP)
                    if rem_start_sec<nrem_start_sec: # if there is a NREMP of 0 min (incomplete cycle but still)
                        nremper_start_lst.append(rem_start_sec)
                        remper_start_lst.append(rem_start_sec)
                    else:
                        nremper_start_lst.append(nrem_start_sec)
                        first_rem_epoch_i = rem_extract[rem_extract['start_sec']>=nrem_start_sec].first_valid_index()
                        if not first_rem_epoch_i == None:
                            remper_start_lst.append(rem_extract.iloc[first_rem_epoch_i].start_sec)
                        # Recording ends in NREMP 
                        else:
                            end_sleep_sec = last_asleep_event.start_sec + last_asleep_event.duration_sec
                            last_NREMP_dur_sec =  end_sleep_sec - nremper_start_lst[-1]
                            # NREMP is longer than NREM_min_len_val_last
                            # there is an artificial extra REMP
                            if last_NREMP_dur_sec/60>= float(parameters_dict['NREM_min_len_val_last']):
                                remper_start_lst.append(remper_end_lst[-1])
                else:
                    nremper_start_lst.append(nrem_start_sec)
                    first_rem_epoch_i = rem_extract[rem_extract['start_sec']>=nrem_start_sec].first_valid_index()
                    if not first_rem_epoch_i == None:
                        #remper_start_lst.append(rem_extract.iloc[first_rem_epoch_i].start_sec)
                        remper_start_lst.append(rem_extract.loc[first_rem_epoch_i].start_sec)
                    # Recording ends in NREMP 
                    else:
                        end_sleep_sec = last_asleep_event.start_sec + last_asleep_event.duration_sec
                        last_NREMP_dur_sec =  end_sleep_sec - nremper_start_lst[-1]
                        # NREMP is longer than NREM_min_len_val_last
                        # there is an artificial extra REMP
                        if last_NREMP_dur_sec/60>= float(parameters_dict['NREM_min_len_val_last']):
                            remper_start_lst.append(remper_end_lst[-1])                      
            # cannot be here: when the recording ends in REMP, we dont want to add the same end twice
            # if there is no more NREM, we dont need to look for a REMP

        return nremper_start_lst, remper_start_lst, remper_end_lst


    def _create_NREM_REM_events(self, NREM_stages, sleep_stages_df):
        """""
        To create a list of NREM and REM events based on the NREM stages.
        Consecutive nrem epochs are merge as one nrem event.

        Parameters
        -----------         
            NREM_stages : String
                List of sleep stages to consider as the nrem.
            sleep_stages_df : dataframe
                List of stages (each stage is an epoch)
        Returns
        -----------
            nrem_rem_df : dataframe columns=['name','start_sec','duration_sec']
                List of nrem and rem events sorted with the start_sec.

        """""
        # Create a list of NREM events
        if 'N1' in NREM_stages:
            NREM_event_df, first_stage_scored_idx, last_stage_scored_idx = \
                self._select_stage(sleep_stages_df, 'N1,N2,N3')
        else:
            NREM_event_df, first_stage_scored_idx, last_stage_scored_idx = \
                self._select_stage(sleep_stages_df, 'N2,N3')
        # Keep track of the first and last nrem
        local_fs_precision = 256
        nrem_stage_lst , nrem_bin_vect = perf.evt_df_to_bin(NREM_event_df,local_fs_precision)
        nrem_stage_lst = perf.bin_evt_to_lst_sec(nrem_bin_vect,local_fs_precision)
        nrem_events = [('nrem', start, dur) for start, dur in nrem_stage_lst]
        # Create a list of REM events
        REM_event_df, first_stage_scored_idx, last_stage_scored_idx = \
            self._select_stage(sleep_stages_df, 'R')
        rem_stage_lst , rem_bin_vect = perf.evt_df_to_bin(REM_event_df, local_fs_precision)
        rem_stage_lst = perf.bin_evt_to_lst_sec(rem_bin_vect,local_fs_precision)
        rem_events = [('rem', start, dur) for start, dur in rem_stage_lst]
        # Merge both lists
        nrem_rem_events = []
        nrem_rem_events.extend(nrem_events)
        nrem_rem_events.extend(rem_events)
        nrem_rem_df = pd.DataFrame(data=nrem_rem_events, columns=['name','start_sec','duration_sec'])
        nrem_rem_df.sort_values(by=['start_sec'],inplace=True)
        nrem_rem_df.reset_index(drop=True,inplace=True)
        return nrem_rem_df


    def _drop_until_first_epoch(self, stage_event_df, stage_name):
        """
        Finds the first epoch scored "stage_name" in the dataframe events 
        "stage_event_df" and drops all the events before the first epoch found.

        Parameters
        -----------
            stage_event_df : DataFrame  
                List of events (columns=['group','name','start_sec','duration_sec','channels'])
            stage_name : String
                Stage names comma separated
        Returns
        ----------- 
            valid_stage_event_df : DataFrame  
                List of events (columns=['group','name','start_sec','duration_sec','channels'])                 
        """
        # Convert names into number
        stages_num = []
        for stage in stage_name.split(','):
            stage = stage.strip()
            stages_num.append(commons.sleep_stages_name[stage])
        # Find the first occurrence of the stages
        first_epoch_i = stage_event_df[stage_event_df['name'].isin(stages_num)].first_valid_index()
        if first_epoch_i==None:
            war_message = "WARNING : events_in parameter must include the sleep stage."
            self._log_manager.log(self.identifier, war_message)
            return pd.DataFrame(columns=['group','name','start_sec','duration_sec','channels'])
        else:
            # Remove all the previous epochs
            valid_stage_event_df = stage_event_df.drop(range(0,first_epoch_i))
            # Reset the index to start at 0
            valid_stage_event_df.reset_index(drop=True,inplace=True)
            return valid_stage_event_df


    def _find_last_epoch(self, stage_event_df, stage_name):
        """
        Finds the last epoch scored "stage_name" in the dataframe events 
        "stage_event_df".

        Parameters
        -----------
            stage_event_df : DataFrame  
                List of events (columns=['group','name','start_sec','duration_sec','channels'])
            stage_name : String
                Stage names comma separated
        Returns
        ----------- 
            last_event_df : DataFrame  
                The last valid events (columns=['group','name','start_sec','duration_sec','channels'])    
        """
        # Convert names into number
        stages_num = []
        for stage in stage_name.split(','):
            stage = stage.strip()
            stages_num.append(commons.sleep_stages_name[stage])
        # Find the first occurrence of the stages
        last_epoch_i = stage_event_df[stage_event_df['name'].isin(stages_num)].last_valid_index()
        # Extract the last valid epoch
        #last_event_df = stage_event_df.iloc[last_epoch_i]
        last_event_df = stage_event_df.loc[last_epoch_i]
        return last_event_df


    def _incomplete_cycle_evaluation(self, parameters_dict, nremper_start_lst, remper_start_lst, remper_end_lst):
        """
        Evaluate (mark or discard) incomplete cycles.
        SOREMP and last complete cycles are evaluated. 
        Last cycles are discarded if parameters_dict[Include_last_incompl]==0.
        The first cycle is kept even in SOREMP but marked as incomplete.

        Parameters
        -----------
            parameters_dict : dict
                Dictionary of parameters linked to the NREMP duration.
                NREM_min_len_first
                NREM_min_len_mid_last
                NREM_min_len_val_last

            nremper_start_lst : list
                List of start of NREM period.
            remper_start_lst : list
                List of start of REM period.
            remper_end_lst : list
                List of end of REM period.

        Returns
        -----------      
            cycle_complete : array
                Each cycle is marked are complete (1) or incomplete (0).          
            nremper_start_lst : list
                List of start of NREM period.
            remper_start_lst : list
                List of start of REM period.
            remper_end_lst : list
                List of end of REM period.
        """
        # Only a single NREMP, no REMP at all
        if len(remper_end_lst)==0:
            if int(parameters_dict['Include_last_incompl'])==0:
                    nremper_start_lst.pop(-1)
                    cycle_complete = []
            else:
                cycle_complete = [0]
            return cycle_complete, nremper_start_lst, remper_start_lst, remper_end_lst
        else:
            cycle_complete = np.ones(len(remper_end_lst)) # incomplete cycles may be discarded
            
#            if parameters_dict['Include_all_incompl']==0:

            # Compute period duration in order to discard cycle
            # The last REMP can be missing (when the last NREMP is < NREM_min_len_val_last)
            if len(remper_end_lst)<len(nremper_start_lst):
                nremper_dur = np.asarray(remper_start_lst)-np.asarray(nremper_start_lst[0:-1])
            else:
                nremper_dur = np.asarray(remper_start_lst)-np.asarray(nremper_start_lst)
            remper_dur = np.asarray(remper_end_lst)-np.asarray(remper_start_lst)
            for cycle_i in range(len(remper_end_lst)-1,-1,-1):
                # Last cycle
                if cycle_i==len(remper_end_lst)-1:
                    if remper_dur[cycle_i]==0:
                        cycle_complete[-1]=0
                    # Recording ends in REMP
                    #   Last cyle is incomplete if 
                    elif float(parameters_dict['NREM_min_len_val_last'])>0:
                        cycle_complete[-1]=0
                # First cycle
                elif cycle_i==0:
                    #if float(parameters_dict['NREM_min_len_first'])>0:
                    if nremper_dur[cycle_i] < (float(parameters_dict['NREM_min_len_first'])*60):
                        cycle_complete[cycle_i] = 0
                        war_message = "Cycle " + str(cycle_i) + \
                            ": NREMP lasts less than " + parameters_dict['NREM_min_len_first'] + " min"
                        self._log_manager.log(self.identifier, war_message)
                # Middle cycle
                else:
                    # REM periods can be shorter than 15 mins when there 
                    # otherwise the REM period continues (we need 15 min without R stage to end a REM period)
                    # The warning is let there in case the NREM_min_len_mid_last is changed > than 15 min
                    #if float(parameters_dict['NREM_min_len_mid_last'])>0:
                    if nremper_dur[cycle_i] < (float(parameters_dict['NREM_min_len_mid_last'])*60):
                        cycle_complete[cycle_i] = 0
                        war_message = "Cycle " + str(cycle_i) + \
                            ": NREMP lasts less than " + parameters_dict['NREM_min_len_mid_last'] + " min"
                        self._log_manager.log(self.identifier, war_message)

            # Middle cycles are incomplete if they last less than 15 min.
            # It is possible with Aeschbach and Floyd when there are awake or n1
            # sleep stages between a REMP and a NREMP. 
            # More than 15 min without R stages ends the REMP and a NREMP can start
            # and could last less than 15 min.

            if int(parameters_dict['Include_all_incompl'])==0:
                # First and last cycle are managed lower with UI option
                for cycle_i in range(1,len(remper_end_lst)-1,1):
                    if cycle_complete[cycle_i]==0:
                        nremper_start_lst.pop(cycle_i)
                        remper_start_lst.pop(cycle_i)
                        remper_end_lst.pop(cycle_i)
                n_cycles = len(remper_end_lst)  # number of complete cycles (including incomplete first and last)
                first_cycle = cycle_complete[0] # save the complete state of the first cycle
                last_cycle = cycle_complete[-1] # save the complete state of the last cycle
                cycle_complete = np.ones(n_cycles) # incomplete middle cycles have been removed
                cycle_complete[0]=first_cycle
                cycle_complete[-1]=last_cycle

            # The last REMP can be missing
            #   when there is no R stage at all and the last NREMP is < NREM_min_len_val_last
            # In that case the cycle is always incomplete
            if len(remper_end_lst)<len(nremper_start_lst):
                cycle_complete[-1]=0
                cycle_complete = np.concatenate([cycle_complete, np.array([0])], axis=0)

            if int(parameters_dict['Include_last_incompl'])==0:
                if len(cycle_complete)>0 and cycle_complete[-1]==0:
                    if len(remper_end_lst)<len(nremper_start_lst):
                        nremper_start_lst.pop(-1)
                        cycle_complete = cycle_complete[0:-1]
                if len(cycle_complete)>0 :
                    if cycle_complete[-1]==0:
                        nremper_start_lst.pop(-1)
                        remper_start_lst.pop(-1)
                        remper_end_lst.pop(-1)
                        cycle_complete = cycle_complete[0:-1] 

            # Remove SOREMP if requested
            if int(parameters_dict['Include_SOREMP'])==0 :
                if len(cycle_complete)>0 and cycle_complete[0]==0:
                    nremper_start_lst.pop(0)
                    remper_start_lst.pop(0)
                    remper_end_lst.pop(0)
                    cycle_complete = cycle_complete[1:]
            
        return cycle_complete, nremper_start_lst, remper_start_lst, remper_end_lst


    def _REMP_fusion(self, parameters_dict, nremper_start_lst, remper_start_lst, remper_end_lst):
        """
        Perform fusion on REMP.
        A too short REMP joins the preceding REMP.
        No fusion in incomplete cycles.

        Parameters
        -----------
            parameters_dict : dict
                Dictionary of parameters linked to the NREMP duration.
                REM_min_len_first
                REM_min_len_mid
                REM_min_len_last
            nremper_start_lst : list
                List of start of NREM period.
            remper_start_lst : list
                List of start of REM period.
            remper_end_lst : list
                List of end of REM period.

        Returns
        -----------              
            nremper_start_lst : list
                List of start of NREM period.
            remper_start_lst : list
                List of start of REM period.
            remper_end_lst : list
                List of end of REM period.
        """
        # Only a single NREMP, no REMP at all, then no fusion
        if len(remper_end_lst)==0:
            return nremper_start_lst, remper_start_lst, remper_end_lst

        cycle_valid = np.ones(len(remper_end_lst)) # invalid cycles are joined to the preceding one
        # Compute period duration in order to join REMP
        remper_dur = np.asarray(remper_end_lst)-np.asarray(remper_start_lst)

        # Test for the fusion of REMP
        for cycle_i, remper_dur_val in enumerate(remper_dur):
            # Apply criteria based on the cycle number
            # First cycle
            if cycle_i==0:
                if float(parameters_dict['REM_min_len_first'])>0:
                    if remper_dur[cycle_i]>0:
                        if remper_dur_val < (float(parameters_dict['REM_min_len_first'])*60):
                            cycle_valid[cycle_i] = 0
                            war_message = "Cycle " + str(cycle_i) + \
                                ": REMP lasts less than " + parameters_dict['REM_min_len_first'] + " min"
                            self._log_manager.log(self.identifier, war_message)
            # Last cycle
            elif cycle_i==len(remper_dur)-1:
                if float(parameters_dict['REM_min_len_last'])>0:
                    if remper_dur[cycle_i]>0:
                        if remper_dur[cycle_i] < (float(parameters_dict['REM_min_len_last'])*60):
                            cycle_valid[cycle_i] = 0
                            war_message = "Cycle " + str(cycle_i) + \
                                ": REMP lasts less than " + parameters_dict['REM_min_len_last'] + " min, then is it joined to the preceding REMP"
                            self._log_manager.log(self.identifier, war_message)
            # Middle cycle
            else:
                if float(parameters_dict['REM_min_len_mid'])>0:
                    if remper_dur[cycle_i]>0:
                        if remper_dur[cycle_i] < (float(parameters_dict['REM_min_len_mid'])*60):
                            cycle_valid[cycle_i] = 0
                            war_message = "Cycle " + str(cycle_i) + \
                                ": REMP lasts less than " + parameters_dict['REM_min_len_mid'] + " min, then is it joined to the preceding REMP"
                            self._log_manager.log(self.identifier, war_message)
        
        # The last REMP can be missing (when the last NREMP is < NREM_min_len_val_last)
        # In that case the cycle is always incomplete
        if len(remper_end_lst)<len(nremper_start_lst):
            last_nremper_start = nremper_start_lst[-1]
        else: 
            last_nremper_start = None

        # Joint invalid cycle with the preceding one
        # The invalid cycle is removed and the preceding rem period end is updated
        nremper_start_lst = [start for (start, cycle_valid) \
            in zip(nremper_start_lst, cycle_valid) if cycle_valid]
        remper_start_lst = [start for (start, cycle_valid) \
            in zip(remper_start_lst, cycle_valid) if cycle_valid]
        for cycle_i, end_sec_remp in enumerate(remper_end_lst):
            if cycle_valid[cycle_i]==0 and cycle_i>0:
                remper_end_lst[cycle_i-1]=end_sec_remp
        remper_end_lst = [end for (end, cycle_valid) \
            in zip(remper_end_lst, cycle_valid) if cycle_valid]

        if last_nremper_start:
            nremper_start_lst.append(last_nremper_start)
    
        return nremper_start_lst, remper_start_lst, remper_end_lst


    def _select_stage(self, stage_event_df, stage_name):
        """
        Extract only the stages included in "stage_name" from the dataframe event list.

        Parameters
        -----------
            stage_event_df : DataFrame  
                List of events (columns=['group','name','start_sec','duration_sec','channels'])
            stage_name : String
                Stage names comma separated
        Returns
        ----------- 
            stage_event_df : DataFrame  
                List of events (columns=['group','name','start_sec','duration_sec','channels'])
            first_index : int
                Index of the first stage included in stage_name
            last_index : int 
                Index of the last stage included in stage_name
        """
        # Convert names into number
        stages_num = []
        for stage in stage_name.split(','):
            stage = stage.strip()
            if stage == 'N1(1 continuous min)':
                stages_num.append(commons.sleep_stages_name['N1'])
            else:
                stages_num.append(commons.sleep_stages_name[stage])
        # Extract only the stages included in "stage_name" from the dataframe event list.
        stage_event_df = stage_event_df[stage_event_df['name'].isin(stages_num)]
        if len(stage_event_df)>0:
            first_index = stage_event_df.index[0]
            last_index = stage_event_df.index[-1]
        else:
            first_index = []
            last_index = []
        # Reset the index to start at 0
        stage_event_df.reset_index(drop=True,inplace=True)
        return stage_event_df, first_index, last_index
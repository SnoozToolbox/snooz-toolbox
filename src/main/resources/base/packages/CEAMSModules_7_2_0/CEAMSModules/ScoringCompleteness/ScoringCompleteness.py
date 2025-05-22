"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    ScoringCompleteness
    TODO CLASS DESCRIPTION
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

import numpy as np
import pandas as pd

DEBUG = False

class ScoringCompleteness(SciNode):
    """
    Evaluate if the scoring (events) is unique, complete and specifique to the sleep staging.
    The output file log any problems. The log includes which event (if any) 
    is not unique or outside the sleep staging.  The log also includes which 
    part of the sleep stage does not have any scoring (events).

    Inputs:
        "sleep_stages":  Pandas Dataframe (columns=['group','name','start_sec','duration_sec','channels']) 
            List of sleep stages and sleep cycles.
        "events":  Pandas Dataframe (columns=['group','name','start_sec','duration_sec','channels']) 
            The scoring, a list of events.
        "output_file": string
            path and name of the output file to log the scoring problems.
    Outputs:
        
    """
    def __init__(self, **kwargs):
        """ Initialize module ScoringCompleteness """
        super().__init__(**kwargs)
        if DEBUG: print('ScoringCompleteness.__init__')

        # Input plugs
        InputPlug('sleep_stages',self)
        InputPlug('events',self)
        InputPlug('output_file',self)
        
        # Output plugs

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, sleep_stages, events, output_file):
        """
            Evaluate if the scoring (events) is unique, complete and specifique to the sleep staging.
            The output file log any problems. The log includes which event (if any) 
            is not unique or outside the sleep staging.  The log also includes which 
            part of the sleep stage does not have any scoring (events).

            Inputs:
                "sleep_stages":  Pandas Dataframe (columns=['group','name','start_sec','duration_sec','channels']) 
                    List of sleep stages and sleep cycles.
                "events":  Pandas Dataframe (columns=['group','name','start_sec','duration_sec','channels']) 
                    The scoring, a list of events.
                "output_file": string
                    path and name of the output file to log the scoring problems.
            Outputs:
        """

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if not isinstance(events,pd.DataFrame):
            raise NodeInputException(self.identifier, "events", \
                f"ScoringCompleteness input of wrong type. Expected: <class 'DataFrame'> received: {type(events)}")
        if not isinstance(sleep_stages,pd.DataFrame):
            raise NodeInputException(self.identifier, "sleep_stages", \
                f"ScoringCompleteness input of wrong type. Expected: <class 'DataFrame'> received: {type(sleep_stages)}")

        outfile_df = pd.DataFrame(data=None, columns=['group','name','start_sec','duration_sec','channels', 'time_elapsed(HH:MM:SS)', 'comment'])

        # Reset index
        events.reset_index(inplace=True, drop=True)
        # Sort events based on the start_sec
        events.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')     
        # Evaluate duplicates and remove them only locally
        duplicated_rows = events.duplicated()
        if any(duplicated_rows==True):
            duplicated_events = events.loc[duplicated_rows].copy()
            if len(duplicated_events)>1:
                for index, duplicated_event in duplicated_events.iterrows():
                    current_event = duplicated_event.copy()
                    current_event['comment'] = 'Same event duplicated'
                    # Compute the time elapsed for each event
                    time_elapsed = {}
                    time_elapsed["HH"] = (np.floor(current_event.start_sec/3600)).astype(int)
                    time_elapsed["MM"] = ( np.floor( (current_event.start_sec-time_elapsed["HH"]*3600) / 60 )).astype(int)
                    time_elapsed["SS"] = current_event.start_sec-time_elapsed["HH"]*3600 - time_elapsed["MM"]*60
                    current_event['time_elapsed(HH:MM:SS)'] = str(time_elapsed["HH"])\
                            + ':' + str(time_elapsed['MM']) + ':' + str(time_elapsed['SS'])
                    current_event_df = current_event.to_frame().T
                    outfile_df = pd.concat([outfile_df, current_event_df])
            else:
                duplicated_events['comment'] = 'Same event duplicated'
                # Compute the time elapsed for each event
                time_elapsed = {}
                time_elapsed["HH"] = (np.floor(duplicated_events['start_sec'].values[0]/3600)).astype(int)
                time_elapsed["MM"] = ( np.floor( (duplicated_events['start_sec'].values[0]-time_elapsed["HH"]*3600) / 60 )).astype(int)
                time_elapsed["SS"] = duplicated_events['start_sec'].values[0]-time_elapsed["HH"]*3600 - time_elapsed["MM"]*60
                duplicated_events['time_elapsed(HH:MM:SS)'] = str(time_elapsed["HH"])\
                        + ':' + str(time_elapsed['MM']) + ':' + str(time_elapsed['SS'])
                # Concatenate the current duplicated event to the group of events
                outfile_df = pd.concat([outfile_df, duplicated_events])
            # The duplicated events are dropped locally to avoid analysing them twice
            events = events.drop_duplicates()  

        # Reset index
        events.reset_index(inplace=True, drop=True)
        # Sort events based on the start_sec
        events.sort_values('start_sec', axis=0, inplace=True, ignore_index='True') 
        # Loop through events to evaluate if they are included in the sleep stages
        stage_i_events = np.empty((len(events),2))
        stage_i_events[:] = np.nan
        for index, event in events.iterrows():
            # Find event.start_sec
            idx_start = sleep_stages[sleep_stages.start_sec <= event.start_sec].index
            idx_stop = sleep_stages[(sleep_stages.start_sec+sleep_stages.duration_sec)\
                 > event.start_sec].index
            idx_select_evt = idx_start.intersection(idx_stop)
            if len(idx_select_evt)==0:
                outside_events_s = event.copy() 
                outside_events_s['comment'] = 'Outside selected sleep stages'
                # Compute the time elapsed for each event
                time_elapsed = {}
                time_elapsed["HH"] = (np.floor(outside_events_s.start_sec/3600)).astype(int)
                time_elapsed["MM"] = ( np.floor( (outside_events_s.start_sec-time_elapsed["HH"]*3600) / 60 )).astype(int)
                time_elapsed["SS"] = outside_events_s.start_sec-time_elapsed["HH"]*3600 - time_elapsed["MM"]*60
                outside_events_s['time_elapsed(HH:MM:SS)'] = str(time_elapsed["HH"])\
                        + ':' + str(time_elapsed['MM']) + ':' + str(time_elapsed['SS'])
                outside_events_df = outside_events_s.to_frame().T
                # Concatenate the current outside event to the group of events
                outfile_df = pd.concat([outfile_df, outside_events_df])
            elif len(idx_select_evt)>1:
                print("Events spread on more than one epoch")
                stage_i_events[index,0] = idx_select_evt[0]
                stage_i_events[index,1] = event.start_sec
            else:
                stage_i_events[index,0] = idx_select_evt[0]
                stage_i_events[index,1] = event.start_sec

        # TODO
        epoch_len_to_process = events['duration_sec'].unique()
        if len(epoch_len_to_process)>1:
            for len_i in epoch_len_to_process:
                # Find all occurence 
                print("Events duration not all unique")
        else:
            epoch_len_to_process = epoch_len_to_process[0]

        # Loop through the sleep stages to evaluate if they are all scored.
        epoch_len = round(int(sleep_stages.duration_sec.values[0]))
        n_mini_epoch = epoch_len/epoch_len_to_process
        if not n_mini_epoch.is_integer():
            raise NodeInputException(self.identifier, "events", \
                f"ScoringCompleteness input with bad content. Expected integer for mini epoch len : [sleep stage duration / events duration]")
        else:
            n_mini_epoch = int(n_mini_epoch)
            for index, stage in sleep_stages.iterrows():
                expected_starts = range(int(stage.start_sec),int(stage.start_sec+epoch_len),int(epoch_len_to_process))
                mini_epoch_start_sec = stage_i_events[stage_i_events[:,0]==index,1]
                if (not (len(expected_starts)==len(mini_epoch_start_sec))) or \
                    (not all(mini_epoch_start_sec==expected_starts)):
                    stage_comment = stage.copy()
                    stage_comment_df = stage_comment.to_frame()
                    stage_comment_df= stage_comment_df.T
                    # Loop through missing ones or duplicated ones to list mini epoch number
                    for i_expt_start in expected_starts:
                        cur_start = mini_epoch_start_sec[mini_epoch_start_sec==i_expt_start]
                        # The expected is missing
                        if len(cur_start)==0:
                            miss_epoch_comment_df = stage_comment_df.copy()
                            miss_epoch_comment_df['group'] = "mini epoch"
                            miss_epoch_comment_df['name'] = "mini epoch"
                            miss_epoch_comment_df['start_sec'] = i_expt_start
                            miss_epoch_comment_df['duration_sec'] = epoch_len_to_process
                            miss_epoch_comment_df['comment'] = f"Miss scoring"
                            # Compute the time elapsed for each event
                            time_elapsed = {}
                            time_elapsed["HH"] = (np.floor(i_expt_start/3600)).astype(int)
                            time_elapsed["MM"] = ( np.floor( (i_expt_start-time_elapsed["HH"]*3600) / 60 )).astype(int)
                            time_elapsed["SS"] = i_expt_start-time_elapsed["HH"]*3600 - time_elapsed["MM"]*60
                            miss_epoch_comment_df['time_elapsed(HH:MM:SS)'] = str(time_elapsed["HH"])\
                                    + ':' + str(time_elapsed['MM']) + ':' + str(time_elapsed['SS'])
                            # Concatenate the current outside event to the group of events
                            outfile_df = pd.concat([outfile_df, miss_epoch_comment_df])                            
                        # The expected is found more than once
                        if len(cur_start)>1:
                            stage_comment = stage.copy()
                            duplicated_epoch_comment_df = stage_comment.to_frame()
                            duplicated_epoch_comment_df= duplicated_epoch_comment_df.T
                            duplicated_epoch_comment_df['group'] = "mini epoch"
                            duplicated_epoch_comment_df['name'] = "mini epoch"
                            duplicated_epoch_comment_df['start_sec'] = i_expt_start
                            duplicated_epoch_comment_df['duration_sec'] = epoch_len_to_process
                            duplicated_epoch_comment_df['comment'] = f"Different scores for same mini epoch"
                            # Compute the time elapsed for each event
                            time_elapsed = {}
                            time_elapsed["HH"] = (np.floor(i_expt_start/3600)).astype(int)
                            time_elapsed["MM"] = ( np.floor( (i_expt_start-time_elapsed["HH"]*3600) / 60 )).astype(int)
                            time_elapsed["SS"] = i_expt_start-time_elapsed["HH"]*3600 - time_elapsed["MM"]*60
                            duplicated_epoch_comment_df['time_elapsed(HH:MM:SS)'] = str(time_elapsed["HH"])\
                                    + ':' + str(time_elapsed['MM']) + ':' + str(time_elapsed['SS'])
                            # Concatenate the current outside event to the group of events
                            outfile_df = pd.concat([outfile_df, duplicated_epoch_comment_df])

        if len(outfile_df)>0:
            try :
                outfile_df.to_csv(path_or_buf=output_file, sep='\t', index=True, mode='w', header=True, encoding="utf_8")
            except :
                error_message = f"Snooz can not write in the file {output_file}."+\
                    f" Check if the drive is accessible and ensure the file is not already open."
                raise NodeRuntimeException(self.identifier, "ScoringCompleteness", error_message)                
        
        # Log message for the Logs tab
        self._log_manager.log(self.identifier, f"{output_file} processed.")  

        # Write to the cache to use the data in the resultTab
        # cache = {}
        # cache['this_is_a_key'] = 42
        # self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
        }
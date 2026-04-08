"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    EventSleepReport
    
    Generate event sleep report.
"""
from datetime import datetime, timedelta
from logging import raiseExceptions
from math import nan
import numpy as np
import os
import pandas as pd
import unicodedata

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from ..PSGReader import commons
from CEAMSModules.EventCompare import performance as perf

DEBUG = False

class EventSleepReport(SciNode):
    """
    Generate event sleep report.
    """
    def __init__(self, **kwargs):
        """ Initialize module EventSleepReport """
        super().__init__(**kwargs)
        if DEBUG: print('EventSleepReport.__init__')

        # Input plugs
        InputPlug('events',self)
        InputPlug('record_info',self)
        InputPlug('sleep_stages',self)
        InputPlug('events_report_criteria',self)
        InputPlug('nominal_values',self)
        InputPlug('report_constants',self)
        InputPlug('html_report',self)
        InputPlug('html_report_config',self)
        InputPlug('csv_report',self)
        InputPlug('save_events_report',self)
        InputPlug('output_prefix',self)
        InputPlug('output_directory',self)
        
        # Output plugs
        OutputPlug('report_events',self)        


    def compute(self, events, record_info, sleep_stages, events_report_criteria, nominal_values, \
        report_constants, html_report, html_report_config, csv_report, save_events_report, output_prefix, output_directory):
        """
        TODO DESCRIPTION

        Inputs:
            "events": Pandas Dataframe
                List of events.
            "record_info": dict
                Dictionary of information about the current recording.
            "sleep_stages" : Pandas Dataframe
                List of sleep stages and sleep cycles.
            "events_report_criteria": list[dict]
                List of event report to generate. Each element is a dictionary with
                all event's selection criteria used in the report.
                (one report per item that can be identified with its name)
            "nominal_values": TODO TYPE
                TODO DESCRIPTION
                (ne pas faire pour l'instant)
            "report_constants": dict
                Constants used in the report (N_HOURS, N_CYCLES)
            "html_report": bool
                Generate the HTML report if True.
            "html_report_config": TODO TYPE
                TODO DESCRIPTION
                (ne pas faire pour l'instant)
            "csv_report": bool
                Generate the CSV report if True.
            save_events_report : bool
                Save events report if true.
            "output_prefix": str
                The prefix of the report filename
            "output_directory": str
                The path to the output directory

        Outputs:
            "report_events": dict(str, Pandas DataFrame)
                DataFrame of events associated with the label of the report. The events
                are the one filtered by the report criteria.
                (events_report_criteria is no more usefull, report_events includes only event)
        """
        if not isinstance(events,pd.DataFrame):
            raise NodeInputException(self.identifier, "events", \
                f"EventSleepReport input of wrong type. Expected: <class 'pd.DataFrame'> received: {type(events)}")         

        if isinstance(report_constants,str) and report_constants == '':
            raise NodeInputException(self.identifier, "report_constants", \
                "SleepReport report_constants parameter must be set.")
        elif isinstance(report_constants,str):
            report_constants = eval(report_constants)
        if isinstance(report_constants,dict) == False:
            raise NodeInputException(self.identifier, "report_constants",\
                "SleepReport report_constants expected type is dict and received type is " + str(type(report_constants)))   

        # Re-order to process "respiratory events first"
        events_report_criteria = self.reorder_reports_for_respiratory(events_report_criteria)

        events_resp = pd.DataFrame(None,columns=['group','name','start_sec','duration_sec','channels'])
        report_events = {}
        for report in events_report_criteria:
            # File name of the current report
            report_name = report['name'].replace(" ", "_")
            report_filename = os.path.join(output_directory, f"{output_prefix}_{report_name}.tsv")
            report_label = self.report_to_string(report)

            info = []

            # Get recording identification
            subject_info_params, info = self.get_recording_id(record_info, info)

            # Get event class
            event_info_params, info = self.get_event_info(report, info)

            # Get report criteria   
            report_info_params, info = self.get_report_criteria(report, info)

            # Manage the events of the current report
            #   Select the group, name, channel is needed
            #   Filter out event outside sleep if event section is sleep only
            #   Filter out events linked to respiratory events
            #   Filter out too short or too long events
            #   Manage series
            filtered_events, n_events_filtered, n_evt_linked_to_resp_evt, events_resp = \
                self.filter_events_by_criteria(events, sleep_stages, report, events_resp)
            
            report_info = {
                "evt_asso_to_resp_count" : n_evt_linked_to_resp_evt, 
                "evt_excl_count" : n_events_filtered
            }
            info.append(["evt_asso_to_resp_count", "Results :  Number of events associated with respiratory events."])
            info.append(["evt_excl_count", "Results : Number of events excluded after criteria application."])            

            # Extract sleep stage (not cycles)
            sleep_stages_nocycle = sleep_stages[sleep_stages.group == commons.sleep_stages_group].copy()
            sleep_stages_nocycle.reset_index(inplace=True, drop=True)
            sleep_stages_nocycle.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')

            #-------------------------------------------------------------------
            # General Event stats : first result
            #-------------------------------------------------------------------
            report_info_results = self.compute_evt_stats_gen(report, filtered_events, sleep_stages_nocycle)
            info.append(["periods_delay_count", "Results : number of periods based on the end_period_delay criteria."])
            info.append(["evt_sleep_first_wake_count", \
                "Results : number of events in sleep or in the first awake epoch (preceding epoch must be sleep)."])
            info.append(["evt_sleep_first_wake_index", \
                "Results : event index (number of events/hour) in sleep or first awake epoch "+\
                    "(evt_sleep_first_wake_count/hours of sleep stage)."])
            info.append(["evt_asso_arousal_count", \
                "Results : number of events associated with an arousal i.e. "+\
                    "The event occurs in sleep but the next epoch is awake or "+\
                        "the event occurs in awake but the preceding epoch is sleep."])
            info.append(["asleep_percent", "Results: '%' of time slept occupied by the event" ])
            if report['events_section'] == "Recording time":
                info.append(["record_percent", "Results: '%' of recording "+\
                    "(from first epoch scored to last epoch scored) occupied by the event" ])
            else:
                info.append(["record_percent", "Results: '%' of recording "+\
                    "(from sleep onset to last asleep stage) occupied by the event" ])                

            #-------------------------------------------------------------------
            # Event stats based on a portion of the night
            #-------------------------------------------------------------------
            #   n_evt : number of events
            #   evt_dur_avg : average duration of the events (s)
            #   n_evt_interval : number of intervals
            #   evt_interval_avg_sec : average interval (s)
            #   evt_index : number of events per hour
            
            # Get stats for each thirds
            div_label = 'third'
            n_divisions = 3
            stats_third = self.compute_evt_stats_division(\
                n_divisions, div_label, filtered_events, sleep_stages_nocycle, report)
            for i_info in range(n_divisions):
                info.append([div_label+"{}_evt_count".format(i_info+1), div_label+\
                    " {} : number of events".format(i_info+1)])
                info.append([div_label+"{}_evt_avg_sec".format(i_info+1), div_label+\
                    " {} : average duration of the events (s)".format(i_info+1)])
                info.append([div_label+"{}_evt_interval_count".format(i_info+1), div_label+\
                    " {} : number of intervals".format(i_info+1)])
                info.append([div_label+"{}_evt_interval_avg_sec".format(i_info+1), div_label+\
                    " {} : average interval (s)".format(i_info+1)])
                if report['events_section'] == "Sleep only":    
                    info.append([div_label+"{}_evt_index".format(i_info+1), div_label+\
                        " {} : number of events per hour in asleep stage".format(i_info+1)])   
                elif report['events_section'] == "Awake in sleep period":
                    info.append([div_label+"{}_evt_index".format(i_info+1), div_label+\
                        " {} : number of events per hour in wake stage".format(i_info+1)]) 
                else:
                    info.append([div_label+"{}_evt_index".format(i_info+1), div_label+\
                        " {} : number of events per hour".format(i_info+1)])                                                      

            # Get stats for each halves
            n_divisions = 2
            div_label = 'half'
            stats_half = self.compute_evt_stats_division(\
                n_divisions, div_label, filtered_events, sleep_stages_nocycle, report)   
            for i_info in range(n_divisions):
                info.append([div_label+"{}_evt_count".format(i_info+1), div_label+\
                    " {} : number of events".format(i_info+1)])
                info.append([div_label+"{}_evt_avg_sec".format(i_info+1), div_label+\
                    " {} : average duration of the events (s)".format(i_info+1)])
                info.append([div_label+"{}_evt_interval_count".format(i_info+1), div_label+\
                    " {} : number of intervals".format(i_info+1)])
                info.append([div_label+"{}_evt_interval_avg_sec".format(i_info+1), div_label+\
                    " {} : average interval (s)".format(i_info+1)])
                if report['events_section'] == "Sleep only":
                    info.append([div_label+"{}_evt_index".format(i_info+1), div_label+\
                        " {} : number of events per hour in asleep stage".format(i_info+1)]) 
                elif report['events_section'] == "Awake in sleep period":
                    info.append([div_label+"{}_evt_index".format(i_info+1), div_label+\
                        " {} : number of events per hour in wake stage".format(i_info+1)]) 
                else:
                    info.append([div_label+"{}_evt_index".format(i_info+1), div_label+\
                        " {} : number of events per hour".format(i_info+1)])  

            # Get stats for total
            n_divisions = 1
            div_label = 'total'
            stats_tot = self.compute_evt_stats_division(\
                n_divisions, div_label, filtered_events, sleep_stages_nocycle, report) 
            info.append(["total_evt_count", "Total : number of events"])
            info.append(["total_evt_avg_sec", "Total : average duration of the events (s)"])
            info.append(["total_evt_interval_count", "Total : number of intervals"])
            info.append(["total_evt_interval_avg_sec", "Total : average interval (s)"])
            if report['events_section'] == "Sleep only":
                info.append(["total_evt_index", "Total : number of events per hour in asleep stage"])  
            elif report['events_section'] == "Awake in sleep period":
                info.append(["total_evt_index", "Total : number of events per hour in wake stage"])  
            else:
                info.append(["total_evt_index", "Total : number of events per hour"])  

            # Get stats all stages
            # List of every stage to compute with its label
            sleep_stage_to_stats = [
                ['0'], ['1'], ['2'], ['3'], ['1', '2', '3'], ['5'], ['9','8']
                ]
            stage_stats_label = [ 'W', 'N1', 'N2', 'N3', 'NREM', 'R', 'Unscored']
            stats_stage, stats_info_stage = self.compute_evt_stats_stage(\
                sleep_stage_to_stats, stage_stats_label, filtered_events, sleep_stages_nocycle, report)
            info = info + stats_info_stage

            # Get stats for each cycles
            stats_cycles, stats_info_cycle = self.compute_evt_stats_cycle(\
                int(report_constants['N_CYCLES']), filtered_events, sleep_stages, report)
            info = info + stats_info_cycle

            if isinstance(save_events_report, str):
                try : 
                    save_events_report = eval(save_events_report)
                except : 
                    raise NodeInputException(self.identifier, "save_events_report", \
                        "EventSleepReport save_events_report parameter must be set.")                
            if type(save_events_report) != bool:
                raise NodeInputException(self.identifier, "save_events_report", \
                    "EventSleepReport save_events_report parameter must be set.")

            if save_events_report:
                HH_series = (np.floor(filtered_events.start_sec/3600)).astype(int)
                MM_series = ( np.floor( (filtered_events.start_sec-HH_series*3600) / 60 )).astype(int)
                SS_series = np.around( (filtered_events.start_sec-HH_series*3600 \
                    - MM_series*60).astype(np.double),decimals=2,out=None)
                filtered_events['time_elapsed(HH:MM:SS)'] = HH_series.astype("string")\
                                + ':' + MM_series.astype("string") + ':' + SS_series.astype("string")
                filtered_events['epoch_num'] = np.floor((filtered_events.start_sec-sleep_stages_nocycle.start_sec.values[0])\
                    /np.round(sleep_stages_nocycle.duration_sec.values[0]))

            report_events[report_label] = filtered_events

            if isinstance(csv_report, str):
                try : 
                    csv_report = eval(csv_report)
                except : 
                    raise NodeInputException(self.identifier, "csv_report", \
                        "EventSleepReport csv_report parameter must be set.")                
            if type(csv_report) != bool:
                raise NodeInputException(self.identifier, "csv_report", \
                    "EventSleepReport csv_report parameter must be set.")

            if csv_report:
                # Each line is an additional subject
                # Construction of the pandas dataframe that will be used to create the CSV file
                output = subject_info_params | event_info_params | report_info_params\
                     | report_info | report_info_results | stats_third | stats_half | stats_tot |\
                         stats_stage | stats_cycles
                report_df = pd.DataFrame.from_records([output])
                # Write the current report for the current subject into the tsv file
                write_header = not os.path.exists(report_filename)
                try :
                    report_df.to_csv(path_or_buf=report_filename, sep='\t', \
                        index=False, mode='a', header=write_header, encoding="utf_8")
                except :
                    error_message = f"Snooz can not write in the file {report_filename}."+\
                        f" Check if the drive is accessible and ensure the file is not already open."
                    raise NodeRuntimeException(self.identifier, "EventSleepReport", error_message)
                # To write the info text file to describe yhe variable names
                if write_header:
                    info_df = pd.DataFrame(None, columns=['name', 'description'])
                    info_df = pd.concat([info_df, pd.DataFrame(info, columns=['name', 'description'])])
                    report_info_filename = os.path.join(output_directory, f"{output_prefix}_{report_name}_info.tsv")
                    try : 
                        info_df.to_csv(path_or_buf=report_info_filename, \
                            sep='\t', index=False, mode='w', header=write_header, encoding="utf_8")
                    except :
                        error_message = f"Snooz can not write in the file {report_info_filename}."+\
                            f" Check if the drive is accessible and ensure the file is not already open."
                        raise NodeRuntimeException(self.identifier, "EventSleepReport", error_message)
                if save_events_report:
                    # Output the events list for each report
                    events_report_filename = os.path.join(output_directory, f"{record_info['filename']}_{output_prefix}_EVENTS_{report_name}.tsv")
                    try : 
                        report_events[report_label].to_csv(path_or_buf=events_report_filename, \
                            sep='\t', index=True, mode='w', header=True, encoding="utf_8")
                    except :
                        error_message = f"Snooz can not write in the file {events_report_filename}."+\
                            f" Check if the drive is accessible and ensure the file is not already open."
                        raise NodeRuntimeException(self.identifier, "EventSleepReport", error_message)                    

        return {
            'report_events': report_events
        }


    def strip_accents(self, str_input):
        return ''.join(c for c in unicodedata.normalize('NFD', str_input)
                    if unicodedata.category(c) != 'Mn')


    # Function to filter events based on the report criterias.
    # Function returns the events filtered and the number of events excluded 
    def filter_events_by_criteria(self, events, sleep_stages, report, events_resp):
        """
        Function to filter events based on the report criterias.

        Parameters
        -----------
            events      : Pandas DataFrame
                Events to filter ('group','name','start_sec','duration_sec','channels')
            sleep_stages : Pandas DataFrame
                Sleep stages from the whole recording ('group','name','start_sec','duration_sec','channels')
            report : dict
                Report criteria (for the current report)
                    "name": report name
                    "min_duration": minimum duration of the event
                    "max_duration": max duration of the event
                    "min_interval": min interval between events to create a serie
                    "max_interval": max interval between events to create a serie
                    "min_count": min event count to make valid a serie
                    "end_period_delay": delay to end a period of events
                    "sleep_event_association_min": minimum interval to considered a respiratory events (i.e. -3.5 s)
                    "sleep_event_association_max": maximum interval to considered a respiratory events (i.e. 8 s)
                    "events_section": i.e. Sleep only, Recording time, Awake in sleep period, Before sleep onset
                    "graphics": None for now
            events_resp : Pandas DataFrame
                Respiratory events ('group','name','start_sec','duration_sec','channels')
            
        Returns
        -----------    
            events : Pandas DataFrame
                Selected events ('group','name','start_sec','duration_sec','channels')
            n_events_filtered : int
                Number of events filtered out.
            n_evt_linked_to_resp_evt : int
                Number of events associated with respiratory events.
            events_resp : Pandas DataFrame
                Respiratory events ('group','name','start_sec','duration_sec','channels')
        """
        loc_events = events.copy()

        index_to_sel = []
        for event_def in report['events_definition']:
            cur_index = loc_events[ (loc_events.group == event_def['group_name']) & (loc_events.name == event_def['event_name']) ].index.to_list()
            index_to_sel.append(cur_index)
        index_flat = [item for sublist in index_to_sel for item in sublist]
        index_unique = np.unique(np.array(index_flat))

        loc_events = loc_events.iloc[index_unique]
        n_events_ori = len(index_unique)

        #------------------------------
        # Remove events occuring outside event section and sleep stage
        #------------------------------
        # Extract sleep stage (not cycles)
        sleep_stages_nocycle = sleep_stages[sleep_stages.group == commons.sleep_stages_group].copy()
        sleep_stages_nocycle.reset_index(inplace=True, drop=True)
        sleep_stages_nocycle.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')         
        # Asleep stages
        sleep_epoch = sleep_stages_nocycle[sleep_stages_nocycle['name'].isin(commons.asleep_stages)]
        sleep_latency_i = sleep_epoch.index[0]
        last_sleep_i = sleep_epoch.index[-1]
        # Valid stages
        valid_epoch = sleep_stages_nocycle[sleep_stages_nocycle['name'].isin(commons.valid_stage)]
        valid_start_i = valid_epoch.index[0]
        last_valid_i = valid_epoch.index[-1]
        # Select the portion of the recording
        if report['events_section'] == "Sleep only":
            # Extract first to the last asleep epoch
            recording_stages = sleep_stages_nocycle.iloc[sleep_latency_i:last_sleep_i+1].copy()
        elif report['events_section'] == "Awake in sleep period":
            # Extract first to the last asleep epoch
            recording_stages = sleep_stages_nocycle.iloc[sleep_latency_i:last_sleep_i+1].copy()
        elif report['events_section'] == "Before sleep onset":
            # Extract the valid stages before sleep onset
            recording_stages = sleep_stages_nocycle.iloc[valid_start_i:sleep_latency_i].copy()
        else:
            # Extract the valid stages during the whole recording
            recording_stages = sleep_stages_nocycle.iloc[valid_start_i:last_valid_i+1].copy()
        recording_stages.reset_index(inplace=True, drop=True)
        recording_stages.sort_values('start_sec', axis=0, inplace=True, ignore_index='True') 

        idx_2_rm = []
        for i_evt, evt in loc_events.iterrows():
            # find the stage of the current event
            idx_start = recording_stages[recording_stages.start_sec<=(evt.start_sec+evt.duration_sec)].index
            idx_stop = recording_stages[ (recording_stages.start_sec+recording_stages.duration_sec) > evt.start_sec].index
            idx_select_stage = idx_start.intersection(idx_stop)
            if len(idx_select_stage) >0 :
                if report['events_section'] == "Sleep only":
                    if not (recording_stages.loc[idx_select_stage[0]]['name'] in commons.asleep_stages):
                        idx_2_rm.append(i_evt)
                elif report['events_section'] == "Awake in sleep period":
                    if not (recording_stages.loc[idx_select_stage[0]]['name'] == '0'):
                        idx_2_rm.append(i_evt)
            else:
                idx_2_rm.append(i_evt)
        # Drop event not included in sleep only
        loc_events = loc_events.drop(idx_2_rm)

        # Respiratory events are important to compute "Number of events linked to respiratory events".
        if report['name'] == "Respiratory Events Report":
            events_resp = pd.concat([events_resp, loc_events])
            # We dont look at index there is problem with the list of channel
            events_resp.drop_duplicates(subset = ["group", "name", "start_sec", "duration_sec"], inplace=True)

        #------------------------------
        # Filter out events linked to respiratory events
        #------------------------------
        idx_2_rm = []
        n_evt_linked_to_resp_evt = 0
        if (report['sleep_event_association_min']!=0) or (report['sleep_event_association_max']!=0):
            if len(events_resp)>0 :
                for i_evt, evt in loc_events.iterrows():
                    interval = evt.start_sec-(events_resp.start_sec+events_resp.duration_sec)
                    #interval = (events_resp.start_sec+events_resp.duration_sec)-evt.start_sec
                    min_criteria = interval>report['sleep_event_association_min']
                    max_criteria = interval<report['sleep_event_association_max']
                    # If at least 1 respiratory event occurs during the interval
                    # exclude the current event
                    if any( min_criteria & max_criteria):
                        n_evt_linked_to_resp_evt = n_evt_linked_to_resp_evt + 1
                        idx_2_rm.append(i_evt)
            else :
                n_evt_linked_to_resp_evt = None
        else:
            n_evt_linked_to_resp_evt = None
        loc_events = loc_events.drop(idx_2_rm)
        
        # AppliqueCriteres in the previous software
        #------------------------------
        # Filter events based on their duration
        #------------------------------
        if report['min_duration'] != 0:
            loc_events = loc_events[loc_events.duration_sec >= report['min_duration']]
        if report['max_duration'] != 0:
            loc_events = loc_events[loc_events.duration_sec <= report['max_duration']]

        #------------------------------
        # Manage series of events
        #------------------------------
        # Reset index
        loc_events.reset_index(inplace=True, drop=True)
        # Sort events based on the start_sec
        loc_events.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')  
        if report['max_interval']>0 or report['min_interval']>0:
            if report['min_count']==0:
                report['min_count']=2 # TODO to confirm in a meeting
            idx_2_rm = []
            if len(loc_events)>0:
                start_sec_serie = loc_events.start_sec.values[0]
                prev_cur_start = start_sec_serie
                n_evt_in_serie = 1
                for i_evt, evt in loc_events.iterrows():
                    if i_evt>0:
                        # evaluate the interval
                        evt_interval = evt.start_sec - prev_cur_start
                        # If the interval is longer it ends the serie
                        if evt_interval>report['max_interval']:
                            # If the minimum number of events is not reached
                            if n_evt_in_serie<report['min_count']:
                                # Eliminate events in the current serie
                                idx_start = loc_events[loc_events.start_sec>=start_sec_serie].index
                                # We dont want to exclude the current evet, it is the start of the new serie
                                idx_stop = loc_events[loc_events.start_sec<evt.start_sec].index
                                idx_serie_lst = idx_start.intersection(idx_stop).to_list()
                                idx_2_rm.append(idx_serie_lst)
                            # Start over the current serie
                            n_evt_in_serie = 1
                            start_sec_serie = evt.start_sec
                            prev_cur_start = evt.start_sec
                        else:
                            # If the interval is too short, eliminate the current event
                            if evt_interval<report['min_interval']:
                                idx_2_rm.append([i_evt])
                                # here the start_sec_serie and prev_cur_start stay the same
                            # If the serie continues
                            else:
                                # update the current position
                                prev_cur_start = evt.start_sec
                                n_evt_in_serie += 1
                # Evaluate if the last serie includes enough events
                if n_evt_in_serie<report['min_count']:
                    # Eliminate events in the current serie
                    idx_start = loc_events[loc_events.start_sec>=start_sec_serie].index
                    # We want to eliminate the current event.  It is the last of a serie.
                    idx_stop = loc_events[loc_events.start_sec<=evt.start_sec].index
                    idx_serie = idx_start.intersection(idx_stop)
                    idx_2_rm.append(idx_serie.to_list())

                flat_list_idx = [item for sublist in idx_2_rm for item in sublist]
                loc_events = loc_events.drop(flat_list_idx)
               
        # Reset index
        loc_events.reset_index(inplace=True, drop=True)
        # Sort events based on the start_sec
        loc_events.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')  

        # Compute the total number of events filtered out
        n_events_filtered = n_events_ori-len(loc_events) 

        return loc_events, n_events_filtered, n_evt_linked_to_resp_evt, events_resp


    def get_event_info(self, report, info):
        event_info_params = {
            "event_class": None,   
            "event_group": report['group_name'],
            "event_name" : report['event_name']
        }
        info.append(["event_class", "The class of the events for the report"])
        info.append(["event_group", "The group of the events for the report"])
        info.append(["event_name", "The name of the events for the report"])
        return event_info_params, info


    def get_recording_id(self, record_info, info):
        # Convert seconds to date text
        if record_info["creation_date"] is not None:
            creation_datetime = datetime(1970, 1, 1) + timedelta(seconds=record_info["creation_date"])
            creation_date_text =  creation_datetime.strftime("%Y-%m-%d")
        else:
            creation_date_text = ""    

        if record_info["birthdate"] is not None:
            birthdate_datetime = datetime(1970, 1, 1) + timedelta(seconds=record_info["birthdate"])
            birthdate_text = birthdate_datetime.strftime("%Y-%m-%d")
        else:
            birthdate_text = ""
        

        subject_info_params = {
            "filename":record_info["filename"],
            "group":None,
            "sex":record_info['sex'],
            "birthdate":birthdate_text,
            "creation_date":creation_date_text,
            "age": record_info['age'] if record_info['age'] != None and record_info['age'] >= 0 else None,
            "height":record_info['height'] if record_info['height'] != None and record_info['height'] > 0 else None,
            "weight":record_info['weight'] if record_info['weight'] != None and record_info['weight'] > 0 else None,
            "bmi":record_info['bmi'] if record_info['bmi'] != None and record_info['bmi'] > 0 else None,
            "waistline":record_info['waistline'] if record_info['waistline'] != None and record_info['waistline'] > 0 else None
        }
        info.append(["filename", "PSG filename"])
        info.append(["group", "Subject Group"])
        info.append(["sex", "Subject Sex"])
        info.append(["birthdate", "The birthdate of the subject, yyyy-mm-dd"])
        info.append(["creation_date", "The creation date of the analysed file, yyyy-mm-dd"])
        info.append(["age", "Subject age at the recording date"])
        info.append(["height", "Subject height"])
        info.append(["weight", "Subject weight"])
        info.append(["bmi", "Subject BMI"])
        info.append(["waistline", "Subject Waistlist size"])
        return subject_info_params, info


    def get_report_criteria(self, report, info):
        report_info_params = {
            "crit_evt_section" : report['events_section'],
            "crit_evt_min_sec" : report['min_duration'],
            "crit_evt_max_sec" : report['max_duration'],
            "crit_evt_min_interval_sec" : report['min_interval'],
            "crit_evt_max_interval_sec" : report['max_interval'],
            "crit_evt_min_count_series" : report['min_count'],
            "crit_excl_min_interval_resp_sec" : report['sleep_event_association_min'], 
            "crit_excl_max_interval_resp_sec" : report['sleep_event_association_max'],
            "crit_end_period_delay_min" : report['end_period_delay'] # Not exactly at the same position than the previous software
        }
        info.append(["crit_evt_section", \
            "Report Event Criteria : event selection (Sleep only, recording time, Awake in sleep period, Before sleep onset)"])
        info.append(["crit_evt_min_sec", "Report Event Criteria : minimum event duration (s). i.e. 0.5"])
        info.append(["crit_evt_max_sec", "Report Event Criteria : maximum event duration (s). i.e. 10"])
        info.append(["crit_evt_min_interval_sec", "Report Event Criteria : minimum interval (s) to create a series. i.e. 5"])
        info.append(["crit_evt_max_interval_sec", "Report Event Criteria :  maximum interval (s) to create a series. i.e. 90"])
        info.append(["crit_evt_min_count_series", "Report Event Criteria : minimum number of events into a series. i.e. 4"])
        info.append(["crit_excl_min_interval_resp_sec", "Report Event Criteria : "+\
            "exclude event that starts during the minimum interval (s) with a respiratory event end. i.e. -3.5"])
        info.append(["crit_excl_max_interval_resp_sec", \
            "Report Event Criteria : exclude event that starts during the maximum interval (s) with a respiratory event end. i.e. 8"])
        # Not exactly at the same position than the previous software
        info.append(["crit_end_period_delay_min", "Report Event Criteria : Delay (min) without events to end a period. i.e. 15"])
        return report_info_params, info


    def report_to_string(self, report):
        if report['event_name'] is not None:
            return f"{report['name']}:{report['group_name']}:{report['event_name']}"
        elif report['group_name'] is not None:
            return f"{report['name']}:{report['group_name']}"
        else:
            return None


    def reorder_reports_for_respiratory(self, events_report_criteria):
        # Re-order the report list to process "respiratory events first"
        # in order to accumulate all the respiratory events into a master list
        # (the same respiratory event cannot be added twice in the master list)
        # to compute events asssociated with respiratory events
        # also usefull for the temporal links
        resp_report_list_idx = []
        for i, report in enumerate(events_report_criteria):
            if report['name']=="Respiratory Events Report":
                resp_report_list_idx.append(i)
        n_reports = len(events_report_criteria)
        other_report_list = set(range(n_reports)).symmetric_difference(resp_report_list_idx)
        resp_report_list_idx = resp_report_list_idx + list(other_report_list)
        events_report_criteria = [events_report_criteria[i] for i in resp_report_list_idx]
        return events_report_criteria


    # Not used anymore
    # This function changes the length of the event is a part of of is outside the selected sleep stage
    def select_events_from_stages(self, selected_sleep_stage, events_selected):
        # Find out if the event occur during a selected sleep stages
        local_fs = 10
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
                valid_event_df = pd.DataFrame(data=None,columns=\
                    ['group','name','start_sec','duration_sec','channels'])
                for valid_event_start, valid_event_dur in valid_event_lst:
                    current_event = pd.DataFrame(data=None,columns=\
                        ['group','name','start_sec','duration_sec','channels'])
                    current_event.at[0,'group'] = event["group"]
                    current_event.at[0,'name'] = event["name"]
                    current_event.at[0,'start_sec'] = valid_event_start+event["start_sec"]
                    current_event.at[0,'duration_sec'] = valid_event_dur
                    current_event.at[0,'channels'] = event["channels"]
                    valid_event_df = pd.concat([valid_event_df,current_event],ignore_index=True)
                events_filtered = pd.concat([events_filtered,valid_event_df],ignore_index=True)     
        return events_filtered


    def compute_evt_stats_division(self, n_divisions, label_division, filtered_events, sleep_stages_nocycle, report):
        """
            Compute the event stats based on a portion of the night.

            Inputs:
                n_divisions : int
                    number of division (2 for half).
                label_division : string
                    string to label the division (i.e. n_divisions=2, label_division=half)
                filtered_events : pandas DataFrame
                    Events to compute the stats on.
                sleep_stages_nocycle : pandas DataFrame
                    Sleep stages (continuous) the whole recording (including unscored 9)
                report : dict
                    Report criteria (for the current report)
                        "name": report name
                        "min_duration": minimum duration of the event
                        "max_duration": max duration of the event
                        "min_interval": min interval between events to create a serie
                        "max_interval": max interval between events to create a serie
                        "min_count": min event count to make valid a serie
                        "end_period_delay": delay to end a period of events
                        "sleep_event_association_min": minimum interval to considered a respiratory events (i.e. -3.5 s)
                        "sleep_event_association_max": maximum interval to considered a respiratory events (i.e. 8 s)
                        "events_section": i.e. Sleep Only, Recording time, Awake in sleep period, Before sleep onset
                        "graphics": None for now
                    
            Outputs:
                stats_division : dict
                    n_evt : number of events
                    evt_dur_avg : average duration of the events (s)
                    n_evt_interval : number of intervals
                    evt_interval_avg_sec : average interval (s)
                    evt_index : number of events per sleeping hour
                    i.e. third1_n_evt, third2_n_evt, third3_n_evt ...
        """

        # Asleep stages
        sleep_epoch = sleep_stages_nocycle[sleep_stages_nocycle['name'].isin(commons.asleep_stages)]
        sleep_latency_i = sleep_epoch.index[0]
        last_sleep_i = sleep_epoch.index[-1]
        # Valid stages
        valid_epoch = sleep_stages_nocycle[sleep_stages_nocycle['name'].isin(commons.valid_stage)]
        valid_start_i = valid_epoch.index[0]
        last_valid_i = valid_epoch.index[-1] 
        # Select the portion of the recording, index (label) selection with .loc is inclusive (even the end)
        if report['events_section'] == "Sleep only":
            # Extract first to the last asleep epoch
            recording_stages = sleep_stages_nocycle.loc[sleep_latency_i:last_sleep_i]
        elif report['events_section'] == "Awake in sleep period":
            # Extract first to the last asleep epoch
            recording_stages = sleep_stages_nocycle.loc[sleep_latency_i:last_sleep_i]
        elif report['events_section'] == "Before sleep onset":
            # Extract the valid stages before sleep onset
            recording_stages = sleep_stages_nocycle.loc[valid_start_i:sleep_latency_i-1]
        else:
            # Extract the valid stages during the whole recording
            recording_stages = sleep_stages_nocycle.loc[valid_start_i:last_valid_i]

        # How many epochs in each subdivision
        n_epochs = len(recording_stages)
        # For dividing a number into (almost) equal whole numbers
        # Remainers are added in the first division first
            # 15 epochs divided by 3 => [5, 5, 5]
            # 14 epochs divided by 3 => [5, 5, 4]
            # 13 epochs divided by 3 => [5, 4, 4]
            # 12 epochs divided by 3 => [4, 4, 4]
        n_epoch_div = [n_epochs // n_divisions + (1 if x < n_epochs % n_divisions else 0)  for x in range (n_divisions)]
        # Create a list of indexes to select the epochs in each division
        # Select the portion of the recording, row integer (NOT label), the end point is excluded with the .iloc
        index_div = []
        index_tmp = 0
        for div in range(n_divisions):
            cur_start = index_tmp
            cur_stop = cur_start+n_epoch_div[div]
            index_div.append([cur_start,cur_stop]) # integer index then last is exclusive
            index_tmp = cur_stop
        if DEBUG:
            print(f"{report['name']} {n_epochs} epochs in {n_divisions} divisions is {n_epoch_div}")

        # Create list of dataframe (each item is a division)
        stages_divided_lst = []
        for div_i in index_div:
            stages_divided_lst.append(recording_stages.iloc[div_i[0]:div_i[1]]) # integer row access, the last point is exclusive
            if DEBUG:
                start_sec_epoch = np.round(recording_stages.iloc[div_i[0]].start_sec,1)
                start_sec_stage = sleep_stages_nocycle["start_sec"].round(1)
                epoch_i_start = start_sec_stage[start_sec_stage==start_sec_epoch].index[0]
                stop_sec_epoch = np.round(recording_stages.iloc[div_i[1]-1].start_sec,1) # inclusive since it is only one value
                epoch_i_stop = start_sec_stage[start_sec_stage==stop_sec_epoch].index[0] # Still inclusive
                # The output events file start the epoch num at the first epoch scored (not 9)             
                print(f"{report['name']} division {div_i} from the first epoch {epoch_i_start} to the last asleep epoch {epoch_i_stop} inclusive")

        # Filter events based on the selected portion and compute stats
        stats_division = {}
        n_evt_interval = 0
        first_evt = False
        for div, cur_stages in enumerate(stages_divided_lst):
            start_time = cur_stages.start_sec.values[0]
            end_time = cur_stages.start_sec.values[-1]+cur_stages.duration_sec.values[-1] # inclusive since the previous iloc excluded the div_i[1]
            # Select event included in the epoch selection
            idx_start = filtered_events[filtered_events.start_sec >= start_time].index
            idx_stop = filtered_events[filtered_events.start_sec <= end_time].index
            idx_select_evt = idx_start.intersection(idx_stop)
            cur_evt_df = filtered_events.loc[idx_select_evt] # all inclusive
            # Add DEBUG info
            if label_division not in filtered_events:
                filtered_events[label_division] =  ""
            filtered_events.loc[idx_select_evt, label_division] = str(div+1)

            # # Drop events that start outside the epoch selection
            # idx_start = filtered_events[filtered_events.start_sec < start_time].index.to_list()
            # idx_stop = filtered_events[filtered_events.start_sec > end_time].index.to_list()
            # cur_evt_df = filtered_events.drop(idx_start+idx_stop)
            
            # Reset indexes
            cur_evt_df.reset_index(inplace=True, drop=True)
            cur_evt_df.sort_values('start_sec', axis=0, inplace=True, ignore_index='True') 
            if report['events_section'] == "Sleep only":
                selected_epoch = cur_stages[cur_stages['name'].isin(commons.asleep_stages)]
            elif report['events_section'] == "Awake in sleep period":
                selected_epoch = cur_stages[cur_stages['name']=='0']
            elif report['events_section'] == "Before sleep onset":
                selected_epoch = cur_stages
            else:
                selected_epoch = cur_stages

            # Compute the intervals, the first division : n_evt_interval=n_evt-1, the other division : n_evt_interval=n_evt
            for index, event in cur_evt_df.iterrows():
                if index>0:
                    if ((event.start_sec - start_int_sec) <= report['max_interval']) or report['max_interval']==0:
                        n_evt_interval = n_evt_interval + 1
                        dur_interval = dur_interval+(event.start_sec - start_int_sec)
                    start_int_sec = event.start_sec
                else:
                    if (div>0) and first_evt:
                        if ((event.start_sec - start_int_sec) <= report['max_interval']) or report['max_interval']==0:
                            n_evt_interval = 1
                            dur_interval = event.start_sec - start_int_sec
                        else:
                            n_evt_interval = 0
                            dur_interval = 0
                        start_int_sec = event.start_sec                        
                    else:
                        first_evt=True
                        n_evt_interval = 0
                        dur_interval = 0
                        start_int_sec = event.start_sec
            if len(cur_evt_df)==0:
                n_evt_interval = 0
                dur_interval = 0                

            if n_divisions>1:
                # To copy the previous software (because of the non integer fs)
                # duration_rec_div = selected_epoch['duration_sec'].sum()
                if len(selected_epoch)>0:
                    duration_rec_div = int(round(selected_epoch['duration_sec'].values[0]))*len(selected_epoch['duration_sec'])
                else:
                    duration_rec_div = 0
                stats_division[label_division+str(div+1)+'_evt_count'] = len(cur_evt_df)
                if len(cur_evt_df)>0:
                    stats_division[label_division+str(div+1)+'_evt_avg_sec'] = \
                        cur_evt_df['duration_sec'].sum()/len(cur_evt_df)
                    stats_division[label_division+str(div+1)+'_evt_interval_count'] = n_evt_interval
                    if n_evt_interval>0:
                        stats_division[label_division+str(div+1)+'_evt_interval_avg_sec'] \
                            = dur_interval/n_evt_interval
                    else:
                        stats_division[label_division+str(div+1)+'_evt_interval_avg_sec'] = None
                    if duration_rec_div>0:
                        stats_division[label_division+str(div+1)+'_evt_index'] = \
                            len(cur_evt_df)/(duration_rec_div/3600)
                    else:
                        stats_division[label_division+str(div+1)+'_evt_index'] = None
                else:
                    stats_division[label_division+str(div+1)+'_evt_avg_sec'] = None
                    stats_division[label_division+str(div+1)+'_evt_interval_count'] = 0
                    stats_division[label_division+str(div+1)+'_evt_interval_avg_sec'] = None
                    stats_division[label_division+str(div+1)+'_evt_index'] = None
            else:
                # To copy the previous software (because of the non-integer fs)
                # duration_rec_div = selected_epoch['duration_sec'].sum()
                if len(selected_epoch)>0:
                    duration_rec_div = int(round(selected_epoch['duration_sec'].values[0]))*len(selected_epoch['duration_sec'])
                else:
                    duration_rec_div = 0                
                stats_division[label_division+'_evt_count'] = len(cur_evt_df)
                if len(cur_evt_df)>0:
                    stats_division[label_division+'_evt_avg_sec'] = \
                        cur_evt_df['duration_sec'].sum()/len(cur_evt_df)
                else:
                    stats_division[label_division+'_evt_avg_sec'] = None
                stats_division[label_division+'_evt_interval_count'] = n_evt_interval
                if n_evt_interval>0:
                    stats_division[label_division+'_evt_interval_avg_sec'] = dur_interval/n_evt_interval
                else:
                    stats_division[label_division+'_evt_interval_avg_sec'] = None
                if duration_rec_div>0:
                    stats_division[label_division+'_evt_index'] = \
                        len(cur_evt_df)/(duration_rec_div/3600)
                else:
                    stats_division[label_division+'_evt_index'] = None

        return stats_division

    
    def compute_evt_stats_gen(self, report, filtered_events, sleep_stages_nocycle):
        """
            Compute the general event stats.

            Inputs:
                report : dict
                    Report criteria (for the current report)
                        "name": report name
                        "min_duration": minimum duration of the event
                        "max_duration": max duration of the event
                        "min_interval": min interval between events to create a serie
                        "max_interval": max interval between events to create a serie
                        "min_count": min event count to make valid a serie
                        "end_period_delay": delay to end a period of events
                        "sleep_event_association_min": minimum interval to considered a respiratory events (i.e. -3.5 s)
                        "sleep_event_association_max": maximum interval to considered a respiratory events (i.e. 8 s)
                        "events_section": i.e. Sleep only, Recording time, Awake in sleep period, Before sleep onset
                        "graphics": None for now
                filtered_events : pandas DataFrame
                    Events to compute the stats on.
                sleep_stages_nocycle : pandas DataFrame
                    Sleep stages (continuous) to know the lengh of the recording.
            Outputs:
                report_info_results : dict
                    "periods_delay_count", "Results : Number of periods based on the end_period_delay criteria."
                    "evt_sleep_first_wake_count", "Results : Number of events in sleep or in the first awake epoch (preceding epoch must be sleep)."
                    "evt_sleep_first_wake_index", "Results : Event index (number of events/hour) in sleep or first awake epoch."
                    "evt_asso_arousal_count", "Results : Number of events associated with an arousal 
                    "asleep_percent", "Results: '%' of time slept occupied by the event"
                    "record_percent", "Results: '%' of recording (from sleep onset to last asleep stage) occupied by the event"
        """
        # Accumulate stats for 
        n_evt_sleep_1wake = 0
        n_evt_arousal = 0
        evt_dur_asleep = 0
        cur_dur_period = 0

        epoch_dur = sleep_stages_nocycle["duration_sec"].values[0]
        # Asleep stages
        sleep_epoch = sleep_stages_nocycle[sleep_stages_nocycle['name'].isin(commons.asleep_stages)]
        # Extract first to the last asleep epoch
        sleep_latency_i = sleep_epoch.index[0]
        last_sleep_i = sleep_epoch.index[-1]
        # Valid stages
        valid_epoch = sleep_stages_nocycle[sleep_stages_nocycle['name'].isin(commons.valid_stage)]
        valid_start_i = valid_epoch.index[0]
        last_valid_i = valid_epoch.index[-1]        

        # Select the portion of the recording
        if report['events_section'] == "Sleep only":
            # Extract first to the last asleep epoch
            recording_stages = sleep_stages_nocycle.iloc[sleep_latency_i:last_sleep_i+1].copy()
        elif report['events_section'] == "Awake in sleep period":
            # Extract first to the last asleep epoch
            recording_stages = sleep_stages_nocycle.iloc[sleep_latency_i:last_sleep_i+1].copy()
        elif report['events_section'] == "Before sleep onset":
            # Extract the valid stages before sleep onset
            recording_stages = sleep_stages_nocycle.iloc[valid_start_i:sleep_latency_i].copy()
        else:
            # Extract the valid stages during the whole recording
            recording_stages = sleep_stages_nocycle.iloc[valid_start_i:last_valid_i+1].copy()

        dur_record = (len(recording_stages))*epoch_dur
        recording_stages.reset_index(inplace=True, drop=True)
        recording_stages.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')

        if len(filtered_events)>0:
            start_pos_period = filtered_events["start_sec"].values[0]+filtered_events["duration_sec"].values[0]
            n_periods = 1
        else:
            start_pos_period = 0
            n_periods = 0
        for i_evt, evt in filtered_events.iterrows():
            # Compute the current period duration
            cur_dur_period = (evt.start_sec+evt.duration_sec)-start_pos_period
            if (cur_dur_period >= (report['end_period_delay']*60)) and (report['end_period_delay']>0):
                n_periods = n_periods+1
            #print("{} to process...".format(i_evt))
            # find the stage of the current event
            idx_start = sleep_stages_nocycle[sleep_stages_nocycle.start_sec<=\
                (evt.start_sec+evt.duration_sec)].index
            idx_stop = sleep_stages_nocycle[sleep_stages_nocycle.start_sec\
                +sleep_stages_nocycle.duration_sec > evt.start_sec].index
            idx_select_stage = idx_start.intersection(idx_stop)
            if all(idx_select_stage != None):
                stage_list = sleep_stages_nocycle.loc[idx_select_stage]['name'].to_list()
                if len(idx_select_stage)>1:
                    if any(sleep_stages_nocycle.loc[idx_select_stage]['name']\
                        .isin(commons.asleep_stages).to_list()) and ('0' in stage_list):
                        if DEBUG:
                            print("{} #{} occurs during awake and sleep".format(evt['name'], i_evt))
                # if the event occurs during sleep stage
                if (stage_list[0] in ' '.join(commons.asleep_stages)):
                    n_evt_sleep_1wake = n_evt_sleep_1wake + 1
                    evt_dur_asleep = evt_dur_asleep + evt.duration_sec
                    if idx_select_stage[0]<(len(sleep_stages_nocycle)-1): # not the last sleep stage
                        # Check if the following is awake
                        if sleep_stages_nocycle.loc[idx_select_stage[0]+1]["name"]=='0': 
                            n_evt_arousal = n_evt_arousal + 1
                else:
                    # if not, the stage before is sleep time
                    if idx_select_stage[0]>0: # not the first sleep stage
                        #print("{} to process in awake...".format(i_evt))
                        if (sleep_stages_nocycle.loc[idx_select_stage[0]-1]["name"] in ' '.join(commons.asleep_stages)):
                            n_evt_sleep_1wake = n_evt_sleep_1wake+1
                            n_evt_arousal = n_evt_arousal + 1
            else:
                raise NodeRuntimeException(self.identifier, report['name'], \
                    f"The event {report['event_name']} is outside the sleep staging")    
            start_pos_period = evt.start_sec+evt.duration_sec
        
        # To copy the previous software
        # duration_asleep = sleep_epoch['duration_sec'].sum()
        if len(sleep_epoch)>0:
            duration_asleep = int(round(sleep_epoch['duration_sec'].values[0]))*len(sleep_epoch['duration_sec'])
        else:
            duration_asleep = 0        
        evt_dur_record = filtered_events['duration_sec'].sum()
        report_info_results = {
            "periods_delay_count" : n_periods, 
            "evt_sleep_first_wake_count" : n_evt_sleep_1wake,
            "evt_sleep_first_wake_index" : n_evt_sleep_1wake/(duration_asleep/3600),
            "evt_asso_arousal_count" : n_evt_arousal,
            "asleep_percent" : evt_dur_asleep/duration_asleep * 100,
            "record_percent" : evt_dur_record/dur_record * 100
        }
        return report_info_results


    def compute_evt_stats_stage(self, sleep_stage_to_stats, stage_stats_label, \
        filtered_events, sleep_stages_df, report):
        """
            Compute the event stats based on a sleep stage or a list of sleep stages.
            The intervals are computed between each consecutive events event 
            if they are not the selected sleep stage.

            Inputs:
                sleep_stage_to_stats : list
                    Each item is a list of sleep stages to compute the event stats
                stage_stats_label : list of string
                    Each item is a string to label the stats variable
                filtered_events : pandas DataFrame
                    Events to compute the stats on.
                sleep_stages_df : pandas DataFrame
                    Sleep stages (continuous) the whole recording (including unscored 9)
                report : dict
                    Report criteria (for the current report)
                        "name": report name
                        "min_duration": minimum duration of the event
                        "max_duration": max duration of the event
                        "min_interval": min interval between events to create a serie
                        "max_interval": max interval between events to create a serie
                        "min_count": min event count to make valid a serie
                        "end_period_delay": delay to end a period of events
                        "sleep_event_association_min": minimum interval to considered a respiratory events (i.e. -3.5 s)
                        "sleep_event_association_max": maximum interval to considered a respiratory events (i.e. 8 s)
                        "events_section": i.e. Sleep Only, Recording time, Awake in sleep period, Before sleep onset
                        "graphics": None for now
                    
            Outputs:
                stats_stages : dict
                    evt_count : number of events
                    evt_avg_sec : average duration of the events (s)
                    evt_interval_count : number of intervals
                    evt_interval_avg_sec : average interval (s)
                    evt_index : number of events per sleeping hour
                    i.e. s0_n_evt, s1_n_evt, nrem_n_evt ...
                stats_info : list [n_variable x 2]
                    each item is 0: variable name 1: description 
        """
        #----------------------------------------
        # Select the right event section    
        #----------------------------------------
        # Asleep stages
        sleep_epoch = sleep_stages_df[sleep_stages_df['name'].isin(commons.asleep_stages)]
        sleep_latency_i = sleep_epoch.index[0]
        last_sleep_i = sleep_epoch.index[-1]
        # Valid stages
        valid_epoch = sleep_stages_df[sleep_stages_df['name'].isin(commons.valid_stage)]
        valid_start_i = valid_epoch.index[0]
        last_valid_i = valid_epoch.index[-1]        
        # Select the portion of the recording
        if report['events_section'] == "Sleep only":
            # Extract first to the last asleep epoch
            recording_stages = sleep_stages_df.iloc[sleep_latency_i:last_sleep_i+1].copy()
        elif report['events_section'] == "Awake in sleep period":
            # Extract first to the last asleep epoch
            recording_stages = sleep_stages_df.iloc[sleep_latency_i:last_sleep_i+1].copy()
        elif report['events_section'] == "Before sleep onset":
            # Extract the valid stages before sleep onset
            recording_stages = sleep_stages_df.iloc[valid_start_i:sleep_latency_i].copy()
        else:
            # Extract the valid stages during the whole recording
            recording_stages = sleep_stages_df.iloc[valid_start_i:last_valid_i+1].copy()

        #----------------------------------------
        # For each event mark its sleep stage
        #----------------------------------------
        #event_stage_df = filtered_events.copy()
        stage_def = []
        for event_i, event in filtered_events.iterrows():
            # Find event.start_sec
            idx_start = recording_stages[recording_stages.start_sec <= event.start_sec].index
            idx_stop = recording_stages[(recording_stages.start_sec+recording_stages.duration_sec)\
                 > event.start_sec].index
            # idx_stop = recording_stages[(recording_stages.start_sec+round(recording_stages.duration_sec))\
            #      > event.start_sec].index
            idx_select_evt = idx_start.intersection(idx_stop)
            cur_evt_df = recording_stages.loc[idx_select_evt]
            if len(cur_evt_df)>0:
                stage_def.append(cur_evt_df['name'].values[0])
            else:
                # To overcome events between 2 epochs (because of Stellate non integer fs)
                # Compute the stage for the whole event (not only the start) and select the first part
                idx_start = recording_stages[recording_stages.start_sec<=\
                    (event.start_sec+event.duration_sec)].index
                idx_stop = recording_stages[recording_stages.start_sec\
                    +recording_stages.duration_sec > event.start_sec].index
                idx_select_stage = idx_start.intersection(idx_stop)
                if len(idx_select_stage)>0:
                    cur_evt_df = recording_stages.loc[idx_select_stage]
                    stage_def.append(cur_evt_df['name'].values[0])
                else:
                    stage_def.append(nan)
        filtered_events['stage'] = stage_def       
        filtered_events = filtered_events.sort_values(by=['start_sec'])
        filtered_events = filtered_events.reset_index(drop=True)

        #----------------------------------------
        # Compute the number of events, duration and interval
        #----------------------------------------         
        
        # Intervals
        n_evt_interval = np.zeros(len(sleep_stage_to_stats))
        dur_interval = np.zeros(len(sleep_stage_to_stats))
        for event_i, event in filtered_events.iterrows():
            if event_i>0:
                if ((event.start_sec - start_int_sec) <= report['max_interval']) or report['max_interval']==0:
                    for sel_i, sel_stage_lst in enumerate(sleep_stage_to_stats):
                        if event.stage in sel_stage_lst:
                            n_evt_interval[sel_i] = n_evt_interval[sel_i] + 1
                            dur_interval[sel_i] = dur_interval[sel_i]+(event.start_sec - start_int_sec)
                start_int_sec = event.start_sec
            else:
                start_int_sec = event.start_sec

        # Number of events, duration
        stats_stages = {}
        stats_info = []
        for sel_i, sel_stage_lst in enumerate(sleep_stage_to_stats):
            # Sleep stage selection
            sleep_stage_sel = recording_stages[recording_stages['name'].isin(sel_stage_lst)]
            if len(sleep_stage_sel)>0:
                # To copy the previous software, the non integer fs makes the total length not a multiple of the epoch length...
                # duration_rec_div = sleep_stage_sel['duration_sec'].sum() 
                duration_rec_div = int(round(sleep_stage_sel['duration_sec'].values[0]))*len(sleep_stage_sel)
            else:
                duration_rec_div = 0
            label_stages = stage_stats_label[sel_i]
            # Selection of the events
            evt_sel_df = filtered_events[filtered_events['stage'].isin(sel_stage_lst)]
            stats_stages[label_stages+'_evt_count'] = len(evt_sel_df)
            if len(evt_sel_df)>0:
                stats_stages[label_stages+'_evt_avg_sec'] = \
                    evt_sel_df['duration_sec'].sum()/len(evt_sel_df)
            else:
                stats_stages[label_stages+'_evt_avg_sec'] = None
            stats_stages[label_stages+'_evt_interval_count'] = n_evt_interval[sel_i]
            if n_evt_interval[sel_i]>0: 
                stats_stages[label_stages+'_evt_interval_avg_sec'] = \
                    dur_interval[sel_i]/n_evt_interval[sel_i]
            else:
                stats_stages[label_stages+'_evt_interval_avg_sec'] = None
            if duration_rec_div>0:
                stats_stages[label_stages+'_evt_index'] = \
                    len(evt_sel_df)/(duration_rec_div/3600)
            else:
                stats_stages[label_stages+'_evt_index'] = None
            # Dump description stats
            stats_info.append([label_stages+"_evt_count", label_stages+" : number of events"])
            stats_info.append([label_stages+"_evt_avg_sec", label_stages+" : average duration of the events (s)"])
            stats_info.append([label_stages+"_evt_interval_count", label_stages+" : number of intervals"])
            stats_info.append([label_stages+"_evt_interval_avg_sec", label_stages+" : average interval (s)"])

            stats_info.append([label_stages+"_evt_index", label_stages\
                +" : number of events per hour (epochs from stage"+str(sel_stage_lst)+')'])

        return stats_stages, stats_info


    def compute_evt_stats_cycle(self, n_cycles, filtered_events, sleep_stages_df, report):
        """
            Compute the event stats based on a sleep cycles.
            The intervals are computed between each consecutive events event 
            if they are not the selected sleep cycle.

            Inputs:
                n_cycles : int
                    Number of cycles to compute stats
                filtered_events : pandas DataFrame
                    Events to compute the stats on.
                sleep_stages_df : pandas DataFrame
                    Sleep stages (continuous) the whole recording (including unscored 9)
                report : dict
                    Report criteria (for the current report)
                        "name": report name
                        "min_duration": minimum duration of the event
                        "max_duration": max duration of the event
                        "min_interval": min interval between events to create a serie
                        "max_interval": max interval between events to create a serie
                        "min_count": min event count to make valid a serie
                        "end_period_delay": delay to end a period of events
                        "sleep_event_association_min": minimum interval to considered a respiratory events (i.e. -3.5 s)
                        "sleep_event_association_max": maximum interval to considered a respiratory events (i.e. 8 s)
                        "events_section": i.e. Sleep only, Recording time, Awake in sleep period, Before sleep onset
                        "graphics": None for now
                    
            Outputs:
                stats_cycles : dict
                    evt_count : number of events
                    evt_avg_sec : average duration of the events (s)
                    evt_interval_count : number of intervals
                    evt_interval_avg_sec : average interval (s)
                    evt_index : number of events per sleeping hour
                    i.e. cyc0_n_evt, cyc1_n_evt, cyc2_n_evt ...
                stats_info : list [n_variable x 2]
                    each item is 0: variable name 1: description 
        """
        #----------------------------------------
        # Split sleep cycles from sleep stages
        #----------------------------------------
        sleep_stages_cpy = sleep_stages_df.copy() # needed because we drop out the cycle info.

        sleep_cycle_df = sleep_stages_cpy[sleep_stages_cpy['group']==commons.sleep_cycle_group]
        sleep_cycle_df = sleep_cycle_df.sort_values(by=['start_sec'])
        sleep_cycle_df = sleep_cycle_df.reset_index(drop=True)
        n_cycles_rec = len(sleep_cycle_df)
        # Modify the name for the cycle number
        sleep_cycle_df = sleep_cycle_df.copy()
        for cycle_i, cycle_event in sleep_cycle_df.iterrows():
            sleep_cycle_df.loc[cycle_i,'name']=cycle_i

        # Sleep stages are usefull for the event section
        sleep_stages_cpy = sleep_stages_cpy[sleep_stages_cpy['group']==commons.sleep_stages_group]
        sleep_stages_cpy = sleep_stages_cpy.sort_values(by=['start_sec'])
        sleep_stages_cpy = sleep_stages_cpy.reset_index(drop=True)

        #----------------------------------------
        # For each event mark its sleep cycle
        #----------------------------------------
        #event_cycle_df = filtered_events.copy()
        cycle_def = []
        for event_i, event in filtered_events.iterrows():
            # Find in which cycle the onset is
            idx_start = sleep_cycle_df[sleep_cycle_df.start_sec <= event.start_sec].index
            idx_stop = sleep_cycle_df[(sleep_cycle_df.start_sec+sleep_cycle_df.duration_sec)\
                 > event.start_sec].index
            idx_select_evt = idx_start.intersection(idx_stop)
            if len(idx_select_evt)>0:
                cur_evt_df = sleep_cycle_df.loc[idx_select_evt[0]]
                cycle_def.append(cur_evt_df['name'])
            # If not included in a cycle but not before the first or after the last.
            elif (len(idx_stop)>0) and (len(idx_start)>0):
                # To match previous software
                # cycle_def.append(None)
                # TODO check if we keep this behavior
                cur_evt_df = sleep_cycle_df.loc[idx_stop[0]]
                cycle_def.append(cur_evt_df['name'])
            # before the first or after the last cycle
            else:
                cycle_def.append(None)
        filtered_events['cycle'] = cycle_def 
        filtered_events = filtered_events.sort_values(by=['start_sec'])
        filtered_events = filtered_events.reset_index(drop=True)

        #----------------------------------------
        # Compute the number of events, duration and interval
        #----------------------------------------         
        
        # Intervals
        n_evt_interval = np.zeros(n_cycles)
        dur_interval = np.zeros(n_cycles)
        for event_i, event in filtered_events.iterrows():
            if event_i>0:
                if ((event.start_sec - start_int_sec) <= report['max_interval'])\
                     or report['max_interval']==0:
                    for sel_i in range(n_cycles):
                        #cur_cycle = event['cycle']
                        # if not (cur_cycle==None):
                        #     cur_cycle = event['cycle'].values[0]
                        if event['cycle'] == sel_i:
                            n_evt_interval[sel_i] = n_evt_interval[sel_i] + 1
                            dur_interval[sel_i] = dur_interval[sel_i]+(event.start_sec - start_int_sec)
                start_int_sec = event.start_sec
            else:
                start_int_sec = event.start_sec

        # Number of events, duration
        stats_cycles = {}
        stats_info = []
        stats_cycles["cycles_count"] = n_cycles_rec
        stats_info.append(["cycles_count", "number of cycles"])        
        for sel_i in range(n_cycles):
            label_cycle_short = "cyc"+str(sel_i+1)
            label_cycle_long = "cycle "+str(sel_i+1)
            if report['events_section'] == "Before sleep onset":
                duration_rec_div = 0
            else:
                # Sleep cycle selection
                current_cycle_df = sleep_cycle_df[sleep_cycle_df['name']==sel_i] 
                if len(current_cycle_df)>0:
                    # To match the previous software because of the non integer fs
                    # duration_rec_div = current_cycle_df.duration_sec.values[0]
                    duration_rec_div = np.round(current_cycle_df.duration_sec.values[0])
                else:
                    duration_rec_div = 0
            
            # Selection of the events
            evt_sel_df = filtered_events[filtered_events.cycle==sel_i]
            stats_cycles[label_cycle_short+'_evt_count'] = len(evt_sel_df)
            if len(evt_sel_df)>0:
                stats_cycles[label_cycle_short+'_evt_avg_sec'] = \
                    evt_sel_df['duration_sec'].sum()/len(evt_sel_df)
            else:
                stats_cycles[label_cycle_short+'_evt_avg_sec'] = None
            stats_cycles[label_cycle_short+'_evt_interval_count'] = n_evt_interval[sel_i]
            if n_evt_interval[sel_i]>0: 
                stats_cycles[label_cycle_short+'_evt_interval_avg_sec'] = \
                    dur_interval[sel_i]/n_evt_interval[sel_i]
            else:
                stats_cycles[label_cycle_short+'_evt_interval_avg_sec'] = None
            if duration_rec_div>0:
                stats_cycles[label_cycle_short+'_evt_index'] = \
                    len(evt_sel_df)/(duration_rec_div/3600)
            else:
                stats_cycles[label_cycle_short+'_evt_index'] = None
            # Dump description stats
            stats_info.append([label_cycle_short+"_evt_count", label_cycle_long+\
                " : Number of events"])
            stats_info.append([label_cycle_short+"_evt_avg_sec",\
                label_cycle_long+" : average duration of the events (s)"])
            stats_info.append([label_cycle_short+"_evt_interval_count", \
                label_cycle_long+" : number of intervals"])
            stats_info.append([label_cycle_short+"_evt_interval_avg_sec", \
                label_cycle_long+" : average interval (s)"])
            stats_info.append([label_cycle_short+"_evt_index", \
                label_cycle_long+" : number of events per hour"])

        return stats_cycles, stats_info


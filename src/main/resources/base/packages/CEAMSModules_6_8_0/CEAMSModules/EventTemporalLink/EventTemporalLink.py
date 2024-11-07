"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    EventTemporalLink
    Generate temporal links listed in the input temporal_links.
"""
import numpy as np
import pandas as pd
import os

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

from ..EventSleepReport import EventSleepReport

DEBUG = False

class EventTemporalLink(SciNode):
    """
    Generate temporal links.

    Inputs:
        "record_info": dict
            Information about the current record
        "report_events": dict(str, Pandas DataFrame)
            DataFrame of events associated with the label of the report. The events
                are the one filtered/selected by the report criteria.
        "sleep_report" : pandas DataFrame
            DataFrame of the sleep report for the current subject.
        "window_size": float
            Window analysis size.
        "temporal_links": list[[bool, str, str]]
            List of temporal links report to generate. bool value can be ignored.
            The str values are associated to the list of events received in the 
            'report_events'. A temporal link report must be generate for each 
            pair of events.
        "html_report": bool
            Generate the html report or not
        "html_report_config": TODO TYPE
            TODO DESCRIPTION
        "csv_report": bool
            Generate the CSV report or not
        "output_prefix": str
            The prefix of the report filename
        "output_directory": str
            The path to the output directory
        
    Outputs:
        None
        
    """
    def __init__(self, **kwargs):
        """ Initialize module EventTemporalLink """
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')

        # Input plugs
        InputPlug('record_info',self)
        InputPlug('report_events',self)
        InputPlug('sleep_report',self)
        InputPlug('window_size',self)
        InputPlug('temporal_links',self)
        InputPlug('html_report',self)
        InputPlug('html_report_config',self)
        InputPlug('csv_report',self)
        InputPlug('output_prefix',self)
        InputPlug('output_directory',self)


    
    def compute(self, record_info, report_events, sleep_report, window_size, temporal_links, \
        html_report, html_report_config, csv_report, output_prefix, output_directory):
        """
        Generate temporal links.

        Inputs:
            "record_info": dict
                Information about the current record
            "report_events": dict(str, Pandas DataFrame)
                DataFrame of events associated with the label of the report. The events
                    are the one filtered/selected by the report criteria.
            "sleep_report" : pandas DataFrame
                DataFrame of the sleep report for the current subject.
            "window_size": float
                Window analysis size.
            "temporal_links": list[[bool, str, str]]
                List of temporal links report to generate. bool value can be ignored.
                The str values are associated to the list of events received in the 
                'report_events'. A temporal link report must be generate for each 
                pair of events.
            "html_report": bool
                Generate the html report or not
            "html_report_config": TODO TYPE
                TODO DESCRIPTION
            "csv_report": bool
                Generate the CSV report or not
            "output_prefix": str
                The prefix of the report filename
            "output_directory": str
                The path to the output directory

        Outputs:
            None
        """
        if temporal_links is None:
            return {}

        info = []

        if isinstance(csv_report, str):
            csv_report = eval(csv_report)
        if not isinstance(csv_report,bool):
            raise NodeInputException(self.identifier, "csv_report", \
                f"EventTemporalLink input of wrong type. Expected: str of bool received: {type(csv_report)}")

        # Get recording identification
        subject_info_params, info = EventSleepReport.get_recording_id(self, record_info, info)

        # Get criteria for temporal links
        criteria_temporal = {
            "window_length_sec" : window_size,
        }
        info.append(['window_length_sec','Windows length (s) used to compute the temporal link.'])

        # Get stats on temporal links
        for temporal_link in temporal_links:
            info_cur_report = []

            event_report_label_1 = EventSleepReport.report_to_string(self, temporal_link[1])
            event_report_label_2 = EventSleepReport.report_to_string(self, temporal_link[2])
            events1 = report_events[event_report_label_1]
            events2 = report_events[event_report_label_2]

            # Get event definition
            info_cur_report.append(['record_min','Duration of the recording (min) used to compute the temporal link index.'])
            
            event_info_params, info_cur_report = self.get_event_definition(\
                events1, events2, info_cur_report)

            if "recording time" in event_report_label_1 + event_report_label_2:
                record_len_min = sleep_report["record_min"].values[0]
            elif "before sleep onset" in event_report_label_1 + event_report_label_2:
                record_len_min = sleep_report["sleep_latency_used_in_this_report_min"].values[0]
            elif "Bruxism" in event_report_label_1 + event_report_label_2:
                record_len_min = sleep_report["record_min"].values[0]
            elif "wake in sleep period" in event_report_label_1 + event_report_label_2:
                record_len_min = record_len_min = sleep_report["total_wake_min"].values[0] - \
                    sleep_report["sleep_latency_used_in_this_report_min"].values[0]- \
                        sleep_report["last_wake_min"].values[0]
            else:
                record_len_min = sleep_report["total_sleep_min"].values[0]

            criteria_temporal_1 = {
                "record_min" : record_len_min
                }

            # Compute stats on temporal links with the 0.5 s windows
            #   event1 starts before the event 2 starts, 
            #   event1 ends before the event 2 starts
            #   event2 starts before the event 1 starts, 
            #   event2 ends before the event 1 starts            
            #       number, mean delay (s), index per hour", percentage of event linked,
            result_links_start, info_cur_report, i_evt1_linked, i_evt2_linked = \
                self.compute_stats_windows(events1, events2, float(window_size), \
                    record_len_min, info_cur_report)

            # Compute stats on overlap
            result_links_over, info_cur_report, i_evt1_ov, i_evt2_ov = \
                self.compute_stats_overlap( events1, events2, record_len_min, info_cur_report)

            # Compute stats on the total number of links
            i_evt1_unique = list(dict.fromkeys(i_evt1_linked+i_evt1_ov))
            i_evt2_unique = list(dict.fromkeys(i_evt2_linked+i_evt2_ov))

            result_links_total = {
                "evt1_linked_count" : len(i_evt1_unique),
                "evt1_index" : len(i_evt1_unique)/record_len_min*60,
                "evt1_link_percent" : len(i_evt1_unique)/len(events1)*100 if len(events1)>0 else 0,
                "evt2_linked_count" : len(i_evt2_unique),
                "evt2_index" : len(i_evt2_unique)/record_len_min*60,
                "evt2_link_percent" : len(i_evt2_unique)/len(events2)*100 if len(events2)>0 else 0,               
            }
            info_cur_report.append(["evt1_linked_count", \
                "event 1 linked :"+" number of events 1 linked"])
            info_cur_report.append(["evt1_index", \
                "event 1 linked :"+" density per hour of events 1 linked per hour"])
            info_cur_report.append(["evt1_link_percent", \
                "event 1 linked :"+" percentage of events 1 linked"])
            info_cur_report.append(["evt2_linked_count", \
                "event 2 linked :"+" number of events 1 linked"])
            info_cur_report.append(["evt2_index", \
                "event 2 linked :"+" density per hour of events 2 linked per hour"])
            info_cur_report.append(["evt2_link_percent", \
                "event 2 linked :"+" percentage of events 2 linked"])      


            if csv_report:
                # File name of the current report
                report_name = 'temporal_link-' + temporal_link[1]['name'] + '-' + temporal_link[2]['name']
                report_filename = os.path.join(output_directory, f"{output_prefix}_{report_name}.tsv")
                report_info_filename = os.path.join(output_directory, f"{output_prefix}_{report_name}_info.tsv")

                # Each line is an additional subject
                # Construction of the pandas dataframe that will be used to create the CSV file
                output = {"filename":record_info['filename']} | subject_info_params \
                    | criteria_temporal | criteria_temporal_1 | event_info_params | result_links_start | \
                        result_links_over | result_links_total
                report_df = pd.DataFrame.from_records([output])
                # Write the current report for the current subject into the tsv file
                write_header = not os.path.exists(report_filename)
                try : 
                    report_df.to_csv(path_or_buf=report_filename, sep='\t', \
                        index=False, mode='a', header=write_header, encoding="utf_8")
                except :
                    error_message = f"Snooz can not write in the file {report_filename}."+\
                        f" Check if the drive is accessible and ensure the file is not already open."
                    raise NodeRuntimeException(self.identifier, "EventTemporalLink", error_message)                

                # To write the info text file to describe yhe variable names
                if write_header:
                    # Write common info
                    info_df = pd.DataFrame(None, columns=['name', 'description'])
                    info_df = pd.concat([info_df, pd.DataFrame(info, columns=['name', 'description'])])
                    try :
                        info_df.to_csv(path_or_buf=report_info_filename, \
                            sep='\t', index=False, mode='w', header=write_header, encoding="utf_8")
                    except :
                        error_message = f"Snooz can not write in the file {report_info_filename}."+\
                            f" Check if the drive is accessible and ensure the file is not already open."
                        raise NodeRuntimeException(self.identifier, "EventTemporalLink", error_message)   
                    # Write 
                    info_df = pd.DataFrame(None, columns=['name', 'description'])
                    info_df = pd.concat([info_df, pd.DataFrame(info_cur_report, columns=['name', 'description'])])     
                    try :                    
                        info_df.to_csv(path_or_buf=report_info_filename, \
                            sep='\t', index=False, mode='a', header=False, encoding="utf_8")
                    except :
                        error_message = f"Snooz can not write in the file {report_info_filename}."+\
                            f" Check if the drive is accessible and ensure the file is not already open."
                        raise NodeRuntimeException(self.identifier, "EventTemporalLink", error_message)          

        return {}


    def compute_delay_start(self, events1, events2, window_size):     
        """"
            Compute stats on temporal links with the 0.5 s windows
            Condition : event1 starts before the event 2 starts      
            Stats : number, mean delay (s), index per hour", percentage of event linked
        """        
        delay_start_evt1_before_evt2 = []
        i_evt1_linked = []
        i_evt2_linked = []
        for i_evt, evt1 in events1.iterrows():
            beg_start_sec = evt1.start_sec
            beg_end_sec = beg_start_sec + window_size
            # Find events 2 during the time windows of the event 1
            sel_event2 = events2[(events2.start_sec>=beg_start_sec) &  (events2.start_sec<=beg_end_sec)]
            if len(sel_event2)>0:
                i_evt1_linked.append(i_evt)
                i_evt2_linked = i_evt2_linked + sel_event2.index.to_list()
                #i_evt2_linked.append(sel_event2.index.to_list())
                cur_delay_start = sel_event2.start_sec-evt1.start_sec
                delay_start_evt1_before_evt2.append(cur_delay_start.values)
        flat_list_delay = [item for sublist in delay_start_evt1_before_evt2 for item in sublist]
        #i_evt2_flat = [item for sublist in i_evt2_linked for item in sublist]
        i_evt2_unique = list(dict.fromkeys(i_evt2_linked))
        return flat_list_delay, i_evt1_linked, i_evt2_unique


    def compute_delay_end(self, events1, events2, window_size):     
        """"
            Compute stats on temporal links with the 0.5 s windows
            Condition : event1 ends before the event 2 starts      
            Stats : number, mean delay (s), index per hour", percentage of event linked
        """        
        delay_end_evt1_before_evt2 = []
        i_evt1_linked = []
        i_evt2_linked = []
        for i_evt, evt1 in events1.iterrows():
            end_start_sec = evt1.start_sec+evt1.duration_sec
            end_end_sec = end_start_sec + window_size
            # Find events 2 during the time windows
            sel_event2 = events2[(events2.start_sec>=end_start_sec) &  (events2.start_sec<=end_end_sec)]
            if len(sel_event2)>0:
                i_evt1_linked.append(i_evt)
                cur_delay_end = sel_event2.start_sec-end_start_sec
                delay_end_evt1_before_evt2.append(cur_delay_end.values)
                i_evt2_linked = i_evt2_linked + sel_event2.index.to_list()
                #i_evt2_linked.append(sel_event2.index.to_list())
        flat_list_delay = [item for sublist in delay_end_evt1_before_evt2 for item in sublist]    
        #i_evt2_flat = [item for sublist in i_evt2_linked for item in sublist]
        i_evt2_unique = list(dict.fromkeys(i_evt2_linked))
        return flat_list_delay, i_evt1_linked, i_evt2_unique


    def compute_stats_overlap(self, events1, events2, record_len_min, info_cur_report):     
        """"
            Compute stats based on the events overlap.
            Condition : event1 starts before the event 2 starts      
            Stats : number, index per hour, percentage of event overlapped
        """
        n_evt1_ov = 0
        n_evt_ov_tot = 0
        i_evt1 = []
        for i_evt, evt1 in events1.iterrows():
            sel_event2 = events2[((events2.start_sec+events2.duration_sec)>evt1.start_sec)\
                & (events2.start_sec<(evt1.start_sec+evt1.duration_sec))]
            if len(sel_event2)>0:
                i_evt1.append(i_evt)
                n_evt1_ov = n_evt1_ov + 1
                n_evt_ov_tot = n_evt_ov_tot + len(sel_event2)

        n_evt2_ov = 0
        i_evt2 = []
        for i_evt, evt2 in events2.iterrows():
            sel_event1 = events1[((events1.start_sec+events1.duration_sec)>evt2.start_sec)\
                & (events1.start_sec<(evt2.start_sec+evt2.duration_sec))]
            if len(sel_event1)>0:
                n_evt2_ov = n_evt2_ov +1
                i_evt2.append(i_evt)

        result_links_over = {
            "overlap_count" : n_evt_ov_tot,
            "overlap_index" : n_evt_ov_tot\
                /record_len_min*60,
            "overlap_evt1_percent" : n_evt1_ov/len(events1)*100 if len(events1)>0 else 0,
            "overlap_evt2_percent" : n_evt2_ov/len(events2)*100 if len(events2)>0 else 0,
        }
        info_cur_report.append(["overlap_count", \
            "overlaps of events1 and events2 :"+" number"])
        info_cur_report.append(["overlap_index", \
            "overlaps of events1 and events2 :"+" density per hour"])
        info_cur_report.append(["overlap_evt1_percent", \
            "overlaps of events1 and events2 :"+" percentage of event1 overlapped"])
        info_cur_report.append(["overlap_evt2_percent", \
            "overlaps of events1 and events2 :"+" percentage of event2 overlapped"])

        return result_links_over, info_cur_report, i_evt1, i_evt2


    def compute_stats_windows(self, events1, events2, window_size, record_len_min, info_cur_report):
        """"
            Compute stats on temporal links with the 0.5 s windows
            Conditions :
                event1 starts before the event 2 starts, 
                event1 ends before the event 2 starts
                event2 starts before the event 1 starts, 
                event2 ends before the event 1 starts 
            Stats for each conditions :           
                number, mean delay (s), density per hour", percentage of event linked

        """
        delay_start_evt1_before_evt2,  i_evt1_start_evt1_before_evt2, i_evt2_start_evt1_before_evt2 = \
            self.compute_delay_start(events1, events2, window_size)
        delay_end_evt1_before_evt2, i_evt1_end_evt1_before_evt2, i_evt2_end_evt1_before_evt2 = \
            self.compute_delay_end(events1, events2, window_size)
        delay_start_evt2_before_evt1, i_evt1_start_evt2_before_evt1, i_evt2_start_evt2_before_evt1 = \
            self.compute_delay_start(events2, events1, window_size)
        delay_end_evt2_before_evt1, i_evt1_end_evt2_before_evt1, i_evt2_end_evt2_before_evt1 = \
            self.compute_delay_end(events2, events1, window_size)

        result_links_start = {
            "1start_before_2start_count" : len(delay_start_evt1_before_evt2),
            "1start_before_2start_delay_sec" : np.mean(delay_start_evt1_before_evt2),
            "1start_before_2start_index" : len(delay_start_evt1_before_evt2)/record_len_min*60,
            "1start_before_2start_evt1_percent" : len(i_evt1_start_evt1_before_evt2)/len(events1)*100 if len(events1)>0 else 0,
            "1start_before_2start_evt2_percent" : len(i_evt2_start_evt1_before_evt2)/len(events2)*100 if len(events2)>0 else 0,

            "1end_before_2start_count" : len(delay_end_evt1_before_evt2),
            "1end_before_2start_delay_sec" : np.mean(delay_end_evt1_before_evt2),
            "1end_before_2start_index" : len(delay_end_evt1_before_evt2)/record_len_min*60,
            "1end_before_2start_evt1_percent" : len(i_evt1_end_evt1_before_evt2)/len(events1)*100 if len(events1)>0 else 0,
            "1end_before_2start_evt2_percent" : len(i_evt2_end_evt1_before_evt2)/len(events2)*100 if len(events2)>0 else 0,

            "2start_before_1start_count" : len(delay_start_evt2_before_evt1),
            "2start_before_1start_delay_sec" : np.mean(delay_start_evt2_before_evt1),
            "2start_before_1start_index" : len(delay_start_evt2_before_evt1)/record_len_min*60,
            "2start_before_1start_evt1_percent" : len(i_evt1_start_evt2_before_evt1)/len(events1)*100 if len(events1)>0 else 0,
            "2start_before_1start_evt2_percent" : len(i_evt2_start_evt2_before_evt1)/len(events2)*100 if len(events2)>0 else 0,

            "2end_before_1start_count" : len(delay_end_evt2_before_evt1),
            "2end_before_1start_delay_sec" : np.mean(delay_end_evt2_before_evt1),
            "2end_before_1start_index" : len(delay_end_evt2_before_evt1)/record_len_min*60,
            "2end_before_1start_evt1_percent" : len(i_evt1_end_evt2_before_evt1)/len(events1)*100 if len(events1)>0 else 0,
            "2end_before_1start_evt2_percent" : len(i_evt2_end_evt2_before_evt1)/len(events2)*100 if len(events2)>0 else 0,
        }
        i_evt1_linked = i_evt1_start_evt1_before_evt2 + i_evt1_end_evt1_before_evt2 \
            + i_evt2_start_evt2_before_evt1 + i_evt2_end_evt2_before_evt1        
        i_evt1_unique = list(dict.fromkeys(i_evt1_linked))

        i_evt2_linked = i_evt2_start_evt1_before_evt2 + i_evt2_end_evt1_before_evt2 \
             + i_evt1_start_evt2_before_evt1 + i_evt1_end_evt2_before_evt1
        i_evt2_unique = list(dict.fromkeys(i_evt2_linked))

        info_cur_report.append(["1start_before_2start_count", \
            "event1 starts before the event 2 starts :"+" number"])
        info_cur_report.append(["1start_before_2start_delay_sec", \
            "event1 starts before the event 2 starts :"+" mean delay (s)"])
        info_cur_report.append(["1start_before_2start_index", \
            "event1 starts before the event 2 starts :"+" density per hour"])
        info_cur_report.append(["1start_before_2start_evt1_percent", \
        "event1 starts before the event 2 starts :"+" percentage of event1 linked"])
        info_cur_report.append(["1start_before_2start_evt2_percent", \
            "event1 starts before the event 2 starts :"+" percentage of event2 linked"])

        info_cur_report.append(["1end_before_2start_count", \
            "event1 ends before the event 2 starts :"+" number"])
        info_cur_report.append(["1end_before_2start_delay_sec", \
            "event1 ends before the event 2 starts :"+" mean delay (s)"])
        info_cur_report.append(["1end_before_2start_index", \
            "event1 ends before the event 2 starts :"+" density per hour"])
        info_cur_report.append(["1end_before_2start_evt1_percent", \
            "event1 ends before the event 2 starts :"+" percentage of event1 linked"])
        info_cur_report.append(["1end_before_2start_evt2_percent", \
            "event1 ends before the event 2 starts :"+" percentage of event2 linked"])

        info_cur_report.append(["2start_before_1start_count", \
            "event2 starts before the event 1 starts :"+" number"])
        info_cur_report.append(["2start_before_1start_delay_sec", \
            "event2 starts before the event 1 starts :"+" mean delay (s)"])
        info_cur_report.append(["2start_before_1start_index", \
            "event2 starts before the event 1 starts :"+" density per hour"])
        info_cur_report.append(["2start_before_1start_evt1_percent", \
            "event2 starts before the event 1 starts :"+" percentage of event1 linked"])
        info_cur_report.append(["2start_before_1start_evt2_percent", \
            "event2 starts before the event 1 starts :"+" percentage of event2 linked"])

        info_cur_report.append(["2end_before_1start_count", \
            "event2 ends before the event 1 starts :"+" number"])
        info_cur_report.append(["2end_before_1start_delay_sec", \
            "event2 ends before the event 1 starts :"+" mean delay (s)"])
        info_cur_report.append(["2end_before_1start_index", \
            "event2 ends before the event 1 starts :"+" density per hour"])
        info_cur_report.append(["2end_before_1start_evt1_percent", \
            "event2 ends before the event 1 starts :"+" percentage of event1 linked"])
        info_cur_report.append(["2end_before_1start_evt2_percent", \
            "event2 ends before the event 1 starts :"+" percentage of event2 linked"])
        return result_links_start, info_cur_report, i_evt1_unique, i_evt2_unique


    def get_event_definition(self, events1, events2, info_cur_report):
        event_info_params = {
            "event1_class": None,   
            "event1_group": events1.loc[0]['group'] if len(events1)>0 else None,
            "event1_name" : events1.loc[0]['name'] if len(events1)>0 else None,
            "event2_class": None,   
            "event2_group": events2.loc[0]['group'] if len(events2)>0 else None,
            "event2_name" : events2.loc[0]['name'] if len(events2)>0 else None,
        }
        info_cur_report.append(["event1_class", "events 1 : the class of the events"])
        info_cur_report.append(["event1_group", "events 1 : the group of the events"])
        info_cur_report.append(["event1_name", "events 1 : the name of the events"])
        info_cur_report.append(["event2_class", "events 2 : the class of the events"])
        info_cur_report.append(["event2_group", "events 2 : the group of the events"])
        info_cur_report.append(["event2_name", "events 2 : the name of the events"])
        return event_info_params, info_cur_report

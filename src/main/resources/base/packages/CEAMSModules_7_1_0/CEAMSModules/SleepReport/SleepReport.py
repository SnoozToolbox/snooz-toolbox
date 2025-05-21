"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Generate a sleep report in CSV file. The sleep report is made of about 300 
    statistics. These stats are based on the sleep stages and the sleep cycles 
    produced by the module SleepCycleDelimiter.
    
    Input:
        "input_filename": String
            The name of the file being analysed, it will be written in the report 
            in the first column.
        "sleep_stages": pandas DataFrame
            A dataframe with all sleep stages of the file to analyze.
        "sleep_cycles": Array
            Array of sleep cycles. This is the one selected by the user.
        "sleep_cycles_params": dict
            Parameters that were selected by the user to create the sleep cycles.
        "record_info": dict
            Information about the user from the PSG file.
        "rem_periods": array
            List of REM periods
        "report_constants": dict
            Constants used in the report (N_HOURS, N_CYCLES)
        "html_report": bool
            Generate the HTML report if True.
        "html_report_config": TODO TYPE
            TODO DESCRIPTION
        "csv_report": bool
            Generate the CSV report if True.
        "output_prefix": str
            The prefix of the report filename
        "output_directory": str
            The path to the output directory

    Output:
        "report": pandas Dataframe
            Dataframe with all statistics of the report. This is then used as an 
            input to another module to produce the HTML report.

"""
from datetime import datetime, timedelta
import math
import numpy as np
import os
import pandas as pd

from flowpipe import SciNode, InputPlug, OutputPlug

from ..PSGReader import commons
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from CEAMSModules.SleepReport.SleepReportDoc import write_doc_file

DEBUG = False

class SleepReport(SciNode):
    """
        Generate a sleep report in CSV file. The sleep report is made of about 300 statistics. 
        These stats are based on the sleep stages and the sleep cycles produced by the 
        module SleepCycleDelimiter.

        Input:
            "input_filename": String
                The name of the file being analysed, it will be written in the report in the first column.
            "sleep_stages": pandas DataFrame
                A dataframe with all sleep stages of the file to analyze.
            "sleep_cycles": Array
                Array of sleep cycles. This is the one selected by the user.
            "sleep_cycles_params": dict
                Parameters that were selected by the user to create the sleep cycles.
            "record_info": dict
                Information about the user from the PSG file.
            "rem_periods": array
                List of REM periods
            "report_constants": dict
                Constants used in the report (N_HOURS, N_CYCLES)
            "html_report": bool
                Generate the HTML report if True.
            "html_report_config": TODO TYPE
                TODO DESCRIPTION
            "csv_report": bool
                Generate the CSV report if True.
            "output_prefix": str
                The prefix of the report filename
            "output_directory": str
                The path to the output directory

        Output:
            "report": pandas Dataframe
                Dataframe with all statistics of the report. This is then used as an input 
                to another module to produce the HTML report.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')
        InputPlug('input_filename', self)
        InputPlug('sleep_stages', self)
        InputPlug('sleep_cycles', self)
        InputPlug('sleep_cycles_params', self)
        InputPlug('record_info', self)
        InputPlug('rem_periods', self)
        InputPlug('report_constants', self)
        InputPlug('html_report',self)
        InputPlug('html_report_config',self)
        InputPlug('csv_report',self)
        InputPlug('output_prefix',self)
        InputPlug('output_directory',self)
        OutputPlug('report', self)
        
        self.epo_to_min = 0
        self.actual_sleep_duration = 0

    def __del__(self):
        if DEBUG: print('SleepReport.__del__')

    def subscribe_topics(self):
        pass

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'SleepReport.on_topic_update {topic}:{message}')

    def compute(self, input_filename, sleep_stages, sleep_cycles, sleep_cycles_params, \
        record_info, rem_periods, report_constants, html_report, html_report_config, \
            csv_report, output_prefix, output_directory):
        """
            Generate a sleep report in CSV file. The sleep report is made of about 300 statistics. 
            These stats are based on the sleep stages and the sleep cycles produced by the 
            module SleepCycleDelimiter.
            
            Input:
                "input_filename": String
                    The name of the file being analysed, it will be written in the report in the first column.
                "sleep_stages": pandas DataFrame
                    A dataframe with all sleep stages of the file to analyze.
                "sleep_cycles": Array
                    Array of sleep cycles. This is the one selected by the user.
                "sleep_cycles_params": dict
                    Parameters that were selected by the user to create the sleep cycles.
                "record_info": dict
                    Information about the user from the PSG file.
                "rem_periods": array
                    List of REM periods
                "report_constants": dict
                    Constants used in the report (N_HOURS, N_CYCLES)
                "html_report": bool
                    Generate the HTML report if True.
                "html_report_config": TODO TYPE
                    TODO DESCRIPTION
                "csv_report": bool
                    Generate the CSV report if True.
                "output_prefix": str
                    The prefix of the report filename
                "output_directory": str
                    The path to the output directory

            Output:
                "report": pandas Dataframe
                    Dataframe with all statistics of the report. This is then used as an input 
                    to another module to produce the HTML report.
        """
        # INPUT VALIDATION
        if type(sleep_stages) != pd.DataFrame:
            raise NodeInputException(self.identifier, "sleep_stages", \
                "SleepReport sleep_stages parameter must be set.")
        
        if type(sleep_cycles) != list:
            raise NodeInputException(self.identifier, "sleep_cycles", \
                "SleepReport sleep_cycles parameter must be set.")

        if type(sleep_cycles_params) != dict:
            raise NodeInputException(self.identifier, "sleep_cycles_params", \
                "SleepReport sleep_cycles_params parameter must be set.")

        if record_info == '' or record_info is None:
            raise NodeInputException(self.identifier, "record_info", \
                "SleepReport record_info parameter must be set.")

        if isinstance(report_constants,str) and report_constants == '':
            raise NodeInputException(self.identifier, "report_constants", \
                "SleepReport report_constants parameter must be set.")
        elif isinstance(report_constants,str):
            report_constants = eval(report_constants)
        if isinstance(report_constants,dict) == False:
            raise NodeInputException(self.identifier, "report_constants",\
                "SleepReport report_constants expected type is dict and received type is " + str(type(report_constants)))
        
        self.max_cycles_count = int(report_constants['N_CYCLES'])

        # Convert all stages
        # All stages that are not the standard scored stages (W, N1, N2, N3, REM) are considered as Undefined.
        # This include: Unscored, Move, Tech
        sleep_stages["name"] = sleep_stages["name"].replace("6","9")
        sleep_stages["name"] = sleep_stages["name"].replace("7","9")
        sleep_stages["name"] = sleep_stages["name"].replace("8","9")

        if not self.is_scored(sleep_stages):
            raise NodeInputException(self.identifier, "input_filename", \
                f"SleepReport {input_filename} is not scored.")

        subject_info_params = self.get_subject_info(record_info)

        # Init epoch variables
        self.epoch_length = math.ceil(sleep_stages['duration_sec'].values[0])
        self.epo_to_min = self.epoch_length / 60 # Conversion from epoch count to minutes
        # TODO add in PSGReader.common?
        aasm_stages = ['1','2','3','4','5']
        feinberg_stages = ['2','3','4','5']

        # set the valid sleep stages depending on the sleep cycle option selected.
        if sleep_cycles_params['defined_option'] == 'Aeschbach 1993' or \
            sleep_cycles_params['defined_option'] == 'Feinberg 1979':
            valid_sleep_stages = feinberg_stages
        else:
            valid_sleep_stages = aasm_stages

        # Extract all stages from the Dataframe into an array.
        all_stages = sleep_stages['name'].values.tolist()

        # Trim the unscored stages at the start and end
        scoring_start = self.find_first_scored_index(all_stages)
        scoring_end = self.find_last_scored_index(all_stages)
        
        # Extract only the period that's been scored. All metrics are based on this list or a subsection.
        scored_stages = all_stages[scoring_start:scoring_end+1]

        # ANALYSIS

        # Sleep latencies
        self.sleep_latency_aasm = self.compute_sleep_latency(scored_stages, aasm_stages)
        self.sleep_latency_feinberg = self.compute_sleep_latency(scored_stages, feinberg_stages)
        self.sleep_latency_aeschbach = self.sleep_latency_feinberg

        if sleep_cycles_params['defined_option'] == 'Aeschbach 1993' or \
            sleep_cycles_params['defined_option'] == 'Feinberg 1979':
            self.sleep_latency = self.sleep_latency_feinberg
        else:
            self.sleep_latency = self.sleep_latency_aasm
        
        # Get general information
        
        sleep_cycle_params = self.get_sleep_cycle_parameters(sleep_cycles_params) 

        # Get information about the recording
        hypnogram_start_time = sleep_stages.iloc[scoring_start]['start_sec']
        hypnogram_end_time = sleep_stages.iloc[scoring_end]['start_sec'] + sleep_stages.iloc[scoring_end]['duration_sec']
        recording_params = self.get_recording_params(scored_stages, record_info['creation_date'], hypnogram_start_time, hypnogram_end_time)

        # Stats for the wake event within the sleep period
        if self.sleep_latency != None:
            sleep_period_end = self.get_last_sleep_epoch(scored_stages, valid_sleep_stages)
            sleep_period_stages = scored_stages[self.sleep_latency:sleep_period_end+1] # +1 because the last index is exclusive
        else:
            sleep_period_stages = []
        wake_stats = self.compute_wake_stats(sleep_period_stages, scored_stages, valid_sleep_stages)

        # Compute stats for all subdivisions, halves and thirds
        thirds_min_stats, thirds_pc_stats, thirds_dis_stats = \
            self.compute_stats_by_subdivisions(3, sleep_period_stages, "third")
        halves_min_stats, halves_pc_stats, halves_dis_stats = \
            self.compute_stats_by_subdivisions(2, sleep_period_stages, "half")
        total_min_stats, total_pc_stats, _ = \
            self.compute_stats_by_subdivisions(1, sleep_period_stages, "total", show_index=False)

        cycles_stats =      self.compute_cycles_stats(sleep_cycles)
        transition_stats =  self.compute_transition_stats(scored_stages)
        stages_latencies =  self.compute_stages_latencies(scored_stages)
        rem_stats =         self.compute_rem_periods_stats(rem_periods, all_stages, scoring_start)

        # Construction of the pandas dataframe that will be used to create the CSV file
        output = subject_info_params | sleep_cycle_params | recording_params | \
           stages_latencies | wake_stats | \
           thirds_min_stats | halves_min_stats | total_min_stats | \
           thirds_pc_stats  | halves_pc_stats  | total_pc_stats  | \
           thirds_dis_stats | halves_dis_stats | \
           cycles_stats     | rem_stats        | transition_stats
        report = pd.DataFrame.from_records([output])

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
            output_filename = os.path.join(output_directory, f"{output_prefix}.tsv")
            if output_filename != '':
                write_header = not os.path.exists(output_filename)
                try : 
                    report.to_csv(path_or_buf=output_filename, sep='\t', index=False, mode='a', header=write_header, encoding="utf_8")
                except :
                    error_message = f"Snooz can not write in the file {output_filename}."+\
                        f" Check if the drive is accessible and ensure the file is not already open."
                    raise NodeRuntimeException(self.identifier, "SleepReport", error_message)   
                # Write the documentation file
                doc_filepath = os.path.join(output_directory, f"{output_prefix}_info.tsv")
                write_doc_file(doc_filepath, self.max_cycles_count)

        return {"report":report}


    def is_scored(self, stages):
        """ Check if the file has been scored. 
        Parameters:
            stages (Dataframe): All stages from the file
        Returns:
            Bool: True if any stage is scored, False if not.
        """
        stages = stages['name'].values.tolist()
        if stages.count("9")>0:
            return stages.count("9") != len(stages) 
        elif stages.count("8")>0:
            return stages.count("9") != len(stages) 
        return True


    def find_first_scored_index(self, sleep_stages):
        """ Find the index of the first stage scored.
            Scored is defined as different than 9.
        Parameters:
            stages (Dataframe): All stages from the file
        Returns:
            int: The index of the first stage scored or None if not found.
        """
        for idx, stage in enumerate(sleep_stages):
            if stage != '9':
                return idx
        else:
            return None


    def find_last_scored_index(self, sleep_stages):
        """ Find the index of the last stage scored.
            Scored is defined as different than 9.
        Parameters:
            stages (Dataframe): All stages from the file
        Returns:
            int: The index of the last stage scored or None if not found.
        """
        for idx, stage in reversed(list(enumerate(sleep_stages))):
            if stage != '9':
                return idx
        else:
            return None


    def compute_sleep_latency(self, scored_stages, valid_sleep_stages):
        """ Compute the sleep latency. Defined as the number of epochs from
        the beginning to the first valid sleep epoch.

        Parameters:
            scored_stages (Dataframe): All scored stages from the file
            valid_sleep_stages (array): List of valid sleep stages
        Returns:
            int: The sleep latency or None if not found
        """
        sleep_latency = None

        for idx, stage in enumerate(scored_stages):
            if stage in valid_sleep_stages:
                sleep_latency = idx
                break

        return sleep_latency
    
    def get_last_sleep_epoch(self, scored_stages, valid_sleep_stages):
        """ Return the index of the last sleep epoch.

        Parameters:
            scored_stages (Dataframe): All scored stages from the file.
            valid_sleep_stages (array): List of valid sleep stages.
        Returns:
            int: The index of the last sleep epoch or None if not found.
        """
        last_sleep_epoch = None
        for idx, stage in reversed(list(enumerate(scored_stages))):
            if stage in valid_sleep_stages:
                last_sleep_epoch = idx
                break

        return last_sleep_epoch

    def get_subject_info(self, record_info):
        """ Return a dictionary with all information about the subject.

        Parameters:
            record_info (dict): The information of the patients to extract.
        Returns:
            dict: A dictionary with all the information of the patient.
        """
        # We do not want the changes to impact the original dict
        record_info = record_info.copy()
        if record_info["birthdate"] is not None:
            birthdate_datetime = datetime(1970, 1, 1) + timedelta(seconds=record_info["birthdate"])
            record_info["birthdate"] = birthdate_datetime.strftime("%Y-%m-%d")
        else:
            record_info["birthdate"] = ""

        if record_info["creation_date"] is not None:
            creation_datetime = datetime.utcfromtimestamp(record_info["creation_date"])
            record_info['creation_date'] = creation_datetime.strftime("%Y-%m-%d")
        else:
            record_info["creation_date"] = ""

        return record_info

    def get_sleep_cycle_parameters(self, sleep_cycles_params):
        """ Return a dictionary with all information about the subject.

        Parameters:
            sleep_cycles_params (dict): The sleep cycle parameters used to compute
                all sleep cycles by the module SleepCycleDelimiter.
        Returns:
            dict: A dictionary with sleep cycles parameters.
        """
        param = {}
        param['cyc_def_option'] = sleep_cycles_params['defined_option']
        param['cyc_def_include_soremp'] = sleep_cycles_params['Include_SOREMP']
        param['cyc_def_include_last_incomplete'] = sleep_cycles_params['Include_last_incompl']
        param['cyc_def_rem_min'] = sleep_cycles_params['dur_ends_REMP']
        param['cyc_def_first_nrem_min'] = sleep_cycles_params['NREM_min_len_first']
        param['cyc_def_mid_last_nrem_min'] = sleep_cycles_params['NREM_min_len_mid_last']
        param['cyc_def_last_nrem_valid_min'] = sleep_cycles_params['NREM_min_len_val_last']
        param['cyc_def_first_rem_min'] = sleep_cycles_params['REM_min_len_first']
        param['cyc_def_mid_rem_min'] = sleep_cycles_params['REM_min_len_mid']
        param['cyc_def_last_rem_min'] = sleep_cycles_params['REM_min_len_last']
        param['cyc_def_move_end_rem'] = sleep_cycles_params['mv_end_REMP']
        param['cyc_def_sleep_stages'] = sleep_cycles_params['sleep_stages']

        return param


    def get_recording_params(self, scored_stages, creation_date, hypnogram_start_time, hypnogram_end_time):
        """ Return a dictionary with the information about the recording.

        Parameters:
            scored_stages (Dataframe): Scored sleep stages
            creation_date (float): Date of creation.
            hypnogram_start_time (float): Start time of the hypnogram.
            hypnogram_end_time (float): end time of the hypnogram.
        Returns:
            dict: A dictionary with all recording informations.
        """

        self.recording_duration = len(scored_stages) * self.epo_to_min

        if type(creation_date) is str:
            first_epoch_time = hypnogram_start_time
        elif type(creation_date) is int and hypnogram_start_time != None:
            first_epoch_datetime = datetime.utcfromtimestamp(creation_date + hypnogram_start_time)
            first_epoch_time = first_epoch_datetime.strftime("%Y-%m-%d %H:%M:%S")
        else:
            first_epoch_time = None

        if type(creation_date) is str:
            last_epoch_time = hypnogram_end_time
        elif type(creation_date) is int and hypnogram_end_time != None:
            last_epoch_datetime = datetime.utcfromtimestamp(creation_date + hypnogram_end_time)
            last_epoch_time = last_epoch_datetime.strftime("%Y-%m-%d %H:%M:%S")
        else:
            last_epoch_time = None

        return {
            "epoch_sec":self.epoch_length,
            "first_epoch_time_win":first_epoch_time,
            "last_epoch_time_win":last_epoch_time,
            "record_min":self.recording_duration
        }

    def compute_cycles_stats(self, sleep_cycles):
        """ Compute sleep cycles stats.
            For each cycle, the following values are returned:
                - The length in minutes of the NREM period
                - The length in minutes of the REM period
                - The length in minutes of the cycle

        Parameters:
            sleep_cycles (list(nrem(start,end), rem(start,end))): Scored sleep stages
        Returns:
            dict: A dictionary with the sleep cycle information.
        """
        stats = {}
        stats["sleep_cycle_count"] = len(sleep_cycles)
        for idx in range(self.max_cycles_count):
            if idx < len(sleep_cycles):
                nrem, rem, is_complete = sleep_cycles[idx]
                stats[f"cyc{idx+1}_nrem_min"] = (nrem[1] - nrem[0] + 1) * self.epo_to_min # +1 because the interval is inclusive
                if rem[0] is not None:
                    stats[f"cyc{idx+1}_R_min"] = (rem[1] - rem[0] + 1) * self.epo_to_min
                    stats[f"cyc{idx+1}_min"] = (rem[1] - nrem[0] + 1) * self.epo_to_min
                else:
                    stats[f"cyc{idx+1}_R_min"] = 0
                    stats[f"cyc{idx+1}_min"] = stats[f"cyc_{idx+1}_nrem_min"]
            else:
                stats[f"cyc{idx+1}_nrem_min"] = None
                stats[f"cyc{idx+1}_R_min"] = None
                stats[f"cyc{idx+1}_min"] = None

        return stats

    def compute_rem_periods_stats(self, rem_periods, stages, scoring_start):
        """ Compute statistics for REM sleep periods.
            REM sleep periods can contains other stages than REM sleep, this function
            counts them and compute the REM sleep efficiency. REM sleep efficiency
            is the time spent in actual REM sleep within the REM period.

            Parameters:
                rem_periods (array): List of sleep REM period
                                    format: [(REM_START,REM_END)]
                                    values are inclusive indexes.
                stages (array): List of all stages.
                scoring_start (int): The index of the first scored epoch.
            Returns:
        """
        rem_stats = []
        period_count = 0
        # For all sleep cycles
        for idx in range(self.max_cycles_count):
            skip = False
            if idx < len(rem_periods):
                rem = rem_periods[idx][0]
                if rem[0] > rem[1]:
                    skip = True
            else:
                skip = True

            # If there is a REM period (some incomplete cycle at the end of a night
            # might not have one).
            if not skip:
                period_count = period_count + 1
                stats = {}

                # Get the sleep stages of this REM period
                rem_stage = stages[rem[0]:rem[1]+1]

                # Count the fragmentation of the REM period. A continious sequence 
                # of REM stages count as one fragment.
                frag_count = 0
                is_in_rem = False
                for stage in rem_stage:
                    if stage == '5' and not is_in_rem:
                        frag_count = frag_count + 1
                        is_in_rem = True
                    elif stage != '5':
                        is_in_rem = False

                stats['frag_count'] = frag_count

                # Interval is the length of time between the beginning of a REM
                # period and the beginning of the REM period of the previous cycle.
                # For the first REM period, it's the delay between the sleep latency
                # and the first REM period.
                if idx == 0:
                    stats['interval'] = rem[0] - scoring_start - self.sleep_latency
                else:
                    stats['interval'] = rem[0] - last_rem[0]

                # Count  stages within the REM period.
                stats['wake_count'] = rem_stage.count("0")
                stats['nrem_count'] = rem_stage.count("1") + rem_stage.count("2") + rem_stage.count("3") + rem_stage.count("4")
                stats['rem_count'] = rem_stage.count("5")
                stats['undef_count'] = rem_stage.count("9")
                stats['total_count'] = len(rem_stage)

                # Efficiency is simple the amount of REM sleep over the total amount
                # of sleep stages within the REM period.
                stats['efficiency'] = stats['rem_count'] / stats['total_count']
                last_rem = rem

                rem_stats.append(stats)
            else:
                stats = {}
                stats['frag_count'] = None
                stats['interval'] = None
                stats['wake_count'] = None
                stats['nrem_count'] = None
                stats['rem_count'] = None
                stats['undef_count'] = None
                stats['total_count'] = None
                stats['efficiency'] = None
                rem_stats.append(stats)

        if period_count > 0:

            # Just add all stats to get the total
            rem_stats_total = {}
            rem_stats_total['frag_count'] = 0
            rem_stats_total['interval'] = 0
            rem_stats_total['wake_count'] = 0
            rem_stats_total['nrem_count'] = 0
            rem_stats_total['rem_count'] = 0
            rem_stats_total['undef_count'] = 0
            rem_stats_total['total_count'] = 0
            for rem_stat in rem_stats:
                rem_stats_total['frag_count'] = rem_stats_total['frag_count'] + (rem_stat['frag_count'] if rem_stat['frag_count'] is not None else 0)
                rem_stats_total['interval'] =   rem_stats_total['interval'] +   (rem_stat['interval'] if rem_stat['interval'] is not None else 0)
                rem_stats_total['wake_count'] = rem_stats_total['wake_count'] + (rem_stat['wake_count'] if rem_stat['wake_count'] is not None else 0)
                rem_stats_total['nrem_count'] = rem_stats_total['nrem_count'] + (rem_stat['nrem_count'] if rem_stat['nrem_count'] is not None else 0)
                rem_stats_total['rem_count'] =  rem_stats_total['rem_count'] +  (rem_stat['rem_count'] if rem_stat['rem_count'] is not None else 0)
                rem_stats_total['undef_count'] =  rem_stats_total['undef_count'] +  (rem_stat['undef_count'] if rem_stat['undef_count'] is not None else 0)
                rem_stats_total['total_count']= rem_stats_total['total_count']+ (rem_stat['total_count'] if rem_stat['total_count'] is not None else 0)
            
            rem_stats_total['efficiency'] = rem_stats_total['rem_count'] / rem_stats_total['total_count']
            rem_stats_total['interval'] = rem_stats_total['interval'] / period_count

            # Export names
            stats = {
                "rem_intervals_mean":rem_stats_total['interval'] * self.epo_to_min,
                "rem_total_R_min":rem_stats_total['rem_count'] * self.epo_to_min,
                "rem_total_N1N2N3_min":rem_stats_total['nrem_count'] * self.epo_to_min,
                "rem_total_W_min":rem_stats_total['wake_count'] * self.epo_to_min,
                "rem_total_Unscored_min":rem_stats_total['undef_count'] * self.epo_to_min,
                "rem_total_time_min":rem_stats_total['total_count'] * self.epo_to_min,
                "rem_fragmentation_count":int(rem_stats_total['frag_count']),
                "rem_R_efficiency_percent":rem_stats_total['efficiency']  * 100,
                "rem_count":period_count
            }
            for idx, rem_stat in enumerate(rem_stats):
                stats[f"rem{idx+1}_interval_min"] = (self.epo_to_min * rem_stat['interval']) if rem_stat['interval'] is not None else None
                stats[f"rem{idx+1}_R_min"] = (self.epo_to_min * rem_stat['rem_count']) if rem_stat['rem_count'] is not None else None
                stats[f"rem{idx+1}_N1N2N3_min"] = (self.epo_to_min * rem_stat['nrem_count']) if rem_stat['nrem_count'] is not None else None
                stats[f"rem{idx+1}_W_min"] = (self.epo_to_min * rem_stat['wake_count']) if rem_stat['wake_count'] is not None else None
                stats[f"rem{idx+1}_Unscored_min"] = (self.epo_to_min * rem_stat['undef_count']) if rem_stat['undef_count'] is not None else None
                stats[f"rem{idx+1}_min"] = (self.epo_to_min * rem_stat['total_count']) if rem_stat['total_count'] is not None else None
                stats[f"rem{idx+1}_fragmentation_count"] = int(rem_stat['frag_count']) if rem_stat['frag_count'] is not None else None
                stats[f"rem{idx+1}_efficiency_percent"] = (rem_stat['efficiency'] * 100) if rem_stat['efficiency'] is not None else None

            return stats
        else:
            stats = {
                "rem_intervals_mean":None,
                "rem_total_R_min":None,
                "rem_total_N1N2N3_min":None,
                "rem_total_W_min":None,
                "rem_total_Unscored_min":None,
                "rem_total_time_min":None,
                "rem_fragmentation_count":None,
                "rem_R_efficiency_percent":None,
                "rem_count":0
            }
            for idx, rem_stat in enumerate(rem_stats):
                stats[f"rem{idx+1}_interval_min"] = None
                stats[f"rem{idx+1}_R_min"] = None
                stats[f"rem{idx+1}_N1N2N3_min"] = None
                stats[f"rem{idx+1}_W_min"] = None
                stats[f"rem{idx+1}_Unscored_min"] = None
                stats[f"rem{idx+1}_min"] = None
                stats[f"rem{idx+1}_fragmentation_count"] = None
                stats[f"rem{idx+1}_efficiency_percent"] = None
            return stats

    def compute_persistant_sleep_latency(self, scored_stages):
        """ Compute persistant sleep latency

            Persistant sleep is defined as 10 minutes of continious sleep stages.
            The latency is the time it takes from the beginning of the hypnogram 
            (assumed to be the lights off) to the beginning of the 10 minutes period.

            Parameters:
            scored_stages (array): List of stages from the complete hypnogram. 

            Returns:
                float: The latency is the time it takes from the beginning of 
                the hypnogram (assumed to be the lights off) to the beginning 
                of the 10 minutes period.
        """
        if self.sleep_latency is None:
            return None
        
        continious_count = 0
        persistant_sleep_latency = None
        continious_length = 10 * 60 / self.epoch_length
        candidate_latency = 0
        for idx, stage in enumerate(scored_stages):
            if idx >= self.sleep_latency:
                if stage == '0':
                    continious_count = 0
                elif continious_count == 0:
                    candidate_latency = idx
                    continious_count = 1
                elif continious_count > 0:
                    continious_count = continious_count + 1
                    if continious_count == continious_length:
                        persistant_sleep_latency = candidate_latency
                        break

        return persistant_sleep_latency
        
    def compute_stages_latencies(self, scored_stages):
        """ Compute latencies for all stages.

            Latencies for stage N1 and N2 are base on the beginning of the of the
            hypnogram (scored_stages). Other stage's latency are based on the 
            sleep_latency.

            Parameters:
            scored_stages (array): List of stages from the complete hypnogram. 
            sleep_latency (float): Sleep latencies

            Returns:
                dict: {
                    "N1":[n1_latency],
                    "N2":[n2_latency],
                    "N3":[n3_latency],
                    "R":[rem_latency],
                    "movement":[movement_latency],
                    "tech":[tech_latency],
                    "unscored":[unscored_latency]
                }
        """
        # Stage latency
        stages_latency = {}
        for j, (stage_name, stage_id) in enumerate(commons.sleep_stages_name.items()):
            try:
                latency = scored_stages.index(stage_id)
                
                if int(stage_id)>2:
                    latency = latency - self.sleep_latency

                latency_min = latency * self.epo_to_min
                stages_latency[stage_name] = (latency, latency_min)

            except:
                stages_latency[stage_name] = (None,None)

        # Compute persistant sleep latency
        persistant_sleep_latency = self.compute_persistant_sleep_latency(scored_stages)

        return {
            "sleep_latency_used_in_this_report_min": self.sleep_latency * self.epo_to_min if self.sleep_latency != None else None,
            "sleep_latency_aasm_min": self.sleep_latency_aasm * self.epo_to_min if self.sleep_latency_aasm != None else None,
            "sleep_latency_aeschbach_min": self.sleep_latency_aeschbach * self.epo_to_min if self.sleep_latency_aeschbach != None else None,
            "sleep_latency_floyd_min": self.sleep_latency_feinberg * self.epo_to_min if self.sleep_latency_feinberg != None else None,
            "persistant_sleep_latency_min":persistant_sleep_latency * self.epo_to_min if persistant_sleep_latency != None else None,
            "sleep_latency_N1_min":stages_latency["N1"][1],
            "sleep_latency_N2_min":stages_latency["N2"][1],
            "sleep_latency_N3_min":stages_latency["N3"][1],
            "sleep_latency_R_min":stages_latency["R"][1]
        }

    def compute_transition_stats(self, sleep_stages):
        """ Compute stages transition stats during the sleep period.

            Parameters:
            sleep_stages (array): List of stages for the sleep period. It is expected
                that the list contains 1 extra stage at the beginning so the very first
                transition of the sleep period can be accounted for.

            Returns:
                dict: A dictionary with the count of all possible transitions.
        """
        # Hack to convert any undefined stages into '8'
        sleep_stages_undefined_hacked = sleep_stages.copy()
        sleep_stages_undefined_hacked = [stage.replace('6', '8') for stage in sleep_stages_undefined_hacked]
        sleep_stages_undefined_hacked = [stage.replace('7', '8') for stage in sleep_stages_undefined_hacked]
        sleep_stages_undefined_hacked = [stage.replace('9', '8') for stage in sleep_stages_undefined_hacked]

        # List of stages we are interest in computing their transitions.
        #transition_stages = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        transition_stages = list(commons.sleep_stages_name.values())
        transition_matrix = np.zeros((len(transition_stages),len(transition_stages)+1)) # The extra +1 columns is the total of the row
        transition_total = 0

        # Go through all stages of interest to compute the transition matrix
        for from_i, from_stage in enumerate(transition_stages):
            for to_i, to_stage in enumerate(transition_stages):
                count = 0
                # For each possible transition pairs
                if from_i != to_i:
                    # Count how many time this pair is found
                    for i in range(len(sleep_stages_undefined_hacked)-1):
                        if f"{from_stage}" == sleep_stages_undefined_hacked[i] and f"{to_stage}" == sleep_stages_undefined_hacked[i+1]:
                            count = count + 1

                transition_matrix[from_i][to_i] = count
            row_total = sum(transition_matrix[from_i])
            transition_matrix[from_i][len(transition_stages)] = row_total
            transition_total = transition_total + row_total

        export_stage_names = {
            "0":"W",
            "1":"N1",
            "2":"N2",
            "3":"N3",
            "4":"N4",
            "5":"R",
            "6":"movement",
            "7":"tech",
            "8":"Unscored",
            "9":"Unscored"
        }

        stats = {}
        stages_to_ignore = [4, 6, 7, 8]
        for from_i, from_stage in enumerate(transition_stages):
            for to_i, to_stage in enumerate(transition_stages):
                if from_i != to_i:
                    if from_i not in stages_to_ignore and to_i  not in stages_to_ignore:
                        from_label = export_stage_names[from_stage]
                        to_label = export_stage_names[to_stage]
                        stats[f'{from_label}_to_{to_label}_count'] = int(transition_matrix[from_i][to_i])
            # Add the stat for the total transition of this stage
            if from_i not in stages_to_ignore:
                stats[f'{from_label}_to_any_count'] = int(transition_matrix[from_i][len(transition_stages)])
        stats[f'any_to_any_count'] = int(transition_total)
        return stats

    def get_stage_name_by_index(self, stage_index):
        for label, idx in commons.sleep_stages_name.items():
            if idx == stage_index:
                return label
        
    def compute_stats_by_subdivisions(self, subdivision_count, sleep_stages, prefix, show_index=True):
        """ Compute all stats related to subdivisions of the sleep period ex: 
                first half, second half, first third, second third, etc.

            Parameters:
            subdivision_count (int): How many subdivision ex: 2 would mean 2 halves
                                                              3 would mean 3 thirds
            sleep_stages (array): List of stages for the sleep period
            prefix (str): Prefix used for the label of the statistic ex:[prefix]1MinStage
            show_index (bool): Show the index in the subdivision or not. This
                is only used to compute the total values when subdivision_count = 1.

            Returns:
                dict: A dictionary with the stats of all subdivisions.

        """
        # Init variables
        nrem_total_count = sleep_stages.count("1") + sleep_stages.count("2") \
            + sleep_stages.count("3") + sleep_stages.count("4")
        undefined_total_count = sleep_stages.count("9")
        stats = [{} for i in range(subdivision_count)]

        sleep_length = len(sleep_stages)
        # How many stages in each subdivision
        # It is a wierd way of doing it but this how it was done with the old software and 
        # in order to validate this one we need to do it the same way.
        # ex: there are 11 stages and we want 3 parts, instead of giving parts of length: 4,4,3
        # we get 3 parts of length: 3,3,5.
        subdivision_size = int(sleep_length / subdivision_count)
        
        subdivision_sizes = []
        for i in range(subdivision_count):
            if i < subdivision_count-1:
                subdivision_sizes.append(subdivision_size)
            else:
                subdivision_sizes.append(sleep_length - subdivision_size*(i))

        # Because the list of stages is passed by reference and we will be modifying it in this function
        sleep_stages_copy = sleep_stages.copy()

        # For each subdivision (each half, each third, etc.)
        for i in range(subdivision_count):
            nrem_count = 0
            nrem_percent = 0
            undefined_count = 0
            undefined_percent = 0

            # Stats will be computed for the stages of the subdivision only
            subdivision_stages = []
            for j in range(subdivision_sizes[i]):
                subdivision_stages.append(sleep_stages_copy.pop(0))

            # Compute the stats for each possible stage ex: Wake, N1, N2, N3, N4, REM, etc
            # within the current subdivision.
            for j, (stage_name, stage_id) in enumerate(commons.sleep_stages_name.items()):
                percent = 0

                # How many N1, N2, N3 etc. in this subdivision
                current_stage_count = subdivision_stages.count(f"{stage_id}")

                # How many N1, N2, N3 etc. in the whole sleep period
                total_stage_count = sleep_stages.count(f"{stage_id}")

                # Distribution is defined as the amount of this current stage 
                # within the subdivision over the total amount of this sleep stage 
                # within the whole sleep period.
                if total_stage_count != 0:
                    distribution = current_stage_count / total_stage_count if total_stage_count > 0 else 0
                else:
                    distribution = None

                if int(stage_id) == 0:
                    # Percent for wake state is based on the duration of the whole sleep period
                    percent = current_stage_count / sleep_length if sleep_length > 0 else None
                elif int(stage_id) >=6:
                    # Percent for undefined states are based on the duration of the actual 
                    # sleep duration within the sleep period.
                    percent = (current_stage_count * self.epo_to_min) / self.get_actual_sleep_duration(sleep_stages) if sleep_length > 0 else None                    
                    undefined_percent = undefined_percent + percent  if sleep_length > 0 else None
                elif int(stage_id) ==5:
                    # Percent for REM states are based on the duration of the actual 
                    # sleep duration within the sleep period.
                    percent = (current_stage_count * self.epo_to_min) / self.get_actual_sleep_duration(sleep_stages) if sleep_length > 0 else None
                elif (int(stage_id) >= 1) and (int(stage_id) <= 4):
                    # Percent for N1, N2, N3, N4, states is also based on the duration 
                    # of the actual sleep duration within the sleep period.
                    percent = (current_stage_count * self.epo_to_min) / self.get_actual_sleep_duration(sleep_stages) if sleep_length > 0 else None
                    nrem_percent = nrem_percent + percent  if sleep_length > 0 else None
                
                
                stats[i][stage_name] = (current_stage_count, percent, distribution)

                # Aggregates values for all NREM stages
                if sleep_length > 0:
                    if int(stage_id) >= 1 and int(stage_id) <= 4:
                        nrem_count = nrem_count + current_stage_count
                    if int(stage_id)>=6: 
                        undefined_count = undefined_count + current_stage_count
                else:
                    nrem_count = None
                    undefined_count = None
        
            nrem_distribution = nrem_count / nrem_total_count if nrem_total_count > 0 else None
            stats[i]['NREM'] = (nrem_count, nrem_percent, nrem_distribution)
            undefined_distribution = undefined_count / undefined_total_count if undefined_total_count > 0 else None
            stats[i]['undefined'] = (undefined_count, undefined_percent, undefined_distribution)            

            # REM and NREM stats
            rem_pc = stats[i]['R'][1]
            nrem_pc = stats[i]['NREM'][1]
            sleep_pc = rem_pc + nrem_pc if sleep_length > 0 else None
            rem_count = stats[i]['R'][0]
            nrem_count = stats[i]['NREM'][0]
            sleep_count = rem_count + nrem_count if sleep_length > 0 else None
            stats[i]['Sleep'] = (sleep_count, sleep_pc, 0)

        # Create the dictionary used to output the data # TODO check to add 8
        stages_to_ignore = [
            self.get_stage_name_by_index('4'),
            self.get_stage_name_by_index('6'),
            self.get_stage_name_by_index('7'),
            self.get_stage_name_by_index('8')]

        export_stage_names = {
            "W":"W",
            "N1":"N1",
            "N2":"N2",
            "N3":"N3",
            "undefined":"Unscored",
            "R":"R",
            "NREM":"N1N2N3",
            "Sleep":"sleep"
        }

        mins = {}
        percents = {}
        distributions = {}
        for idx, stat in enumerate(stats):
            for label, (count, percent, distribution) in stat.items():
                if label not in stages_to_ignore:
                    export_name = export_stage_names[label]
                    if show_index:
                        mins[f"{prefix}{idx+1}_{export_name}_min"] = count * self.epo_to_min if sleep_length > 0 else None
                        percents[f"{prefix}{idx+1}_{export_name}_percent"] = percent * 100 if sleep_length > 0 else None
                        # Distribution for "sleep" makes no sense, we don't need to export that data
                        if label != "Sleep":
                            distributions[f"{prefix}{idx+1}_{export_name}_percent"] = distribution * 100 if distribution is not None else None
                    else:
                        mins[f"{prefix}_{export_name}_min"] = count * self.epo_to_min if sleep_length > 0 else None
                        percents[f"{prefix}_{export_name}_percent"] = percent * 100 if sleep_length > 0 else None
                        # Distribution for "sleep" makes no sense, we don't need to export that data
                        if label != "Sleep":
                            distributions[f"{prefix}_{export_name}_percent"] = distribution * 100  if distribution is not None else None
        return mins, percents, distributions

    def compute_wake_stats(self, sleep_period_stages, scored_stages, valid_sleep_stages):
        """ Compute all stats related to the wake stages during the sleep period

            Parameters:
            sleep_period_stages (array): list of sleep stages that composes the sleep period
            scored_stages (array): Array of scored sleep stages.
            valid_sleep_stages (array): Array of which stages are valid 
                (ex: for the Floyd and Feinberg option the valid stage are: N2,N3,REM)

            Returns:
            dict: A dictionary of all wakes stats.

        """
        wake_periods = []
        count = 0

        # Extract all continious wake period
        for stage in sleep_period_stages:
            if stage == '0':
                count = count + 1
            elif count > 0:
                wake_periods.append(count)
                count = 0

        # How many wake periods were longer than: 1min, 2min, 3min,4min, 5min
        wake_more_than_1 = [period for period in wake_periods if period >= 60 / self.epoch_length ]
        wake_more_than_2 = [period for period in wake_periods if period >= 60 / self.epoch_length * 2]
        wake_more_than_3 = [period for period in wake_periods if period >= 60 / self.epoch_length * 3]
        wake_more_than_4 = [period for period in wake_periods if period >= 60 / self.epoch_length * 4]
        wake_more_than_5 = [period for period in wake_periods if period >= 60 / self.epoch_length * 5]

        # How long was the sleep period, everything from the first sleep cycles 
        # to the last: NREM, REM, Wake, etc.
        sleep_period_duration = len(sleep_period_stages) * self.epo_to_min

        # How many minutes were spent awake during the sleep period 
        wake_duration = sleep_period_stages.count("0") * self.epo_to_min

        # # How many minutes spent in "Movement"
        # movement_duration = sleep_period_stages.count("6") * self.epo_to_min

        # How many minutes send in unscored stages
        undefined_duration =  (sleep_period_stages.count("9"))* self.epo_to_min
        
        # Sleep efficiency is defined as how long you slept during the sleep period
        if sleep_period_duration > 0:
            sleep_efficiency = self.get_actual_sleep_duration(sleep_period_stages)/sleep_period_duration
        else:
            sleep_efficiency = 0

        # Calcul how long is the last wake period.
        last_wake = 0
        for idx in range(len(scored_stages)-1, -1, -1):
            if scored_stages[idx] not in valid_sleep_stages:
                if scored_stages[idx] == '0':
                    last_wake = last_wake + 1
            else:
                break

        stats = {
            "total_W_count":len(wake_periods),
            "wake_1min_count":len(wake_more_than_1),
            "wake_2min_count":len(wake_more_than_2),
            "wake_3min_count":len(wake_more_than_3),
            "wake_4min_count":len(wake_more_than_4),
            "wake_5min_count":len(wake_more_than_5),
            "total_W_min":wake_duration,
            #"total_sleep_length_min":sleep_period_duration - wake_duration - movement_duration - undefined_duration,
            "total_sleep_min":sleep_period_duration - wake_duration - undefined_duration,
            "last_wake_min":last_wake * self.epo_to_min,
            "sleep_efficiency_percent":sleep_efficiency * 100, # Percent from decimal to %
            "sleep_period_min":sleep_period_duration,
            "Unscored_min":undefined_duration
        }
        
        return stats

    def get_actual_sleep_duration(self, sleep_stages):
        """ Get the actual sleep duration that happened during the sleep period.
            This is defined as the length of time spent in N1,N2,N3,N4 or REM 
            (everything but Wake stage) within the sleep period

            Parameters:
            sleep_stages (array): list of sleep stages that composes the sleep period

            Returns: 
            int: time spent actually sleeping within the sleep period.

        """
        # How long was the sleep period, everything from the first sleep cycles 
        # to the last: NREM, REM, Wake, etc.
        sleep_period_duration = len(sleep_stages) * self.epo_to_min

        # How many minutes were spent awake during the sleep period 
        wake_duration = (sleep_stages.count("0") + sleep_stages.count("9")) * self.epo_to_min

        # How many minutes were spent actually sleeping during the sleep period        
        actual_sleep_duration = sleep_period_duration - wake_duration

        return actual_sleep_duration

"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Compare two sets of events (1:gold standard events, 2:estimated events).
    The module computes the performance by event.
    These metrics are available : 
        fn : float
            False negative (event not detected)
        fp : float 
            False positive (wrong detection)
        tp : float
            True positive (event detected)
        tn : float
            True positive (correct non-detection)
        precision : float
            TP / (TP + FP) (proportion of valid detection)
        recall : float
            TP / (TP + FN) (proportion of events found) 
        f1 : float
            2 * (Precision  * Recall) / (Precision  + Recall) 
        (harmonic mean of precision and recall)
        kappa : float
            conservative agreement because the expected agreement is removed from the score
    
    Parameters
    -----------
        events1      : Pandas DataFrame
            The first set of events considered Gold Standard
        event1_name  : String
            Label of the first set of events
        events2      : Pandas DataFrame
            The second set of events considered estimation
        event2_name  : String
            Label of the second set of events
        channel1_name : String
            Channel label to filter events1 (select events only from that channel)
        channel2_name : String
            Channel label to filter events2 (select events only from that channel)
        filename     : String (optional)
            Filename to save performance evaluation
        jaccord_thresh : int
            Jaccord index threshold (similarity between events to be valid).

    Returns
    -----------    
        None
"""

from flowpipe import SciNode, InputPlug, OutputPlug

import os
import pandas as pd
import numpy as np

DEBUG = False

class PerformanceByEvent(SciNode):
    """
        Compare two sets of events (1:gold standard events, 2:estimated events).
        The class computes the performance by sample and the performance by event.

        Parameters
        -----------
            events1      : Pandas DataFrame
                The first set of events considered Gold Standard
            event1_name  : String
                Label of the first set of events
            events2      : Pandas DataFrame
                The second set of events considered estimation
            event2_name  : String
                Label of the second set of events
            channel1_name : String
                Channel label to filter events1 (select events only from that channel)
            channel2_name : String
                Channel label to filter events2 (select events only from that channel)
            filename     : String (optional)
                Filename to save performance evaluation
            jaccord_thresh : int
                Jaccord index threshold (similarity between events to be valid).

        Returns
        -----------    
            None
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('PerformanceByEvent.__init__')
        InputPlug('events1', self)
        InputPlug('event1_name', self)
        InputPlug('events2', self)
        InputPlug('event2_name', self)
        InputPlug('channel1_name', self)
        InputPlug('channel2_name', self)
        InputPlug('filename', self)
        InputPlug('jaccord_thresh', self)
        
        # Counter of sets of events if the plugin is called in a loop
        self._event_set_i = 1
        # List of filename used if the plugin is called in a loop
        self._filenames = []

    def subscribe_topics(self):
        pass


    def compute(self, events1, event1_name, events2, event2_name, channel1_name, \
        channel2_name, filename, jaccord_thresh):
        """
            Compare two sets of events (1:gold standard events, 2:estimated events).
            The class computes the performance by sample and the performance by event.
            
            Parameters
            -----------
                events1      : Pandas DataFrame
                    The first set of events considered Gold Standard
                event1_name  : String
                    Label of the first set of events
                events2      : Pandas DataFrame
                    The second set of events considered estimation
                event2_name  : String
                    Label of the second set of events
                channel1_name : String
                    Channel label to filter events1 (select events only from that channel)
                channel2_name : String
                    Channel label to filter events2 (select events only from that channel)
                filename     : String (optional)
                    Filename to save performance evaluation
                jaccord_thresh : int
                    Jaccord index threshold (similarity between events to be valid).

            Returns
            -----------    
                None
        """
        if DEBUG: print('PerformanceByEvent.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None          

        if event1_name=='': 
            event1_name = None
        if event2_name=='':
            event2_name = None

        if not jaccord_thresh=='':
            jaccord_thresh = float(jaccord_thresh)
        else:
            jaccord_thresh = None

        if isinstance(events1,pd.DataFrame) and isinstance(events2,pd.DataFrame):
            # Drop any event without channel information
            # Probably not event, but sleep stages
            events1 = events1.dropna(axis=0, how='any', inplace=False)
            events2 = events2.dropna(axis=0, how='any', inplace=False)

            tp = 0
            fp = 0
            detections = []
            border = 0
            for index, row in events2.iterrows():
                first_cond = events1[events1['start_sec'] >= row['start_sec']].index.tolist()
                second_cond = events1[(events1['start_sec'] + events1['duration_sec']) < (row['start_sec'] + row['duration_sec'])].index.tolist()
                events_index = list(set(first_cond) & set(second_cond))
                tp = tp + len(events_index)
                if len(events_index) == 0:
                    fp += 1
                else:
                    detections.append(events_index)
                left_border_first = events1[events1['start_sec'] < row['start_sec']].index.tolist()
                left_border_second = events1[(events1['start_sec'] + events1['duration_sec']) > row['start_sec']].index.tolist()
                left_index = list(set(left_border_first) & set(left_border_second))

                right_border_first = events1[events1['start_sec'] < (row['start_sec'] + row['duration_sec'])].index.tolist()
                right_border_second = events1[(events1['start_sec'] + events1['duration_sec']) > (row['start_sec'] + row['duration_sec'])].index.tolist()
                right_index = list(set(right_border_first) & set(right_border_second))
                border = border + len(left_index) + len(right_index)
                
            
            detections = np.hstack(detections)
            fn = len(events1) - len(detections)
            precision = tp / (tp + fp)
            recall = tp / (tp + fn)
            f1 = 2 * (precision  * recall) / (precision  + recall) 

            # Save performance in the cache to display it on the resultsView
            # Only last channel will be listed
            cur_perf_dict = {}
            cur_perf_dict['chan'] = channel1_name
            cur_perf_dict['Events expert'] = len(events1)
            cur_perf_dict['Events EOG_Rejection'] = len(events2)
            cur_perf_dict['False Negative'] = fn
            cur_perf_dict['False Positive'] = fp
            cur_perf_dict['True Positive'] = tp
            cur_perf_dict['Precision'] = precision
            cur_perf_dict['Recall'] = recall
            cur_perf_dict['Harmonic Mean'] = f1
            cur_perf_dict['Events on borders'] = border
        
            # Create a pandas DataFrame from the dict "cur_perf_dict"
            cache = pd.DataFrame.from_dict(cur_perf_dict, orient='index', \
                columns = [channel1_name + '_' + str(self._event_set_i)])
            cache.index.name = 'Performance' 

            # If the file already exist 
            if os.path.exists(filename):
                # if it's not the first loop, append data
                if filename in self._filenames:
                    # Read the existing csv
                    previous_df = pd.read_csv(filename, encoding='utf_8')
                    # Append new cache as column
                    previous_df[channel1_name + '_' + str(self._event_set_i)] = cache.values
                    try:
                        # Write the performance file
                        previous_df.to_csv(path_or_buf = filename, sep=',', \
                            header=True, index=False, index_label=False, encoding="utf_8")
                    except:
                        err_message = "ERROR: unable to write {}".format(filename)
                        self._log_manager.log(self.identifier, err_message)
                        print(err_message)                       
                else:
                    cache.to_csv(path_or_buf = filename, encoding="utf_8")
            else:
                if len(filename)>0:
                    try:
                        cache.to_csv(path_or_buf = filename, encoding="utf_8")
                    except:
                        err_message = "ERROR: unable to write {}".format(filename)
                        self._log_manager.log(self.identifier, err_message)
                        print(err_message)                     

                # To append data in the output file if there is another csv file or channel
                self._filenames.append(filename)

            # To mark the index of the file read
            self._event_set_i += 1

            # Write the cache
            # If the file already exist 
            if 'previous_df' in locals():
                perf_df = previous_df
            else:
                cache.reset_index(inplace=True)
                perf_df = cache
            self._cache_manager.write_mem_cache(self.identifier, perf_df)
        else:
            err_message = "ERROR: unexpected type for events"
            self._log_manager.log(self.identifier, err_message)
            print(err_message) 
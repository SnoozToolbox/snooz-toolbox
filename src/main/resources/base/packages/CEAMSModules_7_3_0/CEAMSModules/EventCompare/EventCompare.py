"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""

"""
    Compare two sets of events (1:gold standard events, 2:estimated events).
    The module computes the performance by sample and the performance by event.
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
        jaccord_thresh : float
            Jaccord index threshold (similarity between events to be valid).
        filename     : String (optional)
            Filename to save performance evaluation
        label       : string (optional)
            Label to add to the column when mutiple comparisons are made.

    Returns
    -----------    
        None
"""
import os
import pandas as pd
import numpy as np

from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from flowpipe import SciNode, InputPlug, OutputPlug
from CEAMSModules.EventCompare.performance import performance_by_sample, performance_by_event, compute_performance_from_stats

DEBUG = False
LOCAL_FS = 100 # to have a precision of 0.01 s on events 

class EventCompare(SciNode):
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
            events_valid_window : Pandas DataFrame
                The valid temporal window to expect events1 or events2.  Useful to compute the True Negative.
                i.e. the selected epochs from NREM sleep stage or R sleep stage.
            channel1_name : String
                Channel label to filter events1 (select events only from that channel)
            channel2_name : String
                Channel label to filter events2 (select events only from that channel)
            jaccord_thresh : float
                Jaccord index threshold (similarity between events to be valid).
            filename     : String (optional)
                Filename to save performance evaluation
            label       : string (optional)
                Label to add to the column when mutiple comparisons are made.

        Returns
        -----------    
            TP_events : Pandas DataFrame
                True positive events
            FNFP_events : Pandas DataFrame
                False Events

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('EventCompare.__init__')
        InputPlug('events1', self)
        InputPlug('event1_name', self)
        InputPlug('events2', self)
        InputPlug('event2_name', self)
        InputPlug('events_valid_window', self)
        InputPlug('channel1_name', self)
        InputPlug('channel2_name', self)
        InputPlug('jaccord_thresh', self)
        InputPlug('filename', self)
        InputPlug('label', self)
        OutputPlug('TP_events', self)
        OutputPlug('FNFP_events', self)
        

    def subscribe_topics(self):
        pass


    def compute(self, events1, event1_name, events2, event2_name, events_valid_window, channel1_name, \
        channel2_name, jaccord_thresh, filename, label):
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
                events_valid_window : Pandas DataFrame
                    The valid temporal window to expect events1 or events2.  Useful to compute the True Negative.
                    i.e. the selected epochs from NREM sleep stage or R sleep stage.
                channel1_name : String
                    Channel label to filter events1 (select events only from that channel)
                channel2_name : String
                    Channel label to filter events2 (select events only from that channel)
                jaccord_thresh : float
                    Jaccord index threshold (similarity between events to be valid).
                filename     : String (optional)
                    Filename to save performance evaluation
                label       : string (optional)
                    Label to add to the column when mutiple comparisons are made.

            Returns
            -----------    
                TP_events : Pandas DataFrame
                    True positive events
                FNFP_events : Pandas DataFrame
                    False Events
        """
        if DEBUG: print('EventCompare.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None          

        if not isinstance(events1,pd.DataFrame):
            raise NodeInputException(self.identifier, "events1", \
                f"EventCompare input of wrong type. Expected: <class 'pd.DataFrame'> received: {type(events1)}")       

        if not isinstance(events2,pd.DataFrame):
            raise NodeInputException(self.identifier, "events2", \
                f"EventCompare input of wrong type. Expected: <class 'pd.DataFrame'> received: {type(events2)}")     

        if event1_name=='': 
            event1_name = None
        else:
            events1 = events1[events1["name"]==event1_name]
        if event2_name=='':
            event2_name = None
        else:
            events2 = events2[events2["name"]==event2_name]

        if not jaccord_thresh=='':
            jaccord_thresh = float(jaccord_thresh)
        else:
            jaccord_thresh = None

        perf_cur_df = []
        TP_events = pd.DataFrame(data=None,columns=[\
            'group','name','start_sec','duration_sec','channels'])    
        FNFP_events = pd.DataFrame(data=None,columns=[\
            'group','name','start_sec','duration_sec','channels'])    

        # Create the unique list of channels
        events1_1chan_df = events1.copy()
        events2_1chan_df = events2.copy()
        chans1 = events1_1chan_df.channels.values
        chans2 = events2_1chan_df.channels.values
        channel_lst = np.unique(np.hstack((pd.unique(chans1),pd.unique(chans2)))).tolist()

        # If the user wants to filter for a specific channel only
        # Events from other channels will be filtered out
        if len(channel1_name)>0:
            channel_lst = [channel1_name]

        # Loop through channels 
        for i_chan in channel_lst:

            # Filter for the current channel (warning can have C3 and C3-OL in the same recording)
            # channels is always a list of a single channel and i_chan is always a string
            events1_chan_cur = events1_1chan_df[events1_1chan_df.channels==i_chan]
            if len(channel2_name)>0:
                events2_chan_cur = events2_1chan_df[events2_1chan_df.channels==channel2_name]
            else:
                events2_chan_cur = events2_1chan_df[events2_1chan_df.channels==i_chan]

            # Compute the performance by sample of estimated events against the gold standard events.
            # Here the GS is the events1
            fn, fp, tp, tn, precision, recall, f1, kappa, specificity, \
                npv, ppv, accuracy = performance_by_sample(
                events1_chan_cur, events2_chan_cur, LOCAL_FS)
            # The tn is computed on the whole time series between the first event and the last event.
            # adapt the tn based on events_valid_window
            if isinstance(events_valid_window,pd.DataFrame):
                if len(events_valid_window)>0:
                    n_tot_samples = events_valid_window.duration_sec.sum() * LOCAL_FS
                    # TODO make sure fp needs to be there
                    tn = int(n_tot_samples - tp - fp - fn)
                    precision, recall, f1, kappa, specificity, npv, ppv, accuracy = \
                            compute_performance_from_stats(fn, fp, tp, tn)

            # Compute the performance by event of estimated events against the gold standard (GS) events. 
            # Here the GS is the events1
            efn, efp, etp, eprecision, erecall, ef1, gs_evt_match, est_evt_match =\
                    performance_by_event(events1_chan_cur, events2_chan_cur, \
                    LOCAL_FS, overlap_thresh = jaccord_thresh)      
            
            TP_cur_events = events1_chan_cur.iloc[gs_evt_match==1]
            TP_events = pd.concat([TP_events,TP_cur_events])
            FN_cur_events = events1_chan_cur.iloc[gs_evt_match==0]
            FP_cur_events = events2_chan_cur.iloc[est_evt_match==0]
            FNFP_cur_events = pd.concat([FN_cur_events,FP_cur_events]) 
            FNFP_events = pd.concat([FNFP_events,FNFP_cur_events])           
                
            if DEBUG:
                print('For channel : {}'.format(i_chan))
                print(f'Performance per sample')
                print(f'fn:{fn}')
                print(f'fp:{fp}')
                print(f'tp:{tp}')
                print(f'tn:{tn}')
                print(f'precision:{precision}')
                print(f'recall:{recall}')
                print(f'f1:{f1}')
                print(f'kappa:{kappa}')
                print(f'specificity:{specificity}')
                print(f'npv:{npv}')
                print(f'ppv:{ppv}')
                print(f'accuracy:{accuracy}')

                print(f'Performance per event')
                print(f'efn:{efn}')
                print(f'efp:{efp}')
                print(f'etp:{etp}')
                print(f'eprecision:{eprecision}')
                print(f'erecall:{erecall}')
                print(f'ef1:{ef1}')
        
            # Save performance in the cache to display it on the resultsView
            # Only last channel will be listed
            cur_perf_dict = {}
            cur_perf_dict['channel'] = i_chan
            cur_perf_dict['FN-samples'] = fn
            cur_perf_dict['FP-samples'] = fp
            cur_perf_dict['TP-samples'] = tp
            cur_perf_dict['TN-samples'] = tn
            cur_perf_dict['precision-samples'] = precision
            cur_perf_dict['recall-samples'] = recall
            cur_perf_dict['f1-samples'] = f1
            cur_perf_dict['kappa-samples'] = kappa
            cur_perf_dict['specificity-samples'] = specificity
            cur_perf_dict['npv-samples'] = npv
            cur_perf_dict['ppv-samples'] = ppv
            cur_perf_dict['accuracy-samples'] = accuracy

            cur_perf_dict['FN-events'] = efn
            cur_perf_dict['FP-events'] = efp
            cur_perf_dict['TP-events'] = etp
            cur_perf_dict['precision-events'] = eprecision
            cur_perf_dict['recall-events'] = erecall
            cur_perf_dict['f1-events'] = ef1

            # Create a pandas DataFrame from the dict "cur_perf_dict"
            if len(label)>0 :
                column_name = label + '_' + i_chan 
                print(label)
            else:
                column_name = i_chan 
            perf_cur_df = pd.DataFrame.from_dict(cur_perf_dict, orient='index', \
                columns = [column_name])
            perf_cur_df.index.name = f'Performance (samples based on fs={LOCAL_FS} Hz)' 

            # If the file already exist 
            if os.path.exists(filename):
                # Read the existing csv
                previous_df = pd.read_csv(filename, sep='\t',encoding='utf_8', keep_default_na=False)
                # Append new performance as column
                previous_df[column_name] = perf_cur_df.values.flatten()
                try :
                    # Write the performance file
                    previous_df.to_csv(path_or_buf = filename, sep='\t', \
                        encoding="utf_8", header=True, index=False, index_label=False)
                except : 
                    error_message = f"ERROR : Snooz can not write in the file {filename}."+\
                        f"Check if the dive is accessible and the file is not already open."
                    raise NodeRuntimeException(self.identifier, "EventCompare", error_message)
            else:
                if len(filename)>0:
                    try :
                        perf_cur_df.to_csv(path_or_buf = filename, sep='\t', encoding="utf_8")
                    except :
                        error_message = f"ERROR : Snooz can not write in the file {filename}."+\
                            f"Check if the dive is accessible and the file is not already open."
                        raise NodeRuntimeException(self.identifier, "EventCompare", error_message)                        
                else:
                    error_message = f"ERROR : The output filename is not defined."
                    raise NodeRuntimeException(self.identifier, "EventCompare", error_message)                 


        # Write the performance
        # If the file already exist 
        if 'previous_df' in locals():
            self._cache_manager.write_mem_cache(self.identifier, previous_df)
        elif isinstance(perf_cur_df,pd.DataFrame):
            perf_cur_df.reset_index(inplace=True)
            self._cache_manager.write_mem_cache(self.identifier, perf_cur_df)
        
        return{
            'TP_events': TP_events,
            'FNFP_events': FNFP_events
        }

"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    ResetSignalArtefact
    To reset the signal that occurs during an artefact.
    This behavior is needed only for specific purpose, such as the TACS artefact for spindles.
    The signal is masked with NaN or forced to zero with a Turkey window (alpha=0.1) to smooth the edge.
    Smoothing the edges avoids additional glitch on the signal when forced directly to zero.
"""
import copy
import numpy as np
import pandas as pd
from scipy import signal as sci

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from flowpipe.ActivationState import ActivationState

from CEAMSModules.EventReader import manage_events
from CEAMSModules.PSGReader.SignalModel import SignalModel

DEBUG = False

class ResetSignalArtefact(SciNode):
    """
    To reset the signal that occurs during an artefact.

    Parameters
    -----------
        signals : a list of SignalModel
            signal.samples : The actual signal data as numpy list
            signal.sample_rate : the original  sampling rate of the signal
            signal.channel : current channel label
        events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
            Events to select based on the sleep stages.
        artefact_group: String
            Event group to reset signal, each group is separated by a comma, as a pattern occurrence.
        artefact_name: String
            Event name to reset signal, each name is separated by a comma, as a pattern occurrence.
        signal_values : String
            Signal values during artefact.
            0 : replace the artefacted signal values with zeros (with turkey mindow)
            NaN : replace the artefacted signal values with NaNs
        signal_copy : Boolean
        
    Returns
    -----------
        signals : a list of SignalModel
            signal.samples : The actual signal data as numpy list
            signal.sample_rate : the original  sampling rate of the signal
            signal.channel : current channel label
        
    """
    def __init__(self, **kwargs):
        """ Initialize module ResetSignalArtefact """
        super().__init__(**kwargs)
        if DEBUG: print('ResetSignalArtefact.__init__')

        # Input plugs
        InputPlug('signals',self)
        InputPlug('events',self)
        InputPlug('artefact_group',self)
        InputPlug('artefact_name',self)
        InputPlug('signal_values',self)

        # Output plugs
        OutputPlug('signals',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
        #self.alpha_turkey = 0.4 it does not make any sens on 30 sec
    

    def compute(self, signals, events, artefact_group, artefact_name, signal_values):
        """
        To reset (with interpolation) the signal that occurs during an artefact.

        Parameters
        -----------
            signals : a list of SignalModel
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the original  sampling rate of the signal
                signal.channel : current channel label
            events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels']) 
                Events to select based on the sleep stages.
            artefact_group: String
                Event group to reset signal, each group is separated by a comma, as a pattern occurrence.
            artefact_name: String
                Event name to reset signal, each name is separated by a comma, as a pattern occurrence.
            signal_values : String
                Signal values during artefact.
                0 : replace the artefacted signal values with zeros (with turkey mindow)
                NaN : replace the artefacted signal values with NaNs

        Returns
        -----------
            signals : a list of SignalModel
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the original  sampling rate of the signal
                signal.channel : current channel label
            
        """
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None    

        if not isinstance(signals,list):
            raise NodeInputException(self.identifier, "signals", \
                f"ResetSignalArtefact input of wrong type. Expected: <class 'list'> received: {type(signals)}")

        if not isinstance(events,pd.DataFrame):
            raise NodeInputException(self.identifier, "events", \
                f"ResetSignalArtefact input of wrong type. Expected: <class 'pd.DataFrame'> received: {type(events)}")            

        #signals_out = copy.deepcopy(signals)
        signals_out = signals

        # It is possible to bypass the "ResetSignalArtefact" by passing the input signals directly
        # to the output signals without any modification
        if self.activation_state == ActivationState.BYPASS:
            return {
                'signals': signals_out
            }        

        # Apply group and name selection. The user can define a single group or a single name. 
        # If group and name are defined, they must be defined in pairs.
        events_selected = manage_events.create_event_dataframe(None)
        if len(events)>0:
            if isinstance(artefact_group,str) and len(artefact_group)>0:
                group_lst = artefact_group.split(',')
            else:
                group_lst = []
            if isinstance(artefact_name,str) and len(artefact_name)>0:
                name_lst = artefact_name.split(',')
            else:
                name_lst = []
            if len(group_lst)==len(name_lst):
                for i, group_cur in enumerate(group_lst):
                    cur_selection = events[ (events['group']==group_cur) & (events['name']==name_lst[i]) ]
                    events_selected = pd.concat([events_selected,cur_selection])
            elif len(group_lst)>0 and len(name_lst)==0:
                for group_cur in group_lst:
                    group_selected = events[events['group']==group_cur]
                    events_selected = pd.concat([events_selected,group_selected])
            elif len(name_lst)>0 and len(group_lst)==0:
                for name_cur in name_lst:
                    name_selected = events[events['name'] == name_cur]
                    events_selected = pd.concat([events_selected,name_selected])
            else:
                raise NodeInputException(self.identifier, "artefact_group", \
                    f"ResetSignalArtefact input of wrong size. If both group and name are defined they need to be the same length, group length:\
                         {len(group_lst)} and name length: {len(name_lst)}")                  
            events_selected.sort_values('start_sec', axis=0, inplace=True, ignore_index='True')
            events_selected.reset_index(inplace=True, drop=True)    
            
            # Transform dataframe events start and duration into array
            start_times = events_selected['start_sec'].to_numpy().astype(float)
            duration_times = events_selected['duration_sec'].to_numpy().astype(float)
            channels = events_selected['channels'].to_numpy()

            # Easier to play with numpy array, signals_starttime and signals_endtime must have the same length as signals
            # Extract start_time of the signals as numpy array
            signals_starttime = SignalModel.get_attribute(signals, 'start_time', group_by=None)
            # Extract end_time of the signals as numpy array
            signals_endtime = SignalModel.get_attribute(signals, 'end_time', group_by=None)
            # Extract FS
            signals_fs = SignalModel.get_attribute(signals, 'sample_rate', group_by=None)

            # For each artefact
            for evt_start, evt_dur, channel in zip(start_times, duration_times, channels):
                # Find in which signal the artefact is included
                evt_start_in_signal = signals_starttime<(evt_start+evt_dur)
                evt_end_in_signal = signals_endtime>evt_start
                evt_sel_in_signal = evt_start_in_signal & evt_end_in_signal
                if sum(evt_sel_in_signal)>0:
                    signal_sel = list(np.nonzero(evt_sel_in_signal)[0])
                    for sel in signal_sel:
                        fs_sel = signals_fs[sel]
                        if signals_out[sel].channel == channel: # right channel
                            # Because of the discontinuity
                            # we have to verify if the signal includes at least partially the events
                            # Look for the Right windows time
                            if (signals_out[sel].start_time<=(evt_start+evt_dur)) and\
                                ((signals_out[sel].start_time+signals_out[sel].duration)>=evt_start):
                                start_i = int(round((evt_start - signals_out[sel].start_time) * signals_out[sel].sample_rate))
                                # stop_i<0: artefact ends after the signal
                                # stop_i>0: artefact ends before the signal
                                stop_i = int(round(( (signals_out[sel].start_time+signals_out[sel].duration) \
                                    - (evt_start+evt_dur) ) * signals_out[sel].sample_rate))
                                # Modify artefacted signal values
                                # artefact starts before the signal
                                if start_i<0:
                                    # artefact stop before the end of the signal
                                    if stop_i>0:
                                        real_stop_i = int(round((evt_start+evt_dur-signals_out[sel].start_time) * signals_out[sel].sample_rate))
                                        length_win = real_stop_i
                                        # we want a slope around 0.5 s as maximum for any artifact length
                                        alpha_turkey = 1/(length_win/fs_sel)
                                        if alpha_turkey>0.5:
                                            alpha_turkey=0.5
                                        if signal_values=='0':
                                            scaling_win = 1-(sci.windows.tukey(real_stop_i, alpha=alpha_turkey))
                                            scaling_win[0:int(round((length_win/2)*alpha_turkey))] = np.zeros(int(round((length_win/2)*alpha_turkey)))
                                            # First part of the scaling is reset since the artifact starts before
                                            signals_out[sel].samples[0:real_stop_i] = signals_out[sel].samples[0:real_stop_i]*scaling_win
                                        elif signal_values == 'NaN':
                                            nan_array = np.empty(real_stop_i)
                                            nan_array[:] = np.nan
                                            signals_out[sel].samples[0:real_stop_i] = nan_array
                                    # artefact stops after the end of the signal
                                    elif stop_i<0:
                                        if signal_values=='0':
                                            # no scaling the whole signal is an artifact
                                            signals_out[sel].samples = np.zeros(len(signals_out[sel].samples)) 
                                        elif signal_values == 'NaN':
                                            nan_array = np.empty(len(signals_out[sel].samples))
                                            nan_array[:] = np.nan                                        
                                            signals_out[sel].samples = nan_array
                                # artefact starts after the start of the signal
                                else:
                                    # artefact stop before the end of the signal
                                    if stop_i>0:
                                        real_stop_i = int(round((evt_start+evt_dur-signals_out[sel].start_time) * signals_out[sel].sample_rate))
                                        length_win = real_stop_i-start_i
                                        # we want a slope around 0.5 s as maximum for any artifact length
                                        alpha_turkey = 1/(length_win/fs_sel)
                                        if alpha_turkey>0.5:
                                            alpha_turkey=0.5
                                        if signal_values=='0':
                                            scaling_win = 1-(sci.windows.tukey(length_win, alpha=alpha_turkey))
                                            signals_out[sel].samples[start_i:real_stop_i] = \
                                                signals_out[sel].samples[start_i:real_stop_i]*scaling_win
                                        elif signal_values == 'NaN':
                                            nan_array = np.empty(length_win)
                                            nan_array[:] = np.nan
                                            signals_out[sel].samples[start_i:real_stop_i] = nan_array
                                    # artefact stop after the signal
                                    elif stop_i<0:
                                        length_win = len(signals_out[sel].samples)-start_i
                                        # we want a slope around 0.5 s as maximum for any artifact length
                                        alpha_turkey = 1/(length_win/fs_sel)
                                        if alpha_turkey>0.5:
                                            alpha_turkey=0.5                                        
                                        if signal_values=='0':
                                            #print(f"evt_start={evt_start}")
                                            scaling_win = 1-(sci.windows.tukey(length_win, alpha=alpha_turkey))
                                            start_slope_end = length_win-int(round(length_win/2*alpha_turkey))
                                            scaling_win[start_slope_end:] = np.zeros(int(round(length_win/2*alpha_turkey)))
                                            signals_out[sel].samples[start_i:] = signals_out[sel].samples[start_i:]*scaling_win
                                        elif signal_values == 'NaN':
                                            nan_array = np.empty(len(signals_out[sel].samples)-start_i)
                                            nan_array[:] = np.nan
                                            signals_out[sel].samples[start_i:] = nan_array
        else:
            # Log message for the Logs tab
            self._log_manager.log(self.identifier, "No events as input.")            
            return {
                'signals': signals_out
            }                  

        # Write to the cache to use the data in the resultTab
        cache = {}
        cache['events'] = events_selected
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'signals': signals_out
        }
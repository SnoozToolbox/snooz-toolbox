"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Manage a list of SignalModel from specific events during a recording.  

    The goal is to extract signals from events (segments : sleep stages or 
    clean segments for analysis). Could also be spindles.

    Create a new list of SignalModel based on the events (create = True), otherwise
    select items from the list of SignalModel based on the events (create = False).

    Parameters
    -----------
        signals : a list of SignalModel
            Each item of the list is a SignalModel object as described below:
                signal.samples : The actual signal data as numpy list
                signal.sample_rate : the sampling rate of the signal
                signal.channel : current channel label
                signal.start_time : The start time of the signal in sec
                signal.end_time : The end time of the signal in sec
                (for more info : look into common/SignalModel)
        events : pandas DataFrame
            df of events with field
            'group': Group of events this event is part of (String)
            'name': Name of the event (String)
            'start_sec': Starting time of the event in sec (Float)
            'duration_sec': Duration of the event in sec (Float)
            'channels' : Channel where the event occures (String)
            (For now events are expected to be on all channels)
        events_names : String
            String of the desired events to take in account. Separated by a 
            comma. ex)'stage_2' or ex)'stage_1,stage2,stage3'

    Returns
    -----------    
        signals_from_events : a list of SignalModel
            Each item is a SignalModel based on one item from events.
            (For now events are expected to be on all channels)
        epochs_to_process : pandas DataFrame
            df of events with field 
            'group': Group of events this event is part of (String)
            'name': Name of the event (String)
            'start_sec': Starting time of the event in sec (Float)
            'duration_sec': Duration of the event in sec (Float)
            'channels' : Channel where the event occures (String)
"""

from flowpipe import SciNode, InputPlug, OutputPlug
import config
from commons.NodeInputException import NodeInputException
from CEAMSModules.PSGReader.SignalModel import SignalModel
from CEAMSModules.EventReader.manage_events import create_event_dataframe
from CEAMSModules.PSGReader import commons

import numpy as np

DEBUG = False

class SignalsFromEvents(SciNode):
    """
        Manage a list of SignalModel from specific events during a recording.  

        The goal is to extract signals from events (segments : sleep stages or 
        clean segments for analysis). Could also be spindles.

        Create a new list of SignalModel based on the events (create = True), otherwise
        select items from the list of SignalModel based on the events (create = False).

        Parameters
        -----------
            signals : a list of SignalModel
                Each item of the list is a SignalModel object as described below:
                    signal.samples : The actual signal data as numpy list
                    signal.sample_rate : the sampling rate of the signal
                    signal.channel : current channel label
                    signal.start_time : The start time of the signal in sec
                    signal.end_time : The end time of the signal in sec
                    (for more info : look into common/SignalModel)
            events : pandas DataFrame
                df of events with field
                'group': Group of events this event is part of (String)
                'name': Name of the event (String)
                'start_sec': Starting time of the event in sec (Float)
                'duration_sec': Duration of the event in sec (Float)
                'channels' : Channel where the event occures (String)
                (For now events are expected to be on all channels)
            events_names : String
                String of the desired events to take in account. Separated by a 
                comma. ex)'stage_2' or ex)'stage_1,stage2,stage3'
            create : bool
                True to create a new list of SignalModel based on the events.
                False to select items from the list of SignalModel based on the events.

        Returns
        -----------    
            signals_from_events : a list of SignalModel
                Each item is a SignalModel based on one item from events.
                (For now events are expected to be on all channels)
            epochs_to_process : pandas DataFrame
                df of events with field 
                'group': Group of events this event is part of (String)
                'name': Name of the event (String)
                'start_sec': Starting time of the event in sec (Float)
                'duration_sec': Duration of the event in sec (Float)
                'channels' : Channel where the event occures (String)
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('SignalsFromEvents.__init__')
        self._filename = None
        InputPlug('signals', self)
        InputPlug('events', self)
        InputPlug('events_names', self)     
        InputPlug('create', self)
        OutputPlug('signals_from_events', self)
        OutputPlug('epochs_to_process', self)


    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass


    def compute(self, signals, events, events_names, create):
        """
        Manage a list of SignalModel from specific events during a recording.  

        The goal is to extract signals from events (segments : sleep stages or 
        clean segments for analysis) that are valid for all the channels.

        No check is made on the channel information, signals are extracted for 
        each selected event from the list. 

        Create a new list of SignalModel based on the events (create = True), otherwise
        select items from the list of SignalModel based on the events (create = False).

        Parameters
        -----------
            signals : a list of SignalModel
                Each item of the list is a SignalModel object as described below:
                    signal.samples : The actual signal data as numpy list
                    signal.sample_rate : the sampling rate of the signal
                    signal.channel : current channel label
                    signal.start_time : The start time of the signal in sec
                    signal.end_time : The end time of the signal in sec
                    (for more info : look into common/SignalModel)
            events : pandas DataFrame
                df of events with field
                'group': Group of events this event is part of (String)
                'name': Name of the event (String)
                'start_sec': Starting time of the event in sec (Float)
                'duration_sec': Duration of the event in sec (Float)
                'channels' : Channel where the event occures (String)
                (For now events are expected to be on all channels)
            events_names : String
                String of the desired events to take in account. Separated by a 
                comma. ex)'stage_2' or ex)'stage_1,stage2,stage3'
            create : bool
                True to create a new list of SignalModel based on the events.
                False to select items from the list of SignalModel based on the events.

        Returns
        -----------    
            signals_from_events : a list of SignalModel
                Each item is a SignalModel based on one item from events.
                (For now events are expected to be on all channels)
            epochs_to_process : pandas DataFrame
                df of events with field 
                'group': Group of events this event is part of (String)
                'name': Name of the event (String)
                'start_sec': Starting time of the event in sec (Float)
                'duration_sec': Duration of the event in sec (Float)
                'channels' : Channel where the event occures (String)
        """

        if DEBUG: print('SignalsFromEvents.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None             

        # Verify inputs
        if isinstance(signals,str) and signals=='':
            err_message = "ERROR: signals not connected"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals", \
                f"SignalsFromEvents this input is not connected.")
        if not isinstance(signals,list):
            err_message = "ERROR: signals unexpected type"
            self._log_manager.log(self.identifier, err_message)
            raise NodeInputException(self.identifier, "signals", \
                f"SignalsFromEvents input of wrong type. Expected: <class 'list'> received: {type(signals)}")
        elif isinstance(signals, list) and len(signals)==0:
            return {
                'signals_from_events': [],
                'epochs_to_process' : create_event_dataframe(None)
            }

        if isinstance(events, str) and events == '':
            err_message = "ERROR: events not connected"
            self._log_manager.log(self.identifier, err_message)
            return {
                'signals_from_events': signals,
                'epochs_to_process' : create_event_dataframe(None)
            }

        # split list to check on the events desired
        event_name = list(events_names.split(","))
        # Select events
        if (events_names == ''):
            events_to_write = events.copy()
        else:
            events_to_write = events.loc[events['name'].isin(event_name)].reset_index(drop=True).copy()   

        # Transform dataframe events start and duration into array
        if (events_names == ''):
            start_times = events['start_sec'].to_numpy().astype(float)
            duration_times = events['duration_sec'].to_numpy().astype(float)
            channel_times = events['channels'].to_numpy()
            event_groups = events['group'].to_numpy()
            event_names = events['name'].to_numpy()
        else:
            start_times = events.loc[events['name'].isin(event_name), 'start_sec'].to_numpy().astype(float)
            duration_times = events.loc[events['name'].isin(event_name), 'duration_sec'].to_numpy().astype(float)
            channel_times = events.loc[events['name'].isin(event_name), 'channels'].to_numpy()
            event_groups = events.loc[events['name'].isin(event_name),'group'].to_numpy()
            event_names = events.loc[events['name'].isin(event_name),'name'].to_numpy()

        if isinstance(create,str):
            try:
                create = eval(create)
            except :
                raise NodeInputException(self.identification, "create", "SignalsFromEvents create parameter must be set")
        if type(create) != bool :
            raise NodeInputException(self.identification, "create", "SignalsFromEvents create parameter must be set")

        if create==True:
            if DEBUG: 
                # Warn user of slower version
                warning_message = f"WARNING: not used in vectorization mode "+\
                    f"(discontinuity in the signals, events do not have the same length or "+\
                    f"channels do not have the same sampling rate)."
                self._log_manager.log(self.identifier, warning_message)
                print(warning_message)

            # Create my list of slice signals
            signals_from_events = []
            real_events_to_write = []
            for group, name, start, dur, chan in zip(event_groups, event_names, start_times, duration_times, channel_times):
                for j, signal in enumerate(signals):
                    # Convert time into samples to avoid rounding errors
                    evt_start_samples = int(np.round(start*signal.sample_rate))
                    evt_dur_samples = int(np.round(dur*signal.sample_rate))
                    evt_end_samples = evt_start_samples + evt_dur_samples
                    signal_start_samples = int(np.round(signal.start_time*signal.sample_rate))
                    signal_dur_samples = int(np.round(signal.duration*signal.sample_rate))
                    signal_end_samples = signal_start_samples + signal_dur_samples
                    # Because of the discontinuity
                    # we have to verify if the signal includes at least partially the events
                    # Look for the Right windows time
                    if len(chan)>0: # events are not applied to all channels (not a stage or a clean selection)
                        if (signal_start_samples<evt_end_samples) and (signal_end_samples>evt_start_samples) and (signal.channel == chan):
                            # Extract and define the new extracted channel_cur
                            channel_cur = self.extract_events_from_signal(signal, evt_start_samples, evt_dur_samples)
                            signals_from_events.append(channel_cur)
                        else:
                            channel_cur = None
                    elif (signal_start_samples<evt_end_samples) and (signal_end_samples>evt_start_samples): 
                        # Extract and define the new extracted channel_cur
                        channel_cur = self.extract_events_from_signal(signal, evt_start_samples, evt_dur_samples)
                        signals_from_events.append(channel_cur)
                    else:
                        channel_cur = None
                    if channel_cur is not None:
                        real_events_to_write.append([group, name, channel_cur.start_time, channel_cur.duration, chan])
                    # else:
                    #     # It is normal to miss some events if not all the channels have been selected.
                    #     # Log the missing event
                    #     self._log_manager.log(self.identifier, f'SignalFromEvents ERROR : event={group} {name} {chan} from {start} to {start + dur} is not found')
            events_to_write = create_event_dataframe(real_events_to_write)
            events_to_write.drop_duplicates(inplace=True,ignore_index=True)
        else:
            # If there is already multiple signal from event just filter the one in events
            if len(np.unique(SignalModel.get_attribute(signals, 'start_time', 'start_time'))) > 1:
                signals_from_events = [signal.clone(clone_samples=True) for signal in signals]
                i = 0
                signals_by_event = SignalModel.get_attribute(signals_from_events, None, 'start_time')
                start_by_event = np.unique(SignalModel.get_attribute(signals_from_events, 'start_time', 'start_time'), axis=1)
                dur_by_event = np.unique(SignalModel.get_attribute(signals_from_events, 'duration', 'start_time'),axis=1)
                for start, dur in zip(start_by_event, dur_by_event):
                    if not np.any(np.all(np.array([np.array(events_to_write['start_sec']) >= start,(np.array(events_to_write['start_sec']) + np.array(events_to_write['duration_sec'])) <= start + dur]), axis=0)):
                        signals_by_event = np.delete(signals_by_event,i,0)
                        i -= 1
                    i += 1
                signals_from_events = list(np.hstack(signals_by_event))
            else:
                raise NodeInputException(self.identifier, "create", \
                    f"SignalsFromEvents is instanciated (create=False) to use already splitted signals but there is only one item in signals")                

        # Extract the number of channels
        channel_lst = [signal.channel for signal in signals]
        n_chan = len(np.unique(np.array(channel_lst)))

        # Write the cache
        cache = {}
        if config.is_dev: # Avoid save of the recording when not developping
            cache['n_chan'] = n_chan
            cache['signals'] = signals_from_events
            self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'signals_from_events': signals_from_events,
            'epochs_to_process': events_to_write
        }


    def extract_events_from_signal(self, signal, evt_start_samples, evt_dur_samples):
        """
        Parameters :
            signal : SignalModel object
                signal with channel, samples, sample_rate...
            evt_start_samples : float
                start in samples of the signal
            dur : float
                duration in samples of the signal
        Return : 
            signal modified (truncated) to extract the samples linked to the event specified by start and dur
        """
        channel_cur = signal.clone(clone_samples=False)
        # Because of the discontinuity, the signal can start with an offset (second section)
        signal_start_samples = int(np.round(signal.start_time * channel_cur.sample_rate))
        signal_dur_samples = int(np.round(signal.duration * signal.sample_rate))
        signal_end_samples = signal_start_samples + signal_dur_samples

        # if the event starts before the signal, we cut the signal
        if evt_start_samples < signal_start_samples:
            channel_cur.start_time = signal.start_time
            chan_start_samples = signal_start_samples
        else:
            channel_cur.start_time = evt_start_samples/channel_cur.sample_rate
            chan_start_samples = evt_start_samples
        # if the event ends after the signal, we cut the signal
        if (evt_start_samples + evt_dur_samples) > signal_end_samples:
            channel_cur.end_time = signal.end_time
            chan_end_samples = signal_end_samples
        else:
            channel_cur.end_time = (evt_start_samples + evt_dur_samples)/channel_cur.sample_rate
            chan_end_samples = evt_start_samples + evt_dur_samples
        channel_cur.duration = channel_cur.end_time - channel_cur.start_time

        # The offset of the signal is removed to extract the event
        channel_cur.samples = signal.samples[chan_start_samples-signal_start_samples:chan_end_samples-signal_start_samples]
        if len(channel_cur.samples)==0:
            self._log_manager.log(self.identifier, f'SignalFromEvents ERROR : event={evt_start_samples/channel_cur.sample_rate} to {(evt_start_samples + evt_dur_samples)/channel_cur.sample_rate} and signal={signal.start_time} to {signal.end_time}')
        return channel_cur
        
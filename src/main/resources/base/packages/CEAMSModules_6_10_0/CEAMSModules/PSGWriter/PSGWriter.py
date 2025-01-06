"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Write a PSG file. This module doesn't create a new file, it opens an existing
    file [input_filename] and modify it with the signals and events received in input.

    Parameters
    -----------
        input_filename :   String
            The name of the input file
        output_filename :  String
            The name of the output file to write. 
        signals : List of SignalModel
            Signals to write to a file
        new_events :  pandas DataFrame columns=['group','name','start_sec','duration_sec','channels']
            New events to write to a file.
        events_to_remove : list of tuple of n events to remove.
            Events group and name to remove from the file.
            ex. [('group1', 'name1'), ('group2', 'name2')]
        overwrite_events :   bool
            True to overwrite old events with the same group and name as the new ones.
        overwrite_signals :  bool
            True to overwrite signals that's been modified

    Returns
    -----------  
        None
"""
import pandas as pd

from commons.NodeInputException import NodeInputException
from flowpipe import SciNode, InputPlug
from CEAMSModules.PSGReader.PSGReaderManager import PSGReaderManager

DEBUG = False

class PSGWriter(SciNode):
    """
        Write a PSG file. 
        The PSG signals are always in a file separated from the annotations file containning the events.
        The setting (bool flag) "overwrite_signals" allows to overwrite the signal and "overwrite_events" allows to overwrite the events.
        If input_filename and output_filename are the same, the PSG file will be overwritten when overwrite_signals is True and
        the annotations file will be overwritten when overwrite_events is True.

        Parameters
        -----------
            input_filename :   String
                The name of the input file
            output_filename :  String
                The name of the output file to write. 
            signals : List of SignalModel
                Signals to write to a file
            events_to_remove : list of tuple of n events to remove.
                Events group and name to remove from the file.
                ex. [('group1', 'name1'), ('group2', 'name2')]
            new_events :  pandas DataFrame columns=['group','name','start_sec','duration_sec','channels']
                New events to write to a file.
            overwrite_events :   bool
                True to overwrite old events with the same group and name as the new ones.
            overwrite_signals :  bool
                True to overwrite signals that's been modified

        Returns
        -----------  
            None
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('PSGWriter.__init__')
        self._psg_reader_manager = PSGReaderManager()
        self._psg_reader_manager._init_readers()

        InputPlug('input_filename', self)
        InputPlug('output_filename', self)
        InputPlug('signals', self)
        InputPlug('new_events', self)
        InputPlug('events_to_remove', self)
        InputPlug('overwrite_events', self)
        InputPlug('overwrite_signals', self)
        

    def subscribe_topics(self):
        pass


    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'PSGWriter.on_topic_update {topic}:{message}')


    def compute(self, input_filename, output_filename, signals, new_events, events_to_remove, overwrite_events, overwrite_signals):
        """
            Write a PSG file. 
            The PSG signals are always in a file separated from the annotations file containning the events.
            The setting (bool flag) "overwrite_signals" allows to overwrite the signal and "overwrite_events" allows to overwrite the events.
            If input_filename and output_filename are the same, the PSG file will be overwritten when overwrite_signals is True and
            the annotations file will be overwritten when overwrite_events is True.

            Parameters
            -----------
                input_filename :   String
                    The name of the input file
                output_filename :  String
                    The name of the output file to write. 
                signals : List of SignalModel
                    Signals to write to a file
                new_events :  pandas DataFrame columns=['group','name','start_sec','duration_sec','channels']
                    New events to write to a file.
                events_to_remove : list of tuple of n events to remove.
                    Events group and name to remove from the file.
                    ex. [('group1', 'name1'), ('group2', 'name2')]
                overwrite_events :   bool
                    True to overwrite old events with the same group and name as the new ones.
                overwrite_signals :  bool
                    True to overwrite signals that's been modified

            Returns
            -----------  
                None
        """
        if DEBUG: print('PSGWriter.compute')

        if input_filename == '':
            raise NodeInputException(self.identifier, "input_filename", \
                "PSGWriter input_filename parameter must be set.")

        if output_filename == '':
            raise NodeInputException(self.identifier, "output_filename", \
                "PSGWriter output_filename parameter must be set.")

        if isinstance(overwrite_events, str):
            try : 
                overwrite_events = eval(overwrite_events)
            except : 
                raise NodeInputException(self.identifier, "overwrite_events", \
                    "PSGWriter overwrite_events parameter must be set.")                
        if type(overwrite_events) != bool:
            raise NodeInputException(self.identifier, "overwrite_events", \
                "PSGWriter overwrite_events parameter must be set.")

        if isinstance(overwrite_signals, str):
            try : 
                overwrite_signals = eval(overwrite_signals)
            except : 
                raise NodeInputException(self.identifier, "overwrite_signals", \
                    "PSGWriter overwrite_signals parameter must be set.")                
        if type(overwrite_signals) != bool:
            raise NodeInputException(self.identifier, "overwrite_signals", \
                "PSGWriter overwrite_signals parameter must be set.")

        if isinstance(events_to_remove, str) and (len(events_to_remove)>0):
            events_to_remove = eval(events_to_remove)
            if not isinstance(events_to_remove, list):
                raise NodeInputException(self.identifier, "events_to_remove", \
                    f"PSGWriter events_to_remove type is {type(events_to_remove)} and list is expected.")                

        if output_filename != input_filename:
            self._psg_reader_manager.copy_file(input_filename, output_filename)

        is_opened = self._psg_reader_manager.open_file(output_filename)

        if not is_opened:
            self._log_manager.log(self.identifier, f'ERROR PSGWriter could not open file: {output_filename}')
            return

        # If there is new events
        if isinstance(new_events, pd.DataFrame):

            # We need to overwrite old events.
            if overwrite_events:
                # Assemble all unique combinaison of group_name:event_name
                events_to_replace = set()
                for index, event in new_events.iterrows():
                    event_name = event['name']
                    group_name = event['group']
                    events_to_replace.add((group_name, event_name))
                # Remove these combinaison from the file
                for (group_name, event_name) in events_to_replace:
                    self._psg_reader_manager.remove_events_by_name(event_name, group_name)

            # Remove events_to_remove
            if len(events_to_remove)>0:
                for group_name, event_name in events_to_remove:
                    self._psg_reader_manager.remove_events_by_name(event_name, group_name)            

            # Add the new events
            for index, event in new_events.iterrows():
                montage_index = self.get_montage_index(signals, event['channels'])
                self._psg_reader_manager.add_event(
                    name=           event['name'],
                    group=          event['group'],
                    start_sec=      event['start_sec'],
                    duration_sec=   event['duration_sec'],
                    channels=       event['channels'],
                    montage_index=  montage_index)
            
            # Write the events in the cache in order to view them on the resultsView
            if new_events is not None:
                cache = {}
                cache['events'] = new_events
                self._cache_manager.write_mem_cache(self.identifier, cache)
        
        if overwrite_signals:
            any_signal_modified = False
            if signals is not None and signals != '':
                for i, signal_model in enumerate(signals):
                    if signal_model.is_modified:
                        any_signal_modified = True
                        break

                if any_signal_modified:
                    self._psg_reader_manager.save_signals(signals)
        
        self._psg_reader_manager.save_file()
        self._psg_reader_manager.close_file()

        return None


    def get_montage_index(self, signals, channels):
        if signals is None or signals == '' or channels is None or channels == '':
            return -1
        for i, signal_model in enumerate(signals):
            if signal_model.channel == channels:
                return signal_model.montage_index
        
        return -1

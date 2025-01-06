"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
import os
from os import listdir
from os.path import isfile, join
import importlib.util
import numpy as np
import pandas as pd
import traceback
import shutil

import config
from CEAMSModules.PSGReader.SignalModel import SignalModel
from . import commons

"""
    
"""
class PSGReaderManager:
   
    def __init__(self):
        self.current_reader = None
        self.current_filename = None
        self.extensions = {}
        self.extensionsFilters = {}

    def _init_readers(self):
        ''' Static function called once to init all readers '''
        # Get the path where PSGReader librairies are stored. 
        readers_path = config.app_context.get_resource(join('extension','PSGReader'))

        # Discard the subfolders, only get the filename
        readers_filenames = [f for f in listdir(readers_path) if isfile(join(readers_path, f))]
        
        for filename in readers_filenames:
            try:
                ext_pos = filename.find('.')

                # Discard the file extension
                module_name = filename[:ext_pos]

                module_path = join(readers_path, filename)
                spec = importlib.util.spec_from_file_location(module_name, module_path)

                if spec is not None:
                    module = importlib.util.module_from_spec(spec)
                    if module is not None:
                        spec.loader.exec_module(module)

                        reader_class = getattr(module, module_name)
                        reader = reader_class()
                        
                        ext = reader.get_extensions()
                        ext_filters = reader.get_extensions_filters()
                        for i, e in enumerate(ext):
                            if e in self.extensions:
                                print(f"PSGReaderManager: ERROR File extension:{e} already registered by the class:{PSGReaderManager.extensions[e].__name__}")
                            else:
                                self.extensions[e] = reader_class
                                self.extensionsFilters[e] = ext_filters[i]
                    else:
                        print(f"ERROR Can\'t load module:{module_name} path:{module_path}")
                else:
                    print(f"ERROR Can\'t load module:{module_name} path:{module_path}")
            except:
                # TODO add message to log manager
                traceback.print_exc()


    def get_file_extensions_filters(self):
        filters = list(self.extensionsFilters.values())

        extenstions = self.get_file_extensions()
        all_filters = 'PSG files (' + ''.join([f'*.{ext} ' for ext in extenstions]) + ')'
        filters.insert(0, all_filters)
        
        return filters


    def get_file_extensions(self):
        return list(self.extensions.keys())


    def get_reader_class_by_extension(self,ext):
        ext = ext.lower()
        if ext in self.extensions:
            return self.extensions[ext]
        else:
            return None


    ### Member functions
    def open_file(self, filename):
        _, extension = os.path.splitext(filename)
        reader_class = self.get_reader_class_by_extension(extension[1:]) # [1:] remove the dot from the extension ".sts" -> "sts"
        if reader_class is None:
            print(f'ERROR PSGReaderManager could not find reader for extension file:{extension}')
            return False
        
        self.current_reader = reader_class()
        success = self.current_reader.open_file(filename)
        
        if not success:
            print(f'ERROR PSGReaderManager could not open file:{filename}')
            return False

        self.current_filename = filename
        return True


    def copy_file(self, source_filename, dest_filename):
        _, extension = os.path.splitext(source_filename)
        reader_class = self.get_reader_class_by_extension(extension[1:]) # [1:] remove the dot from the extension ".sts" -> "sts"
        if reader_class is None:
            print(f'ERROR PSGReaderManager could not find reader for extension file:{extension}')
            return False
        reader = reader_class()
        
        # Check if the reader has implemented the copy_file function
        # if not, simply copy the file using shutil.copy2.
        copy_file = getattr(reader, "copy_file", None)
        if callable(copy_file):
            copy_file(source_filename, dest_filename)
        else:
            shutil.copy2(source_filename, dest_filename)


    def get_montages(self):
        if self.current_reader is None:
            print(f'ERROR PSGReaderManager.get_montages file not loaded')
            return
        return self.current_reader.get_montages()


    def get_channels(self, montage_index):
        if self.current_reader is None:
            print(f'ERROR PSGReaderManager.get_channels file not loaded')
            return
        channels = self.current_reader.get_channels(montage_index)

        signal_models = []
        for channel in channels:
            signal_model = SignalModel()
            signal_model.name = channel.name
            signal_model.sample_rate = channel.sample_rate
            signal_models.append(signal_model)

        return signal_models


    def create_signal_model(self, montage_index, channel):
        if self.current_reader is None:
            print(f'ERROR PSGReaderManager.create_signal_model file not loaded')
            return
        channels = self.current_reader.get_channels(montage_index)
        
        for ch in channels:
            if ch.name == channel:

                signal_model = SignalModel()
                signal_model.name = ch.name
                signal_model.sample_rate = ch.sample_rate
                signal_model.montage_index = montage_index
                return signal_model

        return None


    def get_event_groups(self):
        if self.current_reader is None:
            print(f'ERROR PSGReaderManager.get_event_groups file not loaded')
            return
        return self.current_reader.get_event_groups()


    def get_events(self):
        """
            get_events
            Get events from a PSG reader.
            The format of must be a list of object containing the following variable:
                channels: A list of string for each channel this event is related to.
                name: The name of the event
                group: The group name of the event
                start_time: The start_time of the event
                duration: The duration of the event. None if the event has no duration.
        """
        if self.current_reader is None:
            print(f'ERROR PSGReaderManager.get_events file not loaded')
            return

        eventsObj = self.current_reader.get_events()

        if isinstance(eventsObj, pd.DataFrame):
            events_df = eventsObj
        else:
            events =    []
            for event in eventsObj:
                events.append({
                    'group':event.group,
                    'name': event.name, 
                    'start_sec': event.start_time, 
                    'duration_sec': event.duration, 
                    'channels': event.channels})
            # Convert the list of dicts into a DataFrame
            events_df = pd.DataFrame(events)
        # Clean up lists of channels for a single channel (string) per event
        events_df = self.convert_event_df_to_single_channel(events_df)
        # In NATUS/Stellate the annotations can be duplicated
        events_df.drop_duplicates(inplace=True, ignore_index=True)
        return events_df


    def close_file(self):
        if self.current_reader is None:
            print(f'ERROR PSGReaderManager.close_file file not loaded')
            return
        self.current_reader.close_file()
        self.current_reader = None
        self.current_filename = None


    def save_file(self):

        if self.current_reader is None:
            print(f'ERROR PSGReaderManager.save_file file not loaded')
            return
        self.current_reader.save_file()


    def get_signal_models(self, montage_index, channel_names):
        if self.current_reader is None:
            print(f'ERROR PSGReaderManager.get_signal_by_names file not loaded')
            return None

        signal_models = []
        section_count = self.current_reader.get_signal_section_count()
        for i in range(section_count):
            signals = self.current_reader.get_signal_section(montage_index, channel_names, i)
            
            for signal in signals:

                signal_model = SignalModel()
                if isinstance(signal.samples, np.ndarray):
                    signal_model.samples = signal.samples
                else:
                    signal_model.samples = np.array(signal.samples)
                signal_model.start_time = signal.start_time
                signal_model.end_time = signal.end_time
                signal_model.duration = signal.duration
                signal_model.sample_rate = signal.sample_rate
                signal_model.channel = signal.channel
                signal_model.montage_index = montage_index

                signal_models.append(signal_model)

        return signal_models


    def get_sleep_stages(self):
        if self.current_reader is None:
            print(f'ERROR PSGReaderManager.get_sleep_stages file not loaded')
            return None

        df_label =  ['start_sec', 'duration_sec', 'channels']
        stages =    self.current_reader.get_sleep_stages()
        events =    []

        if isinstance(stages, pd.DataFrame):
            # Clean up lists of channels for a single channel (string) per event
            channels = [""]
            channels = channels * len(stages)
            stages.loc[:,'channels'] = channels
            return stages

        for stage in stages:
            name =          f'{stage.sleep_stage}'
            start_time =    stage.start_time
            duration =      stage.duration
            channels =      ""
            events.append({
                'group': commons.sleep_stages_group,
                'name': name, 
                df_label[0]: start_time, 
                df_label[1]: duration, 
                df_label[2]: channels})

        return pd.DataFrame(events)


    def add_event(self, name, group, start_sec, duration_sec, channels, montage_index):
        if self.current_reader is None:
            print(f'ERROR PSGReaderManager.add_event file not loaded')
            return False
        # The input channels is always a string of a single channel
        # channels has to be a list of string for the current_reader
        channels = [channels]       
        # HarmonieReader asks for those arguments arg0: str, arg1: str, arg2: float, arg3: float, arg4: List[str], arg5: int
        success = self.current_reader.add_event(name, group, start_sec, duration_sec, channels, montage_index)
        if not success:
            error = self.current_reader.get_last_error()
            print(error)
        return success


    def remove_events_by_group(self, group):
        if self.current_reader is None:
            print(f'ERROR PSGReaderManager.remove_events_by_group file not loaded')
            return False
        success = self.current_reader.remove_events_by_group(group)
        if not success:
            error = self.current_reader.get_last_error()
            print(error)
        return success


    def remove_events_by_name(self, event_name, group_name):
        if self.current_reader is None:
            print(f'ERROR PSGReaderManager.remove_events_by_group file not loaded')
            return False
        success = self.current_reader.remove_events_by_name(event_name, group_name)
        if not success:
            error = self.current_reader.get_last_error()
            print(error)
        return success


    def save_signals(self, signals):
        if self.current_reader is None:
            print(f'ERROR PSGReaderManager.save_signals file not loaded')
            return None

        try:
            self.current_reader.save_signals(signals)
        except AttributeError as e:
            print('WARNING This reader has no save_signal function' + e)
    

    def get_subject_info(self):
        if self.current_reader is None:
            print(f'ERROR PSGReaderManager.save_signals file not loaded')
            return None

        si = self.current_reader.get_subject_info()
        
        basename = os.path.basename(self.current_filename)
        file_without_ext, _ = os.path.splitext(basename)
        
        subject_info = {
            "filename":file_without_ext,
            "id1":si.id,
            "id2":None,
            "first_name":si.firstname,
            "last_name":si.lastname,
            "sex":si.sex,
            "birthdate":si.birth_date,
            "creation_date":si.creation_date,
            "age":si.age,
            "height":None,
            "weight":None,
            "bmi":None,
            "waistline":None,
            "height_unit":None,
            "weight_unit":None,
            "waistline_unit":None
        }

        return subject_info


    def find_psg_within_folder(self, folder_path):
        files = [folder_path + '/' + f for f in listdir(folder_path) if isfile(folder_path + '/' + f)]
        valid_file_extensions = self.get_file_extensions()
        valid_file_extensions = [string.lower() for string in valid_file_extensions]
        
        psg_files = []
        for file in files:
            _, file_extension = os.path.splitext(file)
            if file_extension[1:].lower() in valid_file_extensions:
                psg_files.append(file)

        return psg_files


    def convert_event_df_to_single_channel(self, events1):
        """
            Clean up lists of channels for a single channel
            Duplicate events with more than one channels
            Events without channel are skipped

            Parameters:
                events1 : pandas DataFrame with columns : group, name, start_sec, duration_sec, channels
                List of events. An event can be spread on many channels.

            Return:
                event_df_single_chan : pandas DataFrame with columns : group, name, start_sec, duration_sec, channels
                List of events with a single channel in the column "channels"

        """
        # Look for lists of channels with more than a single channel
        channels = events1['channels'].values
        index_many_chans = [i for i, chan_lst in enumerate(channels) if len(chan_lst)>1]
        
        # Convert the list of a single channel into a string
        if len(index_many_chans)>0:
            events1_single = events1.drop(index_many_chans)
            channels = events1_single['channels'].values
        else:
            events1_single = events1
        channels_string = [chan_lst[0] if len(chan_lst)>0 else "" for chan_lst in channels]
        events1_single.loc[:,'channels'] = channels_string

        # Duplicate events spread on more than one channels
        if len(index_many_chans)>0:
            events1_many = events1.iloc[index_many_chans]
            single_chan_events1 = []
            for index, event in events1_many.iterrows():
                if len(event.channels)>0:
                    for i_chan in range(len(event.channels)):
                        single_chan_events1.append([event['group'],event['name'],event['start_sec'], event['duration_sec'], event.channels[i_chan]])
            event_df_single_chan = pd.DataFrame(data=single_chan_events1,columns=['group','name','start_sec','duration_sec','channels'])
            events1_single = pd.concat([events1_single,event_df_single_chan])
        return events1_single
    
    def get_montage_index(self, montage_name):
        montages = self.get_montages()
        for montage in montages:
            if montage.name == montage_name:
                return montage.index
        return None
    
    def get_last_error(self):
        if self.current_reader is None:
            print(f'ERROR PSGReaderManager.get_last_error file not loaded')
            return None
        return self.current_reader.get_last_error()
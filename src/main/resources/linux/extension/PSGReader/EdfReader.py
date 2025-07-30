"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
from ast import literal_eval
from datetime import datetime
import locale
import math
import numpy as np
import pyedflib
import pandas as pd
import os
import re
import shutil
import time
from types import SimpleNamespace

from CEAMSModules.EventReader import manage_events
from CEAMSModules.PSGReader import commons
from commons.NodeRuntimeException import NodeRuntimeException

class EdfSubjectInfo:
    def __init__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.sex = None
        self.birth_date = None
        self.creation_date = None
        self.age = None
        self.height = None
        self.weight = None
        self.bmi = None
        self.waist_size = None      

class EdfMontage:
    def __init__(self):
        self.name = None
        self.index = None
        
class EdfChannelModel:
    def __init__(self):
        self.name = None
        self.samples = None
        self.alias = None
        self.sample_rate = 0
        self.start_time = 0

class LunaFile:
    def __init__(self):
        self._filename = None
        self._df_label =  ['group', 'name', 'start_sec', 'duration_sec', 'channels']
        self._annotations = pd.DataFrame([], columns=self._df_label)

    def open_file(self, basename):
        self._filename = None
        luna_tsv_filename = basename + '.tsv'
        luna_txt_filename = basename + '.txt'
        
        if os.path.isfile(luna_tsv_filename):
            self._filename = luna_tsv_filename
        elif os.path.isfile(luna_txt_filename):
            self._filename = luna_txt_filename

        if self._filename is not None:
            with open(self._filename, 'r', encoding='utf_8') as f:
                header_line = f.readline().strip()
                header_cols = header_line.split('\t')
            if "time elapsed(HH:MM:SS)" in header_cols:
                usecols = [col for col in header_cols if col in self._df_label]
            else:
                usecols = self._df_label
            self._annotations = pd.read_csv(self._filename, header=0, encoding='utf_8', \
                names=usecols, sep ='\t', usecols=range(len(self._df_label)), converters={0:str, 1:str, 2:float, 3:float}) 
            
            # Strip @@chan if any
            ori_n_evt = len(self._annotations)
            name_data = np.hstack(self._annotations['name'].values).tolist()
            name = [list(new_name.split("@@"))[0] if (isinstance(new_name,str) and '@@' in new_name) else new_name for new_name in name_data]
            if not (len(name)==ori_n_evt):
                raise NodeRuntimeException(self.identifier, self._filename,\
                    f"EdfReader event name are corrupted.")
            else:
                # Really important to avoid self._annotations.loc[:]['name']
                #   The data may be not modified
                self._annotations.loc[:,'name'] = name 
                # Snooz supports an event occurring on multiple channels
                #   convert the string of channels list into a python list
                #   if the string does not include a list, we create it for compatibility.
                self._annotations['channels'] = (self._annotations['channels'].apply(lambda x: self.convert_to_list(x)))
        else:
            self._filename = luna_tsv_filename

    def convert_to_list(self, x):
        try:
            return literal_eval(x)
        except:
            return [x]

    def clear_events(self):
        self._annotations = pd.DataFrame()

    def add_event(self, name, group, start_sec, duration_sec, channels):
        current_df = manage_events.create_event_dataframe([[group, name, start_sec, duration_sec, channels]])
        self._annotations = pd.concat([self._annotations, current_df], ignore_index=True)

    def add_events(self, events):
        new_events_df = manage_events.create_event_dataframe(events)
        self._annotations = pd.concat([self._annotations, new_events_df], ignore_index=True)
        self._annotations.sort_values(by=['start_sec'], inplace=True)

    def remove_events_by_group(self, group_name):
        if len(self._annotations) == 0:
            return
        # Filter out all annotation that has a name equal to the group_name
        self._annotations = self._annotations[self._annotations.group != group_name]

    def remove_events_by_name(self, event_name, group_name):
        # Remove out all events that has a event name equal to the event_name and 
        # group name equals to group_event.

        if len(self._annotations) == 0:
            return
        self._annotations = self._annotations[~((self._annotations.name == event_name) &
            (self._annotations.group == group_name))]

    def get_sleep_stages(self):
        return self._annotations[self._annotations['group'] == commons.sleep_stages_group]
        
    @property
    def annotations(self):
        return self._annotations
    
    def save_file(self):
        if self._filename is None:
            return
        
        if len(self._annotations) > 0:
            self._annotations = self._annotations.sort_values(by=['start_sec'])
            event_name_all = []
            for index, event in self._annotations.iterrows():
                current_chan = event["channels"]
                if isinstance(current_chan,list):
                    if len(current_chan)==1:
                        if len(current_chan[0])>0:
                            event["name"] = event["name"]+"@@"+current_chan[0]
                elif isinstance(current_chan,str):
                    if len(current_chan)>0:
                        # If a string of list
                        if '[' in current_chan:
                            current_chan = eval(current_chan)
                            if len(current_chan)>0:
                                event["name"] = event["name"]+"@@"+current_chan[0]
                        else:
                            event["name"] = event["name"]+"@@"+current_chan
                event_name_all.append(event["name"])
            self._annotations["name"] = event_name_all
            time_elapsed_df = pd.DataFrame()
            # Compute the time elapsed for each event
            time_elapsed_df["HH"] = (np.floor(self._annotations['start_sec']/3600)).astype(int)
            time_elapsed_df["MM"] = ( np.floor( (self._annotations['start_sec']-time_elapsed_df["HH"]*3600) / 60 )).astype(int)
            time_elapsed_df["SS"] = self._annotations['start_sec']-time_elapsed_df["HH"]*3600 - time_elapsed_df["MM"]*60

            # concatenate the time as HH:MM:SS and add it to the events dataframe
            self._annotations['time elapsed(HH:MM:SS)'] = time_elapsed_df.HH.apply(str)\
                    + ':' + time_elapsed_df.MM.apply(str) + ':' + time_elapsed_df.SS.apply(str)
            
            self._annotations.to_csv(self._filename, index=False, header=self._df_label + ['time elapsed (HH:MM:SS)'], sep ='\t',encoding="utf_8")
        
class EdfReader:
    def __init__(self):
        self._luna_file = LunaFile()
        self._header = None
        self._filename = None

    def open_file(self, filename):
        self._filename = filename
        self._header = pyedflib.highlevel.read_edf_header(self._filename)
        
        is_compatible = EdfReader.is_file_compatible(self._filename)
        if not is_compatible:
            return False

        basename, _ = os.path.splitext(self._filename)
        self._luna_file.open_file(basename)
        
        return True

    def copy_file(self, source_filename, dest_filename):
        if not os.path.isfile(source_filename):
            return

        # Copy the EDF file        
        shutil.copy2(source_filename, dest_filename)

        # Copy the annotation file if it exist
        src_basename, _ = os.path.splitext(source_filename)
        src_tsv_filename = src_basename + ".tsv"
        src_txt_filename = src_basename + ".txt"
        dest_basename, _ = os.path.splitext(dest_filename)
        if os.path.isfile(src_tsv_filename):
            shutil.copy2(src_tsv_filename, dest_basename + ".tsv")
        elif os.path.isfile(src_txt_filename):
            shutil.copy2(src_txt_filename, dest_basename + ".txt")

    def is_file_compatible(filename):
        return True

    def close_file(self):
        self._header = None

    def save_file(self):
        self._luna_file.save_file()

    def get_montages(self):
        montage = EdfMontage()
        montage.name = 'edf'
        montage.index = 0
        return [montage]

    def get_channels(self, montage):
        channels = []
        for i, signal_header in enumerate(self._header['SignalHeaders']):
            # Create a signalModel object but only fill the info of the channel
            signal = EdfChannelModel()
            signal.name = signal_header['label']
            signal.sample_rate = signal_header['sample_rate']
            channels.append(signal)

        return channels

    def get_signal_section_count(self):
        return 1

    def get_signal_section(self, montage_index, channel_names, section_index):
        if self._filename is None:
            return None

        signals, signal_headers, _ = pyedflib.highlevel.read_edf(self._filename, ch_names=channel_names)
        return_signals = []

        for index, channel_name in enumerate(channel_names):
            duration = len(signals[index]) / signal_headers[index]["sample_frequency"]
            signal = SimpleNamespace(samples=signals[index], start_time=0, 
                end_time=duration,
                duration=duration,
                sample_rate=signal_headers[index]['sample_rate'],
                channel=channel_name)
            return_signals.append(signal)
        return return_signals

    def save_signals(self, signals):
        source_signals, source_signal_headers, header = pyedflib.highlevel.read_edf(self._filename, digital=True)

        for signal in signals:
            for index, signal_header in enumerate(source_signal_headers):
                if signal_header['label'] == signal.channel:
                    physical_min = math.floor(signal.samples.min())
                    physical_max = math.ceil(signal.samples.max())
                    limit = max(abs(physical_min), abs(physical_max))
                    digital_samples = pyedflib.highlevel.phys2dig(
                        signal.samples,
                        signal_header['digital_min'],
                        signal_header['digital_max'],
                        -limit,
                        limit)

                    source_signals[index] = digital_samples.astype(np.int32)
                    break

        pyedflib.highlevel.write_edf(self._filename, source_signals, source_signal_headers, header, digital=True)

    # Return a list of a class with the property name
    # This class has been created to imitate Stellate or Natus
    def get_event_groups(self):
        group_array = pd.unique(self._luna_file.annotations['group'])
        group_list = []
        for group in group_array:
            group_class = SimpleNamespace(name=group)
            group_list.append(group_class)
        return group_list

    def get_events(self):
        return self._luna_file.annotations

    def add_event(self, name, group, start_sec, duration_sec, channels, montage_index):
        self._luna_file.add_event(name, group, start_sec, duration_sec, channels)
        return True

    def get_extensions(self):
        return ['edf']

    def get_extensions_filters(self):
        return ['EDF (*.edf)']

    def get_recording_start_time(self):
        pass

    def remove_events_by_group(self, group_name):
        self._luna_file.remove_events_by_group(group_name)

    def remove_events_by_name(self, event_name, group_name):
        self._luna_file.remove_events_by_name(event_name, group_name)
    
    def get_sleep_stages(self):
        # Generate a alist of unscored stages if the list is empty.
        stages = self._luna_file.get_sleep_stages()
        if stages.size == 0:
            start = 0
            epoch_size = 30

            events = []
            while start < self._header['Duration']:
                events.append([commons.sleep_stages_group, '9', start, epoch_size, ""])
                start = start + epoch_size

            self._luna_file.add_events(events)
            return self._luna_file.get_sleep_stages()
        else:
            return stages

    def get_subject_info(self):

        # Parse the date from a specific date format
        # Return the total of seconds from 1 jan 1970
        def parse_date(birthdate, format):
            current_locale = locale.getlocale()
            locale.setlocale(locale.LC_ALL, "en_US")
            dt = datetime.strptime(birthdate, format)
            locale.setlocale(locale.LC_ALL, current_locale)

            epoch_time = datetime(1970, 1, 1)
            delta = (dt - epoch_time)
            return delta.total_seconds()

        subject_info = EdfSubjectInfo()

        # Convert the birthDate to the number of seconds since the epoch (1 jan 1970)
        # Default to None.
        if self._header['birthdate'] == '':
            subject_info.birth_date = None
        else:
            try:
                birthdate = self._header['birthdate']

                # Find if the birthdate is in a known format
                edf_browser_format = r'^\d{2}\s[A-Za-z]{3}\s\d{4}$' # ex:"01 Jan 2002"
                edf_plus_format = r'^\d{2}-[A-Za-z]{3}-\d{4}$' # ex:"01-Jan-2002"

                if re.match(edf_plus_format, birthdate):
                    # Parse the edf plus format. See the spec here:
                    # https://www.edfplus.info/specs/edfplus.html
                    subject_info.birth_date = parse_date(birthdate, "%d-%b-%Y")
                elif re.match(edf_browser_format, self._header['birthdate']):
                    # Parse the Edf browser format.
                    subject_info.birth_date = parse_date(birthdate, "%d %b %Y")
                else:
                    subject_info.birth_date = None

            except ValueError:
                # If there is an error while parsing the birth date string, set it to None
                subject_info.birth_date = None

        subject_info.sex = self._header['gender']
        subject_info.firstname = None
        subject_info.lastname = self._header['patientname']
        subject_info.id = self._header['patientcode']

        # Convert the startDate to the number of seconds since the epoch (1 jan 1970)
        epoch_time = datetime(1970, 1, 1)
        delta = (self._header['startdate'] - epoch_time)
        subject_info.creation_date = delta.total_seconds()

        return subject_info
    
    def get_last_error(self):
        return ""
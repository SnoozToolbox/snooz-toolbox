"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
# -*- coding: utf-8 -*-
"""
Module to read events extracted with the CEAMS application "Extraction d'evenements".
The events must be saved in a xml file in the compumedics format.

Created on Tue Feb  9 14:09:37 2021

@author: Karine Lacourse (karine.lacourse.cnmtl@ssss.gouv.qc.ca)
"""
import pandas as pd
import numpy as np
import xml.etree.ElementTree as et

def create_event_dataframe(data, index=None, dtype=None, copy=False):
    """ Create new event dataframe with fix columns.
    
    Parameters
    -----------
    data: List or None
        Informations feed to the function to fill dataframe. If None, it creates 
        an empty dataframe.
    index: Index or array-like
        Index to use for resulting frame. Will default to RangeIndex if no 
        indexing information part of input data and no index provided.
    dtype: dtype, default None
        Data type to force. Only a single dtype is allowed. If None, infer.
    copy: bool or None
        Copy data from inputs. For dict data, the default of None behaves like 
        copy=True. For DataFrame or 2d ndarray input, the default of None behaves 
        like copy=False.
    Returns
    -----------
        Pandas DataFrame with columns ['group','name','start_sec','duration_sec','channels']
    """
    return pd.DataFrame(data,
                        index=index,
                        columns=['group','name','start_sec','duration_sec','channels'],
                        dtype=dtype,
                        copy=copy)


def convert_event_df_to_single_channel(events1):
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


def convert_single_chan_string_to_list(events):
    """
        Convert the single channel (string) into a list of channels for each event in the events dataframe.

        Parameters:
            events : pandas DataFrame with columns : group, name, start_sec, duration_sec, channels
                List of events. An event can be spread on many channels.

        Return:
            events : pandas DataFrame with columns : group, name, start_sec, duration_sec, channels
                List of events with a list of channels in "channels"

    """       
    single_channel = events['channels'].values
    list_channels = []
    for chan in single_channel:
        list_channels.append([chan])
    events['channels']=list_channels
    return events


def xml_events_to_df(filename, event_label=None):
    """ Read events from an XML compumedics format and return a data frame.
    
    Parameters
    -----------
    filename        : string
        Path and filename of the XML file to read.
    event_label     : string or a list of string
        Event label to extract from the XML.
    Returns
    -----------
        df_events   : Pandas DataFrame
            A data frame of events with the headers specified by df_label.
        epoch_len   : double
            The epoch length in second.
        sleep_stages : array
            A sleep stage per epoch (an array of stages from 0-9)
            0 : awake
            1 : n1
            2 : n2
            3 : n3 
            4 : n4
            5 : REM
            6 : movement
            7 : technician intervention
            9 : uncored
    """
    
    xtree = et.parse(filename)
    xroot = xtree.getroot() 

    # Extract epoch length
    try : 
        epoch_len = float(xroot.find('EpochLength').text) 
    except : 
        epoch_len = 30.0 # could be missing when it is a discontinuous file

    # Extract events
    events = []
    for scored_event in xroot.iter('ScoredEvent'):
        group = scored_event.find('Name').text
        try:
            name = scored_event.find('EventName').text
        except:
            name = group
        start = scored_event.find('Start').text
        if (',' in start) and ('.' in start):
            start = float(start.replace(',',''))
        elif ',' in start:
            start = float(start.replace(',','.'))
        else:
            start = float(scored_event.find('Start').text)
        dur = scored_event.find('Duration').text
        if (',' in dur) and ('.' in dur):
            dur = float(dur.replace(',',''))
        elif ',' in dur:
            dur = float(dur.replace(',','.'))
        else:
            dur = float(scored_event.find('Duration').text)

        channel = scored_event.find('Input').text
        if channel is not None: 
            if not ('[' in channel):
                channel = [str(channel)]
        else:
            channel = []

        if event_label is not None:
            # Filter for the selected event name
            if name in event_label:
                events.append({'group': group, 'name': name, 'start_sec': start, 'duration_sec': dur, 'channels': channel})
        else:
            events.append({'group': group, 'name': name, 'start_sec': start, 'duration_sec': dur, 'channels': channel})
    
    # Extract sleep stage
    sleep_stages = []
    for stage in xroot.iter('SleepStage'):
        sleep_stages.append(int(stage.text))

    # Convert the list of dict into a DataFrame
    events_df = pd.DataFrame(events)
    # Clean up lists of channels for a single channel (string) per event
    events_df = convert_event_df_to_single_channel(events_df)
    # In NATUS/Stellate the annotations can be duplicated
    events_df.drop_duplicates(inplace=True, ignore_index=True)

    return events_df, epoch_len, np.array(sleep_stages)


#------------------------------------------------------------------------------
# Main to test the class
#------------------------------------------------------------------------------            
if __name__ == "__main__":
    
    #filename = 'C:/Users/klacourse/Documents/NGosselin/data/artefact_musculaire/art_sig_sts_2_export/01-01-0043_Stade_SCORING_RC.edf.xml'
    #event_label = ['CompSpec_SCORING_RC_F4']
    # Would also work with a list
    # event_label = ['CompSpec_experimental-A_C3','Annotation']
    
    #df_event, epoch_len, sleep_stages = xml_events_to_df(filename, event_label)
    # new_df = create_event_dataframe([['blabla', 'blabla', 6, 30, 'EOGL'],
    #                                 ['blabla', 'blabla', 6, 30, 'EOGL'],
    #                                 ['blabla', 'blabla', 6, 30, 'EOGL'],
    #                                 ['blabla', 'blabla', 6, 30, 'EOGL']])
    new_df = create_event_dataframe(None)
    
    print('{} events'.format(len(new_df)))
    print('column name: {}'.format(new_df.keys()))
    print(new_df)


    
    
    
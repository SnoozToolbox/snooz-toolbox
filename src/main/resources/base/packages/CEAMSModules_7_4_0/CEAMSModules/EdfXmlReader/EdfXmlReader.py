"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Read events from a EDF.XML file

    Parameters
    -----------
    filename        : string
        Path and filename of the XML file to read.
    event_name     : (optional) string or a list of string
        Event label to extract from the XML.  
        
    Outputs
    -----------
        filename    : string
            Path and filename of the XML file to read.
        events      : Pandas DataFrame
            DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
        epoch_len   : double
            The epoch length in second.
        stages_epoch : array
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
        stages_df : Pandas DataFrame
            Sleep stages (columns=['group','name','start_sec','duration_sec','channels'])
            group='stage', name='0'(ex.'1','2',...), duration_sec=30, channel=[]
"""

from flowpipe import SciNode, InputPlug, OutputPlug

import pandas as pd
from CEAMSModules.EventReader import manage_events as read_xml_events
import os

DEBUG = False

class EdfXmlReader(SciNode):
    """
        Read events from a EDF.XML file

        Parameters
        -----------
        filename        : string
            Path and filename of the XML file to read.
        event_name     : (optional) string or a list of string
            Event label to extract from the XML.  
            
        Outputs
        -----------
            filename    : string
            Path and filename of the XML file read.
            events      : Pandas DataFrame
                DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
            epoch_len   : double
                The epoch length in second.
            stages_epoch : array
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
            stages_df : Pandas DataFrame
                Sleep stages (columns=['group','name','start_sec','duration_sec','channels'])
                group='stage', name='0'(ex.'1','2',...), duration_sec=30, channel=[]
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('EdfXmlReader.__init__')
        self._cache_duration = 30 # in seconds
        InputPlug('filename', self)
        InputPlug('event_name', self)
        OutputPlug('filename', self)
        OutputPlug('events', self)
        OutputPlug('epoch_len', self)
        OutputPlug('stages_epoch', self)
        OutputPlug('stages_df', self)

    def __del__(self):
        if DEBUG: print('EdfXmlReader.__del__')

    def subscribe_topics(self):
        pass

    def on_topic_update(self, topic, message, sender):
        if DEBUG: print(f'EdfXmlReader.on_topic_update {topic}:{message}')

    def compute(self, filename, event_name):
        """
            Read events from a EDF.XML file

            Parameters
            -----------
            filename        : string
                Path and filename of the XML file to read.
            event_name     : (optional) string or a list of string
                Event label to extract from the XML.  
                
            Outputs
            -----------
            events      : Pandas DataFrame
                DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
            epoch_len   : double
                The epoch length in second.
            stages_epoch : array
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
            stages_df : Pandas DataFrame
                Sleep stages (columns=['group','name','start_sec','duration_sec','channels'])
                group='stage', name='0'(ex.'1','2',...), duration_sec=30, channel=""
        """
        if DEBUG: print('EdfXmlReader.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None

        if filename=='':
            filename = None

        if filename:
            if os.path.isfile(filename):
                # Convert from string all inputs from the settings view
                if len(event_name)>0:
                    events, epoch_len, stages_epoch = \
                        read_xml_events.xml_events_to_df(filename, event_name)
                else:
                    events, epoch_len, stages_epoch = \
                        read_xml_events.xml_events_to_df(filename)

                # Concatenate the channel label to the event_name
                stages_df = pd.DataFrame(columns=['group','name','start_sec','duration_sec','channels'])
                start_sec = 0
                stage_lst = []
                for stage_epoch in stages_epoch:
                    stage_lst.append(['stage', str(stage_epoch), start_sec, epoch_len, ""]) 
                    start_sec = start_sec + epoch_len
                stages_df = pd.DataFrame(data=stage_lst, columns=['group','name','start_sec','duration_sec','channels'])

                if events is not None:
                    cache = {}
                    cache['events'] = events
                    self._cache_manager.write_mem_cache(self.identifier, cache)
                
                    return {
                        'filename' : filename,
                        'events': events,
                        'epoch_len' : epoch_len,
                        'stages_epoch' : stages_epoch,
                        'stages_df' : stages_df
                    }
            else:
                err_message = "ERROR : {} does not exist".format(filename)
                self._log_manager.log(self.identifier, err_message)          
                print(err_message)
                return {
                    'filename' : '',
                    'events': '',
                    'epoch_len' : '',
                    'stages_epoch' : '',
                    'stages_df' : ''
                }                    
        else:
            err_message = "ERROR : filename is empty"
            self._log_manager.log(self.identifier, err_message)          
            print(err_message)
            return {
                'filename' : '',
                'events': '',
                'epoch_len' : '',
                'stages_epoch' : '',
                'stages_df' : ''
            }            

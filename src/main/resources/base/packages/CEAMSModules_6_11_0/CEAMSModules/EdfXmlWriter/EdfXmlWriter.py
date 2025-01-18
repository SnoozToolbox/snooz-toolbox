"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    EdfXmlWriter
    Create an XML file based on compumedic format.
"""
from commons.NodeInputException import NodeInputException
from CEAMSModules.EventReader import manage_events
from flowpipe import SciNode, InputPlug, OutputPlug

import xml.etree.ElementTree as ET
import pandas as pd

DEBUG = False

class EdfXmlWriter(SciNode):
    """
    Create an XML file based on compumedic format.

    Inputs:
        "filename": : string
            Path and filename of the XML file to write.
        "events": Pandas DataFrame
            DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
        "epoch_len": double
            The epoch length in second.
        "stages_df": Pandas DataFrame
            Sleep stages (columns=['group','name','start_sec','duration_sec','channels'])
            group='stage', name='0'(ex.'1','2',...), duration_sec=30, channel=[]
        
    Outputs:
        No output, the XML file is written.
        
    """
    def __init__(self, **kwargs):
        """ Initialize module EdfXmlWriter """
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')

        # Input plugs
        InputPlug('filename',self)
        InputPlug('events',self)
        InputPlug('epoch_len',self)
        InputPlug('stages_df',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    

    def compute(self, filename, events, epoch_len, stages_df):
        """
        Create an XML file based on compumedic format.

        Inputs:
            "filename": : string
                Path and filename of the XML file to write.
            "events": Pandas DataFrame
                DataFrame events (columns=['group','name','start_sec','duration_sec','channels'])
            "epoch_len": double
                The epoch length in second.
            "stages_df": Pandas DataFrame
                Sleep stages (columns=['group','name','start_sec','duration_sec','channels'])
                group='stage', name='0'(ex.'1','2',...), duration_sec=30, channel=[]
            
        Outputs:
            No output, the XML file is written.
            
        """

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if not isinstance(events, pd.DataFrame):
            raise NodeInputException(self.identifier, "events", \
            f"EdfXmlWriter input of wrong type. Expected: <class 'pd.DataFrame'> received: {type(events)}")
        if not isinstance(stages_df, pd.DataFrame):
            raise NodeInputException(self.identifier, "stages_df", \
            f"EdfXmlWriter input of wrong type. Expected: <class 'pd.DataFrame'> received: {type(stages_df)}")

        # create the file structure
        CMPStudyConfig = ET.Element('CMPStudyConfig')

        EpochLength = ET.SubElement(CMPStudyConfig, 'EpochLength')
        EpochLength.text = str(epoch_len)

        # Convert the single channel (string) into a list of channels for each event in the events dataframe.
        events = manage_events.convert_single_chan_string_to_list(events)        

        ScoredEvents = ET.SubElement(CMPStudyConfig, 'ScoredEvents')
        for i_evt, evt in events.iterrows():
            ScoredEvent = ET.SubElement(ScoredEvents, 'ScoredEvent')
            Name = ET.SubElement(ScoredEvent, 'Name')
            Name.text = str(evt['group'])
            Start = ET.SubElement(ScoredEvent, 'Start')
            Start.text = str(evt['start_sec'])
            Duration = ET.SubElement(ScoredEvent, 'Duration')
            Duration.text = str(evt['duration_sec'])       
            Input = ET.SubElement(ScoredEvent, 'Input')
            Input.text = str(evt['channels'])
            EventName = ET.SubElement(ScoredEvent, 'EventName')
            EventName.text = str(evt['name'])

        ScoredEventSettings = ET.SubElement(CMPStudyConfig, 'ScoredEventSettings')
        # extract unique list of event name
        event_group_unique = pd.unique(events.group)
        for group in event_group_unique:
            ScoredEventSetting = ET.SubElement(ScoredEventSettings, 'ScoredEventSetting')
            Name = ET.SubElement(ScoredEventSetting, 'Name')
            Name.text = str(group)
            Colour = ET.SubElement(ScoredEventSetting, 'Colour')
            Colour.text = "16776960"
            TextColour = ET.SubElement(ScoredEventSetting, 'TextColour')
            TextColour.text = "0"
            events_tmp = events[events['group']==group]
            Input = ET.SubElement(ScoredEventSetting, 'Input')
            Input.text = str(events_tmp['channels'].values[0])
            # EventGroup = ET.SubElement(ScoredEventSetting, 'EventGroup')
            # EventGroup.text = str(events_tmp['name'].values[0])

        SleepStages = ET.SubElement(CMPStudyConfig, 'SleepStages')
        for i_stage, stage in stages_df.iterrows():
            SleepStage = ET.SubElement(SleepStages, 'SleepStage')
            SleepStage.text = str(stage['name'])

        # create a new XML file with the results
        tree = ET.ElementTree(CMPStudyConfig)
        tree.write(filename, encoding='utf-8')

        # Write to the cache to use the data in the resultTab
        cache = {}
        cache['events'] = events
        self._cache_manager.write_mem_cache(self.identifier, cache)

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module does nothing.")

        return {
        }
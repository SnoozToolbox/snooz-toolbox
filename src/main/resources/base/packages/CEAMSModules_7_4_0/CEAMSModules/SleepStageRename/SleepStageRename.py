"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    Rename sleep stage annotation. 

    Parameters
    -----------
        events_in : pandas DataFrame
            List of events to rename (columns=['group','name','start_sec','duration_sec','channels']).
        group_lut : string (dict converted into a string)
            Dict where the key is the original group and the value is the new group.
        original_name : string (dict converted into a string)
            Dict where the values are the original annotation names.
            The keys are specified into plugin/PSGReader/commons.py
            ex) sleep_stages = {
                "wake":'0',
                "N1":'1',
                "N2":'2',
                "N3":'3',
                "N4":'4',
                "R":'5',
                "movement":'6',
                "tech":'7',
                "undefined":'8',
                "unscored":'9'
            }
        new_name : string (dict converted into a string)
            Dict where the values are the new annotation names.
            The keys are specified into plugin/PSGReader/commons.py
            ex) sleep_stages = {
                "wake":'0',
                "N1":'1',
                "N2":'2',
                "N3":'3',
                "N4":'4',
                "R":'5',
                "movement":'6',
                "tech":'7',
                "undefined":'8',
                "unscored":'9'
            }        
    Returns
    -----------    
        events_out : pandas DataFrame
            List of events (columns=['group','name','start_sec','duration_sec','channels'])
"""

from flowpipe import SciNode, InputPlug, OutputPlug
import numpy as np
import pandas as pd

DEBUG = False

class SleepStageRename(SciNode):
    """
    Rename sleep stage annotation. 

    Parameters
    -----------
        events_in : pandas DataFrame
            List of events to rename (columns=['group','name','start_sec','duration_sec','channels']).
        group_lut : string (dict converted into a string)
            Dict where the key is the original group and the value is the new group.
        original_name : string (dict converted into a string)
            Dict where the values are the original annotation names.
            The keys are specified into plugin/PSGReader/commons.py
            ex) sleep_stages_name = {
                "wake":  "Eveil",                
                "N1": "Stade1",
                "N2": "Stade2",
                ...
        new_name : string (dict converted into a string)
            Dict where the values are the new annotation names.
            The keys are specified into plugin/PSGReader/commons.py
            ex) sleep_stages_name = {
                "wake":  "0",                
                "N1": "1",
                "N2": "2",
                ...
    Returns
    -----------    
        events_out : pandas DataFrame
            List of events (columns=['group','name','start_sec','duration_sec','channels'])
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if DEBUG: print('SleepStageRename.__init__')
        self._filename = None
        InputPlug('events_in', self)
        InputPlug('group_lut', self)
        InputPlug('original_name', self)
        InputPlug('new_name', self)
        OutputPlug('events_out', self)


    # The plugin subscribes to the publisher to receive the settings (messages) as input
    def subscribe_topics(self):
        pass


    def compute(self, events_in, group_lut, original_name, new_name):
        """
        Rename sleep stage annotation. 

        Parameters
        -----------
            events_in : pandas DataFrame
                List of events to rename (columns=['group','name','start_sec','duration_sec','channels']).
            group_lut : string (dict converted into a string)
                Dict where the key is the original group and the value is the new group.
            original_name : string (dict converted into a string)
                Dict where the values are the original annotation names.
                The keys are specified into plugin/PSGReader/commons.py
                ex) sleep_stages_name = {
                    "wake":  "Eveil",                
                    "N1": "Stade1",
                    "N2": "Stade2",
                    "N3": "Stade3",
                    "N4": "Stade4",
                    "R":   "SP",
                    "movement": "Bouge"
                    "tech":  "Intervention",
                    "unscored": "StdND",
                }
            new_name : string (dict converted into a string)
                Dict where the values are the new annotation names.
                The keys are specified into plugin/PSGReader/commons.py
                ex) sleep_stages_name = {
                    "wake":  "0",                
                    "N1": "1",
                    "N2": "2",
                    "N3": "3",
                    "N4": "4",
                    "R":   "5",
                    "movement": "6"
                    "tech":  "7",
                    "unscored": "9",
        Returns
        -----------    
            events_out : pandas DataFrame
                List of events (columns=['group','name','start_sec','duration_sec','channels'])
        """

        if DEBUG: print('SleepStageRename.compute')
        # Clear the cache (usefull for the second run)
        self.clear_cache() # It  makes the cache=None             

        # A copy is made to avoid the modification of the input as well
        events_out = events_in.copy()

        # Convert the string into a dict to get the LUT for the name conversion
        original_names_dict = eval(original_name)
        new_names_dict = eval(new_name)
        group_dict = eval(group_lut)

        # Extract the original and new group 
        group_ori = list(group_dict.keys())[0]
        group_new = list(group_dict.values())[0]

        for evt_index, evt_row in events_out.iterrows():
            # If the current event is a stage to rename and it is the right group
            if evt_row['name'] in original_names_dict.values() and evt_row['group'] in group_ori:
                # Find the key of the value == evt_row['name']
                current_key = list(original_names_dict.keys())[list(original_names_dict.values()).index(evt_row['name'])]
                # Rename the stage (event name) based on the LUT 
                events_out.at[evt_index, 'name'] = new_names_dict[current_key]
                # Rename the event group based on the group_dict
                events_out.at[evt_index, 'group'] = group_new

        # Write the cache
        cache = {}
        cache['events'] = events_out
        self._cache_manager.write_mem_cache(self.identifier, cache)

        return {
            'events_out': events_out
        }      

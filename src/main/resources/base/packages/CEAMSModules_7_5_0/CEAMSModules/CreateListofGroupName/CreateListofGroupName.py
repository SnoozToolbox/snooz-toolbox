"""
@ Valorisation Recherche HSCM, Société en Commandite – 2025
See the file LICENCE for full license details.

    CreateListofGroupName
    A Flowpipe node that filters events based on group type and generates a list
    of tuples marking events for removal. Primarily used for sleep stage event processing.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
import pandas as pd

DEBUG = False

class CreateListofGroupName(SciNode):
    """
    Creates a list of tuples that has two value of group and name: [(group0, name0), (group1, name1)]

    Parameters
    ----------
        events : pandas DataFrame
            Pandas DataFrame columns=['group','name','start_sec','duration_sec','channels']
        group: str
            The group type to filter by (e.g., 'stage' for sleep stage events)

    Returns
    -------
        group_name_list: List[Tuple(str, str)]
            List of (group, name) tuples for events matching the specified group
    """
    def __init__(self, **kwargs):
        """ Initialize module CreateListofGroupName """
        super().__init__(**kwargs)
        if DEBUG: print('CreateListofGroupName.__init__')

        # Input plugs
        InputPlug('events',self)
        InputPlug('group',self)
        

        # Output plugs
        OutputPlug('group_name_list',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, events,group):
        """
        Processes event data and generates removal tuples based on group type.

        Parameters
        ----------
            events: pandas DataFrame
                Event data containing 'group' and 'name' lists
            group: str
                Target group type for filtering

        Returns
        -------
            group_name_list: List[Tuple(str, str)]
                Filtered list of (group, name) tuples

        Raises
        ------
            NodeInputException
                If inputs are invalid (missing keys, wrong types)
            NodeRuntimeException
                If processing fails
        """
        if DEBUG: print('CreateListofGroupName.compute')

        # Input validation
        if not isinstance(events, pd.DataFrame):
            raise NodeInputException(self.identifier, "events", "Events must be a pandas DataFrame")
        if not all(key in events for key in ['group', 'name']):
            raise NodeInputException(self.identifier, "events", "Dictionary must contain 'group' and 'name' keys")
        if not isinstance(group, str):
            raise NodeInputException(self.identifier, "group", "Group must be a string")
        
        if group == 'stage':
            group_name_list = [(events['group'][i], events['name'][i]) for i, stage in enumerate(events['group'])] # all events will be removed. the user prefers to overwrite the gold standard events.
        else:
            group_name_list = [(events['group'][i], events['name'][i]) for i, stage in enumerate(events['group']) if stage != 'stage'] #everyrhing except the gold standard will be removed.

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module creates a list of tuples to remove unwanted events.")

        return {
            'group_name_list': group_name_list
        }
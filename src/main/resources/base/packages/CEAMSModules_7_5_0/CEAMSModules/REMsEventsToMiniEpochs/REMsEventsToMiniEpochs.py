"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.

    Class to generate a list of 3-sec epochs identified as a MOR_DET or NO_DET based
    on the list of REM detections.
"""
import pandas as pd

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class REMsEventsToMiniEpochs(SciNode):
    """
    Class to generate a list of mini-epochs identified as a MOR_DET or NO_DET based
    on the list of REM detections.

    Parameters
    ----------
        filename : string
            The name of the current PSG file.
        REMs_events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
            List of detections from REMDetectorShotGroup
        epochs_to_proceed: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
            List of mini-epochs to identify as a MOR_DET or NO_DET.
        parameters : dict
            Dictionary of group and name of the mini-epoch..
            'mini_epoch_group': 'DET_MOR'
            'mini_epoch_name_Phasic': 'Snooz_MOR_Phasic'
            'mini_epoch_name_Tonic': 'Snooz_MOR_Tonic'

    Returns
    -------
        mini_epochs_events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
            List of mini-epochs identified as a MOR_DET or NO_DET.

    """
    def __init__(self, **kwargs):
        """ Initialize module REMsEventsToMiniEpochs """
        super().__init__(**kwargs)
        if DEBUG: print('REMsEventsToMiniEpochs.__init__')

        # Input plugs
        InputPlug('filename',self)
        InputPlug('REMs_events',self)
        InputPlug('epochs_to_proceed',self)
        InputPlug('parameters',self)
        # Output plugs
        OutputPlug('mini_epochs_events',self)
    
        # The master module is usally the PSGReader when the REMsEventsToMiniEpochs
        # module is instanciated.
        self._is_master = False 

        # The mini epoch is marked with a MOR if at least 1/3 of the detected MOR is included
        self.overlap_fraction = 3
    

    def compute(self, filename, REMs_events, epochs_to_proceed, parameters):
        """
        To generate a list of mini-epochs identified as a MOR_DET or NO_DET based
        on the list of REM detections.

        Parameters
        ----------
            filename : string
                The name of the current PSG file.
            REMs_events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
                List of detections from REMDetectorShotGroup
            epochs_to_proceed: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
                List of mini-epochs to identify as a MOR_DET or NO_DET.
            parameters : dict
                Dictionary of group and name of the mini-epoch..
                'mini_epoch_group': 'DET_MOR'
                'mini_epoch_name_Phasic': 'Snooz_MOR_Phasic'
                'mini_epoch_name_Tonic': 'Snooz_MOR_Tonic'

        Returns
        -------
            mini_epochs_events: Pandas DataFrame (columns=['group','name','start_sec','duration_sec','channels'])
                List of mini-epochs identified as a MOR_DET or NO_DET.

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """

        # Raise NodeInputException if the an input is wrong. This type of
        # exception will stop the process with the error message given in parameter.
        if isinstance(REMs_events, pd.DataFrame) == False:
            raise NodeInputException(self.identifier, "REMs_events", \
               f"REMsEventsToMiniEpochs this input is expected to be a Pandas DataFrame and not {type(REMs_events)}.")

        if isinstance(epochs_to_proceed, pd.DataFrame) == False:
            raise NodeInputException(self.identifier, "epochs_to_proceed", \
               f"REMsEventsToMiniEpochs this input is expected to be a Pandas DataFrame and not {type(epochs_to_proceed)}.")

        # Raise the runtime exception
        if len(REMs_events) == 0:
            raise NodeRuntimeException(self.identifier, "REMs_events", \
                f"No REMs detected for {filename}.")
        if len(epochs_to_proceed) == 0:
            raise NodeRuntimeException(self.identifier, "epochs_to_proceed", \
                f"No R sleep stages for {filename}.")

        if isinstance(parameters, str) and not parameters == '':
            parameters = eval(parameters)
        if not isinstance(parameters, dict):
            raise NodeInputException(self.identifier, "parameters", \
                f"REMsEventsToMiniEpochs this input is expected to be a dictionary and not {type(parameters)}.")

        # By defaul all the epochs_to_proceed are considered as NO_DET
        epochs_to_proceed['channels'] = REMs_events['channels'].iloc[0]
        mini_epochs_events = epochs_to_proceed
        mini_epochs_events['name'] = parameters["mini_epoch_name_Tonic"]
        # Change the group value for det_MOR_3s
        mini_epochs_events['group'] = parameters["mini_epoch_group"]

        # Extract the unique list of duration of the epochs to proceed
        mini_epochs_duration = epochs_to_proceed['duration_sec'].unique()
        if (len(mini_epochs_duration) > 1):
            raise NodeRuntimeException(self.identifier, "epochs_to_proceed", \
                f"The duration of the epochs to proceed for {filename} is not unique.")
        mini_epochs_duration = mini_epochs_duration[0]

        # Change the name of the event in the epochs_to_proceed to MOR_DET 
        # if it includes at least a third of the a REMs detection in REMs_events
        for index_3s_epoch, row_epoch in epochs_to_proceed.iterrows():
            # Look for a REMs detection in REMs_events that overlaps with the current epoch
            start_before_end = REMs_events[( REMs_events['start_sec'] < (row_epoch['start_sec'] + mini_epochs_duration))]
            stop_after_start = REMs_events[( (REMs_events['start_sec'] + REMs_events['duration_sec']) > row_epoch['start_sec'])]
            # Intersection of the two sets of events
            REMs_cur_epoch = start_before_end.merge(stop_after_start, how='inner')
            for index_REM, row_det in REMs_cur_epoch.iterrows():
                # Compute overlap between the current epoch and the REM detection
                # if det starts before epoch
                if row_det['start_sec'] < row_epoch['start_sec']:
                    overlap_sec = (row_det['start_sec'] + row_det['duration_sec']) - row_epoch['start_sec']
                # if det starts after the epoch
                else:
                    end_sec = min(row_epoch['start_sec'] + mini_epochs_duration, row_det['start_sec'] + row_det['duration_sec'])
                    overlap_sec =  end_sec - row_det['start_sec']
                # Mark the epoch as a MOR_det if the overlap is at least a third of the duration of the detection
                if overlap_sec >= (row_det['duration_sec']/self.overlap_fraction):
                    mini_epochs_events.loc[index_3s_epoch,'name'] = parameters["mini_epoch_name_Phasic"]


        # Write to the cache to use the data in the resultTab
        cache = {}
        cache['events'] = mini_epochs_events
        self._cache_manager.write_mem_cache(self.identifier, cache)

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "Detected MOR converted into mini-epochs.")

        return {
            'mini_epochs_events': mini_epochs_events
        }
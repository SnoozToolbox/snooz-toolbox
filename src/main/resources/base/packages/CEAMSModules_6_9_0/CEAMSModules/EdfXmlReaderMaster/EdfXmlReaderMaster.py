"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    EdfXmlReaderMaster
    Read events from a EDF.XML files or .XML files.
    This class is derived from EdfXmlReader.
    EdfXmlReaderMaster is a master plugin to loop in batch.
    Only one plugin can be master in a pipeline.
"""

from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException
from CEAMSModules.EdfXmlReader.EdfXmlReader import EdfXmlReader

DEBUG = False

class EdfXmlReaderMaster(EdfXmlReader):
    """
    Read events from a EDF.XML files or .XML files.

    Parameters
    -----------
    files        : String of List of string (i.e. '[file1, file2, ...]')
        List of path and filename of the XML file to read.
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
    def __init__(self, **kwargs):
        """ Initialize module EdfXmlReaderMaster """
        super().__init__(**kwargs)
        if DEBUG: print('EdfXmlReaderMaster.__init__')

        # Input plugs
        InputPlug('filename',self)
        InputPlug('event_name',self)
        
        # Output plugs
        OutputPlug('filename',self)
        OutputPlug('events',self)
        OutputPlug('epoch_len',self)
        OutputPlug('stages_epoch',self)
        OutputPlug('stages_df',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self.is_master = True 
        self.is_done = False
        self._cache_duration = 30 # in seconds

    def compute(self, filename, event_name):
        """
        Read events from a EDF.XML files or .XML files.

        Parameters
        -----------
        files         : List of string 
            The files to read
        event_name     : (optional) string or a list of string
            Event label to extract from the XML.  
            
        Outputs
        -----------
            filename    : list of string
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
        if (filename == '[]') or (filename is None) or (filename == '') or (len(filename) == 0):
            raise NodeInputException(self.identifier, "filename", \
                "EdfXmlReaderMaster filename parameter must be set.")

        # Convert the string into a list of string
        files = eval(filename)

        # Get the next filename
        filename = files[self._iteration_counter]

        # Set the iteration_identifier in case there is a problem during the process.
        # This will be used to identify the problematic file.
        self.iteration_identifier = filename

        # Check if done
        if self._iteration_counter + 1 >= len(files):
            self.is_done = True

        if filename is not None:
            return_dict = EdfXmlReader.compute(self, filename, event_name)

            # Update progression information
            self.iteration_count = len(files)

            return {
                'filename': return_dict['filename'],
                'events': return_dict['events'],
                'epoch_len': return_dict['epoch_len'],
                'stages_epoch': return_dict['stages_epoch'],
                'stages_df': return_dict['stages_df']
            }
        else:
            raise NodeRuntimeException(self.identifier, "files", "EdfXmlReaderMaster a file of files is None.")           
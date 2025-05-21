"""
@ Valorisation Recherche HSCM, Société en Commandite – 2025
See the file LICENCE for full license details.

    CreateDict
    A Flowpipe node that creates a dictionary from key-value pairs and outputs both
    the dictionary and the original value. This is useful for data packaging and
    transformation in processing pipelines.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class CreateDict(SciNode):
    """
    Transforms key-value inputs into a dictionary output while preserving the original value.
    The dictionary is stringified for compatibility with downstream Flowpipe nodes.

    Parameters
    ----------
        Key: str
            The key to be used in the output dictionary
        Value: Any
            The value to associate with the key in the dictionary
            
    Returns
    -------
        Dict: str
            String representation of the generated dictionary (for Flowpipe compatibility)
        Value: Any
            The original input value (passed through)
    """

    def __init__(self, **kwargs):
        """ Initialize module CreateDict """
        super().__init__(**kwargs)
        if DEBUG: print('CreateDict.__init__')

        # Input plugs
        InputPlug('Key',self)
        InputPlug('Value',self)
        

        # Output plugs
        OutputPlug('Dict',self)
        OutputPlug('Value',self)

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, Key,Value):
        """
        Creates a dictionary from the input key-value pair and returns both
        the dictionary and original value.

        Parameters
        ----------
            Key: str
                The dictionary key to use
            Value: Any
                The value to associate with the key

        Returns
        -------
            Dict: str
                Stringified version of the {Key: Value} dictionary
            Value: Any
                The original input value (passed through)

        Raises
        ------
            NodeInputException
                If Key is not a string or if Value is None
            NodeRuntimeException
                If dictionary creation fails for any reason
        """

        if DEBUG: print('CreateDict.compute')
        # Input validation
        if not isinstance(Key, str) or not Key.strip():
            raise NodeInputException(self.identifier, "Key", "Key must be a non-empty string")
        if Value is None:
            raise NodeInputException(self.identifier, "Value", "Value cannot be None")
        
        Dictionary = {Key:Value}

        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module creates a dictionary.")

        return {
            'Dict': str(Dictionary), 
            'Value': Value
        }
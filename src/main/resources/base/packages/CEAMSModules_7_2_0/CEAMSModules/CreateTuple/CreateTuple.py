"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2025
See the file LICENCE for full license details.

    CreateTuple
    This module creates a tuple from two input values.
    It is used to combine two values into a single tuple for further processing.
"""
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException
from commons.NodeRuntimeException import NodeRuntimeException

DEBUG = False

class CreateTuple(SciNode):
    """
    This module creates a tuple from two input values.
    It is used to combine two values into a single tuple for further processing.

    Parameters
    ----------
        Idx0: first value to be included in the tuple
        Idx1: second value to be included in the tuple

    Returns
    -------
        Tuple: a tuple containing the two input values
        
    """
    def __init__(self, **kwargs):
        """ Initialize module CreateTuple """
        super().__init__(**kwargs)
        if DEBUG: print('CreateTuple.__init__')

        # Input plugs
        InputPlug('Idx0',self)
        InputPlug('Idx1',self)
        

        # Output plugs
        OutputPlug('Tuple',self)
        
        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
        self._is_master = False 
    
    def compute(self, Idx0,Idx1):
        """
        This module creates a tuple from two input values.
        It is used to combine two values into a single tuple for further processing.

        Parameters
        ----------
            Idx0: first value to be included in the tuple
            Idx1: second value to be included in the tuple

        Returns
        -------
            Tuple: a tuple containing the two input values
            

        Raises
        ------
            NodeInputException
                If any of the input parameters have invalid types or missing keys.
            NodeRuntimeException
                If an error occurs during the execution of the function.
        """
        if DEBUG: print('CreateTuple.compute')
        # Check if the input parameters are valid   
        if not isinstance(Idx0, (int, float)):
            raise NodeInputException("Idx0 must be an int or a float")
        if not isinstance(Idx1, (int, float)):
            raise NodeInputException("Idx1 must be an int or a float")
        
        if Idx0 is None:
            raise NodeInputException("Idx0 is None")
        if Idx1 is None:
            raise NodeInputException("Idx1 is None")

        First = Idx0
        Second = Idx1
        Tuple = (First, Second)


        # Log message for the Logs tab
        self._log_manager.log(self.identifier, "This module creates a tuple.")

        return {
            'Tuple': Tuple
        }
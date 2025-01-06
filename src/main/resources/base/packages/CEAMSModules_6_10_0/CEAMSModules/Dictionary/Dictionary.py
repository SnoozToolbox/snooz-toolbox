"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    Dictionary
    Return a value based on a key received in input.
"""
import ast
from flowpipe import SciNode, InputPlug, OutputPlug
from commons.NodeInputException import NodeInputException

DEBUG = False

class Dictionary(SciNode):
    """
    Dictionary
    Return a value based on a key received in input.

    Inputs:
        "key": str
            The key to lookup in the dictionary.
        "dictionary": dict(str,object)
            The dictionary.
        

    Outputs:
        "value": object
            The value associated with the key.
        
    """
    def __init__(self, **kwargs):
        """ Initialize module Dictionary """
        super().__init__(**kwargs)
        if DEBUG: print('SleepReport.__init__')

        # Input plugs
        InputPlug('key',self)
        InputPlug('dictionary',self)
        

        # Output plugs
        OutputPlug('value',self)
    
    def compute(self, key,dictionary):
        """
        Dictionary
        Return a value based on a key received in input.

        Inputs:
            "key": str
                The key to lookup in the dictionary.
            "dictionary": dict(str,object)
                The dictionary.
            

        Outputs:
            "value": object
                The value associated with the key.
        """
        if isinstance(dictionary, str):
            dictionary = ast.literal_eval(dictionary)
            
        if not isinstance(dictionary, dict):
            raise NodeInputException(self.identifier, "dictionary", \
            f"dictionary input must be set.")

        return {
            'value': dictionary[key] if key in dictionary else None
        }
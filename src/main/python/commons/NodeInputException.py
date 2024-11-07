"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    NodeInputException

    NodeInputException are generated within the compute function of a module 
    (PSGReader, FIRSignal, etc.) when there's a problem with the input its receiving.
"""
from commons.NodeException import NodeException

class NodeInputException(NodeException):
    def __init__(self, node_identifier, param_name, message):
        super().__init__(node_identifier, param_name, message)

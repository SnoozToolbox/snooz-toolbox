"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    NodeRuntimeException

    NodeRuntimeException are generated within the compute function of a module 
    (PSGReader, FIRSignal, etc.) when there's a problem during the normal operation.
"""
from commons.NodeException import NodeException

class NodeRuntimeException(NodeException):
    def __init__(self, node_identifier, param_name, message):
        super().__init__(node_identifier, param_name, message)
        self.message = message

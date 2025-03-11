"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
"""
    NodeException

    NodeException are generated within the compute function of a module 
    (PSGReader, FIRSignal, etc.) when there's a problem (input or runtime).
"""

class NodeException(Exception):
    def __init__(self, node_identifier, param_name, message):
        super().__init__(message)
        self.node_identifier = node_identifier
        self.param_name = param_name

"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from qtpy.QtCore import QObject

class Manager(QObject):
    """ Manager is the base class for all managers. """
    def __init__(self, managers):
        """ Initialize the manager. 
        
        Parameters
        ----------
            managers : Managers
                The managers
        """
        super().__init__()
        self._managers = managers

    def initialize(self):
        """ Initialize the manager. """
        raise NotImplemented

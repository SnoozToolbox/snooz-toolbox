"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
DEBUG = False

from Managers.Manager import Manager

class LogManager(Manager):
    """ LogManager manages logs between the execution of a process and 
    the user interface. """

    def __init__(self, managers):
        """ Initialize the log manager. 
        
        Record the logs for each module and also record the logs over a timeline.

        Parameters
        ----------
            managers : Managers
                The managers
        """
        super().__init__(managers)
        self._logs = {}
        self._timeline_logs = [] 

    @property
    def timeline_logs(self):
        """ Return the logs over a timeline 
        
        Returns
        -------
            Array of logs over a timeline
        """
        return self._timeline_logs

    @property
    def logs(self):
        """ Return the logs for all modules
        
        Returns
        -------
            Dictionary of logs
        """
        return self._logs

    def initialize(self):
        """ Initialize the log manager """
        pass
    
    def log(self, identifier, entry):
        """ Log an entry 
        
        Parameters
        ----------
            identifier : String
                The identifier of the module
            entry : String
                The entry to log
        """
        if DEBUG: print(f'LogManager.log {identifier}.{entry}')
        if identifier not in self._logs:
            self._logs[identifier] = []
        
        self._logs[identifier].append(entry)
        self._timeline_logs.append((identifier, entry))

    def get_logs(self, identifier):
        """ Get logs associated with an identifier """
        if DEBUG: print(f'LogManager.get_logs {identifier}')
        if identifier in self._logs:
            return self._logs[identifier]
        else:
            return []

    def clear(self, identifier=None):
        """ Clear the logs
        If an identifier is set, clear the logs of this identifier.
        If not, clear all logs.
        """
        if identifier is not None:
            if identifier in self._logs:
                self._logs[identifier].clear()
        else:
            self._logs.clear()

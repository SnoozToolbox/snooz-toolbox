"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from Managers.Manager import Manager

class CacheManager(Manager):
    """ CacheManager handles a module's in memory cache.
    
    The cache is used to display information in the results view of a module
    once a process has been executed. When a user runs a process, or a tool, 
    some modules will be setup in a way to send information to the cache. This
    is mostly useful for developer who wish to see the results of a module after
    it's been run.

    For example, the cache is used in a module that is responsible for applying a 
    filter over a signal. When the module is done computing, it will place a subset
    of the signal before the filtering and after the filtering. When the user clicks
    on the module to look at the results tab, they will be able to see both signals
    displayed in a graph to validate visually that the module is correctly filtering
    the signal.
    """
    
    def __init__(self, managers):
        super().__init__(managers)
        """ Init the CacheManager. """
        self._managers = managers
        self._cache = {}
    
    def initialize(self):
        """ Initialize the CacheManager. """       
        pass

    def write_mem_cache(self, node_identifier, data):
        """ Write data to the cache. 
        
        Parameters
        ----------
        node_identifier : str
            The identifier of the node.
        data : object
            The data to write to the cache.

        Returns
        -------
        None
        """
        self._cache[node_identifier] = data
       
    def read_mem_cache(self, node_identifier):
        """ Read data from the cache.
        
        Parameters
        ----------
        node_identifier : str
            The identifier of the node.

        Returns
        -------
            object
                The data read from the cache.
        """
        if node_identifier in self._cache:
            return self._cache[node_identifier]
        else:
            return None
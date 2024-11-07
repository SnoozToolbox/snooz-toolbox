from .node import INode
from .ActivationState import ActivationState

class SciNode(INode):
    """
        Scinode implementation of the INode class from FlowPipe

        This class adds the concept of master node, which allows to control
        the execution of the graph.

        A graph containing a master node will be executed as long as the master
        node is not done. 

        Exemple use:
        A node contains a list of files to run the process on. Everytime the graph
        is run, that node will submit the next file to the process. The graph will
        be executed for each file from that master node. See the plugin PSGReader 
        for an example.

        # A master module allows the process to be reexcuted multiple time.
        # For exemple, this is useful when the process must be repeated over multiple
        # files. When the master module is done, ie when all the files were process, 
        # The compute function must set self.is_done = True
        # There can only be 1 master module per process.
    """
    def __init__(self, name=None, identifier=None, metadata=None,
                 graph='default'):
        """ Initialize """
        super(SciNode, self).__init__(name=name, identifier=identifier, metadata=metadata,
                 graph=graph)

        self._is_master = False
        self._is_done = True
        self._iteration_identifier = None
        self._iteration_count = 1
        self._iteration_counter = 0

    @property
    def is_master(self):
        """ is_master: is this node a master node """
        return self._is_master
    
    @is_master.setter
    def is_master(self, value):
        """ is_master(): set is_master flag """
        self._is_master = value

    @property
    def iteration_count(self):
        """ iteration_count: total number of iteration to be done """
        return self._iteration_count
    
    @iteration_count.setter
    def iteration_count(self, value):
        """ iteration_count(): set the total number of iteration to be done """
        self._iteration_count = value

    @property
    def iteration_counter(self):
        """ iteration_counter: total number of iteration to be done """
        return self._iteration_counter
    
    @iteration_counter.setter
    def iteration_counter(self, value):
        """ iteration_counter(): set the total number of iteration to be done """
        self._iteration_counter = value

    @property
    def iteration_identifier(self):
        """
        iteration_identifier should be set for each iteration of a master node.
        This is used to identify what caused the process when a NodeRuntimeException
        occured within an iteration of the master node. You can ignore this variable
        if self._is_master is False.
        """
        return self._iteration_identifier
    
    @iteration_identifier.setter
    def iteration_identifier(self, value):
        """ iteration_identifier(): set iteration_identifier"""
        self._iteration_identifier = value

    @property
    def is_done(self):
        """ If it's a master node, is it done or do we need to evaluate the
        graph again? """
        return self._is_done
    
    @is_done.setter
    def is_done(self, value):
        """ Sets if it's done processing or not """
        self._is_done = value

    def clear_cache(self):
        self._cache_manager.write_mem_cache(self.identifier, None)

    def post_deserialize(self, data):
        self.activation_state = data[ActivationState.KEY]
        super().post_deserialize(data)

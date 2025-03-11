import copy
import datetime as dt
import gc
from qtpy import QtCore
from qtpy.QtCore import QCoreApplication
import time

from commons.NodeRuntimeException import NodeRuntimeException
from flowpipe import Graph
from flowpipe.ActivationState import ActivationState
from flowpipe.utilities import import_class 
from Managers.LogManager import LogManager
from widgets.WarningDialog import WarningDialog

DEBUG = False

class ProcessWorker(QtCore.QObject):
    """
        Worker objects runs the process inside a thread to avoid blocking the main
        thread.
    """
    finished = QtCore.Signal(list, list)
    interrupted = QtCore.Signal(list, list)
    progression_update = QtCore.Signal(int, int)

    def __init__(self, graph_json, deepcopy_outputs, managers, use_multithread=True):
        """ Initialize member variables """
        super(ProcessWorker, self).__init__()
        self._managers = managers
        self._deepcopy_outputs = deepcopy_outputs
        self._should_stop = False
        self._graph_json = graph_json
        self._use_multithread = use_multithread

    def _init_graph(self, graph_json):
        graph = Graph()
        master_node = None
        for node_json in graph_json["process_params"]["nodes"]:
            if node_json[ActivationState.KEY] == ActivationState.DEACTIVATED:
                continue

            node = import_class(node_json["module"], node_json["cls"])(
                    graph=None
                )
            node_json["name"] = node_json["name"] + node_json["identifier"]
            node.post_deserialize(node_json)
            node.set_pub_sub_manager(self._managers.pub_sub_manager)
            node.set_cache_manager(self._managers.cache_manager)
            node.set_log_manager(self._managers.log_manager)
            
            # Check if a master node is within the process
            if node.is_master:
                master_node = node

            graph.add_node(node)

        nodes = {n.identifier: n for n in graph.nodes}
        activated_nodes = [n for n in graph_json["process_params"]['nodes'] if n[ActivationState.KEY] != ActivationState.DEACTIVATED]

        for node in activated_nodes:
            this = nodes[node['identifier']]
            for name, input_ in node['inputs'].items():
                for identifier, plug in input_['connections'].items():
                    # Handle the case when an upstream node has been deactivated
                    if identifier in nodes:
                        upstream = nodes[identifier]
                        upstream.outputs[plug] >> this.inputs[name]

        return graph, master_node

    @QtCore.Slot()
    def run(self):
        """ Run the process
            The graph will be evaluated once if no master node has been found.
            If a master node is found, the graph will be evaluated until the master
            node is done or until the worker received a stop command.
         """
        if DEBUG: print("Starting run()")

        # WARNING
        # Enable garbage collection
         # The gc is disabled in the MainWindow
         # to bypass a bug in PySide2 5.15.2 (apparently fixed in 5.15.4, but not distributed)
         # the bug makes Snooz closes on setPixmap (~25% of the time)
         # should remove any access to the garbage collector once Snooz uses PySide6        
        gc.enable()

        self._managers.log_manager.clear()
        is_master_done = False
        try:
            total_start_time = time.time()
            self._managers.log_manager.log("process", "*****************************")
            self._managers.log_manager.log("process", "Starting Run")

            # Initialize the list of interruption
            iteration_interruption = []
            iteration = 0
            while not is_master_done and not self._should_stop:
                iteration_start_time = time.time()
                self._managers.log_manager.log("process", "Starting iteration")
                graph, master_node = self._init_graph(self._graph_json)
                try:
                    if master_node is not None:
                        master_node.iteration_counter = iteration
                    if self._use_multithread:
                        graph.evaluate(mode="threading", max_workers=4, data_persistence=False)
                    else:
                        graph.evaluate(mode="linear", max_workers=None, data_persistence=False)
                except NodeRuntimeException as err:
                    if master_node is not None:
                        # Append to the list of interruptions and continue with the next
                        # iteration of the master node.
                        iteration_interruption.append({
                            "identifier":master_node.iteration_identifier,
                            "type":err.param_name,
                            "message":err
                        })
                    else:
                        # Useful when the pipeline does not have a master node.
                        WarningDialog(err.message) 
                        raise err
                    
                iteration += 1

                if master_node is None:
                    is_master_done = True
                else:
                    is_master_done = master_node.is_done

                if not is_master_done:
                    # Set the master node to dirty to compute this node first
                    # before going to the nodes downstream.
                    self.progression_update.emit(master_node.iteration_count, 
                                                    iteration)
                    # Update the UI (to make sure the event are not analyzed only after completion)
                    QCoreApplication.processEvents()

                eval_time = time.time() - iteration_start_time
                feval_time = dt.timedelta(seconds=eval_time)
                self._managers.log_manager.log("process", f"Iteration time:\t{feval_time}\n")

                outputs = {}
                for name, plug in graph.outputs.items():
                    if self._deepcopy_outputs:
                        outputs[name] = copy.deepcopy(plug.value)
                    else:
                        outputs[name] = plug.value

            eval_time = time.time() - total_start_time
            feval_time = dt.timedelta(seconds=eval_time)
            self._managers.log_manager.log("process", f"Total process time:\t{feval_time}\n\n")
            
            if self._should_stop:
                self.interrupted.emit(outputs, iteration_interruption)
            else:
                self.finished.emit(outputs, iteration_interruption)
            QCoreApplication.processEvents()

        except Exception as exc:
            if DEBUG: print(f"General Exception occured {exc}")
            self._managers.log_manager.log("process", f"Interrupted:{exc}")
            self.interrupted.emit([], iteration_interruption)

    def stop(self):
        """ Stop the worker from running iterating over the next graph """
        self._should_stop = True

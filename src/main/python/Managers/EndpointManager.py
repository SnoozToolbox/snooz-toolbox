"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from Managers.Manager import Manager
from Endpoints.EndpointHandlers.MenuEndpointHandler import MenuEndpointHandler
from Endpoints.EndpointHandlers.ModuleEndpointHandler import ModuleEndpointHandler
from Endpoints.EndpointHandlers.CustomEndpointHandler import CustomEndpointHandler
from Endpoints.EndpointHandlers.FileMenuEndpointHandler import FileMenuEndpointHandler

class EndpointManager(Manager):
    """ EndpointManager handles the registration of endpoint handlers.
    
    Endpoints and hooks.
    The concepts of endpoints and hooks are fundatemental to the working of Snooz. It
    is what allow Snooz to be modular and extensible.

    Endpoints are features that Snooz is making available to package items. They are 
    how a package item interact with Snooz and are handled by an EndpointHandler.

    A hook is what is used by a package item to attach to an endpoint. When a package
    item is registered, the package manager will register all the hooks of the item
    to the corresponding endpoint. Hooks are defined within the JSON description file 
    of the package item.

    For example, the MenuEndpoint is an endpoint that can be used by a package item
    to add a new action menu to the menu bar. This endpoint is used by AppPackageItem, 
    ProcessPackageItem and ToolPackageItem. When a package item register its hook to 
    the MenuEndpointHandler, it will add the menu to the menu bar and when the clicked, 
    the corresponding package item will be loaded.
    """
    def __init__(self, managers, main_window):
        """ Initialize the endpoint manager.

        Parameters
        ----------
            managers : Managers
                The managers
            main_window : MainWindow
                The main window
        """
        super().__init__(managers)
        self._handlers = {}
        self._main_window = main_window

    def initialize(self):
        if self._main_window is None:
            return
        
        """ Initialize all endpoint handlers. """
        self._register_handler(MenuEndpointHandler.ENDPOINT_NAME, MenuEndpointHandler(self._managers))
        self._register_handler(ModuleEndpointHandler.ENDPOINT_NAME, ModuleEndpointHandler(self._managers))
        self._register_handler(CustomEndpointHandler.ENDPOINT_NAME, CustomEndpointHandler(self._managers))
        self._register_handler(FileMenuEndpointHandler.ENDPOINT_NAME, FileMenuEndpointHandler(self._managers))

        self.get_handler(MenuEndpointHandler.ENDPOINT_NAME).set_menu_bar(self._main_window.menuBar)
        self.get_handler(MenuEndpointHandler.ENDPOINT_NAME).set_before_menu(self._main_window.menuDev_Tools)

    def get_handler(self, endpoint_name):
        """ Get the endpoint handler. 
        
        Parameters
        ----------
        endpoint_name : str
            The name of the endpoint

        Returns
        -------
        EndpointHandler
            The endpoint handler
        """
        if endpoint_name in self._handlers:
            return self._handlers[endpoint_name]
        return None

    def register_hook(self, hook):
        """ Register a hook.

        Parameters
        ----------
        hook : dict
            The hook to register
        """
        if "endpoint_name" not in hook:
            self._managers.pub_sub_manager.publish(self, "show_error_message", f"Invalid hook: endpoint_name not found in {hook}")
            return
        
        endpoint_name = hook["endpoint_name"]
        if endpoint_name in self._handlers:
            self._handlers[endpoint_name].register_hook(hook)
        else:
            self._managers.pub_sub_manager.publish(self, "show_error_message", f"Invalid endpoint name: {endpoint_name} not found")

    def unregister_hook(self, hook):
        """ Unregister a hook.
        
        Parameters
        ----------
        hook : dict
            The hook to unregister
        """
        if "endpoint_name" not in hook:
            self._managers.pub_sub_manager.publish(self, "show_error_message", f"Invalid hook: endpoint_name not found in {hook}")
            return

        endpoint_name = hook["endpoint_name"]
        if endpoint_name in self._handlers:
            self._handlers[endpoint_name].unregister_hook(hook)
        else:
            self._managers.pub_sub_manager.publish(self, "show_error_message", f"Invalid endpoint name: {endpoint_name} not found")

    def _register_handler(self, endpoint_name, handler):
        """ Register an endpoint handler.
        
        Parameters
        ----------
        endpoint_name : str
            The name of the endpoint
        handler : EndpointHandler
            The endpoint handler
        """
        if endpoint_name not in self._handlers:
            self._handlers[endpoint_name] = handler

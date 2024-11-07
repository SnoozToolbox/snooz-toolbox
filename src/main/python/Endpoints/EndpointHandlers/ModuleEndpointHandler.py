from Endpoints.EndpointHandler import EndpointHandler
from Managers.ModuleManager import ModuleManager

class ModuleEndpointHandler(EndpointHandler):
    # DO NOT CHANGE THIS.
    # The name of the endpoint is used in every modules, tools and apps description file.
    # When you change the name, it breaks all backward compatibility with those.
    ENDPOINT_NAME = "module_endpoint"

    def __init__(self, managers):
        super(ModuleEndpointHandler, self).__init__()
        self._module_manager = managers.module_manager

    def register_hook(self, hook):
        assert "parameters" in hook
        self._module_manager.register_module(hook)
        # Add the module to the module manager
            
    def unregister_hook(self, hook):
        assert "parameters" in hook
        self._module_manager.unregister_module(hook)
        # Remove the module to the module manager
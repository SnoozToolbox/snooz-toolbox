from Endpoints.EndpointHandler import EndpointHandler

class CustomEndpointHandler(EndpointHandler):
    # DO NOT CHANGE THIS.
    # The name of the endpoint is used in every modules, tools and apps description file.
    # When you change the name, it breaks all backward compatibility with those.
    ENDPOINT_NAME = "custom_endpoint"

    def __init__(self, managers):
        super(CustomEndpointHandler, self).__init__()
        self._custom_endpoints = {}
        self._managers = managers
        #self._managers.pub_sub_manager.subscribe(self, "request_custom_hooks")

    #def on_topic_update(self, topic, message, sender):
    #    if topic == "request_custom_hooks":
    #        if message in self._custom_endpoints:
    #            sender.response_custom_hooks(self._custom_endpoints[message])
    #            self._managers.pub_sub_manager.publish(self, "custom_hooks", self._custom_endpoints[message])
    
    @property
    def custom_endpoints(self):
        return self._custom_endpoints

    def register_hook(self, hook):
        assert "parameters" in hook
        custom_endpoint_name = hook["parameters"]["custom_endpoint_name"]
        if custom_endpoint_name not in self._custom_endpoints:
            self._custom_endpoints[custom_endpoint_name] = []

        self._custom_endpoints[custom_endpoint_name].append(hook)
        # Add the module to the module manager
            
    def unregister_hook(self, hook):
        assert "parameters" in hook
        custom_endpoint_name = hook["parameters"]["custom_endpoint_name"]

        if custom_endpoint_name in self._custom_endpoints:
            self._custom_endpoints[custom_endpoint_name].remove(hook)

        if len(self._custom_endpoints[custom_endpoint_name]) == 0:
            del self._custom_endpoints[custom_endpoint_name]

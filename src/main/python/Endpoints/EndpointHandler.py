from qtpy.QtCore import QObject

from Managers.PackageManager import PackageManager

class EndpointHandler(QObject):
    def __init__(self):
        super(EndpointHandler, self).__init__()

    def register_hook(self, hook_parameters):
        raise NotImplemented
    
    def unregister_hook(self, hook_parameters):
        raise NotImplemented
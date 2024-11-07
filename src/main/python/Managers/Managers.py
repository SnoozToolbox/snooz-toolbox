"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from Managers.AppManager import AppManager
from Managers.CacheManager import CacheManager
from Managers.ContentManager import ContentManager
from Managers.EndpointManager import EndpointManager
from Managers.LogManager import LogManager
from Managers.ModuleManager import ModuleManager
from Managers.NavigationManager import NavigationManager
from Managers.PackageManager import PackageManager
from Managers.ProcessManager import ProcessManager
from Managers.PubSubManager import PubSubManager
from Managers.SettingsManager import SettingsManager
from Managers.StyleManager import StyleManager
from Managers.ToolManager import ToolManager

class Managers:
    def __init__(self, main_window):
        """ Create all managers. 
        
        Parameters
        ----------
            main_window : MainWindow
                The main window of the application.
        """
        self._app_manager = AppManager(self)
        self._endpoint_manager = EndpointManager(self, main_window)
        self._module_manager = ModuleManager(self)
        self._process_manager = ProcessManager(self)
        self._tool_manager = ToolManager(self)
        self._pub_sub_manager = PubSubManager(self)
        self._package_manager = PackageManager(self)
        self._content_manager = ContentManager(self, main_window)
        self._style_manager = StyleManager(self)
        self._log_manager = LogManager(self)
        self._cache_manager = CacheManager(self)
        self._settings_manager = SettingsManager(self)
        self._navigation_manager = NavigationManager(self, main_window)

    def initialize(self):
        """ Initialize all managers. """
        self._settings_manager.initialize()
        self._app_manager.initialize()
        self._endpoint_manager.initialize()
        self._module_manager.initialize()
        self._process_manager.initialize()
        self._tool_manager.initialize()
        self._pub_sub_manager.initialize()
        self._package_manager.initialize()
        self._content_manager.initialize()
        self._style_manager.initialize()
        self._log_manager.initialize()
        self._cache_manager.initialize()
        self._navigation_manager.initialize()

    @property
    def app_manager(self) -> AppManager:
        """ Get the app manager. 
        
        Returns
        -------
            AppManager
                The app manager
        """
        return self._app_manager

    @property
    def endpoint_manager(self) -> EndpointManager:
        """ Get the endpoint manager. 
        
        Returns
        -------
            EndpointManager
                The endpoint manager
        """
        return self._endpoint_manager

    @property
    def module_manager(self) -> ModuleManager:
        """ Get the module manager. 
        
        Returns
        -------
            ModuleManager
                The module manager
        """
        return self._module_manager

    @property
    def process_manager(self) -> ProcessManager:
        """ Get the process manager. 
        
        Returns
        -------
            ProcessManager
                The process manager
        """
        return self._process_manager

    @property
    def tool_manager(self) -> ToolManager:
        """ Get the tool manager. 
        
        Returns
        -------
            ToolManager
                The tool manager
        """
        return self._tool_manager

    @property
    def pub_sub_manager(self) -> PubSubManager:
        """ Get the pub/sub manager. 
        
        Returns
        -------
            PubSubManager
                The pub/sub manager
        """
        return self._pub_sub_manager

    @property
    def package_manager(self) -> PackageManager:
        """ Get the package manager. 
        
        Returns
        -------
            PackageManager
                The package manager
        """
        return self._package_manager
    
    @property
    def content_manager(self) -> ContentManager:
        """ Get the content manager. 
        
        Returns
        -------
            ContentManager
                The content manager
        """
        return self._content_manager
    
    @property
    def style_manager(self) -> StyleManager:
        """ Get the style manager. 
        
        Returns
        -------
            StyleManager
                The style manager
        """
        return self._style_manager

    @property
    def log_manager(self) -> LogManager:
        """ Get the log manager. 
        
        Returns
        -------
            LogManager
                The log manager
        """
        return self._log_manager
    
    @property
    def cache_manager(self) -> CacheManager:
        """ Get the cache manager. 
        
        Returns
        -------
            CacheManager
                The cache manager
        """

        return self._cache_manager
    
    @property
    def settings_manager(self) -> SettingsManager:
        """ Get the settings manager. 
        
        Returns
        -------
            SettingsManager
                The settings manager
        """
        return self._settings_manager
    
    @property
    def navigation_manager(self) -> NavigationManager:  
        """ Get the navigation manager.
        
        Returns
        -------
            NavigationManager
                The navigation manager
        """
        return self._navigation_manager
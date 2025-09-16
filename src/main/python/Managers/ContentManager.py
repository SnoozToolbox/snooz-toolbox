"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
import gc

from Managers.Manager import Manager

class ContentManager(Manager):
    """ ContentManager manages the life-cycle of the main content of the application.
    
    There are three type of content: process content, tool content and app content.
    
    The process content is the content that will be displayed in the process tab. The schema
    block made of interconnected modules.

    The tool content is the content that will be displayed in the tool tab. The step-by-step
    interface.

    The app content is the content that will be displayed in the app tab.

    Whenever the user is requesting to load a process, a tool or an app, the content manager will
    ask the user if there is something to be saved. If not, it will unload the previous content 
    and load the new one.

    The content manager is not responsible for the actual content. It only manages the life cycle of
    the content.

    Note: A tool is always associated with a process. A process can run alone
    and is not always associated with a tool. This means that if we are loading
     a process, we must first unload any tool that was loaded first.

    Only one app can be loaded at a time. An app is independent from other tools and processes.
    Therefore when an app is loaded, the current opened tool or process are ignored.
    
    """

    def __init__(self, managers, main_window):
        """ Init the ContentManager. 
        
        Parameters
        ----------
        managers : Managers
            The managers of the application.
        main_window : MainWindow
            The main window of the application.
        """
        super().__init__(managers)
        self._main_window = main_window
        
        # Enum of state values, process or tool. Tools and process are in
        self._TOOL_STATE = "tool"
        self._PROCESS_STATE = "process"
        self._NO_STATE = None
        self._state = self._NO_STATE

    def initialize(self):
        pass
        
    def load_process_content(self, content):
        """ Load the content in the process tab. 
        
        Parameters
        ----------
        content : QWidget
            The content to load.
        """
        self._main_window.process_layout.addWidget(content)
        self._managers.navigation_manager.show_process()
        self._state = self._PROCESS_STATE

    def load_tool_content(self, content):
        """ Load the content in the tool tab. 

        Parameters
        ----------
        content : QWidget
            The content to load.
        """
        self._main_window.tool_layout.addWidget(content)
        self._managers.navigation_manager.show_tool()
        self._state = self._TOOL_STATE

    def load_app_content(self, content):
        """ Load the content in the app tab.

        Parameters
        ----------
        content : QWidget
            The content to load.
        """
        self._main_window.app_layout.addWidget(content)
        self._managers.navigation_manager.show_app()
        
    def ask_permission_to_load_process(self):
        """ Ask the user if there is something to be saved. """
        if self._state == self._TOOL_STATE:
            return self._managers.tool_manager.ask_unsaved()
        elif self._state == self._PROCESS_STATE:
            return self._managers.process_manager.ask_unsaved()
        else:
            return True
    
    def ask_permission_to_load_app(self):
        """ Ask the user if there is something to be saved. """
        return self._managers.app_manager.ask_unsaved()

    def unload_process_content(self):
        """ Unload the content in the process tab. """
        while self._main_window.process_layout.count():
            child = self._main_window.process_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self._managers.process_manager.unload_content()
        
        # GARBAGE COLLECTOR ALWAYS ACTIVATED :
        # Since the garbage collector is desabled in the MainWindow
        # we need to manually call the garbage collector
        #  calling the gc without input argument makes Snooz close    
        #gc.collect(1)

    def unload_tool_content(self):
        """ Unload the content in the tool tab. """
        while self._main_window.tool_layout.count():
            child = self._main_window.tool_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self._managers.tool_manager.unload_content()
    
        # GARBAGE COLLECTOR ALWAYS ACTIVATED :
        # Since the garbage collector is desabled in the MainWindow
        # we need to manually call the garbage collector
        #  calling the gc without input argument makes Snooz close    
        #gc.collect(1)
      
    def unload_app_content(self):
        """ Unload the content in the app tab. """
        while self._main_window.app_layout.count():
            child = self._main_window.app_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self._managers.app_manager.unload_content()

        # GARBAGE COLLECTOR ALWAYS ACTIVATED :
        # Since the garbage collector is desabled in the MainWindow
        # we need to manually call the garbage collector
        #  calling the gc without input argument makes Snooz close    
        #gc.collect(1)
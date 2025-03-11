"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from qtpy.QtWidgets import QMessageBox, QWidget, QVBoxLayout

from Managers.Manager import Manager
from Endpoints.EndpointHandlers.CustomEndpointHandler import CustomEndpointHandler

class AppManager(Manager):
    """AppManager handles the life cycle of an app.
    
    An app is a type of item that Snooz can load dynamically. As it names suggest, it's
    basically an full fledged application that runs within Snooz. Multiple apps can
    be registered in Snooz but only one app can run at the time.

    This manager handles the life cycle of an app. It is responsible for loading
    its dependencies and calling the AppPackageItem to load its content.
    """

    def __init__(self, managers):
        """Init the AppManager."""
        super().__init__(managers)
        self._is_loaded = False
        self._current_package_item = None
        self._app_view = None
        
    def initialize(self):
        """ Initialize the AppManager. """
        # app_activation_request are sent by AppPackageItem to activate the app.
        self._managers.pub_sub_manager.subscribe(self, "app_activation_request")
    
    def on_topic_update(self, topic, message, sender):
        """ On topic update. 
        
        This function is called by the pub_sub_manager when a topic update is received.

        Parameters
        ----------
            topic (str):    The topic
            message (str):  The message
            sender (obj):   The sender

        Returns
        -------
            None
        """
        if topic == "app_activation_request":
            # Ask the permission to load content, the content manager will ask the user if
            # there is something to be saved.
            is_allowed = self._managers.content_manager.ask_permission_to_load_app()
            if not is_allowed:
                return
            
            self._managers.content_manager.unload_app_content()
            try:
                self._load_content(sender, message)
            except Exception as exc:
                message = f"AppManager could load app content {exc}"
                self._managers.pub_sub_manager.publish(self, "show_error_message", message)
                self._managers.content_manager.unload_process_content()
                self._managers.content_manager.unload_tool_content()
                return
            
    def close_app(self):
        """ Close the app. """
        self._app_view.close_app()
        self._managers.content_manager.unload_app_content()

    def get_custom_hooks(self, custom_endpoint_name):
        """ Get the custom hooks. 
        
        Parameters
        ----------
            custom_endpoint_name (str):  The name of the custom endpoint
        """
        handler = self._managers.endpoint_manager.get_handler(CustomEndpointHandler.ENDPOINT_NAME)
        if custom_endpoint_name in handler.custom_endpoints:
            return handler.custom_endpoints[custom_endpoint_name]
        else:
            return []

    def unload_content(self):
        """ Unload the content of the app. """
        if self._app_view is not None:
            self._app_view.close_app()
        self._current_package_item = None
        self._is_loaded = False
        self._app_view = None
        self._managers.navigation_manager.hide_app_buttons()

    def ask_unsaved(self):
        """ Ask the user if there are unsaved changes. """
        if not self._is_loaded:
            return True
        
        if not self._app_view.is_dirty():
            return True
        
        # TODO Check if dirty and ask the user for save
        # Ask yes no answer
        dialog = QMessageBox()
        dialog.setWindowTitle("Unsaved work")
        dialog.setText("The current process has unsaved changes, do you want to save them before closing the process?")
        dialog.setStandardButtons(QMessageBox.Cancel |QMessageBox.Yes | QMessageBox.No)
        dialog.setDefaultButton(QMessageBox.No)
        result = dialog.exec_()
        return result != QMessageBox.Cancel
            
    def _load_content(self, package_item, params):
        """ Load the content of the app. 
        
        Parameters
        ----------
            sender (AppPackageItem): The app package item to load
            params (dict):  The parameters to pass to the app view
        """
        # Important to set the current package before loading it's dependencies
        self._current_package_item = package_item
        self._load_dependencies()

        # Create the app view
        self._app_view = self._current_package_item.create_app_view(params)

        # Form the parent widget
        self._root_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self._app_view)
        self._root_widget.setLayout(layout)

        # Load the content
        self._managers.content_manager.load_app_content(self._root_widget)
        self._is_loaded = True

        self._managers.navigation_manager.show_app_buttons()

    def _load_dependencies(self):
        """ Load the dependencies of the app. """

        # First thing, activate the package of the current item.
        package_name = self._current_package_item.package.name
        package_version = self._current_package_item.package.version
        self._managers.package_manager.activate_package(package_name, package_version)

        # Then activate all other external packages that are in the dependencies
        for dependency in self._current_package_item.description["dependencies"]:
            package_name = dependency["package_name"]
            package_version = dependency["package_version"]
            self._managers.package_manager.activate_package(package_name, package_version)

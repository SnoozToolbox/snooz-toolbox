"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
from qtpy.QtWidgets import QMessageBox, QWidget, QVBoxLayout

from Managers.Manager import Manager

class NavigationManager(Manager):
    """Navigation Manager
    """

    def __init__(self, managers, main_window):
        """Init the NavigationManager."""
        super().__init__(managers)
        self._main_window = main_window
        self._managers = managers
        
    def initialize(self):
        """ Initialize the AppManager. """
        if self._main_window is None:
            return
        
        self.hide_app_buttons()
        self.hide_process_button()
        self.hide_tool_button()

    def show_home(self):
        self._main_window.app_root_nav_frame.setVisible(False)
        self._main_window.tool_root_nav_frame.setVisible(False)
        self._main_window.process_root_nav_frame.setVisible(False)
        self._main_window.content_tabWidget.setCurrentIndex(0)

    def show_app(self):
        if len(self._main_window.app_root_nav_frame.children()) > 1:
            self._main_window.app_root_nav_frame.setVisible(True)
        else:
            self._main_window.app_root_nav_frame.setVisible(False)
        self._main_window.tool_root_nav_frame.setVisible(False)
        self._main_window.process_root_nav_frame.setVisible(False)
        self._main_window.content_tabWidget.setCurrentIndex(2)

    def show_process(self):
        if len(self._main_window.process_root_nav_frame.children()) > 1:
            self._main_window.process_root_nav_frame.setVisible(True)
        else:
            self._main_window.process_root_nav_frame.setVisible(False)
        self._main_window.tool_root_nav_frame.setVisible(False)
        self._main_window.app_root_nav_frame.setVisible(False)
        self._main_window.content_tabWidget.setCurrentIndex(3)
    
    def show_tool(self):
        if len(self._main_window.tool_root_nav_frame.children()) > 1:
            self._main_window.tool_root_nav_frame.setVisible(True)
        else:
            self._main_window.tool_root_nav_frame.setVisible(False)
        self._main_window.process_root_nav_frame.setVisible(False)
        self._main_window.app_root_nav_frame.setVisible(False)
        self._main_window.content_tabWidget.setCurrentIndex(1)

    def hide_app_buttons(self):
        self._main_window.app_pushButton.setVisible(False)
        self._main_window.close_app_pushButton.setVisible(False)

    def show_app_buttons(self):
        self._main_window.app_pushButton.setVisible(True)
        self._main_window.close_app_pushButton.setVisible(True)

    def show_process_button(self):
        self._main_window.process_pushButton.setVisible(True)

    def hide_process_button(self):
        self._main_window.process_pushButton.setVisible(False)

    def show_tool_button(self):
        self._main_window.tool_pushButton.setVisible(True)

    def hide_tool_button(self):
        self._main_window.tool_pushButton.setVisible(False)

    def add_app_widget(self, widget):
        self._main_window.app_buttons_layout.addWidget(widget)

    def remove_app_widget(self, widget):
        self._main_window.app_buttons_layout.removeWidget(widget)
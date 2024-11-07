"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
import json
import os

from qtpy import QtWidgets, QtGui, QtCore
from config import app_settings, settings
from config import C

class RecentWidget(QtWidgets.QWidget):
    """ Display a list of recent files """

    def __init__(self, managers, parent:QtWidgets.QWidget=None):
        super().__init__(parent)
        self._managers = managers
        self.setObjectName("RecentWidget")
        self.setLayout(QtWidgets.QVBoxLayout())
        self.render()
        self._managers.pub_sub_manager.subscribe(self,"file_opened")

    def on_topic_update(self, topic, message, sender):
        if topic == "file_opened":
            self._add_file(message)

    def render(self):
        """ Render the component. """

        # Helper function to create new clickable label
        def create_label(filepath:str):
            text = os.path.basename(filepath)
            label = QtWidgets.QLabel(text)
            label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            label.setStyleSheet(f"color: {C.clickable_link_color};")
            label.setToolTip(filepath)
            label.mousePressEvent = lambda e, filepath=filepath: self.on_file_click(filepath)
            return label

        # Helper function to create a header
        def create_header(header:str):
            label = QtWidgets.QLabel(header)
            header_font = QtGui.QFont()
            header_font.setPointSize(11)
            header_font.setBold(False)
            label.setFont(header_font)
            return label

        # Remove all widget from the layout
        self._clear_layout()

        # Get the list of recent files
        recent_files = app_settings.value(settings.recent_files, None)

        # Init the setting if it was not found
        if recent_files is None:
            app_settings.setValue(settings.recent_files, [])
            recent_files = []

        # Add a header
        header = create_header("Recent Files")
        self.layout().addWidget(header)

        # Add each file to the layout
        if isinstance(recent_files, str):
            recent_files = [recent_files]
            app_settings.setValue(settings.recent_files, recent_files)

        for filepath in recent_files:
            label = create_label(filepath)
            self.layout().addWidget(label)

    def _add_file(self, filepath:str):
        """ add a filename to the list of recent filenames """
        recent_files = app_settings.value(settings.recent_files)
        # Remove it if it was in the list already, this will have the effect
        # of placing it at the top.
        if filepath in recent_files:
            recent_files.remove(filepath)

        recent_files.insert(0, filepath)

        # Save the list of recent files to the settings
        app_settings.setValue(settings.recent_files, recent_files[0:10])

        self.render()

    def on_file_click(self, filepath:str):
        """ Handle the click event. Check if the file exist, if it doesn't, 
        remove it from the list and re-render. If it does, send a signal to the
        main window to open the file """

        # Check if the file exist, remove it if not
        if not os.path.isfile(filepath):
            # If not remove it.
            recent_files = app_settings.value(settings.recent_files)
            recent_files.remove(filepath)
            app_settings.setValue(settings.recent_files, recent_files)

            # Warn the user
            self._managers.pub_sub_manager.publish(self, "show_error_message", "File not found.")
            self.render()
            return

        is_allowed = self._managers.content_manager.ask_permission_to_load_process()
        if not is_allowed:
            return
        
        # Open the file in json and check if its a process or a tool
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                if data["item_type"] == "process":
                    self._managers.process_manager.open_process_file(filepath)
                elif data["item_type"] == "tool":
                    self._managers.tool_manager.load_workspace_from_file(filepath)
        except Exception as err:
            recent_files = app_settings.value(settings.recent_files)
            if filepath in recent_files:
                recent_files.remove(filepath)

            # Save the list of recent files to the settings
            app_settings.setValue(settings.recent_files, recent_files[0:10])
            self._managers.pub_sub_manager.publish(self, "show_error_message", f"Could not load file.{err}")

    def _clear_layout(self):
        """ Remove all children widget from the layout """
        while self.layout().count():
            child = self.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()

"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
DEBUG = False
import config
from qtpy.QtCore import QFile, QTextStream
from qtpy import QtGui

from Managers.Manager import Manager
import themes_rc

class Palette():
    def __init__(self):
        self.grid_background = QtGui.QColor(255, 255, 0)
        self.grid_line = QtGui.QColor(255, 255, 0)
        self.node_selection = QtGui.QColor(255, 255, 0)
        self.node_background_activated = QtGui.QColor(255, 255, 0)
        self.node_background_deactivated = QtGui.QColor(255, 255, 0)
        self.node_background_bypass = QtGui.QColor(255, 255, 0)
        self.node_border = QtGui.QColor(255, 255, 0)
        self.node_text = QtGui.QColor(255, 255, 0)
        self.node_socket_border = QtGui.QColor(255, 255, 0)
        self.node_socket_background = QtGui.QColor(255, 255, 0)

class Style():
    def __init__(self, name, palette, qss_filepath):
        self._name = name
        self._palette = palette
        self._qss_filepath = qss_filepath

    def activate(self):
        if self._qss_filepath is not None:
            file = QFile(self._qss_filepath)
            if file.open(QFile.ReadOnly | QFile.Text):
                stream = QTextStream(file)
                config.app_context.app.setStyleSheet(stream.readAll())
            else:
                print(f"StyleManager:Could not open file {file.errorString()}")

    @property
    def name(self):
        return self._name

    @property
    def palette(self):
        return self._palette

class StyleManager(Manager):
    def __init__(self, managers):
        super().__init__(managers)
        self._default_style = None
        self._styles = {}

        # Set Fusion as the base style for all others
        config.app_context.app.setStyle("Fusion")

    def initialize(self):
        pass

    @property
    def styles(self):
        return self._styles

    # Public functions
    def register_style(self, style):
        self._styles[style.name] = style

    def get_current_style(self):
        current_style_name = config.app_settings.value(config.settings.style)
        return self._styles[current_style_name]

    def set_default_style(self, style_name):
        self._default_style = style_name

    def load_user_style(self):
        current_style = config.app_settings.value(config.settings.style)
        if current_style is not None:
            self._set_style(current_style)
        else:
            self._set_style(self._default_style)

    # Private functions
    def _set_style(self, style_name):
        if style_name in self._styles:
            self._styles[style_name].activate()
            config.app_settings.setValue(config.settings.style, style_name)

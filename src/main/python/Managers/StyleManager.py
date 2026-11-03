"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
DEBUG = False
import json
import re

import config

# Import Qt modules - config.py provides stubs in headless mode via sys.modules
from qtpy.QtCore import QFile, QTextStream
from qtpy import QtGui

from Managers.Manager import Manager

# Import themes_rc conditionally since it's a Qt resource file
# themes_rc is a Qt resource file that requires PySide6
if not config.HEADLESS_MODE:
    import themes_rc
else:
    # Stub module for headless mode
    class themes_rc:
        pass

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
    # QPushButtons narrower than this keep a compact padding (see _compact_button_rules).
    COMPACT_BUTTON_MAX_WIDTH = 79

    def __init__(self, name, palette, qss_filepath, tokens_filepath=None):
        self._name = name
        self._palette = palette
        self._qss_filepath = qss_filepath
        self._tokens = load_tokens(tokens_filepath) if tokens_filepath is not None else {}

    def activate(self):
        if config.HEADLESS_MODE:
            return  # Skip style activation in headless mode
        if self._qss_filepath is not None:
            qss = read_text_file(self._qss_filepath)
            if qss is not None:
                qss = replace_tokens(qss, self._tokens)
                qss += self._compact_button_rules()
                config.app_context.app.setStyleSheet(qss)

    def _compact_button_rules(self):
        """ Rules giving a compact padding to the small QPushButtons (e.g. ">" or "...").

        The padding of the generic QPushButton rule would clip their text. Each
        small button also keeps the width of its maximum width, unless a minimum
        width was set in Qt Designer. "_q_stylesheet_minw" is set by Qt on the
        widgets whose minimum width comes from the style sheet: it keeps the rule
        when the widget is polished again.
        """
        rules = []
        for width in range(10, self.COMPACT_BUTTON_MAX_WIDTH + 1):
            button = f'QPushButton[maximumWidth="{width}"]'
            rules.append(f'{button} {{ padding-left: 0px; padding-right: 0px; }}')
            rules.append(f'{button}[minimumWidth="0"], {button}[_q_stylesheet_minw="true"] '
                f'{{ min-width: {width - 2}px; }}')
        return "\n" + "\n".join(rules) + "\n"

    @property
    def name(self):
        return self._name

    @property
    def palette(self):
        return self._palette

    @property
    def tokens(self):
        """ The colors of the style, by token name (see tokens.json of the theme). """
        return self._tokens


def read_text_file(filepath):
    """ Read a text file, from the file system or from the Qt resources (":/..."). """
    file = QFile(filepath)
    if not file.open(QFile.ReadOnly | QFile.Text):
        print(f"StyleManager:Could not open file {filepath}: {file.errorString()}")
        return None
    text = QTextStream(file).readAll()
    file.close()
    return text


def load_tokens(filepath):
    """ Load the color tokens of a theme from a json file. """
    text = read_text_file(filepath)
    if text is None:
        return {}
    return json.loads(text)


def replace_tokens(qss, tokens):
    """ Replace each @token of the style sheet by its value. """
    def replace(match):
        name = match.group(1)
        if name not in tokens:
            print(f"StyleManager:Unknown style sheet token @{name}")
            return match.group(0)
        return tokens[name]
    return _TOKEN_RE.sub(replace, qss)


_TOKEN_RE = re.compile(r"@([A-Za-z_][A-Za-z0-9_]*)")

class StyleManager(Manager):
    def __init__(self, managers):
        super().__init__(managers)
        self._default_style = None
        self._styles = {}

        # Set Fusion as the base style for all others (only in GUI mode)
        if not config.HEADLESS_MODE:
            from commons.theme_helpers import SnoozStyle
            config.app_context.app.setStyle(SnoozStyle())

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

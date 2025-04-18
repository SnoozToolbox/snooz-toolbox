"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from qtpy import QtGui, QtCore
import importlib.util
is_dev = True

""" Global constants """
LISTBOX_MIMETYPE = "application/x-item"

class ZValues:
    pass
    
Z = ZValues()
Z.CONNECTION = 0
Z.NODE = 1
Z.PORT = 2
Z.SOCKET = 3
Z.NODE_VIEW = 4

""" Global variables """
app_context = {}

class Colors:
    pass
    
C = Colors()
C.text_color = QtGui.QColor(225, 227, 229)
C.border_color = QtGui.QColor(225, 227, 229, 255)
C.background_color = QtGui.QColor(51, 51, 51,255)
C.background_color_X = '#333333'
C.clickable_link_color = '#3daee9'
C.grid_background_color = QtGui.QColor(21, 21, 21,255)
C.selected_border_color = QtGui.QColor(61, 174, 233,255)
C.text_foreground_color_X = '#e1e3e5'

font_size = 12

app_settings = QtCore.QSettings("CEAMS", "Snooz")

class Settings:
    pass
settings = Settings()
settings.recent_files = "recent_files"
settings.recent_presets = "recent_presets"
settings.dev_mode = "dev_mode"
settings.style = "style"
settings.packages = "packages"
settings.skip_beta_disclaimer = "skip_beta_disclaimer"
settings.activated_package_items = "activated_package_items"
settings.active_api_version = "2.0.0"

DOCUMENTATION_URL = "https://snooz-toolbox-documentation.readthedocs.io/latest/"

""" fbs pro validation """
def is_fbs_available():
    try:
        spec = importlib.util.find_spec("fbs_runtime.application_context")
        # Case where fbs is not installed at all
        if spec is None:
            return False
        
        # Case where fbs pro is installed
        from fbs_runtime.application_context import PySide6
        return True
    except (ImportError, ModuleNotFoundError):
        # Case where fbs is free tier
        return False
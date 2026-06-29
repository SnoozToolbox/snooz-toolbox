"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from .SpindleDetectorA7 import SpindleDetectorA7
from .SpindleDetectorA7SettingsView import SpindleDetectorA7SettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .SpindleDetectorA7ResultsView import SpindleDetectorA7ResultsView
    from .Ui_SpindleDetectorA7ResultsView import Ui_SpindleDetectorA7ResultsView
    from .Ui_SpindleDetectorA7SettingsView import Ui_SpindleDetectorA7SettingsView
else:
    # Create stub classes for headless mode
    SpindleDetectorA7ResultsView = None
    Ui_SpindleDetectorA7ResultsView = None
    Ui_SpindleDetectorA7SettingsView = None

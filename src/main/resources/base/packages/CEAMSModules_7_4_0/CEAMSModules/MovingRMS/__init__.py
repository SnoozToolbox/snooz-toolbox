"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .MovingRMS import MovingRMS
from .MovingRMSSettingsView import MovingRMSSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .MovingRMSResultsView import MovingRMSResultsView
    from .Ui_MovingRMSResultsView import Ui_MovingRMSResultsView
    from .Ui_MovingRMSSettingsView import Ui_MovingRMSSettingsView
else:
    # Create stub classes for headless mode
    MovingRMSResultsView = None
    Ui_MovingRMSResultsView = None
    Ui_MovingRMSSettingsView = None

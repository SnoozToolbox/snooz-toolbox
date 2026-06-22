"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .DetectionView import DetectionView
from .DetectionViewSettingsView import DetectionViewSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .DetectionViewResultsView import DetectionViewResultsView
    from .Ui_DetectionViewResultsView import Ui_DetectionViewResultsView
    from .Ui_DetectionViewSettingsView import Ui_DetectionViewSettingsView
else:
    # Create stub classes for headless mode
    DetectionViewResultsView = None
    Ui_DetectionViewResultsView = None
    Ui_DetectionViewSettingsView = None

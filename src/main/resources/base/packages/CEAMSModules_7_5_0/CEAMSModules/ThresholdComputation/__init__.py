"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .ThresholdComputation import ThresholdComputation
from .ThresholdComputationSettingsView import ThresholdComputationSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .ThresholdComputationResultsView import ThresholdComputationResultsView
    from .Ui_ThresholdComputationResultsView import Ui_ThresholdComputationResultsView
    from .Ui_ThresholdComputationSettingsView import Ui_ThresholdComputationSettingsView
else:
    # Create stub classes for headless mode
    ThresholdComputationResultsView = None
    Ui_ThresholdComputationResultsView = None
    Ui_ThresholdComputationSettingsView = None

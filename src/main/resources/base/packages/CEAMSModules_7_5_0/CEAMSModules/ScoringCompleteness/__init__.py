"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .ScoringCompleteness import ScoringCompleteness
from .ScoringCompletenessSettingsView import ScoringCompletenessSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .ScoringCompletenessResultsView import ScoringCompletenessResultsView
    from .Ui_ScoringCompletenessResultsView import Ui_ScoringCompletenessResultsView
    from .Ui_ScoringCompletenessSettingsView import Ui_ScoringCompletenessSettingsView
else:
    # Create stub classes for headless mode
    ScoringCompletenessResultsView = None
    Ui_ScoringCompletenessResultsView = None
    Ui_ScoringCompletenessSettingsView = None

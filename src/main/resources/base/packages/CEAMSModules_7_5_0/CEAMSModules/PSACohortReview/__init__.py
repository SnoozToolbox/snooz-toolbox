"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .PSACohortReview import PSACohortReview
from .PSACohortReviewSettingsView import PSACohortReviewSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .PSACohortReviewResultsView import PSACohortReviewResultsView
    from .Ui_PSACohortReviewResultsView import Ui_PSACohortReviewResultsView
    from .Ui_PSACohortReviewSettingsView import Ui_PSACohortReviewSettingsView
else:
    # Create stub classes for headless mode
    PSACohortReviewResultsView = None
    Ui_PSACohortReviewResultsView = None
    Ui_PSACohortReviewSettingsView = None

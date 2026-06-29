"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
from .DetectionsCohortReview import DetectionsCohortReview
from .DetectionsCohortReviewSettingsView import DetectionsCohortReviewSettingsView

# Only import ResultsView and UI classes in non-headless mode to avoid matplotlib/Qt dependencies
import config
if not config.HEADLESS_MODE:
    from .DetectionsCohortReviewResultsView import DetectionsCohortReviewResultsView
    from .Ui_DetectionsCohortReviewResultsView import Ui_DetectionsCohortReviewResultsView
    from .Ui_DetectionsCohortReviewSettingsView import Ui_DetectionsCohortReviewSettingsView
else:
    # Create stub classes for headless mode
    DetectionsCohortReviewResultsView = None
    Ui_DetectionsCohortReviewResultsView = None
    Ui_DetectionsCohortReviewSettingsView = None

"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2024
See the file LICENCE for full license details.
"""
import os


def _configure_numeric_runtime():
	"""Keep BLAS/OpenMP single-threaded in EEGInspector worker threads."""
	thread_limits = {
		'OPENBLAS_NUM_THREADS': '1',
		'OMP_NUM_THREADS': '1',
		'MKL_NUM_THREADS': '1',
		'NUMEXPR_NUM_THREADS': '1',
	}
	for env_name, env_value in thread_limits.items():
		os.environ.setdefault(env_name, env_value)


_configure_numeric_runtime()

from .EEGInspectorView import EEGInspectorView
from .ui.Ui_EEGInspectorView import Ui_EEGInspectorView
from .ui.Ui_MontageSelection import Ui_MontageSelection
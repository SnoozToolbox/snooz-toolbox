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

'''
When configuring the application's settings under QSettings, it creates new folder (key) with said settings in the OS system.

In Windows, open the Registry Editor, then: Computer>HKEY_CURRENT_USER>Software>CEAMS>Snooz

In macOS, in a terminal, look under ~/Library/Preferences/, you can then inspect that directory and look for "ceams" with the following
command: `ls | grep ceams`, you should then see a or multiple .plist files, those are the equivalent of the key folder in the Windows Registry.

When the user downloads a new version of Snooz, It is preferable to create a new settings location for that version, as some old features
may be deprecated with the new version of Snooz.

For a developer, normally fbs (pro version) should not be installed on the environment. The developer will then be able to have a common settings folder
no matter which version of Snooz he may be using.
'''
try:
    from fbs_runtime import PUBLIC_SETTINGS
    if not is_dev:
        version = PUBLIC_SETTINGS["version"]
        settings_key = f"Snooz_{version}"
    else:
        settings_key = f"Snooz"
        version = 'dev'
except ImportError:
    settings_key = f"Snooz"
    version = 'dev'

app_settings = QtCore.QSettings("CEAMS", settings_key)

if app_settings.value("app/version", "") == "":
    app_settings.clear()
    app_settings.setValue("app/version", version)

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

# Memory management configuration
class MemoryConfig:
    """Memory management constants and configuration for Snooz application."""

    # Modules that should be protected ONLY during execution (to prevent crashes)
    # These are C++ extensions that cannot be safely reimported while running
    # BUT they WILL be removed on shutdown for complete memory cleanup
    PROTECTED_DURING_EXECUTION = {
        'torch', 'torch.nn', 'torch.optim', 'torch.utils', 'torch.cuda',
        'torch.jit', 'torch.autograd', 'torch.distributions', 'torch.fft',
        'torch.linalg', 'torch.sparse', 'torch.special', 'torch.futures',
        'torchvision', 'torchaudio', 'torch._C', 'torch._dynamo',
        'numpy', 'scipy', 'sklearn', 'cv2', 'tensorflow', 'keras',
        'numba', 'numba.core', 'numba.typed', 'numba.types', 'numba.cuda',
        'numba.experimental', 'numba.misc', 'numba.np', 'numba.cpython'
    }

    # Modules that can be safely removed during execution (package changes, etc.)
    # These are large modules without C++ extensions that cause crashes
    SAFE_TO_REMOVE_DURING_EXECUTION = [
        'numpy.random',
        'numpy.lib',
        'numpy.ma',
        'numpy.matrixlib',
        'numpy.polynomial',
        'scipy.stats',
        'scipy.signal',
        'scipy.sparse',
        'scipy.optimize',
        'scipy.interpolate',
        'sklearn.utils',
        'sklearn.preprocessing',
        'sklearn.metrics',
        'matplotlib.pyplot',
        'matplotlib.backends',
        'pandas',
        'seaborn',
    ]

    # On shutdown: ALL modules are removed for complete memory cleanup
    # No exceptions - everything goes for maximum memory release

# Global memory config instance
memory_config = MemoryConfig()
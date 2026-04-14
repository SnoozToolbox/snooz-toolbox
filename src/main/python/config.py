"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
import os
import sys
import importlib.util

is_dev = True

# Check if running in headless mode
HEADLESS_MODE = os.environ.get('SNOOZ_HEADLESS', 'false').lower() == 'true'

# In headless mode, create robust stub modules for Qt imports
if HEADLESS_MODE:
    import types
    
    # Create a proper stub base class that can be inherited from
    class StubBase:
        """Base stub class that can be used in inheritance and handles any attribute access."""
        def __init__(self, *args, **kwargs):
            pass
        def __getattr__(self, name):
            return StubBase()
        def __call__(self, *args, **kwargs):
            return StubBase()
        def __getitem__(self, key):
            return StubBase()
        def __setitem__(self, key, value):
            pass
    
    # Universal stub instance for when we need to return an instance (not a class)
    UniversalStub = StubBase()
    
    # Create stub modules for all Qt-related imports
    def create_stub_module(name):
        stub = types.ModuleType(name)
        
        # Add __getattr__ to handle any attribute access (Python 3.7+)
        def module_getattr(attr):
            # If it's a known submodule, return a stub for it
            submodules = ['QtCore', 'QtGui', 'QtWidgets', 'QtWebEngineWidgets']
            if attr in submodules:
                submod_name = f'{name}.{attr}' if '.' in name else f'{name}.{attr}'
                if submod_name not in sys.modules:
                    sys.modules[submod_name] = create_stub_module(submod_name)
                return sys.modules[submod_name]
            # Return the class itself (not an instance) so it can be used in inheritance
            return StubBase
        
        stub.__getattr__ = module_getattr
        
        # Add common classes that are frequently imported
        if 'QtCore' in name:
            # QCoreApplication needs special methods
            class QCoreApplicationStub(StubBase):
                @staticmethod
                def translate(context, text, disambig=None):
                    return text
                @staticmethod
                def processEvents():
                    pass
            stub.QCoreApplication = QCoreApplicationStub
            stub.QObject = StubBase
            stub.Signal = StubBase
            stub.Qt = StubBase
            stub.QSettings = StubBase
        
        if 'QtWidgets' in name or 'QtWebEngineWidgets' in name:
            stub.QApplication = StubBase
            stub.QWebEngineView = StubBase
            stub.QWebEnginePage = StubBase
            stub.QWidget = StubBase
        
        if 'QtGui' in name:
            stub.QColor = StubBase
        
        if name == 'shiboken6':
            stub.delete = lambda obj: None
        
        return stub
    
    # Register stub modules before any imports
    # Only register modules actually used in this project (PySide6, qtpy, shiboken6)
    qt_parent_modules = ['PySide6', 'qtpy', 'shiboken6']
    for mod_name in qt_parent_modules:
        sys.modules[mod_name] = create_stub_module(mod_name)
    
    # Register submodules
    qt_submodules = [
        'PySide6.QtCore', 'PySide6.QtGui', 'PySide6.QtWidgets', 'PySide6.QtWebEngineWidgets',
        'qtpy.QtCore', 'qtpy.QtGui', 'qtpy.QtWidgets', 'qtpy.QtWebEngineWidgets'
    ]
    for mod_name in qt_submodules:
        sys.modules[mod_name] = create_stub_module(mod_name)
    
    # Create stub classes for use in this module
    class QtGui:
        QColor = StubBase
    
    class QtCore:
        QObject = StubBase
        QSettings = StubBase
else:
    # Import real Qt modules
    from qtpy import QtGui, QtCore

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

if not HEADLESS_MODE:
    app_settings = QtCore.QSettings("CEAMS", settings_key)
    if app_settings.value("app/version", "") == "":
        app_settings.clear()
        app_settings.setValue("app/version", version)
else:
    # Use a simple dict-based settings for headless mode
    class HeadlessSettings:
        def __init__(self):
            self._data = {}
        def value(self, key, default=None):
            return self._data.get(key, default)
        def setValue(self, key, value):
            self._data[key] = value
        def clear(self):
            self._data.clear()
    app_settings = HeadlessSettings()
    if app_settings.value("app/version", "") == "":
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
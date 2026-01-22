#!/usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""
import argparse
import datetime
import json
import multiprocessing
import os
import sys

# Check for --headless flag or --f flag early (before any imports)
# This allows headless mode to be set via command line argument
# When using --f (console mode), automatically enable headless mode
if '--headless' in sys.argv or '--f' in sys.argv:
    os.environ['SNOOZ_HEADLESS'] = 'true'

# Import config early - it will set up Qt stubs if in headless mode
import config

# Set QT_API only if not in headless mode
if not config.HEADLESS_MODE:
    os.environ['QT_API'] = 'pyside6'

# Set NUMBA cache to user temp directory (works on Windows, macOS, Linux)
import tempfile
numba_cache_dir = os.path.join(tempfile.gettempdir(), 'snooz_numba_cache')
os.makedirs(numba_cache_dir, exist_ok=True)
os.environ["NUMBA_CACHE_DIR"] = numba_cache_dir
# To disable numba cache
# os.environ["NUMBA_DISABLE_CACHE"] = "1"

# Hack until I figure out how to properly setup FBS so it includes them when freezing
# in a way that is available to the external packages.
# DONT REMOVE (but skip in headless mode since widgets require Qt)
if not config.HEADLESS_MODE:
    import widgets
from Managers.Managers import Managers
import module_dependencies
import mne
from mne import io, _fiff
# DONT REMOVE

# Import ApplicationContext based on mode
if config.HEADLESS_MODE:
    from runtime.application_context.headless import HeadlessApplicationContext as ApplicationContext
elif config.is_fbs_available():
    if not config.is_dev:
        from fbs_runtime import PUBLIC_SETTINGS
    from fbs_runtime.application_context.PySide6 import ApplicationContext
else:
    from runtime.application_context import ApplicationContext

if not config.HEADLESS_MODE:
    from MainWindow import MainWindow
    from window_geometry import calculate_window_geometry

class AppContext(ApplicationContext):
    def run(self, filename=None):
        config.app_context = self
        if filename is None:
            if config.HEADLESS_MODE:
                raise RuntimeError("Cannot run GUI mode in headless environment. Use --f flag to run a process file.")
            window = MainWindow()
            if not config.is_dev:
                version = PUBLIC_SETTINGS['version']
                window.setWindowTitle("Snooz beta-" + version)
            else:
                window.setWindowTitle("Snooz (DEV)")
            
            if not config.HEADLESS_MODE:
                # Calculate and apply window geometry based on screen resolution
                calculate_window_geometry(window)
            window.show()
            return self.app.exec_() if self.app else None
        
        else:
            executeConsole(filename)
            return None

def main():
    parser = argparse.ArgumentParser(description='Snooz')
    parser.add_argument("--f", help="The process description file in JSON format.")
    parser.add_argument("--headless", action="store_true", help="Run in headless mode (no GUI dependencies).")
    args, unknown = parser.parse_known_args()

    # Redirect stdout/stderr to avoid terminal messages from joblib, etc., in packaged mode
    if not config.is_dev and not config.HEADLESS_MODE:
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')

    app = AppContext()

    if args.f is not None:
        sys.exit(app.run(args.f))
    else:
        if config.HEADLESS_MODE:
            print("ERROR: Cannot run GUI mode in headless environment. Use --f flag to run a process file.")
            sys.exit(1)
        sys.exit(app.run())

def executeConsole(filename):
    if os.path.isfile(filename):
        with open(filename) as process_file:

            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")

            # Create all managers.
            managers = Managers(None)
            managers.initialize()

            # Read process JSON file
            print("Reading file:" + filename)
            json_string = process_file.read()
            json_data = json.loads(json_string)

            success = managers.process_manager.load_dependencies_from_description(json_data)
            if not success:
                print("ERROR Could not load dependencies.")
                return
            
            managers.process_manager.use_multithread = False
            # Call run_process or similar method that doesn't depend on Qt threading
            managers.process_manager.run_console(json_data)

            # Write the logs
            base_name = os.path.splitext(filename)[0]
            log_filename = base_name + "_" + formatted_datetime + ".log"
            with open(log_filename, "w") as file:

                # Write content to the file
                for (id, log) in managers.log_manager.timeline_logs:
                    file.write(f"{id} {log}\n")

            print("Process completed.")
    else:
        print("ERROR Could not find file:" + filename)
    
if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
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
os.environ['QT_API'] = 'pyside6'
os.environ["MNE_USE_LAZY_IMPORT"] = "0"
import sys

# Hack until I figure out how to properly setup FBS so it include them when freezing
# in a way that is available to the external packages.
# DONT REMOVE
import widgets
from Managers.Managers import Managers
import module_dependencies
import mne
from mne import io, _fiff
# DONT REMOVE

import config

if config.is_fbs_available():
    if not config.is_dev:
        from fbs_runtime import PUBLIC_SETTINGS
    from fbs_runtime.application_context.PySide6 import ApplicationContext
else:
    from runtime.application_context import ApplicationContext


from MainWindow import MainWindow

class AppContext(ApplicationContext):
    def run(self, filename=None):
        config.app_context = self
        if filename is None:
            window = MainWindow()
            if not config.is_dev:
                version = PUBLIC_SETTINGS['version']
                window.setWindowTitle("Snooz beta-" + version)
            else:
                window.setWindowTitle("Snooz (DEV)")
            window.resize(900, 700)
            window.show()
            return self.app.exec_()
        
        else:
            executeConsole(filename)
            return None

def main():
    parser = argparse.ArgumentParser(description='Snooz')
    parser.add_argument("--f", help="The process description file in JSON format.")
    args, unknown = parser.parse_known_args()

    app = AppContext()

    if args.f is not None:
        sys.exit(app.run(args.f))
    else:
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
            managers.process_manager.run(json_data)

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
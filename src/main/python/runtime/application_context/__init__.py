"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.


This file was highly inspired from the fbs library. It contains the necessary implementation to run the application without needing
a pro version of fbs, thus making it possible for developers without the pro version of fbs to be able to create tools for Snooz.

Although the logic remains the same, some methods were optimized as the purpose of the file is only to run the application, not to create
installers or packaging the application. If there is a need to create such entities, the user will have to obtain a pro version of fbs.
"""
import errno
import os
from functools import cached_property
from pathlib import Path

from PySide6.QtWidgets import QApplication

from runtime import platform
from runtime.platform import is_linux


class ApplicationContext:
    def __init__(self):
        self.app # Initialization of the QApplication

    def get_resource(self, *rel_path):
        return self._resource_locator.locate(*rel_path)
    
    @cached_property
    def app(self):
        result = QApplication([])
        result.setApplicationName("Snooz - Dev Mode - No FBS")
        result.setApplicationVersion("beta")

        return result

    @cached_property
    def _resource_locator(self):
        return ResourceLocator(self.get_resource_dirs())
    
    def get_resource_dirs(self):
        project_dir = Path(self._get_project_dir())
        resources = project_dir / "src/main/resources"
        return [project_dir / 'src/main/icons'] + [
            resources / profile for profile in reversed(self.get_default_profiles())
        ]
    
    def _get_project_dir(self):
        result =  Path(os.getcwd())
        while result != result.parent:
            if (result / 'src' / 'main' / 'python').is_dir():
                return str(result)
            result = result.parent    
        raise RuntimeError('Could not determine the project base directory. '
                        ' Was expceting src/main/python')
    
    def get_default_profiles(self):
        profiles = ['base', 'secret', platform.name().lower()]

        if is_linux():
            profiles.extend(
                [distro for distro in ("ubuntu", "arch", "fedora") if globals()[f"is_{distro}"]()]
            )

        return profiles

class ResourceLocator:
    def __init__(self, resources_dirs):
        self._dirs = resources_dirs
    def locate(self, *rel_path):
        for resource_dir in self._dirs:
            resource_path = os.path.join(resource_dir, *rel_path)
            if os.path.exists(resource_path):
                return os.path.realpath(resource_path)
        raise FileNotFoundError(
            errno.ENOENT, 'Could not locate resource', os.sep.join(rel_path)
        )
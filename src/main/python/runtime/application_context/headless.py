"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.

Headless ApplicationContext for running Snooz without GUI dependencies.
This allows execution on Compute Canada and other headless servers.
"""
import errno
import os
from functools import cached_property
from pathlib import Path

from runtime import platform
from runtime.platform import is_linux, is_arch, is_fedora, is_ubuntu


class HeadlessApplicationContext:
    """Headless version of ApplicationContext that doesn't require Qt."""
    
    def __init__(self):
        pass

    def get_resource(self, *rel_path):
        return self._resource_locator.locate(*rel_path)
    
    @property
    def app(self):
        """Return None for headless mode - no QApplication needed."""
        return None

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
            # Check for specific Linux distributions
            distro_checks = {
                'ubuntu': is_ubuntu,
                'arch': is_arch,
                'fedora': is_fedora
            }
            profiles.extend(
                [distro for distro, check_func in distro_checks.items() if check_func()]
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


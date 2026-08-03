"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.

Shared resource-resolution logic for GUI and headless application contexts.
"""
import errno
import os
import sys
from functools import cached_property
from pathlib import Path

from runtime import platform
from runtime.platform import is_linux, is_arch, is_fedora, is_ubuntu


class BaseResourceApplicationContext:
    """Common context behavior shared by GUI and headless modes."""

    def get_resource(self, *rel_path):
        return self._resource_locator.locate(*rel_path)

    @cached_property
    def _resource_locator(self):
        return ResourceLocator(self.get_resource_dirs())

    def get_resource_dirs(self):
        project_dir = self._get_project_dir()
        if project_dir is not None:
            project_dir = Path(project_dir)
            resources = project_dir / "src/main/resources"
            search_dirs = [project_dir / "src/main/icons"] + [
                resources / profile for profile in reversed(self.get_default_profiles())
            ]
            return [path for path in search_dirs if path.exists()]

        resources_root = self._get_installed_resources_root()
        search_dirs = [resources_root / profile for profile in reversed(self.get_default_profiles())]
        existing_dirs = [path for path in search_dirs if path.exists()]

        # Some frozen builds flatten the selected resource profile at the root
        # (e.g. packages/, models/, fonts/) instead of base/packages.
        if (resources_root / "packages").is_dir():
            if existing_dirs and any((path / "packages").is_dir() for path in existing_dirs):
                return existing_dirs
            return [resources_root] + existing_dirs

        if existing_dirs:
            return existing_dirs

        return existing_dirs

    def _get_project_dir(self):
        result = Path(os.getcwd())
        while result != result.parent:
            if (result / "src" / "main" / "python").is_dir():
                return str(result)
            result = result.parent
        return None

    def _get_installed_resources_root(self):
        candidate_roots = [
            Path(os.getcwd()),
            Path(sys.executable).resolve().parent,
            Path(sys.executable).resolve().parent / "_internal",
            Path(__file__).resolve(),
        ]

        meipass = getattr(sys, "_MEIPASS", None)
        if meipass:
            candidate_roots.append(Path(meipass))

        for root in candidate_roots:
            current = root if root.is_dir() else root.parent
            for _ in range(10):
                if (current / "base").is_dir():
                    return current
                if (current / "resources" / "base").is_dir():
                    return current / "resources"
                if (current / "packages").is_dir():
                    return current
                if (current / "resources" / "packages").is_dir():
                    return current / "resources"
                if current == current.parent:
                    break
                current = current.parent

        raise RuntimeError(
            "Could not determine runtime resources directory. Expected either src/main/resources in dev mode or a directory containing base profile in installed mode."
        )

    def get_default_profiles(self):
        profiles = ["base", "secret", platform.name().lower()]

        arch_profile = platform.profile_name()
        if arch_profile not in profiles:
            profiles.append(arch_profile)

        if is_linux():
            distro_checks = {
                "ubuntu": is_ubuntu,
                "arch": is_arch,
                "fedora": is_fedora,
            }
            profiles.extend([distro for distro, check_func in distro_checks.items() if check_func()])

        return profiles


class ResourceLocator:
    def __init__(self, resources_dirs):
        self._dirs = resources_dirs

    def locate(self, *rel_path):
        for resource_dir in self._dirs:
            resource_path = os.path.join(resource_dir, *rel_path)
            if os.path.exists(resource_path):
                return os.path.realpath(resource_path)
        raise FileNotFoundError(errno.ENOENT, "Could not locate resource", os.sep.join(rel_path))

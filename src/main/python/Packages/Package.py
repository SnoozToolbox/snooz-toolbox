"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
from Packages.PackageVersion import PackageVersion

class Package(object):
    def __init__(self, name, managers):
        self._name = name
        self._package_versions = []
        self._active_version = None
        self._managers = managers

    # Properties
    @property
    def name(self):
        return self._name
    
    @property
    def package_versions(self):
        return self._package_versions
    
    @property
    def active_version(self):
        return self._active_version

    @active_version.setter
    def active_version(self, value):
        self._active_version = value

    @property
    def latest_version(self):
        if len(self._package_versions) == 0:
            return None

        return self._package_versions[0]

    # Public methods
    def get_package_version(self, package_version_number):
        for package_version in self._package_versions:
            if package_version.version == package_version_number:
                return package_version
        return None
    
    def load_package_version(self, package_path, is_native=False):
        package_version = PackageVersion(package_path, self._managers, is_native)
        self.add_package_version(package_version)
        
    def add_package_version(self, package_version):
        self._package_versions.append(package_version)
        self._package_versions.sort(key=self._version_to_int, reverse=True)

    def activate_latest_version(self):
        if len(self._package_versions) == 0:
            self._active_version = None
            return
        
        self._active_version = self._package_versions[0]

    def register_active_version_hooks(self):
        if self._active_version is None:
            return
        
        self._active_version.register_hooks()

    def unregister_active_version_hooks(self):
        if self._active_version is None:
            return
        
        self._active_version.unregister_hooks()
    
    # Private methods
    def _version_to_int(self, package_version):
        '''
        Convert from a string representation of a version: 0.1.1 to an int: 11
        examples:
        0.0.1 -> 1
        0.1.0 -> 10
        1.0.0 -> 100
        1.1 -> 110
        1 -> 100

            Parameters:
                package_version (PackageVersion): The PackageVersion that will be sorted

            Returns:
                v_int (int): An int representation of the PackageVersion's version.
        '''
        v = package_version.version.split(".")
        while len(v) < 3:
            v.append("0")

        v_string = ''.join(v)
        v_int = int(v_string)

        return v_int
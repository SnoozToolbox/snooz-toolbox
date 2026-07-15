from pathlib import Path

from PyInstaller.utils.hooks import collect_all, collect_data_files, get_package_paths

# lazy_loader needs sibling stub files on disk next to the mne package modules.
# Keep mne as loose .py files (not only in PYZ) so mne/__init__.pyi can be present next to it.
module_collection_mode = "py"

# One hook file per dependency keeps packaging behavior explicit and debuggable.
datas, binaries, hiddenimports = collect_all("mne")
# Request all type stubs packaged by mne.
datas += collect_data_files("mne", includes=["**/*.pyi", "*.pyi"])

package_base, package_dir = get_package_paths("mne")
init_stub = Path(package_dir) / "__init__.pyi"
if init_stub.exists():
	datas.append((str(init_stub), "mne"))

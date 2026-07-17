from pathlib import Path

from PyInstaller.utils.hooks import collect_all, collect_data_files, collect_submodules, get_package_paths

# lazy_loader needs sibling stub files on disk next to the mne package modules.
# Keep mne as loose .py files (not only in PYZ) so mne/__init__.pyi can be present next to it.
module_collection_mode = {"mne": "py"}

# One hook file per dependency keeps packaging behavior explicit and debuggable.
datas, binaries, hiddenimports = collect_all("mne")
hiddenimports += collect_submodules("mne")
hiddenimports += ["mne.utils._logging"]

# Request all type stubs packaged by mne.
datas += collect_data_files("mne", includes=["**/*.pyi", "*.pyi"])

package_base, package_dir = get_package_paths("mne")
init_stub = Path(package_dir) / "__init__.pyi"
if init_stub.exists():
	datas.append((str(init_stub), "mne"))

print(f"[hook-mne] package_dir={package_dir}")
print(f"[hook-mne] init_stub_exists={init_stub.exists()} path={init_stub}")
print(f"[hook-mne] datas={len(datas)} binaries={len(binaries)} hiddenimports={len(hiddenimports)}")

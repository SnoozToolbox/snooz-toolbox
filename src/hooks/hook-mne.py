from pathlib import Path

from PyInstaller.utils.hooks import collect_all, collect_data_files, get_package_paths

# One hook file per dependency keeps packaging behavior explicit and debuggable.
datas, binaries, hiddenimports = collect_all("mne")
# lazy_loader expects .pyi stubs to exist next to package modules at runtime.
datas += collect_data_files("mne", includes=["**/*.pyi"])

package_base, package_dir = get_package_paths("mne")
init_stub = Path(package_dir) / "__init__.pyi"
if init_stub.exists():
	datas.append((str(init_stub), "mne"))

from PyInstaller.utils.hooks import collect_all, collect_data_files

# One hook file per dependency keeps packaging behavior explicit and debuggable.
datas, binaries, hiddenimports = collect_all("mne")
# lazy_loader expects .pyi stubs to exist next to package modules at runtime.
datas += collect_data_files("mne", includes=["**/*.pyi"])

from PyInstaller.utils.hooks import collect_all

# One hook file per dependency keeps packaging behavior explicit and debuggable.
datas, binaries, hiddenimports = collect_all("mne")

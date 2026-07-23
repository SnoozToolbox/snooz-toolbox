from PyInstaller.utils.hooks import collect_all, collect_data_files

datas, binaries, hiddenimports = collect_all("yasa")
datas += collect_data_files("yasa", includes=["**/*.pyi"])

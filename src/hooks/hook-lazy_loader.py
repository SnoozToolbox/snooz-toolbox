from PyInstaller.utils.hooks import collect_all, collect_data_files

datas, binaries, hiddenimports = collect_all("lazy_loader")
datas += collect_data_files("lazy_loader", includes=["**/*.pyi"])

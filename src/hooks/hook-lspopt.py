from PyInstaller.utils.hooks import collect_all, collect_data_files

datas, binaries, hiddenimports = collect_all("lspopt")
datas += collect_data_files("lspopt", includes=["**/*.pyi"])

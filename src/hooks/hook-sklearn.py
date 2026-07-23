from PyInstaller.utils.hooks import collect_all, collect_dynamic_libs

# Keep scikit-learn packaging explicit and stable across platforms.
# collect_all gathers python modules/data; collect_dynamic_libs ensures native DLL/SO files are copied.
datas, binaries, hiddenimports = collect_all("sklearn")
binaries += collect_dynamic_libs("sklearn")

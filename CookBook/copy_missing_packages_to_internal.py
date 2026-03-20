"""
Copy site-packages directories into the frozen Snooz _internal folder.
Each directory is fully overwritten if it already exists.
"""
import shutil
from pathlib import Path

#--------------------------------------------------------------------------------------------
# UPDATE YOUR PATHS HERE
snooz_workspace_path = Path(r"C:\Users\klacourse\Documents\snooz_workspace")
snooz_target_path = Path(r"C:\Users\klacourse\Documents\snooz_workspace\snooz-toolbox-ceams")
#--------------------------------------------------------------------------------------------

SOURCES = [
    snooz_workspace_path / "snooz_310_env" / "Lib" / "site-packages" / "mne",
    snooz_workspace_path / "snooz_310_env" / "Lib" / "site-packages" / "lazy_loader",
    snooz_workspace_path / "snooz_310_env" / "Lib" / "site-packages" / "lspopt",
    snooz_workspace_path / "snooz_310_env" / "Lib" / "site-packages" / "yasa",
]

DESTINATION = snooz_target_path / "target" / "Snooz" / "_internal"

def copy_packages():
    for src_str in SOURCES:
        src = Path(src_str)
        dst = DESTINATION / src.name

        if not src.exists():
            print(f"[SKIP]  Source not found: {src}")
            continue

        if dst.exists():
            print(f"[DEL]   Removing existing: {dst}")
            shutil.rmtree(dst)

        print(f"[COPY]  {src}  ->  {dst}")
        shutil.copytree(src, dst)
        print(f"[OK]    {src.name}")

    print("\nDone.")


if __name__ == "__main__":
    copy_packages()

#Once the .py is generated, you need to change the line to import assets
# for example:
from .assets import CEAMS_logo

# To generate the themes.py
1- Go to the subfolder src/main/python
2- run pyside2-rcc
pyside2-rcc ./ui/themes/themes.qrc -o themes_rc.py
or
qtpy-rcc ./ui/themes/themes.qrc -o themes_rc.py


# How to create a matplotlib plot when debugging
To create a matplotlib plot on the fly without using Qt, render a PNG and open
it in the default image viewer on Windows. Follow these steps:

After updating the package cleanup code, restart Snooz and the debug session
once. Subsequent process reloads and package changes unload only active package
code, not shared libraries such as Qt, Matplotlib, or the debugger. No manual
restoration of `PySide6.QtCore` or `PySide6.QtGui` should be needed.

The VS Code launch configurations use `"guiEventLoop": "none"`. Snooz owns its
Qt event loop; the debugger must not install its automatic Matplotlib/Qt input
hook. In debugpy 2026.6.0's bundled Qt loader, selecting PySide6 incorrectly
removes `PySide6` from `sys.modules`. Keep this setting when adding a launch
configuration. Embedded Qt plots still work through Snooz's event loop or
`dialog.exec()`, but the debugger no longer pumps interactive pyplot windows
automatically while paused.

1- Turn off multithread
In `src/main/python/Managers/ProcessManager.py`, set the multithread variable to False.
Qt dialogs created from the Debug Console must run on the GUI thread.

```
self._use_multithread = False
```

2- Reach your breakpoint where your data will be available.
3- In the debug window, write the following lines one at the time and adjust the parameters as you need:

```
import os
import tempfile

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

fig = Figure(figsize=(10, 4), dpi=100)
canvas = FigureCanvasAgg(fig)
ax = fig.add_subplot(111)

ax.plot([1, 2, 3, 4, 5], [10, 5, 20, 15, 30])
ax.set_xlabel("Sample index")
ax.set_ylabel("Amplitude")
ax.grid(True)
fig.tight_layout()

with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as image:
    image_path = image.name

canvas.print_png(image_path)
os.startfile(image_path)
```

example)

import os
import tempfile

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

fig = Figure(figsize=(10, 4), dpi=100)
canvas = FigureCanvasAgg(fig)
ax = fig.add_subplot(111)
time_axis = np.arange(len(ss_signal)) / fs_chan
ax.plot(time_axis,ss_signal)
ax.set_xlabel("Sample index")
ax.set_ylabel("Amplitude")
ax.grid(True)
fig.tight_layout()

with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as image:
    image_path = image.name

canvas.print_png(image_path)
os.startfile(image_path)
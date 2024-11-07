# How to create a matplotlib plot when debugging
Essentially, in order to create a matplotlib plot on the fly we will create a 
new dialog with the plot in it. Follow these steps:

1- Turn off multithread
In the file MainWindow.py, set the multithread variable to False

```
self._use_multithread = False
```

2- Reach your breakpoint where your data will be available.
3- In the debug window, write the following lines one at the time and adjust the parameters as you need:

```
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide2.QtWidgets import QDialog, QVBoxLayout
dialog = QDialog()
fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvas(fig)
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4, 5], [10, 5, 20, 15, 30])
layout = QVBoxLayout()
layout.addWidget(canvas)
dialog.setLayout(layout)
dialog.exec_()
```
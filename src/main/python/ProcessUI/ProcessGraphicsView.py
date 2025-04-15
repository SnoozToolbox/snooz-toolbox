import json
import math

from qtpy import QtCore
from qtpy import QtGui
from qtpy import QtWidgets
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QGraphicsScene, QGraphicsView
from qtpy.QtGui import QPainter

class ProcessGraphicsView(QtWidgets.QGraphicsView):

    def __init__(self, parent=None):
        super(ProcessGraphicsView, self).__init__(parent)

        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        self.setRenderHints(
            QtGui.QPainter.Antialiasing
            | QtGui.QPainter.SmoothPixmapTransform
            | QtGui.QPainter.TextAntialiasing
            | QtGui.QPainter.SmoothPixmapTransform
        )

        self.setBackgroundBrush(Qt.white)
        self.centerOn(0, 0)

    def wheelEvent(self, event):
        # Check if the control key is pressed
        if event.modifiers() & Qt.ControlModifier:
            # Set the zoom factor
            zoom_in_factor = 1.25
            zoom_out_factor = 0.8
            
            # Calculate zoom factor based on wheel delta
            zoom_factor = zoom_in_factor if event.angleDelta().y() > 0 else zoom_out_factor

            # Adjust the transformation matrix of the view's scene
            self.scale(zoom_factor, zoom_factor)
        else:
            super().wheelEvent(event)


    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        def draw_grid(grid_step):
            window_rect = self.rect()
            top_left = self.mapToScene(window_rect.topLeft())
            bottom_right = self.mapToScene(window_rect.bottomRight())
            left =      math.floor(top_left.x() / grid_step - 0.5)
            right =     math.floor(bottom_right.x() / grid_step + 1.0)
            bottom =    math.floor(top_left.y() / grid_step - 0.5)
            top =       math.floor(bottom_right.y() / grid_step + 1.0)

            # vertical lines
            lines = [
                QtCore.QLineF(xi * grid_step, bottom * grid_step, 
                    xi * grid_step, top * grid_step)
                for xi in range(int(left), int(right) + 1)
            ]

            # horizontal lines
            lines.extend(
                [QtCore.QLineF(left * grid_step, yi * grid_step, 
                    right * grid_step, yi * grid_step)
                 for yi in range(int(bottom), int(top) + 1)
                 ]
            )

            painter.drawLines(lines)

        # Draw grid
        grid_color = QtGui.QColor(200,200,200,255)
        
        fine_pen = QtGui.QPen(grid_color, 0.5)
        painter.setPen(fine_pen)
        draw_grid(15)
        
        fine_pen = QtGui.QPen(grid_color, 1.0)
        painter.setPen(fine_pen)
        draw_grid(150)

        # Draw origin circle
        brush = QtGui.QBrush(grid_color)
        painter.setBrush(brush)
        painter.drawEllipse(QtCore.QPointF(0,0), 3, 3)

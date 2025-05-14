import datetime
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QBrush, QColor, QPen, QPainterPath
from PySide6.QtCore import Qt, QTimer

class OximeterDrawArea(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.resize_timer = QTimer()
        self.resize_timer.setSingleShot(True)
        self.resize_timer.timeout.connect(self._handle_resize_finished)
        self.setMinimumHeight(100)

        # init variables
        self._signal_models = []
        self._saturation_levels = []
        self._exclusion_events = []
        self._discontinuities = []
        self._timestamps = []
        self._is_drawing = False
        self._min_saturation = 0
        self._half_hours_count = 0
        
        self._x_scale_factor = 1
        self._y_scale_factor = 1
        
        self._selection_init_x = 0
        self._selection_final_x = 0

        self._left_padding = 40
        self._right_padding = 10
        self._top_padding = 15
        self._bottom_padding = 30

        # init pens and brushes
        self._grid_pen = QPen(Qt.lightGray)
        self._text_pen = QPen(Qt.black)
        self._signal_pen = QPen(Qt.blue)
        self._disc_pen = QPen(QColor(0,0,0,150))
        self._disc_brush = QBrush(QColor(0,0,0,150))
        self._selection_pen = QPen(QColor(255,0,0,150))
        self._selection_brush = QBrush(QColor(255,0,0,150))

    # PROPERTIES
    @property
    def min_saturation(self):
        return self._min_saturation

    @min_saturation.setter
    def min_saturation(self, value):
        self._min_saturation = value
        self._update_saturation_levels()
        self.update()

    @property
    def exclusion_events(self):
        return self._exclusion_events
    
    @exclusion_events.setter
    def exclusion_events(self, exclusion_events):
        self._exclusion_events = exclusion_events
        self.update()

    # UI EVENTS
    def resizeEvent(self, event):
        # The resizeEvent is called continuously during resizing.
        # Start or restart the timer to handle the resize event
        self.resize_timer.start(50)

    def paintEvent(self, event):
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        brush = QBrush(QColor(255, 255, 255))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawRect(0, 0, self.width(), self.height())

        # Call functions to draw the grid, the signal, the y axis, and the x axis.
        self._paint_h_lines(painter, len(self._saturation_levels))
        self._paint_v_lines(painter, self._timestamps)
        self._paint_signals(painter)
        self._paint_discontinuities(painter)
        self._paint_exclusion_events(painter)
        if self._is_drawing:
            self._paint_selection(painter)
        self._paint_y_axis_labels(painter, self._saturation_levels)
        self._paint_x_axis_labels(painter, self._timestamps)

        painter.setBrush(Qt.NoBrush)
        painter.setPen(QPen(Qt.gray))
        painter.drawRect(0, 0, self.width(), self.height())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if len(self._signal_models) == 0:
                return
            self._selection_init_x = event.pos().x()
            self._is_drawing = True

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if len(self._signal_models) == 0:
                return
            self._selection_final_x = max(min(event.pos().x(), self.width()), self._left_padding)
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if len(self._signal_models) == 0:
                return
        
            self._selection_final_x = event.pos().x()

            if self._selection_init_x == self._selection_final_x:
                self._is_drawing = False
                return
            
            # Reorder from left to right
            if self._selection_init_x > self._selection_final_x:
                tmp = self._selection_init_x
                self._selection_init_x = self._selection_final_x
                self._selection_final_x = tmp

            # Clip values
            self._selection_init_x = max(min(self._selection_init_x, self.width()), self._left_padding)
            self._selection_final_x = max(min(self._selection_final_x, self.width()), self._left_padding)

            x1 = self._px_to_seconds(self._selection_init_x)
            x2 = self._px_to_seconds(self._selection_final_x)
            max_end_time = max(self._signal_models, key=lambda x: x.end_time).end_time
            x2 = min(max_end_time, x2)
                
            self._exclusion_events.append((x1, x2))
             
            # merge overlaping events
            self._exclusion_events = self._merge_overllapping_events(self._exclusion_events)
            self._exclusion_events = self._split_overlapping_discontinuity(self._exclusion_events, self._discontinuities)
            self.update()

            self._is_drawing = False

             
    
    
    # PUBLIC FUNCTIONS
    def set_signal_models(self, signal_models):
        self._signal_models = signal_models

        self._update_scale_factors()
        self._update_discontinuities()
        self._update_timestamps()

    def reset_exclusion_events(self):
        self._exclusion_events = []
        self.update()

    # PRIVATE FUNCTIONS
    def _paint_selection(self, painter: QPainter):
        painter.setBrush(self._selection_brush)
        painter.setPen(self._selection_pen)
        w = self._selection_final_x - self._selection_init_x
        h = self.height() - self._top_padding - self._bottom_padding
        painter.drawRect(self._selection_init_x, self._top_padding, w, h)

    def _paint_h_lines(self, painter:QPainter, line_count):
        if line_count == 0: return

        # Set the pen and brush
        painter.setPen(self._grid_pen)
        painter.setBrush(Qt.NoBrush)
        
        # draw horizontal lines
        y_offset = self._calculate_y_offset(line_count-1)
        for idx in range(line_count):
            y = self._top_padding + y_offset * idx
            x1 = self._left_padding
            x2 = self.width() - self._right_padding
            painter.drawLine(x1, y, x2, y)

    def _paint_v_lines(self, painter:QPainter, timestamps):
        if len(timestamps) == 0: return
        
        # Set the pen and brush
        painter.setPen(self._grid_pen)
        painter.setBrush(Qt.NoBrush)

        # draw horizontal lines
        for idx, hour in enumerate(timestamps):
            seconds = hour * 60 * 60
            x1 = self._seconds_to_pixel(seconds)
            x2 = x1
            y1 = self._top_padding
            y2 = self.height() - self._bottom_padding
            
            painter.drawLine(x1, y1, x2, y2)

    def _paint_signals(self, painter):
        if len(self._signal_models) == 0:
            return
        
        painter.setBrush(Qt.transparent)
        painter.setPen(self._signal_pen)
        
        for signal_model in self._signal_models:
            path = QPainterPath()

            for idx, sample in enumerate(signal_model.samples):
                y = self._sample_to_pixel(sample)
                x_second = idx / signal_model.sample_rate
                x = self._seconds_to_pixel(x_second + signal_model.start_time)
                if idx == 0:
                    path.moveTo(x, y)
                else:
                    path.lineTo(x, y)
            painter.drawPath(path)

    def _paint_discontinuities(self, painter: QPainter):
        if len(self._signal_models) == 0:
            return
        
        self._paint_events(painter, self._discontinuities, self._disc_brush, self._disc_pen)

    def _paint_exclusion_events(self, painter: QPainter):
        if len(self._signal_models) == 0:
            return

        self._paint_events(painter, self._exclusion_events, self._selection_brush, self._selection_pen)

    def _paint_events(self, painter: QPainter, events, brush:QBrush, pen:QPen):
        painter.setBrush(brush)
        painter.setPen(pen)
        
        for event in events:
            start_x = self._seconds_to_pixel(event[0])
            end_x = self._seconds_to_pixel(event[1])
            w = end_x - start_x
            h = self.height() - self._top_padding - self._bottom_padding
            painter.drawRect(start_x, self._top_padding, w, h)

    def _paint_y_axis_labels(self, painter, labels):
        if len(labels) == 0:
            return
        # Draw the y text for the saturation levels
        painter.setPen(self._text_pen)
        font = painter.font()
        font.setPointSize(8)
        painter.setFont(font)

        y_offset = self._calculate_y_offset(len(labels)-1)

        for idx, label in enumerate(labels):
            y = self._top_padding + y_offset * idx

            text = f"{label} %"
            x = self._left_padding - painter.fontMetrics().width(text) - 2
            text_h_offset = painter.fontMetrics().height() / 3
            y = y + text_h_offset

            painter.drawText(x, y, text)

    def _paint_x_axis_labels(self, painter, labels):
        if len(labels) == 0:
            return

        # Draw white background to cover any signal drawing.
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(Qt.white))
        painter.drawRect(self._left_padding-1, self.height() - self._bottom_padding + 1, self.width()-self._left_padding, self._bottom_padding)

        # Set the pen and brush
        painter.setPen(self._text_pen)
        painter.setBrush(Qt.NoBrush)
        font = painter.font()
        font.setPointSize(8)
        painter.setFont(font)

        # Draw the half-hours markers
        bottom_y = self.height() - self._bottom_padding
        for idx, label in enumerate(labels):
            if idx == 0: continue
            x = self._seconds_to_pixel(label * 60 * 60)
            # One and a half our should be written as 1.5h
            hour_text = f"{label}"
            text_width = painter.fontMetrics().width(hour_text) / 2
            hour_text = f"{hour_text} h"
            painter.drawText(x - text_width, bottom_y + 12, hour_text)

    def _update_saturation_levels(self):
        # calculate drawing height
        drawing_height = self.height() - self._top_padding - self._bottom_padding

        # calculate the step size based on the drawing height and the min saturation
        min_step_height_px = 14
        how_many_i_want = 100 - self._min_saturation
        if how_many_i_want * min_step_height_px < drawing_height:
            step_size = 1
        elif how_many_i_want / 2 * min_step_height_px < drawing_height:
            step_size = 2
        elif how_many_i_want / 5 * min_step_height_px < drawing_height:
            step_size = 5
        else:
            step_size = 10

        # update the saturation levels
        self._saturation_levels = list(range(100, self._min_saturation-1, -step_size))

    def _update_timestamps(self):
        # Get max end time of all signal models        
        max_endtime = 0
        for signal_model in self._signal_models:
            max_endtime = max(max_endtime, signal_model.end_time)
        max_endtime = max_endtime / 60 # Convert seconds to minutes
        self._half_hours_count = int(max_endtime // 30) # 30 minutes = 0.5 hours 
        half_hours = list(range(0, self._half_hours_count+1))
        self._timestamps = [x * 0.5 for x in half_hours]

    def _update_scale_factors(self):
        if len(self._signal_models) == 0:
            return
        
        total_signal_duration = max(self._signal_models, key=lambda x: x.end_time).end_time
        total_samples = total_signal_duration * self._signal_models[0].sample_rate
        self._x_scale_factor = (self.width() - self._left_padding - self._right_padding) / total_samples

        drawing_height = self.height() - self._top_padding - self._bottom_padding
        self._y_scale_factor = drawing_height / (100 - self._min_saturation)
        self._one_sample_duration = 1 / self._signal_models[0].sample_rate

    def _update_discontinuities(self):
        self._discontinuities = []
        if len(self._signal_models) < 2:
            return

        for idx, signal_model in enumerate(self._signal_models[1:]):
            
            disc_start = self._signal_models[idx].end_time + self._one_sample_duration
            disc_end = signal_model.start_time - self._one_sample_duration

            # Swap disc_start and disc_end if disc_end is before disc_start which happens
            # when the discontinuity is very narrow.
            if disc_start > disc_end:
                disc_start, disc_end = disc_end, disc_start

            self._discontinuities.append((disc_start, disc_end))

    def _handle_resize_finished(self):
        # This method will be called when resizing is finished
        self._update_saturation_levels()
        self._update_scale_factors()
        self.update()

    def _calculate_y_offset(self, item_count):
        # calculate the offset between items based on the widget height and paddings.
        drawing_height = self.height() - self._top_padding - self._bottom_padding
        return drawing_height / item_count
    
    def _calculate_x_offset(self, item_count):
        # calculate the offset between items based on the widget height and paddings.
        drawing_width = self.width() - self._left_padding - self._right_padding
        return drawing_width / item_count

    def _seconds_to_pixel(self, seconds: float) -> float:
        if len(self._signal_models) == 0:
            return 0.0
        
        return seconds * self._x_scale_factor + self._left_padding
    
    def _sample_to_pixel(self, sample):
        
        drawingarea_height = self.height() - self._top_padding - self._bottom_padding
        saturation_window = 100 - self._min_saturation
        sample_per_pixel = drawingarea_height / saturation_window
        zero_y = self._top_padding + sample_per_pixel * 100
        y = zero_y - sample_per_pixel * sample

        return y
    
    def _px_to_seconds(self, x: int) -> float:
        if len(self._signal_models) == 0:
            return 0.0
        
        return float(x - self._left_padding) / self._x_scale_factor

    def _merge_overllapping_events(self, events):
        events.sort(key=lambda x: x[0])
        merged_sections = []
        current_section = events[0]
        
        for section in events[1:]:
            if section[0] <= current_section[1]:  # Check for overlap
                # Merge the overlapping sections by updating the end index
                current_section = (current_section[0], max(current_section[1], section[1]))
            else:
                # No overlap, add the current_section to the result and update the current_section
                merged_sections.append(current_section)
                current_section = section
        
        # Add the last current_section to the result
        merged_sections.append(current_section)

        return merged_sections
    
    def _split_overlapping_discontinuity(self, sections, discontinuities):
        # Sort the sections and forbidden zones based on their starting indices
        sections.sort(key=lambda x: x[0])
        discontinuities.sort(key=lambda x: x[0])

        result = []

        for section in sections:
            section_start, section_end = section
            split_sections = [(section_start, section_end)]

            for forbidden_start, forbidden_end in discontinuities:
                new_split_sections = []
                for split_start, split_end in split_sections:
                    # If the section overlaps on the right side
                    if split_start < forbidden_start < split_end < forbidden_end:
                        new_split_sections.append((split_start, forbidden_start - self._one_sample_duration))
                        # it's cropped at the end
                    # If the section overlaps on the left side
                    elif forbidden_start < split_start < forbidden_end < split_end:
                        # it's cropped at the beginning
                        new_split_sections.append((forbidden_end + self._one_sample_duration, split_end))
                    # If the section overlaps completely across
                    elif split_start < forbidden_start and split_end > forbidden_end:
                        # it's split in two in the middle
                        new_split_sections.append((split_start, forbidden_start - self._one_sample_duration))
                        new_split_sections.append((forbidden_end + self._one_sample_duration, split_end))
                    # If the section is completely inside
                    elif split_start > forbidden_start and split_start < forbidden_end and \
                        split_end > forbidden_start and split_end < forbidden_end:
                        # it's fully inside
                        pass
                    else:
                        new_split_sections.append((split_start, split_end))
                split_sections = new_split_sections

            result.extend(split_sections)

        return result
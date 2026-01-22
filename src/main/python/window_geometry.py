#!/usr/bin/env python3
"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.

Window geometry calculation module for adaptive resolution handling.
"""

from qtpy.QtWidgets import QApplication
from qtpy.QtGui import QCursor


def calculate_window_geometry(window):
    """
    Calculate and set optimal window geometry based on screen resolution.
    
    This function handles adaptive sizing and positioning for different screen resolutions,
    including small screens (800x600 or less) and multi-monitor setups.
    
    Parameters
    ----------
    window : QMainWindow
        The window instance to configure geometry for.
    """
    # Get the screen that contains the cursor (or primary screen as fallback)
    app = QApplication.instance()
    screen_obj = app.primaryScreen()
    
    # Try to get the screen at cursor position for multi-monitor setups
    try:
        cursor_pos = QCursor.pos()
        for s in app.screens():
            if s.geometry().contains(cursor_pos):
                screen_obj = s
                break
    except:
        pass  # Fallback to primary screen
    
    available_geom = screen_obj.availableGeometry()
    screen_geom = screen_obj.geometry()
    
    # Add safety margins to ensure window never touches edges
    # For small resolutions, increase bottom margin to account for larger taskbars
    margin = 30  # pixels margin on sides
    
    # Adaptive sizing based on screen size
    is_small_screen = (available_geom.width() <= 800 or available_geom.height() <= 600)
    
    if is_small_screen:
        # Very small screen (e.g., 800x600) - maximize window to fit, no margins
        # Use full available geometry
        window_width = available_geom.width() - margin
        window_height = available_geom.height() - margin
    else:
        # Normal/large screen - use standard sizing like before
        usable_width = available_geom.width() - margin
        usable_height = available_geom.height() - margin
        
        # Ensure usable dimensions are positive
        usable_width = max(100, usable_width)
        usable_height = max(100, usable_height)
        
        width_ratio = 0.70
        height_ratio = 0.75  # Normal size for large screens
        min_width = 800
        min_height = 600
        
        # Calculate desired size
        desired_width = int(usable_width * width_ratio)
        desired_height = int(usable_height * height_ratio)
        
        # Clamp to min/max values, ensuring it fits within usable space
        window_width = max(min_width, min(desired_width, usable_width))
        window_height = max(min_height, min(desired_height, usable_height))
        
        # Final absolute safety check - window must fit with margins
        window_width = min(window_width, usable_width)
        window_height = min(window_height, usable_height)
    
    # Calculate position based on screen size
    if is_small_screen:
        # Small screen - center the window within available geometry
        # Since window_width = available_geom.width() - margin, 
        # center_x_offset = margin // 2, so we just use that directly
        center_x_offset = (available_geom.width() - window_width) // 2
        center_y_offset = (available_geom.height() - window_height) // 2
        x = available_geom.x() + center_x_offset
        y = available_geom.y() + (2 * center_y_offset)
    else:
        # Normal/large screen - center the window
        center_x_offset = (usable_width - window_width) // 2
        center_y_offset = (usable_height - window_height) // 2
        x = available_geom.x() - margin + center_x_offset
        y = available_geom.y() - margin + center_y_offset
    
    # Critical: Ensure position is within screen bounds using screen geometry
    # This handles cases where resolution changes or multi-monitor setups
    min_x = screen_geom.x()
    min_y = screen_geom.y()
    max_x = screen_geom.x() + screen_geom.width() - window_width
    max_y = screen_geom.y() + screen_geom.height() - window_height
    
    # Clamp position to screen bounds (after decoration offset)
    x = max(min_x, min(x, max_x))
    y = max(min_y, min(y, max_y))
    
    # For normal screens, check if window would be outside available geometry and re-center if needed
    if not is_small_screen:
        # Account for decoration offsets when checking bounds
        available_min_x = available_geom.x()
        available_max_x = available_geom.x() + available_geom.width() - window_width
        available_min_y = available_geom.y()
        available_max_y = available_geom.y() + available_geom.height() - window_height
        
        if x < available_min_x or x > available_max_x:
            x = available_geom.x() + (available_geom.width() - window_width) // 2
            x = max(min_x, min(x, max_x))
        if y < available_min_y or y > available_max_y:
            y = available_geom.y() + (available_geom.height() - window_height) // 2
            y = max(min_y, min(y, max_y))
    
    # Set minimum size for small screens and apply geometry
    if is_small_screen:
        window.setMinimumSize(window_width, window_height)
    window.setGeometry(x, y, window_width, window_height)

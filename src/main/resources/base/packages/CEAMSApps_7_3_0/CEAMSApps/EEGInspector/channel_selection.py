"""Channel selection widget and logic"""

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from .constants import GSN_HYDRO_129_NON_BRAIN_CHANNELS, NON_BRAIN_CHANNEL_KEYWORDS, GSN_HYDRO_129_MONTAGE_NAME

class ChannelSelector:
    """Handles channel selection logic and UI"""
    
    def __init__(self, parent_widget):
        self.parent = parent_widget
        self.initial_non_brain_chs = []
        self.selected_channels = []
        self.selected_non_brain_channels = []

    def setup_channel_selection_ui(self, placeholder, channel_names, best_montage):
        """Setup the channel selection interface"""
        # Determine initial non-brain channels
        self._detect_non_brain_channels(channel_names, best_montage)
        
        # Clear existing layout
        if placeholder.layout():
            self._clear_layout(placeholder.layout())
        else:
            layout = QVBoxLayout()
            placeholder.setLayout(layout)

        layout = placeholder.layout()
        
        # Add widgets
        label = QLabel("Select non-brain Channels to remove:")
        layout.addWidget(label)

        self.channel_list_widget = QListWidget()
        self.channel_list_widget.setSelectionMode(QAbstractItemView.MultiSelection)

        # Populate channel list
        for ch in channel_names:
            item = QListWidgetItem(ch)
            if ch in self.initial_non_brain_chs:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)
            self.channel_list_widget.addItem(item)

        layout.addWidget(self.channel_list_widget)

        # Add confirm button
        self.confirm_button = QPushButton("Confirm Selection")
        layout.addWidget(self.confirm_button)
        
        return self.confirm_button

    def _detect_non_brain_channels(self, channel_names, best_montage):
        """Automatically detect non-brain channels"""
        self.initial_non_brain_chs = []
        
        # Add montage-specific channels
        if best_montage == GSN_HYDRO_129_MONTAGE_NAME:
            self.initial_non_brain_chs = GSN_HYDRO_129_NON_BRAIN_CHANNELS.copy()
        
        # Add keyword-detected channels
        for ch in channel_names:
            for keyword in NON_BRAIN_CHANNEL_KEYWORDS:
                if ch.lower().find(keyword) != -1:
                    self.initial_non_brain_chs.append(ch)
                    break

    def save_selected_channels(self, all_channel_names):
        """Save user's channel selection"""
        self.selected_non_brain_channels = [
            self.channel_list_widget.item(i).text()
            for i in range(self.channel_list_widget.count())
            if self.channel_list_widget.item(i).checkState() == Qt.Checked
        ]
        
        self.selected_channels = [
            ch for ch in all_channel_names 
            if ch not in self.selected_non_brain_channels
        ]

    def _clear_layout(self, layout):
        """Clear all widgets from layout"""
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
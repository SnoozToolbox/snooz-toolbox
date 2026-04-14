"""Event management and saving"""

import pandas as pd
import numpy as np
from PySide6.QtWidgets import QMessageBox
from .constants import EVENT_GROUP_NAME, EVENT_NAME_NON_BRAIN, EVENT_NAME_BAD_CHANNEL, EVENT_NAME_BAD_EPOCH

class EventManager:
    """Handles event creation and saving"""
    
    def __init__(self, parent_widget):
        self.parent = parent_widget

    def save_annotations(self, selected_non_brain_channels, marked_bad_chs, bad_epoch_idxs, 
                        input_dir, save_path, same_file_checked, overwrite_checked, 
                        start_time, duration, epoch_dur, epochs, selected_montage):
        """Save artifact annotations to file with proper incomplete epoch handling""" 
        
        # Calculate proper durations for bad epochs
        epoch_durations = []
        epoch_starts = []
        
        for idx in bad_epoch_idxs:
            epoch_start = idx * epoch_dur + start_time
            
            # Check if this is the last epoch and it's incomplete
            if (hasattr(self.parent.epoch_processor, 'incomplete_epoch_duration') and 
                self.parent.epoch_processor.incomplete_epoch_duration is not None and
                idx == len(epochs) - 1):
                # Use actual duration of incomplete epoch
                actual_duration = self.parent.epoch_processor.incomplete_epoch_duration
                # Ensure we don't exceed original recording duration
                if epoch_start + actual_duration > start_time + duration:
                    actual_duration = (start_time + duration) - epoch_start
            else:
                actual_duration = epoch_dur
                # Ensure we don't exceed original recording duration
                if epoch_start + actual_duration > start_time + duration:
                    actual_duration = (start_time + duration) - epoch_start
            
            epoch_durations.append(actual_duration)
            epoch_starts.append(epoch_start)

        # Determine output file
        if (not same_file_checked) and save_path != input_dir:
            output_file = save_path
            self.parent._psg_reader_manager.copy_file(input_dir, output_file)
        else:
            output_file = input_dir    

        # Create DataFrames for different artifact types
        artifact_df_non_brain = pd.DataFrame({
            "group": [EVENT_GROUP_NAME] * len(selected_non_brain_channels),
            "name": [EVENT_NAME_NON_BRAIN] * len(selected_non_brain_channels),
            "start_sec": [start_time] * len(selected_non_brain_channels),
            "duration_sec": [duration] * len(selected_non_brain_channels),
            "channels": [ch for ch in selected_non_brain_channels]
        })

        artifact_df_bad_chs = pd.DataFrame({
            "group": [EVENT_GROUP_NAME] * len(marked_bad_chs),
            "name": [EVENT_NAME_BAD_CHANNEL] * len(marked_bad_chs),
            "start_sec": [start_time] * len(marked_bad_chs),
            "duration_sec": [duration] * len(marked_bad_chs),
            "channels": [ch for ch in marked_bad_chs]
        })

        # Create bad epochs DataFrame with proper durations
        if len(bad_epoch_idxs) > 0:
            artifact_df_bad_epochs = pd.DataFrame({
                "group": [EVENT_GROUP_NAME] * len(bad_epoch_idxs),
                "name": [EVENT_NAME_BAD_EPOCH] * len(bad_epoch_idxs),
                "start_sec": epoch_starts,
                "duration_sec": epoch_durations,
                "channels": [list(epochs.info["ch_names"])] * len(bad_epoch_idxs)
            })
            artifact_df_bad_epochs = artifact_df_bad_epochs.explode('channels')
        else:
            artifact_df_bad_epochs = pd.DataFrame()

        # Combine all DataFrames
        dataframes_to_combine = [df for df in [artifact_df_non_brain, artifact_df_bad_chs, artifact_df_bad_epochs] if not df.empty]
        if dataframes_to_combine:
            new_events = pd.concat(dataframes_to_combine, ignore_index=True)
        else:
            new_events = pd.DataFrame()

        if not new_events.empty or overwrite_checked:
            # Open file for writing
            is_opened = self.parent._psg_reader_manager.open_file(output_file)
            if not is_opened:
                self._show_error_message(f'ERROR PSGWriter could not open file: {output_file}')
                return

        # Remove EEG inspector events if overwrite is checked
        # Remove any existing event with the group EVENT_GROUP_NAME, 
        #   and the name EVENT_NAME_NON_BRAIN = 'non_brain', EVENT_NAME_BAD_CHANNEL = 'art_channel' or EVENT_NAME_BAD_EPOCH = 'art_epoch'
        if overwrite_checked:
            events_to_remove = set()
            events_to_remove.add((EVENT_GROUP_NAME, EVENT_NAME_NON_BRAIN))
            events_to_remove.add((EVENT_GROUP_NAME, EVENT_NAME_BAD_CHANNEL))
            events_to_remove.add((EVENT_GROUP_NAME, EVENT_NAME_BAD_EPOCH))
            for (group_name, event_name) in events_to_remove:
                self.parent._psg_reader_manager.remove_events_by_name(event_name, group_name)   

        # Continue with existing save logic...
        if not new_events.empty:
            # Add new events (still need to handle duplicated events)
            for index, event in new_events.iterrows():
                self.parent._psg_reader_manager.add_event(
                    name=event['name'],
                    group=event['group'],
                    start_sec=event['start_sec'],
                    duration_sec=event['duration_sec'],
                    channels=event['channels'],
                    montage_index=selected_montage
                )
        
            self.parent._psg_reader_manager.save_file()
            self.parent._psg_reader_manager.close_file()

        # Show success message
        self._show_info_message("Events saved")

    def _show_error_message(self, message):
        """Show error message dialog"""
        log_msg = QMessageBox()
        log_msg.setWindowTitle("Error")
        log_msg.setText(message)
        log_msg.setIcon(QMessageBox.Critical)
        log_msg.exec_()

    def _show_info_message(self, message):
        """Show information message dialog"""
        log_msg = QMessageBox()
        log_msg.setWindowTitle("Information")
        log_msg.setText(message)
        log_msg.setIcon(QMessageBox.Information)
        log_msg.exec_()
from qtpy import QtWidgets
from widgets.WarningDialog import WarningDialog  # if you need it
import pandas as pd

class RemoveChannelArtefactResultsView(QtWidgets.QWidget):
    """
    Results viewer for RemoveChannelArtefact.
    Displays:
     - a plain‐text list of removed channels
     - a table of removed events
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._parent_node    = parent_node
        self._cache_manager  = cache_manager
        self._pub_sub_manager= pub_sub_manager

        # Build UI
        layout = QtWidgets.QVBoxLayout(self)

        self.channels_label = QtWidgets.QLabel("Removed Channels:")
        self.channels_text  = QtWidgets.QPlainTextEdit()
        self.channels_text.setReadOnly(True)

        self.events_label   = QtWidgets.QLabel("Removed Events:")
        self.events_table   = QtWidgets.QTableWidget()
        self.events_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        layout.addWidget(self.channels_label)
        layout.addWidget(self.channels_text)
        layout.addWidget(self.events_label)
        layout.addWidget(self.events_table)
        self.setLayout(layout)

        # Finally, load & display whatever is in cache
        self.load_results()

    def load_results(self):
        """Read the cache and populate both widgets."""
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier) or {}

        # Plain‐text: removed channels
        removed_channels = cache.get('removed_channels', [])
        self.channels_text.setPlainText("\n".join(removed_channels))

        # Table: removed events DataFrame
        removed_events_df = cache.get('removed_events', pd.DataFrame())
        if not removed_events_df.empty:
            # set headers & dimensions
            self.events_table.setColumnCount(len(removed_events_df.columns))
            self.events_table.setRowCount(len(removed_events_df))
            self.events_table.setHorizontalHeaderLabels(removed_events_df.columns.tolist())

            # fill
            for r in range(len(removed_events_df)):
                for c, col in enumerate(removed_events_df.columns):
                    val = removed_events_df.iloc[r, c]
                    item = QtWidgets.QTableWidgetItem(str(val))
                    self.events_table.setItem(r, c, item)

            self.events_table.resizeColumnsToContents()
        else:
            self.events_table.clear()
            self.events_table.setRowCount(0)
            self.events_table.setColumnCount(0)



# """
# @ Valorisation Recherche HSCM, Societe en Commandite – 2025
# See the file LICENCE for full license details.

#     Results viewer of the RemoveChannelArtefact plugin
# """

# from qtpy import QtWidgets

# from CEAMSModules.RemoveChannelArtefact.Ui_RemoveChannelArtefactResultsView import Ui_RemoveChannelArtefactResultsView

# class RemoveChannelArtefactResultsView(Ui_RemoveChannelArtefactResultsView, QtWidgets.QWidget):
#     """
#         RemoveChannelArtefactResultsView.
#     """
#     def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
#         super(RemoveChannelArtefactResultsView, self).__init__(*args, **kwargs)
#         self._parent_node = parent_node
#         self._pub_sub_manager = pub_sub_manager
#         self._cache_manager = cache_manager

#         # init UI
#         self.setupUi(self)

#     def load_results(self):
#         # Code example to load the cache from the module
#         # cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)
#         # print(cache)
#         pass
from qtpy import QtWidgets
import pandas as pd

class EpochSignalResultsView(QtWidgets.QWidget):
    """
    Results viewer for the EpochSignal node.
    Shows:
      • total number of channels processed
      • number of epochs per channel
      • the DataFrame of epoch events
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._parent_node    = parent_node
        self._cache_manager  = cache_manager
        self._pub_sub_manager= pub_sub_manager

        # Build UI
        layout = QtWidgets.QVBoxLayout(self)

        # Total channels
        layout.addWidget(QtWidgets.QLabel("Channels processed:"))
        self._val_total = QtWidgets.QLabel("(waiting...)")
        layout.addWidget(self._val_total)

        # Epochs per channel
        layout.addWidget(QtWidgets.QLabel("Epochs per channel:"))
        self._txt_per = QtWidgets.QPlainTextEdit()
        self._txt_per.setReadOnly(True)
        layout.addWidget(self._txt_per)

        # Events table
        layout.addWidget(QtWidgets.QLabel("Epoch events:"))
        self._tbl_events = QtWidgets.QTableWidget()
        self._tbl_events.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        layout.addWidget(self._tbl_events)

        self.setLayout(layout)

        # Right away, load whatever is in cache
        self.load_results()

    def load_results(self):
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier) or {}

        # 1) Total channels
        n_ch = cache.get('n_channels', None)
        self._val_total.setText(str(n_ch) if n_ch is not None else "(no data)")

        # 2) Epochs per channel
        per = cache.get('epochs_per_channel', {})
        if per:
            text = "\n".join(f"{ch}: {cnt} epochs" for ch, cnt in per.items())
        else:
            text = "(none)"
        self._txt_per.setPlainText(text)

        # 3) Events DataFrame
        df = cache.get('events_df', pd.DataFrame())
        if not df.empty:
            self._tbl_events.setColumnCount(len(df.columns))
            self._tbl_events.setRowCount(len(df))
            self._tbl_events.setHorizontalHeaderLabels(df.columns.tolist())
            for r in range(len(df)):
                for c, col in enumerate(df.columns):
                    item = QtWidgets.QTableWidgetItem(str(df.iat[r, c]))
                    self._tbl_events.setItem(r, c, item)
            self._tbl_events.resizeColumnsToContents()
        else:
            self._tbl_events.clear()
            self._tbl_events.setRowCount(0)
            self._tbl_events.setColumnCount(0)




"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.
"""

"""
    TableDialog
    Class to display error message as pandas DataFrame.
    Usage :
        import pandas as pd
        from widgets.TableDialog import TableDialog
        error_msg_pd = pd.DataFrame(data=error_msg_lst,columns=['file', 'group', 'name'])
        table_dialog_msg = TableDialog(df=error_msg_pd, title="Warning Message",message="Those events were not found", showDownloadButton=True)
        table_dialog_msg.exec_()

    Pass showConfirmationButtons=True to return QDialog.Accepted for OK and
    QDialog.Rejected for Cancel, Escape, or closing the window.
"""
import os

from pandas.core.frame import DataFrame

from qtpy.QtCore import QCoreApplication, Qt, QTimer
from qtpy.QtWidgets import QTableWidgetItem, QDialog, QPushButton, QFileDialog, QLabel
from qtpy.QtWidgets import QAbstractItemView
from qtpy.QtWidgets import QFormLayout, QGroupBox, QHeaderView, QStyle

from ui.Ui_TableDialog import Ui_TableDialog

class TableDialog(QDialog, Ui_TableDialog):
    """
    Create a custom dialog class based on QDialog and Ui_TableDialog.
    """

    # Define the constructor of the class.
    def __init__(self, df:DataFrame, title:str, message:str, showDownloadButton:bool = False, *args, showConfirmationButtons:bool = False, **kwargs):
        # Call the constructor of the parent class (QDialog) with any arguments 
        # passed to this constructor.
        super(TableDialog, self).__init__(*args, **kwargs)

        # Store the pandas DataFrame in a class attribute for later use.
        self._df = df

        # Call the setupUi method to initialize the user interface.
        self.setupUi(self)

        if showConfirmationButtons:
            self.ok_pushbutton.clicked.disconnect(self.close)
            self.ok_pushbutton.clicked.connect(self.accept)
            self.ok_pushbutton.setText("OK")
            self.ok_pushbutton.setDefault(True)
            self.cancel_pushbutton = QPushButton("Cancel", self)
            self.cancel_pushbutton.clicked.connect(self.reject)
            self.horizontalLayout.addWidget(self.cancel_pushbutton)

        # Set the title and message labels to the values provided in the
        # constructor.
        self.title_label.setText(title)
        self.message_label.setText(message)

        self._expanded_rows = set()
        self._natural_row_heights = {}
        self._details_labels = {}

        self._populate_table(df)

        # Keep the report read-only: users can inspect/export values but not modify them.
        self.tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
                
        # Add a download button if necessary
        if showDownloadButton:
            self.tsv_pushbutton = QPushButton()
            self.tsv_pushbutton.setObjectName(u"tsv_pushbutton")
            self.tsv_pushbutton.setText(QCoreApplication.translate("TableDialog", u"Download as TSV", None))
            self.tsv_pushbutton.clicked.connect(self.download_tsv)

            self.horizontalLayout.insertWidget(0, self.tsv_pushbutton)
            self.horizontalLayout.insertStretch(1,1)

    def _populate_table(self, df):
        """Populate the table while preserving the original column layout and enabling a generic details view."""
        self.resize(900, 560)
        self.tablewidget.setRowCount(len(df))
        self.tablewidget.setColumnCount(len(df.columns))
        self.tablewidget.setHorizontalHeaderLabels(df.columns)
        self.tablewidget.setWordWrap(True)
        self.tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        for row in range(len(df)):
            for col in range(len(df.columns)):
                value = df.iloc[row, col]
                item = QTableWidgetItem(str(value))
                item.setToolTip(str(value))
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                self.tablewidget.setItem(row, col, item)

        self._build_details_panel(df.columns)
        self.tablewidget.currentCellChanged.connect(self._show_row_details)
        self.tablewidget.cellDoubleClicked.connect(self._toggle_row_expansion)
        QTimer.singleShot(0, self._resize_columns_to_content)
        QTimer.singleShot(0, self._resize_row_heights)

    def _resize_columns_to_content(self):
        """Give more room to the columns with longer content, without horizontal scrolling."""
        if self.tablewidget.columnCount() == 0:
            return

        self.tablewidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        header = self.tablewidget.horizontalHeader()
        font_metrics = self.tablewidget.fontMetrics()
        available_width = max(500, self.width() - 80)

        estimated_widths = []
        weights = []
        for col in range(self.tablewidget.columnCount()):
            max_chars = 12
            for row in range(self.tablewidget.rowCount()):
                item = self.tablewidget.item(row, col)
                if item is None:
                    continue
                max_chars = max(max_chars, len(item.text()) if item.text() else 0)

            preferred_width = max(90, min(500, max_chars * font_metrics.averageCharWidth() + 24))
            estimated_widths.append(preferred_width)
            weights.append(max(1, max_chars))

        total_estimated = sum(estimated_widths)
        if total_estimated <= 0:
            return

        if len(estimated_widths) > 1:
            for col in range(self.tablewidget.columnCount()):
                header.setSectionResizeMode(col, QHeaderView.Interactive)

            if total_estimated <= available_width:
                extra_width = available_width - total_estimated
                total_weight = sum(weights)
                widths = estimated_widths[:]
                if total_weight > 0:
                    for idx, _ in enumerate(widths):
                        widths[idx] += int(extra_width * (weights[idx] / total_weight))
                    # Preserve the requested window width exactly while keeping the proportional split.
                    while sum(widths) < available_width:
                        for idx in range(len(widths)):
                            if sum(widths) >= available_width:
                                break
                            widths[idx] += 1
                    while sum(widths) > available_width:
                        for idx in range(len(widths) - 1, -1, -1):
                            if widths[idx] > 90 and sum(widths) > available_width:
                                widths[idx] -= 1
                                if sum(widths) <= available_width:
                                    break
                for col, width in enumerate(widths):
                    header.resizeSection(col, width)
            else:
                scale = available_width / total_estimated
                widths = [max(90, int(width * scale)) for width in estimated_widths]
                for col, width in enumerate(widths):
                    header.resizeSection(col, width)
        else:
            header.setSectionResizeMode(0, QHeaderView.Stretch)

    def _build_details_panel(self, columns):
        """Add a selection details panel that mirrors the current DataFrame columns."""
        self._details_group = QGroupBox("Details", self)
        details_layout = QFormLayout(self._details_group)
        self._details_labels = {}

        for column in columns:
            label = QLabel()
            label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            label.setWordWrap(True)
            self._details_labels[column] = label
            details_layout.addRow(f"{column}:", label)

        self._details_group.hide()
        self.verticalLayout_2.insertWidget(3, self._details_group)

    def _resize_row_heights(self):
        """Fit wrapped cells while keeping long rows compact by default."""
        maximum_height = 120
        self.tablewidget.resizeRowsToContents()
        for row in range(self.tablewidget.rowCount()):
            natural_height = self.tablewidget.rowHeight(row)
            self._natural_row_heights[row] = natural_height
            self.tablewidget.setRowHeight(row, min(natural_height, maximum_height))

    def _resize_interruption_rows(self):
        """Fit wrapped messages while keeping the initial table compact."""
        maximum_height = 120
        self.tablewidget.resizeRowsToContents()
        for row in range(self.tablewidget.rowCount()):
            natural_height = self.tablewidget.rowHeight(row)
            self._natural_row_heights[row] = natural_height
            self.tablewidget.setRowHeight(row, min(natural_height, maximum_height))

    def _toggle_row_expansion(self, row, _column):
        """Expand or collapse a row whose wrapped message exceeds the height cap."""
        natural_height = self._natural_row_heights.get(row, self.tablewidget.rowHeight(row))
        if natural_height <= 120:
            return
        if row in self._expanded_rows:
            self._expanded_rows.remove(row)
            self.tablewidget.setRowHeight(row, 120)
        else:
            self._expanded_rows.add(row)
            self.tablewidget.setRowHeight(row, natural_height)

    def _show_row_details(self, current_row, _current_column, _previous_row, _previous_column):
        """Display the selected row values in Details while keeping the original DataFrame columns."""
        if current_row < 0:
            self._details_group.hide()
            return

        row_values = self._df.iloc[current_row]
        for column, label in self._details_labels.items():
            label.setText(str(row_values[column]))
        self._details_group.show()

    def download_tsv(self):
        """ Download the list as a TSV file      
        """
        filename, _ = QFileDialog.getSaveFileName(None, 'Save TSV file as',filter="*.tsv")

        # save the DataFrame as a TSV file
        if filename is not None and filename:
            self._df.to_csv(filename, index=False, sep='\t')

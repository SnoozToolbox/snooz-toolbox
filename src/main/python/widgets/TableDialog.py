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
    def __init__(self, df:DataFrame, title:str, message:str, showDownloadButton:bool = False, *args, **kwargs):
        # Call the constructor of the parent class (QDialog) with any arguments 
        # passed to this constructor.
        super(TableDialog, self).__init__(*args, **kwargs)

        # Store the pandas DataFrame in a class attribute for later use.
        self._df = df

        # Call the setupUi method to initialize the user interface.
        self.setupUi(self)

        # Set the title and message labels to the values provided in the
        # constructor.
        self.title_label.setText(title)
        self.message_label.setText(message)

        self._is_interruption_table = {
            'identifier', 'message', 'type'
        }.issubset(df.columns)
        self._expanded_rows = set()
        self._natural_row_heights = {}

        if self._is_interruption_table:
            self._setup_interruption_table()
        else:
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
        """Populate the standard table without changing its existing presentation."""

        # Set the number of rows and columns of the tablewidget to match the
        # size of the DataFrame.
        self.tablewidget.setRowCount(len(df))
        self.tablewidget.setColumnCount(len(df.columns))

        # Set the horizontal header labels of the tablewidget to the column
        # names of the DataFrame.
        self.tablewidget.setHorizontalHeaderLabels(df.columns)

        # Populate the tablewidget with the data from the DataFrame.
        for row in range(len(df)):
            for col in range(len(df.columns)):
                value = df.iloc[row, col]
                item = QTableWidgetItem(str(value))
                if isinstance(value, str):
                    item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.tablewidget.setItem(
                    row,
                    col,
                    item
                    )

    def _setup_interruption_table(self):
        """Present process interruptions as readable recording/message rows."""
        self.resize(900, 560)
        self.tablewidget.setColumnCount(2)
        self.tablewidget.setRowCount(len(self._df))
        self.tablewidget.setHorizontalHeaderLabels(["Recording", "Message"])
        self.tablewidget.setWordWrap(True)
        self.tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        warning_icon = self.style().standardIcon(QStyle.SP_MessageBoxWarning)
        for row in range(len(self._df)):
            full_path = str(self._df.iloc[row]['identifier'])
            filename = os.path.basename(full_path.rstrip('/\\')) or full_path
            recording_item = QTableWidgetItem(warning_icon, f"{filename}    {full_path}")
            recording_item.setToolTip(full_path)
            recording_item.setTextAlignment(Qt.AlignLeft | Qt.AlignTop)

            message_item = QTableWidgetItem(str(self._df.iloc[row]['message']))
            message_item.setTextAlignment(Qt.AlignLeft | Qt.AlignTop)

            self.tablewidget.setItem(row, 0, recording_item)
            self.tablewidget.setItem(row, 1, message_item)

        header = self.tablewidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Interactive)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.tablewidget.setColumnWidth(0, 280)

        self._details_group = QGroupBox("Details", self)
        details_layout = QFormLayout(self._details_group)
        self._details_path = QLabel()
        self._details_type = QLabel()
        self._details_message = QLabel()
        for label in (self._details_path, self._details_type, self._details_message):
            label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            label.setWordWrap(True)
        details_layout.addRow("Full path:", self._details_path)
        details_layout.addRow("Type:", self._details_type)
        details_layout.addRow("Message:", self._details_message)
        self._details_group.hide()
        self.verticalLayout_2.insertWidget(3, self._details_group)

        self.tablewidget.currentCellChanged.connect(self._show_interruption_details)
        self.tablewidget.cellDoubleClicked.connect(self._toggle_row_expansion)
        QTimer.singleShot(0, self._resize_interruption_rows)

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

    def _show_interruption_details(self, current_row, _current_column, _previous_row, _previous_column):
        """Show the complete values for the selected interruption."""
        if current_row < 0:
            self._details_group.hide()
            return
        self._details_path.setText(str(self._df.iloc[current_row]['identifier']))
        self._details_type.setText(str(self._df.iloc[current_row]['type']))
        self._details_message.setText(str(self._df.iloc[current_row]['message']))
        self._details_group.show()

    def download_tsv(self):
        """ Download the list as a TSV file      
        """
        filename, _ = QFileDialog.getSaveFileName(None, 'Save TSV file as',filter="*.tsv")

        # save the DataFrame as a TSV file
        if filename is not None and filename:
            self._df.to_csv(filename, index=False, sep='\t')

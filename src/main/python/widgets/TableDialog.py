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
from pandas.core.frame import DataFrame

from qtpy.QtCore import QCoreApplication
from qtpy.QtWidgets import QTableWidgetItem, QDialog, QPushButton, QFileDialog

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
                self.tablewidget.setItem(
                    row,
                    col,
                    QTableWidgetItem(str(df.iloc[row, col]))
                    )
                
        # Add a download button if necessary
        if showDownloadButton:
            self.tsv_pushbutton = QPushButton()
            self.tsv_pushbutton.setObjectName(u"tsv_pushbutton")
            self.tsv_pushbutton.setText(QCoreApplication.translate("TableDialog", u"Download as TSV", None))
            self.tsv_pushbutton.clicked.connect(self.download_tsv)

            self.horizontalLayout.insertWidget(0, self.tsv_pushbutton)
            self.horizontalLayout.insertStretch(1,1)
            
    def download_tsv(self):
        """ Download the list as a TSV file      
        """
        filename, _ = QFileDialog.getSaveFileName(None, 'Save TSV file as',filter="*.tsv")

        # save the DataFrame as a TSV file
        if filename is not None and filename:
            self._df.to_csv(filename, index=False, sep='\t')

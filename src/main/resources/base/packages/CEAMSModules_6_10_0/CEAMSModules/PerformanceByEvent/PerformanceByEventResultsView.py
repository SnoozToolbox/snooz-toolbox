"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""

"""
    Results viewer of the PerformanceByEvent plugin
"""

from qtpy import QtWidgets

from CEAMSModules.PerformanceByEvent.Ui_PerformanceByEventResultsView import Ui_PerformanceByEventResultsView

class PerformanceByEventResultsView( Ui_PerformanceByEventResultsView, QtWidgets.QWidget):
    """
        PerformanceByEventView display the spectrum from SpectraViewver into
        a matplotlib figure on the scene.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(PerformanceByEventResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)
        

    def load_results(self):
        # Clear the data if any
        self.result_tablewidget.setRowCount(0)        
        # Read result cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)
        if cache is not None:
            # Add time elapsed to the events list
            self.write_df_to_qtable(cache, self.result_tablewidget)
    

    def write_df_to_qtable(self, df, table):
        headers = list(df)
        table.setRowCount(df.shape[0])
        table.setColumnCount(df.shape[1])
        table.setHorizontalHeaderLabels(headers)        

        # getting data from df is computationally costly so convert it to array first
        df_array = df.values
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                table.setItem(row, col, QtWidgets.QTableWidgetItem(str(df_array[row,col])))



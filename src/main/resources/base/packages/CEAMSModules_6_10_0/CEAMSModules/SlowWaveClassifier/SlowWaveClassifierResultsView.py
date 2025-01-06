"""
@ CIUSSS DU NORD-DE-L'ILE-DE-MONTREAL – 2023
See the file LICENCE for full license details.
"""
"""
    Results viewer of the SlowWaveClassifier plugin
"""

import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.lines import Line2D
matplotlib.use('Qt5Agg')
from scipy.stats import norm
import numpy as np
from qtpy import QtWidgets, QtCore, QtGui
from CEAMSModules.SlowWaveClassifier.Ui_SlowWaveClassifierResultsView import Ui_SlowWaveClassifierResultsView


def _mix_pdf(x, loc, scale, weights):
    """
    Probability density function of gaussian mixture distribution.
    Used to give different weight to each peak of the gaussian mixture and get
    a nice graph when shown on histogram.
    Taken from :
    https://stats.stackexchange.com/questions/387702/gaussian-mixture-is-this-plot-right 
    
    Parameters
    -----------
        x   : data to analyse
        loc : mean of data
        scale   : covariance of data
        weights : weight of each gaussian mixture peak
    
    Returns
    -----------
        d   :   probability density function
    """

    d = np.zeros_like(x)
    for mu, sigma, pi in zip(loc, scale, weights):
        d += pi * norm.pdf(x, loc=mu, scale=sigma)
    return d

class SlowWaveClassifierResultsView( Ui_SlowWaveClassifierResultsView, QtWidgets.QWidget):
    """
        SlowWaveClassifierResultsView shows an Histogram with a gaussian mixture
        on it, a AIC diagram of the best gaussian mixture fit, a table with 
        various data about each sleep slow wave category found and different graphs
        and tables of the distribution of each category.
    """
    def __init__(self, parent_node, cache_manager, pub_sub_manager, *args, **kwargs):
        super(SlowWaveClassifierResultsView, self).__init__(*args, **kwargs)
        self._parent_node = parent_node
        self._pub_sub_manager = pub_sub_manager
        self._cache_manager = cache_manager

        # init UI
        self.setupUi(self)

        # Create figure : https://matplotlib.org/2.1.2/api/axes_api.html
        self.init_figures()

        self.index = 0 


    def load_results(self):
        # Clear cache from the loaded file, usefull for the second run
        self.disk_cache = {}

         # Read result cache
        cache = self._cache_manager.read_mem_cache(self._parent_node.identifier)
        if cache is not None:       
            # Get data needed from the cache
            self.gm_data = cache['gm_data']
            self.histogram_data = cache['histogram_data']
            self.aic_data = cache['aic_data']
            self.n_categories = cache['n_categories']
            self.categorized_data = cache['categorized_data']
            self.data_details = cache['data_details']
            self.distr_time = cache['distr_time']
            self.distr_cycle = cache['distr_cycle']
            self.distr_quarter = cache['distr_quarter']
            self.has_one_signal_only = cache['has_one_signal_only']

            if self.has_one_signal_only:
                self.id = cache['id']
                self.label_2.setText(f"Distribution of each type of slow wave during the night for {self.id}")

            # Manage figures
            self.figure.clear()
            self.gs = self.figure.add_gridspec(2, 1, hspace=0.5)
            self.ax_histo = self.figure.add_subplot(self.gs[0, 0])
            self.ax_aic = self.figure.add_subplot(self.gs[1, 0])

            self.time_fig.clear()
            self.ax_distr_time = self.time_fig.add_subplot()

            self.cycles_fig.clear()
            self.ax_distr_cycles = self.cycles_fig.add_subplot()

            self.quarter_fig.clear()
            self.gs2 = self.quarter_fig.add_gridspec(2, 2, hspace=0.5)
            self.ax_distr_quarter_1 = self.quarter_fig.add_subplot(self.gs2[0,0])
            self.ax_distr_quarter_2 = self.quarter_fig.add_subplot(self.gs2[0,1])
            self.ax_distr_quarter_3 = self.quarter_fig.add_subplot(self.gs2[1,0])
            self.ax_distr_quarter_4 = self.quarter_fig.add_subplot(self.gs2[1,1])

            # Plot figures
            self.plot_histogram(self.histogram_data, self.gm_data)
            self.plot_aic_results(self.aic_data)
            self.show_categories_data(self.data_details)
            self.show_sleep_time_distribution()
            self.show_sleep_cycles_distribution()
            self.show_sleep_quarter_distribution()


    def plot_histogram(self, data, gm):
        """
        Plots an histogram with the gaussian mixture distribution on it
        Snippet of code below inspired by :
        https://stats.stackexchange.com/questions/387702/gaussian-mixture-is-this-plot-right
        
        Parameters
        -----------
            data : Pandas DataFrame
                DataFrame events (columns=['category','n_t','PaP','Neg', 'tNe', 'tPo', 'Pap_raw', 'Neg_raw', 'mfr', 'tfr'])
                containing data analysis of parameters for each slow wave category
                found
            gm  : list, GaussianMixture value
        """        

        # Constants
        N_BINS = 100
        GAUSSIAN_PRECISION = 0.0001
        MULT_VISUALISATION = len(data)/25     # Better visualise gaussian mixture on histogram

        self.ax_histo.clear()   # clean old histogram plot

        hist_data = np.array(data)
        hist_data = hist_data.reshape(-1, 1)   # Gaussian Mixture requires 2D array
        self.ax_histo.hist(hist_data, bins = N_BINS)
        "Section of code taken from https://stats.stackexchange.com/questions/387702/gaussian-mixture-is-this-plot-right"
        pi, mu, sigma = gm.weights_.flatten(), gm.means_.flatten(), np.sqrt(gm.covariances_.flatten())
        grid = np.arange(np.min(hist_data), np.max(hist_data), GAUSSIAN_PRECISION)
        self.ax_histo.plot(grid, MULT_VISUALISATION * _mix_pdf(grid, mu, sigma, pi))
        "End of section of code"
        self.ax_histo.set_title("Distribution of sleep slow wave's transition frequency")
        self.ax_histo.set_xlabel('Transition frequency (Hz)')
        self.ax_histo.set_ylabel('Number of sleep slow waves')
        custom_legend_lines = [Line2D([0], [0], color='blue', lw=4),
                                Line2D([0], [0], color='orange', lw=4)] 
        self.ax_histo.legend(custom_legend_lines, 
                            ['Histogram of distribution', 'Gaussian mixture of distribution'],
                            loc='upper right')


    def plot_aic_results(self, aic_data):
        """
        Plots the Akaike information criterion (AIC) of the gaussian distribution
        show in the histogram plot

        Parameters
        -----------
            aic_data    : aic_results : list, aic value (float) for each distribution
        """

        self.ax_aic.clear()     # clean old aic plot

        if len(aic_data) > 1:
            x = [i + 1 for i in range(len(aic_data))]
            self.ax_aic.plot(x, aic_data)
            self.ax_aic.set_title("Akaike Information Criterion (AIC)")
            self.ax_aic.set_xlabel('Number of categories')
            self.ax_aic.set_ylabel('AIC value')
            self.ax_aic.set_xticks(x)
        else:
            self.ax_aic.set_axis_off()


    def show_categories_data(self, classification_data):
        """
        Shows tables of each category of sleep slow waves found

        Parameters
        -----------
            classification_data    : Pandas DataFrame
                DataFrame events (columns=['n_t','PaP','Neg', 'tNe', 'tPo', 'Pap_raw', 'Neg_raw', 'mfr', 'tfr'])
                containing data on a certain category of slow waves
        """

        columns = ['Transition frequency (Hz)', 'Peak-to-peak amplitude (V)', 'Negative amplitude (V)',\
                'Time of negative part (ms)', 'Time of positive part (ms)']
        index = ["Min", "Mean", "Max"]

        self.remove_tables(self.tables_layout)
        self.tables_layout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

        i = 1
        for c in classification_data.columns:
            # Add title
            title = QtWidgets.QLabel(f'SSW category #{i}')
            title.setAlignment(QtCore.Qt.AlignHCenter)
            title.setFont(QtGui.QFont('SansSerif', 10))
            self.tables_layout.addWidget(title)
            # Add table
            data = self._extract_wanted_data(classification_data, c)
            self.create_table_view(columns, index, data, self.tables_layout)
            i += 1
        self.tables_layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)


    def show_sleep_time_distribution(self):
        """
        Shows sleep waves distribution by time
        """

        if self.has_one_signal_only and self.distr_time is not None:
            # Get data from DataFrame
            distr_data, distr_columns, distr_index = self._extract_information_from_DataFrame(self.distr_time)

            # Clean old plots
            self.remove_tables(self.distr_time_layout)
            self.ax_distr_time.clear()

            # Create table
            self.create_table_view(distr_columns, distr_index, distr_data, self.distr_time_layout)
            
            # Create plots
            self.ax_distr_time.plot(distr_index, self.distr_time["Total"], label = distr_columns[0])
            for n in range(self.n_categories):
                c = f"SSW category #{n+1}"
                self.ax_distr_time.plot(distr_index, self.distr_time[c], label = distr_columns[n+1])
            self.ax_distr_time.set_xlabel('Time elapsed (mins)')
            self.ax_distr_time.set_ylabel('Number of sleep slow wave detected')
            self.ax_distr_time.set_title('Sleep slow waves distribution through time (NREM periods only)')
            start, end = self.ax_distr_time.get_xlim()
            self.ax_distr_time.set_xticks(np.arange(start, end, 12))
            
            self.ax_distr_time.legend()

        else:
            self.distributions_subclass_tabWidget.setTabEnabled(0, False)

    
    def show_sleep_cycles_distribution(self):
        """
        Shows sleep slow waves distribution by cycles
        """

        if self.has_one_signal_only and self.distr_cycle is not None:
            # Get data from DataFrame
            distr_data, distr_columns, distr_index = self._extract_information_from_DataFrame(self.distr_cycle)

            # Clean old plots
            self.remove_tables(self.distr_cycles_layout)
            self.ax_distr_cycles.clear()

            # Create table view
            self.create_table_view(distr_columns, distr_index, distr_data, self.distr_cycles_layout)
            
            # Create plots
            self.ax_distr_cycles.plot(distr_index, self.distr_cycle["Total"], label = distr_columns[0])
            for i in range(self.n_categories):
                c = f"SSW category #{i+1}"
                self.ax_distr_cycles.plot(distr_index, self.distr_cycle[c], label = distr_columns[i + 1])
            self.ax_distr_cycles.legend()
            self.ax_distr_cycles.set_xlabel('Cycles throughout the patient\'s night')
            self.ax_distr_cycles.set_ylabel('Number of sleep slow wave detected')
            self.ax_distr_cycles.set_title('Sleep slow waves distribution through cycles (NREM periods only)')
        
        else:
            self.distributions_subclass_tabWidget.setTabEnabled(1, False)

    
    def show_sleep_quarter_distribution(self):
        """
        Shows sleep slow waves distribution by quarter (N2 and N3)
        """

        if self.distr_quarter is not None:
            # Variables
            distr_labels = [f'SSW cat#{i + 1}' for i in range(self.n_categories)]

            # Get data from DataFrame
            distr_data, distr_columns, distr_index = self._extract_information_from_DataFrame(self.distr_quarter)

            # Format data for pie charts
            data = []
            for i in range(len(self.distr_quarter.index)):
                data_row = []
                for n in self.distr_quarter.iloc[i]:
                    index = np.char.find(n, " +- ")
                    val = n[:index]
                    data_row.append(val)
                data.append(data_row)

            # Clean old plots
            self.remove_tables(self.distr_quarter_layout)
            self.ax_distr_quarter_1.clear()
            self.ax_distr_quarter_2.clear()
            self.ax_distr_quarter_3.clear()
            self.ax_distr_quarter_4.clear()

            # Show data
            self.create_table_view(distr_columns, distr_index, distr_data, self.distr_quarter_layout)
            self.ax_distr_quarter_1.pie(data[0], labels=distr_labels, autopct='%1.1f%%')
            self.ax_distr_quarter_1.set_title('1/4 of the night')

            self.ax_distr_quarter_2.pie(data[1], labels=distr_labels, autopct='%1.1f%%')
            self.ax_distr_quarter_2.set_title('2/4 of the night')

            self.ax_distr_quarter_3.pie(data[2], labels=distr_labels, autopct='%1.1f%%')
            self.ax_distr_quarter_3.set_title('3/4 of the night')

            self.ax_distr_quarter_4.pie(data[3], labels=distr_labels, autopct='%1.1f%%')
            self.ax_distr_quarter_4.set_title('4/4 of the night')


    def _extract_wanted_data(self, dataframe, column_name):
        """
        Keeps part of the data to show in the view

        Parameters
        -----------
            dataframe   : Pandas DataFrame
                DataFrame containing information on each type of slow wave category.
                Index describes the type of information found in the row.
            column_name : Str
        
        Returns
        -----------
            data : list, 2D list of each data analysis kept for each category
        """

        data_min = []
        data_mean = []
        data_max = []
            
        # Transition frequency
        data_min.append("{:.2f}".format(dataframe.at["min tfr", column_name]))
        data_mean.append("{:.2f}".format(dataframe.at["mean tfr", column_name]))
        data_max.append("{:.2f}".format(dataframe.at["max tfr", column_name]))

        # Peak-to-peak amplitude
        data_min.append("{:.2f}".format(dataframe.at["min PaP", column_name]))
        data_mean.append("{:.2f}".format(dataframe.at["mean PaP", column_name]))
        data_max.append("{:.2f}".format(dataframe.at["max PaP", column_name]))

        # Negative amplitude
        data_min.append("{:.2f}".format(dataframe.at["min Neg", column_name]))
        data_mean.append("{:.2f}".format(dataframe.at["mean Neg", column_name]))
        data_max.append("{:.2f}".format(dataframe.at["max Neg", column_name]))
            
        # Time of negative part
        data_min.append("{:.2f}".format(dataframe.at["min tNe", column_name]))
        data_mean.append("{:.2f}".format(dataframe.at["mean tNe", column_name]))
        data_max.append("{:.2f}".format(dataframe.at["max tNe", column_name]))
            
        # Time of positive part
        data_min.append("{:.2f}".format(dataframe.at["min tPo", column_name]))
        data_mean.append("{:.2f}".format(dataframe.at["mean tPo", column_name]))
        data_max.append("{:.2f}".format(dataframe.at["max tPo", column_name]))

        data = [data_min, data_mean, data_max]
        return data


    def create_table_view(self, columns, index, data, layout):
        """
        Creates a table to easily view data

        Parameters
        -----------
            columns : list, String containing header names
            index   : list, String containing the type of data analysis
            data    : Pandas DataFrame
                DataFrame events containing data
            layout  : QLayout in which to add the table
        """

        table = QtWidgets.QTableWidget()
        table.setColumnCount(len(columns))
        table.setRowCount(len(index))
        table.setHorizontalHeaderLabels(columns)
        table.setVerticalHeaderLabels(index)
        for row in range(len(data)):
            for col in range(len(columns)):
                val = str(data[row][col])
                table.setItem(row, col, QtWidgets.QTableWidgetItem(val))
            
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        layout.addWidget(table)


    def remove_tables(self, layout):
        """
        Removes all table widgets from a layout

        Parameters
        -----------
            layout : QtLayout
        """

        for i in reversed(range(layout.count())): 
            if isinstance(layout.itemAt(i).widget(), QtWidgets.QTableWidget):
                layout.itemAt(i).widget().setParent(None)


    def init_figures(self):
        """
        Initializes all figures needed
        """

        # Histogram and AIC figure
        self.figure = Figure(constrained_layout=False) #To use tight layout
        # Add figure
        self.canvas = FigureCanvas(self.figure)  
        self.canvas.setMinimumSize(self.canvas.size())
        self.figure.clear()
        self.result_layout.addWidget(self.canvas)

        # Time distribution figure
        self.time_fig = Figure(constrained_layout=False)
        self.time_canvas = FigureCanvas(self.time_fig)  
        self.time_canvas.setMinimumSize(self.time_canvas.size())
        self.time_fig.clear()
        self.distr_time_layout.addWidget(self.time_canvas)

        # Cycles distribution figure
        self.cycles_fig = Figure(constrained_layout=False)
        self.cycles_canvas = FigureCanvas(self.cycles_fig)  
        self.cycles_canvas.setMinimumSize(self.cycles_canvas.size())
        self.cycles_fig.clear()
        self.distr_cycles_layout.addWidget(self.cycles_canvas)

        # Stades distribution figure
        self.quarter_fig = Figure(constrained_layout=False)
        self.quarter_canvas = FigureCanvas(self.quarter_fig)  
        self.quarter_canvas.setMinimumSize(self.quarter_canvas.size())
        self.quarter_fig.clear()
        self.distr_quarter_layout.addWidget(self.quarter_canvas)


    def _extract_information_from_DataFrame(self, df):
        """
        Extracts information from a DataFrame

        Parameters
        -----------
            df : Pandas Dataframe

        Returns
        -----------
            data    : list containing the values of each row of the DataFrame
            columns : list containing the columns name of the DataFrame
            index   : list containing the index value of the DataFrame
        """

        data = []
        columns = []
        index = []

        for ind, row in df.iterrows():
            index.append(ind)
            data.append(row.tolist())
        columns = df.columns.values

        return data, columns, index

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\klacourse\Documents\NGosselin\gitRepos\ceamscarms\Stand_alone_apps\scinodes_poc\src\main\python\plugins\CsvReaderMaster\Ui_CsvReaderMasterResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_CsvReaderMasterResultsView(object):
    def setupUi(self, CsvReaderMasterResultsView):
        CsvReaderMasterResultsView.setObjectName("CsvReaderMasterResultsView")
        CsvReaderMasterResultsView.resize(483, 218)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CsvReaderMasterResultsView)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.result_tablewidget = QtWidgets.QTableWidget(CsvReaderMasterResultsView)
        self.result_tablewidget.setObjectName("result_tablewidget")
        self.result_tablewidget.setColumnCount(0)
        self.result_tablewidget.setRowCount(0)
        self.verticalLayout.addWidget(self.result_tablewidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(CsvReaderMasterResultsView)
        QtCore.QMetaObject.connectSlotsByName(CsvReaderMasterResultsView)

    def retranslateUi(self, CsvReaderMasterResultsView):
        _translate = QtCore.QCoreApplication.translate
        CsvReaderMasterResultsView.setWindowTitle(_translate("CsvReaderMasterResultsView", "Form"))

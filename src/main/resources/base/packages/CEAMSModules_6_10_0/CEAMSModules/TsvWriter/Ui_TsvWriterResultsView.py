# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cbrain/projects/snooz-toolbox/src/main/python/plugins/TsvWriter/Ui_TsvWriterResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_TsvWriterResultsView(object):
    def setupUi(self, TsvWriterResultsView):
        TsvWriterResultsView.setObjectName("TsvWriterResultsView")
        TsvWriterResultsView.resize(483, 218)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(TsvWriterResultsView)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.result_tablewidget = QtWidgets.QTableWidget(TsvWriterResultsView)
        self.result_tablewidget.setObjectName("result_tablewidget")
        self.result_tablewidget.setColumnCount(0)
        self.result_tablewidget.setRowCount(0)
        self.verticalLayout.addWidget(self.result_tablewidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(TsvWriterResultsView)
        QtCore.QMetaObject.connectSlotsByName(TsvWriterResultsView)

    def retranslateUi(self, TsvWriterResultsView):
        _translate = QtCore.QCoreApplication.translate
        TsvWriterResultsView.setWindowTitle(_translate("TsvWriterResultsView", "Form"))


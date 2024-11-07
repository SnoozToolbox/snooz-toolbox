# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cbrain/projects/scinodes_poc/src/main/python/plugins/PSGReader/Ui_PSGReaderResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_PSGReaderResultsView(object):
    def setupUi(self, PSGReaderResultsView):
        PSGReaderResultsView.setObjectName("PSGReaderResultsView")
        PSGReaderResultsView.resize(483, 218)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(PSGReaderResultsView)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.result_tablewidget = QtWidgets.QTableWidget(PSGReaderResultsView)
        self.result_tablewidget.setObjectName("result_tablewidget")
        self.result_tablewidget.setColumnCount(0)
        self.result_tablewidget.setRowCount(0)
        self.verticalLayout.addWidget(self.result_tablewidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(PSGReaderResultsView)
        QtCore.QMetaObject.connectSlotsByName(PSGReaderResultsView)

    def retranslateUi(self, PSGReaderResultsView):
        _translate = QtCore.QCoreApplication.translate
        PSGReaderResultsView.setWindowTitle(_translate("PSGReaderResultsView", "Form"))


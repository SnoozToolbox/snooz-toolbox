# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cbrain/projects/scinodes_poc/src/main/python/plugins/EdfXmlReader/Ui_EdfXmlReaderResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_EdfXmlReaderResultsView(object):
    def setupUi(self, EdfXmlReaderResultsView):
        EdfXmlReaderResultsView.setObjectName("EdfXmlReaderResultsView")
        EdfXmlReaderResultsView.resize(483, 218)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EdfXmlReaderResultsView)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.result_tablewidget = QtWidgets.QTableWidget(EdfXmlReaderResultsView)
        self.result_tablewidget.setObjectName("result_tablewidget")
        self.result_tablewidget.setColumnCount(0)
        self.result_tablewidget.setRowCount(0)
        self.verticalLayout.addWidget(self.result_tablewidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(EdfXmlReaderResultsView)
        QtCore.QMetaObject.connectSlotsByName(EdfXmlReaderResultsView)

    def retranslateUi(self, EdfXmlReaderResultsView):
        _translate = QtCore.QCoreApplication.translate
        EdfXmlReaderResultsView.setWindowTitle(_translate("EdfXmlReaderResultsView", "Form"))


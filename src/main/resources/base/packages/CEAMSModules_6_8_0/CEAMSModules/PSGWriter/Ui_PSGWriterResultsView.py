# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cbrain/projects/scinodes_poc/src/main/python/plugins/PSGWriter/Ui_PSGWriterResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_PSGWriterResultsView(object):
    def setupUi(self, PSGWriterResultsView):
        PSGWriterResultsView.setObjectName("PSGWriterResultsView")
        PSGWriterResultsView.resize(483, 360)
        self.verticalLayout = QtWidgets.QVBoxLayout(PSGWriterResultsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.result_layout = QtWidgets.QVBoxLayout()
        self.result_layout.setObjectName("result_layout")
        self.verticalLayout.addLayout(self.result_layout)

        self.retranslateUi(PSGWriterResultsView)
        QtCore.QMetaObject.connectSlotsByName(PSGWriterResultsView)

    def retranslateUi(self, PSGWriterResultsView):
        _translate = QtCore.QCoreApplication.translate
        PSGWriterResultsView.setWindowTitle(_translate("PSGWriterResultsView", "Form"))


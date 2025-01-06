# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cbrain/projects/snooz-toolbox/src/main/python/plugins/Constant/Ui_ConstantResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_ConstantResultsView(object):
    def setupUi(self, ConstantResultsView):
        ConstantResultsView.setObjectName("ConstantResultsView")
        ConstantResultsView.resize(927, 262)
        self.verticalLayout = QtWidgets.QVBoxLayout(ConstantResultsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signal_layout = QtWidgets.QVBoxLayout()
        self.signal_layout.setObjectName("signal_layout")
        self.verticalLayout.addLayout(self.signal_layout)

        self.retranslateUi(ConstantResultsView)
        QtCore.QMetaObject.connectSlotsByName(ConstantResultsView)

    def retranslateUi(self, ConstantResultsView):
        _translate = QtCore.QCoreApplication.translate
        ConstantResultsView.setWindowTitle(_translate("ConstantResultsView", "Form"))


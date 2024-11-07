# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cbrain/projects/scinodes_poc/src/main/python/plugins/AliasSignals/Ui_AliasSignalsResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_AliasSignalsResultsView(object):
    def setupUi(self, AliasSignalsResultsView):
        AliasSignalsResultsView.setObjectName("AliasSignalsResultsView")
        AliasSignalsResultsView.resize(927, 262)
        self.verticalLayout = QtWidgets.QVBoxLayout(AliasSignalsResultsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signal_layout = QtWidgets.QVBoxLayout()
        self.signal_layout.setObjectName("signal_layout")
        self.verticalLayout.addLayout(self.signal_layout)

        self.retranslateUi(AliasSignalsResultsView)
        QtCore.QMetaObject.connectSlotsByName(AliasSignalsResultsView)

    def retranslateUi(self, AliasSignalsResultsView):
        _translate = QtCore.QCoreApplication.translate
        AliasSignalsResultsView.setWindowTitle(_translate("AliasSignalsResultsView", "Form"))


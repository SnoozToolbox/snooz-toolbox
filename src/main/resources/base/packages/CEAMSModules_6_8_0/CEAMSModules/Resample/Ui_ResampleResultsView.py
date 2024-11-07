# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cbrain/projects/scinodes_poc/src/main/python/plugins/Resample/Ui_ResampleResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_ResampleResultsView(object):
    def setupUi(self, ResampleResultsView):
        ResampleResultsView.setObjectName("ResampleResultsView")
        ResampleResultsView.resize(927, 262)
        self.verticalLayout = QtWidgets.QVBoxLayout(ResampleResultsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signal_layout = QtWidgets.QVBoxLayout()
        self.signal_layout.setObjectName("signal_layout")
        self.verticalLayout.addLayout(self.signal_layout)

        self.retranslateUi(ResampleResultsView)
        QtCore.QMetaObject.connectSlotsByName(ResampleResultsView)

    def retranslateUi(self, ResampleResultsView):
        _translate = QtCore.QCoreApplication.translate
        ResampleResultsView.setWindowTitle(_translate("ResampleResultsView", "Form"))


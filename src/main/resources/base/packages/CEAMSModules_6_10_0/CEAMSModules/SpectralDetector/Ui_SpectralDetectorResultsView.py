# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cbrain/projects/snooz-toolbox/src/main/python/plugins/SpectralDetector/Ui_SpectralDetectorResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_SpectralDetectorResultsView(object):
    def setupUi(self, SpectralDetectorResultsView):
        SpectralDetectorResultsView.setObjectName("SpectralDetectorResultsView")
        SpectralDetectorResultsView.resize(677, 303)
        self.verticalLayout = QtWidgets.QVBoxLayout(SpectralDetectorResultsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.result_layout = QtWidgets.QVBoxLayout()
        self.result_layout.setObjectName("result_layout")
        self.verticalLayout.addLayout(self.result_layout)

        self.retranslateUi(SpectralDetectorResultsView)
        QtCore.QMetaObject.connectSlotsByName(SpectralDetectorResultsView)

    def retranslateUi(self, SpectralDetectorResultsView):
        _translate = QtCore.QCoreApplication.translate
        SpectralDetectorResultsView.setWindowTitle(_translate("SpectralDetectorResultsView", "Form"))


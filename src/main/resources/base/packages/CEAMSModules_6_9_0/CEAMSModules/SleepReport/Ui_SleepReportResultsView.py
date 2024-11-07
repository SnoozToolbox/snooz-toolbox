# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/david/projects/scinodes_poc/src/main/python/plugins/SleepReport/Ui_SleepReportResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_SleepReportResultsView(object):
    def setupUi(self, SleepReportResultsView):
        SleepReportResultsView.setObjectName("SleepReportResultsView")
        SleepReportResultsView.resize(927, 262)
        self.verticalLayout = QtWidgets.QVBoxLayout(SleepReportResultsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signal_layout = QtWidgets.QVBoxLayout()
        self.signal_layout.setObjectName("signal_layout")
        self.verticalLayout.addLayout(self.signal_layout)

        self.retranslateUi(SleepReportResultsView)
        QtCore.QMetaObject.connectSlotsByName(SleepReportResultsView)

    def retranslateUi(self, SleepReportResultsView):
        _translate = QtCore.QCoreApplication.translate
        SleepReportResultsView.setWindowTitle(_translate("SleepReportResultsView", "Form"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/david/projects/snooz-toolbox/src/main/python/plugins/EventSleepReport/Ui_EventSleepReportResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_EventSleepReportResultsView(object):
    def setupUi(self, EventSleepReportResultsView):
        EventSleepReportResultsView.setObjectName("EventSleepReportResultsView")
        EventSleepReportResultsView.resize(483, 360)
        self.verticalLayout = QtWidgets.QVBoxLayout(EventSleepReportResultsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.result_layout = QtWidgets.QVBoxLayout()
        self.result_layout.setObjectName("result_layout")
        self.verticalLayout.addLayout(self.result_layout)

        self.retranslateUi(EventSleepReportResultsView)
        QtCore.QMetaObject.connectSlotsByName(EventSleepReportResultsView)

    def retranslateUi(self, EventSleepReportResultsView):
        _translate = QtCore.QCoreApplication.translate
        EventSleepReportResultsView.setWindowTitle(_translate("EventSleepReportResultsView", "Form"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\klacourse\Documents\NGosselin\gitRepos\ceamscarms\Stand_alone_apps\scinodes_poc\src\main\python\plugins\FilterEvents\Ui_FilterEventsResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_FilterEventsResultsView(object):
    def setupUi(self, FilterEventsResultsView):
        FilterEventsResultsView.setObjectName("FilterEventsResultsView")
        FilterEventsResultsView.resize(927, 262)
        self.verticalLayout = QtWidgets.QVBoxLayout(FilterEventsResultsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signal_layout = QtWidgets.QVBoxLayout()
        self.signal_layout.setObjectName("signal_layout")
        self.verticalLayout.addLayout(self.signal_layout)

        self.retranslateUi(FilterEventsResultsView)
        QtCore.QMetaObject.connectSlotsByName(FilterEventsResultsView)

    def retranslateUi(self, FilterEventsResultsView):
        _translate = QtCore.QCoreApplication.translate
        FilterEventsResultsView.setWindowTitle(_translate("FilterEventsResultsView", "Form"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/david/projects/snooz-toolbox/src/main/python/plugins/SleepBouts/Ui_SleepBoutsResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_SleepBoutsResultsView(object):
    def setupUi(self, SleepBoutsResultsView):
        SleepBoutsResultsView.setObjectName("SleepBoutsResultsView")
        SleepBoutsResultsView.resize(927, 262)
        self.verticalLayout = QtWidgets.QVBoxLayout(SleepBoutsResultsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signal_layout = QtWidgets.QVBoxLayout()
        self.signal_layout.setObjectName("signal_layout")
        self.verticalLayout.addLayout(self.signal_layout)

        self.retranslateUi(SleepBoutsResultsView)
        QtCore.QMetaObject.connectSlotsByName(SleepBoutsResultsView)

    def retranslateUi(self, SleepBoutsResultsView):
        _translate = QtCore.QCoreApplication.translate
        SleepBoutsResultsView.setWindowTitle(_translate("SleepBoutsResultsView", "Form"))

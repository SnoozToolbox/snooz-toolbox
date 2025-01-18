# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cbrain/projects/snooz-toolbox/src/main/python/plugins/EventCreator/Ui_EventCreatorResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_EventCreatorResultsView(object):
    def setupUi(self, EventCreatorResultsView):
        EventCreatorResultsView.setObjectName("EventCreatorResultsView")
        EventCreatorResultsView.resize(927, 262)
        self.verticalLayout = QtWidgets.QVBoxLayout(EventCreatorResultsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signal_layout = QtWidgets.QVBoxLayout()
        self.signal_layout.setObjectName("signal_layout")
        self.verticalLayout.addLayout(self.signal_layout)

        self.retranslateUi(EventCreatorResultsView)
        QtCore.QMetaObject.connectSlotsByName(EventCreatorResultsView)

    def retranslateUi(self, EventCreatorResultsView):
        _translate = QtCore.QCoreApplication.translate
        EventCreatorResultsView.setWindowTitle(_translate("EventCreatorResultsView", "Form"))


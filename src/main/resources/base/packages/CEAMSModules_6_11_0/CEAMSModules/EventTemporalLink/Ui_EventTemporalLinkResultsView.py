# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/david/projects/snooz-toolbox/src/main/python/plugins/EventTemporalLink/Ui_EventTemporalLinkResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_EventTemporalLinkResultsView(object):
    def setupUi(self, EventTemporalLinkResultsView):
        EventTemporalLinkResultsView.setObjectName("EventTemporalLinkResultsView")
        EventTemporalLinkResultsView.resize(483, 360)
        self.verticalLayout = QtWidgets.QVBoxLayout(EventTemporalLinkResultsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.result_layout = QtWidgets.QVBoxLayout()
        self.result_layout.setObjectName("result_layout")
        self.verticalLayout.addLayout(self.result_layout)

        self.retranslateUi(EventTemporalLinkResultsView)
        QtCore.QMetaObject.connectSlotsByName(EventTemporalLinkResultsView)

    def retranslateUi(self, EventTemporalLinkResultsView):
        _translate = QtCore.QCoreApplication.translate
        EventTemporalLinkResultsView.setWindowTitle(_translate("EventTemporalLinkResultsView", "Form"))

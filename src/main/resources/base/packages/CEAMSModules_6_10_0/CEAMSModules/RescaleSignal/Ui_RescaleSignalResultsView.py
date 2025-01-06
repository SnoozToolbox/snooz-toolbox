# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_RescaleSignalResultsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RescaleSignalResultsView(object):
    def setupUi(self, RescaleSignalResultsView):
        if not RescaleSignalResultsView.objectName():
            RescaleSignalResultsView.setObjectName(u"RescaleSignalResultsView")
        RescaleSignalResultsView.resize(927, 262)
        self.verticalLayout = QVBoxLayout(RescaleSignalResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signals_layout = QVBoxLayout()
        self.signals_layout.setObjectName(u"signals_layout")

        self.verticalLayout.addLayout(self.signals_layout)


        self.retranslateUi(RescaleSignalResultsView)

        QMetaObject.connectSlotsByName(RescaleSignalResultsView)
    # setupUi

    def retranslateUi(self, RescaleSignalResultsView):
        RescaleSignalResultsView.setWindowTitle(QCoreApplication.translate("RescaleSignalResultsView", u"Form", None))
    # retranslateUi


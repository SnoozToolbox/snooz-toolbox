# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_WpliConnectivityResultsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import themes_rc

class Ui_WpliConnectivityResultsView(object):
    def setupUi(self, WpliConnectivityResultsView):
        if not WpliConnectivityResultsView.objectName():
            WpliConnectivityResultsView.setObjectName(u"WpliConnectivityResultsView")
        WpliConnectivityResultsView.setStyleSheet(u"font: 10pt \"Roboto-Regular\";")
        WpliConnectivityResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(WpliConnectivityResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(WpliConnectivityResultsView)

        QMetaObject.connectSlotsByName(WpliConnectivityResultsView)
    # setupUi

    def retranslateUi(self, WpliConnectivityResultsView):
        WpliConnectivityResultsView.setWindowTitle(QCoreApplication.translate("WpliConnectivityResultsView", u"Form", None))
    # retranslateUi


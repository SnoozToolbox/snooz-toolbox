# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_IcaComponentsResultsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_IcaComponentsResultsView(object):
    def setupUi(self, IcaComponentsResultsView):
        if not IcaComponentsResultsView.objectName():
            IcaComponentsResultsView.setObjectName(u"IcaComponentsResultsView")
        IcaComponentsResultsView.resize(927, 262)
        self.verticalLayout = QVBoxLayout(IcaComponentsResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signal_layout = QVBoxLayout()
        self.signal_layout.setObjectName(u"signal_layout")

        self.verticalLayout.addLayout(self.signal_layout)


        self.retranslateUi(IcaComponentsResultsView)

        QMetaObject.connectSlotsByName(IcaComponentsResultsView)
    # setupUi

    def retranslateUi(self, IcaComponentsResultsView):
        IcaComponentsResultsView.setWindowTitle(QCoreApplication.translate("IcaComponentsResultsView", u"Form", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_RenameFileListResultsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_RenameFileListResultsView(object):
    def setupUi(self, RenameFileListResultsView):
        if not RenameFileListResultsView.objectName():
            RenameFileListResultsView.setObjectName(u"RenameFileListResultsView")
        RenameFileListResultsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        RenameFileListResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(RenameFileListResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(RenameFileListResultsView)

        QMetaObject.connectSlotsByName(RenameFileListResultsView)
    # setupUi

    def retranslateUi(self, RenameFileListResultsView):
        RenameFileListResultsView.setWindowTitle(QCoreApplication.translate("RenameFileListResultsView", u"Form", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MutualInfoSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MutualInfoSettingsView(object):
    def setupUi(self, MutualInfoSettingsView):
        if not MutualInfoSettingsView.objectName():
            MutualInfoSettingsView.setObjectName(u"MutualInfoSettingsView")
        MutualInfoSettingsView.resize(448, 241)
        self.gridLayout = QGridLayout(MutualInfoSettingsView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = QLabel(MutualInfoSettingsView)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(MutualInfoSettingsView)

        QMetaObject.connectSlotsByName(MutualInfoSettingsView)
    # setupUi

    def retranslateUi(self, MutualInfoSettingsView):
        MutualInfoSettingsView.setWindowTitle(QCoreApplication.translate("MutualInfoSettingsView", u"Form", None))
        self.Title.setText(QCoreApplication.translate("MutualInfoSettingsView", u"MutualInfo settings", None))
    # retranslateUi


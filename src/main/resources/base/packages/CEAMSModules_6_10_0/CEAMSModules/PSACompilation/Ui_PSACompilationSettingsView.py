# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_PSACompilationSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PSACompilationSettingsView(object):
    def setupUi(self, PSACompilationSettingsView):
        if not PSACompilationSettingsView.objectName():
            PSACompilationSettingsView.setObjectName(u"PSACompilationSettingsView")
        PSACompilationSettingsView.resize(625, 118)
        self.verticalLayout = QVBoxLayout(PSACompilationSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filename_label = QLabel(PSACompilationSettingsView)
        self.filename_label.setObjectName(u"filename_label")

        self.horizontalLayout.addWidget(self.filename_label)

        self.filename_lineedit = QLineEdit(PSACompilationSettingsView)
        self.filename_lineedit.setObjectName(u"filename_lineedit")
        self.filename_lineedit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.filename_lineedit)

        self.choose_pushButton = QPushButton(PSACompilationSettingsView)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.horizontalLayout.addWidget(self.choose_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(PSACompilationSettingsView)
        self.choose_pushButton.clicked.connect(PSACompilationSettingsView.choose_button_slot)

        QMetaObject.connectSlotsByName(PSACompilationSettingsView)
    # setupUi

    def retranslateUi(self, PSACompilationSettingsView):
        PSACompilationSettingsView.setWindowTitle(QCoreApplication.translate("PSACompilationSettingsView", u"Form", None))
        self.filename_label.setText(QCoreApplication.translate("PSACompilationSettingsView", u"Filename", None))
        self.filename_lineedit.setInputMask("")
        self.filename_lineedit.setText("")
        self.filename_lineedit.setPlaceholderText(QCoreApplication.translate("PSACompilationSettingsView", u"Choose a TSV file to write to", None))
        self.choose_pushButton.setText(QCoreApplication.translate("PSACompilationSettingsView", u"Choose", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SpindlesDetailsSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SpindlesDetailsSettingsView(object):
    def setupUi(self, SpindlesDetailsSettingsView):
        if not SpindlesDetailsSettingsView.objectName():
            SpindlesDetailsSettingsView.setObjectName(u"SpindlesDetailsSettingsView")
        SpindlesDetailsSettingsView.resize(794, 272)
        self.verticalLayout = QVBoxLayout(SpindlesDetailsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(SpindlesDetailsSettingsView)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.details_filename_label = QLabel(SpindlesDetailsSettingsView)
        self.details_filename_label.setObjectName(u"details_filename_label")

        self.horizontalLayout.addWidget(self.details_filename_label)

        self.details_filename_lineedit = QLineEdit(SpindlesDetailsSettingsView)
        self.details_filename_lineedit.setObjectName(u"details_filename_lineedit")
        self.details_filename_lineedit.setMinimumSize(QSize(340, 0))
        self.details_filename_lineedit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.details_filename_lineedit)

        self.pushButton_browse = QPushButton(SpindlesDetailsSettingsView)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout.addWidget(self.pushButton_browse)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SpindlesDetailsSettingsView)
        self.pushButton_browse.clicked.connect(SpindlesDetailsSettingsView.browse_slot)

        QMetaObject.connectSlotsByName(SpindlesDetailsSettingsView)
    # setupUi

    def retranslateUi(self, SpindlesDetailsSettingsView):
        SpindlesDetailsSettingsView.setWindowTitle(QCoreApplication.translate("SpindlesDetailsSettingsView", u"Form", None))
        self.label.setText(QCoreApplication.translate("SpindlesDetailsSettingsView", u"Spindle event details Settings View", None))
        self.details_filename_label.setText(QCoreApplication.translate("SpindlesDetailsSettingsView", u"Spindle events details filename", None))
        self.details_filename_lineedit.setPlaceholderText(QCoreApplication.translate("SpindlesDetailsSettingsView", u"Choose the filename to save the spindle events details...", None))
        self.pushButton_browse.setText(QCoreApplication.translate("SpindlesDetailsSettingsView", u"Browse", None))
    # retranslateUi


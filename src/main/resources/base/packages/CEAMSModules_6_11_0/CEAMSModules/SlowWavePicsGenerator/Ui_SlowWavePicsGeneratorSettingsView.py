# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SlowWavePicsGeneratorSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_SlowWavePicsGeneratorSettingsView(object):
    def setupUi(self, SlowWavePicsGeneratorSettingsView):
        if not SlowWavePicsGeneratorSettingsView.objectName():
            SlowWavePicsGeneratorSettingsView.setObjectName(u"SlowWavePicsGeneratorSettingsView")
        SlowWavePicsGeneratorSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        SlowWavePicsGeneratorSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(SlowWavePicsGeneratorSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.files_horizontalLayout = QHBoxLayout()
        self.files_horizontalLayout.setObjectName(u"files_horizontalLayout")
        self.files_label = QLabel(SlowWavePicsGeneratorSettingsView)
        self.files_label.setObjectName(u"files_label")

        self.files_horizontalLayout.addWidget(self.files_label)

        self.files_lineedit = QLineEdit(SlowWavePicsGeneratorSettingsView)
        self.files_lineedit.setObjectName(u"files_lineedit")

        self.files_horizontalLayout.addWidget(self.files_lineedit)


        self.verticalLayout.addLayout(self.files_horizontalLayout)

        self.file_group_horizontalLayout = QHBoxLayout()
        self.file_group_horizontalLayout.setObjectName(u"file_group_horizontalLayout")
        self.file_group_label = QLabel(SlowWavePicsGeneratorSettingsView)
        self.file_group_label.setObjectName(u"file_group_label")

        self.file_group_horizontalLayout.addWidget(self.file_group_label)

        self.file_group_lineedit = QLineEdit(SlowWavePicsGeneratorSettingsView)
        self.file_group_lineedit.setObjectName(u"file_group_lineedit")

        self.file_group_horizontalLayout.addWidget(self.file_group_lineedit)


        self.verticalLayout.addLayout(self.file_group_horizontalLayout)

        self.sw_char_folder_horizontalLayout = QHBoxLayout()
        self.sw_char_folder_horizontalLayout.setObjectName(u"sw_char_folder_horizontalLayout")
        self.sw_char_folder_label = QLabel(SlowWavePicsGeneratorSettingsView)
        self.sw_char_folder_label.setObjectName(u"sw_char_folder_label")

        self.sw_char_folder_horizontalLayout.addWidget(self.sw_char_folder_label)

        self.sw_char_folder_lineedit = QLineEdit(SlowWavePicsGeneratorSettingsView)
        self.sw_char_folder_lineedit.setObjectName(u"sw_char_folder_lineedit")

        self.sw_char_folder_horizontalLayout.addWidget(self.sw_char_folder_lineedit)


        self.verticalLayout.addLayout(self.sw_char_folder_horizontalLayout)

        self.pics_param_horizontalLayout = QHBoxLayout()
        self.pics_param_horizontalLayout.setObjectName(u"pics_param_horizontalLayout")
        self.pics_param_label = QLabel(SlowWavePicsGeneratorSettingsView)
        self.pics_param_label.setObjectName(u"pics_param_label")

        self.pics_param_horizontalLayout.addWidget(self.pics_param_label)

        self.pics_param_lineedit = QLineEdit(SlowWavePicsGeneratorSettingsView)
        self.pics_param_lineedit.setObjectName(u"pics_param_lineedit")

        self.pics_param_horizontalLayout.addWidget(self.pics_param_lineedit)


        self.verticalLayout.addLayout(self.pics_param_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SlowWavePicsGeneratorSettingsView)

        QMetaObject.connectSlotsByName(SlowWavePicsGeneratorSettingsView)
    # setupUi

    def retranslateUi(self, SlowWavePicsGeneratorSettingsView):
        SlowWavePicsGeneratorSettingsView.setWindowTitle(QCoreApplication.translate("SlowWavePicsGeneratorSettingsView", u"Form", None))
        self.files_label.setText(QCoreApplication.translate("SlowWavePicsGeneratorSettingsView", u"files", None))
        self.file_group_label.setText(QCoreApplication.translate("SlowWavePicsGeneratorSettingsView", u"file_group", None))
        self.sw_char_folder_label.setText(QCoreApplication.translate("SlowWavePicsGeneratorSettingsView", u"sw_char_folder", None))
        self.pics_param_label.setText(QCoreApplication.translate("SlowWavePicsGeneratorSettingsView", u"pics_param", None))
    # retranslateUi


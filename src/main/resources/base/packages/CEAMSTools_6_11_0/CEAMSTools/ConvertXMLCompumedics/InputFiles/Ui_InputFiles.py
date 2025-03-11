# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_InputFiles.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_InputFiles(object):
    def setupUi(self, InputFiles):
        if not InputFiles.objectName():
            InputFiles.setObjectName(u"InputFiles")
        InputFiles.resize(877, 503)
        self.horizontalLayout_2 = QHBoxLayout(InputFiles)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget_files = QTableWidget(InputFiles)
        self.tableWidget_files.setObjectName(u"tableWidget_files")
        self.tableWidget_files.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout.addWidget(self.tableWidget_files)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_choose = QPushButton(InputFiles)
        self.pushButton_choose.setObjectName(u"pushButton_choose")
        self.pushButton_choose.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_choose)

        self.pushButton_clear = QPushButton(InputFiles)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_clear)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(InputFiles)
        self.pushButton_clear.clicked.connect(InputFiles.clear_slot)
        self.pushButton_choose.clicked.connect(InputFiles.choose_slot)

        QMetaObject.connectSlotsByName(InputFiles)
    # setupUi

    def retranslateUi(self, InputFiles):
        InputFiles.setWindowTitle("")
        InputFiles.setStyleSheet(QCoreApplication.translate("InputFiles", u"font: 12pt \"Roboto\";", None))
        self.pushButton_choose.setText(QCoreApplication.translate("InputFiles", u"Choose", None))
        self.pushButton_clear.setText(QCoreApplication.translate("InputFiles", u"Clear", None))
    # retranslateUi


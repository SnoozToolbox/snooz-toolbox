# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_FileErrorDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_FileErrorDialog(object):
    def setupUi(self, FileErrorDialog):
        if not FileErrorDialog.objectName():
            FileErrorDialog.setObjectName(u"FileErrorDialog")
        FileErrorDialog.resize(400, 388)
        self.verticalLayout = QVBoxLayout(FileErrorDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(FileErrorDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.files_listwidget = QListWidget(FileErrorDialog)
        self.files_listwidget.setObjectName(u"files_listwidget")

        self.verticalLayout.addWidget(self.files_listwidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ok_pushbutton = QPushButton(FileErrorDialog)
        self.ok_pushbutton.setObjectName(u"ok_pushbutton")

        self.horizontalLayout.addWidget(self.ok_pushbutton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(FileErrorDialog)
        self.ok_pushbutton.clicked.connect(FileErrorDialog.close)

        QMetaObject.connectSlotsByName(FileErrorDialog)
    # setupUi

    def retranslateUi(self, FileErrorDialog):
        FileErrorDialog.setWindowTitle(QCoreApplication.translate("FileErrorDialog", u"Dialog", None))
        FileErrorDialog.setStyleSheet(QCoreApplication.translate("FileErrorDialog", u"font: 12pt \"Roboto\";", None))
        self.label.setText(QCoreApplication.translate("FileErrorDialog", u"ERROR: could not complete the command in these files:", None))
        self.ok_pushbutton.setText(QCoreApplication.translate("FileErrorDialog", u"Ok", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MissingPackagesDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MissingPackagesDialog(object):
    def setupUi(self, MissingPackagesDialog):
        if not MissingPackagesDialog.objectName():
            MissingPackagesDialog.setObjectName(u"MissingPackagesDialog")
        MissingPackagesDialog.resize(759, 715)
        self.verticalLayout = QVBoxLayout(MissingPackagesDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(MissingPackagesDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(MissingPackagesDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.missing_packages_tablewidget = QTableWidget(MissingPackagesDialog)
        if (self.missing_packages_tablewidget.columnCount() < 2):
            self.missing_packages_tablewidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.missing_packages_tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.missing_packages_tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.missing_packages_tablewidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.missing_packages_tablewidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.missing_packages_tablewidget.setObjectName(u"missing_packages_tablewidget")
        self.missing_packages_tablewidget.setColumnCount(4)
        self.missing_packages_tablewidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.missing_packages_tablewidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ok_pushbutton = QPushButton(MissingPackagesDialog)
        self.ok_pushbutton.setObjectName(u"ok_pushbutton")

        self.horizontalLayout.addWidget(self.ok_pushbutton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(MissingPackagesDialog)
        self.ok_pushbutton.clicked.connect(MissingPackagesDialog.close)

        QMetaObject.connectSlotsByName(MissingPackagesDialog)
    # setupUi

    def retranslateUi(self, MissingPackagesDialog):
        MissingPackagesDialog.setWindowTitle(QCoreApplication.translate("MissingPackagesDialog", u"Missing packages", None))
        self.label.setText(QCoreApplication.translate("MissingPackagesDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Missing package</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MissingPackagesDialog", u"WARNING These package are needed to be able to run this process. Find these package and add them in File->Settings->Package.", None))
        ___qtablewidgetitem = self.missing_packages_tablewidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MissingPackagesDialog", u"Package", None));
        ___qtablewidgetitem1 = self.missing_packages_tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MissingPackagesDialog", u"Version", None));
        self.ok_pushbutton.setText(QCoreApplication.translate("MissingPackagesDialog", u"Ok", None))
    # retranslateUi


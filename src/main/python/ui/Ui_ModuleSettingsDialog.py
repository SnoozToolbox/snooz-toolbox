# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ModuleSettingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ModuleSettingsDialog(object):
    def setupUi(self, ModuleSettingsDialog):
        if not ModuleSettingsDialog.objectName():
            ModuleSettingsDialog.setObjectName(u"ModuleSettingsDialog")
        ModuleSettingsDialog.resize(759, 715)
        self.verticalLayout = QVBoxLayout(ModuleSettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(ModuleSettingsDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(ModuleSettingsDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.package_treewidget = QTreeWidget(ModuleSettingsDialog)
        self.package_treewidget.setObjectName(u"package_treewidget")

        self.verticalLayout_2.addWidget(self.package_treewidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel_pushbutton = QPushButton(ModuleSettingsDialog)
        self.cancel_pushbutton.setObjectName(u"cancel_pushbutton")

        self.horizontalLayout.addWidget(self.cancel_pushbutton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.apply_pushbutton = QPushButton(ModuleSettingsDialog)
        self.apply_pushbutton.setObjectName(u"apply_pushbutton")

        self.horizontalLayout.addWidget(self.apply_pushbutton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(ModuleSettingsDialog)
        self.apply_pushbutton.clicked.connect(ModuleSettingsDialog.apply_clicked)
        self.cancel_pushbutton.clicked.connect(ModuleSettingsDialog.cancel_clicked)
        self.package_treewidget.itemChanged.connect(ModuleSettingsDialog.data_changed)

        QMetaObject.connectSlotsByName(ModuleSettingsDialog)
    # setupUi

    def retranslateUi(self, ModuleSettingsDialog):
        ModuleSettingsDialog.setWindowTitle(QCoreApplication.translate("ModuleSettingsDialog", u"Settings SciNode", None))
        self.label.setText(QCoreApplication.translate("ModuleSettingsDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Module Library Settings</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("ModuleSettingsDialog", u"Please select the packages you want to activate.", None))
        ___qtreewidgetitem = self.package_treewidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("ModuleSettingsDialog", u"Version", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("ModuleSettingsDialog", u"Package", None));
        self.cancel_pushbutton.setText(QCoreApplication.translate("ModuleSettingsDialog", u"Cancel", None))
        self.apply_pushbutton.setText(QCoreApplication.translate("ModuleSettingsDialog", u"Apply", None))
    # retranslateUi


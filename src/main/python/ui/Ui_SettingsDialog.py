# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SettingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(1010, 715)
        SettingsDialog.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(SettingsDialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.settings_list = QListWidget(self.splitter)
        QListWidgetItem(self.settings_list)
        QListWidgetItem(self.settings_list)
        self.settings_list.setObjectName(u"settings_list")
        self.settings_list.setAlternatingRowColors(False)
        self.splitter.addWidget(self.settings_list)
        self.stackedWidget = QStackedWidget(self.splitter)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.general_settings_page = QWidget()
        self.general_settings_page.setObjectName(u"general_settings_page")
        self.verticalLayout_3 = QVBoxLayout(self.general_settings_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.general_settings_page)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.general_settings_page)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.reset_to_default_pushButton = QPushButton(self.general_settings_page)
        self.reset_to_default_pushButton.setObjectName(u"reset_to_default_pushButton")

        self.horizontalLayout.addWidget(self.reset_to_default_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.stackedWidget.addWidget(self.general_settings_page)
        self.plugins_page = QWidget()
        self.plugins_page.setObjectName(u"plugins_page")
        self.verticalLayout_5 = QVBoxLayout(self.plugins_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.plugins_page)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_4 = QLabel(self.plugins_page)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.packages_treewidget = QTreeWidget(self.plugins_page)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(1, u"2");
        __qtreewidgetitem.setText(0, u"1");
        self.packages_treewidget.setHeaderItem(__qtreewidgetitem)
        self.packages_treewidget.setObjectName(u"packages_treewidget")
        self.packages_treewidget.setSortingEnabled(True)
        self.packages_treewidget.setAnimated(True)
        self.packages_treewidget.setColumnCount(2)

        self.verticalLayout_4.addWidget(self.packages_treewidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.plugins_remove_pushbutton = QPushButton(self.plugins_page)
        self.plugins_remove_pushbutton.setObjectName(u"plugins_remove_pushbutton")

        self.horizontalLayout_2.addWidget(self.plugins_remove_pushbutton)

        self.plugins_add_from_folder_pushbutton = QPushButton(self.plugins_page)
        self.plugins_add_from_folder_pushbutton.setObjectName(u"plugins_add_from_folder_pushbutton")

        self.horizontalLayout_2.addWidget(self.plugins_add_from_folder_pushbutton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.plugins_apply_pushButton = QPushButton(self.plugins_page)
        self.plugins_apply_pushButton.setObjectName(u"plugins_apply_pushButton")

        self.horizontalLayout_2.addWidget(self.plugins_apply_pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.stackedWidget.addWidget(self.plugins_page)
        self.splitter.addWidget(self.stackedWidget)

        self.verticalLayout.addWidget(self.splitter)


        self.retranslateUi(SettingsDialog)
        self.plugins_add_from_folder_pushbutton.clicked.connect(SettingsDialog.plugins_on_add_from_folder)
        self.plugins_remove_pushbutton.clicked.connect(SettingsDialog.plugins_on_remove)
        self.reset_to_default_pushButton.clicked.connect(SettingsDialog.reset_to_default)
        self.settings_list.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.plugins_apply_pushButton.clicked.connect(SettingsDialog.apply_package_changes)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings Snooz", None))

        __sortingEnabled = self.settings_list.isSortingEnabled()
        self.settings_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.settings_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("SettingsDialog", u"General Settings", None));
        ___qlistwidgetitem1 = self.settings_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("SettingsDialog", u"Packages", None));
        self.settings_list.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("SettingsDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">General Settings</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"Reset all settings to default", None))
        self.reset_to_default_pushButton.setText(QCoreApplication.translate("SettingsDialog", u"Reset to default", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Packages</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("SettingsDialog", u"Once added, activate the package you want to use by using the associated checkbox then press Apply.", None))
        self.plugins_remove_pushbutton.setText(QCoreApplication.translate("SettingsDialog", u"Remove", None))
        self.plugins_add_from_folder_pushbutton.setText(QCoreApplication.translate("SettingsDialog", u"Add from folder", None))
#if QT_CONFIG(tooltip)
        self.plugins_apply_pushButton.setToolTip(QCoreApplication.translate("SettingsDialog", u"Apply activation selection", None))
#endif // QT_CONFIG(tooltip)
        self.plugins_apply_pushButton.setText(QCoreApplication.translate("SettingsDialog", u"Apply", None))
    # retranslateUi


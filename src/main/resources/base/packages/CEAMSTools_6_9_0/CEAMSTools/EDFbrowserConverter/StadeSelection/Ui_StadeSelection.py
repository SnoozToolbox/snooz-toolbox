# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_StadeSelection.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_StadeSelection(object):
    def setupUi(self, StadeSelection):
        if not StadeSelection.objectName():
            StadeSelection.setObjectName(u"StadeSelection")
        StadeSelection.resize(1204, 469)
        self.horizontalLayout_2 = QHBoxLayout(StadeSelection)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(StadeSelection)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.file_listview = QListView(StadeSelection)
        self.file_listview.setObjectName(u"file_listview")

        self.verticalLayout.addWidget(self.file_listview)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(StadeSelection)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.event_treeview = QListView(StadeSelection)
        self.event_treeview.setObjectName(u"event_treeview")
        self.event_treeview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.event_treeview.setSelectionMode(QAbstractItemView.NoSelection)
        self.event_treeview.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.verticalLayout_2.addWidget(self.event_treeview)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_all_checkBox = QCheckBox(StadeSelection)
        self.select_all_checkBox.setObjectName(u"select_all_checkBox")

        self.horizontalLayout.addWidget(self.select_all_checkBox)

        self.search_lineEdit = QLineEdit(StadeSelection)
        self.search_lineEdit.setObjectName(u"search_lineEdit")

        self.horizontalLayout.addWidget(self.search_lineEdit)

        self.apply_all_pushButton = QPushButton(StadeSelection)
        self.apply_all_pushButton.setObjectName(u"apply_all_pushButton")

        self.horizontalLayout.addWidget(self.apply_all_pushButton)

        self.reset_all_files_pushButton = QPushButton(StadeSelection)
        self.reset_all_files_pushButton.setObjectName(u"reset_all_files_pushButton")

        self.horizontalLayout.addWidget(self.reset_all_files_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.retranslateUi(StadeSelection)
        self.file_listview.clicked.connect(StadeSelection.on_file_selected)
        self.apply_all_pushButton.clicked.connect(StadeSelection.on_apply_to_all_files)
        self.select_all_checkBox.stateChanged.connect(StadeSelection.on_select_all_groups)
        self.reset_all_files_pushButton.clicked.connect(StadeSelection.on_reset_all_files)
        self.search_lineEdit.textEdited.connect(StadeSelection.search_pattern_slot)

        QMetaObject.connectSlotsByName(StadeSelection)
    # setupUi

    def retranslateUi(self, StadeSelection):
        StadeSelection.setWindowTitle(QCoreApplication.translate("StadeSelection", u"Form", None))
        StadeSelection.setStyleSheet(QCoreApplication.translate("StadeSelection", u"font: 12pt \"Roboto\";", None))
        self.label.setText(QCoreApplication.translate("StadeSelection", u"PSG Files", None))
        self.label_2.setText(QCoreApplication.translate("StadeSelection", u"Events", None))
        self.select_all_checkBox.setText(QCoreApplication.translate("StadeSelection", u"Select All", None))
        self.search_lineEdit.setText("")
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("StadeSelection", u"Search Event Group", None))
        self.apply_all_pushButton.setText(QCoreApplication.translate("StadeSelection", u"Apply to all files", None))
        self.reset_all_files_pushButton.setText(QCoreApplication.translate("StadeSelection", u"Reset all files", None))
    # retranslateUi


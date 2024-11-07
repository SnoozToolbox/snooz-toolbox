# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AnnotationsSelection.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_AnnotationsSelection(object):
    def setupUi(self, AnnotationsSelection):
        if not AnnotationsSelection.objectName():
            AnnotationsSelection.setObjectName(u"AnnotationsSelection")
        AnnotationsSelection.resize(837, 667)
        self.horizontalLayout_2 = QHBoxLayout(AnnotationsSelection)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(AnnotationsSelection)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.file_listview = QListView(AnnotationsSelection)
        self.file_listview.setObjectName(u"file_listview")

        self.verticalLayout.addWidget(self.file_listview)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(AnnotationsSelection)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.event_treeview = QTreeView(AnnotationsSelection)
        self.event_treeview.setObjectName(u"event_treeview")
        self.event_treeview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.event_treeview.setSelectionMode(QAbstractItemView.NoSelection)
        self.event_treeview.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.verticalLayout_2.addWidget(self.event_treeview)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_all_checkBox = QCheckBox(AnnotationsSelection)
        self.select_all_checkBox.setObjectName(u"select_all_checkBox")

        self.horizontalLayout.addWidget(self.select_all_checkBox)

        self.search_lineEdit = QLineEdit(AnnotationsSelection)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        self.search_lineEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.search_lineEdit)

        self.apply_all_pushButton = QPushButton(AnnotationsSelection)
        self.apply_all_pushButton.setObjectName(u"apply_all_pushButton")

        self.horizontalLayout.addWidget(self.apply_all_pushButton)

        self.reset_all_files_pushButton = QPushButton(AnnotationsSelection)
        self.reset_all_files_pushButton.setObjectName(u"reset_all_files_pushButton")

        self.horizontalLayout.addWidget(self.reset_all_files_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.reset_excl_event_checkBox = QCheckBox(AnnotationsSelection)
        self.reset_excl_event_checkBox.setObjectName(u"reset_excl_event_checkBox")

        self.verticalLayout_2.addWidget(self.reset_excl_event_checkBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.retranslateUi(AnnotationsSelection)
        self.file_listview.clicked.connect(AnnotationsSelection.on_file_selected)
        self.apply_all_pushButton.clicked.connect(AnnotationsSelection.on_apply_to_all_files)
        self.select_all_checkBox.stateChanged.connect(AnnotationsSelection.on_select_all_groups)
        self.reset_all_files_pushButton.clicked.connect(AnnotationsSelection.on_reset_all_files)
        self.search_lineEdit.textEdited.connect(AnnotationsSelection.search_pattern_slot)

        QMetaObject.connectSlotsByName(AnnotationsSelection)
    # setupUi

    def retranslateUi(self, AnnotationsSelection):
        AnnotationsSelection.setWindowTitle(QCoreApplication.translate("AnnotationsSelection", u"Form", None))
        AnnotationsSelection.setStyleSheet(QCoreApplication.translate("AnnotationsSelection", u"font: 12pt \"Roboto\";", None))
        self.label.setText(QCoreApplication.translate("AnnotationsSelection", u"PSG Files", None))
        self.label_2.setText(QCoreApplication.translate("AnnotationsSelection", u"Events", None))
        self.select_all_checkBox.setText(QCoreApplication.translate("AnnotationsSelection", u"Select All", None))
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("AnnotationsSelection", u"Event group search", None))
        self.apply_all_pushButton.setText(QCoreApplication.translate("AnnotationsSelection", u"Apply to all files", None))
        self.reset_all_files_pushButton.setText(QCoreApplication.translate("AnnotationsSelection", u"Reset all files", None))
        self.reset_excl_event_checkBox.setText(QCoreApplication.translate("AnnotationsSelection", u"Reset the signal of excluded events ", None))
    # retranslateUi


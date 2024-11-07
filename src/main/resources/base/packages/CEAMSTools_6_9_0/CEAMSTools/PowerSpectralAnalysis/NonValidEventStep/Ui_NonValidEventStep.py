# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_NonValidEventStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_NonValidEventStep(object):
    def setupUi(self, NonValidEventStep):
        if not NonValidEventStep.objectName():
            NonValidEventStep.setObjectName(u"NonValidEventStep")
        NonValidEventStep.resize(837, 667)
        self.horizontalLayout_2 = QHBoxLayout(NonValidEventStep)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(NonValidEventStep)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.file_listview = QListView(NonValidEventStep)
        self.file_listview.setObjectName(u"file_listview")
        self.file_listview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.file_listview.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.file_listview.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.verticalLayout.addWidget(self.file_listview)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(NonValidEventStep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.event_treeview = QTreeView(NonValidEventStep)
        self.event_treeview.setObjectName(u"event_treeview")
        self.event_treeview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.event_treeview.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.event_treeview.setSelectionMode(QAbstractItemView.SingleSelection)
        self.event_treeview.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.verticalLayout_2.addWidget(self.event_treeview)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_all_checkBox = QCheckBox(NonValidEventStep)
        self.select_all_checkBox.setObjectName(u"select_all_checkBox")

        self.horizontalLayout.addWidget(self.select_all_checkBox)

        self.search_lineEdit = QLineEdit(NonValidEventStep)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        self.search_lineEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.search_lineEdit)

        self.reset_all_files_pushButton = QPushButton(NonValidEventStep)
        self.reset_all_files_pushButton.setObjectName(u"reset_all_files_pushButton")

        self.horizontalLayout.addWidget(self.reset_all_files_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.reset_excl_event_checkBox = QCheckBox(NonValidEventStep)
        self.reset_excl_event_checkBox.setObjectName(u"reset_excl_event_checkBox")

        self.verticalLayout_2.addWidget(self.reset_excl_event_checkBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.retranslateUi(NonValidEventStep)
        self.file_listview.clicked.connect(NonValidEventStep.on_file_selected)
        self.select_all_checkBox.stateChanged.connect(NonValidEventStep.on_select_all_groups)
        self.reset_all_files_pushButton.clicked.connect(NonValidEventStep.on_reset_all_files)
        self.search_lineEdit.textEdited.connect(NonValidEventStep.search_pattern_slot)

        QMetaObject.connectSlotsByName(NonValidEventStep)
    # setupUi

    def retranslateUi(self, NonValidEventStep):
        NonValidEventStep.setWindowTitle(QCoreApplication.translate("NonValidEventStep", u"Form", None))
        NonValidEventStep.setStyleSheet(QCoreApplication.translate("NonValidEventStep", u"font: 12pt \"Roboto\";", None))
        self.label.setText(QCoreApplication.translate("NonValidEventStep", u"PSG Files", None))
        self.label_2.setText(QCoreApplication.translate("NonValidEventStep", u"Events", None))
        self.select_all_checkBox.setText(QCoreApplication.translate("NonValidEventStep", u"Select All", None))
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("NonValidEventStep", u"Event group search", None))
        self.reset_all_files_pushButton.setText(QCoreApplication.translate("NonValidEventStep", u"Reset all files", None))
        self.reset_excl_event_checkBox.setText(QCoreApplication.translate("NonValidEventStep", u"Reset the signal of excluded events ", None))
    # retranslateUi


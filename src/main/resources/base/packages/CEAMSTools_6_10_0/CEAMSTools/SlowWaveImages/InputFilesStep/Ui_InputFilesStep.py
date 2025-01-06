# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_InputFilesStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_InputFilesStep(object):
    def setupUi(self, InputFilesStep):
        if not InputFilesStep.objectName():
            InputFilesStep.setObjectName(u"InputFilesStep")
        InputFilesStep.resize(947, 595)
        InputFilesStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_4 = QVBoxLayout(InputFilesStep)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.splitter = QSplitter(InputFilesStep)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.files_listview = QListView(self.layoutWidget)
        self.files_listview.setObjectName(u"files_listview")
        self.files_listview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.files_listview.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.files_listview.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.verticalLayout.addWidget(self.files_listview)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.remove_entries_pushbutton = QPushButton(self.layoutWidget)
        self.remove_entries_pushbutton.setObjectName(u"remove_entries_pushbutton")

        self.horizontalLayout_3.addWidget(self.remove_entries_pushbutton)

        self.add_folders_pushbutton = QPushButton(self.layoutWidget)
        self.add_folders_pushbutton.setObjectName(u"add_folders_pushbutton")

        self.horizontalLayout_3.addWidget(self.add_folders_pushbutton)

        self.add_files_pushbutton = QPushButton(self.layoutWidget)
        self.add_files_pushbutton.setObjectName(u"add_files_pushbutton")

        self.horizontalLayout_3.addWidget(self.add_files_pushbutton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.scrollArea = QScrollArea(self.layoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 296, 234))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.events_treeView = QTreeView(self.scrollAreaWidgetContents)
        self.events_treeView.setObjectName(u"events_treeView")

        self.verticalLayout_5.addWidget(self.events_treeView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.splitter.addWidget(self.layoutWidget)
        self.frame_montages = QFrame(self.splitter)
        self.frame_montages.setObjectName(u"frame_montages")
        self.frame_montages.setEnabled(True)
        self.frame_montages.setFrameShape(QFrame.StyledPanel)
        self.frame_montages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_montages)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_montages)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_3.addWidget(self.label_3)

        self.montages_tableview = QTableView(self.frame_montages)
        self.montages_tableview.setObjectName(u"montages_tableview")
        self.montages_tableview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.montages_tableview.setSelectionMode(QAbstractItemView.MultiSelection)
        self.montages_tableview.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.montages_tableview.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.montages_tableview.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.montages_tableview)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.unselect_all_montage_pushbutton = QPushButton(self.frame_montages)
        self.unselect_all_montage_pushbutton.setObjectName(u"unselect_all_montage_pushbutton")

        self.horizontalLayout.addWidget(self.unselect_all_montage_pushbutton)

        self.select_all_montage_pushbutton = QPushButton(self.frame_montages)
        self.select_all_montage_pushbutton.setObjectName(u"select_all_montage_pushbutton")

        self.horizontalLayout.addWidget(self.select_all_montage_pushbutton)

        self.montage_search_lineedit = QLineEdit(self.frame_montages)
        self.montage_search_lineedit.setObjectName(u"montage_search_lineedit")

        self.horizontalLayout.addWidget(self.montage_search_lineedit)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.splitter.addWidget(self.frame_montages)
        self.frame_channels = QFrame(self.splitter)
        self.frame_channels.setObjectName(u"frame_channels")
        self.frame_channels.setFrameShape(QFrame.StyledPanel)
        self.frame_channels.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_channels)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.frame_channels)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_channels)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.import_pushButton = QPushButton(self.frame_channels)
        self.import_pushButton.setObjectName(u"import_pushButton")

        self.horizontalLayout_2.addWidget(self.import_pushButton)

        self.export_pushbutton = QPushButton(self.frame_channels)
        self.export_pushbutton.setObjectName(u"export_pushbutton")

        self.horizontalLayout_2.addWidget(self.export_pushbutton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.channels_tableview = QTableView(self.frame_channels)
        self.channels_tableview.setObjectName(u"channels_tableview")
        self.channels_tableview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.channels_tableview.setDragEnabled(False)
        self.channels_tableview.setDragDropOverwriteMode(False)
        self.channels_tableview.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.channels_tableview.setAlternatingRowColors(True)
        self.channels_tableview.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.channels_tableview.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.channels_tableview.setSortingEnabled(False)
        self.channels_tableview.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.channels_tableview)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.unselect_all_channels_pushbutton = QPushButton(self.frame_channels)
        self.unselect_all_channels_pushbutton.setObjectName(u"unselect_all_channels_pushbutton")

        self.horizontalLayout_4.addWidget(self.unselect_all_channels_pushbutton)

        self.select_all_channels_pushbutton = QPushButton(self.frame_channels)
        self.select_all_channels_pushbutton.setObjectName(u"select_all_channels_pushbutton")

        self.horizontalLayout_4.addWidget(self.select_all_channels_pushbutton)

        self.search_channels_lineedit = QLineEdit(self.frame_channels)
        self.search_channels_lineedit.setObjectName(u"search_channels_lineedit")

        self.horizontalLayout_4.addWidget(self.search_channels_lineedit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.splitter.addWidget(self.frame_channels)

        self.verticalLayout_4.addWidget(self.splitter)


        self.retranslateUi(InputFilesStep)
        self.add_files_pushbutton.clicked.connect(InputFilesStep.on_add_files)
        self.remove_entries_pushbutton.clicked.connect(InputFilesStep.on_remove_entries)
        self.add_folders_pushbutton.clicked.connect(InputFilesStep.on_add_folders)
        self.search_channels_lineedit.textChanged.connect(InputFilesStep.on_channel_search_changed)
        self.montage_search_lineedit.textChanged.connect(InputFilesStep.on_montage_seach_changed)
        self.select_all_channels_pushbutton.clicked.connect(InputFilesStep.on_channels_select_all)
        self.select_all_montage_pushbutton.clicked.connect(InputFilesStep.on_montages_select_all)
        self.unselect_all_channels_pushbutton.clicked.connect(InputFilesStep.on_channels_unselect_all)
        self.unselect_all_montage_pushbutton.clicked.connect(InputFilesStep.on_montages_unselect_all)
        self.files_listview.clicked.connect(InputFilesStep.on_file_selection_changed)
        self.export_pushbutton.clicked.connect(InputFilesStep.export_slot)
        self.import_pushButton.clicked.connect(InputFilesStep.import_slot)

        QMetaObject.connectSlotsByName(InputFilesStep)
    # setupUi

    def retranslateUi(self, InputFilesStep):
        InputFilesStep.setWindowTitle(QCoreApplication.translate("InputFilesStep", u"Form", None))
        self.label.setText(QCoreApplication.translate("InputFilesStep", u"PSG files", None))
        self.remove_entries_pushbutton.setText(QCoreApplication.translate("InputFilesStep", u"Remove", None))
        self.add_folders_pushbutton.setText(QCoreApplication.translate("InputFilesStep", u"Add from folders", None))
        self.add_files_pushbutton.setText(QCoreApplication.translate("InputFilesStep", u"Add files", None))
        self.label_4.setText(QCoreApplication.translate("InputFilesStep", u"Events details", None))
        self.label_3.setText(QCoreApplication.translate("InputFilesStep", u"Montages", None))
        self.unselect_all_montage_pushbutton.setText(QCoreApplication.translate("InputFilesStep", u"Unselect all", None))
        self.select_all_montage_pushbutton.setText(QCoreApplication.translate("InputFilesStep", u"Select all", None))
        self.montage_search_lineedit.setPlaceholderText(QCoreApplication.translate("InputFilesStep", u"Search Montages", None))
        self.label_2.setText(QCoreApplication.translate("InputFilesStep", u"Channels", None))
        self.import_pushButton.setText(QCoreApplication.translate("InputFilesStep", u"Import", None))
        self.export_pushbutton.setText(QCoreApplication.translate("InputFilesStep", u"Export", None))
        self.unselect_all_channels_pushbutton.setText(QCoreApplication.translate("InputFilesStep", u"Unselect all", None))
        self.select_all_channels_pushbutton.setText(QCoreApplication.translate("InputFilesStep", u"Select all", None))
        self.search_channels_lineedit.setInputMask("")
        self.search_channels_lineedit.setPlaceholderText(QCoreApplication.translate("InputFilesStep", u"Search Channels", None))
    # retranslateUi


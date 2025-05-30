# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file ''
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSplitter, QTableView, QTreeView, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_PSGReaderSettingsView(object):
    def setupUi(self, PSGReaderSettingsView):
        if not PSGReaderSettingsView.objectName():
            PSGReaderSettingsView.setObjectName(u"PSGReaderSettingsView")
        PSGReaderSettingsView.resize(1208, 778)
        PSGReaderSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_4 = QVBoxLayout(PSGReaderSettingsView)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.splitter = QSplitter(PSGReaderSettingsView)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_PSG = QLabel(self.layoutWidget)
        self.label_PSG.setObjectName(u"label_PSG")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_PSG.setFont(font)

        self.verticalLayout.addWidget(self.label_PSG)

        self.files_listview = QListView(self.layoutWidget)
        self.files_listview.setObjectName(u"files_listview")
        self.files_listview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.files_listview.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.files_listview.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.verticalLayout.addWidget(self.files_listview)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 385, 319))
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
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_Montages = QLabel(self.frame_montages)
        self.label_Montages.setObjectName(u"label_Montages")
        self.label_Montages.setFont(font)

        self.verticalLayout_3.addWidget(self.label_Montages)

        self.montages_tableview = QTableView(self.frame_montages)
        self.montages_tableview.setObjectName(u"montages_tableview")
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
        self.verticalLayout_2 = QVBoxLayout(self.frame_channels)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_Channels = QLabel(self.frame_channels)
        self.label_Channels.setObjectName(u"label_Channels")
        self.label_Channels.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_Channels)

        self.horizontalSpacer = QSpacerItem(13, 21, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.frame_channels)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_selection = QLabel(self.frame)
        self.label_selection.setObjectName(u"label_selection")

        self.horizontalLayout_2.addWidget(self.label_selection)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.import_pushbutton = QPushButton(self.frame)
        self.import_pushbutton.setObjectName(u"import_pushbutton")

        self.horizontalLayout_2.addWidget(self.import_pushbutton)

        self.export_pushbutton = QPushButton(self.frame)
        self.export_pushbutton.setObjectName(u"export_pushbutton")

        self.horizontalLayout_2.addWidget(self.export_pushbutton)


        self.horizontalLayout_5.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.channels_tableview = QTableView(self.frame_channels)
        self.channels_tableview.setObjectName(u"channels_tableview")
        self.channels_tableview.setEditTriggers(QAbstractItemView.SelectedClicked)
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

        self.splitter.addWidget(self.frame_channels)

        self.verticalLayout_4.addWidget(self.splitter)


        self.retranslateUi(PSGReaderSettingsView)
        self.add_files_pushbutton.clicked.connect(PSGReaderSettingsView.add_files_slot)
        self.remove_entries_pushbutton.clicked.connect(PSGReaderSettingsView.remove_entries_slot)
        self.add_folders_pushbutton.clicked.connect(PSGReaderSettingsView.add_folders_slot)
        self.search_channels_lineedit.textChanged.connect(PSGReaderSettingsView.channel_search_changed_slot)
        self.montage_search_lineedit.textChanged.connect(PSGReaderSettingsView.montage_seach_changed_slot)
        self.select_all_channels_pushbutton.clicked.connect(PSGReaderSettingsView.channels_select_all_slot)
        self.select_all_montage_pushbutton.clicked.connect(PSGReaderSettingsView.montages_select_all_slot)
        self.unselect_all_channels_pushbutton.clicked.connect(PSGReaderSettingsView.channels_unselect_all_slot)
        self.unselect_all_montage_pushbutton.clicked.connect(PSGReaderSettingsView.montages_unselect_all_slot)
        self.files_listview.clicked.connect(PSGReaderSettingsView.file_selection_changed_slot)
        self.export_pushbutton.clicked.connect(PSGReaderSettingsView.export_slot)
        self.import_pushbutton.clicked.connect(PSGReaderSettingsView.import_slot)

        QMetaObject.connectSlotsByName(PSGReaderSettingsView)
    # setupUi

    def retranslateUi(self, PSGReaderSettingsView):
        PSGReaderSettingsView.setWindowTitle(QCoreApplication.translate("PSGReaderSettingsView", u"Form", None))
        self.label_PSG.setText(QCoreApplication.translate("PSGReaderSettingsView", u"PSG files", None))
        self.remove_entries_pushbutton.setText(QCoreApplication.translate("PSGReaderSettingsView", u"Remove", None))
        self.add_folders_pushbutton.setText(QCoreApplication.translate("PSGReaderSettingsView", u"Add from folders", None))
        self.add_files_pushbutton.setText(QCoreApplication.translate("PSGReaderSettingsView", u"Add files", None))
        self.label_4.setText(QCoreApplication.translate("PSGReaderSettingsView", u"Events details", None))
        self.label_Montages.setText(QCoreApplication.translate("PSGReaderSettingsView", u"Montages", None))
        self.unselect_all_montage_pushbutton.setText(QCoreApplication.translate("PSGReaderSettingsView", u"Unselect all", None))
        self.select_all_montage_pushbutton.setText(QCoreApplication.translate("PSGReaderSettingsView", u"Select all", None))
        self.montage_search_lineedit.setPlaceholderText(QCoreApplication.translate("PSGReaderSettingsView", u"Search Montages", None))
        self.label_Channels.setText(QCoreApplication.translate("PSGReaderSettingsView", u"Channels", None))
        self.label_selection.setText(QCoreApplication.translate("PSGReaderSettingsView", u"Selections", None))
#if QT_CONFIG(tooltip)
        self.import_pushbutton.setToolTip(QCoreApplication.translate("PSGReaderSettingsView", u"Press to import a saved selection of files with their montage and channels.", None))
#endif // QT_CONFIG(tooltip)
        self.import_pushbutton.setText(QCoreApplication.translate("PSGReaderSettingsView", u"Import", None))
#if QT_CONFIG(tooltip)
        self.export_pushbutton.setToolTip(QCoreApplication.translate("PSGReaderSettingsView", u"Press to export and save the current selection of files with their montage and channels.", None))
#endif // QT_CONFIG(tooltip)
        self.export_pushbutton.setText(QCoreApplication.translate("PSGReaderSettingsView", u"Export", None))
        self.unselect_all_channels_pushbutton.setText(QCoreApplication.translate("PSGReaderSettingsView", u"Unselect all", None))
        self.select_all_channels_pushbutton.setText(QCoreApplication.translate("PSGReaderSettingsView", u"Select all", None))
        self.search_channels_lineedit.setInputMask("")
        self.search_channels_lineedit.setPlaceholderText(QCoreApplication.translate("PSGReaderSettingsView", u"Search Channels", None))
    # retranslateUi


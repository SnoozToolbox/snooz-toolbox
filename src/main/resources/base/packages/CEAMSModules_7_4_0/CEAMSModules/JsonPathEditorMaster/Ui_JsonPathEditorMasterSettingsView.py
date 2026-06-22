# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_JsonPathEditorMasterSettingsView.ui'
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
    QPushButton, QSizePolicy, QSplitter, QTableView,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_JsonPathEditorMasterSettingsView(object):
    def setupUi(self, JsonPathEditorMasterSettingsView):
        if not JsonPathEditorMasterSettingsView.objectName():
            JsonPathEditorMasterSettingsView.setObjectName(u"JsonPathEditorMasterSettingsView")
        JsonPathEditorMasterSettingsView.resize(941, 669)
        JsonPathEditorMasterSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout_8 = QHBoxLayout(JsonPathEditorMasterSettingsView)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Files_frame = QFrame(JsonPathEditorMasterSettingsView)
        self.Files_frame.setObjectName(u"Files_frame")
        self.Files_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.Files_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Files_frame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.Files_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Json_label = QLabel(self.Files_frame)
        self.Json_label.setObjectName(u"Json_label")

        self.verticalLayout_2.addWidget(self.Json_label)

        self.Files_listView = QListView(self.Files_frame)
        self.Files_listView.setObjectName(u"Files_listView")
        self.Files_listView.setFrameShape(QFrame.Shape.NoFrame)
        self.Files_listView.setLineWidth(0)
        self.Files_listView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Files_listView.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.Files_listView.setViewMode(QListView.ViewMode.ListMode)

        self.verticalLayout_2.addWidget(self.Files_listView)

        self.frame = QFrame(self.Files_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Remove_pushButton = QPushButton(self.frame)
        self.Remove_pushButton.setObjectName(u"Remove_pushButton")

        self.horizontalLayout_3.addWidget(self.Remove_pushButton)

        self.Add_from_folders_pushButton = QPushButton(self.frame)
        self.Add_from_folders_pushButton.setObjectName(u"Add_from_folders_pushButton")

        self.horizontalLayout_3.addWidget(self.Add_from_folders_pushButton)

        self.Add_files_pushButton = QPushButton(self.frame)
        self.Add_files_pushButton.setObjectName(u"Add_files_pushButton")

        self.horizontalLayout_3.addWidget(self.Add_files_pushButton)

        self.SelectAll_pushButton = QPushButton(self.frame)
        self.SelectAll_pushButton.setObjectName(u"SelectAll_pushButton")

        self.horizontalLayout_3.addWidget(self.SelectAll_pushButton)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_5 = QFrame(self.Files_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.New_Suffix = QLabel(self.frame_5)
        self.New_Suffix.setObjectName(u"New_Suffix")

        self.horizontalLayout_7.addWidget(self.New_Suffix)

        self.Suffix_lineEdit = QLineEdit(self.frame_5)
        self.Suffix_lineEdit.setObjectName(u"Suffix_lineEdit")

        self.horizontalLayout_7.addWidget(self.Suffix_lineEdit)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.Select_label = QLabel(self.Files_frame)
        self.Select_label.setObjectName(u"Select_label")
        self.Select_label.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.Select_label)

        self.frame_2 = QFrame(self.Files_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.New_files_lineEdit = QLineEdit(self.frame_2)
        self.New_files_lineEdit.setObjectName(u"New_files_lineEdit")

        self.horizontalLayout_4.addWidget(self.New_files_lineEdit)

        self.Choose_pushButton = QPushButton(self.frame_2)
        self.Choose_pushButton.setObjectName(u"Choose_pushButton")

        self.horizontalLayout_4.addWidget(self.Choose_pushButton)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.Files_frame)

        self.line = QFrame(JsonPathEditorMasterSettingsView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.label = QLabel(JsonPathEditorMasterSettingsView)
        self.label.setObjectName(u"label")
        self.label.setLineWidth(0)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter = QSplitter(JsonPathEditorMasterSettingsView)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFrameShape(QFrame.Shape.NoFrame)
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(15)
        self.splitter.setChildrenCollapsible(True)
        self.Paths_tableView = QTableView(self.splitter)
        self.Paths_tableView.setObjectName(u"Paths_tableView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Paths_tableView.sizePolicy().hasHeightForWidth())
        self.Paths_tableView.setSizePolicy(sizePolicy)
        self.Paths_tableView.setMaximumSize(QSize(16777215, 16777215))
        self.Paths_tableView.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Paths_tableView.setFrameShape(QFrame.Shape.NoFrame)
        self.splitter.addWidget(self.Paths_tableView)
        self.Paths_tableView.horizontalHeader().setDefaultSectionSize(200)
        self.Paths_tableView.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.Paths_tableView.horizontalHeader().setStretchLastSection(True)
        self.New_paths_tableView = QTableView(self.splitter)
        self.New_paths_tableView.setObjectName(u"New_paths_tableView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.New_paths_tableView.sizePolicy().hasHeightForWidth())
        self.New_paths_tableView.setSizePolicy(sizePolicy1)
        self.New_paths_tableView.setFrameShape(QFrame.Shape.NoFrame)
        self.New_paths_tableView.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.splitter.addWidget(self.New_paths_tableView)
        self.New_paths_tableView.horizontalHeader().setDefaultSectionSize(300)
        self.New_paths_tableView.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.splitter)


        self.horizontalLayout_8.addLayout(self.verticalLayout)


        self.retranslateUi(JsonPathEditorMasterSettingsView)

        QMetaObject.connectSlotsByName(JsonPathEditorMasterSettingsView)
    # setupUi

    def retranslateUi(self, JsonPathEditorMasterSettingsView):
        JsonPathEditorMasterSettingsView.setWindowTitle(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Form", None))
        self.Json_label.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Snooz Workspaces", None))
        self.Remove_pushButton.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Remove", None))
        self.Add_from_folders_pushButton.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Add from folders", None))
        self.Add_files_pushButton.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Add files", None))
        self.SelectAll_pushButton.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Select All", None))
        self.New_Suffix.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"<html><head/><body><p>New Snooz workspaces suffix:</p></body></html>", None))
        self.Select_label.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"<html><head/><body><p>Select a folder for new Snooz workspaces to save</p></body></html>", None))
        self.Choose_pushButton.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"Choose", None))
        self.label.setText(QCoreApplication.translate("JsonPathEditorMasterSettingsView", u"<html><head/><body><p>Edit paths inside Snooz workspaces</p></body></html>", None))
    # retranslateUi


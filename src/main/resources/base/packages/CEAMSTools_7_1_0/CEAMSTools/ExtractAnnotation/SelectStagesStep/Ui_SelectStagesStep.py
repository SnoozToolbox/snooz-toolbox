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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QPushButton, QSizePolicy, QTreeView, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_SelectStagesStep(object):
    def setupUi(self, SelectStagesStep):
        if not SelectStagesStep.objectName():
            SelectStagesStep.setObjectName(u"SelectStagesStep")
        SelectStagesStep.resize(837, 667)
        self.horizontalLayout_2 = QHBoxLayout(SelectStagesStep)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(SelectStagesStep)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.file_listview = QListView(SelectStagesStep)
        self.file_listview.setObjectName(u"file_listview")
        self.file_listview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.file_listview.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.file_listview.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.verticalLayout.addWidget(self.file_listview)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(SelectStagesStep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.event_treeview = QTreeView(SelectStagesStep)
        self.event_treeview.setObjectName(u"event_treeview")
        self.event_treeview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.event_treeview.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.event_treeview.setSelectionMode(QAbstractItemView.SingleSelection)
        self.event_treeview.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.verticalLayout_2.addWidget(self.event_treeview)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_all_checkBox = QCheckBox(SelectStagesStep)
        self.select_all_checkBox.setObjectName(u"select_all_checkBox")

        self.horizontalLayout.addWidget(self.select_all_checkBox)

        self.search_lineEdit = QLineEdit(SelectStagesStep)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        self.search_lineEdit.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.search_lineEdit)

        self.reset_all_files_pushButton = QPushButton(SelectStagesStep)
        self.reset_all_files_pushButton.setObjectName(u"reset_all_files_pushButton")

        self.horizontalLayout.addWidget(self.reset_all_files_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.reset_excl_event_checkBox = QCheckBox(SelectStagesStep)
        self.reset_excl_event_checkBox.setObjectName(u"reset_excl_event_checkBox")

        self.verticalLayout_2.addWidget(self.reset_excl_event_checkBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.retranslateUi(SelectStagesStep)
        self.file_listview.clicked.connect(SelectStagesStep.on_file_selected)
        self.select_all_checkBox.stateChanged.connect(SelectStagesStep.on_select_all_groups)
        self.reset_all_files_pushButton.clicked.connect(SelectStagesStep.on_reset_all_files)
        self.search_lineEdit.textEdited.connect(SelectStagesStep.search_pattern_slot)

        QMetaObject.connectSlotsByName(SelectStagesStep)
    # setupUi

    def retranslateUi(self, SelectStagesStep):
        SelectStagesStep.setWindowTitle(QCoreApplication.translate("SelectStagesStep", u"Form", None))
        SelectStagesStep.setStyleSheet(QCoreApplication.translate("SelectStagesStep", u"font: 12pt \"Roboto\";", None))
        self.label.setText(QCoreApplication.translate("SelectStagesStep", u"PSG Files", None))
        self.label_2.setText(QCoreApplication.translate("SelectStagesStep", u"Events", None))
        self.select_all_checkBox.setText(QCoreApplication.translate("SelectStagesStep", u"Select All", None))
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("SelectStagesStep", u"Event group search", None))
        self.reset_all_files_pushButton.setText(QCoreApplication.translate("SelectStagesStep", u"Reset all files", None))
        self.reset_excl_event_checkBox.setText(QCoreApplication.translate("SelectStagesStep", u"Reset the signal of excluded events ", None))
    # retranslateUi


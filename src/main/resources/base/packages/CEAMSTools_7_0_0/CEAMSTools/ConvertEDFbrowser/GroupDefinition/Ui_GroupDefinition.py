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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QListView, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import themes_rc

class Ui_GroupDefinition(object):
    def setupUi(self, GroupDefinition):
        if not GroupDefinition.objectName():
            GroupDefinition.setObjectName(u"GroupDefinition")
        GroupDefinition.resize(1204, 469)
        self.horizontalLayout_2 = QHBoxLayout(GroupDefinition)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(GroupDefinition)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.file_listview = QListView(GroupDefinition)
        self.file_listview.setObjectName(u"file_listview")

        self.verticalLayout.addWidget(self.file_listview)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(GroupDefinition)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.event_treeview = QTableView(GroupDefinition)
        self.event_treeview.setObjectName(u"event_treeview")
        self.event_treeview.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.event_treeview.setSelectionMode(QAbstractItemView.NoSelection)
        self.event_treeview.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.verticalLayout_2.addWidget(self.event_treeview)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.apply_all_pushButton = QPushButton(GroupDefinition)
        self.apply_all_pushButton.setObjectName(u"apply_all_pushButton")

        self.horizontalLayout.addWidget(self.apply_all_pushButton)

        self.reset_all_files_pushButton = QPushButton(GroupDefinition)
        self.reset_all_files_pushButton.setObjectName(u"reset_all_files_pushButton")

        self.horizontalLayout.addWidget(self.reset_all_files_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.retranslateUi(GroupDefinition)
        self.file_listview.clicked.connect(GroupDefinition.on_file_selected)
        self.apply_all_pushButton.clicked.connect(GroupDefinition.on_apply_to_all_files)
        self.reset_all_files_pushButton.clicked.connect(GroupDefinition.on_reset_all_files)

        QMetaObject.connectSlotsByName(GroupDefinition)
    # setupUi

    def retranslateUi(self, GroupDefinition):
        GroupDefinition.setWindowTitle(QCoreApplication.translate("GroupDefinition", u"Form", None))
        GroupDefinition.setStyleSheet(QCoreApplication.translate("GroupDefinition", u"font: 12pt \"Roboto\";", None))
        self.label.setText(QCoreApplication.translate("GroupDefinition", u"PSG Files", None))
        self.label_2.setText(QCoreApplication.translate("GroupDefinition", u"Events", None))
        self.apply_all_pushButton.setText(QCoreApplication.translate("GroupDefinition", u"Apply to all files", None))
        self.reset_all_files_pushButton.setText(QCoreApplication.translate("GroupDefinition", u"Reset all files", None))
    # retranslateUi


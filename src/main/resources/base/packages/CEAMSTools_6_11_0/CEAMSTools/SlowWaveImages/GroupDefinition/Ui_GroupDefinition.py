# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_GroupDefinition.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_GroupDefinition(object):
    def setupUi(self, GroupDefinition):
        if not GroupDefinition.objectName():
            GroupDefinition.setObjectName(u"GroupDefinition")
        GroupDefinition.resize(783, 574)
        GroupDefinition.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout = QHBoxLayout(GroupDefinition)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(GroupDefinition)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.tableView_group = QTableView(GroupDefinition)
        self.tableView_group.setObjectName(u"tableView_group")
        self.tableView_group.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tableView_group.setToolTipDuration(-1)
        self.tableView_group.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView_group.setTextElideMode(Qt.ElideNone)
        self.tableView_group.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableView_group.horizontalHeader().setStretchLastSection(True)
        self.tableView_group.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableView_group)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_apply = QPushButton(GroupDefinition)
        self.pushButton_apply.setObjectName(u"pushButton_apply")

        self.gridLayout.addWidget(self.pushButton_apply, 1, 2, 1, 1)

        self.checkBox_SelectAll = QCheckBox(GroupDefinition)
        self.checkBox_SelectAll.setObjectName(u"checkBox_SelectAll")
        self.checkBox_SelectAll.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.checkBox_SelectAll, 0, 2, 1, 1)

        self.lineEdit_group = QLineEdit(GroupDefinition)
        self.lineEdit_group.setObjectName(u"lineEdit_group")

        self.gridLayout.addWidget(self.lineEdit_group, 1, 1, 1, 1)

        self.lineEdit_search = QLineEdit(GroupDefinition)
        self.lineEdit_search.setObjectName(u"lineEdit_search")

        self.gridLayout.addWidget(self.lineEdit_search, 0, 1, 1, 1)

        self.label_2 = QLabel(GroupDefinition)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 0))

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(GroupDefinition)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(260, 0))

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(GroupDefinition)
        self.pushButton_apply.clicked.connect(GroupDefinition.apply_group_slot)
        self.checkBox_SelectAll.clicked.connect(GroupDefinition.select_all_slot)
        self.lineEdit_search.textEdited.connect(GroupDefinition.edit_search_slot)

        QMetaObject.connectSlotsByName(GroupDefinition)
    # setupUi

    def retranslateUi(self, GroupDefinition):
        GroupDefinition.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("GroupDefinition", u"<html><head/><body><p><span style=\" font-weight:600;\">PSG files - Group </span></p></body></html>", None))
        self.pushButton_apply.setText(QCoreApplication.translate("GroupDefinition", u"Apply all selected", None))
        self.checkBox_SelectAll.setText(QCoreApplication.translate("GroupDefinition", u"Select/Unselect all", None))
        self.lineEdit_group.setPlaceholderText(QCoreApplication.translate("GroupDefinition", u"Define the group label", None))
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("GroupDefinition", u"Search PSG file", None))
        self.label_2.setText(QCoreApplication.translate("GroupDefinition", u"Pattern to filter the PSG files list", None))
        self.label_3.setText(QCoreApplication.translate("GroupDefinition", u"Group label to apply to the PSG files selected", None))
    # retranslateUi


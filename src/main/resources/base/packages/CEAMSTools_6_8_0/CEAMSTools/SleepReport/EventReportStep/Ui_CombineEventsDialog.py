# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_CombineEventsDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_CombineEventsDialog(object):
    def setupUi(self, CombineEventsDialog):
        if not CombineEventsDialog.objectName():
            CombineEventsDialog.setObjectName(u"CombineEventsDialog")
        CombineEventsDialog.resize(400, 565)
        self.verticalLayout = QVBoxLayout(CombineEventsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(CombineEventsDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.events_treewidget = QTreeWidget(CombineEventsDialog)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(1, u"2");
        __qtreewidgetitem.setText(0, u"1");
        self.events_treewidget.setHeaderItem(__qtreewidgetitem)
        self.events_treewidget.setObjectName(u"events_treewidget")
        self.events_treewidget.setColumnCount(2)

        self.verticalLayout.addWidget(self.events_treewidget)

        self.label_2 = QLabel(CombineEventsDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.new_group_lineedit = QLineEdit(CombineEventsDialog)
        self.new_group_lineedit.setObjectName(u"new_group_lineedit")

        self.verticalLayout.addWidget(self.new_group_lineedit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel_pushbutton = QPushButton(CombineEventsDialog)
        self.cancel_pushbutton.setObjectName(u"cancel_pushbutton")

        self.horizontalLayout.addWidget(self.cancel_pushbutton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.add_to_all_pushbutton = QPushButton(CombineEventsDialog)
        self.add_to_all_pushbutton.setObjectName(u"add_to_all_pushbutton")

        self.horizontalLayout.addWidget(self.add_to_all_pushbutton)

        self.add_pushbutton = QPushButton(CombineEventsDialog)
        self.add_pushbutton.setObjectName(u"add_pushbutton")

        self.horizontalLayout.addWidget(self.add_pushbutton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(CombineEventsDialog)
        self.add_pushbutton.clicked.connect(CombineEventsDialog.on_add)
        self.cancel_pushbutton.clicked.connect(CombineEventsDialog.on_cancel)
        self.events_treewidget.itemClicked.connect(CombineEventsDialog.on_item_checked)
        self.add_to_all_pushbutton.clicked.connect(CombineEventsDialog.on_add_to_all)

        QMetaObject.connectSlotsByName(CombineEventsDialog)
    # setupUi

    def retranslateUi(self, CombineEventsDialog):
        CombineEventsDialog.setWindowTitle(QCoreApplication.translate("CombineEventsDialog", u"Dialog", None))
        CombineEventsDialog.setStyleSheet(QCoreApplication.translate("CombineEventsDialog", u"font: 12pt \"Roboto\";", None))
        self.label.setText(QCoreApplication.translate("CombineEventsDialog", u"Select events to combine", None))
        self.label_2.setText(QCoreApplication.translate("CombineEventsDialog", u"New group name:", None))
        self.cancel_pushbutton.setText(QCoreApplication.translate("CombineEventsDialog", u"Cancel", None))
        self.add_to_all_pushbutton.setText(QCoreApplication.translate("CombineEventsDialog", u"Add to all files", None))
        self.add_pushbutton.setText(QCoreApplication.translate("CombineEventsDialog", u"Add", None))
    # retranslateUi


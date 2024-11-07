# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ProcessView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ProcessUI.ModulesTreeWidget import ModulesTreeWidget


class Ui_ProcessView(object):
    def setupUi(self, ProcessView):
        if not ProcessView.objectName():
            ProcessView.setObjectName(u"ProcessView")
        ProcessView.setWindowModality(Qt.NonModal)
        ProcessView.resize(933, 800)
        self.horizontalLayout = QHBoxLayout(ProcessView)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(7, 7, 7, 7)
        self.splitter = QSplitter(ProcessView)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.process_view_verticalLayout = QVBoxLayout(self.layoutWidget)
        self.process_view_verticalLayout.setObjectName(u"process_view_verticalLayout")
        self.process_view_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter.addWidget(self.layoutWidget)
        self.dockWidget = QDockWidget(self.splitter)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setWindowTitle(u"")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.dockWidgetContents)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.library_options_pushButton = QPushButton(self.dockWidgetContents)
        self.library_options_pushButton.setObjectName(u"library_options_pushButton")

        self.horizontalLayout_2.addWidget(self.library_options_pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.module_treeWidget = ModulesTreeWidget(self.dockWidgetContents)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Name");
        self.module_treeWidget.setHeaderItem(__qtreewidgetitem)
        self.module_treeWidget.setObjectName(u"module_treeWidget")

        self.verticalLayout_3.addWidget(self.module_treeWidget)

        self.dockWidget.setWidget(self.dockWidgetContents)
        self.splitter.addWidget(self.dockWidget)

        self.horizontalLayout.addWidget(self.splitter)


        self.retranslateUi(ProcessView)
        self.library_options_pushButton.clicked.connect(ProcessView.library_options_clicked)

        QMetaObject.connectSlotsByName(ProcessView)
    # setupUi

    def retranslateUi(self, ProcessView):
        ProcessView.setWindowTitle(QCoreApplication.translate("ProcessView", u"ProcessView", None))
        self.label.setText(QCoreApplication.translate("ProcessView", u"Module Library", None))
        self.library_options_pushButton.setText(QCoreApplication.translate("ProcessView", u"Options", None))
        ___qtreewidgetitem = self.module_treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("ProcessView", u"Version", None));
    # retranslateUi


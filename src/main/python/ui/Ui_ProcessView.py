# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ProcessView.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QTreeWidgetItem, QVBoxLayout, QWidget)

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
        self.rightPanel = QWidget(self.splitter)
        self.rightPanel.setObjectName(u"rightPanel")
        self.verticalLayout_3 = QVBoxLayout(self.rightPanel)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.rightPanel)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.library_options_pushButton = QPushButton(self.rightPanel)
        self.library_options_pushButton.setObjectName(u"library_options_pushButton")

        self.horizontalLayout_2.addWidget(self.library_options_pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.module_treeWidget = ModulesTreeWidget(self.rightPanel)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Name");
        self.module_treeWidget.setHeaderItem(__qtreewidgetitem)
        self.module_treeWidget.setObjectName(u"module_treeWidget")

        self.verticalLayout_3.addWidget(self.module_treeWidget)

        self.splitter.addWidget(self.rightPanel)

        self.horizontalLayout.addWidget(self.splitter)


        self.retranslateUi(ProcessView)
        self.library_options_pushButton.clicked["bool"].connect(ProcessView.library_options_clicked)

        QMetaObject.connectSlotsByName(ProcessView)
    # setupUi

    def retranslateUi(self, ProcessView):
        ProcessView.setWindowTitle(QCoreApplication.translate("ProcessView", u"ProcessView", None))
        self.label.setText(QCoreApplication.translate("ProcessView", u"Module Library", None))
        self.library_options_pushButton.setText(QCoreApplication.translate("ProcessView", u"Options", None))
        ___qtreewidgetitem = self.module_treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("ProcessView", u"Version", None));
    # retranslateUi


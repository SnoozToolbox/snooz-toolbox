# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_StepsWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_StepsWidget(object):
    def setupUi(self, StepsWidget):
        if not StepsWidget.objectName():
            StepsWidget.setObjectName(u"StepsWidget")
        StepsWidget.resize(986, 671)
        StepsWidget.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_2 = QVBoxLayout(StepsWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(StepsWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.steps_toolbox = QToolBox(self.layoutWidget)
        self.steps_toolbox.setObjectName(u"steps_toolbox")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.steps_toolbox.sizePolicy().hasHeightForWidth())
        self.steps_toolbox.setSizePolicy(sizePolicy)
        self.steps_toolbox.setMinimumSize(QSize(200, 0))
        self.steps_toolbox.setMaximumSize(QSize(16777215, 16777215))
        self.steps_toolbox.setStyleSheet(u"")
        self.steps_toolbox.setLineWidth(1)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setGeometry(QRect(0, 0, 353, 491))
        self.widget.setMinimumSize(QSize(353, 0))
        self.widget.setAutoFillBackground(True)
        self.widget.setStyleSheet(u"")
        self.steps_toolbox.addItem(self.widget, u"")

        self.verticalLayout_4.addWidget(self.steps_toolbox)

        self.save_pushButton = QPushButton(self.layoutWidget)
        self.save_pushButton.setObjectName(u"save_pushButton")
        self.save_pushButton.setMaximumSize(QSize(16777215, 50))
        self.save_pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.save_pushButton)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.run_pushbutton = QPushButton(self.layoutWidget)
        self.run_pushbutton.setObjectName(u"run_pushbutton")
        self.run_pushbutton.setMinimumSize(QSize(0, 50))
        self.run_pushbutton.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.run_pushbutton.setFont(font)
        self.run_pushbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.run_pushbutton.setStyleSheet(u"")
        self.run_pushbutton.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.run_pushbutton)

        self.horizontalLayout_4.setStretch(0, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.steps_tabwidget = QTabWidget(self.layoutWidget1)
        self.steps_tabwidget.setObjectName(u"steps_tabwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.steps_tabwidget.sizePolicy().hasHeightForWidth())
        self.steps_tabwidget.setSizePolicy(sizePolicy1)
        self.steps_tabwidget.setStyleSheet(u"")
        self.empty_tab = QWidget()
        self.empty_tab.setObjectName(u"empty_tab")
        self.verticalLayout_3 = QVBoxLayout(self.empty_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.steps_tabwidget.addTab(self.empty_tab, "")

        self.verticalLayout.addWidget(self.steps_tabwidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.feedback_pushButton = QPushButton(self.layoutWidget1)
        self.feedback_pushButton.setObjectName(u"feedback_pushButton")

        self.horizontalLayout.addWidget(self.feedback_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.previous_pushbutton = QPushButton(self.layoutWidget1)
        self.previous_pushbutton.setObjectName(u"previous_pushbutton")
        self.previous_pushbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.previous_pushbutton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.previous_pushbutton)

        self.next_pushbutton = QPushButton(self.layoutWidget1)
        self.next_pushbutton.setObjectName(u"next_pushbutton")
        self.next_pushbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.next_pushbutton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.next_pushbutton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_2.addWidget(self.splitter)


        self.retranslateUi(StepsWidget)
        self.next_pushbutton.clicked.connect(StepsWidget.on_next)
        self.previous_pushbutton.clicked.connect(StepsWidget.on_previous)
        self.run_pushbutton.clicked.connect(StepsWidget.run_clicked)
        self.feedback_pushButton.clicked.connect(StepsWidget.feedback_pressed)
        self.save_pushButton.clicked.connect(StepsWidget.save_clicked)

        self.steps_toolbox.setCurrentIndex(0)
        self.steps_toolbox.layout().setSpacing(7)


        QMetaObject.connectSlotsByName(StepsWidget)
    # setupUi

    def retranslateUi(self, StepsWidget):
        StepsWidget.setWindowTitle(QCoreApplication.translate("StepsWidget", u"StepsWidget", None))
#if QT_CONFIG(accessibility)
        StepsWidget.setAccessibleName(QCoreApplication.translate("StepsWidget", u"step_widget_main", None))
#endif // QT_CONFIG(accessibility)
        self.steps_toolbox.setItemText(self.steps_toolbox.indexOf(self.widget), "")
#if QT_CONFIG(accessibility)
        self.save_pushButton.setAccessibleName(QCoreApplication.translate("StepsWidget", u"save_pushbutton", None))
#endif // QT_CONFIG(accessibility)
        self.save_pushButton.setText(QCoreApplication.translate("StepsWidget", u"Save Workspace", None))
#if QT_CONFIG(shortcut)
        self.save_pushButton.setShortcut(QCoreApplication.translate("StepsWidget", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.run_pushbutton.setToolTip(QCoreApplication.translate("StepsWidget", u"Run", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.run_pushbutton.setAccessibleName(QCoreApplication.translate("StepsWidget", u"run_pushbutton", None))
#endif // QT_CONFIG(accessibility)
        self.run_pushbutton.setText(QCoreApplication.translate("StepsWidget", u"> Run", None))
#if QT_CONFIG(accessibility)
        self.steps_tabwidget.setAccessibleName(QCoreApplication.translate("StepsWidget", u"steps_tabwidget", None))
#endif // QT_CONFIG(accessibility)
        self.steps_tabwidget.setTabText(self.steps_tabwidget.indexOf(self.empty_tab), "")
#if QT_CONFIG(accessibility)
        self.feedback_pushButton.setAccessibleName(QCoreApplication.translate("StepsWidget", u"feedback_pushbutton", None))
#endif // QT_CONFIG(accessibility)
        self.feedback_pushButton.setText(QCoreApplication.translate("StepsWidget", u"Give us your feedback!", None))
#if QT_CONFIG(accessibility)
        self.previous_pushbutton.setAccessibleName(QCoreApplication.translate("StepsWidget", u"previous_pushbutton", None))
#endif // QT_CONFIG(accessibility)
        self.previous_pushbutton.setText(QCoreApplication.translate("StepsWidget", u"\u25c0 Previous", None))
#if QT_CONFIG(accessibility)
        self.next_pushbutton.setAccessibleName(QCoreApplication.translate("StepsWidget", u"next_pushbutton", None))
#endif // QT_CONFIG(accessibility)
        self.next_pushbutton.setText(QCoreApplication.translate("StepsWidget", u"Next \u25b6", None))
    # retranslateUi


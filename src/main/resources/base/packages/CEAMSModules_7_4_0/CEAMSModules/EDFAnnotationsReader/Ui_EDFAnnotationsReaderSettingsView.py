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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_EDFAnnotationsReaderSettingsView(object):
    def setupUi(self, EDFAnnotationsReaderSettingsView):
        if not EDFAnnotationsReaderSettingsView.objectName():
            EDFAnnotationsReaderSettingsView.setObjectName(u"EDFAnnotationsReaderSettingsView")
        EDFAnnotationsReaderSettingsView.resize(607, 420)
        self.verticalLayout_4 = QVBoxLayout(EDFAnnotationsReaderSettingsView)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(EDFAnnotationsReaderSettingsView)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(30)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_files = QTableWidget(self.layoutWidget)
        self.tableWidget_files.setObjectName(u"tableWidget_files")
        self.tableWidget_files.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_files.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_files.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_files.setAutoScroll(True)
        self.tableWidget_files.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_files.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_files.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_files.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget_files.setWordWrap(True)

        self.verticalLayout.addWidget(self.tableWidget_files)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_choose = QPushButton(self.layoutWidget)
        self.pushButton_choose.setObjectName(u"pushButton_choose")
        self.pushButton_choose.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_choose)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_psg_files = QTableWidget(self.layoutWidget1)
        self.tableWidget_psg_files.setObjectName(u"tableWidget_psg_files")
        self.tableWidget_psg_files.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_2.addWidget(self.tableWidget_psg_files)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.pushButton_choose_psg = QPushButton(self.layoutWidget1)
        self.pushButton_choose_psg.setObjectName(u"pushButton_choose_psg")

        self.horizontalLayout_2.addWidget(self.pushButton_choose_psg)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_3.addWidget(self.splitter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.pushButton_clear = QPushButton(EDFAnnotationsReaderSettingsView)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMinimumSize(QSize(100, 0))
        self.pushButton_clear.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_clear)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.retranslateUi(EDFAnnotationsReaderSettingsView)
        self.pushButton_choose.clicked.connect(EDFAnnotationsReaderSettingsView.choose_slot)
        self.pushButton_clear.clicked.connect(EDFAnnotationsReaderSettingsView.clear_slot)
        self.pushButton_choose_psg.clicked.connect(EDFAnnotationsReaderSettingsView.choose_psg_slot)

        QMetaObject.connectSlotsByName(EDFAnnotationsReaderSettingsView)
    # setupUi

    def retranslateUi(self, EDFAnnotationsReaderSettingsView):
        EDFAnnotationsReaderSettingsView.setWindowTitle("")
        EDFAnnotationsReaderSettingsView.setStyleSheet(QCoreApplication.translate("EDFAnnotationsReaderSettingsView", u"font: 12pt \"Roboto\";", None))
        self.pushButton_choose.setText(QCoreApplication.translate("EDFAnnotationsReaderSettingsView", u"Choose Annotations files", None))
        self.pushButton_choose_psg.setText(QCoreApplication.translate("EDFAnnotationsReaderSettingsView", u"Choose PSG files", None))
        self.pushButton_clear.setText(QCoreApplication.translate("EDFAnnotationsReaderSettingsView", u"Clear All", None))
    # retranslateUi


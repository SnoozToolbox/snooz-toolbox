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
    QSplitter, QTreeView, QVBoxLayout, QWidget)
import themes_rc

class Ui_EditorStep(object):
    def setupUi(self, EditorStep):
        if not EditorStep.objectName():
            EditorStep.setObjectName(u"EditorStep")
        EditorStep.resize(831, 576)
        EditorStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_4 = QVBoxLayout(EditorStep)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.splitter_2 = QSplitter(EditorStep)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.file_listview = QListView(self.layoutWidget)
        self.file_listview.setObjectName(u"file_listview")
        self.file_listview.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout.addWidget(self.file_listview)

        self.splitter_2.addWidget(self.layoutWidget)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.treeView_subject = QTreeView(self.layoutWidget1)
        self.treeView_subject.setObjectName(u"treeView_subject")
        self.treeView_subject.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.treeView_subject.setSelectionMode(QAbstractItemView.NoSelection)
        self.treeView_subject.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.verticalLayout_2.addWidget(self.treeView_subject)

        self.splitter.addWidget(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_3.addWidget(self.label_3)

        self.treeView_cohort = QTreeView(self.layoutWidget2)
        self.treeView_cohort.setObjectName(u"treeView_cohort")

        self.verticalLayout_3.addWidget(self.treeView_cohort)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_refresh = QPushButton(self.layoutWidget2)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")

        self.horizontalLayout.addWidget(self.pushButton_refresh)

        self.reset_all_files_pushButton = QPushButton(self.layoutWidget2)
        self.reset_all_files_pushButton.setObjectName(u"reset_all_files_pushButton")

        self.horizontalLayout.addWidget(self.reset_all_files_pushButton)

        self.pushButton_export = QPushButton(self.layoutWidget2)
        self.pushButton_export.setObjectName(u"pushButton_export")

        self.horizontalLayout.addWidget(self.pushButton_export)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.layoutWidget2)
        self.splitter_2.addWidget(self.splitter)

        self.verticalLayout_4.addWidget(self.splitter_2)


        self.retranslateUi(EditorStep)
        self.file_listview.clicked.connect(EditorStep.on_file_selected)
        self.reset_all_files_pushButton.clicked.connect(EditorStep.on_reset_all_files)
        self.pushButton_refresh.clicked.connect(EditorStep.refresh_view_slot)
        self.pushButton_export.clicked.connect(EditorStep.export_modifications_slot)

        QMetaObject.connectSlotsByName(EditorStep)
    # setupUi

    def retranslateUi(self, EditorStep):
        EditorStep.setWindowTitle(QCoreApplication.translate("EditorStep", u"Form", None))
        self.label.setText(QCoreApplication.translate("EditorStep", u"PSG Files", None))
        self.label_2.setText(QCoreApplication.translate("EditorStep", u"Events from selection", None))
        self.label_3.setText(QCoreApplication.translate("EditorStep", u"Events from cohort", None))
#if QT_CONFIG(tooltip)
        self.pushButton_refresh.setToolTip(QCoreApplication.translate("EditorStep", u"To refresh the cohort view. Useful for merging 2 groups with the same labels.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_refresh.setText(QCoreApplication.translate("EditorStep", u"Refresh", None))
#if QT_CONFIG(tooltip)
        self.reset_all_files_pushButton.setToolTip(QCoreApplication.translate("EditorStep", u"To return to the original labels saved in the file.", None))
#endif // QT_CONFIG(tooltip)
        self.reset_all_files_pushButton.setText(QCoreApplication.translate("EditorStep", u"Back to original labels", None))
#if QT_CONFIG(tooltip)
        self.pushButton_export.setToolTip(QCoreApplication.translate("EditorStep", u"To display all changes that will be performed at runtime.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_export.setText(QCoreApplication.translate("EditorStep", u"Export", None))
    # retranslateUi


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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QTableView, QVBoxLayout, QWidget)
import themes_rc

class Ui_TemporalLinkStep(object):
    def setupUi(self, TemporalLinkStep):
        if not TemporalLinkStep.objectName():
            TemporalLinkStep.setObjectName(u"TemporalLinkStep")
        TemporalLinkStep.resize(730, 590)
        self.verticalLayout_4 = QVBoxLayout(TemporalLinkStep)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.splitter = QSplitter(TemporalLinkStep)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.file_tableview = QTableView(self.verticalLayoutWidget)
        self.file_tableview.setObjectName(u"file_tableview")
        self.file_tableview.setAlternatingRowColors(True)
        self.file_tableview.setSelectionMode(QAbstractItemView.SingleSelection)
        self.file_tableview.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.file_tableview.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.file_tableview)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.clear_all_reports_pushbutton = QPushButton(self.verticalLayoutWidget)
        self.clear_all_reports_pushbutton.setObjectName(u"clear_all_reports_pushbutton")

        self.horizontalLayout_2.addWidget(self.clear_all_reports_pushbutton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.analysis_window_lineedit = QLineEdit(self.layoutWidget)
        self.analysis_window_lineedit.setObjectName(u"analysis_window_lineedit")

        self.horizontalLayout.addWidget(self.analysis_window_lineedit)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.temporal_links_tableview = QTableView(self.layoutWidget)
        self.temporal_links_tableview.setObjectName(u"temporal_links_tableview")
        self.temporal_links_tableview.setAlternatingRowColors(True)
        self.temporal_links_tableview.setWordWrap(False)
        self.temporal_links_tableview.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.temporal_links_tableview)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.apply_to_all_pushbutton = QPushButton(self.layoutWidget)
        self.apply_to_all_pushbutton.setObjectName(u"apply_to_all_pushbutton")

        self.horizontalLayout_3.addWidget(self.apply_to_all_pushbutton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.csv_reports_checkbox = QCheckBox(self.groupBox)
        self.csv_reports_checkbox.setObjectName(u"csv_reports_checkbox")
        self.csv_reports_checkbox.setChecked(True)

        self.horizontalLayout_4.addWidget(self.csv_reports_checkbox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.groupBox)

        self.splitter.addWidget(self.layoutWidget)

        self.verticalLayout_4.addWidget(self.splitter)


        self.retranslateUi(TemporalLinkStep)
        self.apply_to_all_pushbutton.clicked.connect(TemporalLinkStep.on_apply_to_all)
        self.file_tableview.clicked.connect(TemporalLinkStep.on_file_selection_change)
        self.clear_all_reports_pushbutton.clicked.connect(TemporalLinkStep.clear_all_reports)

        QMetaObject.connectSlotsByName(TemporalLinkStep)
    # setupUi

    def retranslateUi(self, TemporalLinkStep):
        TemporalLinkStep.setWindowTitle("")
        TemporalLinkStep.setStyleSheet(QCoreApplication.translate("TemporalLinkStep", u"font: 12pt \"Roboto\";", None))
        self.clear_all_reports_pushbutton.setText(QCoreApplication.translate("TemporalLinkStep", u"Clear all reports", None))
        self.label.setText(QCoreApplication.translate("TemporalLinkStep", u"Analysis window size:", None))
        self.label_2.setText(QCoreApplication.translate("TemporalLinkStep", u"seconds", None))
        self.label_3.setText(QCoreApplication.translate("TemporalLinkStep", u"Choose which report to generate", None))
#if QT_CONFIG(tooltip)
        self.apply_to_all_pushbutton.setToolTip(QCoreApplication.translate("TemporalLinkStep", u"Reset all previous selections and apply this one to all files.", None))
#endif // QT_CONFIG(tooltip)
        self.apply_to_all_pushbutton.setText(QCoreApplication.translate("TemporalLinkStep", u"Apply to all files", None))
        self.groupBox.setTitle(QCoreApplication.translate("TemporalLinkStep", u"Output format", None))
#if QT_CONFIG(tooltip)
        self.csv_reports_checkbox.setToolTip(QCoreApplication.translate("TemporalLinkStep", u"tsv reports are generated by default (values are easily exportable).", None))
#endif // QT_CONFIG(tooltip)
        self.csv_reports_checkbox.setText(QCoreApplication.translate("TemporalLinkStep", u"tsv reports", None))
    # retranslateUi


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
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import themes_rc

class Ui_GenerateReportStep(object):
    def setupUi(self, GenerateReportStep):
        if not GenerateReportStep.objectName():
            GenerateReportStep.setObjectName(u"GenerateReportStep")
        GenerateReportStep.resize(731, 590)
        self.verticalLayout = QVBoxLayout(GenerateReportStep)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(GenerateReportStep)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.csv_report_checkbox = QCheckBox(GenerateReportStep)
        self.csv_report_checkbox.setObjectName(u"csv_report_checkbox")

        self.verticalLayout.addWidget(self.csv_report_checkbox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(GenerateReportStep)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.output_lineedit = QLineEdit(GenerateReportStep)
        self.output_lineedit.setObjectName(u"output_lineedit")

        self.horizontalLayout.addWidget(self.output_lineedit)

        self.choose_pushbutton = QPushButton(GenerateReportStep)
        self.choose_pushbutton.setObjectName(u"choose_pushbutton")

        self.horizontalLayout.addWidget(self.choose_pushbutton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(GenerateReportStep)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.prefix_lineedit = QLineEdit(GenerateReportStep)
        self.prefix_lineedit.setObjectName(u"prefix_lineedit")

        self.horizontalLayout_2.addWidget(self.prefix_lineedit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_2 = QLabel(GenerateReportStep)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.event_report_listwidget = QListWidget(GenerateReportStep)
        self.event_report_listwidget.setObjectName(u"event_report_listwidget")
        self.event_report_listwidget.setEditTriggers(QAbstractItemView.CurrentChanged|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.event_report_listwidget.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.event_report_listwidget)

        self.label_4 = QLabel(GenerateReportStep)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.temporallinks_listwidget = QListWidget(GenerateReportStep)
        self.temporallinks_listwidget.setObjectName(u"temporallinks_listwidget")
        self.temporallinks_listwidget.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.temporallinks_listwidget)


        self.retranslateUi(GenerateReportStep)
        self.choose_pushbutton.clicked.connect(GenerateReportStep.on_choose)

        QMetaObject.connectSlotsByName(GenerateReportStep)
    # setupUi

    def retranslateUi(self, GenerateReportStep):
        GenerateReportStep.setWindowTitle("")
        GenerateReportStep.setStyleSheet(QCoreApplication.translate("GenerateReportStep", u"font: 12pt \"Roboto\";", None))
        self.label_5.setText(QCoreApplication.translate("GenerateReportStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep Report</span></p></body></html>", None))
        self.csv_report_checkbox.setText(QCoreApplication.translate("GenerateReportStep", u"Generate the TSV report : distribution of sleep stages and transitions between different sleep stages.", None))
        self.label.setText(QCoreApplication.translate("GenerateReportStep", u"Output directory", None))
#if QT_CONFIG(tooltip)
        self.output_lineedit.setToolTip(QCoreApplication.translate("GenerateReportStep", u"Choose the output directory for all the reports to generate.", None))
#endif // QT_CONFIG(tooltip)
        self.choose_pushbutton.setText(QCoreApplication.translate("GenerateReportStep", u"Choose", None))
        self.label_3.setText(QCoreApplication.translate("GenerateReportStep", u"Report prefix", None))
#if QT_CONFIG(tooltip)
        self.prefix_lineedit.setToolTip(QCoreApplication.translate("GenerateReportStep", u"Label added to each report to identify your reports.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("GenerateReportStep", u"<html><head/><body><p>List of <span style=\" font-weight:600;\">Events Reports</span> to generate (distribution of events by sleep stage, cycle, and thirds and halves of the night)</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("GenerateReportStep", u"<html><head/><body><p>List of <span style=\" font-weight:600;\">Temporal Links Reports</span> to generate (occurrence of event 1 starting before the start of event 2)</p></body></html>", None))
    # retranslateUi


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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)
import themes_rc

class Ui_HoursCyclesStep(object):
    def setupUi(self, HoursCyclesStep):
        if not HoursCyclesStep.objectName():
            HoursCyclesStep.setObjectName(u"HoursCyclesStep")
        HoursCyclesStep.resize(616, 229)
        HoursCyclesStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(HoursCyclesStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(HoursCyclesStep)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spinBox_hours = QSpinBox(HoursCyclesStep)
        self.spinBox_hours.setObjectName(u"spinBox_hours")
        self.spinBox_hours.setMinimum(1)
        self.spinBox_hours.setMaximum(48)
        self.spinBox_hours.setValue(8)

        self.horizontalLayout.addWidget(self.spinBox_hours)

        self.label_3 = QLabel(HoursCyclesStep)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(HoursCyclesStep)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spinBox_cycles = QSpinBox(HoursCyclesStep)
        self.spinBox_cycles.setObjectName(u"spinBox_cycles")
        self.spinBox_cycles.setMinimum(1)
        self.spinBox_cycles.setMaximum(12)
        self.spinBox_cycles.setValue(6)

        self.horizontalLayout_2.addWidget(self.spinBox_cycles)

        self.label_4 = QLabel(HoursCyclesStep)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 9, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(HoursCyclesStep)

        QMetaObject.connectSlotsByName(HoursCyclesStep)
    # setupUi

    def retranslateUi(self, HoursCyclesStep):
        HoursCyclesStep.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("HoursCyclesStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Maximum number of hours</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("HoursCyclesStep", u"Define the maximum number of hours to analyze in the reports.", None))
        self.label_2.setText(QCoreApplication.translate("HoursCyclesStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Maximum number of sleep cycles</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("HoursCyclesStep", u"Define the maximum number of cycles to analyze in the reports.", None))
    # retranslateUi


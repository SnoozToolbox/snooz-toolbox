# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_OutputFileStep.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_OutputFileStep(object):
    def setupUi(self, OutputFileStep):
        if not OutputFileStep.objectName():
            OutputFileStep.setObjectName(u"OutputFileStep")
        OutputFileStep.resize(747, 590)
        self.verticalLayout = QVBoxLayout(OutputFileStep)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(OutputFileStep)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 2, 1, 3)

        self.label_4 = QLabel(OutputFileStep)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 4)

        self.pushButton_CohortFilename = QPushButton(OutputFileStep)
        self.pushButton_CohortFilename.setObjectName(u"pushButton_CohortFilename")

        self.gridLayout.addWidget(self.pushButton_CohortFilename, 6, 5, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 2, 1, 1)

        self.label_6 = QLabel(OutputFileStep)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 3, 1, 3)

        self.label_2 = QLabel(OutputFileStep)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 3, 1, 2)

        self.label_3 = QLabel(OutputFileStep)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 3, 1, 2)

        self.lineEdit_CohortFilename = QLineEdit(OutputFileStep)
        self.lineEdit_CohortFilename.setObjectName(u"lineEdit_CohortFilename")

        self.gridLayout.addWidget(self.lineEdit_CohortFilename, 6, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(OutputFileStep)

        QMetaObject.connectSlotsByName(OutputFileStep)
    # setupUi

    def retranslateUi(self, OutputFileStep):
        OutputFileStep.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("OutputFileStep", u"<html><head/><body><p><span style=\" font-weight:700;\">REMs Cohort Report (One line per recording)</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("OutputFileStep", u"<html><head/><body><p><span style=\" font-weight:700;\">REMs Events Characteristics</span></p></body></html>", None))
        self.pushButton_CohortFilename.setText(QCoreApplication.translate("OutputFileStep", u"Browse", None))
        self.label_6.setText(QCoreApplication.translate("OutputFileStep", u"<html><head/><body><p>The characteristics folder (saved in the input files directory) includes two files:</p><p><span style=\" font-weight:700;\">Events file:</span> Contains all events in Snooz annotation format.<br/><span style=\" font-weight:700;\">Summary file:</span> Contains per-event details, including start time, peak time, end time, duration,<br/>LOC/ROC absolute amplitude at REM peak (\u03bcV), and LOC/ROC absolute rise and fall slopes (\u03bcV/s).</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("OutputFileStep", u"<html><head/><body><p>Included parameters:</p><p>- REMs count<br/>- Duration of the REMs in second<br/>- Amplitude of the REMs (Difference between the peak and trough of the [LOC - ROC])<br/>- Density of the REMs in cycles and hours<br/>- Variablity of the densities<br/>- Phasic/Tonic REM percentage<br/>- Peak-to-Peak energy in uv squared<br/>- Peak-to-Peak activity index</p><p>The report consists of the average of the mentioned characteristics in:</p><p>- total (all night)<br/>- per sleep cycle<br/>- per clock hour<br/>- per hour spent in each stage</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("OutputFileStep", u"<html><head/><body><p>Select a file name to save the report file:</p></body></html>", None))
    # retranslateUi


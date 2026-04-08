# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DetectorStep.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QWidget)
import themes_rc

class Ui_DetectorStep(object):
    def setupUi(self, DetectorStep):
        if not DetectorStep.objectName():
            DetectorStep.setObjectName(u"DetectorStep")
        DetectorStep.resize(934, 640)
        DetectorStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.gridLayout_2 = QGridLayout(DetectorStep)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_7 = QFrame(DetectorStep)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_7.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.gridLayout.addWidget(self.frame_7, 4, 2, 1, 1)

        self.frame_6 = QFrame(DetectorStep)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_6.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.gridLayout.addWidget(self.frame_6, 5, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 15, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.frame_8 = QFrame(DetectorStep)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_8.setLineWidth(0)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_3 = QLineEdit(self.frame_8)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_8.addWidget(self.lineEdit_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)


        self.gridLayout_5.addWidget(self.frame_8, 2, 2, 1, 1)

        self.frame_9 = QFrame(DetectorStep)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_9.setLineWidth(0)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBox_2 = QCheckBox(self.frame_9)
        self.checkBox_2.setObjectName(u"checkBox_2")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet(u"font: 12pt \"Roboto\";")

        self.horizontalLayout_9.addWidget(self.checkBox_2)


        self.gridLayout_5.addWidget(self.frame_9, 3, 2, 1, 1)

        self.frame_2 = QFrame(DetectorStep)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Roboto-Regular"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setLineWidth(0)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_11)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setSingleStep(0.010000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_6)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_2.addWidget(self.label_12)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setSingleStep(0.010000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)


        self.gridLayout_5.addWidget(self.frame_2, 0, 4, 1, 1)

        self.frame_5 = QFrame(DetectorStep)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_5.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setLineWidth(0)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.checkBox = QCheckBox(self.frame_5)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"font: 12pt \"Roboto\";")

        self.horizontalLayout_5.addWidget(self.checkBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.gridLayout_5.addWidget(self.frame_5, 2, 4, 1, 1)

        self.label_3 = QLabel(DetectorStep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setFont(font1)
        self.label_3.setLineWidth(0)
        self.label_3.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_3, 1, 1, 1, 1)

        self.label_6 = QLabel(DetectorStep)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.frame_4 = QFrame(DetectorStep)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setFont(font1)
        self.label_4.setLineWidth(0)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.frame_4)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setSingleStep(0.010000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.gridLayout_5.addWidget(self.frame_4, 1, 4, 1, 1)

        self.frame = QFrame(DetectorStep)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout.addWidget(self.label_18)

        self.spinBox_2 = QSpinBox(self.frame)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(10000)

        self.horizontalLayout.addWidget(self.spinBox_2)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout.addWidget(self.label_17)

        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(10000)

        self.horizontalLayout.addWidget(self.spinBox)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)


        self.gridLayout_5.addWidget(self.frame, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.label_16 = QLabel(DetectorStep)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setLineWidth(0)

        self.gridLayout_5.addWidget(self.label_16, 2, 1, 1, 1)

        self.label_8 = QLabel(DetectorStep)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setLineWidth(0)

        self.gridLayout_5.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_22 = QLabel(DetectorStep)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_5.addWidget(self.label_22, 3, 3, 1, 1)

        self.frame_3 = QFrame(DetectorStep)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.doubleSpinBox = QDoubleSpinBox(self.frame_3)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setSingleStep(0.010000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox)

        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_3.addWidget(self.label_14)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.frame_3)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setSingleStep(0.010000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_3)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_11)


        self.gridLayout_5.addWidget(self.frame_3, 1, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_5, 6, 0, 1, 4)

        self.label_19 = QLabel(DetectorStep)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_10 = QLabel(DetectorStep)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 17, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit = QLineEdit(DetectorStep)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 2, 3, 1, 1)

        self.label_15 = QLabel(DetectorStep)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setLineWidth(-3)

        self.gridLayout_4.addWidget(self.label_15, 2, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 2, 4, 1, 1)

        self.lineEdit_2 = QLineEdit(DetectorStep)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_4.addWidget(self.lineEdit_2, 3, 3, 1, 1)

        self.label_20 = QLabel(DetectorStep)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 0, 1, 1, 3)

        self.label_9 = QLabel(DetectorStep)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        self.label_9.setLineWidth(0)

        self.gridLayout_4.addWidget(self.label_9, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 4, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_4, 2, 0, 1, 4)

        self.label = QLabel(DetectorStep)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setFont(font1)
        self.label.setLineWidth(0)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 5, 0, 1, 2)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_5 = QLabel(DetectorStep)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 0, 1, 1, 1)

        self.pushButton_CohortFilename = QPushButton(DetectorStep)
        self.pushButton_CohortFilename.setObjectName(u"pushButton_CohortFilename")

        self.gridLayout_7.addWidget(self.pushButton_CohortFilename, 2, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_5, 0, 0, 1, 1)

        self.lineEdit_CohortFilename = QLineEdit(DetectorStep)
        self.lineEdit_CohortFilename.setObjectName(u"lineEdit_CohortFilename")
        self.lineEdit_CohortFilename.setFrame(True)

        self.gridLayout_7.addWidget(self.lineEdit_CohortFilename, 2, 1, 1, 1)

        self.label_21 = QLabel(DetectorStep)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_7.addWidget(self.label_21, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_7, 20, 0, 1, 4)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(DetectorStep)

        QMetaObject.connectSlotsByName(DetectorStep)
    # setupUi

    def retranslateUi(self, DetectorStep):
        DetectorStep.setWindowTitle("")
        self.checkBox_2.setText(QCoreApplication.translate("DetectorStep", u"Yes", None))
        self.label_2.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Duration (s)</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Min:</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Max:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Remove Outliers     </span></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("DetectorStep", u"Yes", None))
        self.label_3.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">REM Frequency (Hz)</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hypnogram is Loaded</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Relative Prominence   </span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Min:</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Max:</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Sleep Stages</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Amplitude (uV)</span></p></body></html>", None))
        self.label_22.setText("")
        self.label_13.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Min:</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Max: </span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">REMs Event Definition</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">REMs Cohort Report</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Event Group</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Event group and name to label the new detection in the annotation file.</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Event Name</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">REMs Detector Criteria</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">REMs characteristics:</span></p><p><span style=\" font-size:12pt;\">	- REMs count<br/>- Duration of the REMs in second<br/>- Amplitude of the REMs (Difference between the peak and trough of the [LOC - ROC])<br/>- Density of the REMs in cycles and hours<br/>- Variablity of the densities</span></p><p><span style=\" font-size:12pt;\">The report consists of the average of the mentioned characteristics in</span></p><p><span style=\" font-size:12pt;\">- total (all selected stages)<br/>- per sleep cycle<br/>- per clock hour<br/>- per hour spent in each stage</span></p><p><br/></p></body></html>", None))
        self.pushButton_CohortFilename.setText(QCoreApplication.translate("DetectorStep", u"Browse", None))
        self.label_21.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Select a file name to save the report file:</span></p></body></html>", None))
    # retranslateUi


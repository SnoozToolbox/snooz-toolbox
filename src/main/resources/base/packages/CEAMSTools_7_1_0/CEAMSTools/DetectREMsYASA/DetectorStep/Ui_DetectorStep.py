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
    QSizePolicy, QSpacerItem, QSpinBox, QWidget)

class Ui_DetectorStep(object):
    def setupUi(self, DetectorStep):
        if not DetectorStep.objectName():
            DetectorStep.setObjectName(u"DetectorStep")
        DetectorStep.resize(874, 602)
        self.gridLayout_2 = QGridLayout(DetectorStep)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_15 = QLabel(DetectorStep)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setLineWidth(-3)

        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 2)

        self.frame_5 = QFrame(DetectorStep)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_5.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox = QCheckBox(self.frame_5)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_5.addWidget(self.checkBox)


        self.gridLayout.addWidget(self.frame_5, 10, 2, 1, 1)

        self.label_7 = QLabel(DetectorStep)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setLineWidth(0)

        self.gridLayout.addWidget(self.label_7, 10, 0, 1, 1)

        self.label_9 = QLabel(DetectorStep)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        self.label_9.setLineWidth(0)

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 7, 3, 1, 1)

        self.label_3 = QLabel(DetectorStep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Roboto-Regular"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(0)
        self.label_3.setWordWrap(True)

        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)

        self.frame_4 = QFrame(DetectorStep)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.frame_4)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setSingleStep(0.010000000000000)

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.gridLayout.addWidget(self.frame_4, 8, 2, 1, 2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_10, 6, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        self.frame_2 = QFrame(DetectorStep)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")

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

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.frame_2, 6, 2, 1, 1)

        self.frame = QFrame(DetectorStep)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.frame, 5, 2, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_12, 10, 3, 1, 1)

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


        self.gridLayout.addWidget(self.frame_8, 9, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_11, 9, 3, 1, 1)

        self.label_4 = QLabel(DetectorStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setFont(font)
        self.label_4.setLineWidth(0)

        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 1, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 15, 0, 1, 1)

        self.label = QLabel(DetectorStep)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setFont(font)
        self.label.setLineWidth(0)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 4, 0, 1, 2)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 5, 3, 1, 1)

        self.label_16 = QLabel(DetectorStep)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setLineWidth(0)

        self.gridLayout.addWidget(self.label_16, 9, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 2)

        self.label_2 = QLabel(DetectorStep)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setFont(font)
        self.label_2.setLineWidth(0)

        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)

        self.label_8 = QLabel(DetectorStep)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setLineWidth(0)

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)

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

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout.addWidget(self.frame_3, 7, 2, 1, 1)

        self.frame_7 = QFrame(DetectorStep)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_7.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_7.addWidget(self.lineEdit)


        self.gridLayout.addWidget(self.frame_7, 0, 2, 1, 1)

        self.frame_6 = QFrame(DetectorStep)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_6.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit_2 = QLineEdit(self.frame_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_6.addWidget(self.lineEdit_2)


        self.gridLayout.addWidget(self.frame_6, 1, 2, 1, 1)

        self.label_6 = QLabel(DetectorStep)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.frame_9 = QFrame(DetectorStep)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_9.setLineWidth(0)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBox_2 = QCheckBox(self.frame_9)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font)

        self.horizontalLayout_9.addWidget(self.checkBox_2)


        self.gridLayout.addWidget(self.frame_9, 2, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(DetectorStep)

        QMetaObject.connectSlotsByName(DetectorStep)
    # setupUi

    def retranslateUi(self, DetectorStep):
        DetectorStep.setWindowTitle("")
        DetectorStep.setStyleSheet(QCoreApplication.translate("DetectorStep", u"font: 10pt \"Roboto-Regular\";", None))
        self.label_15.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">REMs Event group<br/>The group category in the annotation file.</span></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("DetectorStep", u"Yes", None))
        self.label_7.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Remove Outliers<br/></span>If &quot;Yes&quot;, YASA will automatically detect and remove REMs outliers using<br/>its algorithm. <span style=\" font-weight:600;\">Note</span> that this step will only be applied if there are more<br/>than 50 detected REMs in the first place.</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">REMs Event Name<br/>The event name in the annotation file.</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">REM Frequency (Hz)<br/></span>Frequency range of REMs.</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("DetectorStep", u"Value:", None))
        self.label_11.setText(QCoreApplication.translate("DetectorStep", u"Min:", None))
        self.label_12.setText(QCoreApplication.translate("DetectorStep", u"Max:", None))
        self.label_18.setText(QCoreApplication.translate("DetectorStep", u"Min:", None))
        self.label_17.setText(QCoreApplication.translate("DetectorStep", u"Max:", None))
        self.label_4.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Relative Prominence<br/></span>scales the minimum prominence threshold as a fraction of minimum amplitude.<br/>(e.g., relative prominence = 0.5 means peaks must stand out by at least 50%<br/>of the minimum amplitude.)</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">There are 6 main parameters for this tool:</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Sleep Stages<br/></span>If the hypnogram is loaded, the detection will only be applied<br/>to the values defiend in &quot;Sleep Stages&quot;: Default = 5 (REM)<br/>Format for multiple sleep stages, e.g., &quot;Sleep Stages&quot; : [5, 3, ...]</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Duration (s)<br/></span>Minimum and maximum duration of the REMs.</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Amplitude (uV)<br/></span>Minimum and maximum amplitude of the peak of the REM.</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("DetectorStep", u"Min:", None))
        self.label_14.setText(QCoreApplication.translate("DetectorStep", u"Max:", None))
        self.label_6.setText(QCoreApplication.translate("DetectorStep", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hypnogram Loaded</span></p></body></html>", None))
        self.checkBox_2.setText(QCoreApplication.translate("DetectorStep", u"Yes", None))
    # retranslateUi


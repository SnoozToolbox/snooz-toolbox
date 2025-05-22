# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_AlgoIntroStep.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QScrollArea, QSizePolicy, QSpacerItem, QSplitter,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_AlgoIntroStep(object):
    def setupUi(self, AlgoIntroStep):
        if not AlgoIntroStep.objectName():
            AlgoIntroStep.setObjectName(u"AlgoIntroStep")
        AlgoIntroStep.resize(1315, 732)
        AlgoIntroStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_7 = QVBoxLayout(AlgoIntroStep)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.splitter_2 = QSplitter(AlgoIntroStep)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.verticalLayoutWidget = QWidget(self.splitter_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777213, 16777215))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.frame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")
        self.label.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setToolTipDuration(-1)
        self.label_2.setStyleSheet(u"")
        self.label_2.setLineWidth(0)

        self.verticalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.verticalLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")
        self.label_3.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.label_3)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1265, 390))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.label_4.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.label_4.setToolTipDuration(-9)
        self.label_4.setStyleSheet(u"")
        self.label_4.setLineWidth(0)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.label_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.verticalLayoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_3.setLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"")
        self.label_5.setLineWidth(0)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_4.addWidget(self.label_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame_3)

        self.splitter_2.addWidget(self.verticalLayoutWidget)

        self.verticalLayout_7.addWidget(self.splitter_2)


        self.retranslateUi(AlgoIntroStep)

        QMetaObject.connectSlotsByName(AlgoIntroStep)
    # setupUi

    def retranslateUi(self, AlgoIntroStep):
        AlgoIntroStep.setWindowTitle(QCoreApplication.translate("AlgoIntroStep", u"Form", None))
        self.label.setText(QCoreApplication.translate("AlgoIntroStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Score Sleep Stages YASA</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("AlgoIntroStep", u"<html><head/><body><p>This tool <span style=\" font-weight:700;\">classifies sleep stages</span> from PSG recordings using 30-second epochs.</p><p>Sleep stages can be classified based on a single EEG electrode, preferably central ones (C3, C4).<br/>Including one EOG and one EMG channel can improve classification accuracy.</p><p align=\"justify\"><span style=\" font-weight:700;\">In Snooz, you can select up to four high-priority EEG channels</span>, allowing the tool to determine the most confident classification for each. </p><p align=\"justify\">NOTE: Based on the internal analysis of Snooz, configurations combining central channels with one frontal and one occipital channel typically demonstrate marginally better performance.</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("AlgoIntroStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Algorithm Details</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("AlgoIntroStep", u"<html><head/><body><p>The sleep staging algorithm, YASA, is an open-source tool that has been trained,<br/>using over 30,000 hours of polysomnographic (PSG) sleep data across diverse populations. </p><p>-&gt;<span style=\" font-weight:600;\"> Data processing:</span> The algorithm uses a central EEG channel, along with EOG, and EMG channels.<br/>These signals are downsampled to 100 Hz and bandpassed-filtered between 0.4 Hz and 30 Hz. </p><p>-&gt; <span style=\" font-weight:600;\">Feature Extraction:</span> The algorithm extracts a set of time and frequency domain features from the EEG signal, and optionaly from the EOG and EMG signals.<br/>These features are calculated for each 30-second epoch of raw data. </p><p>-&gt; <span style=\" font-weight:600;\">Smoothing and Normalization:</span> The algorithm uses a smoothing approach across all the aformentioned features to incorporate contextual infromation.<br/>All the smoothed features are then z-scored across each night. </p><p>-&gt; <span style=\" font-weight:600"
                        ";\">Machine Learning Classification:</span> A lightGBM classifier, a tree-based gradient-boosting classifier, is used. </p><p>-&gt; <span style=\" font-weight:600;\">Performance Evaluation:</span> The algorithm's performance is evaluated using standardized guidelines,<br/>including accuracy, Cohen's kappa, Matthews correlation coefficient, confusion matrices, and F1-scores. </p><p><span style=\" text-decoration: underline;\">Reference</span>: <br/>Vallat, Raphael, and Matthew P. Walker. \u201cAn open-source, high-performance tool for automated sleep staging.\u201d Elife 10 (2021). <br/>doi: https://doi.org/10.7554/eLife.70092 (Documentation: <a href=\"https://raphaelvallat.com/yasa/\"><span style=\" text-decoration: underline; color:#0000ff;\">https://raphaelvallat.com/yasa/)<br/></span></a></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("AlgoIntroStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Output</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("AlgoIntroStep", u"<html><head/><body><p>The YASA sleep scoring tool is compatible with different input files including, EDF, NATUS, and STS. </p><p>The output of the automatic scoring algorithm is an accessory file that saves the predicted sleep stages.</p></body></html>", None))
    # retranslateUi


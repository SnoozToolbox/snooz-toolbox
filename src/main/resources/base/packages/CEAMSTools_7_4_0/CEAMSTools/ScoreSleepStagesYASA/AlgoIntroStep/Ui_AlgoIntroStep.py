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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_AlgoIntroStep(object):
    def setupUi(self, AlgoIntroStep):
        if not AlgoIntroStep.objectName():
            AlgoIntroStep.setObjectName(u"AlgoIntroStep")
        AlgoIntroStep.resize(766, 367)
        AlgoIntroStep.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_5 = QVBoxLayout(AlgoIntroStep)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(AlgoIntroStep)
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

        self.label_2 = QTextEdit(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setToolTipDuration(-1)
        self.label_2.setStyleSheet(u"")
        self.label_2.setFrameShape(QFrame.Shape.NoFrame)
        self.label_2.setLineWidth(0)
        self.label_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_2.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(AlgoIntroStep)
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

        self.label_4 = QTextEdit(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.label_4.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.label_4.setToolTipDuration(-9)
        self.label_4.setStyleSheet(u"")
        self.label_4.setFrameShape(QFrame.Shape.NoFrame)
        self.label_4.setLineWidth(0)
        self.label_4.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_4.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_4.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(AlgoIntroStep)
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

        self.label_6 = QTextEdit(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"")
        self.label_6.setFrameShape(QFrame.Shape.NoFrame)
        self.label_6.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_6.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_6.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.label_6)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame_3)


        self.verticalLayout_5.addLayout(self.verticalLayout)


        self.retranslateUi(AlgoIntroStep)

        QMetaObject.connectSlotsByName(AlgoIntroStep)
    # setupUi

    def retranslateUi(self, AlgoIntroStep):
        AlgoIntroStep.setWindowTitle(QCoreApplication.translate("AlgoIntroStep", u"Form", None))
        self.label.setText(QCoreApplication.translate("AlgoIntroStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Score Sleep Stages with YASA</span></p></body></html>", None))
        self.label_2.setHtml(QCoreApplication.translate("AlgoIntroStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This tool <span style=\" font-weight:700;\">classifies sleep stages</span> from PSG recordings using 30-second epochs.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sleep stages can be classified based on a single EEG electrode, preferably central ones (C3, C4).<br />Including one EOG and one EMG channel can improve "
                        "classification accuracy.<br /><span style=\" font-weight:700;\">In Snooz, you can select up to four high-priority EEG channels</span>, <br />allowing the tool to determine the most confident classification for each. </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NOTE: Based on the internal analysis of Snooz, configurations combining central channels <br />with one frontal and one occipital channel typically demonstrate marginally better performance.</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("AlgoIntroStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Algorithm Details</span></p></body></html>", None))
        self.label_4.setHtml(QCoreApplication.translate("AlgoIntroStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The sleep staging algorithm, YASA, is an open-source tool that has been trained,<br />using over 30,000 hours of polysomnographic (PSG) sleep data across diverse populations. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">-Data processing:</span><br />The algorithm uses a central E"
                        "EG channel, along with EOG, and EMG channels.<br />These signals are downsampled to 100 Hz and bandpassed-filtered between 0.4 Hz and 30 Hz. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">-Feature Extraction:</span><br />The algorithm extracts a set of time and frequency domain features from the EEG signal, and optionaly from the EOG and EMG signals. <br />These features are calculated for each 30-second epoch of raw data. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">-Smoothing and Normalization:</span><br />The algorithm uses a smoothing approach across all the aformentioned features to incorporate contextual infromation.<br />All the smoothed features are then z-scored across each night. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-"
                        "right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">-Machine Learning Classification:</span><br />A lightGBM classifier, a tree-based gradient-boosting classifier, is used. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">-Performance Evaluation:</span><br />The algorithm's performance is evaluated using standardized guidelines,including accuracy, Cohen's kappa, Matthews correlation coefficient, confusion matrices, and F1-scores. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Reference</span>: <br />Vallat, Raphael, and Matthew P. Walker. \u201cAn open-source, high-performance tool for automated sleep staging.\u201d Elife 10 (2021). <br />doi: https://doi.org/10.7554/eLife.70092 (Documentation: <a href=\"https://raphaelvallat.com/ya"
                        "sa/\"><span style=\" text-decoration: underline; color:#0000ff;\">https://raphaelvallat.com/yasa/)</span></a></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("AlgoIntroStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Output</span></p></body></html>", None))
        self.label_6.setHtml(QCoreApplication.translate("AlgoIntroStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The YASA sleep scoring tool is compatible with different input files including, EDF, NATUS, and STS.<br />NOTE: For proper functionality with discontinuous files, the tool requires at least one EEG channel along with one EOG or EMG channel.<br />The output of the automatic scoring algorithm is an accessory file that saves the predicted sleep stages.</p></body></html>", None))
    # retranslateUi


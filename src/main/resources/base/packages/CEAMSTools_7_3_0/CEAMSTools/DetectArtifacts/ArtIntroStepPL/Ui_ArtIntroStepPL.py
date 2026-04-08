# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ArtIntroStepPL.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QLayout, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_ArtIntroStepPL(object):
    def setupUi(self, ArtIntroStepPL):
        if not ArtIntroStepPL.objectName():
            ArtIntroStepPL.setObjectName(u"ArtIntroStepPL")
        ArtIntroStepPL.resize(900, 854)
        ArtIntroStepPL.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout = QHBoxLayout(ArtIntroStepPL)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(ArtIntroStepPL)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 200))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.textEdit_3 = QTextEdit(self.widget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(4)
        sizePolicy2.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy2)
        self.textEdit_3.setMinimumSize(QSize(850, 0))
        self.textEdit_3.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_3.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_3.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.textEdit_3.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit_3)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setSizeIncrement(QSize(0, 0))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.textEdit_2 = QTextEdit(self.widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(3)
        sizePolicy3.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy3)
        self.textEdit_2.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit_2)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(ArtIntroStepPL)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_9)

        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)


        self.horizontalLayout.addWidget(self.widget_2)


        self.retranslateUi(ArtIntroStepPL)

        QMetaObject.connectSlotsByName(ArtIntroStepPL)
    # setupUi

    def retranslateUi(self, ArtIntroStepPL):
        ArtIntroStepPL.setWindowTitle(QCoreApplication.translate("ArtIntroStepPL", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("ArtIntroStepPL", u"<html><head/><body><p><span style=\" font-weight:600;\">Artifact Detector</span></p><p>This tool <span style=\" font-weight:600;\">detects artifacts</span> from PSG files.</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("ArtIntroStepPL", u"<html><head/><body><p><span style=\" font-weight:600;\">Types of artifacts</span></p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("ArtIntroStepPL", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     Flatline : Segments of low power, flatlined signal.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     High Frequency burst : Segments with a burst of high frequency power (&gt;25 Hz).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   "
                        "  Persistent Noise : Segments with high frequency noise (&gt;25 Hz).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     Power Line Contamination : Segments corrupted by 50 or 60 Hz power.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     Baseline Variation (Breathing, Sweat) : Segments with high power in the low frequency band (&lt;0.4 Hz).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     Muscle artifact : Segments with burst of activity in the frequency band 20.25-32 Hz.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Artifa"
                        "ct detection performs better when similar sleep stages are selected, as the power distribution can be modeled more accurately. Some detectors use a 3-component Gaussian Mixture Model (GMM) to estimate the standard deviation of non-corrupted data, which is then used to define the threshold value.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">We recommend running artifact detection separately for <span style=\" font-weight:700;\">NREM</span>, <span style=\" font-weight:700;\">REM</span>, and <span style=\" font-weight:700;\">Awake</span> stages.<br />Threshold values for the different algorithms can be edited; however, two sets of default values are also available.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Make sure to use different annotation groups or names to avoid confusion when running artifact detection twice. The default labels reflec"
                        "t the selected sleep stages and the chosen set of default values.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">While sleep stages are mandatory for sleep recordings, artifact detection can also be run on any EEG recording if <span style=\" font-weight:700;\">&quot;Unscored&quot;</span> is selected for the sleep stages.</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("ArtIntroStepPL", u"<html><head/><body><p><span style=\" font-weight:600;\">Output</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("ArtIntroStepPL", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The detected artifacts are added in the input file as new events <br />(i.e. .tsv for edf, .sts for Stellate and .ent for NATUS).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If the input file already contains the group and name of the new events to be added, they will first be deleted. </p>\n"
"<p style=\" margin-top:0"
                        "px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you detect artifact on an EDF file without accessory file, the accessory (.tsv) file will be automatically generated.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The output is a TSV (Tab Separated Values) file. A new row is added for every artifact detection.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The channel label is concatened to the artifact name with a @@ (EDFbrowser compatible).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The columns of the file are as follows:</p>\n"
"<p style=\" margin-top:0p"
                        "x; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     1. group : The group of the event is artifact.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     2. name : The name of the event. Ex. flatline.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     3. start_sec : The onset of the event in second. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     4. duration_sec : The duration of the event in second.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">     5. channels : The list of channels on which the event occurs.</p></body></html>", None))
        self.label_6.setText("")
        self.label_8.setText("")
        self.label_5.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
    # retranslateUi


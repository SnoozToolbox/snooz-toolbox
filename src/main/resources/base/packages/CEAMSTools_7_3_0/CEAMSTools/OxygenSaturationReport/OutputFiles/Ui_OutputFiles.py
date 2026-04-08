# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_OutputFiles.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_OutputFiles(object):
    def setupUi(self, OutputFiles):
        if not OutputFiles.objectName():
            OutputFiles.setObjectName(u"OutputFiles")
        OutputFiles.resize(991, 688)
        OutputFiles.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(OutputFiles)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(OutputFiles)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 470))
        self.textEdit.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit.setLineWidth(-1)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_filename = QLineEdit(OutputFiles)
        self.lineEdit_filename.setObjectName(u"lineEdit_filename")
        self.lineEdit_filename.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_filename.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lineEdit_filename)

        self.pushButton_browse = QPushButton(OutputFiles)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.horizontalLayout.addWidget(self.pushButton_browse)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_4 = QLabel(OutputFiles)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label = QLabel(OutputFiles)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.checkBox_writeEvts = QCheckBox(OutputFiles)
        self.checkBox_writeEvts.setObjectName(u"checkBox_writeEvts")

        self.verticalLayout.addWidget(self.checkBox_writeEvts)

        self.label_5 = QLabel(OutputFiles)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(OutputFiles)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_2 = QLabel(OutputFiles)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_picturename = QLineEdit(OutputFiles)
        self.lineEdit_picturename.setObjectName(u"lineEdit_picturename")
        self.lineEdit_picturename.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_picturename.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_picturename)

        self.pushButton_browse_pic = QPushButton(OutputFiles)
        self.pushButton_browse_pic.setObjectName(u"pushButton_browse_pic")

        self.horizontalLayout_2.addWidget(self.pushButton_browse_pic)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(OutputFiles)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(OutputFiles)
        self.pushButton_browse.clicked.connect(OutputFiles.browse_slot)
        self.pushButton_browse_pic.clicked.connect(OutputFiles.browse_pic_slot)
        self.checkBox_writeEvts.clicked.connect(OutputFiles.write_checkbox_slot)

        QMetaObject.connectSlotsByName(OutputFiles)
    # setupUi

    def retranslateUi(self, OutputFiles):
        OutputFiles.setWindowTitle("")
        self.textEdit.setHtml(QCoreApplication.translate("OutputFiles", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Cohort Oxygen Saturation Report</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The oxygen saturation is analyzed during the sleep period, defined as the interval from the first epoch scored as sleep (N1, N2, N3, or R) to the final awakening (including the last epoch scored as s"
                        "leep).</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Automatic artifact detection is applied to the oximeter channel: segments longer than 5 s marked as artifacts are excluded from the analysis, while shorter segments are interpolated.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The report contains three main categories of metrics:</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">1. Oxygen Saturation Variables</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Minimum, maximum, mean, and variability (standard deviation) of saturation values<br />- Percentage of time spent below clinically relevant saturation thresholds (96 % to 60 %)</p>\n"
""
                        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Metrics are computed for the entire sleep period and stratified by sleep thirds, halves, sleep cycles, and sleep stages (W, N1, N2, N3, REM, NREM, N2\u2013N3, and total sleep).</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">2. Oxygen Desaturation Variables</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Total number of events<br />- Index (ODI, events per hour)<br />- Severity (sum of areas under desaturation events, in percent\u00b7sec, over the sleep period)<br />- Percentage of sleep time spent in desaturation<br />- Average and median desaturation characteristics: Duration (s), Area (% s), Slope (% / s) and Drop (%).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">3. Oxygen Recovery Variables</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Total number of events<br />- Index (events per hour)<br />- Severity (sum of areas under recovery events, in percent\u00b7sec, over the sleep period)<br />- Percentage of sleep time spent in recovery<br />- Average and median recovery characteristics: Duration (s), Area (% s), Slope (% / s) and Amplitude (%).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                        "0; text-indent:0px;\">The <span style=\" font-weight:700;\">Total Severity </span>corresponds to the sum of the individual desaturation and recovery areas in percent*sec over the valid sleep period (sec).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All metrics are stored in the Cohort Oxygen Saturation Report, with one line per recording. </p></body></html>", None))
        self.lineEdit_filename.setText("")
        self.lineEdit_filename.setPlaceholderText(QCoreApplication.translate("OutputFiles", u"Define the file to save the Cohort Oxygen Saturation Report...", None))
        self.pushButton_browse.setText(QCoreApplication.translate("OutputFiles", u"Browse", None))
        self.label_4.setText(QCoreApplication.translate("OutputFiles", u"* New recordings are added (appended) at the end of the file ", None))
        self.label.setText(QCoreApplication.translate("OutputFiles", u"<html><head/><body><p><span style=\" font-weight:700;\">Optional outputs</span></p></body></html>", None))
        self.checkBox_writeEvts.setText(QCoreApplication.translate("OutputFiles", u"Write the desaturation events in the accessory file provided with the PSG recording.", None))
        self.label_5.setText(QCoreApplication.translate("OutputFiles", u"Oxygen desaturation events are defined as : group = SpO2; name = desat_SpO2", None))
        self.label_6.setText(QCoreApplication.translate("OutputFiles", u"Oxygen recovery events are defined as : group = SpO2; name = recovery_SpO2", None))
        self.label_2.setText(QCoreApplication.translate("OutputFiles", u" Output directory to save the characteristics report and oxygen saturation graph for each recording", None))
        self.lineEdit_picturename.setText("")
        self.lineEdit_picturename.setPlaceholderText(QCoreApplication.translate("OutputFiles", u"Select a folder to save the optional files ...", None))
        self.pushButton_browse_pic.setText(QCoreApplication.translate("OutputFiles", u"Browse", None))
        self.label_3.setText(QCoreApplication.translate("OutputFiles", u"Files are generated only if the user specifies an output directory.\n"
"Filenames use the PSG filename as a prefix, with 'oxygen_saturation_events' and 'oxygen_saturation_graph' added as suffixes.", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Outputfiles.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_Outputfiles(object):
    def setupUi(self, Outputfiles):
        if not Outputfiles.objectName():
            Outputfiles.setObjectName(u"Outputfiles")
        Outputfiles.resize(864, 876)
        self.verticalLayout_3 = QVBoxLayout(Outputfiles)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Outputfiles)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.radioButton_stage = QRadioButton(Outputfiles)
        self.radioButton_stage.setObjectName(u"radioButton_stage")
        self.radioButton_stage.setEnabled(False)
        self.radioButton_stage.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioButton_stage)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(30, 13, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Outputfiles)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.total_checkBox = QCheckBox(self.frame)
        self.total_checkBox.setObjectName(u"total_checkBox")
        self.total_checkBox.setEnabled(False)
        self.total_checkBox.setMinimumSize(QSize(210, 0))
        self.total_checkBox.setMaximumSize(QSize(210, 16777215))
        self.total_checkBox.setChecked(True)

        self.horizontalLayout.addWidget(self.total_checkBox)

        self.textEdit_tot = QTextEdit(self.frame)
        self.textEdit_tot.setObjectName(u"textEdit_tot")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_tot.sizePolicy().hasHeightForWidth())
        self.textEdit_tot.setSizePolicy(sizePolicy)
        self.textEdit_tot.setMaximumSize(QSize(16777215, 140))
        self.textEdit_tot.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_tot.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_tot.setLineWidth(0)
        self.textEdit_tot.setReadOnly(True)

        self.horizontalLayout.addWidget(self.textEdit_tot)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Outputfiles)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.hour_checkBox = QCheckBox(self.frame_2)
        self.hour_checkBox.setObjectName(u"hour_checkBox")
        self.hour_checkBox.setMinimumSize(QSize(210, 0))
        self.hour_checkBox.setMaximumSize(QSize(210, 16777215))
        self.hour_checkBox.setChecked(True)

        self.horizontalLayout_3.addWidget(self.hour_checkBox)

        self.textEdit_hour = QTextEdit(self.frame_2)
        self.textEdit_hour.setObjectName(u"textEdit_hour")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit_hour.sizePolicy().hasHeightForWidth())
        self.textEdit_hour.setSizePolicy(sizePolicy1)
        self.textEdit_hour.setMinimumSize(QSize(0, 0))
        self.textEdit_hour.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_hour.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_hour.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_hour.setLineWidth(0)
        self.textEdit_hour.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.textEdit_hour)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Outputfiles)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.cycle_checkBox = QCheckBox(self.frame_3)
        self.cycle_checkBox.setObjectName(u"cycle_checkBox")
        self.cycle_checkBox.setMinimumSize(QSize(210, 0))
        self.cycle_checkBox.setMaximumSize(QSize(210, 16777215))
        self.cycle_checkBox.setChecked(True)

        self.horizontalLayout_4.addWidget(self.cycle_checkBox)

        self.textEdit_cycle = QTextEdit(self.frame_3)
        self.textEdit_cycle.setObjectName(u"textEdit_cycle")
        sizePolicy1.setHeightForWidth(self.textEdit_cycle.sizePolicy().hasHeightForWidth())
        self.textEdit_cycle.setSizePolicy(sizePolicy1)
        self.textEdit_cycle.setMinimumSize(QSize(0, 0))
        self.textEdit_cycle.setMaximumSize(QSize(16777215, 135))
        self.textEdit_cycle.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_cycle.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_cycle.setLineWidth(0)
        self.textEdit_cycle.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.textEdit_cycle)


        self.verticalLayout.addWidget(self.frame_3)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.radioButton_annot = QRadioButton(Outputfiles)
        self.radioButton_annot.setObjectName(u"radioButton_annot")
        self.radioButton_annot.setEnabled(False)

        self.verticalLayout.addWidget(self.radioButton_annot)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(Outputfiles)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)

        self.textEdit_4 = QTextEdit(Outputfiles)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMaximumSize(QSize(16777215, 60))
        self.textEdit_4.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_4.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_4.setLineWidth(0)
        self.textEdit_4.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_4.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_4.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Outputfiles)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.filename_lineEdit = QLineEdit(Outputfiles)
        self.filename_lineEdit.setObjectName(u"filename_lineEdit")
        self.filename_lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.filename_lineEdit)

        self.choose_pushButton = QPushButton(Outputfiles)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.horizontalLayout_2.addWidget(self.choose_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Outputfiles)
        self.choose_pushButton.clicked.connect(Outputfiles.choose_button_slot)

        QMetaObject.connectSlotsByName(Outputfiles)
    # setupUi

    def retranslateUi(self, Outputfiles):
        Outputfiles.setWindowTitle("")
        Outputfiles.setStyleSheet(QCoreApplication.translate("Outputfiles", u"font: 12pt \"Roboto\";", None))
        self.label.setText(QCoreApplication.translate("Outputfiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Spectral power distribution to export</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.radioButton_stage.setToolTip(QCoreApplication.translate("Outputfiles", u"To enable the radio button go to the Section Selection Step.", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_stage.setText(QCoreApplication.translate("Outputfiles", u"The spectral power is computed per sleep stage and per hour and/or sleep cycle acording to these selected options:", None))
#if QT_CONFIG(tooltip)
        self.total_checkBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.total_checkBox.setText(QCoreApplication.translate("Outputfiles", u"Total", None))
        self.textEdit_tot.setHtml(QCoreApplication.translate("Outputfiles", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Check &quot;<span style=\" font-weight:600;\">Total</span>&quot; to output the avearge spectral power for the whole recording. <br />The average power includes only valid FFT windows (clean windows of selected stages or periods).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p sty"
                        "le=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">If &quot;Analyse power in sleep cycle only&quot; in the step &quot;4-Section Selection&quot; is checked, <br />the starting point is the sleep onset and gabs between cycles are not analysed.<br />Otherwise all the recording is analysed, even before the sleep onset and after the last asleep epoch.</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.hour_checkBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.hour_checkBox.setText(QCoreApplication.translate("Outputfiles", u"Distribution per hour", None))
        self.textEdit_hour.setHtml(QCoreApplication.translate("Outputfiles", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Check &quot;<span style=\" font-weight:600;\">Distribution per hour</span>&quot; to output the average spectral power for each real clock hour and stage hour, starting from hour 1. <br />The average power includes only valid FFT windows (clean windows of selected stages or periods).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-bl"
                        "ock-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The spectral power value will be empty if no data is available for a given hour <br />(e.g., if only N2 is selected and there are no N2 stages in the first hour, the reported power will be empty).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The maximum clock hour included in the report is defined in the optional settings under &quot;<span style=\" font-weight:600;\">Hours and Cycles</span>&quot;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">If &quot;Analyse power in sleep cycle only&qu"
                        "ot; in the step &quot;4-Section Selection&quot; is checked, <br />the starting point is the sleep onset and gabs between cycles are not analysed.<br />Otherwise all the recording is analysed, even before the sleep onset and after the last asleep epoch.</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.cycle_checkBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.cycle_checkBox.setText(QCoreApplication.translate("Outputfiles", u"Distribution per sleep cycle", None))
        self.textEdit_cycle.setHtml(QCoreApplication.translate("Outputfiles", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Check &quot;<span style=\" font-weight:600;\">Distribution per sleep cycle</span>&quot; to output the average spectral power for each sleep cycle, starting from cycle 1. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The average power includes only valid FFT windows (clean windows of selected stages or periods).</p>\n"
""
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The spectral power value will be empty if the cycle does not exist.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The maximum number of cycles included in the report is defined in the optional settings under &quot;<span style=\" font-weight:600;\">Hours and Cycles</span>&quot;.</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.radioButton_annot.setToolTip(QCoreApplication.translate("Outputfiles", u"To enable the radio button go to the Section Selection Step.", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_annot.setText(QCoreApplication.translate("Outputfiles", u"The spectral power is computed on selected events.", None))
        self.label_4.setText(QCoreApplication.translate("Outputfiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Output</span></p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("Outputfiles", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The output file is a .tsv (tab separated values) file. Each line corresponds to a subject, a channel, and a frequency band. Warning : Spectral data are appended to the output file, so the file will be modified each time the tool is run.</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Outputfiles", u"Filename", None))
        self.filename_lineEdit.setInputMask("")
        self.filename_lineEdit.setText("")
        self.filename_lineEdit.setPlaceholderText(QCoreApplication.translate("Outputfiles", u"Select the file to save the cohort EEG spectral report.", None))
        self.choose_pushButton.setText(QCoreApplication.translate("Outputfiles", u"Choose", None))
    # retranslateUi


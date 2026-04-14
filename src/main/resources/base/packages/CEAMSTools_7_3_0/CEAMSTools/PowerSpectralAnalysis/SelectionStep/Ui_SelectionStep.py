# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SelectionStep.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QRadioButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_SelectionStep(object):
    def setupUi(self, SelectionStep):
        if not SelectionStep.objectName():
            SelectionStep.setObjectName(u"SelectionStep")
        SelectionStep.resize(775, 787)
        self.verticalLayout_4 = QVBoxLayout(SelectionStep)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(SelectionStep)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)

        self.verticalLayout_4.addWidget(self.label)

        self.radioButton_annotations = QRadioButton(SelectionStep)
        self.radioButton_annotations.setObjectName(u"radioButton_annotations")

        self.verticalLayout_4.addWidget(self.radioButton_annotations)

        self.radioButton_sleep = QRadioButton(SelectionStep)
        self.radioButton_sleep.setObjectName(u"radioButton_sleep")
        self.radioButton_sleep.setChecked(True)

        self.verticalLayout_4.addWidget(self.radioButton_sleep)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(SelectionStep)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.label_3 = QLabel(SelectionStep)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.unscored_checkBox = QCheckBox(SelectionStep)
        self.unscored_checkBox.setObjectName(u"unscored_checkBox")
        self.unscored_checkBox.setMinimumSize(QSize(70, 0))

        self.gridLayout.addWidget(self.unscored_checkBox, 0, 0, 1, 1)

        self.n1_checkBox = QCheckBox(SelectionStep)
        self.n1_checkBox.setObjectName(u"n1_checkBox")
        self.n1_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.n1_checkBox, 1, 0, 1, 1)

        self.r_checkBox = QCheckBox(SelectionStep)
        self.r_checkBox.setObjectName(u"r_checkBox")
        self.r_checkBox.setMinimumSize(QSize(70, 0))
        self.r_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.r_checkBox, 2, 1, 1, 1)

        self.w_checkBox = QCheckBox(SelectionStep)
        self.w_checkBox.setObjectName(u"w_checkBox")
        self.w_checkBox.setMinimumSize(QSize(70, 0))
        self.w_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.w_checkBox, 0, 1, 1, 1)

        self.n3_checkBox = QCheckBox(SelectionStep)
        self.n3_checkBox.setObjectName(u"n3_checkBox")
        self.n3_checkBox.setMinimumSize(QSize(70, 0))
        self.n3_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.n3_checkBox, 1, 2, 1, 2)

        self.n2_checkBox = QCheckBox(SelectionStep)
        self.n2_checkBox.setObjectName(u"n2_checkBox")
        self.n2_checkBox.setMinimumSize(QSize(70, 0))
        self.n2_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.n2_checkBox, 1, 1, 1, 1)

        self.s4_checkBox = QCheckBox(SelectionStep)
        self.s4_checkBox.setObjectName(u"s4_checkBox")
        self.s4_checkBox.setEnabled(False)

        self.gridLayout.addWidget(self.s4_checkBox, 2, 0, 1, 1)

        self.nrem_checkBox = QCheckBox(SelectionStep)
        self.nrem_checkBox.setObjectName(u"nrem_checkBox")
        self.nrem_checkBox.setMinimumSize(QSize(70, 0))
        self.nrem_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.nrem_checkBox, 2, 2, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)

        self.label_4 = QLabel(SelectionStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_7 = QLabel(SelectionStep)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.in_cycle_checkBox = QCheckBox(SelectionStep)
        self.in_cycle_checkBox.setObjectName(u"in_cycle_checkBox")
        self.in_cycle_checkBox.setEnabled(True)
        self.in_cycle_checkBox.setCheckable(True)
        self.in_cycle_checkBox.setChecked(True)

        self.gridLayout_2.addWidget(self.in_cycle_checkBox, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.excl_nremp_checkBox = QCheckBox(SelectionStep)
        self.excl_nremp_checkBox.setObjectName(u"excl_nremp_checkBox")
        self.excl_nremp_checkBox.setMinimumSize(QSize(0, 0))
        self.excl_nremp_checkBox.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_2.addWidget(self.excl_nremp_checkBox)

        self.excl_remp_checkBox = QCheckBox(SelectionStep)
        self.excl_remp_checkBox.setObjectName(u"excl_remp_checkBox")

        self.verticalLayout_2.addWidget(self.excl_remp_checkBox)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.textEdit = QTextEdit(SelectionStep)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit, 0, 1, 1, 1)

        self.textEdit_2 = QTextEdit(SelectionStep)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_2.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_2.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_2.setLineWidth(0)
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_2.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit_2, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.retranslateUi(SelectionStep)
        self.radioButton_annotations.clicked.connect(SelectionStep.update_section_selection_slot)
        self.radioButton_sleep.clicked.connect(SelectionStep.update_section_selection_slot)
        self.nrem_checkBox.clicked.connect(SelectionStep.NREM_checkbox_slot)
        self.excl_nremp_checkBox.clicked.connect(SelectionStep.NREM_stages_and_periods_slot)
        self.excl_remp_checkBox.clicked.connect(SelectionStep.REM_stages_and_periods_slot)
        self.n2_checkBox.clicked.connect(SelectionStep.NREM_stages_and_periods_slot)
        self.n3_checkBox.clicked.connect(SelectionStep.NREM_stages_and_periods_slot)
        self.nrem_checkBox.clicked.connect(SelectionStep.NREM_stages_and_periods_slot)
        self.r_checkBox.clicked.connect(SelectionStep.REM_stages_and_periods_slot)

        QMetaObject.connectSlotsByName(SelectionStep)
    # setupUi

    def retranslateUi(self, SelectionStep):
        SelectionStep.setWindowTitle("")
#if QT_CONFIG(tooltip)
        SelectionStep.setToolTip("")
#endif // QT_CONFIG(tooltip)
        SelectionStep.setStyleSheet(QCoreApplication.translate("SelectionStep", u"font: 12pt \"Roboto\";", None))
        self.label.setText(QCoreApplication.translate("SelectionStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Section selection to perform the EEG spectal power. </span></p></body></html>", None))
        self.radioButton_annotations.setText(QCoreApplication.translate("SelectionStep", u"Analyse spectral power for specific annotations (in the next step)", None))
        self.radioButton_sleep.setText(QCoreApplication.translate("SelectionStep", u"Analyse spectral power for sleep stages and/or cycles (below)", None))
        self.label_5.setText(QCoreApplication.translate("SelectionStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep Stage Selection</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("SelectionStep", u"The spectral power is analysed per sleep stage.  Select the stages to include in the analysis.", None))
#if QT_CONFIG(tooltip)
        self.unscored_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA on signal unscored.  PSG recording without sleep staging will be marked \"unscored\".", None))
#endif // QT_CONFIG(tooltip)
        self.unscored_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Unscored", None))
#if QT_CONFIG(tooltip)
        self.n1_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA on signal scored N1.", None))
#endif // QT_CONFIG(tooltip)
        self.n1_checkBox.setText(QCoreApplication.translate("SelectionStep", u"N1", None))
#if QT_CONFIG(tooltip)
        self.r_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA on signal scored R (rem).", None))
#endif // QT_CONFIG(tooltip)
        self.r_checkBox.setText(QCoreApplication.translate("SelectionStep", u"R", None))
#if QT_CONFIG(tooltip)
        self.w_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA on signal scored awake.", None))
#endif // QT_CONFIG(tooltip)
        self.w_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Wake", None))
#if QT_CONFIG(tooltip)
        self.n3_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA on signal scored N3.", None))
#endif // QT_CONFIG(tooltip)
        self.n3_checkBox.setText(QCoreApplication.translate("SelectionStep", u"N3", None))
#if QT_CONFIG(tooltip)
        self.n2_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA on signal scored N2.", None))
#endif // QT_CONFIG(tooltip)
        self.n2_checkBox.setText(QCoreApplication.translate("SelectionStep", u"N2", None))
#if QT_CONFIG(tooltip)
        self.s4_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA on signal scored Stage 4.", None))
#endif // QT_CONFIG(tooltip)
        self.s4_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Stage 4", None))
        self.nrem_checkBox.setText(QCoreApplication.translate("SelectionStep", u"NREM", None))
        self.label_4.setText(QCoreApplication.translate("SelectionStep", u"<html><head/><body><p><span style=\" font-weight:600;\">Sleep Period Selection</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("SelectionStep", u"To perform the analysis on specific section of the recording.", None))
#if QT_CONFIG(tooltip)
        self.in_cycle_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to perform the PSA only on the signal included in the sleep cycles i.e. from sleep onset to the last asleep stage.", None))
#endif // QT_CONFIG(tooltip)
        self.in_cycle_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Analyse power in sleep cycle only", None))
#if QT_CONFIG(tooltip)
        self.excl_nremp_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to exclude NREM periods from the Power Spectral Analysis.", None))
#endif // QT_CONFIG(tooltip)
        self.excl_nremp_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Exclude NREM Periods", None))
#if QT_CONFIG(tooltip)
        self.excl_remp_checkBox.setToolTip(QCoreApplication.translate("SelectionStep", u"Check to exclude REM periods from the Power Spectral Analysis.", None))
#endif // QT_CONFIG(tooltip)
        self.excl_remp_checkBox.setText(QCoreApplication.translate("SelectionStep", u"Exclude REM Periods", None))
        self.textEdit.setHtml(QCoreApplication.translate("SelectionStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To analyse only the signal included in the sleep cycles.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">I.e. from sleep onset to the last asleep stage.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Useful to analyse complete sleep cycles on"
                        "ly (ensure incomplete cycles are excluded in the Common Settings for Sleep Cycles in the tool\u2019s introduction step).</p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("SelectionStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To exclude sleep periods from the spectral analysis.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Useful to analyse NREM stages included in NREM periods only (not in REM periods). In this case, please check \u201cExclude REM periods\u201d.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-ri"
                        "ght:0px; -qt-block-indent:0; text-indent:0px;\">The same approach can be applied to NREM periods.</p></body></html>", None))
    # retranslateUi


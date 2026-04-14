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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_OutputFileStep(object):
    def setupUi(self, OutputFileStep):
        if not OutputFileStep.objectName():
            OutputFileStep.setObjectName(u"OutputFileStep")
        OutputFileStep.resize(990, 603)
        self.verticalLayout = QVBoxLayout(OutputFileStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_16 = QLabel(OutputFileStep)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout.addWidget(self.label_16)

        self.label_15 = QLabel(OutputFileStep)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout.addWidget(self.label_15)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_6 = QLabel(OutputFileStep)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_2 = QLabel(OutputFileStep)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(OutputFileStep)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(65, 0))

        self.horizontalLayout.addWidget(self.label)

        self.tsv_file_lineEdit = QLineEdit(OutputFileStep)
        self.tsv_file_lineEdit.setObjectName(u"tsv_file_lineEdit")
        self.tsv_file_lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.tsv_file_lineEdit)

        self.choose_pushButton = QPushButton(OutputFileStep)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.horizontalLayout.addWidget(self.choose_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_5 = QLabel(OutputFileStep)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_11 = QLabel(OutputFileStep)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.label_13 = QLabel(OutputFileStep)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout.addWidget(self.label_13)

        self.label_14 = QLabel(OutputFileStep)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_7 = QLabel(OutputFileStep)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.label_3 = QLabel(OutputFileStep)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(OutputFileStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(65, 0))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.Hyp_suffix_lineEdit = QLineEdit(OutputFileStep)
        self.Hyp_suffix_lineEdit.setObjectName(u"Hyp_suffix_lineEdit")
        self.Hyp_suffix_lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.Hyp_suffix_lineEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_9 = QLabel(OutputFileStep)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.label_8 = QLabel(OutputFileStep)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.label_10 = QLabel(OutputFileStep)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.label_12 = QLabel(OutputFileStep)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout.addWidget(self.label_12)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(OutputFileStep)
        self.choose_pushButton.clicked.connect(OutputFileStep.choose_slot1)

        QMetaObject.connectSlotsByName(OutputFileStep)
    # setupUi

    def retranslateUi(self, OutputFileStep):
        OutputFileStep.setWindowTitle("")
        OutputFileStep.setStyleSheet(QCoreApplication.translate("OutputFileStep", u"font: 12pt \"Roboto\";", None))
        self.label_16.setText(QCoreApplication.translate("OutputFileStep", u"<html><head/><body><p><span style=\" font-weight:700;\">Outputs</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("OutputFileStep", u"Four outputs can be generated:", None))
        self.label_6.setText(QCoreApplication.translate("OutputFileStep", u"<html><head/><body><p><span style=\" font-weight:700;\">1- Cohort-level report </span>(.tsv)</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("OutputFileStep", u"Lists the start time and duration (s) of each NREM and REM period across all recordings.", None))
        self.label.setText(QCoreApplication.translate("OutputFileStep", u"Filename", None))
        self.tsv_file_lineEdit.setText("")
        self.tsv_file_lineEdit.setPlaceholderText(QCoreApplication.translate("OutputFileStep", u"To save cycles for the cohort...", None))
        self.choose_pushButton.setText(QCoreApplication.translate("OutputFileStep", u"Choose", None))
        self.label_5.setText(QCoreApplication.translate("OutputFileStep", u"* The cycles are appended at the end of the file if it exists. ", None))
        self.label_11.setText(QCoreApplication.translate("OutputFileStep", u"<html><head/><body><p><span style=\" font-weight:700;\">2- Sleep stages and periods</span> (.tsv):</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("OutputFileStep", u"Text file containing the sleep stages and NREM/REM periods for each recording is generated automatically. ", None))
        self.label_14.setText(QCoreApplication.translate("OutputFileStep", u"It is saved in the same folder as the input PSG file and named after it, with the suffix \"_stage_cycle.tsv\".", None))
        self.label_7.setText(QCoreApplication.translate("OutputFileStep", u"<html><head/><body><p><span style=\" font-weight:700;\">3- Hypnogram image </span>(.pdf)</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("OutputFileStep", u"Image file where the hypnogram with sleep cycles of each recording is saved.", None))
        self.label_4.setText(QCoreApplication.translate("OutputFileStep", u"Suffix", None))
        self.Hyp_suffix_lineEdit.setPlaceholderText(QCoreApplication.translate("OutputFileStep", u"Suffix to add to the file saved along the recording (ex _Hyp.pdf).", None))
        self.label_9.setText(QCoreApplication.translate("OutputFileStep", u"* If no extension is specified in the filename, the .pdf extension is added automatically.  PNG is also supported.", None))
        self.label_8.setText(QCoreApplication.translate("OutputFileStep", u"<html><head/><body><p><span style=\" font-weight:700;\">4- Log Files </span>(.txt)</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("OutputFileStep", u"A log file including warnings encountered during sleep cycle delimitation is generated automatically. ", None))
        self.label_12.setText(QCoreApplication.translate("OutputFileStep", u"It is saved in the same folder as the input PSG file and named after it, with the suffix \"_Cycle_WARNING.txt\".", None))
    # retranslateUi


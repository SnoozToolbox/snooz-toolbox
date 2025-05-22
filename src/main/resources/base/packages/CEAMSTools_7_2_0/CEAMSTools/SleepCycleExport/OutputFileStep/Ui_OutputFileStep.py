# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file ''
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
        OutputFileStep.resize(754, 697)
        self.verticalLayout = QVBoxLayout(OutputFileStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(OutputFileStep)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(OutputFileStep)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.tsv_file_lineEdit = QLineEdit(OutputFileStep)
        self.tsv_file_lineEdit.setObjectName(u"tsv_file_lineEdit")
        self.tsv_file_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.tsv_file_lineEdit)

        self.choose_pushButton = QPushButton(OutputFileStep)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.horizontalLayout.addWidget(self.choose_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_5 = QLabel(OutputFileStep)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_3 = QLabel(OutputFileStep)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(OutputFileStep)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.Hyp_suffix_lineEdit = QLineEdit(OutputFileStep)
        self.Hyp_suffix_lineEdit.setObjectName(u"Hyp_suffix_lineEdit")
        self.Hyp_suffix_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.Hyp_suffix_lineEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 555, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(OutputFileStep)
        self.choose_pushButton.clicked.connect(OutputFileStep.choose_slot1)

        QMetaObject.connectSlotsByName(OutputFileStep)
    # setupUi

    def retranslateUi(self, OutputFileStep):
        OutputFileStep.setWindowTitle("")
        OutputFileStep.setStyleSheet(QCoreApplication.translate("OutputFileStep", u"font: 12pt \"Roboto\";", None))
        self.label_2.setText(QCoreApplication.translate("OutputFileStep", u"TSV file to save the start and duration (s) of each NREM and REM period.", None))
        self.label.setText(QCoreApplication.translate("OutputFileStep", u"Filename", None))
        self.tsv_file_lineEdit.setText("")
        self.tsv_file_lineEdit.setPlaceholderText(QCoreApplication.translate("OutputFileStep", u"To save cycles for the cohort...", None))
        self.choose_pushButton.setText(QCoreApplication.translate("OutputFileStep", u"Choose", None))
        self.label_5.setText(QCoreApplication.translate("OutputFileStep", u"* The cycles are appended at the end of the file it exists. ", None))
        self.label_3.setText(QCoreApplication.translate("OutputFileStep", u"Hypnogram (PNG) of each recording", None))
        self.label_4.setText(QCoreApplication.translate("OutputFileStep", u"Suffix", None))
        self.Hyp_suffix_lineEdit.setPlaceholderText(QCoreApplication.translate("OutputFileStep", u"Suffix to add to the file saved along the recording (ex _Hyp.pdf).", None))
    # retranslateUi


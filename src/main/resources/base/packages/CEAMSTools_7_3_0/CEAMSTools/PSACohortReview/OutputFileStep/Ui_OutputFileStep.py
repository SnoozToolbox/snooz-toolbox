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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_OutputFileStep(object):
    def setupUi(self, OutputFileStep):
        if not OutputFileStep.objectName():
            OutputFileStep.setObjectName(u"OutputFileStep")
        OutputFileStep.resize(842, 732)
        self.verticalLayout = QVBoxLayout(OutputFileStep)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(OutputFileStep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(350, 0))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.export_raw_checkBox = QCheckBox(OutputFileStep)
        self.export_raw_checkBox.setObjectName(u"export_raw_checkBox")
        self.export_raw_checkBox.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.export_raw_checkBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(OutputFileStep)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(350, 0))
        self.label_8.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.label_8)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.export_transpose_checkBox = QCheckBox(OutputFileStep)
        self.export_transpose_checkBox.setObjectName(u"export_transpose_checkBox")
        self.export_transpose_checkBox.setMaximumSize(QSize(16777215, 16777215))
        self.export_transpose_checkBox.setChecked(True)

        self.verticalLayout.addWidget(self.export_transpose_checkBox)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_4 = QLabel(OutputFileStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 20))

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.textEdit = QTextEdit(OutputFileStep)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 200))
        self.textEdit.setMaximumSize(QSize(16777215, 250))
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_4.addWidget(self.textEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(OutputFileStep)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.label)

        self.activity_comboBox = QComboBox(OutputFileStep)
        self.activity_comboBox.setObjectName(u"activity_comboBox")
        self.activity_comboBox.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.activity_comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(OutputFileStep)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 2)

        self.filename_lineEdit = QLineEdit(OutputFileStep)
        self.filename_lineEdit.setObjectName(u"filename_lineEdit")
        self.filename_lineEdit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.filename_lineEdit, 1, 0, 1, 1)

        self.choose_pushButton = QPushButton(OutputFileStep)
        self.choose_pushButton.setObjectName(u"choose_pushButton")
        self.choose_pushButton.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.choose_pushButton, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 12, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.retranslateUi(OutputFileStep)
        self.choose_pushButton.clicked.connect(OutputFileStep.choose_button_slot)
        self.export_transpose_checkBox.clicked.connect(OutputFileStep.export_transposed_checkbox_slot)

        QMetaObject.connectSlotsByName(OutputFileStep)
    # setupUi

    def retranslateUi(self, OutputFileStep):
        OutputFileStep.setWindowTitle("")
        OutputFileStep.setStyleSheet(QCoreApplication.translate("OutputFileStep", u"font: 12pt \"Roboto\";", None))
        self.label_3.setText(QCoreApplication.translate("OutputFileStep", u"This tool can be used to clean the EEG Spectral report.", None))
#if QT_CONFIG(tooltip)
        self.export_raw_checkBox.setToolTip(QCoreApplication.translate("OutputFileStep", u"Check to export PSA activity of selected channels only (same format as the input PSA file).", None))
#endif // QT_CONFIG(tooltip)
        self.export_raw_checkBox.setText(QCoreApplication.translate("OutputFileStep", u"Export the clean EEG Spectral report", None))
        self.label_8.setText(QCoreApplication.translate("OutputFileStep", u"This tool can be used to transpose the EEG Spectral report.", None))
#if QT_CONFIG(tooltip)
        self.export_transpose_checkBox.setToolTip(QCoreApplication.translate("OutputFileStep", u"Check to export the transposed PSA file. The format is one sujet per row and the selected channels (including ROIs) and frequency bands are packed as additional columns. ", None))
#endif // QT_CONFIG(tooltip)
        self.export_transpose_checkBox.setText(QCoreApplication.translate("OutputFileStep", u"Export transposed EEG Spectral report", None))
        self.label_4.setText(QCoreApplication.translate("OutputFileStep", u"When the EEG spectral power is computed per frequency band and sleep stage :", None))
        self.textEdit.setHtml(QCoreApplication.translate("OutputFileStep", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select<span style=\" font-weight:700;\"> Total </span>to output the average through the whole recording.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select <span style=\" font-weight:700;\">Distribution per clock hour</span> to output the average power for each real clock hour.</p>\n"
"<p style=\" margin-top:0px; margi"
                        "n-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select <span style=\" font-weight:700;\">Distribution per hour spent in each sleep stage </span>to output the average power for each stage hour.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select <span style=\" font-weight:700;\">Distribution per sleep cycle </span>to output the average power per sleep cycle</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When the PSA activity is computed per frequency band and annotation : </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select <span style=\" font-weight:700;\">Distributio"
                        "n per annotation</span> to output the average per annotation. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">No cycle or hour information here.</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("OutputFileStep", u"Activity variables exported in the transposed report", None))
        self.label_2.setText(QCoreApplication.translate("OutputFileStep", u"Define the filename to save the exported files (the sufix _clean.tsv or _transposed.tsv will be added to the filename)", None))
        self.filename_lineEdit.setInputMask("")
        self.filename_lineEdit.setText("")
        self.filename_lineEdit.setPlaceholderText(QCoreApplication.translate("OutputFileStep", u"Choose a directory to save file ...", None))
        self.choose_pushButton.setText(QCoreApplication.translate("OutputFileStep", u"Choose", None))
    # retranslateUi


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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_OutputFileStep(object):
    def setupUi(self, OutputFileStep):
        if not OutputFileStep.objectName():
            OutputFileStep.setObjectName(u"OutputFileStep")
        OutputFileStep.resize(980, 642)
        OutputFileStep.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_3 = QHBoxLayout(OutputFileStep)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(OutputFileStep)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(350, 0))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.label_3)

        self.export_raw_checkBox = QCheckBox(OutputFileStep)
        self.export_raw_checkBox.setObjectName(u"export_raw_checkBox")
        self.export_raw_checkBox.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.export_raw_checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(40, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(OutputFileStep)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(350, 0))
        self.label_8.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.label_8)

        self.export_transpose_checkBox = QCheckBox(OutputFileStep)
        self.export_transpose_checkBox.setObjectName(u"export_transpose_checkBox")
        self.export_transpose_checkBox.setMaximumSize(QSize(16777215, 16777215))
        self.export_transpose_checkBox.setChecked(True)

        self.horizontalLayout_2.addWidget(self.export_transpose_checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(OutputFileStep)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 20))

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 2)

        self.label_7 = QLabel(OutputFileStep)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 20))

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 2)

        self.label = QLabel(OutputFileStep)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.activity_comboBox = QComboBox(OutputFileStep)
        self.activity_comboBox.setObjectName(u"activity_comboBox")
        self.activity_comboBox.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.activity_comboBox, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

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

        self.label_4 = QLabel(OutputFileStep)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(OutputFileStep)
        self.choose_pushButton.clicked.connect(OutputFileStep.choose_button_slot)
        self.export_transpose_checkBox.clicked.connect(OutputFileStep.export_transposed_checkbox_slot)

        QMetaObject.connectSlotsByName(OutputFileStep)
    # setupUi

    def retranslateUi(self, OutputFileStep):
        OutputFileStep.setWindowTitle("")
        OutputFileStep.setStyleSheet(QCoreApplication.translate("OutputFileStep", u"font: 12pt \"Roboto\";", None))
        self.label_3.setText(QCoreApplication.translate("OutputFileStep", u"This tool can be used to clean the detailed events cohort report.", None))
#if QT_CONFIG(tooltip)
        self.export_raw_checkBox.setToolTip(QCoreApplication.translate("OutputFileStep", u"Check to export PSA activity of selected channels only (same format as the input PSA file).", None))
#endif // QT_CONFIG(tooltip)
        self.export_raw_checkBox.setText(QCoreApplication.translate("OutputFileStep", u"Export clean report", None))
        self.label_8.setText(QCoreApplication.translate("OutputFileStep", u"This tool can be used to transpose the detailed events cohort report.", None))
#if QT_CONFIG(tooltip)
        self.export_transpose_checkBox.setToolTip(QCoreApplication.translate("OutputFileStep", u"Check to export the transposed PSA file. The format is one sujet per row and the selected channels (including ROIs) and frequency bands are packed as additional columns. ", None))
#endif // QT_CONFIG(tooltip)
        self.export_transpose_checkBox.setText(QCoreApplication.translate("OutputFileStep", u"Export transposed report", None))
        self.label_5.setText(QCoreApplication.translate("OutputFileStep", u" - Select \"Total\" to output the average through the whole recording.", None))
        self.label_7.setText(QCoreApplication.translate("OutputFileStep", u" - Select \"Distribution per sleep cycle\" to output the average per sleep cycle, from sleep cycle 1 to 9.  The start point is the sleep onset.", None))
        self.label.setText(QCoreApplication.translate("OutputFileStep", u"Activity variables exported in the transposed PSA file", None))
        self.label_2.setText(QCoreApplication.translate("OutputFileStep", u"Define the filename to save the exported files (the sufix _clean.tsv or _transposed.tsv will be added to the filename)", None))
        self.filename_lineEdit.setInputMask("")
        self.filename_lineEdit.setText("")
        self.filename_lineEdit.setPlaceholderText(QCoreApplication.translate("OutputFileStep", u"Define the file to save the report in ...", None))
        self.choose_pushButton.setText(QCoreApplication.translate("OutputFileStep", u"Choose", None))
        self.label_4.setText(QCoreApplication.translate("OutputFileStep", u"* Warning : the output file is overwritten.  To append different cohort reports: add the cohort reports in the step \"1 - Input Files\".", None))
    # retranslateUi


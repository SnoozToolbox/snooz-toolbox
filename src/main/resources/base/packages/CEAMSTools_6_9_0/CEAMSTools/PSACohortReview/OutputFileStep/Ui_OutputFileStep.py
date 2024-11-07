# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_OutputFileStep.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_OutputFileStep(object):
    def setupUi(self, OutputFileStep):
        if not OutputFileStep.objectName():
            OutputFileStep.setObjectName(u"OutputFileStep")
        OutputFileStep.resize(726, 642)
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

        self.verticalSpacer = QSpacerItem(40, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

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

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.activity_comboBox = QComboBox(OutputFileStep)
        self.activity_comboBox.setObjectName(u"activity_comboBox")
        self.activity_comboBox.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.activity_comboBox, 6, 1, 1, 1)

        self.label_5 = QLabel(OutputFileStep)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 20))

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 2)

        self.label_9 = QLabel(OutputFileStep)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 2)

        self.label_7 = QLabel(OutputFileStep)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 20))

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 2)

        self.label_6 = QLabel(OutputFileStep)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 20))

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 2)

        self.label = QLabel(OutputFileStep)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)

        self.label_4 = QLabel(OutputFileStep)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 20))

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)

        self.label_10 = QLabel(OutputFileStep)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

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

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

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
        self.label_3.setText(QCoreApplication.translate("OutputFileStep", u"The PSA Cohort Review tool can be used to clean the PSA file.", None))
#if QT_CONFIG(tooltip)
        self.export_raw_checkBox.setToolTip(QCoreApplication.translate("OutputFileStep", u"Check to export PSA activity of selected channels only (same format as the input PSA file).", None))
#endif // QT_CONFIG(tooltip)
        self.export_raw_checkBox.setText(QCoreApplication.translate("OutputFileStep", u"Export PSA file clean", None))
        self.label_8.setText(QCoreApplication.translate("OutputFileStep", u"The PSA Cohort Review tool can be used to transpose the PSA file.", None))
#if QT_CONFIG(tooltip)
        self.export_transpose_checkBox.setToolTip(QCoreApplication.translate("OutputFileStep", u"Check to export the transposed PSA file. The format is one sujet per row and the selected channels (including ROIs) and frequency bands are packed as additional columns. ", None))
#endif // QT_CONFIG(tooltip)
        self.export_transpose_checkBox.setText(QCoreApplication.translate("OutputFileStep", u"Export transposed PSA file", None))
        self.label_5.setText(QCoreApplication.translate("OutputFileStep", u" - Select \"Total\" to output the average through the whole recording.", None))
        self.label_9.setText(QCoreApplication.translate("OutputFileStep", u"When the PSA activity is computed per frequency band and annotation : ", None))
        self.label_7.setText(QCoreApplication.translate("OutputFileStep", u" - Select \"Distribution per sleep cycle\" to output the average per sleep cycle, from sleep cycle 1 to 6.  The start point is the sleep onset.", None))
        self.label_6.setText(QCoreApplication.translate("OutputFileStep", u" - Select \"Distribution per hour\" to output the average per real clock hour, from hour 1 to 12.  The start point is the sleep onset.", None))
        self.label.setText(QCoreApplication.translate("OutputFileStep", u"Activity variables exported in the transposed PSA file", None))
        self.label_4.setText(QCoreApplication.translate("OutputFileStep", u"When the PSA activity is computed per frequency band and sleep stage :", None))
        self.label_10.setText(QCoreApplication.translate("OutputFileStep", u" - Select \"Distribution per annotation\" to output the average per annotation. No cycle or hour information here.", None))
        self.label_2.setText(QCoreApplication.translate("OutputFileStep", u"Define the filename to save the exported files (the sufix _clean.tsv or _transposed.tsv will be added to the filename)", None))
        self.filename_lineEdit.setInputMask("")
        self.filename_lineEdit.setText("")
        self.filename_lineEdit.setPlaceholderText(QCoreApplication.translate("OutputFileStep", u"Choose a directory to save file ...", None))
        self.choose_pushButton.setText(QCoreApplication.translate("OutputFileStep", u"Choose", None))
    # retranslateUi


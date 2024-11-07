# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SSWCOutputFiles.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_SSWCOutputFiles(object):
    def setupUi(self, SSWCOutputFiles):
        if not SSWCOutputFiles.objectName():
            SSWCOutputFiles.setObjectName(u"SSWCOutputFiles")
        SSWCOutputFiles.resize(1050, 707)
        SSWCOutputFiles.setInputMethodHints(Qt.ImhNone)
        self.verticalLayout = QVBoxLayout(SSWCOutputFiles)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_10 = QLabel(SSWCOutputFiles)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)

        self.verticalLayout.addWidget(self.label_10)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.choose_pushButton = QPushButton(SSWCOutputFiles)
        self.choose_pushButton.setObjectName(u"choose_pushButton")
        self.choose_pushButton.setEnabled(True)

        self.gridLayout.addWidget(self.choose_pushButton, 0, 2, 1, 1)

        self.foldername_lineEdit = QLineEdit(SSWCOutputFiles)
        self.foldername_lineEdit.setObjectName(u"foldername_lineEdit")
        self.foldername_lineEdit.setEnabled(True)
        self.foldername_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.foldername_lineEdit, 0, 1, 1, 1)

        self.label = QLabel(SSWCOutputFiles)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(SSWCOutputFiles)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_2 = QLabel(SSWCOutputFiles)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(SSWCOutputFiles)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_6 = QLabel(SSWCOutputFiles)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_5 = QLabel(SSWCOutputFiles)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_7 = QLabel(SSWCOutputFiles)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(SSWCOutputFiles)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.label_18 = QLabel(SSWCOutputFiles)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout.addWidget(self.label_18)

        self.label_17 = QLabel(SSWCOutputFiles)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout.addWidget(self.label_17)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.label_11 = QLabel(SSWCOutputFiles)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_9 = QLabel(SSWCOutputFiles)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)

        self.spinBox_n_division = QSpinBox(SSWCOutputFiles)
        self.spinBox_n_division.setObjectName(u"spinBox_n_division")

        self.horizontalLayout_2.addWidget(self.spinBox_n_division)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_16 = QLabel(SSWCOutputFiles)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout.addWidget(self.label_16)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_12 = QLabel(SSWCOutputFiles)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout.addWidget(self.label_12)

        self.label_title = QLabel(SSWCOutputFiles)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setFont(font)

        self.verticalLayout.addWidget(self.label_title)

        self.label_13 = QLabel(SSWCOutputFiles)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout.addWidget(self.label_13)

        self.label_14 = QLabel(SSWCOutputFiles)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)

        self.label_15 = QLabel(SSWCOutputFiles)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout.addWidget(self.label_15)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SSWCOutputFiles)
        self.choose_pushButton.clicked.connect(SSWCOutputFiles.on_choose)

        QMetaObject.connectSlotsByName(SSWCOutputFiles)
    # setupUi

    def retranslateUi(self, SSWCOutputFiles):
        SSWCOutputFiles.setWindowTitle(QCoreApplication.translate("SSWCOutputFiles", u"Form", None))
        SSWCOutputFiles.setStyleSheet(QCoreApplication.translate("SSWCOutputFiles", u"font: 12pt \"Roboto\";", None))
        self.label_10.setText(QCoreApplication.translate("SSWCOutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Output folder</span></p></body></html>", None))
        self.choose_pushButton.setText(QCoreApplication.translate("SSWCOutputFiles", u"Choose", None))
        self.foldername_lineEdit.setText("")
        self.foldername_lineEdit.setPlaceholderText(QCoreApplication.translate("SSWCOutputFiles", u"Choose a destination folder for the ouput files", None))
        self.label.setText(QCoreApplication.translate("SSWCOutputFiles", u"Folder name", None))
        self.label_4.setText(QCoreApplication.translate("SSWCOutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Slow wave characteristics by event level</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("SSWCOutputFiles", u"Each slow wave event is labeled with its corresponding category.", None))
        self.label_3.setText(QCoreApplication.translate("SSWCOutputFiles", u"The slow wave characteristic files are copied and saved in the output directory, with the corresponding slow wave category appended.", None))
        self.label_6.setText(QCoreApplication.translate("SSWCOutputFiles", u"There is one slow wave characteristics file per PSG recording.", None))
        self.label_5.setText(QCoreApplication.translate("SSWCOutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Slow wave characteristics by suject level</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("SSWCOutputFiles", u"A cohort report containing the averaged slow wave characteristics per category is generated.", None))
        self.label_8.setText(QCoreApplication.translate("SSWCOutputFiles", u"The slow wave characteristics are also provided per sleep cycle and segment of the night.", None))
        self.label_18.setText(QCoreApplication.translate("SSWCOutputFiles", u"For the information per sleep cycle: only valid data is considered; artifacts and unselected sleep stages for detection are excluded.", None))
        self.label_17.setText(QCoreApplication.translate("SSWCOutputFiles", u"For the information per segment of night: all data is considered for dividing the night; The time from lights off to lights on is included.", None))
        self.label_11.setText(QCoreApplication.translate("SSWCOutputFiles", u"Choose the granularity of the segment you are interested in. Select 2 to divide the night into halves, 3 for thirds, 4 for quarters, and so forth.", None))
        self.label_9.setText(QCoreApplication.translate("SSWCOutputFiles", u"Number of segments for dividing the night.", None))
        self.label_16.setText(QCoreApplication.translate("SSWCOutputFiles", u"<html><head/><body><p><span style=\" font-style:italic;\">* A description file named with the suffix &quot;_info&quot; contains the definition of each field included in the cohort report.</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("SSWCOutputFiles", u"<html><head/><body><p><span style=\" font-weight:600;\">Classification model</span></p></body></html>", None))
        self.label_title.setText(QCoreApplication.translate("SSWCOutputFiles", u"The distribution of transition frequency values for the cohort is modeled using a Gaussian mixture.", None))
        self.label_13.setText(QCoreApplication.translate("SSWCOutputFiles", u"The histogram of transition frequency values along with the resulting model is saved in the output folder.", None))
        self.label_14.setText(QCoreApplication.translate("SSWCOutputFiles", u"When the number of categories is computed automatically (not manually defined) ", None))
        self.label_15.setText(QCoreApplication.translate("SSWCOutputFiles", u"the Akaike Criterion Information (AIC) for 1 to 4 categories is also included in the picture.", None))
    # retranslateUi


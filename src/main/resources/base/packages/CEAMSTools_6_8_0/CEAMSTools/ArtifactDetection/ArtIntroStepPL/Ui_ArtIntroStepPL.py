# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ArtIntroStepPL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from . import intro_res_rc
import themes_rc

class Ui_ArtIntroStepPL(object):
    def setupUi(self, ArtIntroStepPL):
        if not ArtIntroStepPL.objectName():
            ArtIntroStepPL.setObjectName(u"ArtIntroStepPL")
        ArtIntroStepPL.resize(1099, 778)
        ArtIntroStepPL.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout_7 = QVBoxLayout(ArtIntroStepPL)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.splitter_2 = QSplitter(ArtIntroStepPL)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 170))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.AutoText)

        self.verticalLayout_6.addWidget(self.label_2)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.splitter = QSplitter(self.layoutWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.scrollArea_2 = QScrollArea(self.layoutWidget1)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1001, 180))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea_2)

        self.splitter.addWidget(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.splitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setSizeIncrement(QSize(0, 0))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.scrollArea_3 = QScrollArea(self.layoutWidget2)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setFrameShadow(QFrame.Plain)
        self.scrollArea_3.setLineWidth(0)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1001, 319))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.label_7)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_2.addWidget(self.scrollArea_3)

        self.splitter.addWidget(self.layoutWidget2)

        self.verticalLayout_6.addWidget(self.splitter)

        self.splitter_2.addWidget(self.layoutWidget)
        self.scrollArea = QScrollArea(self.splitter_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1042, 929))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/intro/2_amplitude_v2.png"))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/intro/3_burst_noise_v2.png"))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setPixmap(QPixmap(u":/intro/3b_persistent_noise.png"))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u":/intro/4_powerLine_v2.png"))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_9)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u":/intro/5_BSLVar_v2.png"))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(u":/intro/6_muscular_v2.png"))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter_2.addWidget(self.scrollArea)

        self.verticalLayout_7.addWidget(self.splitter_2)


        self.retranslateUi(ArtIntroStepPL)

        QMetaObject.connectSlotsByName(ArtIntroStepPL)
    # setupUi

    def retranslateUi(self, ArtIntroStepPL):
        ArtIntroStepPL.setWindowTitle(QCoreApplication.translate("ArtIntroStepPL", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("ArtIntroStepPL", u"<html><head/><body><p><span style=\" font-weight:600;\">Artifact Detector</span></p><p>This tool <span style=\" font-weight:600;\">detects artifacts</span> from PSG files.</p><p>Detection is performed on the entire recording. <br/>However, you can select specific sleep stages to potentially establish a cleaner baseline <br/>for the algorithms using a 3-component Gaussian Mixture Model (GMM). <br/>It is recommended to select sleep stages where the signal is typically cleaner (i.e. N1, N2, N3, R). </p><p>While sleep stages are mandatory for sleep recordings, <br/>artifact detection can be run on any EEG recording if &quot;Unscored&quot; is selected for the sleep stages.</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("ArtIntroStepPL", u"<html><head/><body><p><span style=\" font-weight:600;\">Types of artifacts</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("ArtIntroStepPL", u"-> Flatline : Segments of low power, flatlined signal.\n"
"-> High Frequency burst : Segments with a burst of high frequency power (>25 Hz).\n"
"-> Persistent Noise : Segments with high frequency noise (>25 Hz).\n"
"-> Power Line Contamination : Segments corrupted by 50 or 60 Hz power.\n"
"-> Baseline Variation (Breathing, Sweat) : Segments with high power in the low frequency band (<0.4 Hz).\n"
"-> Muscle artifact : Segments with burst of activity in the frequency band 20.25-32 Hz.", None))
        self.label_4.setText(QCoreApplication.translate("ArtIntroStepPL", u"<html><head/><body><p><span style=\" font-weight:600;\">Output</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("ArtIntroStepPL", u"The detected artifacts are added in the input file as new events (i.e. .tsv for edf, .sts for Stellate and .ent for NATUS).\n"
"If the input file already contains the group and name of the new events to be added, they will first be deleted. \n"
"If you detect artifact on an EDF file without accessory file, the accessory (.tsv) file will be automatically generated.\n"
"\n"
"The output is a TSV (Tab Separated Values) file. A new row is added for every artifact detection.\n"
"The channel label is concatened to the artifact name with a @@ (EDFbrowser compatible).\n"
"The columns of the file are as follows:\n"
"-> 1. group : The group of the event is artifact.\n"
"-> 2. name : The name of the event. Ex. flatline.\n"
"-> 3. start_sec : The onset of the event in second. \n"
"-> 4. duration_sec : The duration of the event in second.\n"
"-> 5. channels : The list of channels on which the event occurs.", None))
        self.label_6.setText("")
        self.label_8.setText("")
        self.label_5.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
    # retranslateUi


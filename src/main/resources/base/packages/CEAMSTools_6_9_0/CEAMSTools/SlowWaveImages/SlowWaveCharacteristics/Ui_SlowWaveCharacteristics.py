# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SlowWaveCharacteristics.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_SlowWaveCharacteristics(object):
    def setupUi(self, SlowWaveCharacteristics):
        if not SlowWaveCharacteristics.objectName():
            SlowWaveCharacteristics.setObjectName(u"SlowWaveCharacteristics")
        SlowWaveCharacteristics.resize(918, 440)
        SlowWaveCharacteristics.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(SlowWaveCharacteristics)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(SlowWaveCharacteristics)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(SlowWaveCharacteristics)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(SlowWaveCharacteristics)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(SlowWaveCharacteristics)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(400, 0))
        self.lineEdit.setMaximumSize(QSize(570, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(SlowWaveCharacteristics)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SlowWaveCharacteristics)
        self.pushButton.clicked.connect(SlowWaveCharacteristics.choose_slot)

        QMetaObject.connectSlotsByName(SlowWaveCharacteristics)
    # setupUi

    def retranslateUi(self, SlowWaveCharacteristics):
        SlowWaveCharacteristics.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("SlowWaveCharacteristics", u"<html><head/><body><p><span style=\" font-weight:600;\">Slow wave characteristics files</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("SlowWaveCharacteristics", u"The characteristics are used as references to properly align the superimposed signals of slow waves.", None))
        self.label_3.setText(QCoreApplication.translate("SlowWaveCharacteristics", u"If the slow wave category is included in the files, the information can be used to group slow wave signals in the generated pictures.", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("SlowWaveCharacteristics", u"Select the folder where the slow wave characteristics files are saved", None))
        self.pushButton.setText(QCoreApplication.translate("SlowWaveCharacteristics", u"Choose", None))
    # retranslateUi


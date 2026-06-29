# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DetectionSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QHBoxLayout,
    QLabel, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_DetectionSettings(object):
    def setupUi(self, DetectionSettings):
        if not DetectionSettings.objectName():
            DetectionSettings.setObjectName(u"DetectionSettings")
        DetectionSettings.resize(836, 580)
        DetectionSettings.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(DetectionSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DetectionSettings)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(DetectionSettings)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_pic = QLabel(DetectionSettings)
        self.label_pic.setObjectName(u"label_pic")
        self.label_pic.setMaximumSize(QSize(16777215, 330))

        self.horizontalLayout_2.addWidget(self.label_pic)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_6 = QLabel(DetectionSettings)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(DetectionSettings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.radioButton_20s = QRadioButton(DetectionSettings)
        self.buttonGroup_2 = QButtonGroup(DetectionSettings)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_20s)
        self.radioButton_20s.setObjectName(u"radioButton_20s")
        self.radioButton_20s.setMinimumSize(QSize(115, 0))

        self.gridLayout.addWidget(self.radioButton_20s, 1, 3, 1, 1)

        self.radioButton_3perc = QRadioButton(DetectionSettings)
        self.buttonGroup = QButtonGroup(DetectionSettings)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_3perc)
        self.radioButton_3perc.setObjectName(u"radioButton_3perc")
        self.radioButton_3perc.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_3perc, 0, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(118, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_10, 1, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 0, 4, 1, 1)

        self.radioButton_hold_5s = QRadioButton(DetectionSettings)
        self.buttonGroup_3 = QButtonGroup(DetectionSettings)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton_hold_5s)
        self.radioButton_hold_5s.setObjectName(u"radioButton_hold_5s")

        self.gridLayout.addWidget(self.radioButton_hold_5s, 2, 3, 1, 1)

        self.label_4 = QLabel(DetectionSettings)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)

        self.radioButton_4perc = QRadioButton(DetectionSettings)
        self.buttonGroup.addButton(self.radioButton_4perc)
        self.radioButton_4perc.setObjectName(u"radioButton_4perc")

        self.gridLayout.addWidget(self.radioButton_4perc, 0, 3, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(108, 18, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_11, 2, 4, 1, 1)

        self.label_17 = QLabel(DetectionSettings)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 1, 1, 1, 1)

        self.radioButton_180s = QRadioButton(DetectionSettings)
        self.buttonGroup_2.addButton(self.radioButton_180s)
        self.radioButton_180s.setObjectName(u"radioButton_180s")
        self.radioButton_180s.setMinimumSize(QSize(115, 0))
        self.radioButton_180s.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_180s, 1, 2, 1, 1)

        self.radioButton_hold_10s = QRadioButton(DetectionSettings)
        self.buttonGroup_3.addButton(self.radioButton_hold_10s)
        self.radioButton_hold_10s.setObjectName(u"radioButton_hold_10s")
        self.radioButton_hold_10s.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_hold_10s, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label_7 = QLabel(DetectionSettings)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.verticalSpacer_6 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.label_10 = QLabel(DetectionSettings)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.label_9 = QLabel(DetectionSettings)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.label_12 = QLabel(DetectionSettings)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout.addWidget(self.label_12)

        self.label_11 = QLabel(DetectionSettings)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.label_13 = QLabel(DetectionSettings)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout.addWidget(self.label_13)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_8 = QLabel(DetectionSettings)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.label_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(DetectionSettings)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_7 = QSpacerItem(20, 139, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)


        self.retranslateUi(DetectionSettings)

        QMetaObject.connectSlotsByName(DetectionSettings)
    # setupUi

    def retranslateUi(self, DetectionSettings):
        DetectionSettings.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("DetectionSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Oxygen Desaturation Crtieria</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("DetectionSettings", u"The oximeter measures the percentage of oxygen in the blood.", None))
        self.label_pic.setText("")
        self.label_6.setText(QCoreApplication.translate("DetectionSettings", u"Define the criteria for detecting a desaturation.", None))
        self.label_2.setText(QCoreApplication.translate("DetectionSettings", u"The oxygen level drop", None))
        self.radioButton_20s.setText(QCoreApplication.translate("DetectionSettings", u"20 sec [CEAMS]", None))
        self.radioButton_3perc.setText(QCoreApplication.translate("DetectionSettings", u"3 %", None))
        self.radioButton_hold_5s.setText(QCoreApplication.translate("DetectionSettings", u"5 sec [1, CEAMS]", None))
        self.label_4.setText(QCoreApplication.translate("DetectionSettings", u"Minimum desaturation time", None))
        self.radioButton_4perc.setText(QCoreApplication.translate("DetectionSettings", u"4 %", None))
        self.label_17.setText(QCoreApplication.translate("DetectionSettings", u"Maximum desaturation time", None))
        self.radioButton_180s.setText(QCoreApplication.translate("DetectionSettings", u"180 sec [1]", None))
        self.radioButton_hold_10s.setText(QCoreApplication.translate("DetectionSettings", u"10 sec [1]", None))
        self.label_7.setText(QCoreApplication.translate("DetectionSettings", u"The oximeter signal is analyzed for desaturations during the sleep period (from sleep onset to final awakening).", None))
        self.label_10.setText(QCoreApplication.translate("DetectionSettings", u"<html><head/><body><p><span style=\" font-weight:700;\">Recovery criteria</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("DetectionSettings", u"The minimum duration is 3 sec.", None))
        self.label_12.setText(QCoreApplication.translate("DetectionSettings", u"The maximum duration is the maximum between\n"
"   120 sec and 2 X the desaturation event before the recovery.", None))
        self.label_11.setText(QCoreApplication.translate("DetectionSettings", u"The minimum amplitude is 2%", None))
        self.label_13.setText(QCoreApplication.translate("DetectionSettings", u"The minimum slope is 0.05 %/s", None))
        self.label_8.setText(QCoreApplication.translate("DetectionSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">References</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("DetectionSettings", u"[1] Karhu, T., Lepp\u00e4nen, T., T\u00f6yr\u00e4s, J., Oksenberg, A., Myllymaa, S., & Nikkonen, S. (2022). ABOSA \u2013 Freely available automatic blood oxygen saturation signal analysis software\u202f: Structure and validation. Computer Methods and Programs in Biomedicine, 226, 107120. https://doi.org/10.1016/j.cmpb.2022.107120\n"
"", None))
    # retranslateUi


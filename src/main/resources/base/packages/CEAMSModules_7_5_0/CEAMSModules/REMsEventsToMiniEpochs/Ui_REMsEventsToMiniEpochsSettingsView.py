# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_REMsEventsToMiniEpochsSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_REMsEventsToMiniEpochsSettingsView(object):
    def setupUi(self, REMsEventsToMiniEpochsSettingsView):
        if not REMsEventsToMiniEpochsSettingsView.objectName():
            REMsEventsToMiniEpochsSettingsView.setObjectName(u"REMsEventsToMiniEpochsSettingsView")
        REMsEventsToMiniEpochsSettingsView.resize(838, 425)
        self.verticalLayout = QVBoxLayout(REMsEventsToMiniEpochsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(REMsEventsToMiniEpochsSettingsView)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(REMsEventsToMiniEpochsSettingsView)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(REMsEventsToMiniEpochsSettingsView)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_group = QLineEdit(REMsEventsToMiniEpochsSettingsView)
        self.lineEdit_group.setObjectName(u"lineEdit_group")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_group)

        self.label_2 = QLabel(REMsEventsToMiniEpochsSettingsView)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_name_Phasic = QLineEdit(REMsEventsToMiniEpochsSettingsView)
        self.lineEdit_name_Phasic.setObjectName(u"lineEdit_name_Phasic")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_name_Phasic)

        self.label_3 = QLabel(REMsEventsToMiniEpochsSettingsView)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_name_Tonic = QLineEdit(REMsEventsToMiniEpochsSettingsView)
        self.lineEdit_name_Tonic.setObjectName(u"lineEdit_name_Tonic")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_name_Tonic)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 316, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(REMsEventsToMiniEpochsSettingsView)

        QMetaObject.connectSlotsByName(REMsEventsToMiniEpochsSettingsView)
    # setupUi

    def retranslateUi(self, REMsEventsToMiniEpochsSettingsView):
        REMsEventsToMiniEpochsSettingsView.setWindowTitle(QCoreApplication.translate("REMsEventsToMiniEpochsSettingsView", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("REMsEventsToMiniEpochsSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Define the labels of the mini-epochs for Rapid Eye Movements (REM).</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("REMsEventsToMiniEpochsSettingsView", u"Each event belongs to a group and is labeled by a name. ", None))
        self.label.setText(QCoreApplication.translate("REMsEventsToMiniEpochsSettingsView", u"Group for the mini-epoch", None))
        self.label_2.setText(QCoreApplication.translate("REMsEventsToMiniEpochsSettingsView", u"Name for the Phasic mini-epoch", None))
        self.label_3.setText(QCoreApplication.translate("REMsEventsToMiniEpochsSettingsView", u"Name for the Tonic mini-epoch", None))
    # retranslateUi


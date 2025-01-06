# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_PSGWriterSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_PSGWriterSettingsView(object):
    def setupUi(self, PSGWriterSettingsView):
        if not PSGWriterSettingsView.objectName():
            PSGWriterSettingsView.setObjectName(u"PSGWriterSettingsView")
        PSGWriterSettingsView.resize(432, 160)
        PSGWriterSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout = QHBoxLayout(PSGWriterSettingsView)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(PSGWriterSettingsView)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_input_filename = QLineEdit(PSGWriterSettingsView)
        self.lineEdit_input_filename.setObjectName(u"lineEdit_input_filename")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_input_filename)

        self.label_2 = QLabel(PSGWriterSettingsView)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_output_filename = QLineEdit(PSGWriterSettingsView)
        self.lineEdit_output_filename.setObjectName(u"lineEdit_output_filename")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_output_filename)


        self.verticalLayout.addLayout(self.formLayout)

        self.checkBox_overwrite_events = QCheckBox(PSGWriterSettingsView)
        self.checkBox_overwrite_events.setObjectName(u"checkBox_overwrite_events")
        self.checkBox_overwrite_events.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_overwrite_events)

        self.checkBox_overwrite_signals = QCheckBox(PSGWriterSettingsView)
        self.checkBox_overwrite_signals.setObjectName(u"checkBox_overwrite_signals")

        self.verticalLayout.addWidget(self.checkBox_overwrite_signals)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(187, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(PSGWriterSettingsView)

        QMetaObject.connectSlotsByName(PSGWriterSettingsView)
    # setupUi

    def retranslateUi(self, PSGWriterSettingsView):
        PSGWriterSettingsView.setWindowTitle(QCoreApplication.translate("PSGWriterSettingsView", u"Form", None))
        self.label.setText(QCoreApplication.translate("PSGWriterSettingsView", u"input filename", None))
        self.label_2.setText(QCoreApplication.translate("PSGWriterSettingsView", u"output filename", None))
#if QT_CONFIG(tooltip)
        self.checkBox_overwrite_events.setToolTip(QCoreApplication.translate("PSGWriterSettingsView", u"Check to write new events. Events saved in the file with the same group, name, and channels as the new events will be deleted first.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_overwrite_events.setText(QCoreApplication.translate("PSGWriterSettingsView", u"Overwrite events", None))
#if QT_CONFIG(tooltip)
        self.checkBox_overwrite_signals.setToolTip(QCoreApplication.translate("PSGWriterSettingsView", u"Check to replace signals. Original signals with the same label as the new signals will be overwritten.  New labels will be ignored.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_overwrite_signals.setText(QCoreApplication.translate("PSGWriterSettingsView", u"Overwrite signals", None))
    # retranslateUi


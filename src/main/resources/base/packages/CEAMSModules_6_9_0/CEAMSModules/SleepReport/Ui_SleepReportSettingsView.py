# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/david/projects/scinodes_poc/src/main/python/plugins/SleepReport/Ui_SleepReportSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_SleepReportSettingsView(object):
    def setupUi(self, SleepReportSettingsView):
        SleepReportSettingsView.setObjectName("SleepReportSettingsView")
        SleepReportSettingsView.resize(415, 224)
        self.verticalLayout = QtWidgets.QVBoxLayout(SleepReportSettingsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(SleepReportSettingsView)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.output_file_lineedit = QtWidgets.QLineEdit(SleepReportSettingsView)
        self.output_file_lineedit.setObjectName("output_file_lineedit")
        self.horizontalLayout.addWidget(self.output_file_lineedit)
        self.choose_file_pushbutton = QtWidgets.QPushButton(SleepReportSettingsView)
        self.choose_file_pushbutton.setObjectName("choose_file_pushbutton")
        self.horizontalLayout.addWidget(self.choose_file_pushbutton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(SleepReportSettingsView)
        self.choose_file_pushbutton.clicked.connect(SleepReportSettingsView.on_choose_ouput_file)
        QtCore.QMetaObject.connectSlotsByName(SleepReportSettingsView)

    def retranslateUi(self, SleepReportSettingsView):
        _translate = QtCore.QCoreApplication.translate
        SleepReportSettingsView.setWindowTitle(_translate("SleepReportSettingsView", "Form"))
        self.label.setText(_translate("SleepReportSettingsView", "Output file"))
        self.choose_file_pushbutton.setText(_translate("SleepReportSettingsView", "Choose file"))

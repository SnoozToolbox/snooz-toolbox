# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\klacourse\Documents\NGosselin\gitRepos\ceamscarms\Stand_alone_apps\scinodes_poc\src\main\python\plugins\WindowsToSamples\Ui_WindowsToSamplesSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_WindowsToSamplesSettingsView(object):
    def setupUi(self, WindowsToSamplesSettingsView):
        WindowsToSamplesSettingsView.setObjectName("WindowsToSamplesSettingsView")
        WindowsToSamplesSettingsView.resize(185, 161)
        self.verticalLayout = QtWidgets.QVBoxLayout(WindowsToSamplesSettingsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windows_values_horizontalLayout = QtWidgets.QHBoxLayout()
        self.windows_values_horizontalLayout.setObjectName("windows_values_horizontalLayout")
        self.verticalLayout.addLayout(self.windows_values_horizontalLayout)
        self.win_step_sec_horizontalLayout = QtWidgets.QHBoxLayout()
        self.win_step_sec_horizontalLayout.setObjectName("win_step_sec_horizontalLayout")
        self.win_step_sec_label = QtWidgets.QLabel(WindowsToSamplesSettingsView)
        self.win_step_sec_label.setObjectName("win_step_sec_label")
        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_label)
        self.win_step_sec_lineedit = QtWidgets.QLineEdit(WindowsToSamplesSettingsView)
        self.win_step_sec_lineedit.setObjectName("win_step_sec_lineedit")
        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_lineedit)
        self.verticalLayout.addLayout(self.win_step_sec_horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(WindowsToSamplesSettingsView)
        QtCore.QMetaObject.connectSlotsByName(WindowsToSamplesSettingsView)

    def retranslateUi(self, WindowsToSamplesSettingsView):
        _translate = QtCore.QCoreApplication.translate
        WindowsToSamplesSettingsView.setWindowTitle(_translate("WindowsToSamplesSettingsView", "Form"))
        self.win_step_sec_label.setText(_translate("WindowsToSamplesSettingsView", "win_step_sec"))
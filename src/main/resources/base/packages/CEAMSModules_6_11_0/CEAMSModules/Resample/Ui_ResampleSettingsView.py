# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cbrain/projects/snooz-toolbox/src/main/python/plugins/Resample/Ui_ResampleSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_ResampleSettingsView(object):
    def setupUi(self, ResampleSettingsView):
        ResampleSettingsView.setObjectName("ResampleSettingsView")
        ResampleSettingsView.resize(415, 224)
        self.layoutWidget = QtWidgets.QWidget(ResampleSettingsView)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 248, 46))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.target_sample_rate_lineedit = QLineEditLive(self.layoutWidget)
        self.target_sample_rate_lineedit.setObjectName("target_sample_rate_lineedit")
        self.gridLayout_2.addWidget(self.target_sample_rate_lineedit, 1, 1, 1, 1)

        self.retranslateUi(ResampleSettingsView)
        QtCore.QMetaObject.connectSlotsByName(ResampleSettingsView)

    def retranslateUi(self, ResampleSettingsView):
        _translate = QtCore.QCoreApplication.translate
        ResampleSettingsView.setWindowTitle(_translate("ResampleSettingsView", "Form"))
        self.label_8.setText(_translate("ResampleSettingsView", "Resample settings"))
        self.label_9.setText(_translate("ResampleSettingsView", "Target sample rate"))

from widgets.QLineEditLive import QLineEditLive

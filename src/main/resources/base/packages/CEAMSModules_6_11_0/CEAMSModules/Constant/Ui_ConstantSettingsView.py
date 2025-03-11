# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cbrain/projects/snooz-toolbox/src/main/python/plugins/Constant/Ui_ConstantSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_ConstantSettingsView(object):
    def setupUi(self, ConstantSettingsView):
        ConstantSettingsView.setObjectName("ConstantSettingsView")
        ConstantSettingsView.resize(415, 224)
        self.layoutWidget = QtWidgets.QWidget(ConstantSettingsView)
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
        self.constant_lineedit = QLineEditLive(self.layoutWidget)
        self.constant_lineedit.setObjectName("constant_lineedit")
        self.gridLayout_2.addWidget(self.constant_lineedit, 1, 1, 1, 1)

        self.retranslateUi(ConstantSettingsView)
        QtCore.QMetaObject.connectSlotsByName(ConstantSettingsView)

    def retranslateUi(self, ConstantSettingsView):
        _translate = QtCore.QCoreApplication.translate
        ConstantSettingsView.setWindowTitle(_translate("ConstantSettingsView", "Form"))
        self.label_8.setText(_translate("ConstantSettingsView", "Constant settings"))
        self.label_9.setText(_translate("ConstantSettingsView", "Constant value"))

from widgets.QLineEditLive import QLineEditLive

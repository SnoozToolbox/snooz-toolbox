# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/DATADRIVE/gitRepos/ceams-carsm/CEAMS/scinodes_poc/src/main/python/plugins/EventCompare/Ui_EventCompareSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_EventCompareSettingsView(object):
    def setupUi(self, EventCompareSettingsView):
        EventCompareSettingsView.setObjectName("EventCompareSettingsView")
        EventCompareSettingsView.resize(469, 380)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(EventCompareSettingsView)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(EventCompareSettingsView)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.line_2 = QtWidgets.QFrame(EventCompareSettingsView)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.jaccord_lineEdit = QtWidgets.QLineEdit(EventCompareSettingsView)
        self.jaccord_lineEdit.setObjectName("jaccord_lineEdit")
        self.gridLayout.addWidget(self.jaccord_lineEdit, 4, 1, 1, 1)
        self.chan_label = QtWidgets.QLabel(EventCompareSettingsView)
        self.chan_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chan_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.chan_label.setObjectName("chan_label")
        self.gridLayout.addWidget(self.chan_label, 2, 0, 1, 1)
        self.event1_name_lineedit = QtWidgets.QLineEdit(EventCompareSettingsView)
        self.event1_name_lineedit.setObjectName("event1_name_lineedit")
        self.gridLayout.addWidget(self.event1_name_lineedit, 0, 1, 1, 1)
        self.event2_name_lineedit = QtWidgets.QLineEdit(EventCompareSettingsView)
        self.event2_name_lineedit.setObjectName("event2_name_lineedit")
        self.gridLayout.addWidget(self.event2_name_lineedit, 1, 1, 1, 1)
        self.channel1_lineedit = QtWidgets.QLineEdit(EventCompareSettingsView)
        self.channel1_lineedit.setObjectName("channel1_lineedit")
        self.gridLayout.addWidget(self.channel1_lineedit, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(EventCompareSettingsView)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(EventCompareSettingsView)
        self.label_6.setMinimumSize(QtCore.QSize(150, 0))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(EventCompareSettingsView)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(EventCompareSettingsView)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.channel2_lineedit = QtWidgets.QLineEdit(EventCompareSettingsView)
        self.channel2_lineedit.setObjectName("channel2_lineedit")
        self.gridLayout.addWidget(self.channel2_lineedit, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.label_4 = QtWidgets.QLabel(EventCompareSettingsView)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.line = QtWidgets.QFrame(EventCompareSettingsView)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(EventCompareSettingsView)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.filename_lineEdit = QtWidgets.QLineEdit(EventCompareSettingsView)
        self.filename_lineEdit.setObjectName("filename_lineEdit")
        self.horizontalLayout.addWidget(self.filename_lineEdit)
        self.browse_pushButton = QtWidgets.QPushButton(EventCompareSettingsView)
        self.browse_pushButton.setObjectName("browse_pushButton")
        self.horizontalLayout.addWidget(self.browse_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(EventCompareSettingsView)
        self.label_8.setMinimumSize(QtCore.QSize(150, 0))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.label_lineEdit = QtWidgets.QLineEdit(EventCompareSettingsView)
        self.label_lineEdit.setObjectName("label_lineEdit")
        self.horizontalLayout_2.addWidget(self.label_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)

        self.retranslateUi(EventCompareSettingsView)
        self.browse_pushButton.clicked.connect(EventCompareSettingsView.on_choose)
        QtCore.QMetaObject.connectSlotsByName(EventCompareSettingsView)

    def retranslateUi(self, EventCompareSettingsView):
        _translate = QtCore.QCoreApplication.translate
        EventCompareSettingsView.setWindowTitle(_translate("EventCompareSettingsView", "Form"))
        self.label_5.setText(_translate("EventCompareSettingsView", "Input settings"))
        self.jaccord_lineEdit.setToolTip(_translate("EventCompareSettingsView", "Enter the Jaccord index (similarity) threshold (from 0 et 1) to mark an event as valid."))
        self.jaccord_lineEdit.setText(_translate("EventCompareSettingsView", "0.2"))
        self.chan_label.setText(_translate("EventCompareSettingsView", "Channel label event 1"))
        self.event1_name_lineedit.setToolTip(_translate("EventCompareSettingsView", "Enter the event label to evaluate."))
        self.event2_name_lineedit.setToolTip(_translate("EventCompareSettingsView", "Enter the event label to evaluate."))
        self.channel1_lineedit.setToolTip(_translate("EventCompareSettingsView", "Enter the channel to filter events 1 to evaluate.  Let it empty to compare the events from all channels."))
        self.label.setText(_translate("EventCompareSettingsView", "Event 1 name"))
        self.label_6.setText(_translate("EventCompareSettingsView", "Jaccord Index threshold"))
        self.label_2.setText(_translate("EventCompareSettingsView", "Event 2 name"))
        self.label_7.setText(_translate("EventCompareSettingsView", "Channel label event 2"))
        self.channel2_lineedit.setToolTip(_translate("EventCompareSettingsView", "Enter the channel to filter events 2 to evaluate.  Let it empty to compare the events from all channels."))
        self.label_4.setText(_translate("EventCompareSettingsView", "Output settings"))
        self.label_3.setText(_translate("EventCompareSettingsView", "Filename"))
        self.filename_lineEdit.setToolTip(_translate("EventCompareSettingsView", "Filename to save performance evaluation. "))
        self.browse_pushButton.setText(_translate("EventCompareSettingsView", "Browse"))
        self.label_8.setText(_translate("EventCompareSettingsView", "Label"))
        self.label_lineEdit.setToolTip(_translate("EventCompareSettingsView", "Optional to add information to the column header in the performance output file. "))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\klacourse\Documents\NGosselin\gitRepos\ceamscarms\Stand_alone_apps\scinodes_poc\src\main\python\plugins\DetectionView\Ui_DetectionViewSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_DetectionViewSettingsView(object):
    def setupUi(self, DetectionViewSettingsView):
        DetectionViewSettingsView.setObjectName("DetectionViewSettingsView")
        DetectionViewSettingsView.resize(572, 333)
        self.gridLayout_2 = QtWidgets.QGridLayout(DetectionViewSettingsView)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Title_label = QtWidgets.QLabel(DetectionViewSettingsView)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Title_label.setFont(font)
        self.Title_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Title_label.setObjectName("Title_label")
        self.verticalLayout_2.addWidget(self.Title_label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(DetectionViewSettingsView)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.time_label = QtWidgets.QLabel(DetectionViewSettingsView)
        self.time_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.time_label.setObjectName("time_label")
        self.gridLayout.addWidget(self.time_label, 0, 0, 1, 1)
        self.time_lineedit = QLineEditLive(DetectionViewSettingsView)
        self.time_lineedit.setObjectName("time_lineedit")
        self.gridLayout.addWidget(self.time_lineedit, 0, 1, 1, 2)
        self.win_show_label = QtWidgets.QLabel(DetectionViewSettingsView)
        self.win_show_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.win_show_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.win_show_label.setObjectName("win_show_label")
        self.gridLayout.addWidget(self.win_show_label, 1, 0, 1, 1)
        self.win_show_lineedit = QLineEditLive(DetectionViewSettingsView)
        self.win_show_lineedit.setText("")
        self.win_show_lineedit.setObjectName("win_show_lineedit")
        self.gridLayout.addWidget(self.win_show_lineedit, 1, 1, 1, 2)
        self.event_label = QtWidgets.QLabel(DetectionViewSettingsView)
        self.event_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.event_label.setObjectName("event_label")
        self.gridLayout.addWidget(self.event_label, 2, 0, 1, 1)
        self.event_lineEdit = QLineEditLive(DetectionViewSettingsView)
        self.event_lineEdit.setObjectName("event_lineEdit")
        self.gridLayout.addWidget(self.event_lineEdit, 2, 1, 1, 2)
        self.chan_label = QtWidgets.QLabel(DetectionViewSettingsView)
        self.chan_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.chan_label.setObjectName("chan_label")
        self.gridLayout.addWidget(self.chan_label, 3, 0, 1, 1)
        self.channel_lineedit = QLineEditLive(DetectionViewSettingsView)
        self.channel_lineedit.setText("")
        self.channel_lineedit.setObjectName("channel_lineedit")
        self.gridLayout.addWidget(self.channel_lineedit, 3, 1, 1, 2)
        self.windet_step_label = QtWidgets.QLabel(DetectionViewSettingsView)
        self.windet_step_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.windet_step_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.windet_step_label.setObjectName("windet_step_label")
        self.gridLayout.addWidget(self.windet_step_label, 4, 0, 1, 1)
        self.windet_step_lineedit = QLineEditLive(DetectionViewSettingsView)
        self.windet_step_lineedit.setText("")
        self.windet_step_lineedit.setObjectName("windet_step_lineedit")
        self.gridLayout.addWidget(self.windet_step_lineedit, 4, 1, 1, 2)
        self.thresh_label = QtWidgets.QLabel(DetectionViewSettingsView)
        self.thresh_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.thresh_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.thresh_label.setObjectName("thresh_label")
        self.gridLayout.addWidget(self.thresh_label, 5, 0, 1, 1)
        self.thresh_lineedit = QLineEditLive(DetectionViewSettingsView)
        self.thresh_lineedit.setText("")
        self.thresh_lineedit.setObjectName("thresh_lineedit")
        self.gridLayout.addWidget(self.thresh_lineedit, 5, 1, 1, 1)
        self.threshUnit_comboBox = QComboBoxLive(DetectionViewSettingsView)
        self.threshUnit_comboBox.setObjectName("threshUnit_comboBox")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.gridLayout.addWidget(self.threshUnit_comboBox, 5, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(DetectionViewSettingsView)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(DetectionViewSettingsView)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.filename_lineedit = QLineEditLive(DetectionViewSettingsView)
        self.filename_lineedit.setText("")
        self.filename_lineedit.setObjectName("filename_lineedit")
        self.horizontalLayout_2.addWidget(self.filename_lineedit)
        self.ChooseBut = QtWidgets.QPushButton(DetectionViewSettingsView)
        self.ChooseBut.setObjectName("ChooseBut")
        self.horizontalLayout_2.addWidget(self.ChooseBut)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(DetectionViewSettingsView)
        self.ChooseBut.clicked.connect(DetectionViewSettingsView.on_choose)
        QtCore.QMetaObject.connectSlotsByName(DetectionViewSettingsView)

    def retranslateUi(self, DetectionViewSettingsView):
        _translate = QtCore.QCoreApplication.translate
        DetectionViewSettingsView.setWindowTitle(_translate("DetectionViewSettingsView", "Form"))
        self.Title_label.setText(_translate("DetectionViewSettingsView", "Detection View settings"))
        self.label_3.setText(_translate("DetectionViewSettingsView", "-------- Input Settings -----------------------------------------------------"))
        self.time_label.setText(_translate("DetectionViewSettingsView", "Time elapsed (HH:MM:SS)"))
        self.time_lineedit.setToolTip(_translate("DetectionViewSettingsView", "Time elapsed since the beginning of the recording (ex. 01:10:5.5)"))
        self.win_show_label.setText(_translate("DetectionViewSettingsView", "Window length to show (s)"))
        self.win_show_lineedit.setToolTip(_translate("DetectionViewSettingsView", "Window length to display in second."))
        self.event_label.setText(_translate("DetectionViewSettingsView", "Event name"))
        self.chan_label.setText(_translate("DetectionViewSettingsView", "Channel selection"))
        self.channel_lineedit.setToolTip(_translate("DetectionViewSettingsView", "Single channel label to display (ex. EEG C3)"))
        self.windet_step_label.setToolTip(_translate("DetectionViewSettingsView", "Window step in second used to detect events."))
        self.windet_step_label.setText(_translate("DetectionViewSettingsView", "Detection window step (s)"))
        self.thresh_label.setText(_translate("DetectionViewSettingsView", "Threshold"))
        self.thresh_lineedit.setToolTip(_translate("DetectionViewSettingsView", "Threshold used to detect events."))
        self.threshUnit_comboBox.setToolTip(_translate("DetectionViewSettingsView", "Select threshold unit : fixed (as µV²), x times the baseline median or x times the baseline standard deviation."))
        self.threshUnit_comboBox.setItemText(0, _translate("DetectionViewSettingsView", "fixed"))
        self.threshUnit_comboBox.setItemText(1, _translate("DetectionViewSettingsView", "x BSL median"))
        self.threshUnit_comboBox.setItemText(2, _translate("DetectionViewSettingsView", "x BSL STD"))
        self.threshUnit_comboBox.setItemText(3, _translate("DetectionViewSettingsView", "x BSL STD (log10)"))
        self.label_2.setText(_translate("DetectionViewSettingsView", "-------- Output Settings ---------------------------------------------------"))
        self.label.setText(_translate("DetectionViewSettingsView", "Filename"))
        self.filename_lineedit.setToolTip(_translate("DetectionViewSettingsView", "Python filename to save the detection information and signal to display."))
        self.ChooseBut.setToolTip(_translate("DetectionViewSettingsView", "Browse the filename to save."))
        self.ChooseBut.setText(_translate("DetectionViewSettingsView", "Choose"))
from widgets.QComboBoxLive import QComboBoxLive
from widgets.QLineEditLive import QLineEditLive

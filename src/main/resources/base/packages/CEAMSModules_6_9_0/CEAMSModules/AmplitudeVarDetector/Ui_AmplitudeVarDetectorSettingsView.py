# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/DATADRIVE/gitRepos/ceams-carsm/CEAMS/scinodes_poc/src/main/python/plugins/AmplitudeVarDetector/Ui_AmplitudeVarDetectorSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_AmplitudeVarDetectorSettingsView(object):
    def setupUi(self, AmplitudeVarDetectorSettingsView):
        AmplitudeVarDetectorSettingsView.setObjectName("AmplitudeVarDetectorSettingsView")
        AmplitudeVarDetectorSettingsView.resize(417, 273)
        AmplitudeVarDetectorSettingsView.setToolTip("")
        self.verticalLayout = QtWidgets.QVBoxLayout(AmplitudeVarDetectorSettingsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(AmplitudeVarDetectorSettingsView)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(AmplitudeVarDetectorSettingsView)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.event_name_lineedit = QtWidgets.QLineEdit(AmplitudeVarDetectorSettingsView)
        self.event_name_lineedit.setObjectName("event_name_lineedit")
        self.gridLayout.addWidget(self.event_name_lineedit, 1, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(AmplitudeVarDetectorSettingsView)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.win_length_lineedit = QtWidgets.QLineEdit(AmplitudeVarDetectorSettingsView)
        self.win_length_lineedit.setText("")
        self.win_length_lineedit.setObjectName("win_length_lineedit")
        self.gridLayout.addWidget(self.win_length_lineedit, 2, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(AmplitudeVarDetectorSettingsView)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.win_step_lineedit = QtWidgets.QLineEdit(AmplitudeVarDetectorSettingsView)
        self.win_step_lineedit.setObjectName("win_step_lineedit")
        self.gridLayout.addWidget(self.win_step_lineedit, 3, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(AmplitudeVarDetectorSettingsView)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.baseline_win_len_lineedit = QtWidgets.QLineEdit(AmplitudeVarDetectorSettingsView)
        self.baseline_win_len_lineedit.setText("")
        self.baseline_win_len_lineedit.setObjectName("baseline_win_len_lineedit")
        self.gridLayout.addWidget(self.baseline_win_len_lineedit, 4, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(AmplitudeVarDetectorSettingsView)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.pad_lineEdit = QtWidgets.QLineEdit(AmplitudeVarDetectorSettingsView)
        self.pad_lineEdit.setObjectName("pad_lineEdit")
        self.gridLayout.addWidget(self.pad_lineEdit, 5, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(AmplitudeVarDetectorSettingsView)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.tresholdval_lineedit = QtWidgets.QLineEdit(AmplitudeVarDetectorSettingsView)
        self.tresholdval_lineedit.setText("")
        self.tresholdval_lineedit.setObjectName("tresholdval_lineedit")
        self.gridLayout.addWidget(self.tresholdval_lineedit, 6, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(AmplitudeVarDetectorSettingsView)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.threshBeha_comboBox = QtWidgets.QComboBox(AmplitudeVarDetectorSettingsView)
        self.threshBeha_comboBox.setObjectName("threshBeha_comboBox")
        self.threshBeha_comboBox.addItem("")
        self.threshBeha_comboBox.addItem("")
        self.gridLayout.addWidget(self.threshBeha_comboBox, 7, 1, 1, 1)
        self.threshUnit_comboBox = QtWidgets.QComboBox(AmplitudeVarDetectorSettingsView)
        self.threshUnit_comboBox.setObjectName("threshUnit_comboBox")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.gridLayout.addWidget(self.threshUnit_comboBox, 7, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(AmplitudeVarDetectorSettingsView)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.chan_det_info_lineedit = QtWidgets.QLineEdit(AmplitudeVarDetectorSettingsView)
        self.chan_det_info_lineedit.setText("")
        self.chan_det_info_lineedit.setObjectName("chan_det_info_lineedit")
        self.gridLayout.addWidget(self.chan_det_info_lineedit, 8, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(AmplitudeVarDetectorSettingsView)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.group_lineedit = QtWidgets.QLineEdit(AmplitudeVarDetectorSettingsView)
        self.group_lineedit.setObjectName("group_lineedit")
        self.gridLayout.addWidget(self.group_lineedit, 0, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(336, 11, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(AmplitudeVarDetectorSettingsView)
        QtCore.QMetaObject.connectSlotsByName(AmplitudeVarDetectorSettingsView)

    def retranslateUi(self, AmplitudeVarDetectorSettingsView):
        _translate = QtCore.QCoreApplication.translate
        AmplitudeVarDetectorSettingsView.setWindowTitle(_translate("AmplitudeVarDetectorSettingsView", "Form"))
        self.label_5.setText(_translate("AmplitudeVarDetectorSettingsView", "Amplitude Detector settings"))
        self.label.setText(_translate("AmplitudeVarDetectorSettingsView", "Event name"))
        self.label_2.setText(_translate("AmplitudeVarDetectorSettingsView", "Window length (s)"))
        self.win_length_lineedit.setToolTip(_translate("AmplitudeVarDetectorSettingsView", "The window length (in second) used to compute the amplitude variation."))
        self.label_3.setText(_translate("AmplitudeVarDetectorSettingsView", "Window step (s)"))
        self.win_step_lineedit.setToolTip(_translate("AmplitudeVarDetectorSettingsView", "The window step (in seconds) between two amplitude variation calculations."))
        self.label_6.setText(_translate("AmplitudeVarDetectorSettingsView", "Baseline window length (s)"))
        self.baseline_win_len_lineedit.setToolTip(_translate("AmplitudeVarDetectorSettingsView", "Optional"))
        self.label_4.setText(_translate("AmplitudeVarDetectorSettingsView", "Pad length (s)"))
        self.pad_lineEdit.setToolTip(_translate("AmplitudeVarDetectorSettingsView", "Padding event added to both the beginning and  the end of the originally detected event."))
        self.label_7.setText(_translate("AmplitudeVarDetectorSettingsView", "Threshold value"))
        self.label_8.setToolTip(_translate("AmplitudeVarDetectorSettingsView", "Select behavior: artefact when above/below the threshold."))
        self.label_8.setText(_translate("AmplitudeVarDetectorSettingsView", "Threshold behavior"))
        self.threshBeha_comboBox.setToolTip(_translate("AmplitudeVarDetectorSettingsView", "Select behavior: artefact when above/below the threshold."))
        self.threshBeha_comboBox.setItemText(0, _translate("AmplitudeVarDetectorSettingsView", "Above"))
        self.threshBeha_comboBox.setItemText(1, _translate("AmplitudeVarDetectorSettingsView", "Below"))
        self.threshUnit_comboBox.setToolTip(_translate("AmplitudeVarDetectorSettingsView", "Select threshold unit : \n"
"-fixed (as µV²),\n"
"-x times the baseline median or\n"
"-x times the baseline standard deviation or\n"
"-x times the baseline standard deviation on data log10 transformed."))
        self.threshUnit_comboBox.setItemText(0, _translate("AmplitudeVarDetectorSettingsView", "fixed"))
        self.threshUnit_comboBox.setItemText(1, _translate("AmplitudeVarDetectorSettingsView", "x BSL median"))
        self.threshUnit_comboBox.setItemText(2, _translate("AmplitudeVarDetectorSettingsView", "x BSL STD"))
        self.threshUnit_comboBox.setItemText(3, _translate("AmplitudeVarDetectorSettingsView", "x BSL STD (log10)"))
        self.label_9.setToolTip(_translate("AmplitudeVarDetectorSettingsView", "Select behavior: artefact when above/below the threshold."))
        self.label_9.setText(_translate("AmplitudeVarDetectorSettingsView", "Channel to exit detection info"))
        self.chan_det_info_lineedit.setToolTip(_translate("AmplitudeVarDetectorSettingsView", "Channel label to see detection info (debug purpose only)"))
        self.label_10.setText(_translate("AmplitudeVarDetectorSettingsView", "Event group"))


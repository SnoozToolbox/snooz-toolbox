# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/DATADRIVE/gitRepos/ceams-carsm/CEAMS/snooz-toolbox/src/main/python/plugins/AmplitudeDetector/Ui_AmplitudeDetectorSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_AmplitudeDetectorSettingsView(object):
    def setupUi(self, AmplitudeDetectorSettingsView):
        AmplitudeDetectorSettingsView.setObjectName("AmplitudeDetectorSettingsView")
        AmplitudeDetectorSettingsView.resize(376, 217)
        AmplitudeDetectorSettingsView.setToolTip("")
        self.gridLayout_2 = QtWidgets.QGridLayout(AmplitudeDetectorSettingsView)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(AmplitudeDetectorSettingsView)
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
        self.label = QtWidgets.QLabel(AmplitudeDetectorSettingsView)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.event_name_lineedit = QtWidgets.QLineEdit(AmplitudeDetectorSettingsView)
        self.event_name_lineedit.setObjectName("event_name_lineedit")
        self.gridLayout.addWidget(self.event_name_lineedit, 1, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(AmplitudeDetectorSettingsView)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pad_length_lineedit = QtWidgets.QLineEdit(AmplitudeDetectorSettingsView)
        self.pad_length_lineedit.setText("")
        self.pad_length_lineedit.setObjectName("pad_length_lineedit")
        self.gridLayout.addWidget(self.pad_length_lineedit, 2, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(AmplitudeDetectorSettingsView)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.baseline_win_len_lineedit = QtWidgets.QLineEdit(AmplitudeDetectorSettingsView)
        self.baseline_win_len_lineedit.setText("")
        self.baseline_win_len_lineedit.setObjectName("baseline_win_len_lineedit")
        self.gridLayout.addWidget(self.baseline_win_len_lineedit, 3, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(AmplitudeDetectorSettingsView)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.tresholdval_lineedit = QtWidgets.QLineEdit(AmplitudeDetectorSettingsView)
        self.tresholdval_lineedit.setText("")
        self.tresholdval_lineedit.setObjectName("tresholdval_lineedit")
        self.gridLayout.addWidget(self.tresholdval_lineedit, 4, 1, 1, 1)
        self.threshUnit_comboBox = QtWidgets.QComboBox(AmplitudeDetectorSettingsView)
        self.threshUnit_comboBox.setObjectName("threshUnit_comboBox")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.gridLayout.addWidget(self.threshUnit_comboBox, 4, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(AmplitudeDetectorSettingsView)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.threshBeha_comboBox = QtWidgets.QComboBox(AmplitudeDetectorSettingsView)
        self.threshBeha_comboBox.setObjectName("threshBeha_comboBox")
        self.threshBeha_comboBox.addItem("")
        self.threshBeha_comboBox.addItem("")
        self.gridLayout.addWidget(self.threshBeha_comboBox, 5, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(AmplitudeDetectorSettingsView)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.chan_det_info_lineedit = QtWidgets.QLineEdit(AmplitudeDetectorSettingsView)
        self.chan_det_info_lineedit.setText("")
        self.chan_det_info_lineedit.setObjectName("chan_det_info_lineedit")
        self.gridLayout.addWidget(self.chan_det_info_lineedit, 6, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(AmplitudeDetectorSettingsView)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.group_lineedit = QtWidgets.QLineEdit(AmplitudeDetectorSettingsView)
        self.group_lineedit.setObjectName("group_lineedit")
        self.gridLayout.addWidget(self.group_lineedit, 0, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(AmplitudeDetectorSettingsView)
        QtCore.QMetaObject.connectSlotsByName(AmplitudeDetectorSettingsView)

    def retranslateUi(self, AmplitudeDetectorSettingsView):
        _translate = QtCore.QCoreApplication.translate
        AmplitudeDetectorSettingsView.setWindowTitle(_translate("AmplitudeDetectorSettingsView", "Form"))
        self.label_5.setText(_translate("AmplitudeDetectorSettingsView", "Amplitude Detector settings"))
        self.label.setText(_translate("AmplitudeDetectorSettingsView", "Event name"))
        self.label_2.setText(_translate("AmplitudeDetectorSettingsView", "Pad length (s)"))
        self.pad_length_lineedit.setToolTip(_translate("AmplitudeDetectorSettingsView", "Padding event added to both the beginning and  the end of the originally detected event."))
        self.label_6.setText(_translate("AmplitudeDetectorSettingsView", "Baseline window length (s)"))
        self.baseline_win_len_lineedit.setToolTip(_translate("AmplitudeDetectorSettingsView", "Optional"))
        self.label_7.setText(_translate("AmplitudeDetectorSettingsView", "Threshold value"))
        self.threshUnit_comboBox.setToolTip(_translate("AmplitudeDetectorSettingsView", "Select threshold unit : \n"
"-fixed (as µV²),\n"
"-x times the baseline median or\n"
"-x times the baseline standard deviation or\n"
"-x times the baseline standard deviation on data log10 transformed."))
        self.threshUnit_comboBox.setItemText(0, _translate("AmplitudeDetectorSettingsView", "fixed"))
        self.threshUnit_comboBox.setItemText(1, _translate("AmplitudeDetectorSettingsView", "x BSL median"))
        self.threshUnit_comboBox.setItemText(2, _translate("AmplitudeDetectorSettingsView", "x BSL STD"))
        self.threshUnit_comboBox.setItemText(3, _translate("AmplitudeDetectorSettingsView", "x BSL STD (log10)"))
        self.label_8.setToolTip(_translate("AmplitudeDetectorSettingsView", "Select behavior: artefact when above/below the threshold."))
        self.label_8.setText(_translate("AmplitudeDetectorSettingsView", "Threshold behavior"))
        self.threshBeha_comboBox.setToolTip(_translate("AmplitudeDetectorSettingsView", "Select behavior: artefact when above/below the threshold."))
        self.threshBeha_comboBox.setItemText(0, _translate("AmplitudeDetectorSettingsView", "Above"))
        self.threshBeha_comboBox.setItemText(1, _translate("AmplitudeDetectorSettingsView", "Below"))
        self.label_9.setToolTip(_translate("AmplitudeDetectorSettingsView", "Select behavior: artefact when above/below the threshold."))
        self.label_9.setText(_translate("AmplitudeDetectorSettingsView", "Channel to exit detection info"))
        self.chan_det_info_lineedit.setToolTip(_translate("AmplitudeDetectorSettingsView", "Channel label to see detection info (debug purpose only)"))
        self.label_3.setText(_translate("AmplitudeDetectorSettingsView", "Event group"))


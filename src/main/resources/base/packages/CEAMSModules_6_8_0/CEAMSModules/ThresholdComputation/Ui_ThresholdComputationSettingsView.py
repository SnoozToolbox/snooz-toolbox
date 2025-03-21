# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\klacourse\Documents\NGosselin\gitRepos\ceamscarms\Stand_alone_apps\scinodes_poc\src\main\python\plugins\ThresholdComputation\Ui_ThresholdComputationSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_ThresholdComputationSettingsView(object):
    def setupUi(self, ThresholdComputationSettingsView):
        ThresholdComputationSettingsView.setObjectName("ThresholdComputationSettingsView")
        ThresholdComputationSettingsView.resize(369, 261)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ThresholdComputationSettingsView)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.threshold_definition_label = QtWidgets.QLabel(ThresholdComputationSettingsView)
        self.threshold_definition_label.setMinimumSize(QtCore.QSize(150, 0))
        self.threshold_definition_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.threshold_definition_label.setObjectName("threshold_definition_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.threshold_definition_label)
        self.threshold_definition_lineedit = QtWidgets.QLineEdit(ThresholdComputationSettingsView)
        self.threshold_definition_lineedit.setObjectName("threshold_definition_lineedit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.threshold_definition_lineedit)
        self.threshold_metric_label = QtWidgets.QLabel(ThresholdComputationSettingsView)
        self.threshold_metric_label.setMinimumSize(QtCore.QSize(150, 0))
        self.threshold_metric_label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.threshold_metric_label.setObjectName("threshold_metric_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.threshold_metric_label)
        self.unit_comboBox = QtWidgets.QComboBox(ThresholdComputationSettingsView)
        self.unit_comboBox.setObjectName("unit_comboBox")
        self.unit_comboBox.addItem("")
        self.unit_comboBox.addItem("")
        self.unit_comboBox.addItem("")
        self.unit_comboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.unit_comboBox)
        self.label_2 = QtWidgets.QLabel(ThresholdComputationSettingsView)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_2)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(ThresholdComputationSettingsView)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.thresh_signal_radioButton = QtWidgets.QRadioButton(ThresholdComputationSettingsView)
        self.thresh_signal_radioButton.setObjectName("thresh_signal_radioButton")
        self.verticalLayout.addWidget(self.thresh_signal_radioButton)
        self.thresh_cycle_radioButton = QtWidgets.QRadioButton(ThresholdComputationSettingsView)
        self.thresh_cycle_radioButton.setObjectName("thresh_cycle_radioButton")
        self.verticalLayout.addWidget(self.thresh_cycle_radioButton)
        self.thresh_channel_radioButton = QtWidgets.QRadioButton(ThresholdComputationSettingsView)
        self.thresh_channel_radioButton.setObjectName("thresh_channel_radioButton")
        self.verticalLayout.addWidget(self.thresh_channel_radioButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)

        self.retranslateUi(ThresholdComputationSettingsView)
        self.thresh_signal_radioButton.clicked.connect(ThresholdComputationSettingsView.on_settings_changed)
        self.thresh_cycle_radioButton.clicked.connect(ThresholdComputationSettingsView.on_settings_changed)
        self.thresh_channel_radioButton.clicked.connect(ThresholdComputationSettingsView.on_settings_changed)
        QtCore.QMetaObject.connectSlotsByName(ThresholdComputationSettingsView)

    def retranslateUi(self, ThresholdComputationSettingsView):
        _translate = QtCore.QCoreApplication.translate
        ThresholdComputationSettingsView.setWindowTitle(_translate("ThresholdComputationSettingsView", "Form"))
        self.threshold_definition_label.setText(_translate("ThresholdComputationSettingsView", "threshold value (definition)"))
        self.threshold_definition_lineedit.setToolTip(_translate("ThresholdComputationSettingsView", "Enter the threshold value to compute i.e. 95 for 95 percentile or 4 for 4 x standard deviation."))
        self.threshold_metric_label.setText(_translate("ThresholdComputationSettingsView", "threshold metric (unit)"))
        self.unit_comboBox.setItemText(0, _translate("ThresholdComputationSettingsView", "percentile"))
        self.unit_comboBox.setItemText(1, _translate("ThresholdComputationSettingsView", "standard deviation"))
        self.unit_comboBox.setItemText(2, _translate("ThresholdComputationSettingsView", "median"))
        self.unit_comboBox.setItemText(3, _translate("ThresholdComputationSettingsView", "variance"))
        self.label_2.setText(_translate("ThresholdComputationSettingsView", "Threshold Computation Settings"))
        self.label.setText(_translate("ThresholdComputationSettingsView", "Compute a theshold per ..."))
        self.thresh_signal_radioButton.setToolTip(_translate("ThresholdComputationSettingsView", "Select to compute a threshold per item of signals (each channel and bout of signals will be linked to its own threshold)"))
        self.thresh_signal_radioButton.setText(_translate("ThresholdComputationSettingsView", "item of signals"))
        self.thresh_cycle_radioButton.setToolTip(_translate("ThresholdComputationSettingsView", "Select to compute a threshold per sleep cycle and channel(the threshold will be duplicated for all signals included in the same sleep cycle)."))
        self.thresh_cycle_radioButton.setText(_translate("ThresholdComputationSettingsView", "sleep cycle and channel"))
        self.thresh_channel_radioButton.setToolTip(_translate("ThresholdComputationSettingsView", "Select to compute a single threshold per channel (through all signals and/or sleep cycles)."))
        self.thresh_channel_radioButton.setText(_translate("ThresholdComputationSettingsView", "channel (through all signals)"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\klacourse\Documents\NGosselin\gitRepos\ceamscarms\Stand_alone_apps\scinodes_poc\src\main\python\plugins\FilterEvents\Ui_FilterEventsSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_FilterEventsSettingsView(object):
    def setupUi(self, FilterEventsSettingsView):
        FilterEventsSettingsView.setObjectName("FilterEventsSettingsView")
        FilterEventsSettingsView.resize(312, 452)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(FilterEventsSettingsView)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(FilterEventsSettingsView)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_33 = QtWidgets.QLabel(FilterEventsSettingsView)
        self.label_33.setObjectName("label_33")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_33)
        self.group_lineEdit = QtWidgets.QLineEdit(FilterEventsSettingsView)
        self.group_lineEdit.setObjectName("group_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.group_lineEdit)
        self.label_34 = QtWidgets.QLabel(FilterEventsSettingsView)
        self.label_34.setObjectName("label_34")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.name_lineEdit = QtWidgets.QLineEdit(FilterEventsSettingsView)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name_lineEdit)
        self.label_9 = QtWidgets.QLabel(FilterEventsSettingsView)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.stages_lineEdit = QtWidgets.QLineEdit(FilterEventsSettingsView)
        self.stages_lineEdit.setEnabled(True)
        self.stages_lineEdit.setReadOnly(True)
        self.stages_lineEdit.setObjectName("stages_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.stages_lineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.frame = QtWidgets.QFrame(FilterEventsSettingsView)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.stage2_checkBox = QtWidgets.QCheckBox(self.frame)
        self.stage2_checkBox.setObjectName("stage2_checkBox")
        self.gridLayout.addWidget(self.stage2_checkBox, 2, 0, 1, 1)
        self.nrem_checkBox = QtWidgets.QCheckBox(self.frame)
        self.nrem_checkBox.setObjectName("nrem_checkBox")
        self.gridLayout.addWidget(self.nrem_checkBox, 0, 1, 1, 1)
        self.rem_checkBox = QtWidgets.QCheckBox(self.frame)
        self.rem_checkBox.setObjectName("rem_checkBox")
        self.gridLayout.addWidget(self.rem_checkBox, 5, 0, 1, 1)
        self.undetermined_checkBox = QtWidgets.QCheckBox(self.frame)
        self.undetermined_checkBox.setObjectName("undetermined_checkBox")
        self.gridLayout.addWidget(self.undetermined_checkBox, 8, 0, 1, 1)
        self.stage1_checkBox = QtWidgets.QCheckBox(self.frame)
        self.stage1_checkBox.setObjectName("stage1_checkBox")
        self.gridLayout.addWidget(self.stage1_checkBox, 1, 0, 1, 1)
        self.technicaltime_checkBox = QtWidgets.QCheckBox(self.frame)
        self.technicaltime_checkBox.setObjectName("technicaltime_checkBox")
        self.gridLayout.addWidget(self.technicaltime_checkBox, 7, 0, 1, 1)
        self.nwake_checkBox = QtWidgets.QCheckBox(self.frame)
        self.nwake_checkBox.setObjectName("nwake_checkBox")
        self.gridLayout.addWidget(self.nwake_checkBox, 1, 1, 1, 1)
        self.wake_checkBox = QtWidgets.QCheckBox(self.frame)
        self.wake_checkBox.setEnabled(True)
        self.wake_checkBox.setChecked(False)
        self.wake_checkBox.setObjectName("wake_checkBox")
        self.gridLayout.addWidget(self.wake_checkBox, 0, 0, 1, 1)
        self.stage4_checkBox = QtWidgets.QCheckBox(self.frame)
        self.stage4_checkBox.setObjectName("stage4_checkBox")
        self.gridLayout.addWidget(self.stage4_checkBox, 4, 0, 1, 1)
        self.stage3_checkBox = QtWidgets.QCheckBox(self.frame)
        self.stage3_checkBox.setObjectName("stage3_checkBox")
        self.gridLayout.addWidget(self.stage3_checkBox, 3, 0, 1, 1)
        self.movementtime_checkBox = QtWidgets.QCheckBox(self.frame)
        self.movementtime_checkBox.setObjectName("movementtime_checkBox")
        self.gridLayout.addWidget(self.movementtime_checkBox, 6, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 52, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(FilterEventsSettingsView)
        self.wake_checkBox.stateChanged['int'].connect(FilterEventsSettingsView.on_event_stages_changed)
        self.undetermined_checkBox.stateChanged['int'].connect(FilterEventsSettingsView.on_event_stages_changed)
        self.technicaltime_checkBox.stateChanged['int'].connect(FilterEventsSettingsView.on_event_stages_changed)
        self.movementtime_checkBox.stateChanged['int'].connect(FilterEventsSettingsView.on_event_stages_changed)
        self.rem_checkBox.stateChanged['int'].connect(FilterEventsSettingsView.on_event_stages_changed)
        self.stage4_checkBox.stateChanged['int'].connect(FilterEventsSettingsView.on_event_stages_changed)
        self.stage3_checkBox.stateChanged['int'].connect(FilterEventsSettingsView.on_event_stages_changed)
        self.stage2_checkBox.stateChanged['int'].connect(FilterEventsSettingsView.on_event_stages_changed)
        self.stage1_checkBox.stateChanged['int'].connect(FilterEventsSettingsView.on_event_stages_changed)
        self.nwake_checkBox.stateChanged['int'].connect(FilterEventsSettingsView.on_event_nwake_changed)
        self.nrem_checkBox.stateChanged['int'].connect(FilterEventsSettingsView.on_event_nrem_changed)
        QtCore.QMetaObject.connectSlotsByName(FilterEventsSettingsView)

    def retranslateUi(self, FilterEventsSettingsView):
        _translate = QtCore.QCoreApplication.translate
        FilterEventsSettingsView.setWindowTitle(_translate("FilterEventsSettingsView", "Form"))
        self.label_8.setText(_translate("FilterEventsSettingsView", "Filter Events settings"))
        self.label_33.setText(_translate("FilterEventsSettingsView", "Group"))
        self.group_lineEdit.setToolTip(_translate("FilterEventsSettingsView", "Filter events based on their group (literal string pattern)."))
        self.label_34.setText(_translate("FilterEventsSettingsView", "Name"))
        self.name_lineEdit.setToolTip(_translate("FilterEventsSettingsView", "Filter events based on their name (literal string pattern)."))
        self.label_9.setText(_translate("FilterEventsSettingsView", "Stages"))
        self.stages_lineEdit.setToolTip(_translate("FilterEventsSettingsView", "Define the sleep stage selection with the checkbox below."))
        self.stage2_checkBox.setText(_translate("FilterEventsSettingsView", "N2"))
        self.nrem_checkBox.setText(_translate("FilterEventsSettingsView", "All NREM"))
        self.rem_checkBox.setText(_translate("FilterEventsSettingsView", "R"))
        self.undetermined_checkBox.setText(_translate("FilterEventsSettingsView", "Unscored"))
        self.stage1_checkBox.setText(_translate("FilterEventsSettingsView", "N1"))
        self.technicaltime_checkBox.setText(_translate("FilterEventsSettingsView", "Technical time"))
        self.nwake_checkBox.setToolTip(_translate("FilterEventsSettingsView", "Check to select all sleep stages and exclude wake, movement, technical issues and unscored"))
        self.nwake_checkBox.setText(_translate("FilterEventsSettingsView", "All asleep stages"))
        self.wake_checkBox.setText(_translate("FilterEventsSettingsView", "Wake"))
        self.stage4_checkBox.setText(_translate("FilterEventsSettingsView", "Stage 4"))
        self.stage3_checkBox.setText(_translate("FilterEventsSettingsView", "N3"))
        self.movementtime_checkBox.setText(_translate("FilterEventsSettingsView", "Movement time"))
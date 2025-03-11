# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cbrain/projects/snooz-toolbox/src/main/python/plugins/EventCreator/Ui_EventCreatorSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

class Ui_EventCreatorSettingsView(object):
    def setupUi(self, EventCreatorSettingsView):
        EventCreatorSettingsView.setObjectName("EventCreatorSettingsView")
        EventCreatorSettingsView.resize(415, 224)
        self.widget = QtWidgets.QWidget(EventCreatorSettingsView)
        self.widget.setGeometry(QtCore.QRect(10, 12, 208, 162))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.event_name_lineedit = QLineEditLive(self.widget)
        self.event_name_lineedit.setObjectName("event_name_lineedit")
        self.gridLayout.addWidget(self.event_name_lineedit, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.start_time_lineedit = QLineEditLive(self.widget)
        self.start_time_lineedit.setObjectName("start_time_lineedit")
        self.gridLayout.addWidget(self.start_time_lineedit, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        self.duration_lineedit = QLineEditLive(self.widget)
        self.duration_lineedit.setObjectName("duration_lineedit")
        self.gridLayout.addWidget(self.duration_lineedit, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)
        self.group_name_lineedit = QLineEditLive(self.widget)
        self.group_name_lineedit.setObjectName("group_name_lineedit")
        self.gridLayout.addWidget(self.group_name_lineedit, 4, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)
        self.channels_lineedit = QLineEditLive(self.widget)
        self.channels_lineedit.setObjectName("channels_lineedit")
        self.gridLayout.addWidget(self.channels_lineedit, 5, 1, 1, 1)

        self.retranslateUi(EventCreatorSettingsView)
        QtCore.QMetaObject.connectSlotsByName(EventCreatorSettingsView)

    def retranslateUi(self, EventCreatorSettingsView):
        _translate = QtCore.QCoreApplication.translate
        EventCreatorSettingsView.setWindowTitle(_translate("EventCreatorSettingsView", "Form"))
        self.label_8.setText(_translate("EventCreatorSettingsView", "EventCreator settings"))
        self.label_9.setText(_translate("EventCreatorSettingsView", "Event name"))
        self.label_10.setText(_translate("EventCreatorSettingsView", "Start time"))
        self.label_11.setText(_translate("EventCreatorSettingsView", "Duration"))
        self.label_12.setText(_translate("EventCreatorSettingsView", "Group name"))
        self.label_13.setText(_translate("EventCreatorSettingsView", "Channels"))
        self.channels_lineedit.setToolTip(_translate("EventCreatorSettingsView", "Space separated list of channels"))

from widgets.QLineEditLive import QLineEditLive

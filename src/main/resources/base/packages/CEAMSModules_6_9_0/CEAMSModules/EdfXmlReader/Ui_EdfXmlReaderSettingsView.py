# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\klacourse\Documents\NGosselin\gitRepos\ceamscarms\Stand_alone_apps\scinodes_poc\src\main\python\plugins\EdfXmlReader\Ui_EdfXmlReaderSettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_EdfXmlReaderSettingsView(object):
    def setupUi(self, EdfXmlReaderSettingsView):
        EdfXmlReaderSettingsView.setObjectName("EdfXmlReaderSettingsView")
        EdfXmlReaderSettingsView.resize(415, 224)
        self.verticalLayout = QtWidgets.QVBoxLayout(EdfXmlReaderSettingsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.filename_lineedit = QLineEditLive(EdfXmlReaderSettingsView)
        self.filename_lineedit.setText("")
        self.filename_lineedit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.filename_lineedit.setObjectName("filename_lineedit")
        self.gridLayout.addWidget(self.filename_lineedit, 0, 1, 1, 1)
        self.filename_label = QtWidgets.QLabel(EdfXmlReaderSettingsView)
        self.filename_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.filename_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.filename_label.setObjectName("filename_label")
        self.gridLayout.addWidget(self.filename_label, 0, 0, 1, 1)
        self.choose_pushbutton = QtWidgets.QPushButton(EdfXmlReaderSettingsView)
        self.choose_pushbutton.setObjectName("choose_pushbutton")
        self.gridLayout.addWidget(self.choose_pushbutton, 0, 2, 1, 1)
        self.event_label = QtWidgets.QLabel(EdfXmlReaderSettingsView)
        self.event_label.setObjectName("event_label")
        self.gridLayout.addWidget(self.event_label, 1, 0, 1, 1)
        self.event_name_lineEdit = QLineEditLive(EdfXmlReaderSettingsView)
        self.event_name_lineEdit.setObjectName("event_name_lineEdit")
        self.gridLayout.addWidget(self.event_name_lineEdit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(EdfXmlReaderSettingsView)
        self.choose_pushbutton.clicked.connect(EdfXmlReaderSettingsView.on_choose)
        QtCore.QMetaObject.connectSlotsByName(EdfXmlReaderSettingsView)

    def retranslateUi(self, EdfXmlReaderSettingsView):
        _translate = QtCore.QCoreApplication.translate
        EdfXmlReaderSettingsView.setWindowTitle(_translate("EdfXmlReaderSettingsView", "Form"))
        self.filename_lineedit.setPlaceholderText(_translate("EdfXmlReaderSettingsView", "Choose a EDF.XML file to read"))
        self.filename_label.setText(_translate("EdfXmlReaderSettingsView", "Filename"))
        self.choose_pushbutton.setText(_translate("EdfXmlReaderSettingsView", "Choose"))
        self.event_label.setText(_translate("EdfXmlReaderSettingsView", "Event name"))
        self.event_name_lineEdit.setToolTip(_translate("EdfXmlReaderSettingsView", "Event name is optional. Event name can be a list of labels."))
from widgets.QLineEditLive import QLineEditLive
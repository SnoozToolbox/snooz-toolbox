# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EdfXmlReaderMasterSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from widgets.QLineEditLive import QLineEditLive


class Ui_EdfXmlReaderMasterSettingsView(object):
    def setupUi(self, EdfXmlReaderMasterSettingsView):
        if not EdfXmlReaderMasterSettingsView.objectName():
            EdfXmlReaderMasterSettingsView.setObjectName(u"EdfXmlReaderMasterSettingsView")
        EdfXmlReaderMasterSettingsView.resize(415, 224)
        self.verticalLayout = QVBoxLayout(EdfXmlReaderMasterSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.filename_lineedit = QLineEditLive(EdfXmlReaderMasterSettingsView)
        self.filename_lineedit.setObjectName(u"filename_lineedit")
        self.filename_lineedit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.filename_lineedit, 0, 1, 1, 1)

        self.filename_label = QLabel(EdfXmlReaderMasterSettingsView)
        self.filename_label.setObjectName(u"filename_label")
        self.filename_label.setLayoutDirection(Qt.LeftToRight)
        self.filename_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.filename_label, 0, 0, 1, 1)

        self.choose_pushbutton = QPushButton(EdfXmlReaderMasterSettingsView)
        self.choose_pushbutton.setObjectName(u"choose_pushbutton")

        self.gridLayout.addWidget(self.choose_pushbutton, 0, 2, 1, 1)

        self.event_label = QLabel(EdfXmlReaderMasterSettingsView)
        self.event_label.setObjectName(u"event_label")

        self.gridLayout.addWidget(self.event_label, 1, 0, 1, 1)

        self.event_name_lineEdit = QLineEditLive(EdfXmlReaderMasterSettingsView)
        self.event_name_lineEdit.setObjectName(u"event_name_lineEdit")

        self.gridLayout.addWidget(self.event_name_lineEdit, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(EdfXmlReaderMasterSettingsView)
        self.choose_pushbutton.clicked.connect(EdfXmlReaderMasterSettingsView.on_choose)

        QMetaObject.connectSlotsByName(EdfXmlReaderMasterSettingsView)
    # setupUi

    def retranslateUi(self, EdfXmlReaderMasterSettingsView):
        EdfXmlReaderMasterSettingsView.setWindowTitle(QCoreApplication.translate("EdfXmlReaderMasterSettingsView", u"Form", None))
        self.filename_lineedit.setText("")
        self.filename_lineedit.setPlaceholderText(QCoreApplication.translate("EdfXmlReaderMasterSettingsView", u"Choose XML files to read", None))
        self.filename_label.setText(QCoreApplication.translate("EdfXmlReaderMasterSettingsView", u"Filename", None))
        self.choose_pushbutton.setText(QCoreApplication.translate("EdfXmlReaderMasterSettingsView", u"Choose", None))
        self.event_label.setText(QCoreApplication.translate("EdfXmlReaderMasterSettingsView", u"Event name", None))
#if QT_CONFIG(tooltip)
        self.event_name_lineEdit.setToolTip(QCoreApplication.translate("EdfXmlReaderMasterSettingsView", u"Event name is optional. Event name can be a list of labels.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_StringManipSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StringManipSettingsView(object):
    def setupUi(self, StringManipSettingsView):
        if not StringManipSettingsView.objectName():
            StringManipSettingsView.setObjectName(u"StringManipSettingsView")
        StringManipSettingsView.resize(344, 188)
        self.verticalLayout = QVBoxLayout(StringManipSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.prefix_label = QLabel(StringManipSettingsView)
        self.prefix_label.setObjectName(u"prefix_label")

        self.gridLayout_2.addWidget(self.prefix_label, 1, 0, 1, 1)

        self.ext_rm_checkBox = QCheckBox(StringManipSettingsView)
        self.ext_rm_checkBox.setObjectName(u"ext_rm_checkBox")

        self.gridLayout_2.addWidget(self.ext_rm_checkBox, 7, 1, 1, 1)

        self.suffix_label = QLabel(StringManipSettingsView)
        self.suffix_label.setObjectName(u"suffix_label")

        self.gridLayout_2.addWidget(self.suffix_label, 2, 0, 1, 1)

        self.path_rm_checkBox = QCheckBox(StringManipSettingsView)
        self.path_rm_checkBox.setObjectName(u"path_rm_checkBox")

        self.gridLayout_2.addWidget(self.path_rm_checkBox, 6, 1, 1, 1)

        self.file_ext_label = QLabel(StringManipSettingsView)
        self.file_ext_label.setObjectName(u"file_ext_label")

        self.gridLayout_2.addWidget(self.file_ext_label, 7, 0, 1, 1)

        self.label = QLabel(StringManipSettingsView)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 6, 0, 1, 1)

        self.suffix_lineedit = QLineEdit(StringManipSettingsView)
        self.suffix_lineedit.setObjectName(u"suffix_lineedit")

        self.gridLayout_2.addWidget(self.suffix_lineedit, 2, 1, 1, 1)

        self.title = QLabel(StringManipSettingsView)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)

        self.gridLayout_2.addWidget(self.title, 0, 0, 1, 3)

        self.prefix_lineedit = QLineEdit(StringManipSettingsView)
        self.prefix_lineedit.setObjectName(u"prefix_lineedit")

        self.gridLayout_2.addWidget(self.prefix_lineedit, 1, 1, 1, 1)

        self.label_2 = QLabel(StringManipSettingsView)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 1)

        self.filename_rm_checkBox = QCheckBox(StringManipSettingsView)
        self.filename_rm_checkBox.setObjectName(u"filename_rm_checkBox")

        self.gridLayout_2.addWidget(self.filename_rm_checkBox, 5, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 36, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(StringManipSettingsView)

        QMetaObject.connectSlotsByName(StringManipSettingsView)
    # setupUi

    def retranslateUi(self, StringManipSettingsView):
        StringManipSettingsView.setWindowTitle(QCoreApplication.translate("StringManipSettingsView", u"Form", None))
        self.prefix_label.setText(QCoreApplication.translate("StringManipSettingsView", u"Prefix", None))
#if QT_CONFIG(tooltip)
        self.ext_rm_checkBox.setToolTip(QCoreApplication.translate("StringManipSettingsView", u"Check to remove the \".ext\" from the input string.", None))
#endif // QT_CONFIG(tooltip)
        self.ext_rm_checkBox.setText(QCoreApplication.translate("StringManipSettingsView", u"Remove", None))
        self.suffix_label.setText(QCoreApplication.translate("StringManipSettingsView", u"Suffix", None))
#if QT_CONFIG(tooltip)
        self.path_rm_checkBox.setToolTip(QCoreApplication.translate("StringManipSettingsView", u"Check to remove any characters before the last '/' from the input string.", None))
#endif // QT_CONFIG(tooltip)
        self.path_rm_checkBox.setText(QCoreApplication.translate("StringManipSettingsView", u"Remove", None))
        self.file_ext_label.setText(QCoreApplication.translate("StringManipSettingsView", u"File ext", None))
        self.label.setText(QCoreApplication.translate("StringManipSettingsView", u"Path", None))
#if QT_CONFIG(tooltip)
        self.suffix_lineedit.setToolTip(QCoreApplication.translate("StringManipSettingsView", u"String added to the end of the input string.", None))
#endif // QT_CONFIG(tooltip)
        self.title.setText(QCoreApplication.translate("StringManipSettingsView", u"String Manipulation settings", None))
#if QT_CONFIG(tooltip)
        self.prefix_lineedit.setToolTip(QCoreApplication.translate("StringManipSettingsView", u"String added at the beginning the input string.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("StringManipSettingsView", u"Filename", None))
        self.filename_rm_checkBox.setText(QCoreApplication.translate("StringManipSettingsView", u"Remove", None))
    # retranslateUi


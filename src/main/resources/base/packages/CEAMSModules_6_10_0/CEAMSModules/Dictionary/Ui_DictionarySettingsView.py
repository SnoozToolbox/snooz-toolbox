# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/david/projects/snooz-toolbox/src/main/python/plugins/Dictionary/Ui_DictionarySettingsView.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_DictionarySettingsView(object):
    def setupUi(self, DictionarySettingsView):
        DictionarySettingsView.setObjectName("DictionarySettingsView")
        DictionarySettingsView.resize(711, 333)
        self.verticalLayout = QtWidgets.QVBoxLayout(DictionarySettingsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.key_horizontalLayout = QtWidgets.QHBoxLayout()
        self.key_horizontalLayout.setObjectName("key_horizontalLayout")
        self.key_label = QtWidgets.QLabel(DictionarySettingsView)
        self.key_label.setObjectName("key_label")
        self.key_horizontalLayout.addWidget(self.key_label)
        self.key_lineedit = QtWidgets.QLineEdit(DictionarySettingsView)
        self.key_lineedit.setObjectName("key_lineedit")
        self.key_horizontalLayout.addWidget(self.key_lineedit)
        self.verticalLayout.addLayout(self.key_horizontalLayout)
        self.dictionary_horizontalLayout = QtWidgets.QHBoxLayout()
        self.dictionary_horizontalLayout.setObjectName("dictionary_horizontalLayout")
        self.dictionary_label = QtWidgets.QLabel(DictionarySettingsView)
        self.dictionary_label.setObjectName("dictionary_label")
        self.dictionary_horizontalLayout.addWidget(self.dictionary_label)
        self.dictionary_lineedit = QtWidgets.QLineEdit(DictionarySettingsView)
        self.dictionary_lineedit.setObjectName("dictionary_lineedit")
        self.dictionary_horizontalLayout.addWidget(self.dictionary_lineedit)
        self.verticalLayout.addLayout(self.dictionary_horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(DictionarySettingsView)
        QtCore.QMetaObject.connectSlotsByName(DictionarySettingsView)

    def retranslateUi(self, DictionarySettingsView):
        _translate = QtCore.QCoreApplication.translate
        DictionarySettingsView.setWindowTitle(_translate("DictionarySettingsView", "Form"))
        self.key_label.setText(_translate("DictionarySettingsView", "key"))
        self.dictionary_label.setText(_translate("DictionarySettingsView", "dictionary"))

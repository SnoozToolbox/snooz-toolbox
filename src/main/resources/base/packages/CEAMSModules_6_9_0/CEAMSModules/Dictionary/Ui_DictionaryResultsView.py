# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/david/projects/scinodes_poc/src/main/python/plugins/Dictionary/Ui_DictionaryResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_DictionaryResultsView(object):
    def setupUi(self, DictionaryResultsView):
        DictionaryResultsView.setObjectName("DictionaryResultsView")
        DictionaryResultsView.resize(483, 360)
        self.verticalLayout = QtWidgets.QVBoxLayout(DictionaryResultsView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.result_layout = QtWidgets.QVBoxLayout()
        self.result_layout.setObjectName("result_layout")
        self.verticalLayout.addLayout(self.result_layout)

        self.retranslateUi(DictionaryResultsView)
        QtCore.QMetaObject.connectSlotsByName(DictionaryResultsView)

    def retranslateUi(self, DictionaryResultsView):
        _translate = QtCore.QCoreApplication.translate
        DictionaryResultsView.setWindowTitle(_translate("DictionaryResultsView", "Form"))

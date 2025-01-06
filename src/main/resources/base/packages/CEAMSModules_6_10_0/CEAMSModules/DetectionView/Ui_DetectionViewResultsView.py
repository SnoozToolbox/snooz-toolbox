# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\klacourse\Documents\NGosselin\gitRepos\ceamscarms\Stand_alone_apps\snooz-toolbox\src\main\python\plugins\DetectionView\Ui_DetectionViewResultsView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qtpy import QtCore, QtGui, QtWidgets


class Ui_DetectionViewResultsView(object):
    def setupUi(self, DetectionViewResultsView):
        DetectionViewResultsView.setObjectName("DetectionViewResultsView")
        DetectionViewResultsView.resize(633, 125)
        self.gridLayout = QtWidgets.QGridLayout(DetectionViewResultsView)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(DetectionViewResultsView)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.filename_label = QtWidgets.QLabel(DetectionViewResultsView)
        self.filename_label.setObjectName("filename_label")
        self.horizontalLayout_2.addWidget(self.filename_label)
        self.filename_lineedit_2 = QtWidgets.QLineEdit(DetectionViewResultsView)
        self.filename_lineedit_2.setObjectName("filename_lineedit_2")
        self.horizontalLayout_2.addWidget(self.filename_lineedit_2)
        self.choose_but = QtWidgets.QPushButton(DetectionViewResultsView)
        self.choose_but.setObjectName("choose_but")
        self.horizontalLayout_2.addWidget(self.choose_but)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.time_label = QtWidgets.QLabel(DetectionViewResultsView)
        self.time_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout.addWidget(self.time_label)
        self.time_lineedit = QLineEditLive(DetectionViewResultsView)
        self.time_lineedit.setText("00:00:0.0")
        self.time_lineedit.setObjectName("time_lineedit")
        self.horizontalLayout.addWidget(self.time_lineedit)
        self.prev_but = QtWidgets.QPushButton(DetectionViewResultsView)
        self.prev_but.setEnabled(False)
        self.prev_but.setObjectName("prev_but")
        self.horizontalLayout.addWidget(self.prev_but)
        self.next_but = QtWidgets.QPushButton(DetectionViewResultsView)
        self.next_but.setEnabled(False)
        self.next_but.setObjectName("next_but")
        self.horizontalLayout.addWidget(self.next_but)
        self.label = QtWidgets.QLabel(DetectionViewResultsView)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.win_len_lineEdit = QtWidgets.QLineEdit(DetectionViewResultsView)
        self.win_len_lineEdit.setObjectName("win_len_lineEdit")
        self.horizontalLayout.addWidget(self.win_len_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.result_layout = QtWidgets.QVBoxLayout()
        self.result_layout.setObjectName("result_layout")
        self.verticalLayout.addLayout(self.result_layout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(DetectionViewResultsView)
        self.choose_but.clicked.connect(DetectionViewResultsView.on_choose_button)
        self.next_but.clicked.connect(DetectionViewResultsView.on_next_button)
        self.prev_but.clicked.connect(DetectionViewResultsView.on_prev_button)
        self.time_lineedit.returnPressed.connect(DetectionViewResultsView.on_show_button)
        self.win_len_lineEdit.returnPressed.connect(DetectionViewResultsView.on_show_button)
        QtCore.QMetaObject.connectSlotsByName(DetectionViewResultsView)

    def retranslateUi(self, DetectionViewResultsView):
        _translate = QtCore.QCoreApplication.translate
        DetectionViewResultsView.setWindowTitle(_translate("DetectionViewResultsView", "Form"))
        self.label_2.setText(_translate("DetectionViewResultsView", "To display an additional detection window"))
        self.filename_label.setText(_translate("DetectionViewResultsView", "Filename"))
        self.filename_lineedit_2.setToolTip(_translate("DetectionViewResultsView", "Python filename to load to display detection window."))
        self.choose_but.setToolTip(_translate("DetectionViewResultsView", "Browse the Python filename to load data to display an additional detection window."))
        self.choose_but.setText(_translate("DetectionViewResultsView", "Choose"))
        self.time_label.setText(_translate("DetectionViewResultsView", "Time elapsed (HH:MM:SS)"))
        self.time_lineedit.setToolTip(_translate("DetectionViewResultsView", "Time elapsed since the beginning of the recording (ex. 01:10:5.5)\n"
"Press enter to display the detection window."))
        self.prev_but.setToolTip(_translate("DetectionViewResultsView", "Display the previous window (window length will be added to the time elapsed)."))
        self.prev_but.setText(_translate("DetectionViewResultsView", "<<"))
        self.next_but.setToolTip(_translate("DetectionViewResultsView", "Display the next window (window length will be added to the time elapsed)."))
        self.next_but.setText(_translate("DetectionViewResultsView", ">>"))
        self.label.setText(_translate("DetectionViewResultsView", "Window length"))
        self.win_len_lineEdit.setToolTip(_translate("DetectionViewResultsView", "Time window length to show. \n"
"Press enter to display the detection window."))
        self.win_len_lineEdit.setText(_translate("DetectionViewResultsView", "30"))
from widgets.QLineEditLive import QLineEditLive

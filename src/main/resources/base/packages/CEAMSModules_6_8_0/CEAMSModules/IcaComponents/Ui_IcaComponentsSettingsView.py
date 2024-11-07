# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_IcaComponentsSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_IcaComponentsSettingsView(object):
    def setupUi(self, IcaComponentsSettingsView):
        if not IcaComponentsSettingsView.objectName():
            IcaComponentsSettingsView.setObjectName(u"IcaComponentsSettingsView")
        IcaComponentsSettingsView.setEnabled(True)
        IcaComponentsSettingsView.resize(791, 487)
        IcaComponentsSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout_3 = QHBoxLayout(IcaComponentsSettingsView)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(IcaComponentsSettingsView)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)

        self.verticalLayout.addWidget(self.label_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.radioButton_infomax = QRadioButton(IcaComponentsSettingsView)
        self.algo_ICA_radio_group = QButtonGroup(IcaComponentsSettingsView)
        self.algo_ICA_radio_group.setObjectName(u"algo_ICA_radio_group")
        self.algo_ICA_radio_group.addButton(self.radioButton_infomax)
        self.radioButton_infomax.setObjectName(u"radioButton_infomax")
        self.radioButton_infomax.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButton_infomax)

        self.radioButton_fastICA = QRadioButton(IcaComponentsSettingsView)
        self.algo_ICA_radio_group.addButton(self.radioButton_fastICA)
        self.radioButton_fastICA.setObjectName(u"radioButton_fastICA")
        self.radioButton_fastICA.setFont(font)

        self.horizontalLayout_2.addWidget(self.radioButton_fastICA)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_5 = QLabel(IcaComponentsSettingsView)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(IcaComponentsSettingsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.algorithm_comboBox = QComboBox(IcaComponentsSettingsView)
        self.algorithm_comboBox.addItem("")
        self.algorithm_comboBox.addItem("")
        self.algorithm_comboBox.setObjectName(u"algorithm_comboBox")
        self.algorithm_comboBox.setEnabled(False)
        self.algorithm_comboBox.setFont(font)

        self.gridLayout.addWidget(self.algorithm_comboBox, 0, 1, 1, 1)

        self.label_3 = QLabel(IcaComponentsSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.max_iter_spinBox = QSpinBox(IcaComponentsSettingsView)
        self.max_iter_spinBox.setObjectName(u"max_iter_spinBox")
        self.max_iter_spinBox.setEnabled(False)
        self.max_iter_spinBox.setFont(font)
        self.max_iter_spinBox.setMaximum(10000)
        self.max_iter_spinBox.setSingleStep(100)
        self.max_iter_spinBox.setValue(1000)

        self.gridLayout.addWidget(self.max_iter_spinBox, 3, 1, 1, 1)

        self.random_state_spinBox = QSpinBox(IcaComponentsSettingsView)
        self.random_state_spinBox.setObjectName(u"random_state_spinBox")
        self.random_state_spinBox.setEnabled(False)
        self.random_state_spinBox.setFont(font)

        self.gridLayout.addWidget(self.random_state_spinBox, 5, 1, 1, 1)

        self.random_state_checkBox = QCheckBox(IcaComponentsSettingsView)
        self.random_state_checkBox.setObjectName(u"random_state_checkBox")
        self.random_state_checkBox.setFont(font)
        self.random_state_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.random_state_checkBox, 5, 2, 1, 1)

        self.whiten_comboBox = QComboBox(IcaComponentsSettingsView)
        self.whiten_comboBox.addItem("")
        self.whiten_comboBox.addItem("")
        self.whiten_comboBox.addItem("")
        self.whiten_comboBox.setObjectName(u"whiten_comboBox")
        self.whiten_comboBox.setEnabled(False)
        self.whiten_comboBox.setMinimumSize(QSize(140, 0))
        self.whiten_comboBox.setFont(font)

        self.gridLayout.addWidget(self.whiten_comboBox, 1, 1, 1, 1)

        self.label_10 = QLabel(IcaComponentsSettingsView)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_2 = QLabel(IcaComponentsSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.fun_comboBox = QComboBox(IcaComponentsSettingsView)
        self.fun_comboBox.addItem("")
        self.fun_comboBox.addItem("")
        self.fun_comboBox.addItem("")
        self.fun_comboBox.setObjectName(u"fun_comboBox")
        self.fun_comboBox.setEnabled(False)
        self.fun_comboBox.setFont(font)

        self.gridLayout.addWidget(self.fun_comboBox, 2, 1, 1, 1)

        self.tol_doubleSpinBox = QDoubleSpinBox(IcaComponentsSettingsView)
        self.tol_doubleSpinBox.setObjectName(u"tol_doubleSpinBox")
        self.tol_doubleSpinBox.setEnabled(False)
        self.tol_doubleSpinBox.setFont(font)
        self.tol_doubleSpinBox.setDecimals(5)
        self.tol_doubleSpinBox.setMinimum(0.000000000000000)
        self.tol_doubleSpinBox.setMaximum(1.000000000000000)
        self.tol_doubleSpinBox.setSingleStep(0.000100000000000)
        self.tol_doubleSpinBox.setValue(0.000100000000000)

        self.gridLayout.addWidget(self.tol_doubleSpinBox, 4, 1, 1, 1)

        self.label_7 = QLabel(IcaComponentsSettingsView)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_6 = QLabel(IcaComponentsSettingsView)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 156, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(194, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.retranslateUi(IcaComponentsSettingsView)
        self.random_state_checkBox.clicked.connect(IcaComponentsSettingsView.random_state_changed)
        self.algo_ICA_radio_group.buttonClicked.connect(IcaComponentsSettingsView.ICA_algorithms_slot)

        QMetaObject.connectSlotsByName(IcaComponentsSettingsView)
    # setupUi

    def retranslateUi(self, IcaComponentsSettingsView):
        IcaComponentsSettingsView.setWindowTitle(QCoreApplication.translate("IcaComponentsSettingsView", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("IcaComponentsSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Algorithm to extract the components</span></p></body></html>", None))
        self.radioButton_infomax.setText(QCoreApplication.translate("IcaComponentsSettingsView", u"Info Max", None))
        self.radioButton_fastICA.setText(QCoreApplication.translate("IcaComponentsSettingsView", u"Fast ICA", None))
        self.label_5.setText(QCoreApplication.translate("IcaComponentsSettingsView", u"<html><head/><body><p><span style=\" font-weight:600;\">Settings</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("IcaComponentsSettingsView", u"Functional form used in the approximation to neg-entropy", None))
        self.algorithm_comboBox.setItemText(0, QCoreApplication.translate("IcaComponentsSettingsView", u"deflation", None))
        self.algorithm_comboBox.setItemText(1, QCoreApplication.translate("IcaComponentsSettingsView", u"parallel", None))

#if QT_CONFIG(tooltip)
        self.algorithm_comboBox.setToolTip(QCoreApplication.translate("IcaComponentsSettingsView", u"Apply parallel or deflational algorithm for FastICA. Valid value are : 'parallel',  'deflation'", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("IcaComponentsSettingsView", u"Whitening strategy to use", None))
#if QT_CONFIG(tooltip)
        self.max_iter_spinBox.setToolTip(QCoreApplication.translate("IcaComponentsSettingsView", u"Maximum number of iterations during fit.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.random_state_spinBox.setToolTip(QCoreApplication.translate("IcaComponentsSettingsView", u"Used to initialize ``w_init`` when not specified, with anormal distribution. Pass an int, for reproducible results across multiple function calls.", None))
#endif // QT_CONFIG(tooltip)
        self.random_state_checkBox.setText(QCoreApplication.translate("IcaComponentsSettingsView", u"None", None))
        self.whiten_comboBox.setItemText(0, QCoreApplication.translate("IcaComponentsSettingsView", u"arbitrary-variance", None))
        self.whiten_comboBox.setItemText(1, QCoreApplication.translate("IcaComponentsSettingsView", u"unit-variance", None))
        self.whiten_comboBox.setItemText(2, QCoreApplication.translate("IcaComponentsSettingsView", u"False", None))

#if QT_CONFIG(tooltip)
        self.whiten_comboBox.setToolTip(QCoreApplication.translate("IcaComponentsSettingsView", u"If whiten is false, the data is already considered to be whitened, and no whitening is performed.", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("IcaComponentsSettingsView", u"Random state to init the un-mixing array.\n"
"Pass an int, for reproducible results.\n"
"If None, values are from a normal distribution.", None))
        self.label_2.setText(QCoreApplication.translate("IcaComponentsSettingsView", u"Fast ICA algorithm", None))
        self.fun_comboBox.setItemText(0, QCoreApplication.translate("IcaComponentsSettingsView", u"cube", None))
        self.fun_comboBox.setItemText(1, QCoreApplication.translate("IcaComponentsSettingsView", u"logcosh", None))
        self.fun_comboBox.setItemText(2, QCoreApplication.translate("IcaComponentsSettingsView", u"exp", None))

#if QT_CONFIG(tooltip)
        self.fun_comboBox.setToolTip(QCoreApplication.translate("IcaComponentsSettingsView", u"The functional form of the G function used in the approximation to neg-entropy. Could be either 'logcosh', 'exp', or 'cube'.\n"
"            ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.tol_doubleSpinBox.setToolTip(QCoreApplication.translate("IcaComponentsSettingsView", u"Tolerance on update at each iteration.", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("IcaComponentsSettingsView", u"Convergence tolerance ", None))
        self.label_6.setText(QCoreApplication.translate("IcaComponentsSettingsView", u"Maximum number of iterations during fit", None))
    # retranslateUi


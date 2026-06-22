# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_IRASAYASASettingsView.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_IRASAYASASettingsView(object):
    def setupUi(self, IRASAYASASettingsView):
        if not IRASAYASASettingsView.objectName():
            IRASAYASASettingsView.setObjectName(u"IRASAYASASettingsView")
        IRASAYASASettingsView.resize(711, 333)
        IRASAYASASettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(IRASAYASASettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signals_horizontalLayout = QHBoxLayout()
        self.signals_horizontalLayout.setObjectName(u"signals_horizontalLayout")
        self.signals_label = QLabel(IRASAYASASettingsView)
        self.signals_label.setObjectName(u"signals_label")

        self.signals_horizontalLayout.addWidget(self.signals_label)

        self.signals_lineedit = QLineEdit(IRASAYASASettingsView)
        self.signals_lineedit.setObjectName(u"signals_lineedit")

        self.signals_horizontalLayout.addWidget(self.signals_lineedit)


        self.verticalLayout.addLayout(self.signals_horizontalLayout)

        self.win_len_sec_horizontalLayout = QHBoxLayout()
        self.win_len_sec_horizontalLayout.setObjectName(u"win_len_sec_horizontalLayout")
        self.win_len_sec_label = QLabel(IRASAYASASettingsView)
        self.win_len_sec_label.setObjectName(u"win_len_sec_label")

        self.win_len_sec_horizontalLayout.addWidget(self.win_len_sec_label)

        self.win_len_sec_lineedit = QLineEdit(IRASAYASASettingsView)
        self.win_len_sec_lineedit.setObjectName(u"win_len_sec_lineedit")

        self.win_len_sec_horizontalLayout.addWidget(self.win_len_sec_lineedit)


        self.verticalLayout.addLayout(self.win_len_sec_horizontalLayout)

        self.win_step_sec_horizontalLayout = QHBoxLayout()
        self.win_step_sec_horizontalLayout.setObjectName(u"win_step_sec_horizontalLayout")
        self.win_step_sec_label = QLabel(IRASAYASASettingsView)
        self.win_step_sec_label.setObjectName(u"win_step_sec_label")

        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_label)

        self.win_step_sec_lineedit = QLineEdit(IRASAYASASettingsView)
        self.win_step_sec_lineedit.setObjectName(u"win_step_sec_lineedit")

        self.win_step_sec_horizontalLayout.addWidget(self.win_step_sec_lineedit)


        self.verticalLayout.addLayout(self.win_step_sec_horizontalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.window_name_label = QLabel(IRASAYASASettingsView)
        self.window_name_label.setObjectName(u"window_name_label")

        self.horizontalLayout.addWidget(self.window_name_label)

        self.window_name_comboBox = QComboBox(IRASAYASASettingsView)
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.addItem("")
        self.window_name_comboBox.setObjectName(u"window_name_comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.window_name_comboBox.sizePolicy().hasHeightForWidth())
        self.window_name_comboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.window_name_comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.first_freq_horizontalLayout = QHBoxLayout()
        self.first_freq_horizontalLayout.setObjectName(u"first_freq_horizontalLayout")
        self.first_freq_label = QLabel(IRASAYASASettingsView)
        self.first_freq_label.setObjectName(u"first_freq_label")

        self.first_freq_horizontalLayout.addWidget(self.first_freq_label)

        self.first_freq_lineedit = QLineEdit(IRASAYASASettingsView)
        self.first_freq_lineedit.setObjectName(u"first_freq_lineedit")

        self.first_freq_horizontalLayout.addWidget(self.first_freq_lineedit)


        self.verticalLayout.addLayout(self.first_freq_horizontalLayout)

        self.last_freq_horizontalLayout = QHBoxLayout()
        self.last_freq_horizontalLayout.setObjectName(u"last_freq_horizontalLayout")
        self.last_freq_label = QLabel(IRASAYASASettingsView)
        self.last_freq_label.setObjectName(u"last_freq_label")

        self.last_freq_horizontalLayout.addWidget(self.last_freq_label)

        self.last_freq_lineedit = QLineEdit(IRASAYASASettingsView)
        self.last_freq_lineedit.setObjectName(u"last_freq_lineedit")

        self.last_freq_horizontalLayout.addWidget(self.last_freq_lineedit)


        self.verticalLayout.addLayout(self.last_freq_horizontalLayout)

        self.flag_horizontalLayout = QHBoxLayout()
        self.flag_horizontalLayout.setObjectName(u"flag_horizontalLayout")
        self.flag_label = QLabel(IRASAYASASettingsView)
        self.flag_label.setObjectName(u"flag_label")

        self.flag_horizontalLayout.addWidget(self.flag_label)

        self.flag_lineedit = QLineEdit(IRASAYASASettingsView)
        self.flag_lineedit.setObjectName(u"flag_lineedit")

        self.flag_horizontalLayout.addWidget(self.flag_lineedit)


        self.verticalLayout.addLayout(self.flag_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(IRASAYASASettingsView)

        QMetaObject.connectSlotsByName(IRASAYASASettingsView)
    # setupUi

    def retranslateUi(self, IRASAYASASettingsView):
        IRASAYASASettingsView.setWindowTitle(QCoreApplication.translate("IRASAYASASettingsView", u"Form", None))
        self.signals_label.setText(QCoreApplication.translate("IRASAYASASettingsView", u"signals", None))
        self.win_len_sec_label.setText(QCoreApplication.translate("IRASAYASASettingsView", u"win_len_sec", None))
        self.win_step_sec_label.setText(QCoreApplication.translate("IRASAYASASettingsView", u"win_step_sec", None))
        self.window_name_label.setText(QCoreApplication.translate("IRASAYASASettingsView", u"window_name", None))
        self.window_name_comboBox.setItemText(0, QCoreApplication.translate("IRASAYASASettingsView", u"boxcar", None))
        self.window_name_comboBox.setItemText(1, QCoreApplication.translate("IRASAYASASettingsView", u"trlang", None))
        self.window_name_comboBox.setItemText(2, QCoreApplication.translate("IRASAYASASettingsView", u"blackman", None))
        self.window_name_comboBox.setItemText(3, QCoreApplication.translate("IRASAYASASettingsView", u"hamming", None))
        self.window_name_comboBox.setItemText(4, QCoreApplication.translate("IRASAYASASettingsView", u"hann", None))
        self.window_name_comboBox.setItemText(5, QCoreApplication.translate("IRASAYASASettingsView", u"bartlett", None))
        self.window_name_comboBox.setItemText(6, QCoreApplication.translate("IRASAYASASettingsView", u"flattop", None))
        self.window_name_comboBox.setItemText(7, QCoreApplication.translate("IRASAYASASettingsView", u"parzen", None))
        self.window_name_comboBox.setItemText(8, QCoreApplication.translate("IRASAYASASettingsView", u"bohman", None))
        self.window_name_comboBox.setItemText(9, QCoreApplication.translate("IRASAYASASettingsView", u"blackmanharris", None))
        self.window_name_comboBox.setItemText(10, QCoreApplication.translate("IRASAYASASettingsView", u"nuttall", None))
        self.window_name_comboBox.setItemText(11, QCoreApplication.translate("IRASAYASASettingsView", u"barthann", None))
        self.window_name_comboBox.setItemText(12, QCoreApplication.translate("IRASAYASASettingsView", u"kasier", None))
        self.window_name_comboBox.setItemText(13, QCoreApplication.translate("IRASAYASASettingsView", u"gaussian", None))
        self.window_name_comboBox.setItemText(14, QCoreApplication.translate("IRASAYASASettingsView", u"general_gaussian", None))
        self.window_name_comboBox.setItemText(15, QCoreApplication.translate("IRASAYASASettingsView", u"dpss", None))
        self.window_name_comboBox.setItemText(16, QCoreApplication.translate("IRASAYASASettingsView", u"chebwin", None))
        self.window_name_comboBox.setItemText(17, QCoreApplication.translate("IRASAYASASettingsView", u"exponential", None))
        self.window_name_comboBox.setItemText(18, QCoreApplication.translate("IRASAYASASettingsView", u"tukey", None))
        self.window_name_comboBox.setItemText(19, QCoreApplication.translate("IRASAYASASettingsView", u"taylor", None))

        self.window_name_comboBox.setCurrentText(QCoreApplication.translate("IRASAYASASettingsView", u"hann", None))
        self.first_freq_label.setText(QCoreApplication.translate("IRASAYASASettingsView", u"first_freq", None))
        self.last_freq_label.setText(QCoreApplication.translate("IRASAYASASettingsView", u"last_freq", None))
        self.flag_label.setText(QCoreApplication.translate("IRASAYASASettingsView", u"flag", None))
    # retranslateUi


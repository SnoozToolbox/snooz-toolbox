# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file ''
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from widgets.QCheckBoxLive import QCheckBoxLive
from widgets.QComboBoxLive import QComboBoxLive
from widgets.QLineEditLive import QLineEditLive

class Ui_StftSettingsView(object):
    def setupUi(self, StftSettingsView):
        if not StftSettingsView.objectName():
            StftSettingsView.setObjectName(u"StftSettingsView")
        StftSettingsView.resize(331, 275)
        self.gridLayout_2 = QGridLayout(StftSettingsView)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(StftSettingsView)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label = QLabel(StftSettingsView)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.window_len_lineedit = QLineEditLive(StftSettingsView)
        self.window_len_lineedit.setObjectName(u"window_len_lineedit")

        self.gridLayout.addWidget(self.window_len_lineedit, 1, 1, 1, 2)

        self.label_6 = QLabel(StftSettingsView)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.window_step_lineedit = QLineEditLive(StftSettingsView)
        self.window_step_lineedit.setObjectName(u"window_step_lineedit")

        self.gridLayout.addWidget(self.window_step_lineedit, 2, 1, 1, 2)

        self.label_4 = QLabel(StftSettingsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.zero_padding_checkbox = QCheckBoxLive(StftSettingsView)
        self.zero_padding_checkbox.setObjectName(u"zero_padding_checkbox")
        self.zero_padding_checkbox.setEnabled(False)

        self.gridLayout.addWidget(self.zero_padding_checkbox, 3, 1, 1, 1)

        self.label_3 = QLabel(StftSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.window_combobox = QComboBoxLive(StftSettingsView)
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.addItem("")
        self.window_combobox.setObjectName(u"window_combobox")

        self.gridLayout.addWidget(self.window_combobox, 4, 1, 1, 2)

        self.label_9 = QLabel(StftSettingsView)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)

        self.label_7 = QLabel(StftSettingsView)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.remove_means_checkbox = QCheckBoxLive(StftSettingsView)
        self.remove_means_checkbox.setObjectName(u"remove_means_checkbox")
        self.remove_means_checkbox.setChecked(True)

        self.gridLayout.addWidget(self.remove_means_checkbox, 6, 1, 1, 1)

        self.label_8 = QLabel(StftSettingsView)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.norm_combobox = QComboBoxLive(StftSettingsView)
        self.norm_combobox.addItem("")
        self.norm_combobox.addItem("")
        self.norm_combobox.addItem("")
        self.norm_combobox.addItem("")
        self.norm_combobox.setObjectName(u"norm_combobox")

        self.gridLayout.addWidget(self.norm_combobox, 7, 1, 1, 2)

        self.label_2 = QLabel(StftSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 8, 0, 1, 1)

        self.label_10 = QLabel(StftSettingsView)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.filename_lineEdit = QLineEditLive(StftSettingsView)
        self.filename_lineEdit.setObjectName(u"filename_lineEdit")

        self.gridLayout.addWidget(self.filename_lineEdit, 9, 1, 1, 1)

        self.choose_pb = QPushButton(StftSettingsView)
        self.choose_pb.setObjectName(u"choose_pb")

        self.gridLayout.addWidget(self.choose_pb, 9, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 78, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(StftSettingsView)
        self.choose_pb.clicked.connect(StftSettingsView.on_choose)

        self.window_combobox.setCurrentIndex(4)
        self.norm_combobox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StftSettingsView)
    # setupUi

    def retranslateUi(self, StftSettingsView):
        StftSettingsView.setWindowTitle(QCoreApplication.translate("StftSettingsView", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("StftSettingsView", u"FFT settings", None))
        self.label.setText(QCoreApplication.translate("StftSettingsView", u"Window length (sec)", None))
        self.label_6.setText(QCoreApplication.translate("StftSettingsView", u"Window step (sec)", None))
        self.label_4.setText(QCoreApplication.translate("StftSettingsView", u"Zero padding", None))
        self.zero_padding_checkbox.setText("")
        self.label_3.setText(QCoreApplication.translate("StftSettingsView", u"Window", None))
        self.window_combobox.setItemText(0, QCoreApplication.translate("StftSettingsView", u"boxcar", None))
        self.window_combobox.setItemText(1, QCoreApplication.translate("StftSettingsView", u"trlang", None))
        self.window_combobox.setItemText(2, QCoreApplication.translate("StftSettingsView", u"blackman", None))
        self.window_combobox.setItemText(3, QCoreApplication.translate("StftSettingsView", u"hamming", None))
        self.window_combobox.setItemText(4, QCoreApplication.translate("StftSettingsView", u"hann", None))
        self.window_combobox.setItemText(5, QCoreApplication.translate("StftSettingsView", u"bartlett", None))
        self.window_combobox.setItemText(6, QCoreApplication.translate("StftSettingsView", u"flattop", None))
        self.window_combobox.setItemText(7, QCoreApplication.translate("StftSettingsView", u"parzen", None))
        self.window_combobox.setItemText(8, QCoreApplication.translate("StftSettingsView", u"bohman", None))
        self.window_combobox.setItemText(9, QCoreApplication.translate("StftSettingsView", u"blackmanharris", None))
        self.window_combobox.setItemText(10, QCoreApplication.translate("StftSettingsView", u"nuttall", None))
        self.window_combobox.setItemText(11, QCoreApplication.translate("StftSettingsView", u"barthann", None))
        self.window_combobox.setItemText(12, QCoreApplication.translate("StftSettingsView", u"kaiser", None))
        self.window_combobox.setItemText(13, QCoreApplication.translate("StftSettingsView", u"gaussian", None))
        self.window_combobox.setItemText(14, QCoreApplication.translate("StftSettingsView", u"general_gaussian", None))
        self.window_combobox.setItemText(15, QCoreApplication.translate("StftSettingsView", u"dpss", None))
        self.window_combobox.setItemText(16, QCoreApplication.translate("StftSettingsView", u"chebwin", None))
        self.window_combobox.setItemText(17, QCoreApplication.translate("StftSettingsView", u"exponential", None))
        self.window_combobox.setItemText(18, QCoreApplication.translate("StftSettingsView", u"tukey", None))
        self.window_combobox.setItemText(19, QCoreApplication.translate("StftSettingsView", u"taylor", None))

        self.window_combobox.setCurrentText(QCoreApplication.translate("StftSettingsView", u"hann", None))
        self.label_9.setText(QCoreApplication.translate("StftSettingsView", u"Normalisation", None))
        self.label_7.setText(QCoreApplication.translate("StftSettingsView", u"Remove means", None))
        self.remove_means_checkbox.setText("")
        self.label_8.setText(QCoreApplication.translate("StftSettingsView", u"Normalisation", None))
        self.norm_combobox.setItemText(0, QCoreApplication.translate("StftSettingsView", u"integrate", None))
        self.norm_combobox.setItemText(1, QCoreApplication.translate("StftSettingsView", u"rms", None))
        self.norm_combobox.setItemText(2, QCoreApplication.translate("StftSettingsView", u"noise", None))
        self.norm_combobox.setItemText(3, QCoreApplication.translate("StftSettingsView", u"no", None))

        self.norm_combobox.setCurrentText(QCoreApplication.translate("StftSettingsView", u"integrate", None))
        self.label_2.setText(QCoreApplication.translate("StftSettingsView", u"Output", None))
        self.label_10.setText(QCoreApplication.translate("StftSettingsView", u"python filename", None))
        self.choose_pb.setText(QCoreApplication.translate("StftSettingsView", u"Choose", None))
    # retranslateUi


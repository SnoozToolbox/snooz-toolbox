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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from widgets.QComboBoxLive import QComboBoxLive
from widgets.QLineEditLive import QLineEditLive

class Ui_DetectionViewSettingsView(object):
    def setupUi(self, DetectionViewSettingsView):
        if not DetectionViewSettingsView.objectName():
            DetectionViewSettingsView.setObjectName(u"DetectionViewSettingsView")
        DetectionViewSettingsView.resize(572, 333)
        self.gridLayout_2 = QGridLayout(DetectionViewSettingsView)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Title_label = QLabel(DetectionViewSettingsView)
        self.Title_label.setObjectName(u"Title_label")
        font = QFont()
        font.setBold(True)
        self.Title_label.setFont(font)
        self.Title_label.setLayoutDirection(Qt.LeftToRight)
        self.Title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.Title_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(DetectionViewSettingsView)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.time_label = QLabel(DetectionViewSettingsView)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setLayoutDirection(Qt.LeftToRight)
        self.time_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.time_label, 0, 0, 1, 1)

        self.time_lineedit = QLineEditLive(DetectionViewSettingsView)
        self.time_lineedit.setObjectName(u"time_lineedit")

        self.gridLayout.addWidget(self.time_lineedit, 0, 1, 1, 2)

        self.win_show_label = QLabel(DetectionViewSettingsView)
        self.win_show_label.setObjectName(u"win_show_label")
        self.win_show_label.setLayoutDirection(Qt.LeftToRight)
        self.win_show_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.win_show_label, 1, 0, 1, 1)

        self.win_show_lineedit = QLineEditLive(DetectionViewSettingsView)
        self.win_show_lineedit.setObjectName(u"win_show_lineedit")

        self.gridLayout.addWidget(self.win_show_lineedit, 1, 1, 1, 2)

        self.event_label = QLabel(DetectionViewSettingsView)
        self.event_label.setObjectName(u"event_label")
        self.event_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.event_label, 2, 0, 1, 1)

        self.event_lineEdit = QLineEditLive(DetectionViewSettingsView)
        self.event_lineEdit.setObjectName(u"event_lineEdit")

        self.gridLayout.addWidget(self.event_lineEdit, 2, 1, 1, 2)

        self.chan_label = QLabel(DetectionViewSettingsView)
        self.chan_label.setObjectName(u"chan_label")
        self.chan_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.chan_label, 3, 0, 1, 1)

        self.channel_lineedit = QLineEditLive(DetectionViewSettingsView)
        self.channel_lineedit.setObjectName(u"channel_lineedit")

        self.gridLayout.addWidget(self.channel_lineedit, 3, 1, 1, 2)

        self.windet_step_label = QLabel(DetectionViewSettingsView)
        self.windet_step_label.setObjectName(u"windet_step_label")
        self.windet_step_label.setLayoutDirection(Qt.LeftToRight)
        self.windet_step_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.windet_step_label, 4, 0, 1, 1)

        self.windet_step_lineedit = QLineEditLive(DetectionViewSettingsView)
        self.windet_step_lineedit.setObjectName(u"windet_step_lineedit")

        self.gridLayout.addWidget(self.windet_step_lineedit, 4, 1, 1, 2)

        self.thresh_label = QLabel(DetectionViewSettingsView)
        self.thresh_label.setObjectName(u"thresh_label")
        self.thresh_label.setLayoutDirection(Qt.LeftToRight)
        self.thresh_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.thresh_label, 5, 0, 1, 1)

        self.thresh_lineedit = QLineEditLive(DetectionViewSettingsView)
        self.thresh_lineedit.setObjectName(u"thresh_lineedit")

        self.gridLayout.addWidget(self.thresh_lineedit, 5, 1, 1, 1)

        self.threshUnit_comboBox = QComboBoxLive(DetectionViewSettingsView)
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.setObjectName(u"threshUnit_comboBox")

        self.gridLayout.addWidget(self.threshUnit_comboBox, 5, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(DetectionViewSettingsView)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(DetectionViewSettingsView)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.filename_lineedit = QLineEditLive(DetectionViewSettingsView)
        self.filename_lineedit.setObjectName(u"filename_lineedit")

        self.horizontalLayout_2.addWidget(self.filename_lineedit)

        self.ChooseBut = QPushButton(DetectionViewSettingsView)
        self.ChooseBut.setObjectName(u"ChooseBut")

        self.horizontalLayout_2.addWidget(self.ChooseBut)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(DetectionViewSettingsView)
        self.ChooseBut.clicked.connect(DetectionViewSettingsView.on_choose)

        QMetaObject.connectSlotsByName(DetectionViewSettingsView)
    # setupUi

    def retranslateUi(self, DetectionViewSettingsView):
        DetectionViewSettingsView.setWindowTitle(QCoreApplication.translate("DetectionViewSettingsView", u"Form", None))
        self.Title_label.setText(QCoreApplication.translate("DetectionViewSettingsView", u"Detection View settings", None))
        self.label_3.setText(QCoreApplication.translate("DetectionViewSettingsView", u"-------- Input Settings -----------------------------------------------------", None))
        self.time_label.setText(QCoreApplication.translate("DetectionViewSettingsView", u"Time elapsed (HH:MM:SS)", None))
#if QT_CONFIG(tooltip)
        self.time_lineedit.setToolTip(QCoreApplication.translate("DetectionViewSettingsView", u"Time elapsed since the beginning of the recording (ex. 01:10:5.5)", None))
#endif // QT_CONFIG(tooltip)
        self.win_show_label.setText(QCoreApplication.translate("DetectionViewSettingsView", u"Window length to show (s)", None))
#if QT_CONFIG(tooltip)
        self.win_show_lineedit.setToolTip(QCoreApplication.translate("DetectionViewSettingsView", u"Window length to display in second.", None))
#endif // QT_CONFIG(tooltip)
        self.win_show_lineedit.setText("")
        self.event_label.setText(QCoreApplication.translate("DetectionViewSettingsView", u"Event name", None))
        self.chan_label.setText(QCoreApplication.translate("DetectionViewSettingsView", u"Channel selection", None))
#if QT_CONFIG(tooltip)
        self.channel_lineedit.setToolTip(QCoreApplication.translate("DetectionViewSettingsView", u"Single channel label to display (ex. EEG C3)", None))
#endif // QT_CONFIG(tooltip)
        self.channel_lineedit.setText("")
#if QT_CONFIG(tooltip)
        self.windet_step_label.setToolTip(QCoreApplication.translate("DetectionViewSettingsView", u"Window step in second used to detect events.", None))
#endif // QT_CONFIG(tooltip)
        self.windet_step_label.setText(QCoreApplication.translate("DetectionViewSettingsView", u"Detection window step (s)", None))
        self.windet_step_lineedit.setText("")
        self.thresh_label.setText(QCoreApplication.translate("DetectionViewSettingsView", u"Threshold", None))
#if QT_CONFIG(tooltip)
        self.thresh_lineedit.setToolTip(QCoreApplication.translate("DetectionViewSettingsView", u"Threshold used to detect events.", None))
#endif // QT_CONFIG(tooltip)
        self.thresh_lineedit.setText("")
        self.threshUnit_comboBox.setItemText(0, QCoreApplication.translate("DetectionViewSettingsView", u"fixed", None))
        self.threshUnit_comboBox.setItemText(1, QCoreApplication.translate("DetectionViewSettingsView", u"x BSL median", None))
        self.threshUnit_comboBox.setItemText(2, QCoreApplication.translate("DetectionViewSettingsView", u"x BSL STD", None))
        self.threshUnit_comboBox.setItemText(3, QCoreApplication.translate("DetectionViewSettingsView", u"x BSL STD (log10)", None))

#if QT_CONFIG(tooltip)
        self.threshUnit_comboBox.setToolTip(QCoreApplication.translate("DetectionViewSettingsView", u"Select threshold unit : fixed (as \u00b5V\u00b2), x times the baseline median or x times the baseline standard deviation.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("DetectionViewSettingsView", u"-------- Output Settings ---------------------------------------------------", None))
        self.label.setText(QCoreApplication.translate("DetectionViewSettingsView", u"Filename", None))
#if QT_CONFIG(tooltip)
        self.filename_lineedit.setToolTip(QCoreApplication.translate("DetectionViewSettingsView", u"Python filename to save the detection information and signal to display.", None))
#endif // QT_CONFIG(tooltip)
        self.filename_lineedit.setText("")
#if QT_CONFIG(tooltip)
        self.ChooseBut.setToolTip(QCoreApplication.translate("DetectionViewSettingsView", u"Browse the filename to save.", None))
#endif // QT_CONFIG(tooltip)
        self.ChooseBut.setText(QCoreApplication.translate("DetectionViewSettingsView", u"Choose", None))
    # retranslateUi


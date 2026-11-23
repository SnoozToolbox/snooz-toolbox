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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_AmplitudeDetectorSettingsView(object):
    def setupUi(self, AmplitudeDetectorSettingsView):
        if not AmplitudeDetectorSettingsView.objectName():
            AmplitudeDetectorSettingsView.setObjectName(u"AmplitudeDetectorSettingsView")
        AmplitudeDetectorSettingsView.resize(376, 217)
        self.gridLayout_2 = QGridLayout(AmplitudeDetectorSettingsView)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(AmplitudeDetectorSettingsView)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(AmplitudeDetectorSettingsView)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.event_name_lineedit = QLineEdit(AmplitudeDetectorSettingsView)
        self.event_name_lineedit.setObjectName(u"event_name_lineedit")

        self.gridLayout.addWidget(self.event_name_lineedit, 1, 1, 1, 2)

        self.label_2 = QLabel(AmplitudeDetectorSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.pad_length_lineedit = QLineEdit(AmplitudeDetectorSettingsView)
        self.pad_length_lineedit.setObjectName(u"pad_length_lineedit")

        self.gridLayout.addWidget(self.pad_length_lineedit, 2, 1, 1, 2)

        self.label_6 = QLabel(AmplitudeDetectorSettingsView)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.baseline_win_len_lineedit = QLineEdit(AmplitudeDetectorSettingsView)
        self.baseline_win_len_lineedit.setObjectName(u"baseline_win_len_lineedit")

        self.gridLayout.addWidget(self.baseline_win_len_lineedit, 3, 1, 1, 2)

        self.label_7 = QLabel(AmplitudeDetectorSettingsView)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.tresholdval_lineedit = QLineEdit(AmplitudeDetectorSettingsView)
        self.tresholdval_lineedit.setObjectName(u"tresholdval_lineedit")

        self.gridLayout.addWidget(self.tresholdval_lineedit, 4, 1, 1, 1)

        self.threshUnit_comboBox = QComboBox(AmplitudeDetectorSettingsView)
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.setObjectName(u"threshUnit_comboBox")

        self.gridLayout.addWidget(self.threshUnit_comboBox, 4, 2, 1, 1)

        self.label_8 = QLabel(AmplitudeDetectorSettingsView)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)

        self.threshBeha_comboBox = QComboBox(AmplitudeDetectorSettingsView)
        self.threshBeha_comboBox.addItem("")
        self.threshBeha_comboBox.addItem("")
        self.threshBeha_comboBox.setObjectName(u"threshBeha_comboBox")

        self.gridLayout.addWidget(self.threshBeha_comboBox, 5, 1, 1, 2)

        self.label_9 = QLabel(AmplitudeDetectorSettingsView)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)

        self.chan_det_info_lineedit = QLineEdit(AmplitudeDetectorSettingsView)
        self.chan_det_info_lineedit.setObjectName(u"chan_det_info_lineedit")

        self.gridLayout.addWidget(self.chan_det_info_lineedit, 6, 1, 1, 2)

        self.label_3 = QLabel(AmplitudeDetectorSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.group_lineedit = QLineEdit(AmplitudeDetectorSettingsView)
        self.group_lineedit.setObjectName(u"group_lineedit")

        self.gridLayout.addWidget(self.group_lineedit, 0, 1, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(AmplitudeDetectorSettingsView)

        QMetaObject.connectSlotsByName(AmplitudeDetectorSettingsView)
    # setupUi

    def retranslateUi(self, AmplitudeDetectorSettingsView):
        AmplitudeDetectorSettingsView.setWindowTitle(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Form", None))
#if QT_CONFIG(tooltip)
        AmplitudeDetectorSettingsView.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Amplitude Detector settings", None))
        self.label.setText(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Event name", None))
        self.label_2.setText(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Pad length (s)", None))
#if QT_CONFIG(tooltip)
        self.pad_length_lineedit.setToolTip(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Padding event added to both the beginning and  the end of the originally detected event.", None))
#endif // QT_CONFIG(tooltip)
        self.pad_length_lineedit.setText("")
        self.label_6.setText(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Baseline window length (s)", None))
#if QT_CONFIG(tooltip)
        self.baseline_win_len_lineedit.setToolTip(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Optional", None))
#endif // QT_CONFIG(tooltip)
        self.baseline_win_len_lineedit.setText("")
        self.label_7.setText(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Threshold value", None))
        self.tresholdval_lineedit.setText("")
        self.threshUnit_comboBox.setItemText(0, QCoreApplication.translate("AmplitudeDetectorSettingsView", u"fixed", None))
        self.threshUnit_comboBox.setItemText(1, QCoreApplication.translate("AmplitudeDetectorSettingsView", u"x BSL median", None))
        self.threshUnit_comboBox.setItemText(2, QCoreApplication.translate("AmplitudeDetectorSettingsView", u"x BSL STD", None))
        self.threshUnit_comboBox.setItemText(3, QCoreApplication.translate("AmplitudeDetectorSettingsView", u"x BSL STD (log10)", None))

#if QT_CONFIG(tooltip)
        self.threshUnit_comboBox.setToolTip(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Select threshold unit : \n"
"-fixed (as \u00b5V\u00b2),\n"
"-x times the baseline median or\n"
"-x times the baseline standard deviation or\n"
"-x times the baseline standard deviation on data log10 transformed.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Select behavior: artefact when above/below the threshold.", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Threshold behavior", None))
        self.threshBeha_comboBox.setItemText(0, QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Above", None))
        self.threshBeha_comboBox.setItemText(1, QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Below", None))

#if QT_CONFIG(tooltip)
        self.threshBeha_comboBox.setToolTip(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Select behavior: artefact when above/below the threshold.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Select behavior: artefact when above/below the threshold.", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Channel to exit detection info", None))
#if QT_CONFIG(tooltip)
        self.chan_det_info_lineedit.setToolTip(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Channel label to see detection info (debug purpose only)", None))
#endif // QT_CONFIG(tooltip)
        self.chan_det_info_lineedit.setText("")
        self.label_3.setText(QCoreApplication.translate("AmplitudeDetectorSettingsView", u"Event group", None))
    # retranslateUi


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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_SpectralDetectorSettingsView(object):
    def setupUi(self, SpectralDetectorSettingsView):
        if not SpectralDetectorSettingsView.objectName():
            SpectralDetectorSettingsView.setObjectName(u"SpectralDetectorSettingsView")
        SpectralDetectorSettingsView.resize(562, 293)
        self.gridLayout_2 = QGridLayout(SpectralDetectorSettingsView)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(SpectralDetectorSettingsView)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.event_name_lineedit = QLineEdit(SpectralDetectorSettingsView)
        self.event_name_lineedit.setObjectName(u"event_name_lineedit")

        self.gridLayout.addWidget(self.event_name_lineedit, 1, 1, 1, 2)

        self.baseline_win_len_lineedit = QLineEdit(SpectralDetectorSettingsView)
        self.baseline_win_len_lineedit.setObjectName(u"baseline_win_len_lineedit")

        self.gridLayout.addWidget(self.baseline_win_len_lineedit, 6, 1, 1, 2)

        self.label_2 = QLabel(SpectralDetectorSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.tresholdval_lineedit = QLineEdit(SpectralDetectorSettingsView)
        self.tresholdval_lineedit.setObjectName(u"tresholdval_lineedit")

        self.gridLayout.addWidget(self.tresholdval_lineedit, 7, 1, 1, 1)

        self.rel_checkBox = QCheckBox(SpectralDetectorSettingsView)
        self.rel_checkBox.setObjectName(u"rel_checkBox")

        self.gridLayout.addWidget(self.rel_checkBox, 2, 2, 1, 1)

        self.label_9 = QLabel(SpectralDetectorSettingsView)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)

        self.label = QLabel(SpectralDetectorSettingsView)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.threshUnit_comboBox = QComboBox(SpectralDetectorSettingsView)
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.addItem("")
        self.threshUnit_comboBox.setObjectName(u"threshUnit_comboBox")

        self.gridLayout.addWidget(self.threshUnit_comboBox, 7, 2, 1, 1)

        self.label_3 = QLabel(SpectralDetectorSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.threshBeha_comboBox = QComboBox(SpectralDetectorSettingsView)
        self.threshBeha_comboBox.addItem("")
        self.threshBeha_comboBox.addItem("")
        self.threshBeha_comboBox.setObjectName(u"threshBeha_comboBox")

        self.gridLayout.addWidget(self.threshBeha_comboBox, 8, 1, 1, 2)

        self.label_6 = QLabel(SpectralDetectorSettingsView)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.bsl_high_freq_lineedit = QLineEdit(SpectralDetectorSettingsView)
        self.bsl_high_freq_lineedit.setObjectName(u"bsl_high_freq_lineedit")
        self.bsl_high_freq_lineedit.setEnabled(False)

        self.gridLayout.addWidget(self.bsl_high_freq_lineedit, 4, 2, 1, 1)

        self.bsl_low_freq_lineedit = QLineEdit(SpectralDetectorSettingsView)
        self.bsl_low_freq_lineedit.setObjectName(u"bsl_low_freq_lineedit")
        self.bsl_low_freq_lineedit.setEnabled(False)

        self.gridLayout.addWidget(self.bsl_low_freq_lineedit, 3, 2, 1, 1)

        self.label_10 = QLabel(SpectralDetectorSettingsView)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 1, 1, 1)

        self.high_frequency_lineedit = QLineEdit(SpectralDetectorSettingsView)
        self.high_frequency_lineedit.setObjectName(u"high_frequency_lineedit")

        self.gridLayout.addWidget(self.high_frequency_lineedit, 4, 1, 1, 1)

        self.label_7 = QLabel(SpectralDetectorSettingsView)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)

        self.low_frequency_lineedit = QLineEdit(SpectralDetectorSettingsView)
        self.low_frequency_lineedit.setObjectName(u"low_frequency_lineedit")

        self.gridLayout.addWidget(self.low_frequency_lineedit, 3, 1, 1, 1)

        self.chan_det_info_lineedit = QLineEdit(SpectralDetectorSettingsView)
        self.chan_det_info_lineedit.setObjectName(u"chan_det_info_lineedit")

        self.gridLayout.addWidget(self.chan_det_info_lineedit, 9, 1, 1, 2)

        self.label_8 = QLabel(SpectralDetectorSettingsView)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)

        self.label_4 = QLabel(SpectralDetectorSettingsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.group_lineedit = QLineEdit(SpectralDetectorSettingsView)
        self.group_lineedit.setObjectName(u"group_lineedit")

        self.gridLayout.addWidget(self.group_lineedit, 0, 1, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(SpectralDetectorSettingsView)
        self.rel_checkBox.stateChanged.connect(SpectralDetectorSettingsView.on_input_format_changed)

        QMetaObject.connectSlotsByName(SpectralDetectorSettingsView)
    # setupUi

    def retranslateUi(self, SpectralDetectorSettingsView):
        SpectralDetectorSettingsView.setWindowTitle(QCoreApplication.translate("SpectralDetectorSettingsView", u"Form", None))
#if QT_CONFIG(tooltip)
        SpectralDetectorSettingsView.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("SpectralDetectorSettingsView", u"Spectral Detector settings", None))
#if QT_CONFIG(tooltip)
        self.baseline_win_len_lineedit.setToolTip(QCoreApplication.translate("SpectralDetectorSettingsView", u"Optional", None))
#endif // QT_CONFIG(tooltip)
        self.baseline_win_len_lineedit.setText("")
        self.label_2.setText(QCoreApplication.translate("SpectralDetectorSettingsView", u"Low frequency", None))
        self.tresholdval_lineedit.setText("")
        self.rel_checkBox.setText(QCoreApplication.translate("SpectralDetectorSettingsView", u"Relative power", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("SpectralDetectorSettingsView", u"Select behavior: artefact when above/below the threshold.", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("SpectralDetectorSettingsView", u"Channel to display detection info", None))
        self.label.setText(QCoreApplication.translate("SpectralDetectorSettingsView", u"Event name", None))
        self.threshUnit_comboBox.setItemText(0, QCoreApplication.translate("SpectralDetectorSettingsView", u"fixed", None))
        self.threshUnit_comboBox.setItemText(1, QCoreApplication.translate("SpectralDetectorSettingsView", u"x BSL median", None))
        self.threshUnit_comboBox.setItemText(2, QCoreApplication.translate("SpectralDetectorSettingsView", u"x BSL STD", None))
        self.threshUnit_comboBox.setItemText(3, QCoreApplication.translate("SpectralDetectorSettingsView", u"x BSL STD (log10)", None))
        self.threshUnit_comboBox.setItemText(4, QCoreApplication.translate("SpectralDetectorSettingsView", u"x epochs STD", None))
        self.threshUnit_comboBox.setItemText(5, QCoreApplication.translate("SpectralDetectorSettingsView", u"x epochs STD (log10)", None))

#if QT_CONFIG(tooltip)
        self.threshUnit_comboBox.setToolTip(QCoreApplication.translate("SpectralDetectorSettingsView", u"Select threshold unit : fixed (as \u00b5V\u00b2), x times the baseline median or x times the baseline standard deviation.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("SpectralDetectorSettingsView", u"High frequency", None))
        self.threshBeha_comboBox.setItemText(0, QCoreApplication.translate("SpectralDetectorSettingsView", u"Above", None))
        self.threshBeha_comboBox.setItemText(1, QCoreApplication.translate("SpectralDetectorSettingsView", u"Below", None))

#if QT_CONFIG(tooltip)
        self.threshBeha_comboBox.setToolTip(QCoreApplication.translate("SpectralDetectorSettingsView", u"Select behavior: artefact when above/below the threshold.", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("SpectralDetectorSettingsView", u"Baseline window length (s)", None))
#if QT_CONFIG(tooltip)
        self.bsl_high_freq_lineedit.setToolTip(QCoreApplication.translate("SpectralDetectorSettingsView", u"Enter the high frequency (Hz) of the background band.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.bsl_low_freq_lineedit.setToolTip(QCoreApplication.translate("SpectralDetectorSettingsView", u"Enter the low frequency (Hz) of the background band.", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("SpectralDetectorSettingsView", u"Absolute/num band", None))
#if QT_CONFIG(tooltip)
        self.high_frequency_lineedit.setToolTip(QCoreApplication.translate("SpectralDetectorSettingsView", u"Enter the high frequency (Hz) of the band of interest.", None))
#endif // QT_CONFIG(tooltip)
        self.high_frequency_lineedit.setText("")
        self.label_7.setText(QCoreApplication.translate("SpectralDetectorSettingsView", u"Threshold value", None))
#if QT_CONFIG(tooltip)
        self.low_frequency_lineedit.setToolTip(QCoreApplication.translate("SpectralDetectorSettingsView", u"Enter the low frequency (Hz) of the band of interest.", None))
#endif // QT_CONFIG(tooltip)
        self.low_frequency_lineedit.setText("")
#if QT_CONFIG(tooltip)
        self.chan_det_info_lineedit.setToolTip(QCoreApplication.translate("SpectralDetectorSettingsView", u"Channel label to see detection info (debug purpose only)", None))
#endif // QT_CONFIG(tooltip)
        self.chan_det_info_lineedit.setText("")
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("SpectralDetectorSettingsView", u"Select behavior: artefact when above/below the threshold.", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("SpectralDetectorSettingsView", u"Threshold behavior", None))
        self.label_4.setText(QCoreApplication.translate("SpectralDetectorSettingsView", u"Event group", None))
    # retranslateUi


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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_SleepStageEventsSettingsView(object):
    def setupUi(self, SleepStageEventsSettingsView):
        if not SleepStageEventsSettingsView.objectName():
            SleepStageEventsSettingsView.setObjectName(u"SleepStageEventsSettingsView")
        SleepStageEventsSettingsView.resize(445, 628)
        self.horizontalLayout_2 = QHBoxLayout(SleepStageEventsSettingsView)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_8 = QLabel(SleepStageEventsSettingsView)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(SleepStageEventsSettingsView)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 20))
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_9)

        self.stages_lineEdit = QLineEdit(SleepStageEventsSettingsView)
        self.stages_lineEdit.setObjectName(u"stages_lineEdit")
        self.stages_lineEdit.setEnabled(False)

        self.verticalLayout.addWidget(self.stages_lineEdit)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.wake_checkBox = QCheckBox(SleepStageEventsSettingsView)
        self.wake_checkBox.setObjectName(u"wake_checkBox")
        self.wake_checkBox.setChecked(False)

        self.gridLayout_2.addWidget(self.wake_checkBox, 0, 0, 1, 1)

        self.nrem_checkBox = QCheckBox(SleepStageEventsSettingsView)
        self.nrem_checkBox.setObjectName(u"nrem_checkBox")

        self.gridLayout_2.addWidget(self.nrem_checkBox, 0, 1, 1, 1)

        self.stage1_checkBox = QCheckBox(SleepStageEventsSettingsView)
        self.stage1_checkBox.setObjectName(u"stage1_checkBox")

        self.gridLayout_2.addWidget(self.stage1_checkBox, 1, 0, 1, 1)

        self.nwake_checkBox = QCheckBox(SleepStageEventsSettingsView)
        self.nwake_checkBox.setObjectName(u"nwake_checkBox")

        self.gridLayout_2.addWidget(self.nwake_checkBox, 1, 1, 1, 1)

        self.stage2_checkBox = QCheckBox(SleepStageEventsSettingsView)
        self.stage2_checkBox.setObjectName(u"stage2_checkBox")

        self.gridLayout_2.addWidget(self.stage2_checkBox, 2, 0, 1, 1)

        self.stage3_checkBox = QCheckBox(SleepStageEventsSettingsView)
        self.stage3_checkBox.setObjectName(u"stage3_checkBox")

        self.gridLayout_2.addWidget(self.stage3_checkBox, 3, 0, 1, 1)

        self.stage4_checkBox = QCheckBox(SleepStageEventsSettingsView)
        self.stage4_checkBox.setObjectName(u"stage4_checkBox")

        self.gridLayout_2.addWidget(self.stage4_checkBox, 4, 0, 1, 1)

        self.rem_checkBox = QCheckBox(SleepStageEventsSettingsView)
        self.rem_checkBox.setObjectName(u"rem_checkBox")

        self.gridLayout_2.addWidget(self.rem_checkBox, 5, 0, 1, 1)

        self.movementtime_checkBox = QCheckBox(SleepStageEventsSettingsView)
        self.movementtime_checkBox.setObjectName(u"movementtime_checkBox")

        self.gridLayout_2.addWidget(self.movementtime_checkBox, 6, 0, 1, 1)

        self.technicaltime_checkBox = QCheckBox(SleepStageEventsSettingsView)
        self.technicaltime_checkBox.setObjectName(u"technicaltime_checkBox")

        self.gridLayout_2.addWidget(self.technicaltime_checkBox, 7, 0, 1, 1)

        self.undetermined_checkBox = QCheckBox(SleepStageEventsSettingsView)
        self.undetermined_checkBox.setObjectName(u"undetermined_checkBox")

        self.gridLayout_2.addWidget(self.undetermined_checkBox, 8, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.merge_events_checkBox = QCheckBox(SleepStageEventsSettingsView)
        self.merge_events_checkBox.setObjectName(u"merge_events_checkBox")
        self.merge_events_checkBox.setMinimumSize(QSize(200, 0))

        self.verticalLayout.addWidget(self.merge_events_checkBox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_33 = QLabel(SleepStageEventsSettingsView)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)

        self.verticalLayout.addWidget(self.label_33)

        self.newname_lineEdit = QLineEdit(SleepStageEventsSettingsView)
        self.newname_lineEdit.setObjectName(u"newname_lineEdit")

        self.verticalLayout.addWidget(self.newname_lineEdit)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_34 = QLabel(SleepStageEventsSettingsView)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font)

        self.verticalLayout.addWidget(self.label_34)

        self.evt_in_cycle_checkBox = QCheckBox(SleepStageEventsSettingsView)
        self.evt_in_cycle_checkBox.setObjectName(u"evt_in_cycle_checkBox")

        self.verticalLayout.addWidget(self.evt_in_cycle_checkBox)

        self.excl_nremp_checkBox = QCheckBox(SleepStageEventsSettingsView)
        self.excl_nremp_checkBox.setObjectName(u"excl_nremp_checkBox")

        self.verticalLayout.addWidget(self.excl_nremp_checkBox)

        self.excl_remp_checkBox_2 = QCheckBox(SleepStageEventsSettingsView)
        self.excl_remp_checkBox_2.setObjectName(u"excl_remp_checkBox_2")

        self.verticalLayout.addWidget(self.excl_remp_checkBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_32 = QLabel(SleepStageEventsSettingsView)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(16777215, 20))
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_32)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_15 = QLabel(SleepStageEventsSettingsView)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)

        self.label_11 = QLabel(SleepStageEventsSettingsView)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 7, 1, 1, 1)

        self.label_6 = QLabel(SleepStageEventsSettingsView)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_28 = QLabel(SleepStageEventsSettingsView)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_28, 1, 2, 1, 1)

        self.label_31 = QLabel(SleepStageEventsSettingsView)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_31, 7, 2, 1, 1)

        self.label_23 = QLabel(SleepStageEventsSettingsView)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_23, 8, 2, 1, 1)

        self.label_29 = QLabel(SleepStageEventsSettingsView)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_29, 0, 2, 1, 1)

        self.label_21 = QLabel(SleepStageEventsSettingsView)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_21, 7, 0, 1, 1)

        self.label_10 = QLabel(SleepStageEventsSettingsView)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 5, 1, 1, 1)

        self.label_25 = QLabel(SleepStageEventsSettingsView)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_25, 6, 2, 1, 1)

        self.label_26 = QLabel(SleepStageEventsSettingsView)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_26, 9, 2, 1, 1)

        self.label_13 = QLabel(SleepStageEventsSettingsView)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 1)

        self.label_3 = QLabel(SleepStageEventsSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)

        self.label_4 = QLabel(SleepStageEventsSettingsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 6, 1, 1, 1)

        self.label_20 = QLabel(SleepStageEventsSettingsView)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_20, 3, 0, 1, 1)

        self.label_22 = QLabel(SleepStageEventsSettingsView)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_22, 4, 2, 1, 1)

        self.label_17 = QLabel(SleepStageEventsSettingsView)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_17, 9, 0, 1, 1)

        self.label_12 = QLabel(SleepStageEventsSettingsView)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_5 = QLabel(SleepStageEventsSettingsView)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 9, 1, 1, 1)

        self.label_2 = QLabel(SleepStageEventsSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.label_18 = QLabel(SleepStageEventsSettingsView)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_18, 5, 0, 1, 1)

        self.label_30 = QLabel(SleepStageEventsSettingsView)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_30, 3, 2, 1, 1)

        self.label_19 = QLabel(SleepStageEventsSettingsView)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_27 = QLabel(SleepStageEventsSettingsView)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_27, 5, 2, 1, 1)

        self.label_14 = QLabel(SleepStageEventsSettingsView)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_14, 8, 0, 1, 1)

        self.label_7 = QLabel(SleepStageEventsSettingsView)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 8, 1, 1, 1)

        self.label_24 = QLabel(SleepStageEventsSettingsView)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_24, 2, 2, 1, 1)

        self.label = QLabel(SleepStageEventsSettingsView)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.label_16 = QLabel(SleepStageEventsSettingsView)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_16, 6, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(18, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.retranslateUi(SleepStageEventsSettingsView)
        self.wake_checkBox.stateChanged.connect(SleepStageEventsSettingsView.on_event_stages_changed)
        self.undetermined_checkBox.stateChanged.connect(SleepStageEventsSettingsView.on_event_stages_changed)
        self.technicaltime_checkBox.stateChanged.connect(SleepStageEventsSettingsView.on_event_stages_changed)
        self.movementtime_checkBox.stateChanged.connect(SleepStageEventsSettingsView.on_event_stages_changed)
        self.rem_checkBox.stateChanged.connect(SleepStageEventsSettingsView.on_event_stages_changed)
        self.stage4_checkBox.stateChanged.connect(SleepStageEventsSettingsView.on_event_stages_changed)
        self.stage3_checkBox.stateChanged.connect(SleepStageEventsSettingsView.on_event_stages_changed)
        self.stage2_checkBox.stateChanged.connect(SleepStageEventsSettingsView.on_event_stages_changed)
        self.stage1_checkBox.stateChanged.connect(SleepStageEventsSettingsView.on_event_stages_changed)
        self.nwake_checkBox.stateChanged.connect(SleepStageEventsSettingsView.on_event_nwake_changed)
        self.nrem_checkBox.stateChanged.connect(SleepStageEventsSettingsView.on_event_nrem_changed)

        QMetaObject.connectSlotsByName(SleepStageEventsSettingsView)
    # setupUi

    def retranslateUi(self, SleepStageEventsSettingsView):
        SleepStageEventsSettingsView.setWindowTitle(QCoreApplication.translate("SleepStageEventsSettingsView", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Sleep Stage Events Settings", None))
        self.label_9.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Stages to select", None))
        self.wake_checkBox.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Wake", None))
        self.nrem_checkBox.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"NREM", None))
        self.stage1_checkBox.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Stage 1", None))
        self.nwake_checkBox.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"NWAKE", None))
        self.stage2_checkBox.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Stage 2", None))
        self.stage3_checkBox.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Stage 3", None))
        self.stage4_checkBox.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Stage 4", None))
        self.rem_checkBox.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"REM", None))
        self.movementtime_checkBox.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Movement time", None))
        self.technicaltime_checkBox.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Technical time", None))
        self.undetermined_checkBox.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Undetermined", None))
#if QT_CONFIG(tooltip)
        self.merge_events_checkBox.setToolTip(QCoreApplication.translate("SleepStageEventsSettingsView", u"Check to merge selected continuous events (i.e. two selected 30 second stage 2 events will be merged into one continuous minute of stage 2 event)", None))
#endif // QT_CONFIG(tooltip)
        self.merge_events_checkBox.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"To merge selected continuous events", None))
        self.label_33.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"To rename selected events", None))
#if QT_CONFIG(tooltip)
        self.newname_lineEdit.setToolTip(QCoreApplication.translate("SleepStageEventsSettingsView", u"Optional. Let blank to keep the original event name.", None))
#endif // QT_CONFIG(tooltip)
        self.label_34.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Sleep Cycles", None))
#if QT_CONFIG(tooltip)
        self.evt_in_cycle_checkBox.setToolTip(QCoreApplication.translate("SleepStageEventsSettingsView", u"Check to keep only events included in the sleep cycles.", None))
#endif // QT_CONFIG(tooltip)
        self.evt_in_cycle_checkBox.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Only events included in the cycles", None))
        self.excl_nremp_checkBox.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Exclude NREM period", None))
        self.excl_remp_checkBox_2.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Exclude REM period", None))
        self.label_32.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Reference table", None))
        self.label_15.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Stage 1", None))
        self.label_11.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"6", None))
        self.label_6.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"0", None))
        self.label_28.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"W", None))
        self.label_31.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"6", None))
        self.label_23.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"-", None))
        self.label_29.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"AASM", None))
        self.label_21.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Movement time", None))
        self.label_10.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"4", None))
        self.label_25.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"R", None))
        self.label_26.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"-", None))
        self.label_13.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Stage 3", None))
        self.label_3.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"3", None))
        self.label_4.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"5", None))
        self.label_20.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Stage 2", None))
        self.label_22.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"N3", None))
        self.label_17.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Undetermined", None))
        self.label_12.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"R&K", None))
        self.label_5.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"9", None))
        self.label_2.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"2", None))
        self.label_18.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Stage 4", None))
        self.label_30.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"N2", None))
        self.label_19.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Wake", None))
        self.label_27.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"-", None))
        self.label_14.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"Technical time", None))
        self.label_7.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"7", None))
        self.label_24.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"N1", None))
        self.label.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"1", None))
        self.label_16.setText(QCoreApplication.translate("SleepStageEventsSettingsView", u"REM", None))
    # retranslateUi


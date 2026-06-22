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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from widgets.QComboBoxLive import QComboBoxLive

class Ui_EventCombineSettingsView(object):
    def setupUi(self, EventCombineSettingsView):
        if not EventCombineSettingsView.objectName():
            EventCombineSettingsView.setObjectName(u"EventCombineSettingsView")
        EventCombineSettingsView.resize(432, 430)
        self.gridLayout_3 = QGridLayout(EventCombineSettingsView)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(EventCombineSettingsView)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_2 = QFrame(EventCombineSettingsView)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.chan_wise_checkBox = QCheckBox(EventCombineSettingsView)
        self.chan_wise_checkBox.setObjectName(u"chan_wise_checkBox")
        self.chan_wise_checkBox.setChecked(True)

        self.verticalLayout.addWidget(self.chan_wise_checkBox)

        self.label_9 = QLabel(EventCombineSettingsView)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout.addWidget(self.label_9)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(EventCombineSettingsView)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.event1_name_lineedit = QLineEdit(EventCombineSettingsView)
        self.event1_name_lineedit.setObjectName(u"event1_name_lineedit")

        self.gridLayout.addWidget(self.event1_name_lineedit, 0, 1, 1, 1)

        self.label_2 = QLabel(EventCombineSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.event2_name_lineedit = QLineEdit(EventCombineSettingsView)
        self.event2_name_lineedit.setObjectName(u"event2_name_lineedit")

        self.gridLayout.addWidget(self.event2_name_lineedit, 1, 1, 1, 1)

        self.chan1_label = QLabel(EventCombineSettingsView)
        self.chan1_label.setObjectName(u"chan1_label")
        self.chan1_label.setLayoutDirection(Qt.LeftToRight)
        self.chan1_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.chan1_label, 2, 0, 1, 1)

        self.channel1_lineedit = QLineEdit(EventCombineSettingsView)
        self.channel1_lineedit.setObjectName(u"channel1_lineedit")

        self.gridLayout.addWidget(self.channel1_lineedit, 2, 1, 1, 1)

        self.chan2_label = QLabel(EventCombineSettingsView)
        self.chan2_label.setObjectName(u"chan2_label")
        self.chan2_label.setLayoutDirection(Qt.LeftToRight)
        self.chan2_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.chan2_label, 3, 0, 1, 1)

        self.channel2_lineedit = QLineEdit(EventCombineSettingsView)
        self.channel2_lineedit.setObjectName(u"channel2_lineedit")

        self.gridLayout.addWidget(self.channel2_lineedit, 3, 1, 1, 1)

        self.label_3 = QLabel(EventCombineSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.behavior_comboBox = QComboBoxLive(EventCombineSettingsView)
        self.behavior_comboBox.addItem("")
        self.behavior_comboBox.addItem("")
        self.behavior_comboBox.addItem("")
        self.behavior_comboBox.setObjectName(u"behavior_comboBox")

        self.gridLayout.addWidget(self.behavior_comboBox, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.line = QFrame(EventCombineSettingsView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(EventCombineSettingsView)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout.addWidget(self.label_8)

        self.rename_checkBox = QCheckBox(EventCombineSettingsView)
        self.rename_checkBox.setObjectName(u"rename_checkBox")
        self.rename_checkBox.setFont(font)

        self.horizontalLayout.addWidget(self.rename_checkBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(EventCombineSettingsView)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.new_event_group_lineedit = QLineEdit(EventCombineSettingsView)
        self.new_event_group_lineedit.setObjectName(u"new_event_group_lineedit")
        self.new_event_group_lineedit.setEnabled(False)

        self.gridLayout_2.addWidget(self.new_event_group_lineedit, 0, 1, 1, 1)

        self.label_4 = QLabel(EventCombineSettingsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.new_event_name_lineedit = QLineEdit(EventCombineSettingsView)
        self.new_event_name_lineedit.setObjectName(u"new_event_name_lineedit")
        self.new_event_name_lineedit.setEnabled(False)

        self.gridLayout_2.addWidget(self.new_event_name_lineedit, 1, 1, 1, 1)

        self.label_6 = QLabel(EventCombineSettingsView)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.event_channel_lineedit = QLineEdit(EventCombineSettingsView)
        self.event_channel_lineedit.setObjectName(u"event_channel_lineedit")
        self.event_channel_lineedit.setEnabled(False)

        self.gridLayout_2.addWidget(self.event_channel_lineedit, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(EventCombineSettingsView)
        self.rename_checkBox.stateChanged.connect(EventCombineSettingsView.on_modify_checkbox)
        self.chan_wise_checkBox.stateChanged.connect(EventCombineSettingsView.on_chan_wise_checkbox)

        QMetaObject.connectSlotsByName(EventCombineSettingsView)
    # setupUi

    def retranslateUi(self, EventCombineSettingsView):
        EventCombineSettingsView.setWindowTitle(QCoreApplication.translate("EventCombineSettingsView", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("EventCombineSettingsView", u"Event Combine settings ", None))
#if QT_CONFIG(tooltip)
        self.chan_wise_checkBox.setToolTip(QCoreApplication.translate("EventCombineSettingsView", u"Check to work with channel specific events only (if checked sleep stages are discarded).  Events are combined per channel.", None))
#endif // QT_CONFIG(tooltip)
        self.chan_wise_checkBox.setText(QCoreApplication.translate("EventCombineSettingsView", u"Channel Wise", None))
        self.label_9.setText(QCoreApplication.translate("EventCombineSettingsView", u"Select the events to combine", None))
        self.label.setText(QCoreApplication.translate("EventCombineSettingsView", u"Event 1 name", None))
#if QT_CONFIG(tooltip)
        self.event1_name_lineedit.setToolTip(QCoreApplication.translate("EventCombineSettingsView", u"To filter events with a specific name otherwise all events will be combined.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("EventCombineSettingsView", u"Event 2 name", None))
#if QT_CONFIG(tooltip)
        self.event2_name_lineedit.setToolTip(QCoreApplication.translate("EventCombineSettingsView", u"To filter events with a specific name otherwise all events will be combined.", None))
#endif // QT_CONFIG(tooltip)
        self.chan1_label.setText(QCoreApplication.translate("EventCombineSettingsView", u"Channel1 label", None))
#if QT_CONFIG(tooltip)
        self.channel1_lineedit.setToolTip(QCoreApplication.translate("EventCombineSettingsView", u"To filter events based on a channel label, otherwise all events are combined per channel.", None))
#endif // QT_CONFIG(tooltip)
        self.chan2_label.setText(QCoreApplication.translate("EventCombineSettingsView", u"Channel2 label", None))
#if QT_CONFIG(tooltip)
        self.channel2_lineedit.setToolTip(QCoreApplication.translate("EventCombineSettingsView", u"To filter events based on a channel label, otherwise all events are combined per channel.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("EventCombineSettingsView", u"Behavior", None))
        self.behavior_comboBox.setItemText(0, QCoreApplication.translate("EventCombineSettingsView", u"union", None))
        self.behavior_comboBox.setItemText(1, QCoreApplication.translate("EventCombineSettingsView", u"union without concurrent events", None))
        self.behavior_comboBox.setItemText(2, QCoreApplication.translate("EventCombineSettingsView", u"intersection", None))

#if QT_CONFIG(tooltip)
        self.behavior_comboBox.setToolTip(QCoreApplication.translate("EventCombineSettingsView", u"Select how to combine events : union (all events), union without concurrent events (events merge) or intersection (concurrent events only).", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("EventCombineSettingsView", u"Modify the combined events", None))
#if QT_CONFIG(tooltip)
        self.rename_checkBox.setToolTip(QCoreApplication.translate("EventCombineSettingsView", u"Check to rename the combined events.", None))
#endif // QT_CONFIG(tooltip)
        self.rename_checkBox.setText("")
        self.label_7.setText(QCoreApplication.translate("EventCombineSettingsView", u"New event group", None))
#if QT_CONFIG(tooltip)
        self.new_event_group_lineedit.setToolTip(QCoreApplication.translate("EventCombineSettingsView", u"Event group is mandatory to rename combined events.  Can be left blank if the \"New event name\" is also left blank.", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("EventCombineSettingsView", u"New event name", None))
#if QT_CONFIG(tooltip)
        self.new_event_name_lineedit.setToolTip(QCoreApplication.translate("EventCombineSettingsView", u"To rename the combined events. The name of the source is taken if it is left blank.", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("EventCombineSettingsView", u"New event channel", None))
#if QT_CONFIG(tooltip)
        self.event_channel_lineedit.setToolTip(QCoreApplication.translate("EventCombineSettingsView", u"On which channel new created events are added.  If blank, the channel from events 1 is taken.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi


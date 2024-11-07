# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EventReaderSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EventReaderSettingsView(object):
    def setupUi(self, EventReaderSettingsView):
        if not EventReaderSettingsView.objectName():
            EventReaderSettingsView.setObjectName(u"EventReaderSettingsView")
        EventReaderSettingsView.resize(778, 697)
        EventReaderSettingsView.setInputMethodHints(Qt.ImhNone)
        self.horizontalLayout_3 = QHBoxLayout(EventReaderSettingsView)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.label_10 = QLabel(EventReaderSettingsView)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)

        self.verticalLayout_3.addWidget(self.label_10)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(EventReaderSettingsView)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.filename_lineedit = QLineEdit(EventReaderSettingsView)
        self.filename_lineedit.setObjectName(u"filename_lineedit")
        self.filename_lineedit.setMaximumSize(QSize(16777215, 16777215))
        self.filename_lineedit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.filename_lineedit, 1, 1, 1, 1)

        self.choose_pushbutton = QPushButton(EventReaderSettingsView)
        self.choose_pushbutton.setObjectName(u"choose_pushbutton")
        self.choose_pushbutton.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.choose_pushbutton, 1, 2, 1, 1)

        self.label_12 = QLabel(EventReaderSettingsView)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radioButton_personalized = QRadioButton(EventReaderSettingsView)
        self.buttonGroup = QButtonGroup(EventReaderSettingsView)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_personalized)
        self.radioButton_personalized.setObjectName(u"radioButton_personalized")

        self.gridLayout_3.addWidget(self.radioButton_personalized, 0, 0, 1, 2)

        self.radioButton_snooz = QRadioButton(EventReaderSettingsView)
        self.buttonGroup.addButton(self.radioButton_snooz)
        self.radioButton_snooz.setObjectName(u"radioButton_snooz")
        self.radioButton_snooz.setChecked(True)

        self.gridLayout_3.addWidget(self.radioButton_snooz, 1, 0, 1, 2)

        self.label_11 = QLabel(EventReaderSettingsView)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)

        self.delimiter_lineedit = QLineEdit(EventReaderSettingsView)
        self.delimiter_lineedit.setObjectName(u"delimiter_lineedit")
        self.delimiter_lineedit.setInputMethodHints(Qt.ImhDialableCharactersOnly)
        self.delimiter_lineedit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.delimiter_lineedit, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_13 = QLabel(EventReaderSettingsView)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.verticalLayout_2.addWidget(self.label_13)

        self.label_5 = QLabel(EventReaderSettingsView)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(20, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.time_radiobutton = QRadioButton(EventReaderSettingsView)
        self.buttonGroup_2 = QButtonGroup(EventReaderSettingsView)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.time_radiobutton)
        self.time_radiobutton.setObjectName(u"time_radiobutton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_radiobutton.sizePolicy().hasHeightForWidth())
        self.time_radiobutton.setSizePolicy(sizePolicy)
        self.time_radiobutton.setChecked(True)

        self.gridLayout_2.addWidget(self.time_radiobutton, 0, 0, 1, 1)

        self.sample_radiobutton = QRadioButton(EventReaderSettingsView)
        self.buttonGroup_2.addButton(self.sample_radiobutton)
        self.sample_radiobutton.setObjectName(u"sample_radiobutton")
        sizePolicy.setHeightForWidth(self.sample_radiobutton.sizePolicy().hasHeightForWidth())
        self.sample_radiobutton.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.sample_radiobutton, 0, 1, 1, 1)

        self.label_6 = QLabel(EventReaderSettingsView)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.sample_rate_lineedit = QLineEdit(EventReaderSettingsView)
        self.sample_rate_lineedit.setObjectName(u"sample_rate_lineedit")
        self.sample_rate_lineedit.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sample_rate_lineedit.sizePolicy().hasHeightForWidth())
        self.sample_rate_lineedit.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.sample_rate_lineedit, 1, 1, 1, 1)

        self.comboBox_time_format = QComboBox(EventReaderSettingsView)
        self.comboBox_time_format.addItem("")
        self.comboBox_time_format.addItem("")
        self.comboBox_time_format.addItem("")
        self.comboBox_time_format.setObjectName(u"comboBox_time_format")

        self.gridLayout_2.addWidget(self.comboBox_time_format, 2, 0, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label_7 = QLabel(EventReaderSettingsView)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_9 = QLabel(EventReaderSettingsView)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(80, 0))
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self.checkBox_group_enabled = QCheckBox(EventReaderSettingsView)
        self.checkBox_group_enabled.setObjectName(u"checkBox_group_enabled")
        self.checkBox_group_enabled.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_group_enabled, 0, 1, 1, 1)

        self.group_spinbox = QSpinBox(EventReaderSettingsView)
        self.group_spinbox.setObjectName(u"group_spinbox")
        sizePolicy1.setHeightForWidth(self.group_spinbox.sizePolicy().hasHeightForWidth())
        self.group_spinbox.setSizePolicy(sizePolicy1)
        self.group_spinbox.setValue(1)

        self.gridLayout_4.addWidget(self.group_spinbox, 0, 2, 1, 1)

        self.checkBox_define_group = QCheckBox(EventReaderSettingsView)
        self.checkBox_define_group.setObjectName(u"checkBox_define_group")
        self.checkBox_define_group.setEnabled(False)

        self.gridLayout_4.addWidget(self.checkBox_define_group, 0, 3, 1, 1)

        self.group_lineEdit = QLineEdit(EventReaderSettingsView)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setEnabled(False)

        self.gridLayout_4.addWidget(self.group_lineEdit, 0, 4, 1, 1)

        self.label_2 = QLabel(EventReaderSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.event_name_spinbox = QSpinBox(EventReaderSettingsView)
        self.event_name_spinbox.setObjectName(u"event_name_spinbox")
        sizePolicy1.setHeightForWidth(self.event_name_spinbox.sizePolicy().hasHeightForWidth())
        self.event_name_spinbox.setSizePolicy(sizePolicy1)
        self.event_name_spinbox.setMinimum(0)
        self.event_name_spinbox.setValue(2)

        self.gridLayout_4.addWidget(self.event_name_spinbox, 1, 2, 1, 1)

        self.checkBox_define_name = QCheckBox(EventReaderSettingsView)
        self.checkBox_define_name.setObjectName(u"checkBox_define_name")
        self.checkBox_define_name.setEnabled(False)

        self.gridLayout_4.addWidget(self.checkBox_define_name, 1, 3, 1, 1)

        self.name_lineEdit = QLineEdit(EventReaderSettingsView)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setEnabled(False)
        self.name_lineEdit.setMinimumSize(QSize(250, 0))

        self.gridLayout_4.addWidget(self.name_lineEdit, 1, 4, 1, 1)

        self.label_3 = QLabel(EventReaderSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.onset_spinbox = QSpinBox(EventReaderSettingsView)
        self.onset_spinbox.setObjectName(u"onset_spinbox")
        sizePolicy1.setHeightForWidth(self.onset_spinbox.sizePolicy().hasHeightForWidth())
        self.onset_spinbox.setSizePolicy(sizePolicy1)
        self.onset_spinbox.setMinimum(0)
        self.onset_spinbox.setValue(3)

        self.gridLayout_4.addWidget(self.onset_spinbox, 2, 2, 1, 1)

        self.center_checkBox = QCheckBox(EventReaderSettingsView)
        self.center_checkBox.setObjectName(u"center_checkBox")

        self.gridLayout_4.addWidget(self.center_checkBox, 2, 3, 1, 2)

        self.label_4 = QLabel(EventReaderSettingsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)

        self.checkBox_dur_enabled = QCheckBox(EventReaderSettingsView)
        self.checkBox_dur_enabled.setObjectName(u"checkBox_dur_enabled")
        self.checkBox_dur_enabled.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_dur_enabled, 3, 1, 1, 1)

        self.duration_spinbox = QSpinBox(EventReaderSettingsView)
        self.duration_spinbox.setObjectName(u"duration_spinbox")
        sizePolicy1.setHeightForWidth(self.duration_spinbox.sizePolicy().hasHeightForWidth())
        self.duration_spinbox.setSizePolicy(sizePolicy1)
        self.duration_spinbox.setMinimum(0)
        self.duration_spinbox.setValue(4)

        self.gridLayout_4.addWidget(self.duration_spinbox, 3, 2, 1, 1)

        self.checkBox_define_dur = QCheckBox(EventReaderSettingsView)
        self.checkBox_define_dur.setObjectName(u"checkBox_define_dur")
        self.checkBox_define_dur.setEnabled(False)

        self.gridLayout_4.addWidget(self.checkBox_define_dur, 3, 3, 1, 1)

        self.fixed_dur_lineEdit = QLineEdit(EventReaderSettingsView)
        self.fixed_dur_lineEdit.setObjectName(u"fixed_dur_lineEdit")
        self.fixed_dur_lineEdit.setEnabled(False)

        self.gridLayout_4.addWidget(self.fixed_dur_lineEdit, 3, 4, 1, 1)

        self.label_8 = QLabel(EventReaderSettingsView)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_8, 4, 0, 1, 1)

        self.checkBox_chan_enabled = QCheckBox(EventReaderSettingsView)
        self.checkBox_chan_enabled.setObjectName(u"checkBox_chan_enabled")
        self.checkBox_chan_enabled.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_chan_enabled, 4, 1, 1, 1)

        self.channel_spinBox = QSpinBox(EventReaderSettingsView)
        self.channel_spinBox.setObjectName(u"channel_spinBox")
        sizePolicy1.setHeightForWidth(self.channel_spinBox.sizePolicy().hasHeightForWidth())
        self.channel_spinBox.setSizePolicy(sizePolicy1)
        self.channel_spinBox.setValue(5)

        self.gridLayout_4.addWidget(self.channel_spinBox, 4, 2, 1, 1)

        self.checkBox_define_chan = QCheckBox(EventReaderSettingsView)
        self.checkBox_define_chan.setObjectName(u"checkBox_define_chan")
        self.checkBox_define_chan.setEnabled(False)

        self.gridLayout_4.addWidget(self.checkBox_define_chan, 4, 3, 1, 1)

        self.fixed_chan_lineEdit = QLineEdit(EventReaderSettingsView)
        self.fixed_chan_lineEdit.setObjectName(u"fixed_chan_lineEdit")
        self.fixed_chan_lineEdit.setEnabled(False)

        self.gridLayout_4.addWidget(self.fixed_chan_lineEdit, 4, 4, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(210, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.retranslateUi(EventReaderSettingsView)
        self.choose_pushbutton.clicked.connect(EventReaderSettingsView.on_choose)
        self.time_radiobutton.clicked.connect(EventReaderSettingsView.on_input_format_changed)
        self.sample_radiobutton.clicked.connect(EventReaderSettingsView.on_input_format_changed)
        self.checkBox_define_dur.clicked.connect(EventReaderSettingsView.on_event_pos_changed)
        self.group_spinbox.valueChanged.connect(EventReaderSettingsView.on_group_index_changed)
        self.event_name_spinbox.valueChanged.connect(EventReaderSettingsView.on_name_index_changed)
        self.radioButton_personalized.clicked.connect(EventReaderSettingsView.snooz_event_update_slot)
        self.radioButton_snooz.clicked.connect(EventReaderSettingsView.snooz_event_update_slot)
        self.checkBox_group_enabled.clicked.connect(EventReaderSettingsView.group_enabled_slot)
        self.checkBox_dur_enabled.clicked.connect(EventReaderSettingsView.dur_enabled_slot)
        self.checkBox_chan_enabled.clicked.connect(EventReaderSettingsView.chan_enabled_slot)
        self.checkBox_define_group.clicked.connect(EventReaderSettingsView.on_event_pos_changed)
        self.checkBox_define_name.clicked.connect(EventReaderSettingsView.on_event_pos_changed)
        self.checkBox_define_chan.clicked.connect(EventReaderSettingsView.on_event_pos_changed)
        self.duration_spinbox.valueChanged.connect(EventReaderSettingsView.on_duration_index_changed)
        self.channel_spinBox.valueChanged.connect(EventReaderSettingsView.on_chan_index_changed)

        QMetaObject.connectSlotsByName(EventReaderSettingsView)
    # setupUi

    def retranslateUi(self, EventReaderSettingsView):
        EventReaderSettingsView.setWindowTitle(QCoreApplication.translate("EventReaderSettingsView", u"Form", None))
        self.label_10.setText(QCoreApplication.translate("EventReaderSettingsView", u"Event Reader Settings", None))
        self.label.setText(QCoreApplication.translate("EventReaderSettingsView", u"Filename", None))
        self.filename_lineedit.setText("")
        self.filename_lineedit.setPlaceholderText(QCoreApplication.translate("EventReaderSettingsView", u"Choose a file to read", None))
        self.choose_pushbutton.setText(QCoreApplication.translate("EventReaderSettingsView", u"Choose", None))
        self.label_12.setText(QCoreApplication.translate("EventReaderSettingsView", u"Input File Format", None))
        self.radioButton_personalized.setText(QCoreApplication.translate("EventReaderSettingsView", u"Read the input file without any control quality", None))
        self.radioButton_snooz.setText(QCoreApplication.translate("EventReaderSettingsView", u"Convert the input file into a Snooz event DataFrame", None))
        self.label_11.setText(QCoreApplication.translate("EventReaderSettingsView", u"Delimiter", None))
#if QT_CONFIG(tooltip)
        self.delimiter_lineedit.setToolTip(QCoreApplication.translate("EventReaderSettingsView", u"<html><head/><body><p>For tabulation write \\t.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.delimiter_lineedit.setPlaceholderText(QCoreApplication.translate("EventReaderSettingsView", u"Insert delimiter(s)", None))
        self.label_13.setText(QCoreApplication.translate("EventReaderSettingsView", u"Snooz Annotation Format", None))
        self.label_5.setText(QCoreApplication.translate("EventReaderSettingsView", u"Annotation Time format", None))
        self.time_radiobutton.setText(QCoreApplication.translate("EventReaderSettingsView", u"Time", None))
        self.sample_radiobutton.setText(QCoreApplication.translate("EventReaderSettingsView", u"Samples", None))
        self.label_6.setText(QCoreApplication.translate("EventReaderSettingsView", u"Sample rate", None))
        self.sample_rate_lineedit.setText(QCoreApplication.translate("EventReaderSettingsView", u"256", None))
        self.comboBox_time_format.setItemText(0, QCoreApplication.translate("EventReaderSettingsView", u"in seconds, relative to start of file", None))
        self.comboBox_time_format.setItemText(1, QCoreApplication.translate("EventReaderSettingsView", u"hh:mm:ss", None))
        self.comboBox_time_format.setItemText(2, QCoreApplication.translate("EventReaderSettingsView", u"hh:mm:ss.xx", None))

        self.label_7.setText(QCoreApplication.translate("EventReaderSettingsView", u"Column Index", None))
        self.label_9.setText(QCoreApplication.translate("EventReaderSettingsView", u"Group Label", None))
        self.checkBox_group_enabled.setText("")
        self.checkBox_define_group.setText(QCoreApplication.translate("EventReaderSettingsView", u"Define a group", None))
#if QT_CONFIG(tooltip)
        self.group_lineEdit.setToolTip(QCoreApplication.translate("EventReaderSettingsView", u"To define a default event group (when group index column is 0).", None))
#endif // QT_CONFIG(tooltip)
        self.group_lineEdit.setPlaceholderText(QCoreApplication.translate("EventReaderSettingsView", u"Define the group label for all the annotations.", None))
        self.label_2.setText(QCoreApplication.translate("EventReaderSettingsView", u"Name label", None))
        self.checkBox_define_name.setText(QCoreApplication.translate("EventReaderSettingsView", u"Define a name", None))
#if QT_CONFIG(tooltip)
        self.name_lineEdit.setToolTip(QCoreApplication.translate("EventReaderSettingsView", u"To define a default event name (when name index column is 0).", None))
#endif // QT_CONFIG(tooltip)
        self.name_lineEdit.setPlaceholderText(QCoreApplication.translate("EventReaderSettingsView", u"Define the name label for all the annotations.", None))
        self.label_3.setText(QCoreApplication.translate("EventReaderSettingsView", u"Onset/Center", None))
#if QT_CONFIG(tooltip)
        self.center_checkBox.setToolTip(QCoreApplication.translate("EventReaderSettingsView", u"Check if the event is identified by its center instead of its onset.", None))
#endif // QT_CONFIG(tooltip)
        self.center_checkBox.setText(QCoreApplication.translate("EventReaderSettingsView", u"Event identified by its center", None))
        self.label_4.setText(QCoreApplication.translate("EventReaderSettingsView", u"Duration", None))
        self.checkBox_dur_enabled.setText("")
        self.checkBox_define_dur.setText(QCoreApplication.translate("EventReaderSettingsView", u"Define a duration", None))
#if QT_CONFIG(tooltip)
        self.fixed_dur_lineEdit.setToolTip(QCoreApplication.translate("EventReaderSettingsView", u"Enter a fixed duration for all events. Use the \"Annotation Time Format\" defined above.", None))
#endif // QT_CONFIG(tooltip)
        self.fixed_dur_lineEdit.setPlaceholderText(QCoreApplication.translate("EventReaderSettingsView", u"Define a duration for all the annotations.", None))
        self.label_8.setText(QCoreApplication.translate("EventReaderSettingsView", u"Channels", None))
        self.checkBox_chan_enabled.setText("")
#if QT_CONFIG(tooltip)
        self.channel_spinBox.setToolTip(QCoreApplication.translate("EventReaderSettingsView", u"Mark 0 if events are not channel specific (as sleep stage).", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_define_chan.setText(QCoreApplication.translate("EventReaderSettingsView", u"Define a channel", None))
        self.fixed_chan_lineEdit.setPlaceholderText(QCoreApplication.translate("EventReaderSettingsView", u"Define a channel label for all the annotations.", None))
    # retranslateUi


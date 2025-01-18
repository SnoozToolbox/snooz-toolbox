# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_TextFileDefinition.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_TextFileDefinition(object):
    def setupUi(self, TextFileDefinition):
        if not TextFileDefinition.objectName():
            TextFileDefinition.setObjectName(u"TextFileDefinition")
        TextFileDefinition.resize(778, 697)
        TextFileDefinition.setStyleSheet(u"font: 12pt \"Roboto\";")
        TextFileDefinition.setInputMethodHints(Qt.ImhNone)
        self.horizontalLayout_3 = QHBoxLayout(TextFileDefinition)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.label_10 = QLabel(TextFileDefinition)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)

        self.verticalLayout_3.addWidget(self.label_10)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_11 = QLabel(TextFileDefinition)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)

        self.delimiter_lineedit = QLineEdit(TextFileDefinition)
        self.delimiter_lineedit.setObjectName(u"delimiter_lineedit")
        self.delimiter_lineedit.setInputMethodHints(Qt.ImhDialableCharactersOnly)
        self.delimiter_lineedit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.delimiter_lineedit, 0, 1, 1, 1)

        self.label = QLabel(TextFileDefinition)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)

        self.spinBox_nrows_hdr = QSpinBox(TextFileDefinition)
        self.spinBox_nrows_hdr.setObjectName(u"spinBox_nrows_hdr")

        self.gridLayout_3.addWidget(self.spinBox_nrows_hdr, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(TextFileDefinition)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(20, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sample_rate_lineedit = QLineEdit(TextFileDefinition)
        self.sample_rate_lineedit.setObjectName(u"sample_rate_lineedit")
        self.sample_rate_lineedit.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sample_rate_lineedit.sizePolicy().hasHeightForWidth())
        self.sample_rate_lineedit.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.sample_rate_lineedit, 1, 1, 1, 1)

        self.label_6 = QLabel(TextFileDefinition)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.time_radiobutton = QRadioButton(TextFileDefinition)
        self.buttonGroup_2 = QButtonGroup(TextFileDefinition)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.time_radiobutton)
        self.time_radiobutton.setObjectName(u"time_radiobutton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.time_radiobutton.sizePolicy().hasHeightForWidth())
        self.time_radiobutton.setSizePolicy(sizePolicy1)
        self.time_radiobutton.setChecked(True)

        self.gridLayout_2.addWidget(self.time_radiobutton, 0, 0, 1, 1)

        self.textEdit = QTextEdit(TextFileDefinition)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.textEdit, 4, 0, 1, 2)

        self.sample_radiobutton = QRadioButton(TextFileDefinition)
        self.buttonGroup_2.addButton(self.sample_radiobutton)
        self.sample_radiobutton.setObjectName(u"sample_radiobutton")
        sizePolicy1.setHeightForWidth(self.sample_radiobutton.sizePolicy().hasHeightForWidth())
        self.sample_radiobutton.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.sample_radiobutton, 0, 1, 1, 1)

        self.lineEdit_time_format = QLineEdit(TextFileDefinition)
        self.lineEdit_time_format.setObjectName(u"lineEdit_time_format")

        self.gridLayout_2.addWidget(self.lineEdit_time_format, 2, 1, 1, 1)

        self.label_12 = QLabel(TextFileDefinition)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_13 = QLabel(TextFileDefinition)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1)

        self.comboBox_encoding = QComboBox(TextFileDefinition)
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.addItem("")
        self.comboBox_encoding.setObjectName(u"comboBox_encoding")

        self.gridLayout_2.addWidget(self.comboBox_encoding, 3, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.label_7 = QLabel(TextFileDefinition)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_9 = QLabel(TextFileDefinition)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(80, 0))
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self.checkBox_group_enabled = QCheckBox(TextFileDefinition)
        self.checkBox_group_enabled.setObjectName(u"checkBox_group_enabled")
        self.checkBox_group_enabled.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_group_enabled, 0, 1, 1, 1)

        self.group_spinbox = QSpinBox(TextFileDefinition)
        self.group_spinbox.setObjectName(u"group_spinbox")
        sizePolicy.setHeightForWidth(self.group_spinbox.sizePolicy().hasHeightForWidth())
        self.group_spinbox.setSizePolicy(sizePolicy)
        self.group_spinbox.setValue(1)

        self.gridLayout_4.addWidget(self.group_spinbox, 0, 2, 1, 1)

        self.checkBox_define_group = QCheckBox(TextFileDefinition)
        self.checkBox_define_group.setObjectName(u"checkBox_define_group")
        self.checkBox_define_group.setEnabled(False)

        self.gridLayout_4.addWidget(self.checkBox_define_group, 0, 3, 1, 1)

        self.group_lineEdit = QLineEdit(TextFileDefinition)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setEnabled(False)

        self.gridLayout_4.addWidget(self.group_lineEdit, 0, 4, 1, 1)

        self.label_2 = QLabel(TextFileDefinition)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.event_name_spinbox = QSpinBox(TextFileDefinition)
        self.event_name_spinbox.setObjectName(u"event_name_spinbox")
        sizePolicy.setHeightForWidth(self.event_name_spinbox.sizePolicy().hasHeightForWidth())
        self.event_name_spinbox.setSizePolicy(sizePolicy)
        self.event_name_spinbox.setMinimum(0)
        self.event_name_spinbox.setValue(2)

        self.gridLayout_4.addWidget(self.event_name_spinbox, 1, 2, 1, 1)

        self.checkBox_define_name = QCheckBox(TextFileDefinition)
        self.checkBox_define_name.setObjectName(u"checkBox_define_name")
        self.checkBox_define_name.setEnabled(False)

        self.gridLayout_4.addWidget(self.checkBox_define_name, 1, 3, 1, 1)

        self.name_lineEdit = QLineEdit(TextFileDefinition)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setEnabled(False)
        self.name_lineEdit.setMinimumSize(QSize(250, 0))

        self.gridLayout_4.addWidget(self.name_lineEdit, 1, 4, 1, 1)

        self.label_3 = QLabel(TextFileDefinition)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.onset_spinbox = QSpinBox(TextFileDefinition)
        self.onset_spinbox.setObjectName(u"onset_spinbox")
        sizePolicy.setHeightForWidth(self.onset_spinbox.sizePolicy().hasHeightForWidth())
        self.onset_spinbox.setSizePolicy(sizePolicy)
        self.onset_spinbox.setMinimum(0)
        self.onset_spinbox.setValue(3)

        self.gridLayout_4.addWidget(self.onset_spinbox, 2, 2, 1, 1)

        self.center_checkBox = QCheckBox(TextFileDefinition)
        self.center_checkBox.setObjectName(u"center_checkBox")

        self.gridLayout_4.addWidget(self.center_checkBox, 2, 3, 1, 2)

        self.label_4 = QLabel(TextFileDefinition)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)

        self.checkBox_dur_enabled = QCheckBox(TextFileDefinition)
        self.checkBox_dur_enabled.setObjectName(u"checkBox_dur_enabled")
        self.checkBox_dur_enabled.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_dur_enabled, 3, 1, 1, 1)

        self.duration_spinbox = QSpinBox(TextFileDefinition)
        self.duration_spinbox.setObjectName(u"duration_spinbox")
        sizePolicy.setHeightForWidth(self.duration_spinbox.sizePolicy().hasHeightForWidth())
        self.duration_spinbox.setSizePolicy(sizePolicy)
        self.duration_spinbox.setMinimum(0)
        self.duration_spinbox.setValue(4)

        self.gridLayout_4.addWidget(self.duration_spinbox, 3, 2, 1, 1)

        self.checkBox_define_dur = QCheckBox(TextFileDefinition)
        self.checkBox_define_dur.setObjectName(u"checkBox_define_dur")
        self.checkBox_define_dur.setEnabled(False)

        self.gridLayout_4.addWidget(self.checkBox_define_dur, 3, 3, 1, 1)

        self.fixed_dur_lineEdit = QLineEdit(TextFileDefinition)
        self.fixed_dur_lineEdit.setObjectName(u"fixed_dur_lineEdit")
        self.fixed_dur_lineEdit.setEnabled(False)

        self.gridLayout_4.addWidget(self.fixed_dur_lineEdit, 3, 4, 1, 1)

        self.label_8 = QLabel(TextFileDefinition)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_8, 4, 0, 1, 1)

        self.checkBox_chan_enabled = QCheckBox(TextFileDefinition)
        self.checkBox_chan_enabled.setObjectName(u"checkBox_chan_enabled")
        self.checkBox_chan_enabled.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_chan_enabled, 4, 1, 1, 1)

        self.channel_spinBox = QSpinBox(TextFileDefinition)
        self.channel_spinBox.setObjectName(u"channel_spinBox")
        sizePolicy.setHeightForWidth(self.channel_spinBox.sizePolicy().hasHeightForWidth())
        self.channel_spinBox.setSizePolicy(sizePolicy)
        self.channel_spinBox.setValue(5)

        self.gridLayout_4.addWidget(self.channel_spinBox, 4, 2, 1, 1)

        self.checkBox_define_chan = QCheckBox(TextFileDefinition)
        self.checkBox_define_chan.setObjectName(u"checkBox_define_chan")
        self.checkBox_define_chan.setEnabled(False)

        self.gridLayout_4.addWidget(self.checkBox_define_chan, 4, 3, 1, 1)

        self.fixed_chan_lineEdit = QLineEdit(TextFileDefinition)
        self.fixed_chan_lineEdit.setObjectName(u"fixed_chan_lineEdit")
        self.fixed_chan_lineEdit.setEnabled(False)

        self.gridLayout_4.addWidget(self.fixed_chan_lineEdit, 4, 4, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.retranslateUi(TextFileDefinition)
        self.time_radiobutton.clicked.connect(TextFileDefinition.on_input_format_changed)
        self.sample_radiobutton.clicked.connect(TextFileDefinition.on_input_format_changed)
        self.checkBox_define_dur.clicked.connect(TextFileDefinition.on_event_pos_changed)
        self.group_spinbox.valueChanged.connect(TextFileDefinition.on_group_index_changed)
        self.event_name_spinbox.valueChanged.connect(TextFileDefinition.on_name_index_changed)
        self.checkBox_group_enabled.clicked.connect(TextFileDefinition.group_enabled_slot)
        self.checkBox_dur_enabled.clicked.connect(TextFileDefinition.dur_enabled_slot)
        self.checkBox_chan_enabled.clicked.connect(TextFileDefinition.chan_enabled_slot)
        self.checkBox_define_group.clicked.connect(TextFileDefinition.on_event_pos_changed)
        self.checkBox_define_name.clicked.connect(TextFileDefinition.on_event_pos_changed)
        self.checkBox_define_chan.clicked.connect(TextFileDefinition.on_event_pos_changed)
        self.duration_spinbox.valueChanged.connect(TextFileDefinition.on_duration_index_changed)
        self.channel_spinBox.valueChanged.connect(TextFileDefinition.on_chan_index_changed)

        QMetaObject.connectSlotsByName(TextFileDefinition)
    # setupUi

    def retranslateUi(self, TextFileDefinition):
        TextFileDefinition.setWindowTitle(QCoreApplication.translate("TextFileDefinition", u"Form", None))
        self.label_10.setText(QCoreApplication.translate("TextFileDefinition", u"<html><head/><body><p><span style=\" font-weight:600;\">Annotations Reader</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("TextFileDefinition", u"File item separator", None))
#if QT_CONFIG(tooltip)
        self.delimiter_lineedit.setToolTip(QCoreApplication.translate("TextFileDefinition", u"<html><head/><body><p>For tabulation write \\t.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.delimiter_lineedit.setPlaceholderText(QCoreApplication.translate("TextFileDefinition", u"Insert delimiter(s)", None))
        self.label.setText(QCoreApplication.translate("TextFileDefinition", u"Number of rows to skip (reserved for the header)\n"
"Do not include blank rows in the count\n"
"Do not include the row with the column names in the count.", None))
#if QT_CONFIG(tooltip)
        self.spinBox_nrows_hdr.setToolTip(QCoreApplication.translate("TextFileDefinition", u"Blank rows are skipped automatically, so do not include them in the row count to skip. This feature is important to prevent issues with files that end with blank rows.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("TextFileDefinition", u"Annotation Time format", None))
        self.sample_rate_lineedit.setText(QCoreApplication.translate("TextFileDefinition", u"256", None))
        self.label_6.setText(QCoreApplication.translate("TextFileDefinition", u"Sample rate", None))
        self.time_radiobutton.setText(QCoreApplication.translate("TextFileDefinition", u"Time", None))
        self.textEdit.setHtml(QCoreApplication.translate("TextFileDefinition", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For the complete definition see : https://strftime.org/</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Examples of string format code for time : </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" "
                        "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%H:%M:%S for 14:30:45</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%H.%M.%S for 14.30.45</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%H:%M:%S.%f for 14:30:45.123456</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%I:%M:%S %p for 02:30:45 PM</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Leave the time format empty if it is provided as seconds elapsed.</p></body></html>", None))
        self.sample_radiobutton.setText(QCoreApplication.translate("TextFileDefinition", u"Samples", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_time_format.setToolTip(QCoreApplication.translate("TextFileDefinition", u"Let empty to define the time elapsed in seconds. Otherwise define the string format (see https://strftime.org/). ", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("TextFileDefinition", u"Time format if not seconds", None))
        self.label_13.setText(QCoreApplication.translate("TextFileDefinition", u"File encoding", None))
        self.comboBox_encoding.setItemText(0, QCoreApplication.translate("TextFileDefinition", u"utf-8", None))
        self.comboBox_encoding.setItemText(1, QCoreApplication.translate("TextFileDefinition", u"latin-1", None))
        self.comboBox_encoding.setItemText(2, QCoreApplication.translate("TextFileDefinition", u"utf-16", None))
        self.comboBox_encoding.setItemText(3, QCoreApplication.translate("TextFileDefinition", u"utf-32", None))
        self.comboBox_encoding.setItemText(4, QCoreApplication.translate("TextFileDefinition", u"iso-8859", None))
        self.comboBox_encoding.setItemText(5, QCoreApplication.translate("TextFileDefinition", u"ascii", None))
        self.comboBox_encoding.setItemText(6, QCoreApplication.translate("TextFileDefinition", u"ansi", None))

        self.label_7.setText(QCoreApplication.translate("TextFileDefinition", u"Column Index", None))
        self.label_9.setText(QCoreApplication.translate("TextFileDefinition", u"Group Label", None))
        self.checkBox_group_enabled.setText("")
        self.checkBox_define_group.setText(QCoreApplication.translate("TextFileDefinition", u"Define a group", None))
#if QT_CONFIG(tooltip)
        self.group_lineEdit.setToolTip(QCoreApplication.translate("TextFileDefinition", u"To define a default event group (when group index column is 0).", None))
#endif // QT_CONFIG(tooltip)
        self.group_lineEdit.setPlaceholderText(QCoreApplication.translate("TextFileDefinition", u"Define the group label for all the annotations.", None))
        self.label_2.setText(QCoreApplication.translate("TextFileDefinition", u"Name label", None))
        self.checkBox_define_name.setText(QCoreApplication.translate("TextFileDefinition", u"Define a name", None))
#if QT_CONFIG(tooltip)
        self.name_lineEdit.setToolTip(QCoreApplication.translate("TextFileDefinition", u"To define a default event name (when name index column is 0).", None))
#endif // QT_CONFIG(tooltip)
        self.name_lineEdit.setPlaceholderText(QCoreApplication.translate("TextFileDefinition", u"Define the name label for all the annotations.", None))
        self.label_3.setText(QCoreApplication.translate("TextFileDefinition", u"Onset/Center", None))
#if QT_CONFIG(tooltip)
        self.center_checkBox.setToolTip(QCoreApplication.translate("TextFileDefinition", u"Check if the event is identified by its center instead of its onset.", None))
#endif // QT_CONFIG(tooltip)
        self.center_checkBox.setText(QCoreApplication.translate("TextFileDefinition", u"Event identified by its center", None))
        self.label_4.setText(QCoreApplication.translate("TextFileDefinition", u"Duration", None))
        self.checkBox_dur_enabled.setText("")
        self.checkBox_define_dur.setText(QCoreApplication.translate("TextFileDefinition", u"Define a duration", None))
#if QT_CONFIG(tooltip)
        self.fixed_dur_lineEdit.setToolTip(QCoreApplication.translate("TextFileDefinition", u"Enter a fixed duration for all events. Use the \"Annotation Time Format\" defined above.", None))
#endif // QT_CONFIG(tooltip)
        self.fixed_dur_lineEdit.setPlaceholderText(QCoreApplication.translate("TextFileDefinition", u"Define a duration for all the annotations.", None))
        self.label_8.setText(QCoreApplication.translate("TextFileDefinition", u"Channels", None))
        self.checkBox_chan_enabled.setText("")
#if QT_CONFIG(tooltip)
        self.channel_spinBox.setToolTip(QCoreApplication.translate("TextFileDefinition", u"Mark 0 if events are not channel specific (as sleep stage).", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_define_chan.setText(QCoreApplication.translate("TextFileDefinition", u"Define a channel", None))
        self.fixed_chan_lineEdit.setPlaceholderText(QCoreApplication.translate("TextFileDefinition", u"Define a channel label for all the annotations.", None))
    # retranslateUi


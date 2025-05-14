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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_CsvReaderMasterSettingsView(object):
    def setupUi(self, CsvReaderMasterSettingsView):
        if not CsvReaderMasterSettingsView.objectName():
            CsvReaderMasterSettingsView.setObjectName(u"CsvReaderMasterSettingsView")
        CsvReaderMasterSettingsView.resize(725, 353)
        self.horizontalLayout_4 = QHBoxLayout(CsvReaderMasterSettingsView)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(CsvReaderMasterSettingsView)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.fileListWidget = QListWidget(CsvReaderMasterSettingsView)
        self.fileListWidget.setObjectName(u"fileListWidget")

        self.verticalLayout.addWidget(self.fileListWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.choose_pushbutton = QPushButton(CsvReaderMasterSettingsView)
        self.choose_pushbutton.setObjectName(u"choose_pushbutton")

        self.horizontalLayout_3.addWidget(self.choose_pushbutton)

        self.clear_pushButton = QPushButton(CsvReaderMasterSettingsView)
        self.clear_pushButton.setObjectName(u"clear_pushButton")

        self.horizontalLayout_3.addWidget(self.clear_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(CsvReaderMasterSettingsView)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_7)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.group_spinbox = QSpinBox(CsvReaderMasterSettingsView)
        self.group_spinbox.setObjectName(u"group_spinbox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_spinbox.sizePolicy().hasHeightForWidth())
        self.group_spinbox.setSizePolicy(sizePolicy)
        self.group_spinbox.setValue(1)

        self.gridLayout.addWidget(self.group_spinbox, 5, 1, 1, 1)

        self.center_checkBox = QCheckBox(CsvReaderMasterSettingsView)
        self.center_checkBox.setObjectName(u"center_checkBox")

        self.gridLayout.addWidget(self.center_checkBox, 8, 2, 1, 1)

        self.label_10 = QLabel(CsvReaderMasterSettingsView)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)

        self.label_6 = QLabel(CsvReaderMasterSettingsView)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 3, 1, 1)

        self.personnalized_header_checkBox = QCheckBox(CsvReaderMasterSettingsView)
        self.personnalized_header_checkBox.setObjectName(u"personnalized_header_checkBox")

        self.gridLayout.addWidget(self.personnalized_header_checkBox, 12, 1, 1, 1)

        self.label_8 = QLabel(CsvReaderMasterSettingsView)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 1)

        self.label_5 = QLabel(CsvReaderMasterSettingsView)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.time_radiobutton = QRadioButton(CsvReaderMasterSettingsView)
        self.buttonGroup_2 = QButtonGroup(CsvReaderMasterSettingsView)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.time_radiobutton)
        self.time_radiobutton.setObjectName(u"time_radiobutton")
        self.time_radiobutton.setChecked(True)

        self.gridLayout.addWidget(self.time_radiobutton, 1, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 9, 3, 1, 1)

        self.label_2 = QLabel(CsvReaderMasterSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)

        self.channel_spinBox = QSpinBox(CsvReaderMasterSettingsView)
        self.channel_spinBox.setObjectName(u"channel_spinBox")
        sizePolicy.setHeightForWidth(self.channel_spinBox.sizePolicy().hasHeightForWidth())
        self.channel_spinBox.setSizePolicy(sizePolicy)
        self.channel_spinBox.setValue(5)

        self.gridLayout.addWidget(self.channel_spinBox, 11, 1, 1, 1)

        self.label_4 = QLabel(CsvReaderMasterSettingsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 8, 3, 1, 1)

        self.label_9 = QLabel(CsvReaderMasterSettingsView)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 10, 2, 1, 1)

        self.onset_spinbox = QSpinBox(CsvReaderMasterSettingsView)
        self.onset_spinbox.setObjectName(u"onset_spinbox")
        sizePolicy.setHeightForWidth(self.onset_spinbox.sizePolicy().hasHeightForWidth())
        self.onset_spinbox.setSizePolicy(sizePolicy)
        self.onset_spinbox.setMinimum(1)
        self.onset_spinbox.setValue(3)

        self.gridLayout.addWidget(self.onset_spinbox, 8, 1, 1, 1)

        self.label_3 = QLabel(CsvReaderMasterSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)

        self.sample_rate_lineedit = QLineEdit(CsvReaderMasterSettingsView)
        self.sample_rate_lineedit.setObjectName(u"sample_rate_lineedit")
        self.sample_rate_lineedit.setEnabled(False)
        sizePolicy.setHeightForWidth(self.sample_rate_lineedit.sizePolicy().hasHeightForWidth())
        self.sample_rate_lineedit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.sample_rate_lineedit, 3, 2, 1, 1)

        self.sample_radiobutton = QRadioButton(CsvReaderMasterSettingsView)
        self.buttonGroup_2.addButton(self.sample_radiobutton)
        self.sample_radiobutton.setObjectName(u"sample_radiobutton")

        self.gridLayout.addWidget(self.sample_radiobutton, 1, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 10, 3, 1, 1)

        self.fixed_dur_lineEdit = QLineEdit(CsvReaderMasterSettingsView)
        self.fixed_dur_lineEdit.setObjectName(u"fixed_dur_lineEdit")
        self.fixed_dur_lineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.fixed_dur_lineEdit, 10, 1, 1, 1)

        self.event_name_spinbox = QSpinBox(CsvReaderMasterSettingsView)
        self.event_name_spinbox.setObjectName(u"event_name_spinbox")
        sizePolicy.setHeightForWidth(self.event_name_spinbox.sizePolicy().hasHeightForWidth())
        self.event_name_spinbox.setSizePolicy(sizePolicy)
        self.event_name_spinbox.setMinimum(1)
        self.event_name_spinbox.setValue(2)

        self.gridLayout.addWidget(self.event_name_spinbox, 7, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 7, 3, 1, 1)

        self.duration_spinbox = QSpinBox(CsvReaderMasterSettingsView)
        self.duration_spinbox.setObjectName(u"duration_spinbox")
        sizePolicy.setHeightForWidth(self.duration_spinbox.sizePolicy().hasHeightForWidth())
        self.duration_spinbox.setSizePolicy(sizePolicy)
        self.duration_spinbox.setMinimum(0)
        self.duration_spinbox.setValue(4)

        self.gridLayout.addWidget(self.duration_spinbox, 9, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.label_11 = QLabel(CsvReaderMasterSettingsView)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.radioButton_tab = QRadioButton(CsvReaderMasterSettingsView)
        self.buttonGroup = QButtonGroup(CsvReaderMasterSettingsView)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_tab)
        self.radioButton_tab.setObjectName(u"radioButton_tab")
        self.radioButton_tab.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_tab, 0, 1, 1, 1)

        self.radioButton_comma = QRadioButton(CsvReaderMasterSettingsView)
        self.buttonGroup.addButton(self.radioButton_comma)
        self.radioButton_comma.setObjectName(u"radioButton_comma")

        self.gridLayout.addWidget(self.radioButton_comma, 0, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.retranslateUi(CsvReaderMasterSettingsView)
        self.choose_pushbutton.clicked.connect(CsvReaderMasterSettingsView.on_choose)
        self.time_radiobutton.clicked.connect(CsvReaderMasterSettingsView.on_input_format_changed)
        self.sample_radiobutton.clicked.connect(CsvReaderMasterSettingsView.on_input_format_changed)
        self.clear_pushButton.clicked.connect(self.fileListWidget.clear)
        self.duration_spinbox.valueChanged.connect(CsvReaderMasterSettingsView.on_event_pos_changed)
        self.clear_pushButton.clicked.connect(CsvReaderMasterSettingsView.clear_list_slot)

        QMetaObject.connectSlotsByName(CsvReaderMasterSettingsView)
    # setupUi

    def retranslateUi(self, CsvReaderMasterSettingsView):
        CsvReaderMasterSettingsView.setWindowTitle(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Form", None))
        self.label.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Filenames", None))
#if QT_CONFIG(tooltip)
        self.choose_pushbutton.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Select csv files", None))
#endif // QT_CONFIG(tooltip)
        self.choose_pushbutton.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Add", None))
        self.clear_pushButton.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Clear", None))
        self.label_7.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Csv Reader Master Settings", None))
#if QT_CONFIG(tooltip)
        self.group_spinbox.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"The index of the column for the event group. To disable the group mark 0.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.center_checkBox.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Check if the event is identified by its center instead of its onset.", None))
#endif // QT_CONFIG(tooltip)
        self.center_checkBox.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Event identified by its center", None))
        self.label_10.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Event group column", None))
        self.label_6.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Sample rate", None))
#if QT_CONFIG(tooltip)
        self.personnalized_header_checkBox.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Check to keep the read file header, otherwise the header will be replaced with the Snooz header.", None))
#endif // QT_CONFIG(tooltip)
        self.personnalized_header_checkBox.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Personnalized header", None))
        self.label_8.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Fixed duration", None))
        self.label_5.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Input format", None))
        self.time_radiobutton.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Time(s)", None))
        self.label_2.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Event name column", None))
        self.label_4.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Duration column", None))
        self.label_9.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Channel column", None))
#if QT_CONFIG(tooltip)
        self.onset_spinbox.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"The index of the column for the event onset or center. Can not be disabled.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Onset/Center column", None))
        self.sample_rate_lineedit.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"256", None))
        self.sample_radiobutton.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Samples", None))
#if QT_CONFIG(tooltip)
        self.fixed_dur_lineEdit.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"Enter a fixed duration for all events.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.event_name_spinbox.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"The index of the column for the event name. Can not be disabled.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.duration_spinbox.setToolTip(QCoreApplication.translate("CsvReaderMasterSettingsView", u"The index of the column for the event duration. To disable the duration mark 0.", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"File format separator", None))
        self.radioButton_tab.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"tab", None))
        self.radioButton_comma.setText(QCoreApplication.translate("CsvReaderMasterSettingsView", u"comma", None))
    # retranslateUi


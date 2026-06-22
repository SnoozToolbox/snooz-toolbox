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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_EventCompareSettingsView(object):
    def setupUi(self, EventCompareSettingsView):
        if not EventCompareSettingsView.objectName():
            EventCompareSettingsView.setObjectName(u"EventCompareSettingsView")
        EventCompareSettingsView.resize(469, 380)
        self.verticalLayout_3 = QVBoxLayout(EventCompareSettingsView)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(EventCompareSettingsView)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)

        self.verticalLayout_3.addWidget(self.label_5)

        self.line_2 = QFrame(EventCompareSettingsView)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.jaccord_lineEdit = QLineEdit(EventCompareSettingsView)
        self.jaccord_lineEdit.setObjectName(u"jaccord_lineEdit")

        self.gridLayout.addWidget(self.jaccord_lineEdit, 4, 1, 1, 1)

        self.chan_label = QLabel(EventCompareSettingsView)
        self.chan_label.setObjectName(u"chan_label")
        self.chan_label.setLayoutDirection(Qt.LeftToRight)
        self.chan_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.chan_label, 2, 0, 1, 1)

        self.event1_name_lineedit = QLineEdit(EventCompareSettingsView)
        self.event1_name_lineedit.setObjectName(u"event1_name_lineedit")

        self.gridLayout.addWidget(self.event1_name_lineedit, 0, 1, 1, 1)

        self.event2_name_lineedit = QLineEdit(EventCompareSettingsView)
        self.event2_name_lineedit.setObjectName(u"event2_name_lineedit")

        self.gridLayout.addWidget(self.event2_name_lineedit, 1, 1, 1, 1)

        self.channel1_lineedit = QLineEdit(EventCompareSettingsView)
        self.channel1_lineedit.setObjectName(u"channel1_lineedit")

        self.gridLayout.addWidget(self.channel1_lineedit, 2, 1, 1, 1)

        self.label = QLabel(EventCompareSettingsView)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_6 = QLabel(EventCompareSettingsView)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)

        self.label_2 = QLabel(EventCompareSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 4, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_7 = QLabel(EventCompareSettingsView)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.channel2_lineedit = QLineEdit(EventCompareSettingsView)
        self.channel2_lineedit.setObjectName(u"channel2_lineedit")

        self.gridLayout.addWidget(self.channel2_lineedit, 3, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(EventCompareSettingsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_3.addWidget(self.label_4)

        self.line = QFrame(EventCompareSettingsView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(EventCompareSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.label_3)

        self.filename_lineEdit = QLineEdit(EventCompareSettingsView)
        self.filename_lineEdit.setObjectName(u"filename_lineEdit")

        self.horizontalLayout.addWidget(self.filename_lineEdit)

        self.browse_pushButton = QPushButton(EventCompareSettingsView)
        self.browse_pushButton.setObjectName(u"browse_pushButton")

        self.horizontalLayout.addWidget(self.browse_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(EventCompareSettingsView)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_8)

        self.label_lineEdit = QLineEdit(EventCompareSettingsView)
        self.label_lineEdit.setObjectName(u"label_lineEdit")

        self.horizontalLayout_2.addWidget(self.label_lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.retranslateUi(EventCompareSettingsView)
        self.browse_pushButton.clicked.connect(EventCompareSettingsView.on_choose)

        QMetaObject.connectSlotsByName(EventCompareSettingsView)
    # setupUi

    def retranslateUi(self, EventCompareSettingsView):
        EventCompareSettingsView.setWindowTitle(QCoreApplication.translate("EventCompareSettingsView", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("EventCompareSettingsView", u"Input settings", None))
#if QT_CONFIG(tooltip)
        self.jaccord_lineEdit.setToolTip(QCoreApplication.translate("EventCompareSettingsView", u"Enter the Jaccord index (similarity) threshold (from 0 et 1) to mark an event as valid.", None))
#endif // QT_CONFIG(tooltip)
        self.jaccord_lineEdit.setText(QCoreApplication.translate("EventCompareSettingsView", u"0.2", None))
        self.chan_label.setText(QCoreApplication.translate("EventCompareSettingsView", u"Channel label event 1", None))
#if QT_CONFIG(tooltip)
        self.event1_name_lineedit.setToolTip(QCoreApplication.translate("EventCompareSettingsView", u"Enter the event label to evaluate.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.event2_name_lineedit.setToolTip(QCoreApplication.translate("EventCompareSettingsView", u"Enter the event label to evaluate.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.channel1_lineedit.setToolTip(QCoreApplication.translate("EventCompareSettingsView", u"Enter the channel to filter events 1 to evaluate.  Let it empty to compare the events from all channels.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("EventCompareSettingsView", u"Event 1 name", None))
        self.label_6.setText(QCoreApplication.translate("EventCompareSettingsView", u"Jaccord Index threshold", None))
        self.label_2.setText(QCoreApplication.translate("EventCompareSettingsView", u"Event 2 name", None))
        self.label_7.setText(QCoreApplication.translate("EventCompareSettingsView", u"Channel label event 2", None))
#if QT_CONFIG(tooltip)
        self.channel2_lineedit.setToolTip(QCoreApplication.translate("EventCompareSettingsView", u"Enter the channel to filter events 2 to evaluate.  Let it empty to compare the events from all channels.", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("EventCompareSettingsView", u"Output settings", None))
        self.label_3.setText(QCoreApplication.translate("EventCompareSettingsView", u"Filename", None))
#if QT_CONFIG(tooltip)
        self.filename_lineEdit.setToolTip(QCoreApplication.translate("EventCompareSettingsView", u"Filename to save performance evaluation. ", None))
#endif // QT_CONFIG(tooltip)
        self.browse_pushButton.setText(QCoreApplication.translate("EventCompareSettingsView", u"Browse", None))
        self.label_8.setText(QCoreApplication.translate("EventCompareSettingsView", u"Label", None))
#if QT_CONFIG(tooltip)
        self.label_lineEdit.setToolTip(QCoreApplication.translate("EventCompareSettingsView", u"Optional to add information to the column header in the performance output file. ", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi


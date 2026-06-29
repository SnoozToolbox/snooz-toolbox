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

class Ui_PerformanceByEventSettingsView(object):
    def setupUi(self, PerformanceByEventSettingsView):
        if not PerformanceByEventSettingsView.objectName():
            PerformanceByEventSettingsView.setObjectName(u"PerformanceByEventSettingsView")
        PerformanceByEventSettingsView.resize(469, 380)
        self.verticalLayout_3 = QVBoxLayout(PerformanceByEventSettingsView)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(PerformanceByEventSettingsView)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)

        self.verticalLayout_2.addWidget(self.label_5)

        self.line_2 = QFrame(PerformanceByEventSettingsView)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.jaccord_lineEdit = QLineEdit(PerformanceByEventSettingsView)
        self.jaccord_lineEdit.setObjectName(u"jaccord_lineEdit")

        self.gridLayout.addWidget(self.jaccord_lineEdit, 4, 1, 1, 1)

        self.chan_label = QLabel(PerformanceByEventSettingsView)
        self.chan_label.setObjectName(u"chan_label")
        self.chan_label.setLayoutDirection(Qt.LeftToRight)
        self.chan_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.chan_label, 2, 0, 1, 1)

        self.event1_name_lineedit = QLineEdit(PerformanceByEventSettingsView)
        self.event1_name_lineedit.setObjectName(u"event1_name_lineedit")

        self.gridLayout.addWidget(self.event1_name_lineedit, 0, 1, 1, 1)

        self.event2_name_lineedit = QLineEdit(PerformanceByEventSettingsView)
        self.event2_name_lineedit.setObjectName(u"event2_name_lineedit")

        self.gridLayout.addWidget(self.event2_name_lineedit, 1, 1, 1, 1)

        self.channel1_lineedit = QLineEdit(PerformanceByEventSettingsView)
        self.channel1_lineedit.setObjectName(u"channel1_lineedit")

        self.gridLayout.addWidget(self.channel1_lineedit, 2, 1, 1, 1)

        self.label = QLabel(PerformanceByEventSettingsView)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_6 = QLabel(PerformanceByEventSettingsView)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 2, 1, 1)

        self.label_2 = QLabel(PerformanceByEventSettingsView)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 4, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_7 = QLabel(PerformanceByEventSettingsView)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.channel2_lineedit = QLineEdit(PerformanceByEventSettingsView)
        self.channel2_lineedit.setObjectName(u"channel2_lineedit")

        self.gridLayout.addWidget(self.channel2_lineedit, 3, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(PerformanceByEventSettingsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)

        self.line = QFrame(PerformanceByEventSettingsView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(PerformanceByEventSettingsView)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.filename_lineEdit = QLineEdit(PerformanceByEventSettingsView)
        self.filename_lineEdit.setObjectName(u"filename_lineEdit")

        self.horizontalLayout.addWidget(self.filename_lineEdit)

        self.browse_pushButton = QPushButton(PerformanceByEventSettingsView)
        self.browse_pushButton.setObjectName(u"browse_pushButton")

        self.horizontalLayout.addWidget(self.browse_pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(PerformanceByEventSettingsView)
        self.browse_pushButton.clicked.connect(PerformanceByEventSettingsView.on_choose)

        QMetaObject.connectSlotsByName(PerformanceByEventSettingsView)
    # setupUi

    def retranslateUi(self, PerformanceByEventSettingsView):
        PerformanceByEventSettingsView.setWindowTitle(QCoreApplication.translate("PerformanceByEventSettingsView", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("PerformanceByEventSettingsView", u"Input settings", None))
#if QT_CONFIG(tooltip)
        self.jaccord_lineEdit.setToolTip(QCoreApplication.translate("PerformanceByEventSettingsView", u"Enter the Jaccord index (similarity) threshold (from 0 et 1) to mark an event as valid.", None))
#endif // QT_CONFIG(tooltip)
        self.jaccord_lineEdit.setText(QCoreApplication.translate("PerformanceByEventSettingsView", u"0.2", None))
        self.chan_label.setText(QCoreApplication.translate("PerformanceByEventSettingsView", u"Channel label event 1", None))
#if QT_CONFIG(tooltip)
        self.event1_name_lineedit.setToolTip(QCoreApplication.translate("PerformanceByEventSettingsView", u"Enter the event label to evaluate.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.event2_name_lineedit.setToolTip(QCoreApplication.translate("PerformanceByEventSettingsView", u"Enter the event label to evaluate.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.channel1_lineedit.setToolTip(QCoreApplication.translate("PerformanceByEventSettingsView", u"Enter the channel to filter events 1 to evaluate.  Let it empty to compare the events from all channels.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("PerformanceByEventSettingsView", u"Event 1 name", None))
        self.label_6.setText(QCoreApplication.translate("PerformanceByEventSettingsView", u"Jaccord Index threshold", None))
        self.label_2.setText(QCoreApplication.translate("PerformanceByEventSettingsView", u"Event 2 name", None))
        self.label_7.setText(QCoreApplication.translate("PerformanceByEventSettingsView", u"Channel label event 2", None))
#if QT_CONFIG(tooltip)
        self.channel2_lineedit.setToolTip(QCoreApplication.translate("PerformanceByEventSettingsView", u"Enter the channel to filter events 2 to evaluate.  Let it empty to compare the events from all channels.", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("PerformanceByEventSettingsView", u"Output settings", None))
        self.label_3.setText(QCoreApplication.translate("PerformanceByEventSettingsView", u"Filename", None))
#if QT_CONFIG(tooltip)
        self.filename_lineEdit.setToolTip(QCoreApplication.translate("PerformanceByEventSettingsView", u"Filename to save performance evaluation. ", None))
#endif // QT_CONFIG(tooltip)
        self.browse_pushButton.setText(QCoreApplication.translate("PerformanceByEventSettingsView", u"Browse", None))
    # retranslateUi


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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SubtractSignalsSettingsView(object):
    def setupUi(self, SubtractSignalsSettingsView):
        if not SubtractSignalsSettingsView.objectName():
            SubtractSignalsSettingsView.setObjectName(u"SubtractSignalsSettingsView")
        SubtractSignalsSettingsView.resize(348, 161)
        self.gridLayout_2 = QGridLayout(SubtractSignalsSettingsView)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(SubtractSignalsSettingsView)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(SubtractSignalsSettingsView)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.channel_lineEdit = QLineEdit(SubtractSignalsSettingsView)
        self.channel_lineEdit.setObjectName(u"channel_lineEdit")

        self.gridLayout.addWidget(self.channel_lineEdit, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.label_2 = QLabel(SubtractSignalsSettingsView)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.channel_to_sub_lineEdit = QLineEdit(SubtractSignalsSettingsView)
        self.channel_to_sub_lineEdit.setObjectName(u"channel_to_sub_lineEdit")

        self.gridLayout.addWidget(self.channel_to_sub_lineEdit, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.line = QFrame(SubtractSignalsSettingsView)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 0, 0, 1, 2)

        self.label_3 = QLabel(SubtractSignalsSettingsView)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.new_chan_name_lineEdit = QLineEdit(SubtractSignalsSettingsView)
        self.new_chan_name_lineEdit.setObjectName(u"new_chan_name_lineEdit")

        self.gridLayout.addWidget(self.new_chan_name_lineEdit, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(SubtractSignalsSettingsView)

        QMetaObject.connectSlotsByName(SubtractSignalsSettingsView)
    # setupUi

    def retranslateUi(self, SubtractSignalsSettingsView):
        SubtractSignalsSettingsView.setWindowTitle(QCoreApplication.translate("SubtractSignalsSettingsView", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("SubtractSignalsSettingsView", u"SubtractSignals settings", None))
        self.label.setText(QCoreApplication.translate("SubtractSignalsSettingsView", u"channel", None))
#if QT_CONFIG(tooltip)
        self.channel_lineEdit.setToolTip(QCoreApplication.translate("SubtractSignalsSettingsView", u"Name of the initial channel (separate additional channel with a comma without space) ", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("SubtractSignalsSettingsView", u"channel to Subtract", None))
#if QT_CONFIG(tooltip)
        self.channel_to_sub_lineEdit.setToolTip(QCoreApplication.translate("SubtractSignalsSettingsView", u"Name of the channel to Subtract to channel.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("SubtractSignalsSettingsView", u"new channel name", None))
#if QT_CONFIG(tooltip)
        self.new_chan_name_lineEdit.setToolTip(QCoreApplication.translate("SubtractSignalsSettingsView", u"To rename the new Subtracted channel (valid only when a single channel is Subtracted).  The default name is \"channel - channel to Subtract\".", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi


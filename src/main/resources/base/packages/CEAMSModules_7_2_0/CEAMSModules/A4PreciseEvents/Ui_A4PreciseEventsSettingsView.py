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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_A4PreciseEventsSettingsView(object):
    def setupUi(self, A4PreciseEventsSettingsView):
        if not A4PreciseEventsSettingsView.objectName():
            A4PreciseEventsSettingsView.setObjectName(u"A4PreciseEventsSettingsView")
        A4PreciseEventsSettingsView.resize(560, 316)
        self.verticalLayout = QVBoxLayout(A4PreciseEventsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(A4PreciseEventsSettingsView)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_2)

        self.label_3 = QLabel(A4PreciseEventsSettingsView)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(170, 0))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.group_lineEdit = QLineEdit(A4PreciseEventsSettingsView)
        self.group_lineEdit.setObjectName(u"group_lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.group_lineEdit)

        self.label_4 = QLabel(A4PreciseEventsSettingsView)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(170, 0))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.name_lineEdit = QLineEdit(A4PreciseEventsSettingsView)
        self.name_lineEdit.setObjectName(u"name_lineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.name_lineEdit)

        self.label_5 = QLabel(A4PreciseEventsSettingsView)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(170, 0))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.min_dur_lineEdit = QLineEdit(A4PreciseEventsSettingsView)
        self.min_dur_lineEdit.setObjectName(u"min_dur_lineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.min_dur_lineEdit)

        self.label_6 = QLabel(A4PreciseEventsSettingsView)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(170, 0))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.max_dur_lineEdit = QLineEdit(A4PreciseEventsSettingsView)
        self.max_dur_lineEdit.setObjectName(u"max_dur_lineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.max_dur_lineEdit)

        self.label = QLabel(A4PreciseEventsSettingsView)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.label)

        self.win_len_sec_label = QLabel(A4PreciseEventsSettingsView)
        self.win_len_sec_label.setObjectName(u"win_len_sec_label")
        self.win_len_sec_label.setMinimumSize(QSize(170, 0))

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.win_len_sec_label)

        self.win_len_sec_lineedit = QLineEdit(A4PreciseEventsSettingsView)
        self.win_len_sec_lineedit.setObjectName(u"win_len_sec_lineedit")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.win_len_sec_lineedit)

        self.len_adjust_sec_label = QLabel(A4PreciseEventsSettingsView)
        self.len_adjust_sec_label.setObjectName(u"len_adjust_sec_label")
        self.len_adjust_sec_label.setMinimumSize(QSize(170, 0))

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.len_adjust_sec_label)

        self.len_adjust_sec_lineedit = QLineEdit(A4PreciseEventsSettingsView)
        self.len_adjust_sec_lineedit.setObjectName(u"len_adjust_sec_lineedit")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.len_adjust_sec_lineedit)


        self.horizontalLayout.addLayout(self.formLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(A4PreciseEventsSettingsView)

        QMetaObject.connectSlotsByName(A4PreciseEventsSettingsView)
    # setupUi

    def retranslateUi(self, A4PreciseEventsSettingsView):
        A4PreciseEventsSettingsView.setWindowTitle(QCoreApplication.translate("A4PreciseEventsSettingsView", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("A4PreciseEventsSettingsView", u"To filter events", None))
        self.label_3.setText(QCoreApplication.translate("A4PreciseEventsSettingsView", u"Event Group", None))
        self.label_4.setText(QCoreApplication.translate("A4PreciseEventsSettingsView", u"Event Name", None))
        self.label_5.setText(QCoreApplication.translate("A4PreciseEventsSettingsView", u"Minimum duration accepted (sec)", None))
        self.label_6.setText(QCoreApplication.translate("A4PreciseEventsSettingsView", u"Maximum duration accepted (sec)", None))
        self.label.setText(QCoreApplication.translate("A4PreciseEventsSettingsView", u"To precise events", None))
        self.win_len_sec_label.setText(QCoreApplication.translate("A4PreciseEventsSettingsView", u"Windows length (sec)", None))
#if QT_CONFIG(tooltip)
        self.win_len_sec_lineedit.setToolTip(QCoreApplication.translate("A4PreciseEventsSettingsView", u"Window length used to compute the RMS value.", None))
#endif // QT_CONFIG(tooltip)
        self.len_adjust_sec_label.setText(QCoreApplication.translate("A4PreciseEventsSettingsView", u"Length adjust (sec)", None))
#if QT_CONFIG(tooltip)
        self.len_adjust_sec_lineedit.setToolTip(QCoreApplication.translate("A4PreciseEventsSettingsView", u"The window length to evaluate before and after the original event.", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi


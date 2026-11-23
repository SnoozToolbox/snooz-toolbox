# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EventSubdivisionSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QSpinBox, QWidget)

class Ui_EventSubdivisionSettingsView(object):
    def setupUi(self, EventSubdivisionSettingsView):
        if not EventSubdivisionSettingsView.objectName():
            EventSubdivisionSettingsView.setObjectName(u"EventSubdivisionSettingsView")
        EventSubdivisionSettingsView.resize(446, 328)
        self.label_8 = QLabel(EventSubdivisionSettingsView)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 8, 231, 20))
        font = QFont()
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayoutWidget = QWidget(EventSubdivisionSettingsView)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 30, 361, 84))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.events_names_lineEdit = QLineEdit(self.formLayoutWidget)
        self.events_names_lineEdit.setObjectName(u"events_names_lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.events_names_lineEdit)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.win_time_spinbox = QSpinBox(self.formLayoutWidget)
        self.win_time_spinbox.setObjectName(u"win_time_spinbox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.win_time_spinbox)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.n_window_spinBox = QSpinBox(self.formLayoutWidget)
        self.n_window_spinBox.setObjectName(u"n_window_spinBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.n_window_spinBox)


        self.retranslateUi(EventSubdivisionSettingsView)

        QMetaObject.connectSlotsByName(EventSubdivisionSettingsView)
    # setupUi

    def retranslateUi(self, EventSubdivisionSettingsView):
        EventSubdivisionSettingsView.setWindowTitle(QCoreApplication.translate("EventSubdivisionSettingsView", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("EventSubdivisionSettingsView", u"EventSubdivision settings", None))
        self.label.setText(QCoreApplication.translate("EventSubdivisionSettingsView", u"Event name", None))
#if QT_CONFIG(tooltip)
        self.events_names_lineEdit.setToolTip(QCoreApplication.translate("EventSubdivisionSettingsView", u"String of desired events separated by , \n"
"An empty string will do every events. (e.g N1 or N1,N2,N3,R)", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("EventSubdivisionSettingsView", u"Window lenght (sec)", None))
#if QT_CONFIG(tooltip)
        self.win_time_spinbox.setToolTip(QCoreApplication.translate("EventSubdivisionSettingsView", u"Window lenght of the subdivision in seconds. \n"
"Must be a dividers of the original event duration.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("EventSubdivisionSettingsView", u"Number of windows", None))
#if QT_CONFIG(tooltip)
        self.n_window_spinBox.setToolTip(QCoreApplication.translate("EventSubdivisionSettingsView", u"<html><head/><body><p>Optional. The number of window overlapping inside the previous event. 0 if there is no overlapping.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi


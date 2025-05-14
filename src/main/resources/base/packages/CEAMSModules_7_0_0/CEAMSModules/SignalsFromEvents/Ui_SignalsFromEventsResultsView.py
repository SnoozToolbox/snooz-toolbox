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
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from widgets.QLineEditLive import QLineEditLive

class Ui_SignalsFromEventsResultsView(object):
    def setupUi(self, SignalsFromEventsResultsView):
        if not SignalsFromEventsResultsView.objectName():
            SignalsFromEventsResultsView.setObjectName(u"SignalsFromEventsResultsView")
        SignalsFromEventsResultsView.resize(791, 190)
        self.gridLayout = QGridLayout(SignalsFromEventsResultsView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(SignalsFromEventsResultsView)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(SignalsFromEventsResultsView)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.event_index_lineEdit = QLineEdit(SignalsFromEventsResultsView)
        self.event_index_lineEdit.setObjectName(u"event_index_lineEdit")
        self.event_index_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.event_index_lineEdit)

        self.prev_but = QPushButton(SignalsFromEventsResultsView)
        self.prev_but.setObjectName(u"prev_but")
        self.prev_but.setEnabled(True)

        self.horizontalLayout.addWidget(self.prev_but)

        self.next_but = QPushButton(SignalsFromEventsResultsView)
        self.next_but.setObjectName(u"next_but")
        self.next_but.setEnabled(True)

        self.horizontalLayout.addWidget(self.next_but)

        self.time_label = QLabel(SignalsFromEventsResultsView)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setLayoutDirection(Qt.LeftToRight)
        self.time_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.time_label)

        self.time_lineedit = QLineEditLive(SignalsFromEventsResultsView)
        self.time_lineedit.setObjectName(u"time_lineedit")
        self.time_lineedit.setEnabled(False)
        self.time_lineedit.setMaximumSize(QSize(100, 16777215))
        self.time_lineedit.setText(u"00:00:00")

        self.horizontalLayout.addWidget(self.time_lineedit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(SignalsFromEventsResultsView)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.event_lineEdit = QLineEdit(SignalsFromEventsResultsView)
        self.event_lineEdit.setObjectName(u"event_lineEdit")
        self.event_lineEdit.setEnabled(False)
        self.event_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.event_lineEdit)

        self.duration_label = QLabel(SignalsFromEventsResultsView)
        self.duration_label.setObjectName(u"duration_label")

        self.horizontalLayout_3.addWidget(self.duration_label)

        self.duration_lineEdit = QLineEdit(SignalsFromEventsResultsView)
        self.duration_lineEdit.setObjectName(u"duration_lineEdit")
        self.duration_lineEdit.setEnabled(False)
        self.duration_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.duration_lineEdit)

        self.checkBox_ylim_norm = QCheckBox(SignalsFromEventsResultsView)
        self.checkBox_ylim_norm.setObjectName(u"checkBox_ylim_norm")
        self.checkBox_ylim_norm.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBox_ylim_norm)

        self.lineEdit_ylim_fixed = QLineEdit(SignalsFromEventsResultsView)
        self.lineEdit_ylim_fixed.setObjectName(u"lineEdit_ylim_fixed")
        self.lineEdit_ylim_fixed.setEnabled(False)
        self.lineEdit_ylim_fixed.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_ylim_fixed)

        self.checkBox_display_y = QCheckBox(SignalsFromEventsResultsView)
        self.checkBox_display_y.setObjectName(u"checkBox_display_y")

        self.horizontalLayout_3.addWidget(self.checkBox_display_y)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")
        self.result_layout.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout.addLayout(self.result_layout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(SignalsFromEventsResultsView)
        self.next_but.clicked.connect(SignalsFromEventsResultsView.on_next_button)
        self.prev_but.clicked.connect(SignalsFromEventsResultsView.on_prev_button)
        self.event_index_lineEdit.editingFinished.connect(SignalsFromEventsResultsView.on_event_index_changed)
        self.checkBox_ylim_norm.clicked.connect(SignalsFromEventsResultsView.y_limits_change_slot)
        self.lineEdit_ylim_fixed.editingFinished.connect(SignalsFromEventsResultsView.y_limits_change_slot)
        self.checkBox_display_y.clicked.connect(SignalsFromEventsResultsView.update_y_axis_label_slot)

        QMetaObject.connectSlotsByName(SignalsFromEventsResultsView)
    # setupUi

    def retranslateUi(self, SignalsFromEventsResultsView):
        SignalsFromEventsResultsView.setWindowTitle(QCoreApplication.translate("SignalsFromEventsResultsView", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("SignalsFromEventsResultsView", u"Display signals from events", None))
        self.label_4.setText(QCoreApplication.translate("SignalsFromEventsResultsView", u"Event Number", None))
        self.event_index_lineEdit.setText(QCoreApplication.translate("SignalsFromEventsResultsView", u"0", None))
#if QT_CONFIG(tooltip)
        self.prev_but.setToolTip(QCoreApplication.translate("SignalsFromEventsResultsView", u"Display the previous window (window length will be added to the time elapsed).", None))
#endif // QT_CONFIG(tooltip)
        self.prev_but.setText(QCoreApplication.translate("SignalsFromEventsResultsView", u"<<", None))
#if QT_CONFIG(tooltip)
        self.next_but.setToolTip(QCoreApplication.translate("SignalsFromEventsResultsView", u"Display the next window (window length will be added to the time elapsed).", None))
#endif // QT_CONFIG(tooltip)
        self.next_but.setText(QCoreApplication.translate("SignalsFromEventsResultsView", u">>", None))
        self.time_label.setText(QCoreApplication.translate("SignalsFromEventsResultsView", u"Time elapsed (HH:MM:SS)", None))
#if QT_CONFIG(tooltip)
        self.time_lineedit.setToolTip(QCoreApplication.translate("SignalsFromEventsResultsView", u"Time elapsed since the beginning of the recording (ex. 01:10:5.5)\n"
"Press enter to display the detection window.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("SignalsFromEventsResultsView", u"Event", None))
        self.duration_label.setText(QCoreApplication.translate("SignalsFromEventsResultsView", u"Duration (sec)", None))
        self.checkBox_ylim_norm.setText(QCoreApplication.translate("SignalsFromEventsResultsView", u"Normaliize y limits", None))
        self.checkBox_display_y.setText(QCoreApplication.translate("SignalsFromEventsResultsView", u"Display y axis", None))
    # retranslateUi


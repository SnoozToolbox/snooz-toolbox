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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from widgets.QLineEditLive import QLineEditLive

class Ui_DetectionViewResultsView(object):
    def setupUi(self, DetectionViewResultsView):
        if not DetectionViewResultsView.objectName():
            DetectionViewResultsView.setObjectName(u"DetectionViewResultsView")
        DetectionViewResultsView.resize(633, 125)
        self.gridLayout = QGridLayout(DetectionViewResultsView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(DetectionViewResultsView)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.filename_label = QLabel(DetectionViewResultsView)
        self.filename_label.setObjectName(u"filename_label")

        self.horizontalLayout_2.addWidget(self.filename_label)

        self.filename_lineedit_2 = QLineEdit(DetectionViewResultsView)
        self.filename_lineedit_2.setObjectName(u"filename_lineedit_2")

        self.horizontalLayout_2.addWidget(self.filename_lineedit_2)

        self.choose_but = QPushButton(DetectionViewResultsView)
        self.choose_but.setObjectName(u"choose_but")

        self.horizontalLayout_2.addWidget(self.choose_but)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.time_label = QLabel(DetectionViewResultsView)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setLayoutDirection(Qt.LeftToRight)
        self.time_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.time_label)

        self.time_lineedit = QLineEditLive(DetectionViewResultsView)
        self.time_lineedit.setObjectName(u"time_lineedit")
        self.time_lineedit.setText(u"00:00:0.0")

        self.horizontalLayout.addWidget(self.time_lineedit)

        self.prev_but = QPushButton(DetectionViewResultsView)
        self.prev_but.setObjectName(u"prev_but")
        self.prev_but.setEnabled(False)

        self.horizontalLayout.addWidget(self.prev_but)

        self.next_but = QPushButton(DetectionViewResultsView)
        self.next_but.setObjectName(u"next_but")
        self.next_but.setEnabled(False)

        self.horizontalLayout.addWidget(self.next_but)

        self.label = QLabel(DetectionViewResultsView)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.win_len_lineEdit = QLineEdit(DetectionViewResultsView)
        self.win_len_lineEdit.setObjectName(u"win_len_lineEdit")

        self.horizontalLayout.addWidget(self.win_len_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(DetectionViewResultsView)
        self.choose_but.clicked.connect(DetectionViewResultsView.on_choose_button)
        self.next_but.clicked.connect(DetectionViewResultsView.on_next_button)
        self.prev_but.clicked.connect(DetectionViewResultsView.on_prev_button)
        self.time_lineedit.returnPressed.connect(DetectionViewResultsView.on_show_button)
        self.win_len_lineEdit.returnPressed.connect(DetectionViewResultsView.on_show_button)

        QMetaObject.connectSlotsByName(DetectionViewResultsView)
    # setupUi

    def retranslateUi(self, DetectionViewResultsView):
        DetectionViewResultsView.setWindowTitle(QCoreApplication.translate("DetectionViewResultsView", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("DetectionViewResultsView", u"To display an additional detection window", None))
        self.filename_label.setText(QCoreApplication.translate("DetectionViewResultsView", u"Filename", None))
#if QT_CONFIG(tooltip)
        self.filename_lineedit_2.setToolTip(QCoreApplication.translate("DetectionViewResultsView", u"Python filename to load to display detection window.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.choose_but.setToolTip(QCoreApplication.translate("DetectionViewResultsView", u"Browse the Python filename to load data to display an additional detection window.", None))
#endif // QT_CONFIG(tooltip)
        self.choose_but.setText(QCoreApplication.translate("DetectionViewResultsView", u"Choose", None))
        self.time_label.setText(QCoreApplication.translate("DetectionViewResultsView", u"Time elapsed (HH:MM:SS)", None))
#if QT_CONFIG(tooltip)
        self.time_lineedit.setToolTip(QCoreApplication.translate("DetectionViewResultsView", u"Time elapsed since the beginning of the recording (ex. 01:10:5.5)\n"
"Press enter to display the detection window.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.prev_but.setToolTip(QCoreApplication.translate("DetectionViewResultsView", u"Display the previous window (window length will be added to the time elapsed).", None))
#endif // QT_CONFIG(tooltip)
        self.prev_but.setText(QCoreApplication.translate("DetectionViewResultsView", u"<<", None))
#if QT_CONFIG(tooltip)
        self.next_but.setToolTip(QCoreApplication.translate("DetectionViewResultsView", u"Display the next window (window length will be added to the time elapsed).", None))
#endif // QT_CONFIG(tooltip)
        self.next_but.setText(QCoreApplication.translate("DetectionViewResultsView", u">>", None))
        self.label.setText(QCoreApplication.translate("DetectionViewResultsView", u"Window length", None))
#if QT_CONFIG(tooltip)
        self.win_len_lineEdit.setToolTip(QCoreApplication.translate("DetectionViewResultsView", u"Time window length to show. \n"
"Press enter to display the detection window.", None))
#endif // QT_CONFIG(tooltip)
        self.win_len_lineEdit.setText(QCoreApplication.translate("DetectionViewResultsView", u"30", None))
    # retranslateUi


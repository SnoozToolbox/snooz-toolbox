# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DetectionsCohortReviewSettingsView.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QHBoxLayout, QLabel, QListView, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSplitter,
    QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_DetectionsCohortReviewSettingsView(object):
    def setupUi(self, DetectionsCohortReviewSettingsView):
        if not DetectionsCohortReviewSettingsView.objectName():
            DetectionsCohortReviewSettingsView.setObjectName(u"DetectionsCohortReviewSettingsView")
        DetectionsCohortReviewSettingsView.resize(929, 800)
        DetectionsCohortReviewSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.horizontalLayout_3 = QHBoxLayout(DetectionsCohortReviewSettingsView)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.splitter = QSplitter(DetectionsCohortReviewSettingsView)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.splitter.setHandleWidth(15)
        self.splitter.setChildrenCollapsible(False)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.subject_listView = QListView(self.layoutWidget)
        self.subject_listView.setObjectName(u"subject_listView")
        self.subject_listView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.gridLayout.addWidget(self.subject_listView, 1, 0, 1, 1)

        self.chan_subject_listView = QListView(self.layoutWidget)
        self.chan_subject_listView.setObjectName(u"chan_subject_listView")

        self.gridLayout.addWidget(self.chan_subject_listView, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.clear_pushButton = QPushButton(self.layoutWidget)
        self.clear_pushButton.setObjectName(u"clear_pushButton")

        self.horizontalLayout.addWidget(self.clear_pushButton)

        self.add_pushButton = QPushButton(self.layoutWidget)
        self.add_pushButton.setObjectName(u"add_pushButton")

        self.horizontalLayout.addWidget(self.add_pushButton)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.all_subject_chan_checkBox = QCheckBox(self.layoutWidget)
        self.all_subject_chan_checkBox.setObjectName(u"all_subject_chan_checkBox")

        self.gridLayout.addWidget(self.all_subject_chan_checkBox, 2, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.all_cohort_chan_checkBox = QCheckBox(self.layoutWidget)
        self.all_cohort_chan_checkBox.setObjectName(u"all_cohort_chan_checkBox")

        self.horizontalLayout_2.addWidget(self.all_cohort_chan_checkBox)

        self.add_ROI_pushButton = QPushButton(self.layoutWidget)
        self.add_ROI_pushButton.setObjectName(u"add_ROI_pushButton")

        self.horizontalLayout_2.addWidget(self.add_ROI_pushButton)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)

        self.chan_cohort_listWidget = QListWidget(self.layoutWidget)
        self.chan_cohort_listWidget.setObjectName(u"chan_cohort_listWidget")

        self.gridLayout.addWidget(self.chan_cohort_listWidget, 1, 2, 1, 1)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.message_textEdit = QTextEdit(self.layoutWidget1)
        self.message_textEdit.setObjectName(u"message_textEdit")
        self.message_textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.message_textEdit)

        self.splitter.addWidget(self.layoutWidget1)

        self.horizontalLayout_3.addWidget(self.splitter)


        self.retranslateUi(DetectionsCohortReviewSettingsView)
        self.clear_pushButton.clicked.connect(DetectionsCohortReviewSettingsView.clear_subject_slot)
        self.add_pushButton.clicked.connect(DetectionsCohortReviewSettingsView.add_subject_slot)
        self.all_subject_chan_checkBox.clicked.connect(DetectionsCohortReviewSettingsView.select_all_subject_chan_slot)
        self.all_cohort_chan_checkBox.clicked.connect(DetectionsCohortReviewSettingsView.select_all_cohort_chan_slot)
        self.add_ROI_pushButton.clicked.connect(DetectionsCohortReviewSettingsView.add_ROI_slot)
        self.subject_listView.clicked.connect(DetectionsCohortReviewSettingsView.subject_selection_changed_slot)

        QMetaObject.connectSlotsByName(DetectionsCohortReviewSettingsView)
    # setupUi

    def retranslateUi(self, DetectionsCohortReviewSettingsView):
        DetectionsCohortReviewSettingsView.setWindowTitle(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Form", None))
        self.label.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Subject List", None))
        self.label_2.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Subject Channel List", None))
        self.label_3.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Cohort Channel List", None))
        self.clear_pushButton.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Clear", None))
        self.add_pushButton.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Add Events Report", None))
        self.all_subject_chan_checkBox.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Select All", None))
        self.all_cohort_chan_checkBox.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Select All", None))
#if QT_CONFIG(tooltip)
        self.add_ROI_pushButton.setToolTip(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Rename your channel labels first. Adding the ROIs must be the final step.", None))
#endif // QT_CONFIG(tooltip)
        self.add_ROI_pushButton.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Add ROI", None))
        self.label_4.setText(QCoreApplication.translate("DetectionsCohortReviewSettingsView", u"Event File information", None))
    # retranslateUi


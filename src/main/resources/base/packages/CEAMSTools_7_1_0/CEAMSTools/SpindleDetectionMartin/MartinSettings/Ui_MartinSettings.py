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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_MartinSettings(object):
    def setupUi(self, MartinSettings):
        if not MartinSettings.objectName():
            MartinSettings.setObjectName(u"MartinSettings")
        MartinSettings.resize(846, 552)
        self.verticalLayout_2 = QVBoxLayout(MartinSettings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_6 = QLabel(MartinSettings)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_6.setFont(font)

        self.verticalLayout_2.addWidget(self.label_6)

        self.textEdit = QTextEdit(MartinSettings)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 185))
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label = QLabel(MartinSettings)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(MartinSettings)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(230, 0))
        self.label_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.label_2)

        self.group_lineEdit = QLineEdit(MartinSettings)
        self.group_lineEdit.setObjectName(u"group_lineEdit")
        self.group_lineEdit.setMinimumSize(QSize(120, 0))
        self.group_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.group_lineEdit)


        self.formLayout_2.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout_2.setItem(0, QFormLayout.FieldRole, self.horizontalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(MartinSettings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(230, 0))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.name_lineEdit = QLineEdit(MartinSettings)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(120, 0))
        self.name_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_3.addWidget(self.name_lineEdit)


        self.formLayout_2.setLayout(1, QFormLayout.LabelRole, self.horizontalLayout_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout_2.setItem(1, QFormLayout.FieldRole, self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.label_5 = QLabel(MartinSettings)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_2.addWidget(self.label_5)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(MartinSettings)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(230, 0))
        self.label_4.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.threshold_lineEdit = QLineEdit(MartinSettings)
        self.threshold_lineEdit.setObjectName(u"threshold_lineEdit")
        self.threshold_lineEdit.setMinimumSize(QSize(120, 0))
        self.threshold_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_2.addWidget(self.threshold_lineEdit)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout.setItem(0, QFormLayout.FieldRole, self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.threshold_cycle_checkBox = QCheckBox(MartinSettings)
        self.threshold_cycle_checkBox.setObjectName(u"threshold_cycle_checkBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.threshold_cycle_checkBox.sizePolicy().hasHeightForWidth())
        self.threshold_cycle_checkBox.setSizePolicy(sizePolicy1)
        self.threshold_cycle_checkBox.setMinimumSize(QSize(350, 0))
        self.threshold_cycle_checkBox.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.threshold_cycle_checkBox)

        self.precise_checkBox = QCheckBox(MartinSettings)
        self.precise_checkBox.setObjectName(u"precise_checkBox")
        self.precise_checkBox.setMinimumSize(QSize(350, 0))

        self.verticalLayout.addWidget(self.precise_checkBox)


        self.formLayout.setLayout(1, QFormLayout.LabelRole, self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formLayout.setItem(1, QFormLayout.FieldRole, self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(MartinSettings)
        self.threshold_cycle_checkBox.stateChanged.connect(MartinSettings.thresh_per_cycle_slot)

        QMetaObject.connectSlotsByName(MartinSettings)
    # setupUi

    def retranslateUi(self, MartinSettings):
        MartinSettings.setWindowTitle("")
        MartinSettings.setStyleSheet(QCoreApplication.translate("MartinSettings", u"font: 12pt \"Roboto\";", None))
        self.label_6.setText(QCoreApplication.translate("MartinSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Spindle detector based on RMS values in the sigma band.</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("MartinSettings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:135%;\">Band-pass filters (11\u201315 Hz) the EEG signal to compute the RMS on sliding windows (25 ms length with a step of 25 ms), and then applies a threshold (95th percentile).</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:135%;\"><span style=\" text-decoration: underline;\">Reference</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:135%;\">[1] N. Martin <span styl"
                        "e=\" font-style:italic;\">et al.</span>, \u201cTopography of age-related changes in sleep spindles,\u201d <span style=\" font-style:italic;\">Neurobiol. Aging</span>, vol. 34, no. 2, pp. 468\u2013476, Feb. 2013, doi: <a href=\"https://doi.org/10.1016/j.neurobiolaging.2012.05.020\"><span style=\" text-decoration: underline; color:#0000ff;\">10.1016/j.neurobiolaging.2012.05.020</span></a>. </p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MartinSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Events Settings</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MartinSettings", u"Group", None))
#if QT_CONFIG(tooltip)
        self.group_lineEdit.setToolTip(QCoreApplication.translate("MartinSettings", u"Define in which group the spindles will be added.", None))
#endif // QT_CONFIG(tooltip)
        self.group_lineEdit.setText(QCoreApplication.translate("MartinSettings", u"spindle", None))
        self.label_3.setText(QCoreApplication.translate("MartinSettings", u"Name", None))
#if QT_CONFIG(tooltip)
        self.name_lineEdit.setToolTip(QCoreApplication.translate("MartinSettings", u"Define the name of the spindle events.", None))
#endif // QT_CONFIG(tooltip)
        self.name_lineEdit.setText(QCoreApplication.translate("MartinSettings", u"a4", None))
        self.label_5.setText(QCoreApplication.translate("MartinSettings", u"<html><head/><body><p><span style=\" font-weight:600;\">Martin (alias a4) Settings</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MartinSettings", u"Threshold (percentile)", None))
        self.threshold_lineEdit.setText(QCoreApplication.translate("MartinSettings", u"95", None))
        self.threshold_cycle_checkBox.setText(QCoreApplication.translate("MartinSettings", u"Compute the threshold for each sleep cycle", None))
#if QT_CONFIG(tooltip)
        self.precise_checkBox.setToolTip(QCoreApplication.translate("MartinSettings", u"The RMS values are computed on a sliding window (for each sample) before the onset and after the end of the event to precise the event length.  The detected even cannot be shorter only unchanged or longer.", None))
#endif // QT_CONFIG(tooltip)
        self.precise_checkBox.setText(QCoreApplication.translate("MartinSettings", u"Precise onset and duration of detected events", None))
    # retranslateUi


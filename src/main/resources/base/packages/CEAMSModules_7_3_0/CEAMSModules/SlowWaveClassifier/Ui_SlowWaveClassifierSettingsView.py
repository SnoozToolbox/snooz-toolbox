# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SlowWaveClassifierSettingsView.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)
import themes_rc

class Ui_SlowWaveClassifierSettingsView(object):
    def setupUi(self, SlowWaveClassifierSettingsView):
        if not SlowWaveClassifierSettingsView.objectName():
            SlowWaveClassifierSettingsView.setObjectName(u"SlowWaveClassifierSettingsView")
        SlowWaveClassifierSettingsView.resize(985, 325)
        SlowWaveClassifierSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(SlowWaveClassifierSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(2)
        self.label = QLabel(SlowWaveClassifierSettingsView)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.textEdit = QTextEdit(SlowWaveClassifierSettingsView)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 70))
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.textEdit)

        self.radioButton_automatic_classification = QRadioButton(SlowWaveClassifierSettingsView)
        self.radioButton_automatic_classification.setObjectName(u"radioButton_automatic_classification")
        self.radioButton_automatic_classification.setChecked(True)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.radioButton_automatic_classification)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_categories = QRadioButton(SlowWaveClassifierSettingsView)
        self.radioButton_categories.setObjectName(u"radioButton_categories")

        self.horizontalLayout_2.addWidget(self.radioButton_categories)

        self.categories_label = QLabel(SlowWaveClassifierSettingsView)
        self.categories_label.setObjectName(u"categories_label")
        self.categories_label.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.categories_label)

        self.num_categories_spinBox = QSpinBox(SlowWaveClassifierSettingsView)
        self.num_categories_spinBox.setObjectName(u"num_categories_spinBox")
        self.num_categories_spinBox.setEnabled(False)
        self.num_categories_spinBox.setMinimum(1)
        self.num_categories_spinBox.setMaximum(4)
        self.num_categories_spinBox.setValue(2)

        self.horizontalLayout_2.addWidget(self.num_categories_spinBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(4, QFormLayout.SpanningRole, self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(5, QFormLayout.LabelRole, self.verticalSpacer_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SlowWaveClassifierSettingsView)

        QMetaObject.connectSlotsByName(SlowWaveClassifierSettingsView)
    # setupUi

    def retranslateUi(self, SlowWaveClassifierSettingsView):
        SlowWaveClassifierSettingsView.setWindowTitle(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"Form", None))
        self.label.setText(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"<html><head/><body><p><span style=\" font-weight:700;\">Select the criteria</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For an automatic classification, you can keep the parameters as they are. If you want to specify the number of categories, please uncheck the automatic classification option and change the number in the box for the number of categories desired.</p></body></html>", None))
        self.radioButton_automatic_classification.setText(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"Classify sleep slow waves automatically with a gaussian mixture and Akaike Criterion Information (AIC)", None))
        self.radioButton_categories.setText(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"Specify the number of categories                          ", None))
        self.categories_label.setText(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"Number of sleep slow waves categories               ", None))
    # retranslateUi


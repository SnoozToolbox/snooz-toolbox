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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QLabel,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_SlowWaveClassifierSettingsView(object):
    def setupUi(self, SlowWaveClassifierSettingsView):
        if not SlowWaveClassifierSettingsView.objectName():
            SlowWaveClassifierSettingsView.setObjectName(u"SlowWaveClassifierSettingsView")
        SlowWaveClassifierSettingsView.resize(805, 252)
        SlowWaveClassifierSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.verticalLayout = QVBoxLayout(SlowWaveClassifierSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(2)
        self.categories_label = QLabel(SlowWaveClassifierSettingsView)
        self.categories_label.setObjectName(u"categories_label")
        self.categories_label.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.categories_label)

        self.num_categories_spinBox = QSpinBox(SlowWaveClassifierSettingsView)
        self.num_categories_spinBox.setObjectName(u"num_categories_spinBox")
        self.num_categories_spinBox.setEnabled(False)
        self.num_categories_spinBox.setMinimum(1)
        self.num_categories_spinBox.setMaximum(4)
        self.num_categories_spinBox.setValue(2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.num_categories_spinBox)

        self.automatic_classification_checkBox = QCheckBox(SlowWaveClassifierSettingsView)
        self.automatic_classification_checkBox.setObjectName(u"automatic_classification_checkBox")
        self.automatic_classification_checkBox.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.automatic_classification_checkBox)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SlowWaveClassifierSettingsView)
        self.automatic_classification_checkBox.clicked.connect(SlowWaveClassifierSettingsView.on_input_format_changed)

        QMetaObject.connectSlotsByName(SlowWaveClassifierSettingsView)
    # setupUi

    def retranslateUi(self, SlowWaveClassifierSettingsView):
        SlowWaveClassifierSettingsView.setWindowTitle(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"Form", None))
        self.categories_label.setText(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"Number of sleep slow waves categories", None))
        self.automatic_classification_checkBox.setText(QCoreApplication.translate("SlowWaveClassifierSettingsView", u"Classify sleep slow waves automatically with a gaussian mixture and Akaike Criterion Information (AIC)", None))
    # retranslateUi


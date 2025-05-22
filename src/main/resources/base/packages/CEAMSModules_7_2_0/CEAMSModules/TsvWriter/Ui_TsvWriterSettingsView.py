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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_TsvWriterSettingsView(object):
    def setupUi(self, TsvWriterSettingsView):
        if not TsvWriterSettingsView.objectName():
            TsvWriterSettingsView.setObjectName(u"TsvWriterSettingsView")
        TsvWriterSettingsView.resize(411, 210)
        self.verticalLayout = QVBoxLayout(TsvWriterSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(TsvWriterSettingsView)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.filename_lineedit = QLineEdit(TsvWriterSettingsView)
        self.filename_lineedit.setObjectName(u"filename_lineedit")
        self.filename_lineedit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.filename_lineedit, 0, 1, 1, 1)

        self.choose_pushbutton = QPushButton(TsvWriterSettingsView)
        self.choose_pushbutton.setObjectName(u"choose_pushbutton")

        self.gridLayout.addWidget(self.choose_pushbutton, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.EDF_annot_checkBox = QCheckBox(TsvWriterSettingsView)
        self.EDF_annot_checkBox.setObjectName(u"EDF_annot_checkBox")
        self.EDF_annot_checkBox.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.EDF_annot_checkBox)

        self.add_time_checkBox = QCheckBox(TsvWriterSettingsView)
        self.add_time_checkBox.setObjectName(u"add_time_checkBox")

        self.verticalLayout.addWidget(self.add_time_checkBox)

        self.append_data_checkBox = QCheckBox(TsvWriterSettingsView)
        self.append_data_checkBox.setObjectName(u"append_data_checkBox")

        self.verticalLayout.addWidget(self.append_data_checkBox)

        self.index_checkBox = QCheckBox(TsvWriterSettingsView)
        self.index_checkBox.setObjectName(u"index_checkBox")

        self.verticalLayout.addWidget(self.index_checkBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(TsvWriterSettingsView)
        self.choose_pushbutton.clicked.connect(TsvWriterSettingsView.on_choose)

        QMetaObject.connectSlotsByName(TsvWriterSettingsView)
    # setupUi

    def retranslateUi(self, TsvWriterSettingsView):
        TsvWriterSettingsView.setWindowTitle(QCoreApplication.translate("TsvWriterSettingsView", u"Form", None))
        self.label.setText(QCoreApplication.translate("TsvWriterSettingsView", u"Filename", None))
        self.filename_lineedit.setText("")
        self.filename_lineedit.setPlaceholderText(QCoreApplication.translate("TsvWriterSettingsView", u"Choose a TSV file write to", None))
        self.choose_pushbutton.setText(QCoreApplication.translate("TsvWriterSettingsView", u"Choose", None))
#if QT_CONFIG(tooltip)
        self.EDF_annot_checkBox.setToolTip(QCoreApplication.translate("TsvWriterSettingsView", u"To write specific channel event in the EDF+ format.\n"
"event_name = event_name@@channel_label ex) spindle@@EEG C3", None))
#endif // QT_CONFIG(tooltip)
        self.EDF_annot_checkBox.setText(QCoreApplication.translate("TsvWriterSettingsView", u"EDF+ annotations format", None))
        self.add_time_checkBox.setText(QCoreApplication.translate("TsvWriterSettingsView", u"Add time elapsed (HH:MM:SS)", None))
        self.append_data_checkBox.setText(QCoreApplication.translate("TsvWriterSettingsView", u"Append data to file", None))
        self.index_checkBox.setText(QCoreApplication.translate("TsvWriterSettingsView", u"Add index values", None))
    # retranslateUi


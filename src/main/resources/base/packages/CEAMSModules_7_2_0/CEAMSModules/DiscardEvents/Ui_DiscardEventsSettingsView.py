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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_DiscardEventsSettingsView(object):
    def setupUi(self, DiscardEventsSettingsView):
        if not DiscardEventsSettingsView.objectName():
            DiscardEventsSettingsView.setObjectName(u"DiscardEventsSettingsView")
        DiscardEventsSettingsView.resize(625, 417)
        self.verticalLayout = QVBoxLayout(DiscardEventsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DiscardEventsSettingsView)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.event_group_lineEdit = QLineEdit(DiscardEventsSettingsView)
        self.event_group_lineEdit.setObjectName(u"event_group_lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.event_group_lineEdit)

        self.label_2 = QLabel(DiscardEventsSettingsView)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.event_name_lineEdit = QLineEdit(DiscardEventsSettingsView)
        self.event_name_lineEdit.setObjectName(u"event_name_lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.event_name_lineEdit)

        self.min_len_sec_label = QLabel(DiscardEventsSettingsView)
        self.min_len_sec_label.setObjectName(u"min_len_sec_label")
        self.min_len_sec_label.setMinimumSize(QSize(180, 0))
        self.min_len_sec_label.setMaximumSize(QSize(180, 16777215))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.min_len_sec_label)

        self.min_len_sec_lineedit = QLineEdit(DiscardEventsSettingsView)
        self.min_len_sec_lineedit.setObjectName(u"min_len_sec_lineedit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.min_len_sec_lineedit)

        self.max_len_sec_label = QLabel(DiscardEventsSettingsView)
        self.max_len_sec_label.setObjectName(u"max_len_sec_label")
        self.max_len_sec_label.setMinimumSize(QSize(180, 0))
        self.max_len_sec_label.setMaximumSize(QSize(180, 16777215))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.max_len_sec_label)

        self.max_len_sec_lineedit = QLineEdit(DiscardEventsSettingsView)
        self.max_len_sec_lineedit.setObjectName(u"max_len_sec_lineedit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.max_len_sec_lineedit)

        self.artefact_free_checkBox = QCheckBox(DiscardEventsSettingsView)
        self.artefact_free_checkBox.setObjectName(u"artefact_free_checkBox")
        self.artefact_free_checkBox.setMinimumSize(QSize(180, 0))
        self.artefact_free_checkBox.setMaximumSize(QSize(180, 16777215))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.artefact_free_checkBox)

        self.artefact_group_label = QLabel(DiscardEventsSettingsView)
        self.artefact_group_label.setObjectName(u"artefact_group_label")
        self.artefact_group_label.setMinimumSize(QSize(180, 0))
        self.artefact_group_label.setMaximumSize(QSize(180, 16777215))

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.artefact_group_label)

        self.artefact_group_lineedit = QLineEdit(DiscardEventsSettingsView)
        self.artefact_group_lineedit.setObjectName(u"artefact_group_lineedit")
        self.artefact_group_lineedit.setEnabled(False)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.artefact_group_lineedit)

        self.artefact_name_label = QLabel(DiscardEventsSettingsView)
        self.artefact_name_label.setObjectName(u"artefact_name_label")
        self.artefact_name_label.setMinimumSize(QSize(180, 0))
        self.artefact_name_label.setMaximumSize(QSize(180, 16777215))

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.artefact_name_label)

        self.artefact_name_lineedit = QLineEdit(DiscardEventsSettingsView)
        self.artefact_name_lineedit.setObjectName(u"artefact_name_lineedit")
        self.artefact_name_lineedit.setEnabled(False)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.artefact_name_lineedit)


        self.horizontalLayout.addLayout(self.formLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 193, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(DiscardEventsSettingsView)
        self.artefact_free_checkBox.clicked.connect(DiscardEventsSettingsView.on_artefact_free_check)

        QMetaObject.connectSlotsByName(DiscardEventsSettingsView)
    # setupUi

    def retranslateUi(self, DiscardEventsSettingsView):
        DiscardEventsSettingsView.setWindowTitle(QCoreApplication.translate("DiscardEventsSettingsView", u"Form", None))
        self.label.setText(QCoreApplication.translate("DiscardEventsSettingsView", u"Event group", None))
#if QT_CONFIG(tooltip)
        self.event_group_lineEdit.setToolTip(QCoreApplication.translate("DiscardEventsSettingsView", u"The user can define a single group (and let the name blank) or a single name (and let the group blank). \n"
"If group and name are defined, they must be defined in pairs.\n"
"Each group should be separated by a comma.\n"
"The group works as a pattern matching.  ", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("DiscardEventsSettingsView", u"Event name", None))
#if QT_CONFIG(tooltip)
        self.event_name_lineEdit.setToolTip(QCoreApplication.translate("DiscardEventsSettingsView", u"The user can define a single group (and let the name blank) or a single name (and let the group blank). \n"
"If group and name are defined, they must be defined in pairs.\n"
"Each name should be separated by a comma.\n"
"The name works as a pattern matching.  ", None))
#endif // QT_CONFIG(tooltip)
        self.min_len_sec_label.setText(QCoreApplication.translate("DiscardEventsSettingsView", u"minimum length accepted (s)", None))
        self.max_len_sec_label.setText(QCoreApplication.translate("DiscardEventsSettingsView", u"maximum length accepted (s)", None))
#if QT_CONFIG(tooltip)
        self.artefact_free_checkBox.setToolTip(QCoreApplication.translate("DiscardEventsSettingsView", u"Check to discard events that occur during an artefact.", None))
#endif // QT_CONFIG(tooltip)
        self.artefact_free_checkBox.setText(QCoreApplication.translate("DiscardEventsSettingsView", u"artefact free", None))
        self.artefact_group_label.setText(QCoreApplication.translate("DiscardEventsSettingsView", u"artefact group", None))
#if QT_CONFIG(tooltip)
        self.artefact_group_lineedit.setToolTip(QCoreApplication.translate("DiscardEventsSettingsView", u"The user can define a single group (and let the name blank) or a single name (and let the group blank). \n"
"If group and name are defined, they must be defined in pairs.\n"
"Each group should be separated by a comma.\n"
"The group works as a pattern matching.  ", None))
#endif // QT_CONFIG(tooltip)
        self.artefact_name_label.setText(QCoreApplication.translate("DiscardEventsSettingsView", u"artefact name", None))
#if QT_CONFIG(tooltip)
        self.artefact_name_lineedit.setToolTip(QCoreApplication.translate("DiscardEventsSettingsView", u"The user can define a single group (and let the name blank) or a single name (and let the group blank). \n"
"If group and name are defined, they must be defined in pairs.\n"
"Each name should be separated by a comma.\n"
"The name works as a pattern matching.  ", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi


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
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_FilterEventsSettingsView(object):
    def setupUi(self, FilterEventsSettingsView):
        if not FilterEventsSettingsView.objectName():
            FilterEventsSettingsView.setObjectName(u"FilterEventsSettingsView")
        FilterEventsSettingsView.resize(312, 452)
        self.horizontalLayout_3 = QHBoxLayout(FilterEventsSettingsView)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_8 = QLabel(FilterEventsSettingsView)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_8)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_33 = QLabel(FilterEventsSettingsView)
        self.label_33.setObjectName(u"label_33")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_33)

        self.group_lineEdit = QLineEdit(FilterEventsSettingsView)
        self.group_lineEdit.setObjectName(u"group_lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.group_lineEdit)

        self.label_34 = QLabel(FilterEventsSettingsView)
        self.label_34.setObjectName(u"label_34")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_34)

        self.name_lineEdit = QLineEdit(FilterEventsSettingsView)
        self.name_lineEdit.setObjectName(u"name_lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name_lineEdit)

        self.label_9 = QLabel(FilterEventsSettingsView)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.stages_lineEdit = QLineEdit(FilterEventsSettingsView)
        self.stages_lineEdit.setObjectName(u"stages_lineEdit")
        self.stages_lineEdit.setEnabled(True)
        self.stages_lineEdit.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.stages_lineEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.frame = QFrame(FilterEventsSettingsView)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.stage2_checkBox = QCheckBox(self.frame)
        self.stage2_checkBox.setObjectName(u"stage2_checkBox")

        self.gridLayout.addWidget(self.stage2_checkBox, 2, 0, 1, 1)

        self.nrem_checkBox = QCheckBox(self.frame)
        self.nrem_checkBox.setObjectName(u"nrem_checkBox")

        self.gridLayout.addWidget(self.nrem_checkBox, 0, 1, 1, 1)

        self.rem_checkBox = QCheckBox(self.frame)
        self.rem_checkBox.setObjectName(u"rem_checkBox")

        self.gridLayout.addWidget(self.rem_checkBox, 5, 0, 1, 1)

        self.undetermined_checkBox = QCheckBox(self.frame)
        self.undetermined_checkBox.setObjectName(u"undetermined_checkBox")

        self.gridLayout.addWidget(self.undetermined_checkBox, 8, 0, 1, 1)

        self.stage1_checkBox = QCheckBox(self.frame)
        self.stage1_checkBox.setObjectName(u"stage1_checkBox")

        self.gridLayout.addWidget(self.stage1_checkBox, 1, 0, 1, 1)

        self.technicaltime_checkBox = QCheckBox(self.frame)
        self.technicaltime_checkBox.setObjectName(u"technicaltime_checkBox")

        self.gridLayout.addWidget(self.technicaltime_checkBox, 7, 0, 1, 1)

        self.nwake_checkBox = QCheckBox(self.frame)
        self.nwake_checkBox.setObjectName(u"nwake_checkBox")

        self.gridLayout.addWidget(self.nwake_checkBox, 1, 1, 1, 1)

        self.wake_checkBox = QCheckBox(self.frame)
        self.wake_checkBox.setObjectName(u"wake_checkBox")
        self.wake_checkBox.setEnabled(True)
        self.wake_checkBox.setChecked(False)

        self.gridLayout.addWidget(self.wake_checkBox, 0, 0, 1, 1)

        self.stage4_checkBox = QCheckBox(self.frame)
        self.stage4_checkBox.setObjectName(u"stage4_checkBox")

        self.gridLayout.addWidget(self.stage4_checkBox, 4, 0, 1, 1)

        self.stage3_checkBox = QCheckBox(self.frame)
        self.stage3_checkBox.setObjectName(u"stage3_checkBox")

        self.gridLayout.addWidget(self.stage3_checkBox, 3, 0, 1, 1)

        self.movementtime_checkBox = QCheckBox(self.frame)
        self.movementtime_checkBox.setObjectName(u"movementtime_checkBox")

        self.gridLayout.addWidget(self.movementtime_checkBox, 6, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 52, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(FilterEventsSettingsView)
        self.wake_checkBox.stateChanged.connect(FilterEventsSettingsView.on_event_stages_changed)
        self.undetermined_checkBox.stateChanged.connect(FilterEventsSettingsView.on_event_stages_changed)
        self.technicaltime_checkBox.stateChanged.connect(FilterEventsSettingsView.on_event_stages_changed)
        self.movementtime_checkBox.stateChanged.connect(FilterEventsSettingsView.on_event_stages_changed)
        self.rem_checkBox.stateChanged.connect(FilterEventsSettingsView.on_event_stages_changed)
        self.stage4_checkBox.stateChanged.connect(FilterEventsSettingsView.on_event_stages_changed)
        self.stage3_checkBox.stateChanged.connect(FilterEventsSettingsView.on_event_stages_changed)
        self.stage2_checkBox.stateChanged.connect(FilterEventsSettingsView.on_event_stages_changed)
        self.stage1_checkBox.stateChanged.connect(FilterEventsSettingsView.on_event_stages_changed)
        self.nwake_checkBox.stateChanged.connect(FilterEventsSettingsView.on_event_nwake_changed)
        self.nrem_checkBox.stateChanged.connect(FilterEventsSettingsView.on_event_nrem_changed)

        QMetaObject.connectSlotsByName(FilterEventsSettingsView)
    # setupUi

    def retranslateUi(self, FilterEventsSettingsView):
        FilterEventsSettingsView.setWindowTitle(QCoreApplication.translate("FilterEventsSettingsView", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("FilterEventsSettingsView", u"Filter Events settings", None))
        self.label_33.setText(QCoreApplication.translate("FilterEventsSettingsView", u"Group", None))
#if QT_CONFIG(tooltip)
        self.group_lineEdit.setToolTip(QCoreApplication.translate("FilterEventsSettingsView", u"Filter events based on their group (literal string pattern).", None))
#endif // QT_CONFIG(tooltip)
        self.label_34.setText(QCoreApplication.translate("FilterEventsSettingsView", u"Name", None))
#if QT_CONFIG(tooltip)
        self.name_lineEdit.setToolTip(QCoreApplication.translate("FilterEventsSettingsView", u"Filter events based on their name (literal string pattern).", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("FilterEventsSettingsView", u"Stages", None))
#if QT_CONFIG(tooltip)
        self.stages_lineEdit.setToolTip(QCoreApplication.translate("FilterEventsSettingsView", u"Define the sleep stage selection with the checkbox below.", None))
#endif // QT_CONFIG(tooltip)
        self.stage2_checkBox.setText(QCoreApplication.translate("FilterEventsSettingsView", u"N2", None))
        self.nrem_checkBox.setText(QCoreApplication.translate("FilterEventsSettingsView", u"All NREM", None))
        self.rem_checkBox.setText(QCoreApplication.translate("FilterEventsSettingsView", u"R", None))
        self.undetermined_checkBox.setText(QCoreApplication.translate("FilterEventsSettingsView", u"Unscored", None))
        self.stage1_checkBox.setText(QCoreApplication.translate("FilterEventsSettingsView", u"N1", None))
        self.technicaltime_checkBox.setText(QCoreApplication.translate("FilterEventsSettingsView", u"Technical time", None))
#if QT_CONFIG(tooltip)
        self.nwake_checkBox.setToolTip(QCoreApplication.translate("FilterEventsSettingsView", u"Check to select all sleep stages and exclude wake, movement, technical issues and unscored", None))
#endif // QT_CONFIG(tooltip)
        self.nwake_checkBox.setText(QCoreApplication.translate("FilterEventsSettingsView", u"All asleep stages", None))
        self.wake_checkBox.setText(QCoreApplication.translate("FilterEventsSettingsView", u"Wake", None))
        self.stage4_checkBox.setText(QCoreApplication.translate("FilterEventsSettingsView", u"Stage 4", None))
        self.stage3_checkBox.setText(QCoreApplication.translate("FilterEventsSettingsView", u"N3", None))
        self.movementtime_checkBox.setText(QCoreApplication.translate("FilterEventsSettingsView", u"Movement time", None))
    # retranslateUi


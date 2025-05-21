# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_IntroStepYASA.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QLabel,
    QLayout, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
import themes_rc

class Ui_IntroStepYASA(object):
    def setupUi(self, IntroStepYASA):
        if not IntroStepYASA.objectName():
            IntroStepYASA.setObjectName(u"IntroStepYASA")
        IntroStepYASA.resize(736, 568)
        IntroStepYASA.setStyleSheet(u"font: 10pt \"Roboto-Regular\"; QLabel {background-color: rgb(255, 255, 255);}")
        self.verticalLayout_4 = QVBoxLayout(IntroStepYASA)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(IntroStepYASA)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 100))
        self.label_2.setMaximumSize(QSize(500, 60))
        font = QFont()
        font.setFamilies([u"Roboto-Regular"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label = QLabel(IntroStepYASA)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.textEdit = QTextEdit(IntroStepYASA)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.textEdit.setStyleSheet(u"")
        self.textEdit.setFrameShape(QFrame.Shape.HLine)
        self.textEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_4 = QLabel(IntroStepYASA)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setSizeIncrement(QSize(0, 0))
        self.label_4.setFont(font)
        self.label_4.setFrameShadow(QFrame.Shadow.Plain)
        self.label_4.setLineWidth(0)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.textEdit_2 = QTextEdit(IntroStepYASA)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(0, 0))
        self.textEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_2.setFrameShape(QFrame.Shape.HLine)
        self.textEdit_2.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_2.setLineWidth(0)
        self.textEdit_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_3 = QLabel(IntroStepYASA)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_3)

        self.textEdit_3 = QTextEdit(IntroStepYASA)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit_3.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_3.setLineWidth(0)
        self.textEdit_3.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.textEdit_3.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit_3)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(715, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.retranslateUi(IntroStepYASA)

        QMetaObject.connectSlotsByName(IntroStepYASA)
    # setupUi

    def retranslateUi(self, IntroStepYASA):
        IntroStepYASA.setWindowTitle(QCoreApplication.translate("IntroStepYASA", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("IntroStepYASA", u"<html><head/><body><p><span style=\" font-family:'Roboto'; font-size:12pt; font-weight:700;\">YASA RAPID EYE MOVEMENTS DETECTOR</span></p><p><span style=\" font-family:'Roboto'; font-size:12pt;\">This tool utilizes the </span><span style=\" font-family:'Roboto'; font-size:12pt; font-weight:700;\">YASA</span><span style=\" font-family:'Roboto'; font-size:12pt;\"> rapid eye movements (</span><span style=\" font-family:'Roboto'; font-size:12pt; font-weight:700;\">REMs</span><span style=\" font-family:'Roboto'; font-size:12pt;\">) detector algorithm. </span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("IntroStepYASA", u"<html><head/><body><p><span style=\" font-family:'Roboto'; font-size:12pt; font-weight:600;\">Input</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("IntroStepYASA", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto-Regular'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; font-size:12pt;\">PSG files including header and events are needed (all saved in the same directory).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0"
                        "px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; font-size:12pt;\">-&gt; European Data Format (EDF) : .edf and .tsv files with the exact same filename.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; font-size:12pt;\">-&gt; Stellate : .sig and .sts files with the exact same filename.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; font-size:12pt;\">-&gt; NATUS :  the whole NATUS subject folder</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; font-size:12pt;\">The annotations files have to include the sleep staging.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom"
                        ":0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; font-size:12pt;\">Channels:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; font-size:12pt;\">This tool requires the selection of </span><span style=\" font-family:'Roboto'; font-size:12pt; font-weight:600;\">2</span><span style=\" font-family:'Roboto'; font-size:12pt;\"> </span><span style=\" font-family:'Roboto'; font-size:12pt; font-weight:600;\">EOG</span><span style=\" font-family:'Roboto'; font-size:12pt;\"> </span><span style=\" font-family:'Roboto'; font-size:12pt; font-weight:600;\">channels</span><span style=\" font-family:'Roboto'; font-size:12pt;\"> per recording for REMs detection.</span><"
                        "/p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Roboto'; font-size:12pt;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("IntroStepYASA", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Output</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("IntroStepYASA", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto-Regular'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">The REMs detected events are added in the annotations files (.tsv, .sts or .ent) depending of the format used.<br /></span><span style=\" font-size:12pt;\">If the annotations file already includes the group event to be added, the existing entries will be removed before adding the new ones.</span></p>\n"
"<p style=\" margin-top:0px"
                        "; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt;\">Each events is defined by : </span><span style=\" font-size:12pt;\"><br />-&gt; 1. group : The group where the events are added (i.e. REM).<br />-&gt; 2. name : The name of the event (i.e. YASA_REM)<br />-&gt; 3. start_sec : The onset of the event in second. <br />-&gt; 4. duration_sec : The duration of the event in second.<br />-&gt; 5. channels : The list of channels on which the event occurs.</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("IntroStepYASA", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">References</span></p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("IntroStepYASA", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto-Regular'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto';\">  </span><span style=\" font-family:'Roboto'; font-size:12pt;\">[1] Yetton, B. D., et al. (2016). Automatic detection of rapid eye movements (REMs): A machine learning approach. </span><span style=\" font-family:'Roboto';\">  </span><span style=\" font-family:'Roboto'; font-size:12pt; font-style:italic;\">Journal of neuroscience methods</span><span style=\""
                        " font-family:'Roboto';\">  </span><span style=\" font-family:'Roboto'; font-size:12pt;\">, </span><span style=\" font-family:'Roboto';\">  </span><span style=\" font-family:'Roboto'; font-size:12pt; font-style:italic;\">259</span><span style=\" font-family:'Roboto';\">  </span><span style=\" font-family:'Roboto'; font-size:12pt;\">, 72-82.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto';\">  </span><span style=\" font-family:'Roboto'; font-size:12pt;\">[2] Agarwal, R., et al. (2005). Detection of rapid-eye movements in sleep studies. </span><span style=\" font-family:'Roboto';\">  </span><span style=\" font-family:'Roboto'; font-size:12pt; font-style:italic;\">IEEE Transactions on biomedical engineering</span><span style=\" font-family:'Roboto';\">  </span><span style=\" font-family:'Roboto'; font-size:12pt;\">, </span><span style=\" font-family:'Roboto';\">  </span><span style=\" font-"
                        "family:'Roboto'; font-size:12pt; font-style:italic;\">52</span><span style=\" font-family:'Roboto';\">  </span><span style=\" font-family:'Roboto'; font-size:12pt;\">(8), 1390-1396.</span></p></body></html>", None))
    # retranslateUi


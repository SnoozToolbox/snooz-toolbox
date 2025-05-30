# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QTabWidget, QVBoxLayout,
    QWidget)
import themes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(819, 702)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"font: 12pt \"Roboto\";")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionLoad_package = QAction(MainWindow)
        self.actionLoad_package.setObjectName(u"actionLoad_package")
        self.actionUnload_package = QAction(MainWindow)
        self.actionUnload_package.setObjectName(u"actionUnload_package")
        self.actionNew_process = QAction(MainWindow)
        self.actionNew_process.setObjectName(u"actionNew_process")
        self.actionOpen_process = QAction(MainWindow)
        self.actionOpen_process.setObjectName(u"actionOpen_process")
        self.actionSave_process = QAction(MainWindow)
        self.actionSave_process.setObjectName(u"actionSave_process")
        self.actionSave_process_as = QAction(MainWindow)
        self.actionSave_process_as.setObjectName(u"actionSave_process_as")
        self.actionClose_process = QAction(MainWindow)
        self.actionClose_process.setObjectName(u"actionClose_process")
        self.actionLoad_workspace = QAction(MainWindow)
        self.actionLoad_workspace.setObjectName(u"actionLoad_workspace")
        self.actionConvert_from_beta_to_v1_0_0 = QAction(MainWindow)
        self.actionConvert_from_beta_to_v1_0_0.setObjectName(u"actionConvert_from_beta_to_v1_0_0")
        self.actionRun = QAction(MainWindow)
        self.actionRun.setObjectName(u"actionRun")
        self.actionLogs = QAction(MainWindow)
        self.actionLogs.setObjectName(u"actionLogs")
        self.actionAbout_Snooz = QAction(MainWindow)
        self.actionAbout_Snooz.setObjectName(u"actionAbout_Snooz")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionData_Files = QAction(MainWindow)
        self.actionData_Files.setObjectName(u"actionData_Files")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_pushButton = QPushButton(self.centralwidget)
        self.home_pushButton.setObjectName(u"home_pushButton")
        self.home_pushButton.setStyleSheet(u"text-align: left;")

        self.verticalLayout.addWidget(self.home_pushButton)

        self.tool_pushButton = QPushButton(self.centralwidget)
        self.tool_pushButton.setObjectName(u"tool_pushButton")
        self.tool_pushButton.setStyleSheet(u"text-align: left;")

        self.verticalLayout.addWidget(self.tool_pushButton)

        self.tool_root_nav_frame = QFrame(self.centralwidget)
        self.tool_root_nav_frame.setObjectName(u"tool_root_nav_frame")
        self.tool_buttons_root_layout = QVBoxLayout(self.tool_root_nav_frame)
        self.tool_buttons_root_layout.setSpacing(0)
        self.tool_buttons_root_layout.setObjectName(u"tool_buttons_root_layout")
        self.tool_buttons_root_layout.setContentsMargins(11, 0, 0, 0)

        self.verticalLayout.addWidget(self.tool_root_nav_frame)

        self.process_pushButton = QPushButton(self.centralwidget)
        self.process_pushButton.setObjectName(u"process_pushButton")
        self.process_pushButton.setStyleSheet(u"text-align: left;")

        self.verticalLayout.addWidget(self.process_pushButton)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.app_pushButton = QPushButton(self.centralwidget)
        self.app_pushButton.setObjectName(u"app_pushButton")
        self.app_pushButton.setStyleSheet(u"text-align: left;")

        self.horizontalLayout_3.addWidget(self.app_pushButton)

        self.close_app_pushButton = QPushButton(self.centralwidget)
        self.close_app_pushButton.setObjectName(u"close_app_pushButton")
        self.close_app_pushButton.setMinimumSize(QSize(32, 32))
        self.close_app_pushButton.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.close_app_pushButton)

        self.horizontalLayout_3.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.process_root_nav_frame = QFrame(self.centralwidget)
        self.process_root_nav_frame.setObjectName(u"process_root_nav_frame")
        self.process_buttons_root_layout = QVBoxLayout(self.process_root_nav_frame)
        self.process_buttons_root_layout.setSpacing(0)
        self.process_buttons_root_layout.setObjectName(u"process_buttons_root_layout")
        self.process_buttons_root_layout.setContentsMargins(11, 0, 0, 0)

        self.verticalLayout.addWidget(self.process_root_nav_frame)

        self.app_root_nav_frame = QFrame(self.centralwidget)
        self.app_root_nav_frame.setObjectName(u"app_root_nav_frame")
        self.app_buttons_root_layout = QVBoxLayout(self.app_root_nav_frame)
        self.app_buttons_root_layout.setSpacing(0)
        self.app_buttons_root_layout.setObjectName(u"app_buttons_root_layout")
        self.app_buttons_root_layout.setContentsMargins(11, 0, 0, 0)
        self.app_buttons_layout = QVBoxLayout()
        self.app_buttons_layout.setObjectName(u"app_buttons_layout")

        self.app_buttons_root_layout.addLayout(self.app_buttons_layout)

        self.line = QFrame(self.app_root_nav_frame)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.app_buttons_root_layout.addWidget(self.line)


        self.verticalLayout.addWidget(self.app_root_nav_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.content_tabWidget = QTabWidget(self.centralwidget)
        self.content_tabWidget.setObjectName(u"content_tabWidget")
        self.content_tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.content_tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.content_tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.content_tabWidget.setDocumentMode(False)
        self.content_tabWidget.setTabBarAutoHide(True)
        self.home_tab = QWidget()
        self.home_tab.setObjectName(u"home_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.home_tab)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.home_tab)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setChildrenCollapsible(False)
        self.left_pane = QWidget(self.splitter)
        self.left_pane.setObjectName(u"left_pane")
        self.verticalLayout_6 = QVBoxLayout(self.left_pane)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.left_pane_layout = QVBoxLayout()
        self.left_pane_layout.setObjectName(u"left_pane_layout")

        self.verticalLayout_6.addLayout(self.left_pane_layout)

        self.splitter.addWidget(self.left_pane)
        self.right_pane = QWidget(self.splitter)
        self.right_pane.setObjectName(u"right_pane")
        self.verticalLayout_8 = QVBoxLayout(self.right_pane)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.right_pane_layout = QVBoxLayout()
        self.right_pane_layout.setObjectName(u"right_pane_layout")

        self.verticalLayout_8.addLayout(self.right_pane_layout)

        self.splitter.addWidget(self.right_pane)

        self.horizontalLayout_2.addWidget(self.splitter)

        self.horizontalLayout_2.setStretch(0, 1)
        self.content_tabWidget.addTab(self.home_tab, "")
        self.tool_tab = QWidget()
        self.tool_tab.setObjectName(u"tool_tab")
        self.verticalLayout_5 = QVBoxLayout(self.tool_tab)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tool_layout = QVBoxLayout()
        self.tool_layout.setSpacing(0)
        self.tool_layout.setObjectName(u"tool_layout")

        self.verticalLayout_5.addLayout(self.tool_layout)

        self.content_tabWidget.addTab(self.tool_tab, "")
        self.app_tab = QWidget()
        self.app_tab.setObjectName(u"app_tab")
        self.verticalLayout_4 = QVBoxLayout(self.app_tab)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.app_layout = QVBoxLayout()
        self.app_layout.setSpacing(0)
        self.app_layout.setObjectName(u"app_layout")

        self.verticalLayout_4.addLayout(self.app_layout)

        self.content_tabWidget.addTab(self.app_tab, "")
        self.process_tab = QWidget()
        self.process_tab.setObjectName(u"process_tab")
        self.verticalLayout_3 = QVBoxLayout(self.process_tab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.process_layout = QVBoxLayout()
        self.process_layout.setSpacing(0)
        self.process_layout.setObjectName(u"process_layout")

        self.verticalLayout_3.addLayout(self.process_layout)

        self.content_tabWidget.addTab(self.process_tab, "")

        self.horizontalLayout.addWidget(self.content_tabWidget)

        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 819, 33))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuDev_Tools = QMenu(self.menuBar)
        self.menuDev_Tools.setObjectName(u"menuDev_Tools")
        self.menuConvert_tool_file = QMenu(self.menuDev_Tools)
        self.menuConvert_tool_file.setObjectName(u"menuConvert_tool_file")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuDev_Tools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionLoad_workspace)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuDev_Tools.addAction(self.actionNew_process)
        self.menuDev_Tools.addAction(self.actionOpen_process)
        self.menuDev_Tools.addAction(self.actionSave_process)
        self.menuDev_Tools.addAction(self.actionSave_process_as)
        self.menuDev_Tools.addAction(self.actionClose_process)
        self.menuDev_Tools.addAction(self.menuConvert_tool_file.menuAction())
        self.menuDev_Tools.addSeparator()
        self.menuDev_Tools.addAction(self.actionRun)
        self.menuConvert_tool_file.addAction(self.actionConvert_from_beta_to_v1_0_0)
        self.menuHelp.addAction(self.actionLogs)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionData_Files)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Snooz)

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.actionNew_process.triggered.connect(MainWindow.new_process_clicked)
        self.actionOpen_process.triggered.connect(MainWindow.open_process_clicked)
        self.actionSave_process.triggered.connect(MainWindow.save_process_clicked)
        self.actionSave_process_as.triggered.connect(MainWindow.save_process_as_clicked)
        self.actionClose_process.triggered.connect(MainWindow.close_process_clicked)
        self.actionLoad_workspace.triggered.connect(MainWindow.load_workspace_clicked)
        self.actionConvert_from_beta_to_v1_0_0.triggered.connect(MainWindow.convert_file_clicked)
        self.actionRun.triggered.connect(MainWindow.run_clicked)
        self.actionLogs.triggered.connect(MainWindow.logs_clicked)
        self.actionAbout_Snooz.triggered.connect(MainWindow.about_clicked)
        self.actionPreferences.triggered.connect(MainWindow.preferences_clicked)
        self.home_pushButton.clicked.connect(MainWindow.home_clicked)
        self.process_pushButton.clicked.connect(MainWindow.process_clicked)
        self.tool_pushButton.clicked.connect(MainWindow.tool_clicked)
        self.app_pushButton.clicked.connect(MainWindow.app_clicked)
        self.actionOpen_File.triggered.connect(MainWindow.open_clicked)
        self.close_app_pushButton.clicked.connect(MainWindow.close_app_clicked)
        self.actionDocumentation.triggered.connect(MainWindow.documentation_clicked)
        self.actionData_Files.triggered.connect(MainWindow.data_clicked)

        self.content_tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Snooz", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionLoad_package.setText(QCoreApplication.translate("MainWindow", u"Load package", None))
#if QT_CONFIG(shortcut)
        self.actionLoad_package.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionUnload_package.setText(QCoreApplication.translate("MainWindow", u"Unload all packages", None))
        self.actionNew_process.setText(QCoreApplication.translate("MainWindow", u"New process", None))
        self.actionOpen_process.setText(QCoreApplication.translate("MainWindow", u"Open process", None))
        self.actionSave_process.setText(QCoreApplication.translate("MainWindow", u"Save process", None))
        self.actionSave_process_as.setText(QCoreApplication.translate("MainWindow", u"Save process as...", None))
        self.actionClose_process.setText(QCoreApplication.translate("MainWindow", u"Close process", None))
        self.actionLoad_workspace.setText(QCoreApplication.translate("MainWindow", u"Load workspace", None))
#if QT_CONFIG(shortcut)
        self.actionLoad_workspace.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionConvert_from_beta_to_v1_0_0.setText(QCoreApplication.translate("MainWindow", u"Convert from beta to v1.0.0", None))
        self.actionRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
#if QT_CONFIG(shortcut)
        self.actionRun.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionLogs.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.actionAbout_Snooz.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen_File.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionData_Files.setText(QCoreApplication.translate("MainWindow", u"Data Files", None))
#if QT_CONFIG(accessibility)
        self.home_pushButton.setAccessibleName(QCoreApplication.translate("MainWindow", u"home_button", None))
#endif // QT_CONFIG(accessibility)
        self.home_pushButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(accessibility)
        self.tool_pushButton.setAccessibleName(QCoreApplication.translate("MainWindow", u"task_button", None))
#endif // QT_CONFIG(accessibility)
        self.tool_pushButton.setText(QCoreApplication.translate("MainWindow", u"Tool", None))
#if QT_CONFIG(accessibility)
        self.process_pushButton.setAccessibleName(QCoreApplication.translate("MainWindow", u"schema_button", None))
#endif // QT_CONFIG(accessibility)
        self.process_pushButton.setText(QCoreApplication.translate("MainWindow", u"Process", None))
#if QT_CONFIG(accessibility)
        self.app_pushButton.setAccessibleName(QCoreApplication.translate("MainWindow", u"app_button", None))
#endif // QT_CONFIG(accessibility)
        self.app_pushButton.setText(QCoreApplication.translate("MainWindow", u"App", None))
        self.close_app_pushButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.content_tabWidget.setTabText(self.content_tabWidget.indexOf(self.home_tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.content_tabWidget.setTabText(self.content_tabWidget.indexOf(self.tool_tab), QCoreApplication.translate("MainWindow", u"Tool", None))
        self.content_tabWidget.setTabText(self.content_tabWidget.indexOf(self.app_tab), QCoreApplication.translate("MainWindow", u"App", None))
        self.content_tabWidget.setTabText(self.content_tabWidget.indexOf(self.process_tab), QCoreApplication.translate("MainWindow", u"Process", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuDev_Tools.setTitle(QCoreApplication.translate("MainWindow", u"Dev Tools", None))
        self.menuConvert_tool_file.setTitle(QCoreApplication.translate("MainWindow", u"Convert tool file", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


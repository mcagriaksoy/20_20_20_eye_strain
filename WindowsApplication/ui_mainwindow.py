# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(507, 228)
        MainWindow.setMinimumSize(QSize(507, 228))
        MainWindow.setMaximumSize(QSize(507, 228))
        font = QFont()
        font.setFamilies([u"Arial"])
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u"img/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.990000000000000)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        MainWindow.setIconSize(QSize(30, 30))
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 521, 241))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayoutWidget = QWidget(self.tab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(280, 150, 211, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.timer_label = QLabel(self.horizontalLayoutWidget)
        self.timer_label.setObjectName(u"timer_label")

        self.horizontalLayout.addWidget(self.timer_label)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(350, 10, 151, 121))
        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 20, 159, 89))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.night_mode = QCheckBox(self.verticalLayoutWidget_2)
        self.night_mode.setObjectName(u"night_mode")

        self.verticalLayout_2.addWidget(self.night_mode)

        self.visual_button = QCheckBox(self.verticalLayoutWidget_2)
        self.visual_button.setObjectName(u"visual_button")
        self.visual_button.setChecked(True)

        self.verticalLayout_2.addWidget(self.visual_button)

        self.sound_button = QCheckBox(self.verticalLayoutWidget_2)
        self.sound_button.setObjectName(u"sound_button")

        self.verticalLayout_2.addWidget(self.sound_button)

        self.horizontalLayoutWidget_2 = QWidget(self.tab)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 150, 257, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stop_button = QPushButton(self.horizontalLayoutWidget_2)
        self.stop_button.setObjectName(u"stop_button")

        self.horizontalLayout_2.addWidget(self.stop_button)

        self.reset_button = QPushButton(self.horizontalLayoutWidget_2)
        self.reset_button.setObjectName(u"reset_button")

        self.horizontalLayout_2.addWidget(self.reset_button)

        self.start_button = QPushButton(self.horizontalLayoutWidget_2)
        self.start_button.setObjectName(u"start_button")

        self.horizontalLayout_2.addWidget(self.start_button)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 5, 331, 141))
        self.label_3.setPixmap(QPixmap(u"img/rule.jpg"))
        self.label_3.setScaledContents(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.textBrowser_2 = QTextBrowser(self.tab_3)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(10, 40, 481, 101))
        self.textBrowser_2.setAutoFillBackground(True)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 160, 481, 20))
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 80, 391, 16))
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 100, 91, 16))
        self.label_5.setTextFormat(Qt.RichText)
        self.label_5.setOpenExternalLinks(True)
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 120, 361, 20))
        self.label_6.setTextFormat(Qt.RichText)
        self.label_6.setOpenExternalLinks(True)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"20 20 20 Reduce Eye Strain ", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"A useful application to apply 20 20 20 method for reduce your eye strain!", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(QCoreApplication.translate("MainWindow", u"A useful application to apply 20 20 20 method for reduce your eye strain!", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Remaining Time:", None))
        self.timer_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.night_mode.setText(QCoreApplication.translate("MainWindow", u"Night Mode \ud83c\udf13", None))
        self.visual_button.setText(QCoreApplication.translate("MainWindow", u"Visual Notification \ud83d\udc41", None))
        self.sound_button.setText(QCoreApplication.translate("MainWindow", u"Sound Notification \ud83d\udd0a", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"Stop Timer", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"Reset Timer", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start Timer", None))
        self.label_3.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"...", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Arial'; font-size:9pt;\">The 20-20-20 rule is a simple practice designed to reduce eye strain and prevent digital eye fatigue, also known as computer vision syndrome. Here\u2019s how it works: For every 20 minutes you spend looking at a screen, take a break and look at something 20 feet away for at least 20 seconds. This helps relax your eye muscles and gives your brain a much-needed respite. \ud83c\udf1f</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"What is 20 20 20 rule?", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"If you experience any eye discomfort or headaches, please consult a doctor immediately.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"20 20 20 Reduce Eye Strain - designed and written by mcagriaksoy 2024. ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://www.github.com/mcagriaksoy\"><span style=\" text-decoration: underline; color:#0000ff;\">Github </span></a><a href=\"https://www.linkedin.com/in/mcagriaksoy\"><span style=\" text-decoration: underline; color:#0000ff;\">LinkedIn</span></a></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>v1.0 - If you experience any bug, feel free to report it at <a href=\"https://github.com/mcagriaksoy/20_20_20_eye_strain\"><span style=\" text-decoration: underline; color:#0000ff;\">here.</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


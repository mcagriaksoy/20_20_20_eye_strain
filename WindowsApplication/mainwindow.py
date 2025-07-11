# A useful application to apply 20 20 20 method for reduce your eye strain!
# Author: Mehmet Cagri Aksoy - 2024-2025
# Version: 1.1

from PySide6 import QtUiTools
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication, QSystemTrayIcon, QMenu
from PySide6.QtCore import QTimer, QTime, Qt, QEvent
from PySide6.QtGui import QPixmap, QIcon, QCloseEvent
import platform

if platform.system() == "Windows":
    import winsound, winreg
elif platform.system() == "Darwin" or platform.system() == "Linux":
    import os

def is_windows_dark_mode(self):
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        registry_key = winreg.OpenKey(registry, r'Software\Microsoft\Windows\CurrentVersion\Themes\Personalize')
        value, _ = winreg.QueryValueEx(registry_key, 'AppsUseLightTheme')
        return value == 0  # 0 means dark mode is enabled
    except WindowsError:
        return False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file = QtUiTools.QUiLoader().load("mainWindow.ui")
        self.setCentralWidget(ui_file)
        self.stop_button = ui_file.stop_button
        self.night_mode = ui_file.night_mode
        self.start_button = ui_file.start_button
        self.reset_button = ui_file.reset_button
        self.timer_label = ui_file.timer_label
        self.label_2 = ui_file.label_2
        self.label_3 = ui_file.label_3
        self.visual_button = ui_file.visual_button
        self.sound_button = ui_file.sound_button

        self.setWindowTitle("20 20 20 Eye Strain Relief")
        if is_windows_dark_mode(self):
            # Toggle night mode on startup if Windows is in dark mode
            self.night_mode.setChecked(True)
            self.mode()
        self.show()
        self.stop_button.setEnabled(False)
        self.night_mode.toggled.connect(self.mode)
        self.start_button.clicked.connect(self.start_timer)
        self.stop_button.clicked.connect(self.stop_timer)
        self.reset_button.clicked.connect(self.reset_timer)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.remaining_time = QTime(0, 20, 0)  # 20 minutes

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("./img/eye.png"))
        tray_menu = QMenu()
        show_action = tray_menu.addAction("Show")
        exit_action = tray_menu.addAction("Exit")
        show_action.triggered.connect(self.show_window)
        exit_action.triggered.connect(QApplication.instance().quit)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.activated.connect(self.on_tray_icon_activated)
        self.tray_icon.show()
    
    def mode(self):
        if self.night_mode.isChecked():
            self.setStyleSheet("background-color: #333; color: white")
            self.timer_label.setStyleSheet("color: white")
            # Set pixmap at label_3 with transparency support
            pixmap = QPixmap("./img/rule-inverted.jpg")
            pixmap.setDevicePixelRatio(self.devicePixelRatio())
            self.label_3.setPixmap(pixmap)
            self.label_3.setAttribute(Qt.WA_TranslucentBackground)
            #Change button colors
            self.start_button.setStyleSheet("background-color: #888; color: white")
            self.stop_button.setStyleSheet("background-color: #888; color: white")
            self.reset_button.setStyleSheet("background-color: #888; color: white")

            # Change label_2 text color
            self.label_2.setStyleSheet("color: white")

            # Change timer text color
            self.timer_label.setStyleSheet("color: white")

            self.night_mode.setStyleSheet("color: white")
            self.visual_button.setStyleSheet("color: white")
            self.sound_button.setStyleSheet("color: white")

            # Change the windows ui frame color
        else:
            self.setStyleSheet("background-color: white; color: black")
            self.timer_label.setStyleSheet("color: black")
            # Set pixmap at label_3 with transparency support
            pixmap = QPixmap("./img/rule.jpg")
            pixmap.setDevicePixelRatio(self.devicePixelRatio())
            self.label_3.setPixmap(pixmap)
            self.label_3.setAttribute(Qt.WA_TranslucentBackground)
            #Change button colors
            self.start_button.setStyleSheet("background-color: white; color: black")
            self.stop_button.setStyleSheet("background-color: white; color: black")
            self.reset_button.setStyleSheet("background-color: white; color: black")

            # Change label_2 text color
            self.label_2.setStyleSheet("color: black")

            # Change timer text color
            self.timer_label.setStyleSheet("color: black")

            self.night_mode.setStyleSheet("color: black")
            self.visual_button.setStyleSheet("color: black")
            self.sound_button.setStyleSheet("color: black")
    

    def start_timer(self):
        self.stop_button.setEnabled(True)
        self.start_button.setEnabled(False)
        self.timer.start(1000)  # start timer, 1 tick per second
    
    def update_timer(self):
        self.remaining_time = self.remaining_time.addSecs(-1)
        self.timer_label.setText(self.remaining_time.toString())

        if self.remaining_time == QTime(0, 0, 0):
            self.timer.stop()
            self.timer_label.setText("Time's up! Rest :)")
            if self.sound_button.isChecked():
                self.play_sound()
            if self.visual_button.isChecked():
                self.show_popup()
    
    def play_sound(self):
        if platform.system() == "Windows":
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        elif platform.system() == "Darwin" or platform.system() == "Linux":
            os.system('play -n synth 0.1 sine 660')
    
    def show_popup(self):
        # Get the screen resolution
        screen = QApplication.screens()[0]
        screen_resolution = screen.geometry()
        screen_width, screen_height = screen_resolution.width() - 10, screen_resolution.height() - 100

        msg = QMessageBox()
        # Make borderless
        msg.setWindowFlag(Qt.FramelessWindowHint)
        # Make the message box stay on top
        msg.setWindowFlag(Qt.WindowStaysOnTopHint)

        msg.setText("Hey there! Time for a break!\r\nTime's UP! Please focus on something 20 feet / 6 meters away for 20 seconds.")
        
        # Set an image to the popup
        msg.setIconPixmap(QPixmap("./img/eye.png"))

        # Get the message box size
        msg_box_size = msg.sizeHint()

        # Calculate the position for the message box to be at the bottom right
        position_x = screen_width - msg_box_size.width()
        position_y = screen_height - msg_box_size.height()

        # Move the message box to the calculated position
        msg.move(position_x, position_y)

        # Create a QTimer
        timer = QTimer()
        timer.setSingleShot(True)  # Set the timer to single shot
        timer.timeout.connect(msg.close)  # Connect the timeout signal to the close slot of the message box
        timer.start(20000)  # Start the timer (20000 milliseconds = 20 seconds)
        # Connect the finished signal of the message box to the reset_timer method
        msg.finished.connect(self.reset_timer)
        msg.exec()
        
    def reset_timer(self):
        self.start_button.setEnabled(True)
        self.remaining_time = QTime(0, 20, 0)
        self.timer_label.setText(self.remaining_time.toString())
        self.start_timer()

    def stop_timer(self):
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.timer.stop()

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.isMinimized():
                QTimer.singleShot(0, self.hide)
                self.tray_icon.showMessage(
                    "20 20 20 Eye Strain Relief",
                    "App is running in the background.",
                    QSystemTrayIcon.Information,
                    2000
                )
        super().changeEvent(event)

    def show_window(self):
        self.showNormal()
        self.activateWindow()

    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.show_window()

    def closeEvent(self, event: QCloseEvent):
        self.tray_icon.hide()
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    #main_window.show()
    app.exec()

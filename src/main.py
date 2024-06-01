# A useful application to apply 20 20 20 method for reduce your eye strain!
# Author: Mehmet Cagri Aksoy - 2024
# Version: 1.0

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt6.QtCore import QTimer, QTime, Qt
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.show()
        self.night_mode.toggled.connect(self.mode)
        self.start_button.clicked.connect(self.start_timer)
        self.stop_button.clicked.connect(self.stop_timer)
        self.reset_button.clicked.connect(self.reset_timer)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.remaining_time = QTime(0, 0, 1)  # 20 minutes

    def mode(self):
        if self.night_mode.isChecked():
            self.setStyleSheet("background-color: black; color: white")
        else:
            self.setStyleSheet("background-color: white; color: black") # todo fix this
    
    def start_timer(self):
        self.timer.start(1000)  # start timer, 1 tick per second
    
    def update_timer(self):
        self.remaining_time = self.remaining_time.addSecs(-1)
        self.timer_label.setText(self.remaining_time.toString())

        if self.remaining_time == QTime(0, 0, 0):
            self.timer.stop()
            self.timer_label.setText("Time's up! Rest :)")

            if self.visual_button.isChecked():
                self.show_popup()
            
            #if self.sound_button.isChecked():
                #self.play_sound() # todo fix this
    
    def show_popup(self):
        # Get the screen resolution
        screen = QApplication.screens()[0]
        screen_resolution = screen.geometry()
        screen_width, screen_height = screen_resolution.width() - 10, screen_resolution.height() - 100

        msg = QMessageBox()
        # Make borderless
        msg.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        # Make the message box stay on top
        msg.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)

        msg.setText("Hey there! Time for a break!\r\nTime's UP! Please focus on something 20 feet / 6 meters away for 20 seconds.")
        
        # Set an image to the popup
        msg.setIconPixmap(QPixmap("./img/eye.png"))

        #msg.setIcon(QMessageBox.Icon.Information)

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
        self.remaining_time = QTime(0, 20, 0)
        self.timer_label.setText(self.remaining_time.toString())
        self.start_timer()

    def stop_timer(self):
        self.timer.stop()

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    #main_window.show()
    app.exec()
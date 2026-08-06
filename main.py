import sys, time
from PySide6.QtWidgets import QApplication, QFontDialog, QFontComboBox, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
from os import getlogin

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.time_left = 0
        self.setWindowTitle('Focus timer')
        self.setFixedSize(600, 400)
        self.welcome = QLabel(f'WELCOME {getlogin()}!')
        self.timeinfo = QLabel('Choose the required time below!')
        self.clock = QLabel('00:00:00')
        self.clock.setFont(QFont('Arial', 40))
        self.welcome.setFont(QFont('Arial', 20))
        self.timeinfo.setFont(QFont('Arial', 20))
        self.btn30 = QPushButton('30 min')
        self.btn1 = QPushButton('1 hour')
        self.btn2 = QPushButton('2 hours')
        self.surrbtn = QPushButton('Surrender')
        self.surrbtn.setObjectName("surrbtn")

        self.qtimer = QTimer()
        self.qtimer.timeout.connect(self.update_timer)
        self.btn30.setFixedSize(150, 50)
        self.btn1.setFixedSize(150, 50)
        self.btn2.setFixedSize(150, 50)
        self.surrbtn.setFixedSize(250, 50)
        self.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            }

            QPushButton:hover {
                background-color: #45a049;
            }

            QPushButton:pressed {
                background-color: #357a38;
            }

            QPushButton#surrbtn {
            background-color: red;
            color: white;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
            }
            """)

        self.btn30.clicked.connect(lambda: self.timer(30))
        self.btn1.clicked.connect(lambda: self.timer(60))
        self.btn2.clicked.connect(lambda: self.timer(120))
        self.surrbtn.clicked.connect(self.surrender_button)

        layoutV = QVBoxLayout()
        layoutH = QHBoxLayout()

        layoutV.addWidget(self.welcome, alignment=Qt.AlignCenter)
        layoutV.addWidget(self.timeinfo, alignment=Qt.AlignCenter)
        layoutV.addWidget(self.clock, alignment=Qt.AlignCenter)
        
        layoutH.addWidget(self.btn30)
        layoutH.addWidget(self.btn1)
        layoutH.addWidget(self.btn2)
        layoutH.addWidget(self.surrbtn)
        self.surrbtn.setEnabled(False)
        self.surrbtn.hide()
        layoutV.addWidget(self.clock, alignment=Qt.AlignCenter)
        layoutH.setAlignment(Qt.AlignCenter)
        layoutV.addStretch()
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)
        

    def timer(self, minutes):
        
        self.time_left = minutes*60 
        self.qtimer.start(1000)
        self.btn30.setEnabled(False)
        self.btn1.setEnabled(False)
        self.btn2.setEnabled(False)
        self.surrbtn.setEnabled(True)
        self.btn30.hide()
        self.btn1.hide()
        self.btn2.hide()

        self.surrbtn.show()

    
    def update_timer(self):
        self.time_left-=1
        hours = self.time_left // 3600
        minutes = (self.time_left % 3600) // 60
        seconds = self.time_left % 60
        if self.time_left <= 0:
            self.qtimer.stop()
            self.time_left = 0
            self.btn30.setEnabled(True)
            self.btn1.setEnabled(True)
            self.btn2.setEnabled(True)
            self.btn30.show()
            self.btn1.show()
            self.btn2.show()
            self.surrbtn.hide()
            self.surrbtn.setEnabled(False)

    
        self.clock.setText(f"{hours:02}:{minutes:02}:{seconds:02}")
        
    def surrender_button(self):
        self.qtimer.stop()
        self.clock.setText('00:00:00')
        self.time_left = 0
        self.btn30.setEnabled(True)
        self.btn1.setEnabled(True)
        self.btn2.setEnabled(True)
        self.btn30.show()
        self.btn1.show()
        self.btn2.show()
        self.surrbtn.setEnabled(False)
        self.surrbtn.hide()

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
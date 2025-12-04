from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QPushButton

class ControlPanel(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Alarm System Control Panel")

        button = QPushButton("Press Me!")

        self.setFixedSize(QSize(960, 540))

        # Set the central widget of the Window.
        # self.setCentralWidget(button)


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class HelloWorldWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setGeometry(200, 200, 400, 200)

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 300, 50)
        self.label.setText("Welcome to the Captivating Hello World Program!")
        self.label.setStyleSheet("font-size: 20px; color: #333; text-align: center;")

        self.button = QPushButton(self)
        self.button.setGeometry(150, 120, 100, 50)
        self.button.setText("Click Me!")
        self.button.setStyleSheet("font-size: 16px; background-color: #FF4081; color: white;")
        self.button.clicked.connect(self.display_message)

    def display_message(self):
        self.label.setText("Hello, World! You've been captivated!")
        self.label.setStyleSheet("font-size: 24px; color: #03A9F4; text-align: center;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelloWorldWindow()
    window.show()
    sys.exit(app.exec())

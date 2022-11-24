from client.mainwindow import MainWindow
import sys
from PyQt6.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = MainWindow()
    app.exec()
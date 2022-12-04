from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtCore import Qt
from client.loginwindow import LoginWindow
from client.registerwindow import RegisterWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__initUi()
        self.__settingUi()
        self.show()

    def __initUi(self) -> None:
        self.central_widget = QWidget()
        self.main_v_layout = QVBoxLayout()

    def __settingUi(self) -> None:
        self.resize(930, 615)
        self.setWindowTitle('Touragency Client')

        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_v_layout)

    def show_message(self, text: str, error: bool = False, parent=None) -> None:
        messagebox = QMessageBox(self if not parent else parent)
        messagebox.setStandardButtons(QMessageBox.StandardButton.Ok)
        messagebox.setWindowTitle("Error" if error else "Information")
        messagebox.setText(text)
        messagebox.setIcon(QMessageBox.Icon.Critical if error else QMessageBox.Icon.Information)
        messagebox.show()

    def exit(self) -> None:
        self.close()

    class PageList(QWidget):
        def __init__(self):
            super().__init__()

    class AuthorizationWidget(QWidget):
        def __init__(self):
            super().__init__()
            self.__initUi()
            self.__settingUi()

        def __initUi(self):
            self.main_layout = QVBoxLayout()

            self.button_container = QWidget(self)

            self.login_button = QPushButton()
            self.register_button = QPushButton()

        def __settingUi(self):
            self.setLayout(self.main_layout)

            # Set texts for elements
            self.login_button.setText('Login')
            self.register_button.setText('Register')

            # Appending widgets
            self.main_layout.addWidget(self.login_button)
            self.main_layout.addWidget(self.register_button)

            # Buttons connect
            self.login_button.clicked.connect(self.on_press_login)
            self.register_button.clicked.connect(self.on_press_register)

        def on_press_login(self):
            LoginWindow(self.parent())

        def on_press_register(self):
            RegisterWindow(self.parent())

    

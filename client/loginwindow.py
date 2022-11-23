from PyQt6.QtWidgets import QDialog, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QErrorMessage, QMessageBox
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt
import api.resolvers


class LoginWindow(QDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent=parent)
        self.__initUi()
        self.__settingUi()
        self.show()

    def __initUi(self) -> None:
        self.setWindowTitle('Login')
        self.setFixedSize(200, 100)

        self.main_v_layout = QVBoxLayout()
        self.label_lineedit_h_layout = QHBoxLayout()
        self.label_v_layout = QVBoxLayout()
        self.line_edit_v_layout = QVBoxLayout()

        self.label_login = QLabel()
        self.label_password = QLabel()

        self.line_edit_login = QLineEdit()
        self.line_edit_password = QLineEdit()

        self.login_button = QPushButton()

    def __settingUi(self) -> None:
        self.setLayout(self.main_v_layout)
        self.main_v_layout.addLayout(self.label_lineedit_h_layout)
        self.label_lineedit_h_layout.addLayout(self.label_v_layout)
        self.label_lineedit_h_layout.addLayout(self.line_edit_v_layout)

        self.label_v_layout.addWidget(self.label_login)
        self.label_v_layout.addWidget(self.label_password)

        self.line_edit_v_layout.addWidget(self.line_edit_login)
        self.line_edit_v_layout.addWidget(self.line_edit_password)

        self.main_v_layout.addWidget(self.login_button)

        self.label_login.setText('Login')
        self.label_password.setText('Password')
        self.login_button.setText('Login')

        self.line_edit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button.clicked.connect(self.on_login_button_clicked)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Return.numerator:
            self.login()

    def on_login_button_clicked(self) -> None:
        self.login()

    def login(self) -> None:
        answer = api.resolvers.login(self.line_edit_login.text(), self.line_edit_password.text())

        messagebox = QMessageBox(self)
        messagebox.setStandardButtons(QMessageBox.StandardButton.Ok)
        messagebox.setWindowTitle("Error" if not answer else "Information")
        messagebox.setText("Incorrect login or password" if not answer else "Successful login")
        messagebox.setIcon(QMessageBox.Icon.Critical if not answer else QMessageBox.Icon.Information)
        messagebox.show()
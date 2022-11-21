from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt
from loginwindow import LoginWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__initUi()
        self.__settingUi()
        self.show()

    def __initUi(self) -> None:
        self.central_widget = QWidget()
        self.main_v_layout = QVBoxLayout()
        self.login_button_v_layout = QVBoxLayout()
        self.exit_button_v_layout = QVBoxLayout()
        self.login_button = QPushButton()
        self.exit_button = QPushButton()

    def __settingUi(self) -> None:
        self.setFixedSize(300, 400)
        self.setWindowTitle('Touragency Client')

        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_v_layout)
        self.main_v_layout.addLayout(self.login_button_v_layout)
        self.main_v_layout.addLayout(self.exit_button_v_layout)

        self.login_button_v_layout.addWidget(self.login_button)
        self.exit_button_v_layout.addWidget(self.exit_button)

        self.login_button_v_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.exit_button_v_layout.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.login_button.setText('Login')
        self.exit_button.setText('Exit')

        self.login_button.clicked.connect(self.on_login_button_clicked)
        self.exit_button.clicked.connect(self.on_exit_button_clicked)

    def on_login_button_clicked(self) -> None:
        self.open_login_dialog()

    def on_exit_button_clicked(self) -> None:
        self.exit()

    def open_login_dialog(self) -> None:
        login_window = LoginWindow(self)

    def exit(self) -> None:
        self.close()

from PySide6 import QtWidgets
from PySide6 import QtCore
from client.loginwindow import LoginWindow
from client.registerwindow import RegisterWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__initUi()
        self.__settingUi()
        self.show()

    def __initUi(self) -> None:
        self.central_widget = QtWidgets.QWidget()
        self.main_v_layout = QtWidgets.QHBoxLayout()
        self.page_list = self.PageListMenu()
        self.tour_list = self.TourList()
        self.authorization_menu = self.AuthorizationMenu()

    def __settingUi(self):
        self.resize(930, 615)
        self.setWindowTitle('Touragency Client')
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_v_layout)

        self.main_v_layout.addWidget(self.page_list)
        self.main_v_layout.addWidget(self.tour_list)
        self.main_v_layout.addWidget(self.authorization_menu)

    def show_message(self, text: str, error: bool = False, parent=None) -> None:
        messagebox = QtWidgets.QMessageBox(self if not parent else parent)
        messagebox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        messagebox.setWindowTitle("Error" if error else "Information")
        messagebox.setText(text)
        messagebox.setIcon(QtWidgets.QMessageBox.Icon.Critical if error else QtWidgets.QMessageBox.Icon.Information)
        messagebox.show()

    def exit(self) -> None:
        self.close()

    class PageListMenu(QtWidgets.QWidget):
        def __init__(self) -> None:
            super().__init__()
            self.__initUi()
            self.__settingUi()

        def __initUi(self) -> None:
            self.main_layout = QtWidgets.QVBoxLayout()
            self.page_list = QtWidgets.QListWidget()
            self.tour_item = QtWidgets.QListWidgetItem()
            self.ticket_item = QtWidgets.QListWidgetItem()

        def __settingUi(self):
            self.setMaximumWidth(150)
            self.setLayout(self.main_layout)
            self.main_layout.setContentsMargins(0, 0, 0, 0)

            self.main_layout.addWidget(self.page_list)

            self.page_list.addItem(self.tour_item)
            self.page_list.addItem(self.ticket_item)

            self.tour_item.setText('Tours')
            self.ticket_item.setText('Tickets')

            self.page_list.itemClicked.connect(self.itemClicked)

        def itemClicked(self, item):
            pass

    class TourList(QtWidgets.QWidget):
        def __init__(self) -> None:
            super().__init__()
            self.__initUi()
            self.__settingUi()

        def __initUi(self) -> None:
            self.main_v_layout = QtWidgets.QVBoxLayout()
            self.scroll_area = QtWidgets.QScrollArea()
            self.scroll_widget = QtWidgets.QWidget()
            self.scroll_layout = QtWidgets.QVBoxLayout()

        def __settingUi(self):
            self.setLayout(self.main_v_layout)
            self.main_v_layout.setContentsMargins(0, 0, 0, 0)
            self.scroll_area.setWidget(self.scroll_widget)
            self.scroll_widget.setLayout(self.scroll_layout)
            self.main_v_layout.addWidget(self.scroll_area)
            self.scroll_area.setWidgetResizable(True)
            self.scroll_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        class TourItem(QtWidgets.QWidget):
            def __init__(self):
                super().__init__()
                self.__initUi()
                self.__settingUi()

            def __initUi(self):
                self.main_h_layout = QtWidgets.QHBoxLayout()
                self.country = QtWidgets.QLabel()
                self.hours = QtWidgets.QLabel()
                self.price = QtWidgets.QLabel()
                self.buy_button = QtWidgets.QPushButton()

            def __settingUi(self):
                self.setLayout(self.main_h_layout)
                self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

                self.main_h_layout.addWidget(self.country)
                self.main_h_layout.addWidget(self.hours)
                self.main_h_layout.addWidget(self.price)
                self.main_h_layout.addWidget(self.buy_button)

                self.buy_button.setText('Buy')

            def set_tour_info(self, country: str, hours: str, price: str):
                self.country.setText(country)
                self.hours.setText(hours)
                self.price.setText(price)

    class AuthorizationMenu(QtWidgets.QWidget):
        def __init__(self) -> None:
            super().__init__()
            self.__initUi()
            self.__settingUi()

        def __initUi(self) -> None:
            self.main_v_layout = QtWidgets.QVBoxLayout()
            self.login_button = QtWidgets.QPushButton()
            self.register_button = QtWidgets.QPushButton()

        def __settingUi(self):
            self.setObjectName('sf')
            self.setLayout(self.main_v_layout)
            self.setMaximumWidth(120)

            self.main_v_layout.addWidget(self.login_button)
            self.main_v_layout.addWidget(self.register_button)

            self.main_v_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)

            self.login_button.setText('Login')
            self.register_button.setText('Register')

            self.login_button.clicked.connect(self.on_login_click)
            self.register_button.clicked.connect(self.on_register_click)

        def on_login_click(self):
            LoginWindow(self.parent().parent())

        def on_register_click(self):
            RegisterWindow(self.parent().parent())

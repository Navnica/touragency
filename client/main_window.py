from PySide6 import QtWidgets, QtCore, QtGui
from client.login_form import LoginWindow
from client.register_form import RegisterWindow
from client.tools import get_pixmap_path
from client.api.session import Session
import client.api.resolvers
from server.sql_base.models import User
import threading

session: Session = Session()


def include_widgets_by_pl(element: dict[str, QtWidgets.QWidget]):
    global session

    for key, item in element.items():
        if not issubclass(type(item), QtWidgets.QWidget):
            continue

        if item.property('power_level') is not None:
            item.show() if session.user.power_level >= item.property('power_level') else item.hide()

        include_widgets_by_pl(item.__dict__)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__initUi()
        self.__setupUi()
        self.show()

    def __initUi(self) -> None:
        self.central_widget = QtWidgets.QWidget()
        self.main_h_layout = QtWidgets.QHBoxLayout()
        self.page_list = PageListMenu()
        self.tour_list = TourList()
        self.ticket_list = TicketList()
        self.authorization_menu = AuthorizationMenu()
        self.user_profile = UserProfile()

    def __setupUi(self) -> None:
        self.resize(930, 615)
        self.setWindowTitle('Tour agency Client')
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_h_layout)
        self.main_h_layout.setContentsMargins(0, 0, 0, 0)

        self.main_h_layout.addWidget(self.page_list)
        self.main_h_layout.addWidget(self.tour_list)
        self.main_h_layout.addWidget(self.ticket_list)
        self.main_h_layout.addWidget(self.authorization_menu)
        self.main_h_layout.addWidget(self.user_profile)

        self.ticket_list.hide()

        self.page_list.switch_page(self.tour_list)

        self.page_list.ticket_item.connect_function(lambda: self.page_list.switch_page(self.ticket_list))
        self.page_list.tour_item.connect_function(lambda: self.page_list.switch_page(self.tour_list))

        include_widgets_by_pl(self.__dict__)

        self.user_profile.hide()

    def show_message(self, text: str, error: bool = False, parent=None) -> None:
        messagebox = QtWidgets.QMessageBox(self if not parent else parent)
        messagebox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        messagebox.setWindowTitle("Error" if error else "Information")
        messagebox.setText(text)
        messagebox.setIcon(QtWidgets.QMessageBox.Icon.Critical if error else QtWidgets.QMessageBox.Icon.Information)
        messagebox.show()

    def set_session(self, new_session: Session):
        global session
        session = new_session
        self.authorization()

    def authorization(self):
        self.authorization_menu.hide()
        self.user_profile.show()
        include_widgets_by_pl(self.__dict__)
        self.user_profile.fill_line_edits()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        exit()

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        pass


class PageListMenu(QtWidgets.QWidget):
    opened_widget = None

    def __init__(self) -> None:
        super().__init__()
        self.__initUi()
        self.__setupUi()

    def __initUi(self) -> None:
        self.main_v_layout = QtWidgets.QVBoxLayout()
        self.tour_item = MenuItem()
        self.ticket_item = MenuItem()

    def __setupUi(self) -> None:
        self.setMaximumWidth(120)
        self.setLayout(self.main_v_layout)
        self.main_v_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.main_v_layout.setContentsMargins(5, 5, 5, 5)
        self.opened_widget = self.tour_item

        self.tour_item.setup('tour.png', 'Tours')
        self.ticket_item.setup('ticket.png', 'Tickets')

        self.main_v_layout.addWidget(self.tour_item)
        self.main_v_layout.addWidget(self.ticket_item)

        self.tour_item.setProperty('power_level', 0)
        self.ticket_item.setProperty('power_level', 1)

    def switch_page(self, page):
        self.opened_widget.hide()
        self.opened_widget = page
        page.show()


class MenuItem(QtWidgets.QFrame):
    connection_def = None

    def __init__(self) -> None:
        super().__init__()
        self.__initUi()
        self.__setupUi()

    def __initUi(self) -> None:
        self.main_h_layout = QtWidgets.QHBoxLayout()
        self.container_widget = QtWidgets.QWidget()
        self.container_layout = QtWidgets.QHBoxLayout()
        self.icon = QtWidgets.QLabel()
        self.title = QtWidgets.QLabel()

    def __setupUi(self) -> None:
        self.setLayout(self.main_h_layout)
        self.main_h_layout.addWidget(self.container_widget)
        self.container_widget.setLayout(self.container_layout)
        self.main_h_layout.setContentsMargins(5, 5, 5, 5)
        self.container_layout.setContentsMargins(5, 5, 5, 5)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)

        self.title.setStyleSheet('color: black')

        self.container_layout.addWidget(self.icon)
        self.container_layout.addWidget(self.title)
        self.icon.setFixedSize(32, 32)

    def setup(self, icon_name: str, title: str):
        self.set_icon(icon_name)
        self.set_title(title)

    def set_icon(self, icon_name: str) -> None:
        self.icon.setPixmap(QtGui.QPixmap(get_pixmap_path(icon_name)))

    def set_title(self, title: str) -> None:
        self.title.setText(title)

    def on_mouse_enter(self):
        self.setStyleSheet('QFrame{background-color: darkgray; border-radius: 15px}')
        self.title.setStyleSheet('color: white')

    def on_mouse_leave(self):
        self.setStyleSheet('QFrame{background-color: none; border-radius: 15px}')
        self.title.setStyleSheet('color: black')

    def on_mouse_clicked(self):
        if self.connection_def:
            self.connection_def()

    def connect_function(self, foo):
        self.connection_def = foo

    def enterEvent(self, event: QtGui.QEnterEvent) -> None:
        self.on_mouse_enter()

    def leaveEvent(self, event: QtCore.QEvent) -> None:
        self.on_mouse_leave()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        self.on_mouse_clicked()


class TourList(QtWidgets.QWidget):
    add_tour_signal = QtCore.Signal(str, str, str, str)
    stop_flag: bool = False

    def __init__(self) -> None:
        super().__init__()
        self.__initUi()
        self.__setupUi()

    def __initUi(self) -> None:
        self.main_v_layout = QtWidgets.QVBoxLayout()
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout()

    def __setupUi(self) -> None:
        self.setLayout(self.main_v_layout)
        self.main_v_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_widget.setLayout(self.scroll_layout)
        self.main_v_layout.addWidget(self.scroll_area)
        self.scroll_area.setWidgetResizable(True)

        self.add_tour_signal.connect(self.add_tour_slot)

        threading.Thread(target=self.load_tours).start()

    def load_tours(self) -> None:
        for tour in client.api.resolvers.get_all_tours():
            country = client.api.resolvers.get_country_by_id(int(tour['country_id']))['name']
            self.add_tour_signal.emit(
                str(tour['id']),
                country,
                str(tour['hours']),
                str(tour['price']))

    def add_tour(self, tour_id: str, country: str, hours: str, price: str) -> None:
        new_tour = TourItem()
        new_tour.set_tour_info(country, hours, price)
        self.scroll_widget.__dict__.update({tour_id: new_tour})
        self.scroll_layout.addWidget(new_tour)

    @QtCore.Slot(str, str, str, str)
    def add_tour_slot(self, tour_id: str, country: str, hours: str, price: str) -> None:
        self.add_tour(tour_id, country, hours, price)
        include_widgets_by_pl(self.__dict__)


class TourItem(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__initUi()
        self.__setupUi()

    def __initUi(self) -> None:
        self.main_h_layout = QtWidgets.QHBoxLayout()
        self.country = QtWidgets.QLabel()
        self.hours = QtWidgets.QLabel()
        self.price = QtWidgets.QLabel()
        self.buy_button = QtWidgets.QPushButton()
        self.edit_button = QtWidgets.QPushButton()
        self.delete_button = QtWidgets.QPushButton()

    def __setupUi(self) -> None:
        self.setLayout(self.main_h_layout)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.main_h_layout.addWidget(self.country)
        self.main_h_layout.addWidget(self.hours)
        self.main_h_layout.addWidget(self.price)
        self.main_h_layout.addWidget(self.buy_button)
        self.main_h_layout.addWidget(self.edit_button)
        self.main_h_layout.addWidget(self.delete_button)

        self.buy_button.setText('Buy')
        self.edit_button.setIcon(QtGui.QPixmap(get_pixmap_path('edit.png')))
        self.delete_button.setIcon(QtGui.QPixmap(get_pixmap_path('delete.png')))
        self.edit_button.setProperty('power_level', 2)
        self.delete_button.setProperty('power_level', 2)

        self.edit_button.setFixedSize(24, 24)
        self.delete_button.setFixedSize(24, 24)

    # include_widgets_by_pl(self.__dict__)

    def set_tour_info(self, country: str, hours: str, price: str) -> None:
        self.country.setText(country)
        self.hours.setText(hours)
        self.price.setText(price)


class TicketList(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__initUi()
        self.__setupUi()

    def __initUi(self) -> None:
        self.main_v_layout = QtWidgets.QVBoxLayout()
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout()

    def __setupUi(self) -> None:
        self.setLayout(self.main_v_layout)
        self.main_v_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_widget.setLayout(self.scroll_layout)
        self.main_v_layout.addWidget(self.scroll_area)
        self.scroll_area.setWidgetResizable(True)


class AuthorizationMenu(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__initUi()
        self.__setupUi()

    def __initUi(self) -> None:
        self.main_v_layout = QtWidgets.QVBoxLayout()
        self.login_button = QtWidgets.QPushButton()
        self.register_button = QtWidgets.QPushButton()

    def __setupUi(self) -> None:
        self.setLayout(self.main_v_layout)
        self.setMaximumWidth(120)

        self.main_v_layout.addWidget(self.login_button)
        self.main_v_layout.addWidget(self.register_button)

        self.main_v_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)

        self.login_button.setText('Login')
        self.register_button.setText('Register')

        self.login_button.clicked.connect(self.on_login_click)
        self.register_button.clicked.connect(self.on_register_click)

    def on_login_click(self) -> None:
        self.open_login_dialog()

    def on_register_click(self) -> None:
        self.open_register_dialog()

    def open_login_dialog(self):
        LoginWindow(self.parent().parent())  # Надеюсь увидеть этот комментарий и всё-таки отрефакторить код

    def open_register_dialog(self):
        RegisterWindow(self)

    def show_message(self, text: str, error: bool = False, parent=None) -> None:
        self.parent().parent().show_message(
            text=text,
            error=error,
            parent=parent
        )


class UserProfile(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__initUi()
        self.__setupUi()

    def __initUi(self) -> None:
        self.main_v_layout = QtWidgets.QVBoxLayout()

        self.name_layout = QtWidgets.QHBoxLayout()
        self.surname_layout = QtWidgets.QHBoxLayout()
        self.phone_layout = QtWidgets.QHBoxLayout()
        self.password_layout = QtWidgets.QHBoxLayout()
        self.confirm_layout = QtWidgets.QHBoxLayout()
        self.button_layout = QtWidgets.QHBoxLayout()

        self.name_label = QtWidgets.QLabel()
        self.surname_label = QtWidgets.QLabel()
        self.phone_label = QtWidgets.QLabel()
        self.password_label = QtWidgets.QLabel()
        self.confirm_password_label = QtWidgets.QLabel()
        self.power_level_label = QtWidgets.QLabel()

        self.name_line_edit = QtWidgets.QLineEdit()
        self.surname_line_edit = QtWidgets.QLineEdit()
        self.phone_line_edit = QtWidgets.QLineEdit()
        self.password_line_edit = QtWidgets.QLineEdit()
        self.confirm_password_line_edit = QtWidgets.QLineEdit()

        self.edit_button = QtWidgets.QPushButton()
        self.allow_button = QtWidgets.QPushButton()

        self.spacer = QtWidgets.QSpacerItem(0, 10)

    def __setupUi(self) -> None:
        self.setLayout(self.main_v_layout)
        self.main_v_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.setMaximumWidth(250)
        self.main_v_layout.addLayout(self.name_layout)
        self.main_v_layout.addLayout(self.surname_layout)
        self.main_v_layout.addLayout(self.phone_layout)
        self.main_v_layout.addSpacerItem(self.spacer)
        self.main_v_layout.addLayout(self.password_layout)
        self.main_v_layout.addLayout(self.confirm_layout)
        self.main_v_layout.addWidget(self.power_level_label)
        self.main_v_layout.addSpacerItem(self.spacer)
        self.main_v_layout.addLayout(self.button_layout)

        self.name_layout.addWidget(self.name_label)
        self.surname_layout.addWidget(self.surname_label)
        self.phone_layout.addWidget(self.phone_label)
        self.password_layout.addWidget(self.password_label)
        self.confirm_layout.addWidget(self.confirm_password_label)

        self.name_layout.addWidget(self.name_line_edit)
        self.surname_layout.addWidget(self.surname_line_edit)
        self.phone_layout.addWidget(self.phone_line_edit)
        self.password_layout.addWidget(self.password_line_edit)
        self.confirm_layout.addWidget(self.confirm_password_line_edit)

        self.button_layout.addWidget(self.edit_button)
        self.button_layout.addWidget(self.allow_button)

        self.edit_button.setText('Edit')
        self.allow_button.setText('Allow')

        self.name_label.setText('Name:')
        self.surname_label.setText('Surname:')
        self.phone_label.setText('Phone:')
        self.password_label.setText('Password:')
        self.confirm_password_label.setText('Confirm:')
        self.power_level_label.setText('Power level: 0')

        self.name_line_edit.setFixedWidth(150)
        self.surname_line_edit.setFixedWidth(150)
        self.phone_line_edit.setFixedWidth(150)
        self.password_line_edit.setFixedWidth(150)
        self.confirm_password_line_edit.setFixedWidth(150)

        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.confirm_password_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.set_line_edit_enable(False)

        self.allow_button.setEnabled(False)

        self.edit_button.clicked.connect(self.on_edit_click)
        self.allow_button.clicked.connect(self.on_allow_click)

    def set_line_edit_enable(self, enabled: bool) -> None:
        self.name_line_edit.setEnabled(enabled)
        self.surname_line_edit.setEnabled(enabled)
        self.phone_line_edit.setEnabled(enabled)
        self.password_line_edit.setEnabled(enabled)
        self.confirm_password_line_edit.setEnabled(enabled)

    def fill_line_edits(self) -> None:
        global session

        self.name_line_edit.setText(session.user.name)
        self.surname_line_edit.setText(session.user.surname)
        self.phone_line_edit.setText(session.user.phone)
        self.password_line_edit.setText(session.user.password)
        self.power_level_label.setText(f'Power level: {str(session.user.power_level)}')

    def on_edit_click(self) -> None:
        self.edit_button.setEnabled(False)
        self.allow_button.setEnabled(True)

        self.set_line_edit_enable(True)

    def validate_password(self) -> bool:
        global session
        return self.confirm_password_line_edit.text() == self.password_line_edit.text()

    def on_allow_click(self) -> None:
        global session

        if not self.validate_password():
            return self.parent().parent().show_message(
                text='Incorrect confirm password',
                error=True,
                parent=self
            )

        user = User(
            id=session.user.id,
            name=self.name_line_edit.text(),
            surname=self.surname_line_edit.text(),
            phone=self.phone_line_edit.text(),
            password=self.password_line_edit.text(),
            power_level=session.user.power_level
        )

        session.update(user)

        if session.error:
            return self.parent().parent().show_message(
                text=session.error,
                error=True,
                parent=self
            )

        self.set_line_edit_enable(False)
        self.allow_button.setEnabled(False)
        self.edit_button.setEnabled(True)

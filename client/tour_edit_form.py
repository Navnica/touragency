from PySide6 import QtWidgets, QtCore


class TourEdit(QtWidgets.QDialog):
    tour_id: int = None

    def __init__(self, parent, tour_id: int) -> None:
        super().__init__(parent=parent)
        self.tour_id = tour_id
        self.__initUi()
        self.__settingUi()
        self.show()

    def __initUi(self) -> None:
        self.main_layout = QtWidgets.QGridLayout()
        self.country_label = QtWidgets.QLabel()
        self.hours_label = QtWidgets.QLabel()
        self.price_label = QtWidgets.QLabel()
        self.country_combo_box = QtWidgets.QComboBox()
        self.hours_line_edit = QtWidgets.QLineEdit()
        self.price_line_edit = QtWidgets.QLineEdit()
        self.update_button = QtWidgets.QPushButton()
        self.close_button = QtWidgets.QPushButton()
        self.spacer = QtWidgets.QWidget()

    def __settingUi(self) -> None:
        self.setWindowTitle(f'Edit {self.tour_id}-tour')
        self.setLayout(self.main_layout)

        self.main_layout.addWidget(self.country_label, 1, 1, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(self.hours_label, 1, 2, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(self.price_label, 1, 3, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(self.country_combo_box, 2, 1, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(self.hours_line_edit, 2, 2, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(self.price_line_edit, 2, 3, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(self.spacer, 3, 2, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.main_layout.addWidget(self.update_button, 4, 2, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        self.main_layout.addWidget(self.close_button, 4, 3, alignment=QtCore.Qt.AlignmentFlag.AlignRight)

        self.country_label.setText('Country')
        self.hours_label.setText('Hours')
        self.price_label.setText('Price')
        self.update_button.setText('Update')
        self.close_button.setText('Close')

        self.update_button.clicked.connect(self.on_update_clicK)
        self.close_button.clicked.connect(self.on_close_click)

        self.spacer.setFixedHeight(10)
        self.update_button.setFixedWidth(50)
        self.close_button.setFixedWidth(50)

    def on_update_clicK(self):
        pass

    def on_close_click(self):
        self.close()

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

from data_modules import db
from data_modules import json

from static.login_form_ui import Ui_main_window
# This module is not used, but it must be imported for the icons to work
from static.icons import ico

import sys


class Login_form_window(QMainWindow, Ui_main_window):
    def __init__(self):
        # Base class init
        super().__init__()

        self.setupUi(self)

        # Need this for calling selection window from main.py if we need it
        # (And also there weren't any error from QApplication)
        # Value will be updated before closeEvent if program need it
        self.need_to_open_select_menu = False
        # Args for opening board selection menu
        self.selection_menu_args = []

        # Set bindings and some styles to widgets
        self.init_ui()

    def init_ui(self) -> None:
        """
        Setting up all of the bindings for signals and
        adjusts the settings for widgets
        """

        # Set up all icons from resource file
        self.setWindowIcon(QIcon(":/icons/app.png"))
        self.label_create_user_icon.setPixmap(QPixmap(":/icons/user.png"))
        self.label_user_icon.setPixmap(QPixmap(":/icons/user.png"))
        self.label_create_key_icon.setPixmap(QPixmap(":/icons/key.png"))
        self.label_create_repeat_key_icon.setPixmap(QPixmap(":/icons/key.png"))
        self.label_key_icon.setPixmap(QPixmap(":/icons/key.png"))

        # Align all layouts
        self.vlayout_left.setAlignment(Qt.AlignJustify | Qt.AlignHCenter)
        self.vlayout_midle.setAlignment(Qt.AlignJustify | Qt.AlignHCenter)
        self.vlayout_right.setAlignment(Qt.AlignJustify | Qt.AlignHCenter)
        self.vlayout_login_form.setAlignment(Qt.AlignRight)
        self.vlayout_create_account_form.setAlignment(Qt.AlignLeft)

        # Align buttons in layouts
        self.vlayout_offline.setAlignment(self.button_continue_offline, Qt.AlignHCenter | Qt.AlignCenter)
        self.vlayout_login_form.setAlignment(self.button_enter, Qt.AlignCenter)
        self.vlayout_create_account_form.setAlignment(self.button_create_account, Qt.AlignCenter)

        # Set layouts on widgets with background
        self.widget_left_background.setLayout(self.vlayout_left_form)
        self.widget_midle_background.setLayout(self.vlayout_offline)
        self.widget_right_background.setLayout(self.vlayout_right_form)

        # Setting up bindings for signals
        self.button_enter.clicked.connect(self.enter_account)
        self.button_create_account.clicked.connect(self.create_account)
        self.button_continue_offline.clicked.connect(self.work_offline)
        self.Form.mousePressEvent = lambda event: self.Form.setFocus()
        self.label_sign_up.mousePressEvent = lambda event: self.lineEdit_login_create_input.setFocus(True)
        self.label_sign_in.mousePressEvent = lambda event: self.lineEdit_login_input.setFocus(True)

        # For removing focus from QLineEdit widget on launch
        self.Form.setFocus()
        # Main layout with all widgets
        self.Form.setLayout(self.hlayout_main)

    def check_form_field(self, field_value: str) -> bool:
        """
        Method checks value of form field, for example login or password

        :param field_value: Value of the field to check (login or password)
        :return: True if value correct False if not
        """

        # This much easier than filtering all
        # forbidden characters with str.isalnum() method
        ALLOWED_SYMBOLS = {
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        }
        for char in field_value.lower():
            if char not in ALLOWED_SYMBOLS:
                return False
        return len(field_value) != 0

    def enter_account(self):
        # Checking login and password
        login = self.lineEdit_login_input.text()
        password = self.lineEdit_password_input.text()

        is_login_correct = self.check_form_field(login)
        is_password_correct = self.check_form_field(password)

        # All possible cases down below
        if not is_login_correct:
            self.label_user_icon.setPixmap(QPixmap(":/icons/error.png"))
            self.label_user_icon.setToolTip("Некорректный логин")
            self.label_user_icon.setToolTipDuration(5000)
        else:
            # Turning back user icon if all is ok
            self.label_user_icon.setPixmap(QPixmap(":/icons/user.png"))
            self.label_user_icon.setToolTip('')

        if not is_password_correct:
            self.label_key_icon.setPixmap(QPixmap(":/icons/error.png"))
            self.label_key_icon.setToolTip("Некорректный пароль")
            self.label_key_icon.setToolTipDuration(5000)
        else:
            # Turning back key icon if all is ok
            self.label_key_icon.setPixmap(QPixmap(":/icons/key.png"))
            self.label_key_icon.setToolTip('')

        if not is_password_correct or not is_login_correct:
            return

        database = db.database()
        # Trying to get user id
        try:
            user_id = database.get_user_id_from_db_by_form_data(login, password)
        except db.AccountNotExists as e:
            # Setting error icon and tool tip if something goes wrong
            self.label_user_icon.setPixmap(QPixmap(":/icons/error.png"))
            self.label_user_icon.setToolTip("Неверный логин")
            return
        except db.IncorrectPassword as e:
            # Setting error icon and tool tip if something goes wrong
            self.label_key_icon.setPixmap(QPixmap(":/icons/error.png"))
            self.label_key_icon.setToolTip("Неверный пароль")
            return
        else:
            self.label_user_icon.setPixmap(QPixmap(":/icons/user.png"))
            self.label_user_icon.setToolTip('')
            self.label_key_icon.setPixmap(QPixmap(":/icons/key.png"))
            self.label_key_icon.setToolTip('')

        # All code down bellow needs for comparison between json from
        # database and json from device
        boards_from_db = database.get_boards_json_by_user_id(user_id)
        boards_from_device = json.load_raw_json_from_file("boards.json")

        # Comparing boards json
        if json.can_combine_boards_jsons(json.format_json(boards_from_device),
                                         json.format_json(boards_from_db)):
            message = QMessageBox(QMessageBox.Information, '',
                                  "На устройстве найдены досоки, а в аккаунте ничего не сохранено\n" +
                                  "Хотите добавить данные в аккаунт?")
            message.setWindowIcon(QIcon(":/icons/app.png"))
            message.setWindowTitle("Yello")
            message.addButton(button_yes := QPushButton("Да", message), QMessageBox.YesRole)
            message.addButton(QPushButton("Нет", message), QMessageBox.NoRole)
            message.exec()

            if message.clickedButton() == button_yes:
                # Getting combined data and json
                combined_json, combined_boards_data = json.combine_boards_jsons(boards_from_device,
                                                                                boards_from_db)
                database.update_boards_json_by_user_id(user_id,
                                                       combined_json)
        # Args for opening next window
        self.need_to_open_select_menu = True
        self.selection_menu_args = [user_id]
        self.close()

    def create_account(self) -> None:
        login = self.lineEdit_login_create_input.text()
        password = self.lineEdit_password_create_input.text()
        repeat_password = self.lineEdit_password_repeat_input.text()

        # Checking login and password
        is_login_correct = self.check_form_field(login)
        is_password_correct = self.check_form_field(password)

        # All possible cases down below
        if not is_login_correct:
            self.label_create_user_icon.setPixmap(QPixmap(":/icons/error.png"))
            self.label_create_user_icon.setToolTip("Некорректный логин")
            self.label_create_user_icon.setToolTipDuration(5000)
        else:
            # Turning back user icon if all is ok
            self.label_create_user_icon.setPixmap(QPixmap(":/icons/user.png"))
            self.label_create_user_icon.setToolTip('')

        if not is_password_correct:
            self.label_create_key_icon.setPixmap(QPixmap(":/icons/error.png"))
            self.label_create_key_icon.setToolTip("Некорректный пароль")
            self.label_create_key_icon.setToolTipDuration(5000)
        else:
            # Turning back key icon if all is ok
            self.label_create_key_icon.setPixmap(QPixmap(":/icons/key.png"))
            self.label_create_key_icon.setToolTip('')

        if not is_password_correct or not is_login_correct:
            return

        elif repeat_password != password:
            # First password
            self.label_create_key_icon.setPixmap(QPixmap(":/icons/error.png"))
            self.label_create_key_icon.setToolTip("Пароли не совпадают")
            self.label_create_key_icon.setToolTipDuration(5000)
            # Repeat password
            self.label_create_repeat_key_icon.setPixmap(QPixmap(":/icons/error.png"))
            self.label_create_repeat_key_icon.setToolTip("Пароли не совпадают")
            self.label_create_repeat_key_icon.setToolTipDuration(5000)
            return

        database = db.database()
        # Trying to add account to database
        try:
            database.add_account_to_db(login, password)
        except db.AccountAlreadyExists as e:
            self.label_create_user_icon.setPixmap(QPixmap(":/icons/error.png"))
            self.label_create_user_icon.setToolTip("Такой аккаунт уже есть")
            self.label_create_user_icon.setToolTipDuration(5000)
            return
        else:
            # User icon
            self.label_user_icon.setPixmap(QPixmap(":/icons/user.png"))
            self.label_user_icon.setToolTip('')
            # First password icon
            self.label_create_key_icon.setPixmap(QPixmap(":/icons/key.png"))
            self.label_create_key_icon.setToolTip('')
            # Repeat password icon
            self.label_create_repeat_key_icon.setPixmap(QPixmap(":/icons/key.png"))
            self.label_create_repeat_key_icon.setToolTip('')

        # Don't need to handle exceptions
        user_id = database.get_user_id_from_db_by_form_data(login, password)
        self.need_to_open_select_menu = True
        self.selection_menu_args = [user_id]
        self.close()

    def work_offline(self) -> None:
        self.selection_menu_args = [-1]
        self.need_to_open_select_menu = True
        self.close()


def start() -> list:
    application = QApplication(sys.argv)
    application_window = Login_form_window()
    application_window.show()
    application.exec()
    # Returns value to main.py tells need to open selection window or not.
    # And also there are arguments for opening a new window
    return [application_window.selection_menu_args,
            application_window.need_to_open_select_menu]

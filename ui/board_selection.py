import sys
import os

from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QShortcut, \
    QPushButton, QHBoxLayout, QSizePolicy, QInputDialog, QLineEdit
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QEvent
# This module is not used, but it must be imported for the icons to work
from static.icons import ico
from static.board_selection_ui import Ui_Form

from ui import board_edit

from data_modules import json
from data_modules import db


class Board_selection_window(Ui_Form, QWidget):
    def __init__(self, user_id: int, boards_data: dict):
        """
        Init method
        :param user_id: Id of user
        :param board_data: Dict with all board data
        """

        # Base class init
        super().__init__()

        # Id of user (-1 if program works in offline mode)
        self.current_user_id = user_id
        # Id of board for editing
        self.board_id_for_editing = -1
        # Data of all boards
        self.boards_data = boards_data

        self.setupUi(self)

        # Set bindings and some styles to widgets
        self.init_ui()

    def init_ui(self):
        # Icon for window
        self.setWindowIcon(QtGui.QIcon(":/icons/app.png"))
        # Shortcut for saving boards data to file
        QShortcut(QtGui.QKeySequence.Save, self).activated.connect(self.save)
        self.button_create_board.clicked.connect(self.add_board)
        # Setting up layout in widget for scroll area
        self.scroll_area_widget_container.setLayout(self.vlayout_items)

        # Adding all items
        for board in self.boards_data["boards"]:
            # Change title if it's empty
            title = board["title"]
            if not title:
                title = "Без названия"

            label_board_name = QLabel(title, self)
            label_board_name.setStyleSheet("color: #FFFFFF;")
            label_board_name.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            label_board_name.setFont(QtGui.QFont("Nirmala UI", pointSize=16))
            label_board_name.installEventFilter(self)

            # Add item to layout
            self.vlayout_items.addWidget(label_board_name)

        # Adding widgets to main layout
        self.vlayout_main.addWidget(self.button_create_board, Qt.AlignHCenter)
        self.vlayout_main.addWidget(self.scroll_area, Qt.AlignHCenter | Qt.AlignVCenter)
        # Applying layout to Board_selection_window
        self.setLayout(self.vlayout_main)

    def add_board(self):
        # Dialog for get name for board
        name, is_dialog_ok = QInputDialog.getText(self, "Название",
                                                  "Введите название для доски",
                                                  QLineEdit.Normal)
        # Check name from input
        name = name.replace('\t', ' ').replace('\n', ' ')
        if not (is_dialog_ok and name.replace(' ', '')):
            name = "Без названия"

        # Updating boards data
        self.boards_data["boards"].append({"title": name, "groups": []})
        # Label with board name
        label_board_name = QLabel(name, self)
        label_board_name.setStyleSheet("color: #FFFFFF;")
        label_board_name.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        label_board_name.setFont(QtGui.QFont("Nirmala UI", pointSize=16))
        label_board_name.installEventFilter(self)
        self.vlayout_items.insertWidget(self.vlayout_items.count(), label_board_name)

    def closeEvent(self, event):
        # Auto save
        self.save()

    def save(self, *args) -> None:
        """
        Method saves to file data of current board. Also if user enter
        in account from db, information in database will updated.
        :param args: Event data
        """
        # All data of current board
        if self.current_user_id != -1:
            from data_modules import db
            database = db.database()
            database.update_boards_json_by_user_id(self.current_user_id, json.get_json_by_data(self.boards_data))
        else:
            json.save_json_data_to_file("boards.json", self.boards_data)

    def eventFilter(self, source_obj, event) -> bool:
        # Using this to get QLabel widget that was clicked by user
        if event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
            # Call open board method
            self.open_board(source_obj)
        return super().eventFilter(source_obj, event)

    def open_board(self, sender) -> None:
        """
        Method that open a board that respond to given sender widget
        :param sender: Widget that called a method
        """
        # Id of the board
        self.board_id_for_editing = self.vlayout_items.indexOf(sender)
        self.close()


def start(user_id: int, extra_args={}):
    """
    Function that launch boards selection window
    :param user_id: Id of user
    :param extra_args: Dict with extra arguments from board edit window
    """
    # Empty boards data by default
    boards_data = {
        "boards": []
    }

    # Creating database object if user have entered in his account
    if user_id != -1:
        database = db.database()
    else:
        database = None

    # Check that file exists
    if os.path.isfile("boards.json") and user_id == -1:
        # Loading data from device
        data_device = json.load_json_data_from_file("boards.json")
        # Trying to add boards from data
        boards_data["boards"].extend(data_device.get("boards", []))

    # Check that user enter in account
    if database:
        # Boards data from database by given id
        data_database = database.get_boards_json_by_user_id(user_id)
        # Converting this data to python types
        data_database = json.parse_json(data_database)
        new_boards = data_database.get("boards", [])
        if new_boards:
            # Adding boards from data
            boards_data["boards"].extend(new_boards)
        del new_boards

    # Removing duplicates from boards_data (before applying changes from .json)
    temp = []
    for data in boards_data["boards"]:
        if data not in temp:
            temp.append(data)
    # Collecting all values back
    boards_data["boards"] = temp.copy()
    # Freeing memory after temp
    del temp

    # Check that file with last board changes exists
    if os.path.isfile("last_board.json"):
        data_changed = json.load_json_data_from_file("last_board.json")
        # Check if data in file is not empty
        if data_changed != {"boards": []}:
            # Set changes in boards
            if data_changed["board_id"] < len(boards_data["boards"]):
                boards_data["boards"][data_changed["board_id"]] = {
                    "title": data_changed["title"],
                    "groups": data_changed["groups"],
                }
            # Or add, if it was created recently
            else:
                boards_data["boards"].append({
                    "title": data_changed["title"],
                    "groups": data_changed["groups"],
                })
            # Saving changes in file if we can
            if os.path.isfile("boards.json") and data_changed.get("was_on_device", False):
                json.save_json_data_to_file("boards.json", boards_data)
        # Clearing file with last changes
        last_file = open("last_board.json", mode='r+', encoding="utf-8")
        last_file.truncate(0)
        last_file.close()

    # Updating data database
    if extra_args.get("update_db_from_file", False) and database:
        # Updating json
        database.update_boards_json_by_user_id(user_id,
                                               json.get_json_by_data(boards_data))

    # Starting application after all needed data was collected
    application = QApplication(sys.argv)
    application_window = Board_selection_window(user_id, boards_data)
    application_window.show()
    application.exec()
    # Freeing memory for avoid memory leak
    del application
    del database
    # If user select any board...
    if application_window.board_id_for_editing != -1:
        # ...open the edit window for it
        board_edit.start(user_id, application_window.board_id_for_editing,
                         boards_data["boards"][application_window.board_id_for_editing])

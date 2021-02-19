import sys

from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QShortcut, \
    QMessageBox, QPushButton, QFrame, QHBoxLayout
from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt
# This module is not used, but it must be imported for the icons to work
from static.icons import ico
from static.board_edit_ui import Ui_Form
from static.custom_widgets import QCard, QGroup

from ui import board_selection

from data_modules import json


class Board_edit_window(Ui_Form, QWidget):
    def __init__(self, user_id: int, board_id: int, board_data: dict):
        """
        Init method
        :param user_id: Id of user
        :param board_data: Dict with all board data
        """

        # Base class init
        super().__init__()
        # Id of user (-1 if program works in offline mode)
        self.current_user_id = user_id
        # Id of current board
        self.current_board_id = board_id
        # Data of current board
        self.board_data = board_data
        # Title of the board
        self.title = board_data["title"]
        # Variables for behavior after window closed
        self.need_to_open_selection_window = False
        self.args_for_opening_selection_window = {
            "board_id": self.current_board_id,
            "update_db_from_file": False,
        }

        self.setupUi(self)

        # Set bindings and some styles to widgets
        self.init_ui()

    def init_ui(self):
        # Shortcut for saving boards data to file
        QShortcut(QtGui.QKeySequence.Save, self).activated.connect(self.save)
        # Icons for navbar
        # Set layout with icons on navbar
        self.widget_navbar.setLayout(self.hlayout_navbar)
        self.vlayout_main.setAlignment(self.widget_navbar, Qt.AlignTop)
        self.hlayout_navbar.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        # Save icon
        self.label_icon_save = QLabel()
        self.label_icon_save.setPixmap(QtGui.QPixmap(":/icons/save.png"))
        self.hlayout_navbar.addWidget(self.label_icon_save)
        self.label_icon_save.mousePressEvent = self.save
        # Info icon
        self.label_icon_info = QLabel()
        self.label_icon_info.setPixmap(QtGui.QPixmap(":/icons/info.png"))
        self.hlayout_navbar.addWidget(self.label_icon_info)
        self.label_icon_info.mousePressEvent = self.show_info
        # Home icon
        self.label_icon_home = QLabel()
        self.label_icon_home.setPixmap(QtGui.QPixmap(":/icons/home.png"))
        self.hlayout_navbar.addWidget(self.label_icon_home)
        self.label_icon_home.mousePressEvent = self.open_selection_window

        # Title of current board
        self.label_title = QLabel(self.title)
        self.label_title.setFont(QtGui.QFont("Nirmala UI", pointSize=14))
        self.label_title.setStyleSheet("QLabel{color: #FFFFFF;}")
        # Adding title to navbar
        self.hlayout_navbar.addWidget(self.label_title)
        self.hlayout_navbar.setAlignment(self.label_title, Qt.AlignHCenter | Qt.AlignVCenter)

        # All groups from given data
        for index, group in enumerate(self.board_data["groups"]):
            # Group with empty cards
            current_group = QGroup(index, group["title"], [])
            # Adding cards to group
            for card_data in group["cards"]:
                current_group.add_card(title=card_data["title"],
                                       marks_colors=card_data["marks_colors"].copy(),
                                       description=card_data["description"])
            # Inserting QGroup to layout
            self.hlayout_groups.insertWidget(self.hlayout_groups.count() - 1, current_group)

        # Setting up all scroll area stuff
        self.scroll_area_widget_window.setLayout(self.hlayout_groups)
        self.vlayout_main.addWidget(self.scroll_area_window, Qt.AlignHCenter | Qt.AlignVCenter)

        # Add group button
        self.button_add_group.clicked.connect(self.add_group)
        # Extra customisations
        self.mousePressEvent = self.set_focus
        self.setFocus()  # To remove focus from QLineEdit widget
        self.setWindowIcon(QtGui.QIcon(":/icons/app.png"))
        self.setLayout(self.vlayout_main)
        self.setMinimumSize(1000, 550)

    def add_group(self):
        group = QGroup(len(self.board_data["groups"]), "Без названия", cards=[])
        self.hlayout_groups.insertWidget(self.hlayout_groups.count() - 1, group)
        self.board_data["groups"].append(group.to_dict())

    def set_focus(self, event):
        if event.button() == Qt.LeftButton:
            self.setFocus()

    def save(self, *args) -> None:
        """
        Method saves to file data of current board.
        :param args: Event data from mousePressEvent
        """
        # All data of current board
        data = {
            "title": self.title,
            "board_id": self.current_board_id,
            "groups": [],
            "was_on_device": self.current_user_id == -1
        }
        for i in range(self.hlayout_groups.count() - 1):
            data["groups"].append(self.hlayout_groups.itemAt(i).widget().to_dict())

        json.save_json_data_to_file("last_board.json", data)

    def show_info(self, *args) -> None:
        """
        :param args: Event data from mousePressEvent
        """
        INFO = str("Это раздел с редактированием доски, вы можете создавать группы,\n" +
               "добавлять карточки внутрь группы. Можно открыть окно с\n" +
               "выбором досок и открыть другую доску. Удачного использования :D")
        message = QMessageBox(QMessageBox.Information, "Информация", INFO)
        message.setWindowIcon(QtGui.QIcon(":/icons/app.png"))
        message.exec_()

    def open_selection_window(self, *args) -> None:
        """
        :param args: Event data from mousePressEvent
        """
        self.save()
        self.need_to_open_selection_window = True
        self.args_for_opening_selection_window["update_db_from_file"] = True
        self.close()


def start(user_id: int, board_id: int, board_data):
    """
    Function that launch boards selection window
    :param user_id: Id of user
    :param board_id: If of board
    :param board_data: Dict with all board data
    """
    application = QApplication(sys.argv)
    application_window = Board_edit_window(user_id, board_id, board_data)
    application_window.show()
    application.exec()
    # Freeing memory for avoid memory leak
    del application
    # Open the selection window if we need it
    if application_window.need_to_open_selection_window:
        board_selection.start(user_id, application_window.args_for_opening_selection_window)

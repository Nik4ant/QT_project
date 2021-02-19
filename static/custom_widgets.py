import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QFrame, QLabel, QApplication, \
    QVBoxLayout, QHBoxLayout, QSizePolicy, QPlainTextEdit, QLineEdit, \
    QScrollArea, QScrollBar, QColorDialog, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
# This module is not used, but it must be imported for the icons to work
from static.icons import ico


class QCard(QWidget):
    def __init__(self, card_id: int, title='', marks_colors=[], description='', parent=None):
        super().__init__(parent)
        # Group of card
        self.group_parent = parent

        # List with colors for card marks
        self.marks_colors = marks_colors
        # Title of the card
        self.title = title
        # Description
        self.description = description
        # Id of the card
        self.card_id = card_id

        self.init_ui()

    def init_ui(self):
        # Setting up main_widget
        self.card_widget_main = QWidget(self)
        self.card_widget_main.setObjectName("card_widget_main")
        self.card_widget_main.resize(140, 120)
        self.card_widget_main.setMinimumSize(130, 120)
        self.card_widget_main.setMaximumSize(260, 260)
        self.card_widget_main.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Title of the card (editable)
        self.lineEdit_title = QLineEdit(self.title)
        self.lineEdit_title.setStyleSheet("""
                                          QLineEdit { 
                                          background:rgba(0, 0, 0, 0);
                                          color: rgba(255, 255, 255, 93%);
                                          border-style: None; }""")
        self.lineEdit_title.setFont(QtGui.QFont("Nirmala UI", pointSize=10))
        self.lineEdit_title.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        # Layout with all card marks and with edit icon
        self.hlayout_marks = QHBoxLayout()
        for color in self.marks_colors:
            current_mark = QWidget()
            current_mark.setMinimumSize(22, 5)
            current_mark.setMaximumHeight(8)
            current_mark.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            current_mark.setStyleSheet("QWidget {background: " + color + ";}")
            self.hlayout_marks.addWidget(current_mark)

        # Adding delete icon to layout with marks
        self.label_add_mark_icon = QLabel()
        self.label_add_mark_icon.setPixmap(QtGui.QPixmap(":/icons/add.png"))
        self.label_add_mark_icon.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_add_mark_icon.mousePressEvent = self.add_mark
        self.hlayout_marks.addWidget(self.label_add_mark_icon)

        # Adding delete icon to layout with marks
        self.label_delete_icon = QLabel()
        self.label_delete_icon.setPixmap(QtGui.QPixmap(":/icons/delete.png"))
        self.label_delete_icon.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_delete_icon.mousePressEvent = self.delete_card
        self.hlayout_marks.addWidget(self.label_delete_icon)

        # Description of the card
        self.textEdit_deskription = QPlainTextEdit(self.description)
        self.textEdit_deskription.setStyleSheet("""
                                                QPlainTextEdit { 
                                                margin-top: 0.1em;
                                                margin-bottom: 0.1em;
                                                background:rgba(0, 0, 0, 0%);
                                                color: rgba(255, 255, 255, 79%);
                                                selection-background-color: grey;
                                                border: None; }""")
        self.textEdit_deskription.setFont(QtGui.QFont("Nirmala UI", pointSize=10))
        self.textEdit_deskription.setWordWrapMode(QtGui.QTextOption.WordWrap)
        self.textEdit_deskription.setFrameStyle(QFrame.NoFrame)
        self.textEdit_deskription.setAutoFillBackground(False)
        # Palette for text edit
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Highlight,  QtGui.QColor(255, 255, 255, 200))
        palette.setColor(QtGui.QPalette.HighlightedText,  QtGui.QColor(255, 255, 255, 200))
        self.textEdit_deskription.setPalette(palette)

        # Combine all widgets to main layout
        self.vlayout_main = QVBoxLayout()
        self.vlayout_main.setContentsMargins(8, 5, 8, 5)
        self.vlayout_main.addLayout(self.hlayout_marks)
        self.vlayout_main.addWidget(self.lineEdit_title)
        self.vlayout_main.addWidget(self.textEdit_deskription)
        self.vlayout_main.setStretch(3, 2)
        self.card_widget_main.setLayout(self.vlayout_main)

        # Container for whole card with card_widget_main inside
        self.vlayout_card_container = QVBoxLayout()
        self.vlayout_card_container.addWidget(self.card_widget_main)
        self.setLayout(self.vlayout_card_container)
        self.setStyleSheet("""#card_widget_main {
                              padding-top: 0.2em;
                              padding-bottom: 0.2em;
                              background: #38304D;
                              border-style: outset;
                              border-radius: 15px;
                              }
                              #card_widget_main::hover {
                              background: #443B5E; 
                              }""")
        self.mousePressEvent = self.change_focus

    def change_focus(self, *args):
        """
        Method that sets focus on widget
        :param args: Event data
        """
        self.setFocus()

    def add_mark(self, *args):
        """
        Method adds color mark to card
        :param args: Event data
        """
        # Limit for marks color
        if len(self.marks_colors) > 2:
            message = QMessageBox(QMessageBox.Information, "Внимание!",
                                  "Достигнут лимит по цветным меткам")
            message.setWindowIcon(QtGui.QIcon(":/icons/app.png"))
            message.exec_()
            return

        # Selecting color
        dialog = QColorDialog()
        dialog.exec_()
        color = dialog.selectedColor()
        # Adding mark
        self.marks_colors.append(color.name())
        current_mark = QWidget()
        current_mark.setMinimumSize(22, 5)
        current_mark.setMaximumHeight(8)
        current_mark.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        current_mark.setStyleSheet("QWidget {background: " + color.name() + ";}")
        self.hlayout_marks.insertWidget(1, current_mark)

    def delete_card(self, *args):
        """
        Method that delete current card
        :param args: Event data
        """
        self.group_parent.remove_card(self)

    def to_dict(self) -> dict:
        return {
                "title": self.title,
                "description": self.description,
                "marks_colors": self.marks_colors
        }


class QGroup(QWidget):
    def __init__(self, group_id: int, title='', cards=[], parent=None):
        super().__init__(parent)

        # Title of the group
        self.title = title
        # List of cards in group
        self.cards = cards
        # Id of current group
        self.group_id = group_id

        self.init_ui()

    def init_ui(self):
        # Widget with main layout
        self.group_widget_main = QWidget(self)

        # Title of the group
        self.lineEdit_title = QLineEdit(self.title)
        self.lineEdit_title.mouseDoubleClickEvent = lambda event: self.lineEdit_title.selectAll()
        self.lineEdit_title.focusInEvent = lambda event: None
        self.lineEdit_title.setStyleSheet("""
                                          QLineEdit { 
                                          margin-right: 8px;
                                          background:rgba(0, 0, 0, 0);
                                          color: rgba(255, 255, 255, 93%);
                                          border-style:None }""")
        self.lineEdit_title.setFont(QtGui.QFont("Nirmala UI", pointSize=12))
        self.lineEdit_title.setAlignment(Qt.AlignLeft | Qt.AlignCenter)
        self.lineEdit_title.setMaxLength(30)

        self.label_add_group = QLabel("+ Добавить ещё одну карточку")
        self.label_add_group.setFont(QtGui.QFont("Nirmala UI", pointSize=10))
        self.label_add_group.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.label_add_group.setStyleSheet("""
                                           QLabel { 
                                           color: rgba(255, 255, 255, 79%);
                                           padding: 4px 4px 4px 4px;
                                           }
                                           QLabel:hover {
                                           background: #302746;                                       
                                           }""")
        self.label_add_group.mousePressEvent = lambda event: self.add_card()

        # Layout with all cards of this group
        self.vlayout_cards = QVBoxLayout()
        self.vlayout_cards.setSpacing(6)
        for card_data in self.cards:
            widget_cart_current = QCard(self.vlayout_cards.count(),
                                        card_data.title,
                                        card_data.marks_colors,
                                        card_data.description,
                                        parent=self)
            self.vlayout_cards.addWidget(widget_cart_current)

        # Scroll area for displaying all widgets
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setFrameStyle(QFrame.NoFrame)
        self.scroll_area.setStyleSheet("QScrollArea{background:transparent;}")
        self.scroll_area.setAutoFillBackground(False)
        # Container for scroll area
        self.widget_cards_container = QWidget()
        self.widget_cards_container.setAutoFillBackground(False)
        self.widget_cards_container.setObjectName("widget_cards_container")
        self.widget_cards_container.setStyleSheet("""#widget_cards_container{
                                                  background:#241E35;
                                                  border-style: outset;
                                                  border-radius: 25px;}""")
        # Layout for container
        self.widget_cards_container.setLayout(self.vlayout_cards)
        self.scroll_area.setWidget(self.widget_cards_container)
        self.scroll_area.setWidgetResizable(True)

        # Combine all widgets to main layout
        self.vlayout_main = QVBoxLayout()
        self.vlayout_main.addWidget(self.lineEdit_title)
        self.vlayout_main.addWidget(self.scroll_area)
        self.vlayout_main.addWidget(self.label_add_group)
        self.vlayout_main.setAlignment(self.label_add_group, Qt.AlignLeft | Qt.AlignCenter)
        self.vlayout_main.setContentsMargins(5, 5, 5, 5)
        self.group_widget_main.setLayout(self.vlayout_main)

        # Layout with group_widget_main
        self.vlayout_group_container = QVBoxLayout()
        self.vlayout_group_container.addWidget(self.group_widget_main)
        self.setLayout(self.vlayout_group_container)

    def add_card(self, marks_colors=[], title="Без названия", description="Без описания") -> None:
        """
        Method add cart to QGroup
        :param title: Title for new card
        :param description: Description for card
        :param marks_colors: HEX colors for marks on card
        """
        card = QCard(len(self.cards), title=title,
                     marks_colors=list(marks_colors), description=description,
                     parent=self)
        # Append card in QGroup list
        self.cards.append(card)
        # Adding card to current group
        self.vlayout_cards.addWidget(card)

    def remove_card(self, card: QCard) -> None:
        if card in self.cards:
            # Remove card from QGroup list
            self.cards.remove(card)
            # Remove card from current group\
            self.vlayout_cards.removeWidget(card)
            card.setParent(None)
            self.vlayout_cards.update()
            del card

    def to_dict(self) -> dict:
        result = {
            "title": self.title,
            "cards": []
        }

        for card in self.cards:
            result["cards"].append(card.to_dict())

        return result

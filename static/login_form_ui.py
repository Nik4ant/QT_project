# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1163, 860)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/interface_images/icon_app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)
        main_window.setAutoFillBackground(False)
        main_window.setStyleSheet("")
        main_window.setIconSize(QtCore.QSize(25, 25))
        self.Form = QtWidgets.QWidget(main_window)
        self.Form.setStyleSheet("#Form {\n"
"    background: #2D2C3F;\n"
"}")
        self.Form.setObjectName("Form")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1171, 861))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hlayout_main = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hlayout_main.setContentsMargins(0, 0, 0, 0)
        self.hlayout_main.setSpacing(0)
        self.hlayout_main.setObjectName("hlayout_main")
        self.vlayout_left = QtWidgets.QVBoxLayout()
        self.vlayout_left.setContentsMargins(3, 2, 0, 2)
        self.vlayout_left.setSpacing(0)
        self.vlayout_left.setObjectName("vlayout_left")
        self.widget_left_background = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_left_background.setStyleSheet("background: #2D2C3F;")
        self.widget_left_background.setObjectName("widget_left_background")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.widget_left_background)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 2016, 851))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.vlayout_left_form = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.vlayout_left_form.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vlayout_left_form.setContentsMargins(0, 2, 0, 2)
        self.vlayout_left_form.setSpacing(5)
        self.vlayout_left_form.setObjectName("vlayout_left_form")
        self.vspaser_left_form_top_layout = QtWidgets.QHBoxLayout()
        self.vspaser_left_form_top_layout.setObjectName("vspaser_left_form_top_layout")
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vspaser_left_form_top_layout.addItem(spacerItem)
        self.vlayout_left_form.addLayout(self.vspaser_left_form_top_layout)
        self.widget_create_form_background = QtWidgets.QWidget(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_create_form_background.sizePolicy().hasHeightForWidth())
        self.widget_create_form_background.setSizePolicy(sizePolicy)
        self.widget_create_form_background.setMinimumSize(QtCore.QSize(340, 380))
        self.widget_create_form_background.setStyleSheet("#widget_create_form_background {\n"
"    border-style: outset;\n"
"    border-radius: 35px;\n"
"}\n"
"\n"
"* {\n"
"    background: #241E35;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    color: #FFFFFF;\n"
"    background: #38304D;\n"
"    border-style: outset;\n"
"    border-radius: 6px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 3px;\n"
"}\n"
"QLineEdit:focus {\n"
"    color: #FFFFFF;\n"
"    background: #59506d;\n"
"}")
        self.widget_create_form_background.setObjectName("widget_create_form_background")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.widget_create_form_background)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 40, 291, 291))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.vlayout_create_account_form = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.vlayout_create_account_form.setContentsMargins(0, 0, 0, 0)
        self.vlayout_create_account_form.setSpacing(4)
        self.vlayout_create_account_form.setObjectName("vlayout_create_account_form")
        self.label_create_account = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.label_create_account.setFont(font)
        self.label_create_account.setStyleSheet("color: #FFFFFF;\n"
"margin-bottom: 1em;")
        self.label_create_account.setAlignment(QtCore.Qt.AlignCenter)
        self.label_create_account.setObjectName("label_create_account")
        self.vlayout_create_account_form.addWidget(self.label_create_account)
        self.gridLayout_create_account_input = QtWidgets.QGridLayout()
        self.gridLayout_create_account_input.setContentsMargins(2, 0, 2, 3)
        self.gridLayout_create_account_input.setHorizontalSpacing(4)
        self.gridLayout_create_account_input.setVerticalSpacing(1)
        self.gridLayout_create_account_input.setObjectName("gridLayout_create_account_input")
        self.label_create_user_icon = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_create_user_icon.sizePolicy().hasHeightForWidth())
        self.label_create_user_icon.setSizePolicy(sizePolicy)
        self.label_create_user_icon.setMinimumSize(QtCore.QSize(39, 39))
        self.label_create_user_icon.setMaximumSize(QtCore.QSize(42, 42))
        self.label_create_user_icon.setStyleSheet("margin-right: 2px;")
        self.label_create_user_icon.setText("")
        self.label_create_user_icon.setPixmap(QtGui.QPixmap(":/icons/interface_images/icon_user.png"))
        self.label_create_user_icon.setObjectName("label_create_user_icon")
        self.gridLayout_create_account_input.addWidget(self.label_create_user_icon, 0, 1, 1, 1)
        self.label_create_key_icon = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_create_key_icon.sizePolicy().hasHeightForWidth())
        self.label_create_key_icon.setSizePolicy(sizePolicy)
        self.label_create_key_icon.setMinimumSize(QtCore.QSize(39, 39))
        self.label_create_key_icon.setMaximumSize(QtCore.QSize(42, 42))
        self.label_create_key_icon.setStyleSheet("margin-right: 2px;")
        self.label_create_key_icon.setText("")
        self.label_create_key_icon.setPixmap(QtGui.QPixmap(":/icons/interface_images/icon_key.png"))
        self.label_create_key_icon.setObjectName("label_create_key_icon")
        self.gridLayout_create_account_input.addWidget(self.label_create_key_icon, 1, 1, 1, 1)
        self.label_create_password = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_create_password.setFont(font)
        self.label_create_password.setStyleSheet("color: #FFFFFF;")
        self.label_create_password.setWordWrap(False)
        self.label_create_password.setObjectName("label_create_password")
        self.gridLayout_create_account_input.addWidget(self.label_create_password, 1, 0, 1, 1)
        self.label_create_login = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_create_login.setFont(font)
        self.label_create_login.setStyleSheet("color: #FFFFFF;")
        self.label_create_login.setWordWrap(False)
        self.label_create_login.setObjectName("label_create_login")
        self.gridLayout_create_account_input.addWidget(self.label_create_login, 0, 0, 1, 1)
        self.lineEdit_password_create_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lineEdit_password_create_input.setFont(font)
        self.lineEdit_password_create_input.setToolTipDuration(-1)
        self.lineEdit_password_create_input.setStyleSheet("")
        self.lineEdit_password_create_input.setText("")
        self.lineEdit_password_create_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_create_input.setPlaceholderText("")
        self.lineEdit_password_create_input.setClearButtonEnabled(True)
        self.lineEdit_password_create_input.setObjectName("lineEdit_password_create_input")
        self.gridLayout_create_account_input.addWidget(self.lineEdit_password_create_input, 1, 2, 1, 1)
        self.lineEdit_login_create_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lineEdit_login_create_input.setFont(font)
        self.lineEdit_login_create_input.setStyleSheet("")
        self.lineEdit_login_create_input.setText("")
        self.lineEdit_login_create_input.setPlaceholderText("")
        self.lineEdit_login_create_input.setClearButtonEnabled(True)
        self.lineEdit_login_create_input.setObjectName("lineEdit_login_create_input")
        self.gridLayout_create_account_input.addWidget(self.lineEdit_login_create_input, 0, 2, 1, 1)
        self.lineEdit_password_repeat_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lineEdit_password_repeat_input.setFont(font)
        self.lineEdit_password_repeat_input.setStyleSheet("")
        self.lineEdit_password_repeat_input.setText("")
        self.lineEdit_password_repeat_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_repeat_input.setPlaceholderText("")
        self.lineEdit_password_repeat_input.setClearButtonEnabled(True)
        self.lineEdit_password_repeat_input.setObjectName("lineEdit_password_repeat_input")
        self.gridLayout_create_account_input.addWidget(self.lineEdit_password_repeat_input, 3, 2, 1, 1)
        self.label_create_repeat_key_icon = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_create_repeat_key_icon.sizePolicy().hasHeightForWidth())
        self.label_create_repeat_key_icon.setSizePolicy(sizePolicy)
        self.label_create_repeat_key_icon.setMinimumSize(QtCore.QSize(39, 39))
        self.label_create_repeat_key_icon.setMaximumSize(QtCore.QSize(42, 42))
        self.label_create_repeat_key_icon.setStyleSheet("margin-right: 2px;")
        self.label_create_repeat_key_icon.setText("")
        self.label_create_repeat_key_icon.setPixmap(QtGui.QPixmap(":/icons/interface_images/icon_key.png"))
        self.label_create_repeat_key_icon.setObjectName("label_create_repeat_key_icon")
        self.gridLayout_create_account_input.addWidget(self.label_create_repeat_key_icon, 3, 1, 1, 1)
        self.label_create_repeat_password = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_create_repeat_password.setFont(font)
        self.label_create_repeat_password.setStyleSheet("color: #FFFFFF;")
        self.label_create_repeat_password.setWordWrap(False)
        self.label_create_repeat_password.setObjectName("label_create_repeat_password")
        self.gridLayout_create_account_input.addWidget(self.label_create_repeat_password, 3, 0, 1, 1)
        self.gridLayout_create_account_input.setColumnMinimumWidth(1, 42)
        self.vlayout_create_account_form.addLayout(self.gridLayout_create_account_input)
        self.button_create_account = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_create_account.sizePolicy().hasHeightForWidth())
        self.button_create_account.setSizePolicy(sizePolicy)
        self.button_create_account.setMinimumSize(QtCore.QSize(120, 30))
        self.button_create_account.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.button_create_account.setFont(font)
        self.button_create_account.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_create_account.setStyleSheet("#button_create_account {\n"
"    border-color: #0DF5E3;\n"
"    border-style: outset;\n"
"    border-radius: 5px;\n"
"\n"
"    padding-left: 2px;\n"
"    padding-right: 2px;\n"
"    padding-top: 2px;\n"
"    padding-bottom:  2px;\n"
"    margin-bottom: 8px;\n"
"\n"
"    background-color: #0DF5E3;\n"
"}\n"
"\n"
"#button_create_account::hover {\n"
"    background-color: #33D2C6;\n"
"}\n"
"\n"
"#button_create_account:pressed {\n"
"    background-color: #2EBEB2;\n"
"}")
        self.button_create_account.setAutoExclusive(False)
        self.button_create_account.setAutoDefault(False)
        self.button_create_account.setDefault(False)
        self.button_create_account.setFlat(False)
        self.button_create_account.setObjectName("button_create_account")
        self.vlayout_create_account_form.addWidget(self.button_create_account)
        self.label_sign_in = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_sign_in.setFont(font)
        self.label_sign_in.setStyleSheet("color: #FFFFFF;")
        self.label_sign_in.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sign_in.setOpenExternalLinks(False)
        self.label_sign_in.setObjectName("label_sign_in")
        self.vlayout_create_account_form.addWidget(self.label_sign_in)
        self.vlayout_left_form.addWidget(self.widget_create_form_background)
        self.vspaser_left_form_bottom_layout = QtWidgets.QHBoxLayout()
        self.vspaser_left_form_bottom_layout.setObjectName("vspaser_left_form_bottom_layout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vspaser_left_form_bottom_layout.addItem(spacerItem1)
        self.vlayout_left_form.addLayout(self.vspaser_left_form_bottom_layout)
        self.vlayout_left.addWidget(self.widget_left_background)
        self.hlayout_main.addLayout(self.vlayout_left)
        self.vlayout_midle = QtWidgets.QVBoxLayout()
        self.vlayout_midle.setContentsMargins(0, 2, 0, 2)
        self.vlayout_midle.setSpacing(0)
        self.vlayout_midle.setObjectName("vlayout_midle")
        self.widget_midle_background = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_midle_background.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2D2C3F, stop:1 #2D2C3F);")
        self.widget_midle_background.setObjectName("widget_midle_background")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget_midle_background)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 841))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vlayout_offline = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vlayout_offline.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vlayout_offline.setContentsMargins(3, 2, 3, 2)
        self.vlayout_offline.setSpacing(5)
        self.vlayout_offline.setObjectName("vlayout_offline")
        self.vspacer_offline_top_layout = QtWidgets.QHBoxLayout()
        self.vspacer_offline_top_layout.setObjectName("vspacer_offline_top_layout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 165, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vspacer_offline_top_layout.addItem(spacerItem2)
        self.vlayout_offline.addLayout(self.vspacer_offline_top_layout)
        self.label_ofline = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.label_ofline.setFont(font)
        self.label_ofline.setStyleSheet("color: #FFFFFF;\n"
"margin-bottom: 1em;")
        self.label_ofline.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ofline.setObjectName("label_ofline")
        self.vlayout_offline.addWidget(self.label_ofline)
        self.label_info = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        self.label_info.setFont(font)
        self.label_info.setStyleSheet("color: #CBC5CB;\n"
"margin-bottom: 1em;")
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.vlayout_offline.addWidget(self.label_info)
        self.button_continue_offline = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_continue_offline.sizePolicy().hasHeightForWidth())
        self.button_continue_offline.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.button_continue_offline.setFont(font)
        self.button_continue_offline.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_continue_offline.setStyleSheet("#button_continue_offline {\n"
"    border-color: #0DF5E3;\n"
"    border-style: outset;\n"
"    border-radius: 5px;\n"
"    \n"
"    padding-left: 2px;\n"
"    padding-right: 2px;\n"
"    padding-top: 2px;\n"
"    padding-bottom:  2px;\n"
"    margin-bottom: 8px;\n"
"    background-color: #0DF5E3;\n"
"}\n"
"\n"
"#button_continue_offline::hover {\n"
"    background-color: #33D2C6;\n"
"}\n"
"\n"
"#button_continue_offline:pressed {\n"
"    background-color: #2EBEB2;\n"
"}")
        self.button_continue_offline.setAutoDefault(False)
        self.button_continue_offline.setDefault(False)
        self.button_continue_offline.setFlat(False)
        self.button_continue_offline.setObjectName("button_continue_offline")
        self.vlayout_offline.addWidget(self.button_continue_offline)
        self.vspacer_offline_botton_layout = QtWidgets.QVBoxLayout()
        self.vspacer_offline_botton_layout.setObjectName("vspacer_offline_botton_layout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vspacer_offline_botton_layout.addItem(spacerItem3)
        self.vlayout_offline.addLayout(self.vspacer_offline_botton_layout)
        self.vlayout_midle.addWidget(self.widget_midle_background)
        self.hlayout_main.addLayout(self.vlayout_midle)
        self.vlayout_right = QtWidgets.QVBoxLayout()
        self.vlayout_right.setContentsMargins(0, 2, 3, 2)
        self.vlayout_right.setSpacing(0)
        self.vlayout_right.setObjectName("vlayout_right")
        self.widget_right_background = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget_right_background.setStyleSheet("background: #2D2C3F;")
        self.widget_right_background.setObjectName("widget_right_background")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.widget_right_background)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 2016, 851))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.vlayout_right_form = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.vlayout_right_form.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vlayout_right_form.setContentsMargins(0, 2, 0, 2)
        self.vlayout_right_form.setSpacing(5)
        self.vlayout_right_form.setObjectName("vlayout_right_form")
        self.vspaser_form_top_layout = QtWidgets.QHBoxLayout()
        self.vspaser_form_top_layout.setObjectName("vspaser_form_top_layout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vspaser_form_top_layout.addItem(spacerItem4)
        self.vlayout_right_form.addLayout(self.vspaser_form_top_layout)
        self.widget_login_form_background = QtWidgets.QWidget(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_login_form_background.sizePolicy().hasHeightForWidth())
        self.widget_login_form_background.setSizePolicy(sizePolicy)
        self.widget_login_form_background.setMinimumSize(QtCore.QSize(340, 380))
        self.widget_login_form_background.setStyleSheet("#widget_login_form_background {\n"
"    border-style: outset;\n"
"    border-radius: 35px;\n"
"}\n"
"\n"
"* {\n"
"    background: #241E35;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    color: #FFFFFF;\n"
"    background: #38304D;\n"
"    border-style: outset;\n"
"    border-radius: 6px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 3px;\n"
"}\n"
"QLineEdit:focus {\n"
"    background: #59506d;\n"
"}")
        self.widget_login_form_background.setObjectName("widget_login_form_background")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget_login_form_background)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 40, 281, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.vlayout_login_form = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vlayout_login_form.setContentsMargins(0, 0, 0, 0)
        self.vlayout_login_form.setSpacing(4)
        self.vlayout_login_form.setObjectName("vlayout_login_form")
        self.label_enter_account = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.label_enter_account.setFont(font)
        self.label_enter_account.setStyleSheet("color: #FFFFFF;\n"
"margin-bottom: 1em;")
        self.label_enter_account.setAlignment(QtCore.Qt.AlignCenter)
        self.label_enter_account.setObjectName("label_enter_account")
        self.vlayout_login_form.addWidget(self.label_enter_account)
        self.gridLayout_form_input = QtWidgets.QGridLayout()
        self.gridLayout_form_input.setContentsMargins(2, 0, 2, 3)
        self.gridLayout_form_input.setHorizontalSpacing(4)
        self.gridLayout_form_input.setVerticalSpacing(1)
        self.gridLayout_form_input.setObjectName("gridLayout_form_input")
        self.lineEdit_password_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lineEdit_password_input.setFont(font)
        self.lineEdit_password_input.setStyleSheet("")
        self.lineEdit_password_input.setText("")
        self.lineEdit_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_input.setPlaceholderText("")
        self.lineEdit_password_input.setClearButtonEnabled(True)
        self.lineEdit_password_input.setObjectName("lineEdit_password_input")
        self.gridLayout_form_input.addWidget(self.lineEdit_password_input, 1, 2, 1, 1)
        self.label_key_icon = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_key_icon.sizePolicy().hasHeightForWidth())
        self.label_key_icon.setSizePolicy(sizePolicy)
        self.label_key_icon.setMinimumSize(QtCore.QSize(39, 39))
        self.label_key_icon.setMaximumSize(QtCore.QSize(42, 42))
        self.label_key_icon.setStyleSheet("margin-right: 2px;")
        self.label_key_icon.setText("")
        self.label_key_icon.setPixmap(QtGui.QPixmap(":/icons/interface_images/icon_key.png"))
        self.label_key_icon.setObjectName("label_key_icon")
        self.gridLayout_form_input.addWidget(self.label_key_icon, 1, 1, 1, 1)
        self.label_password = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet("color: #FFFFFF;")
        self.label_password.setWordWrap(False)
        self.label_password.setObjectName("label_password")
        self.gridLayout_form_input.addWidget(self.label_password, 1, 0, 1, 1)
        self.label_login = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet("color: #FFFFFF;")
        self.label_login.setWordWrap(False)
        self.label_login.setObjectName("label_login")
        self.gridLayout_form_input.addWidget(self.label_login, 0, 0, 1, 1)
        self.label_user_icon = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy)
        self.label_user_icon.setMinimumSize(QtCore.QSize(39, 39))
        self.label_user_icon.setMaximumSize(QtCore.QSize(42, 42))
        self.label_user_icon.setStyleSheet("margin-right: 2px;")
        self.label_user_icon.setText("")
        self.label_user_icon.setPixmap(QtGui.QPixmap(":/icons/interface_images/icon_user.png"))
        self.label_user_icon.setObjectName("label_user_icon")
        self.gridLayout_form_input.addWidget(self.label_user_icon, 0, 1, 1, 1)
        self.lineEdit_login_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lineEdit_login_input.setFont(font)
        self.lineEdit_login_input.setStyleSheet("")
        self.lineEdit_login_input.setText("")
        self.lineEdit_login_input.setFrame(True)
        self.lineEdit_login_input.setPlaceholderText("")
        self.lineEdit_login_input.setClearButtonEnabled(True)
        self.lineEdit_login_input.setObjectName("lineEdit_login_input")
        self.gridLayout_form_input.addWidget(self.lineEdit_login_input, 0, 2, 1, 1)
        self.vlayout_login_form.addLayout(self.gridLayout_form_input)
        self.button_enter = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button_enter.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_enter.sizePolicy().hasHeightForWidth())
        self.button_enter.setSizePolicy(sizePolicy)
        self.button_enter.setMinimumSize(QtCore.QSize(120, 30))
        self.button_enter.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        self.button_enter.setFont(font)
        self.button_enter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_enter.setStyleSheet("#button_enter {\n"
"    border-color: #0DF5E3;\n"
"    border-style: outset;\n"
"    border-radius: 5px;\n"
"\n"
"    padding-left: 2px;\n"
"    padding-right: 2px;\n"
"    padding-top: 2px;\n"
"    padding-bottom:  2px;\n"
"    margin-bottom: 8px;\n"
"\n"
"    background-color: #0DF5E3;\n"
"}\n"
"\n"
"#button_enter::hover {\n"
"    background-color: #33D2C6;\n"
"}\n"
"\n"
"#button_enter:pressed {\n"
"    background-color: #2EBEB2;\n"
"}")
        self.button_enter.setAutoExclusive(False)
        self.button_enter.setAutoDefault(False)
        self.button_enter.setDefault(False)
        self.button_enter.setFlat(False)
        self.button_enter.setObjectName("button_enter")
        self.vlayout_login_form.addWidget(self.button_enter)
        self.label_sign_up = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_sign_up.setFont(font)
        self.label_sign_up.setStyleSheet("color: #FFFFFF;")
        self.label_sign_up.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sign_up.setOpenExternalLinks(False)
        self.label_sign_up.setObjectName("label_sign_up")
        self.vlayout_login_form.addWidget(self.label_sign_up)
        self.label_accaunt_info = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.label_accaunt_info.setFont(font)
        self.label_accaunt_info.setStyleSheet("color: #CBC5CB;\n"
"margin-top: 1em;")
        self.label_accaunt_info.setTextFormat(QtCore.Qt.AutoText)
        self.label_accaunt_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_accaunt_info.setWordWrap(True)
        self.label_accaunt_info.setObjectName("label_accaunt_info")
        self.vlayout_login_form.addWidget(self.label_accaunt_info)
        self.vlayout_login_form.setStretch(1, 1)
        self.vlayout_login_form.setStretch(2, 1)
        self.vlayout_right_form.addWidget(self.widget_login_form_background)
        self.vspaser_form_bottom_layout = QtWidgets.QHBoxLayout()
        self.vspaser_form_bottom_layout.setObjectName("vspaser_form_bottom_layout")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vspaser_form_bottom_layout.addItem(spacerItem5)
        self.vlayout_right_form.addLayout(self.vspaser_form_bottom_layout)
        self.vlayout_right.addWidget(self.widget_right_background)
        self.hlayout_main.addLayout(self.vlayout_right)
        main_window.setCentralWidget(self.Form)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        main_window.setTabOrder(self.lineEdit_login_input, self.lineEdit_password_input)
        main_window.setTabOrder(self.lineEdit_password_input, self.button_enter)
        main_window.setTabOrder(self.button_enter, self.lineEdit_login_create_input)
        main_window.setTabOrder(self.lineEdit_login_create_input, self.lineEdit_password_create_input)
        main_window.setTabOrder(self.lineEdit_password_create_input, self.lineEdit_password_repeat_input)
        main_window.setTabOrder(self.lineEdit_password_repeat_input, self.button_create_account)
        main_window.setTabOrder(self.button_create_account, self.button_continue_offline)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Yello"))
        self.label_create_account.setText(_translate("main_window", "Создать аккаунт"))
        self.label_create_password.setText(_translate("main_window", "Пароль"))
        self.label_create_login.setText(_translate("main_window", "Логин"))
        self.label_create_repeat_password.setText(_translate("main_window", "Подтверждение"))
        self.button_create_account.setText(_translate("main_window", "Создать"))
        self.label_sign_in.setText(_translate("main_window", "Есть аккаунт - войди в него"))
        self.label_ofline.setText(_translate("main_window", "Работать офлайн"))
        self.label_info.setText(_translate("main_window", "Нажимая кнопку продолжить, вы соглашаетесь\n"
"на сохранение файлов вашего прогресса\n"
"в одной директории с программой."))
        self.button_continue_offline.setText(_translate("main_window", "Продолжить"))
        self.label_enter_account.setText(_translate("main_window", "Войти в аккаунт"))
        self.label_password.setText(_translate("main_window", "Пароль"))
        self.label_login.setText(_translate("main_window", "Логин"))
        self.button_enter.setText(_translate("main_window", "Войти"))
        self.label_sign_up.setText(_translate("main_window", "Нет аккаунта - создай его"))
        self.label_accaunt_info.setText(_translate("main_window", "<html><head/><body><p>Нажимая кнопку войти, вы соглашаетесь на хранение файлов программы в одной директории с программой</p></body></html>"))

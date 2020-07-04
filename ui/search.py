# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
import sys
import register
import login
import register_win
import register_fail
import jump_buy
import add_flight, change_flight, mytickets, change_fly


class Register_Window(QDialog, register.Ui_Dialog):
    def __init__(self, parent=None):
        super(Register_Window, self).__init__(parent)
        self.setupUi(self)

class Change_Fly_Window(QDialog, change_fly.Ui_Dialog):
    def __init__(self, parent=None):
        super(Change_Fly_Window, self).__init__(parent)
        self.setupUi(self)

class Change_Flight_Window(QDialog, change_flight.Ui_Dialog):
    def __init__(self, parent=None):
        super(Change_Flight_Window, self).__init__(parent)
        self.setupUi(self)

class MyTickets_Window(QDialog, mytickets.Ui_Mytickets):
    def __init__(self, parent=None):
        super(MyTickets_Window, self).__init__(parent)
        self.setupUi(self)


class Login_Window(QDialog, login.Ui_Dialog):
    def __init__(self, parent=None):
        super(Login_Window, self).__init__(parent)
        self.setupUi(self)


class Jump_Buy_Window(QDialog, jump_buy.Ui_Dialog_jump_buy):
    def __init__(self, parent=None):
        super(Jump_Buy_Window, self).__init__(parent)
        self.setupUi(self)


class Add_Flight_Window(QDialog, add_flight.Ui_Dialog):
    def __init__(self, parent=None):
        super(Add_Flight_Window, self).__init__(parent)
        self.setupUi(self)


class Ui_MainWindow(object):
    state = -1  # 选中的票的状态，0为出发-目的，1为出发-经停，2为经停-目的，-1为未被选中
    username = ''
    num = -1  # 选中航程号
    index = -1
    power = 0  # 权限0为未登录，1为用户，2为管理员

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setMinimumSize(QtCore.QSize(567, 384))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("flight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_departure = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_departure.sizePolicy().hasHeightForWidth())
        self.label_departure.setSizePolicy(sizePolicy)
        self.label_departure.setAlignment(QtCore.Qt.AlignCenter)
        self.label_departure.setObjectName("label_departure")
        self.horizontalLayout_2.addWidget(self.label_departure)
        self.comboBox_departure = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_departure.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_departure.sizePolicy().hasHeightForWidth())
        self.comboBox_departure.setSizePolicy(sizePolicy)
        self.comboBox_departure.setEditable(False)
        self.comboBox_departure.setObjectName("comboBox_departure")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.comboBox_departure.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_departure)
        self.label_destination = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_destination.sizePolicy().hasHeightForWidth())
        self.label_destination.setSizePolicy(sizePolicy)
        self.label_destination.setAlignment(QtCore.Qt.AlignCenter)
        self.label_destination.setObjectName("label_destination")
        self.horizontalLayout_2.addWidget(self.label_destination)
        self.comboBox_destination = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_destination.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_destination.sizePolicy().hasHeightForWidth())
        self.comboBox_destination.setSizePolicy(sizePolicy)
        self.comboBox_destination.setEditable(False)
        self.comboBox_destination.setObjectName("comboBox_destination")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.comboBox_destination.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_destination)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_date.sizePolicy().hasHeightForWidth())
        self.label_date.setSizePolicy(sizePolicy)
        self.label_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date.setObjectName("label_date")
        self.horizontalLayout_4.addWidget(self.label_date)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_4.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_class = QtWidgets.QLabel(self.centralwidget)
        self.label_class.setAlignment(QtCore.Qt.AlignCenter)
        self.label_class.setObjectName("label_class")
        self.horizontalLayout_5.addWidget(self.label_class)
        self.comboBox_class = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_class.setObjectName("comboBox_class")
        self.comboBox_class.addItem("")
        self.comboBox_class.addItem("")
        self.comboBox_class.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_class)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.Search = QtWidgets.QPushButton(self.centralwidget)
        self.Search.setObjectName("Search")
        self.verticalLayout.addWidget(self.Search)
        self.pushbutton_buy = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_buy.setObjectName("pushbutton_buy")
        self.verticalLayout.addWidget(self.pushbutton_buy)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_departure_arrival = QtWidgets.QLabel(self.centralwidget)
        self.label_departure_arrival.setObjectName("label_departure_arrival")
        self.verticalLayout_2.addWidget(self.label_departure_arrival)
        self.tableView_departure_arrival = QtWidgets.QTableView(self.centralwidget)
        self.tableView_departure_arrival.setObjectName("tableView_departure_arrival")
        self.verticalLayout_2.addWidget(self.tableView_departure_arrival)
        self.label_departure_transit = QtWidgets.QLabel(self.centralwidget)
        self.label_departure_transit.setObjectName("label_departure_transit")
        self.verticalLayout_2.addWidget(self.label_departure_transit)
        self.tableView_departure_transit = QtWidgets.QTableView(self.centralwidget)
        self.tableView_departure_transit.setObjectName("tableView_departure_transit")
        self.verticalLayout_2.addWidget(self.tableView_departure_transit)
        self.label_transit_arrival = QtWidgets.QLabel(self.centralwidget)
        self.label_transit_arrival.setObjectName("label_transit_arrival")
        self.verticalLayout_2.addWidget(self.label_transit_arrival)
        self.tableView_transit_destination = QtWidgets.QTableView(self.centralwidget)
        self.tableView_transit_destination.setObjectName("tableView_transit_destination")
        self.verticalLayout_2.addWidget(self.tableView_transit_destination)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 21))
        self.menubar.setObjectName("menubar")
        self.menu_register_login = QtWidgets.QMenu(self.menubar)
        self.menu_register_login.setObjectName("menu_register_login")
        self.menu_function = QtWidgets.QMenu(self.menubar)
        self.menu_function.setObjectName("menu_function")
        self.menu_user = QtWidgets.QMenu(self.menu_function)
        self.menu_user.setObjectName("menu_user")
        self.menu_administrator = QtWidgets.QMenu(self.menu_function)
        self.menu_administrator.setEnabled(True)
        self.menu_administrator.setObjectName("menu_administrator")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionregister = QtWidgets.QAction(MainWindow)
        self.actionregister.setObjectName("actionregister")
        self.actionbuy = QtWidgets.QAction(MainWindow)
        self.actionbuy.setObjectName("actionbuy")
        self.action_buy = QtWidgets.QAction(MainWindow)
        self.action_buy.setObjectName("action_buy")
        self.actiond_my_ticket = QtWidgets.QAction(MainWindow)
        self.actiond_my_ticket.setObjectName("actiond_my_ticket")
        self.action_add_flight = QtWidgets.QAction(MainWindow)
        self.action_add_flight.setEnabled(True)
        self.action_add_flight.setObjectName("action_add_flight")
        self.actionlogin = QtWidgets.QAction(MainWindow)
        self.actionlogin.setObjectName("actionlogin")
        self.action_alter_flight = QtWidgets.QAction(MainWindow)
        self.action_alter_flight.setObjectName("action_alter_flight")
        self.actionquit = QtWidgets.QAction(MainWindow)
        self.actionquit.setObjectName("actionquit")
        self.actionchangefly = QtWidgets.QAction(MainWindow)
        self.actionchangefly.setObjectName("actionchangefly")
        self.menu_register_login.addAction(self.actionregister)
        self.menu_register_login.addAction(self.actionlogin)
        self.menu_register_login.addAction(self.actionquit)
        self.menu_user.addAction(self.action_buy)
        self.menu_user.addAction(self.actiond_my_ticket)
        self.menu_administrator.addAction(self.action_add_flight)
        self.menu_administrator.addAction(self.action_alter_flight)
        self.menu_administrator.addAction(self.actionchangefly)
        self.menu_function.addAction(self.menu_user.menuAction())
        self.menu_function.addSeparator()
        self.menu_function.addAction(self.menu_administrator.menuAction())
        self.menubar.addAction(self.menu_register_login.menuAction())
        self.menubar.addAction(self.menu_function.menuAction())

        self.retranslateUi(MainWindow)
        self.actionquit.triggered.connect(self.quit_login)
        self.action_alter_flight.triggered.connect(self.open_change_flight)
        self.Search.clicked.connect(self.searchresult)
        self.actiond_my_ticket.triggered.connect(self.open_mytickets)
        # self.login.clicked.connect(self.open_login)
        self.pushbutton_buy.clicked.connect(self.jump_buy)
        self.actionregister.triggered.connect(self.open_register)
        self.actionlogin.triggered.connect(self.open_login)
        # self.register_2.clicked.connect(self.open_register)
        self.action_add_flight.triggered.connect(self.open_add_flight)
        self.tableView_departure_arrival.clicked.connect(self.da)
        self.tableView_departure_transit.clicked.connect(self.dt)
        self.tableView_transit_destination.clicked.connect(self.ta)
        self.tableView_departure_arrival.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_transit_destination.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_departure_transit.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.actionchangefly.triggered.connect(self.open_change_fly)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def searchresult(self):
        self.state = -1
        query_flight_dt = QSqlQuery()
        query_flight_dt.prepare('SELECT 航班编号 FROM 航班 '
                                'WHERE 航班.出发机场代码 in (SELECT 机场代码 FROM 机场 where 所在城市 = :departure) '
                                'and 航班.经停机场代码 in (SELECT 机场代码 FROM 机场 where 所在城市 = :destination)')
        query_flight_dt.bindValue(":departure", self.comboBox_departure.currentText())
        query_flight_dt.bindValue(":destination", self.comboBox_destination.currentText())  # 绑定占位符和相应的功能
        query_flight_dt.exec_()
        flight_dt = '('
        while query_flight_dt.next():
            flight_dt += "'" + query_flight_dt.value(0) + "'"
            if query_flight_dt.next():
                flight_dt += ","
                query_flight_dt.previous()
        flight_dt += ")"  # flight ： (A, B, ....)

        self.model1 = QSqlTableModel()
        self.tableView_departure_transit.setModel(self.model1)
        self.model1.setTable('飞行计划安排')
        self.model1.setFilter("航班编号 in %s and DATEDIFF(DAYOFYEAR, '%s', 计划出发时间) = 0 and [%s（开始-经停）剩余座位] > 0 "
                              % (flight_dt, self.dateEdit.date().toString("yyyy-MM-dd"),
                                 self.comboBox_class.currentText()))
        self.model1.select()

        self.tableView_departure_transit.hideColumn(4)
        self.tableView_departure_transit.hideColumn(5)
        self.tableView_departure_transit.hideColumn(6)
        self.tableView_departure_transit.hideColumn(7)
        self.tableView_departure_transit.hideColumn(8)
        self.tableView_departure_transit.hideColumn(9)
        self.tableView_departure_transit.hideColumn(10)
        self.tableView_departure_transit.hideColumn(11)
        self.tableView_departure_transit.hideColumn(15)
        self.tableView_departure_transit.hideColumn(17)
        self.tableView_departure_transit.hideColumn(18)
        self.tableView_departure_transit.hideColumn(20)
        self.tableView_departure_transit.hideColumn(21)
        self.tableView_departure_transit.hideColumn(23)
        if self.comboBox_class.currentText() == "头等舱":
            self.tableView_departure_transit.hideColumn(16)
            self.tableView_departure_transit.hideColumn(19)
            self.tableView_departure_transit.hideColumn(12)
            self.tableView_departure_transit.hideColumn(13)
        elif self.comboBox_class.currentText() == "经济舱":
            self.tableView_departure_transit.hideColumn(19)
            self.tableView_departure_transit.hideColumn(22)
            self.tableView_departure_transit.hideColumn(13)
            self.tableView_departure_transit.hideColumn(14)
        else:
            self.tableView_departure_transit.hideColumn(16)
            self.tableView_departure_transit.hideColumn(22)
            self.tableView_departure_transit.hideColumn(12)
            self.tableView_departure_transit.hideColumn(14)

        self.tableView_departure_transit.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_departure_transit.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.tableView_departure_transit.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.tableView_departure_transit.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
        self.tableView_departure_transit.horizontalHeader().setSectionResizeMode(3, QHeaderView.Interactive)
        self.tableView_departure_transit.setColumnWidth(0, 90)
        self.tableView_departure_transit.setColumnWidth(1, 90)
        self.tableView_departure_transit.setColumnWidth(2, 200)
        self.tableView_departure_transit.setColumnWidth(3, 210)
        self.tableView_departure_transit.show()

        query_flight = QSqlQuery()  # 新建QSqlQuery对象
        query_flight.prepare('SELECT 航班编号 FROM 航班 '
                             'WHERE 航班.出发机场代码 in (SELECT 机场代码 FROM 机场 where 所在城市 = :departure) '
                             'and 航班.到达机场代码 in (SELECT 机场代码 FROM 机场 where 所在城市 = :destination)')  # 输入SQL语句
        query_flight.bindValue(":departure", self.comboBox_departure.currentText())
        query_flight.bindValue(":destination", self.comboBox_destination.currentText())  # 绑定占位符和相应的功能
        query_flight.exec_()  # 执行
        flight = "("
        while query_flight.next():
            flight += "'" + query_flight.value(0) + "'"
            if query_flight.next():
                flight += ","
                query_flight.previous()
        flight += ")"  # flight ： (A, B, ....)

        self.model = QSqlTableModel()  # 新建SQLTableModel 对象
        self.tableView_departure_arrival.setModel(self.model)  # 绑定到tableView对象上
        self.model.setTable('飞行计划安排')  # 相当于 from 语句
        self.model.setFilter("航班编号 in %s and DATEDIFF(DAYOFYEAR, '%s', 计划出发时间) = 0 and [%s（开始-到达）剩余座位] > 0 "
                             % (flight, self.dateEdit.date().toString("yyyy-MM-dd"),
                                self.comboBox_class.currentText()))  # 相当于where语句
        # self.model.setFilter("DATEDIFF(DAYOFYEAR, '%s', 计划出发时间) = 0" % (self.dateEdit.date().toString("yyyy-MM-dd") ))

        # print(self.model.filter())
        self.model.select()  # 执行SQL select
        self.tableView_departure_arrival.hideColumn(3)
        self.tableView_departure_arrival.hideColumn(4)
        self.tableView_departure_arrival.hideColumn(9)
        self.tableView_departure_arrival.hideColumn(10)
        self.tableView_departure_arrival.hideColumn(11)
        self.tableView_departure_arrival.hideColumn(12)
        self.tableView_departure_arrival.hideColumn(13)
        self.tableView_departure_arrival.hideColumn(14)
        self.tableView_departure_arrival.hideColumn(16)
        self.tableView_departure_arrival.hideColumn(17)
        self.tableView_departure_arrival.hideColumn(19)
        self.tableView_departure_arrival.hideColumn(20)
        self.tableView_departure_arrival.hideColumn(22)
        self.tableView_departure_arrival.hideColumn(23)
        if self.comboBox_class.currentText() == "头等舱":
            self.tableView_departure_arrival.hideColumn(15)
            self.tableView_departure_arrival.hideColumn(18)
            self.tableView_departure_arrival.hideColumn(6)
            self.tableView_departure_arrival.hideColumn(7)
        elif self.comboBox_class.currentText() == "经济舱":
            self.tableView_departure_arrival.hideColumn(21)
            self.tableView_departure_arrival.hideColumn(18)
            self.tableView_departure_arrival.hideColumn(7)
            self.tableView_departure_arrival.hideColumn(8)
        else:
            self.tableView_departure_arrival.hideColumn(15)
            self.tableView_departure_arrival.hideColumn(21)
            self.tableView_departure_arrival.hideColumn(6)
            self.tableView_departure_arrival.hideColumn(8)

        # self.tableView_departure_arrival.setColumnWidth(3,200)
        self.tableView_departure_arrival.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_departure_arrival.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.tableView_departure_arrival.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.tableView_departure_arrival.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
        self.tableView_departure_arrival.horizontalHeader().setSectionResizeMode(5, QHeaderView.Interactive)
        self.tableView_departure_arrival.setColumnWidth(0, 90)
        self.tableView_departure_arrival.setColumnWidth(1, 90)
        self.tableView_departure_arrival.setColumnWidth(2, 200)
        self.tableView_departure_arrival.setColumnWidth(5, 190)

        self.tableView_departure_arrival.show()  # 显示

        query_flight_ta = QSqlQuery()
        query_flight_ta.prepare('SELECT 航班编号 FROM 航班 '
                                'WHERE 航班.经停机场代码 in (SELECT 机场代码 FROM 机场 where 所在城市 = :departure) '
                                'and 航班.到达机场代码 in (SELECT 机场代码 FROM 机场 where 所在城市 = :destination)')
        query_flight_ta.bindValue(":departure", self.comboBox_departure.currentText())
        query_flight_ta.bindValue(":destination", self.comboBox_destination.currentText())  # 绑定占位符和相应的功能
        query_flight_ta.exec_()
        flight_ta = '('
        while query_flight_ta.next():
            flight_ta += "'" + query_flight_ta.value(0) + "'"
            if query_flight_ta.next():
                flight_ta += ","
                query_flight_ta.previous()
        flight_ta += ")"  # flight ： (A, B, ....)
        # print (flight_ta)

        self.model2 = QSqlTableModel()
        self.tableView_transit_destination.setModel(self.model2)
        self.model2.setTable('飞行计划安排')
        self.model2.setFilter("航班编号 in %s and DATEDIFF(DAYOFYEAR, '%s', 计划出发时间) = 0 and [%s（经停-到达）剩余座位] > 0 "
                              % (flight_ta, self.dateEdit.date().toString("yyyy-MM-dd"),
                                 self.comboBox_class.currentText()))
        # print(self.model2.filter())
        self.model2.select()

        self.tableView_transit_destination.hideColumn(2)
        self.tableView_transit_destination.hideColumn(3)
        self.tableView_transit_destination.hideColumn(6)
        self.tableView_transit_destination.hideColumn(7)
        self.tableView_transit_destination.hideColumn(8)
        self.tableView_transit_destination.hideColumn(12)
        self.tableView_transit_destination.hideColumn(13)
        self.tableView_transit_destination.hideColumn(14)
        self.tableView_transit_destination.hideColumn(15)
        self.tableView_transit_destination.hideColumn(16)
        self.tableView_transit_destination.hideColumn(18)
        self.tableView_transit_destination.hideColumn(19)
        self.tableView_transit_destination.hideColumn(21)
        self.tableView_transit_destination.hideColumn(22)
        if self.comboBox_class.currentText() == "头等舱":
            self.tableView_transit_destination.hideColumn(17)
            self.tableView_transit_destination.hideColumn(20)
            self.tableView_transit_destination.hideColumn(9)
            self.tableView_transit_destination.hideColumn(10)
        elif self.comboBox_class.currentText() == "经济舱":
            self.tableView_transit_destination.hideColumn(20)
            self.tableView_transit_destination.hideColumn(23)
            self.tableView_transit_destination.hideColumn(10)
            self.tableView_transit_destination.hideColumn(11)
        else:
            self.tableView_transit_destination.hideColumn(17)
            self.tableView_transit_destination.hideColumn(23)
            self.tableView_transit_destination.hideColumn(9)
            self.tableView_transit_destination.hideColumn(11)
        #
        self.tableView_transit_destination.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_transit_destination.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.tableView_transit_destination.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.tableView_transit_destination.horizontalHeader().setSectionResizeMode(4, QHeaderView.Interactive)
        self.tableView_transit_destination.horizontalHeader().setSectionResizeMode(5, QHeaderView.Interactive)
        self.tableView_transit_destination.setColumnWidth(0, 90)
        self.tableView_transit_destination.setColumnWidth(1, 90)
        self.tableView_transit_destination.setColumnWidth(4, 230)
        self.tableView_transit_destination.setColumnWidth(5, 190)
        self.tableView_transit_destination.show()

        if self.model.rowCount()+self.model1.rowCount()+self.model2.rowCount() == 0:
            QMessageBox.information(self, "提示", "没有符合条件的航班!", QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "航空票务系统  -V 1.0.0"))
        self.label_departure.setText(_translate("MainWindow", "Departure"))
        self.comboBox_departure.setCurrentText(_translate("MainWindow", "北京"))
        self.comboBox_departure.setItemText(0, _translate("MainWindow", "北京"))
        self.comboBox_departure.setItemText(1, _translate("MainWindow", "成都"))
        self.comboBox_departure.setItemText(2, _translate("MainWindow", "香港"))
        self.comboBox_departure.setItemText(3, _translate("MainWindow", "哈尔滨"))
        self.comboBox_departure.setItemText(4, _translate("MainWindow", "海南"))
        self.comboBox_departure.setItemText(5, _translate("MainWindow", "上海"))
        self.comboBox_departure.setItemText(6, _translate("MainWindow", "长春"))
        self.comboBox_departure.setItemText(7, _translate("MainWindow", "兰州"))
        self.comboBox_departure.setItemText(8, _translate("MainWindow", "广州"))
        self.comboBox_departure.setItemText(9, _translate("MainWindow", "长沙"))
        self.comboBox_departure.setItemText(10, _translate("MainWindow", "南昌"))
        self.label_destination.setText(_translate("MainWindow", "Destination"))
        self.comboBox_destination.setItemText(0, _translate("MainWindow", "北京"))
        self.comboBox_destination.setItemText(1, _translate("MainWindow", "成都"))
        self.comboBox_destination.setItemText(2, _translate("MainWindow", "香港"))
        self.comboBox_destination.setItemText(3, _translate("MainWindow", "哈尔滨"))
        self.comboBox_destination.setItemText(4, _translate("MainWindow", "海南"))
        self.comboBox_destination.setItemText(5, _translate("MainWindow", "上海"))
        self.comboBox_destination.setItemText(6, _translate("MainWindow", "长春"))
        self.comboBox_destination.setItemText(7, _translate("MainWindow", "兰州"))
        self.comboBox_destination.setItemText(8, _translate("MainWindow", "广州"))
        self.comboBox_destination.setItemText(9, _translate("MainWindow", "长沙"))
        self.comboBox_destination.setItemText(10, _translate("MainWindow", "南昌"))
        self.label_date.setText(_translate("MainWindow", "DATE"))
        self.label_class.setText(_translate("MainWindow", "Class"))
        self.comboBox_class.setItemText(0, _translate("MainWindow", "头等舱"))
        self.comboBox_class.setItemText(1, _translate("MainWindow", "商务舱"))
        self.comboBox_class.setItemText(2, _translate("MainWindow", "经济舱"))
        self.Search.setText(_translate("MainWindow", "Search"))
        self.pushbutton_buy.setText(_translate("MainWindow", "Buy"))
        self.label_departure_arrival.setText(_translate("MainWindow", "出发 - 到达："))
        self.label_departure_transit.setText(_translate("MainWindow", "出发 - 经停："))
        self.label_transit_arrival.setText(_translate("MainWindow", "经停 - 到达："))
        self.menu_register_login.setTitle(_translate("MainWindow", "注册"))
        self.menu_function.setTitle(_translate("MainWindow", "功能"))
        self.menu_user.setTitle(_translate("MainWindow", "用户"))
        self.menu_administrator.setTitle(_translate("MainWindow", "管理员"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.actionregister.setText(_translate("MainWindow", "用户注册"))
        self.actionbuy.setText(_translate("MainWindow", "机票购买"))
        self.action_buy.setText(_translate("MainWindow", "机票购买"))
        self.actiond_my_ticket.setText(_translate("MainWindow", "我的机票"))
        self.action_add_flight.setText(_translate("MainWindow", "添加航程"))
        self.actionlogin.setText(_translate("MainWindow", "用户/管理员登录"))
        self.action_alter_flight.setText(_translate("MainWindow", "修改航程"))
        self.actionquit.setText(_translate("MainWindow", "退出登录"))
        self.actionchangefly.setText(_translate("MainWindow", "修改航班"))

    def open_mytickets(self):
        if (self.power != 1):
            reply = QMessageBox.warning(self, "消息框标题","请用户先登录后再查看购票历史！", QMessageBox.Ok)
        else:
            my_ticket = MyTickets_Window()
            my_ticket.username = self.username
            my_ticket.exec_()

    def quit_login(self):
        if self.power != 0:
            self.username = ''
            self.power = 0
            QMessageBox.information(self,
                            "提示",
                            "成功退出登录！",
                            QMessageBox.Ok)
        else:
            QMessageBox.warning(self,
                                "警告",
                                "您还未登录！",
                                QMessageBox.Ok)
            pass
        pass
    pass


    def open_change_fly(self):
        if self.power == 2:
           change_fly_window = Change_Fly_Window()
           change_fly_window.exec_()
        elif self.power == 0:
            QMessageBox.warning(self,
                                "警告",
                                "您还未登录，请登录后使用该功能！",
                                QMessageBox.Ok)
        elif self.power == 1:
            QMessageBox.warning(self,
                                "警告",
                                "您不具备管理员权限！",
                                QMessageBox.Ok)
            pass
        pass
    pass

    def open_change_flight(self):
        if self.power == 2:
           change_flight_window = Change_Flight_Window()
           change_flight_window.exec_()
        elif self.power == 0:
            QMessageBox.warning(self,
                                "警告",
                                "您还未登录，请登录后使用该功能！",
                                QMessageBox.Ok)
        elif self.power == 1:
            QMessageBox.warning(self,
                                "警告",
                                "您不具备管理员权限！",
                                QMessageBox.Ok)



    def open_login(self):
        login_window = Login_Window()
        login_window.exec_()
        self.username = login_window.username
        self.power = login_window.power


    def open_register(self):
        register_window = Register_Window()
        register_window.exec_()

    def open_add_flight(self):
        if self.power == 2:
            add_flight_window = Add_Flight_Window()
            add_flight_window.exec_()
        elif self.power == 0:
            QMessageBox.warning(self,
                                "警告",
                                "您还未登录，请登录后使用该功能！",
                                QMessageBox.Ok)
        elif self.power == 1:
            QMessageBox.warning(self,
                                "警告",
                                "您不具备管理员权限！",
                                QMessageBox.Ok)

    def jump_buy(self):
        if (self.power < 1):
            reply = QMessageBox.warning(self,
                                        "提示",
                                        "请先登录后再购票！",
                                        QMessageBox.Ok)
        elif (self.state == -1):
            reply = QMessageBox.warning(self,
                                        "提示",
                                        "请选取要买的票！",
                                        QMessageBox.Ok)
        else:
            jump_buy_window = Jump_Buy_Window()
            jump_buy_window.state = self.state
            jump_buy_window.num = self.num
            jump_buy_window.username = self.username
            jump_buy_window.exec_()
            self.state = -1

    def da(self):
        self.state = 0
        self.index = self.tableView_departure_arrival.currentIndex().row()
        # print(self.index)
        model = self.tableView_departure_arrival.model()
        index = model.index(self.index, 0)
        self.num = model.data(index)
        # print(data)

    def dt(self):
        self.state = 1
        self.index = self.tableView_departure_transit.currentIndex().row()
        # print(self.index)
        model = self.tableView_departure_transit.model()
        index = model.index(self.index, 0)
        self.num = model.data(index)

    def ta(self):
        self.state = 2
        self.index = self.tableView_transit_destination.currentIndex().row()
        # print(self.index)
        model = self.tableView_transit_destination.model()
        index = model.index(self.index, 0)
        self.num = model.data(index)

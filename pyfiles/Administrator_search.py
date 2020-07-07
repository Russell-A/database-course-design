# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Administrator_search.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtSql import QSqlTableModel, QSqlQueryModel
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1065, 323)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/flight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("\n"
                             "/**********主界面样式**********/\n"
                             "QWidget#Dialog {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: rgb(232, 241, 252);\n"
                             "}\n"
                             "\n"
                             "QWidget#messageWidget {\n"
                             "        background: rgba(173, 202, 232, 50%);\n"
                             "}\n"
                             "\n"
                             "QWidget#loadingWidget {\n"
                             "        border: none;\n"
                             "        border-radius: 5px;\n"
                             "        background: rgb(187, 212, 238);\n"
                             "}\n"
                             "\n"
                             "StyledWidget {\n"
                             "        qproperty-normalColor: rgb(65, 65, 65);\n"
                             "        qproperty-disableColor: rgb(180, 180, 180);\n"
                             "        qproperty-highlightColor: rgb(0, 160, 230);\n"
                             "        qproperty-errorColor: red;\n"
                             "}\n"
                             "\n"
                             "QProgressIndicator {\n"
                             "        qproperty-color: rgb(2, 65, 132);\n"
                             "}\n"
                             "\n"
                             "/**********表头**********/\n"
                             "QHeaderView{\n"
                             "        border: none;\n"
                             "        border-bottom: 3px solid rgb(0, 78, 161);\n"
                             "        background: transparent;\n"
                             "        min-height: 30px;\n"
                             "}\n"
                             "QHeaderView::section:horizontal {\n"
                             "        border: none;\n"
                             "        color: rgb(2, 65, 132);\n"
                             "        background: transparent;\n"
                             "        padding-left: 5px;\n"
                             "}\n"
                             "QHeaderView::section:horizontal:hover {\n"
                             "        color: white;\n"
                             "        background: rgb(0, 78, 161);\n"
                             "}\n"
                             "QHeaderView::section:horizontal:pressed {\n"
                             "        color: white;\n"
                             "        background: rgb(6, 94, 187);\n"
                             "}\n"
                             "QHeaderView::up-arrow {\n"
                             "        width: 13px;\n"
                             "        height: 11px;\n"
                             "        padding-right: 5px;\n"
                             "        image: url(:/White/topArrow);\n"
                             "        subcontrol-position: center right;\n"
                             "}\n"
                             "QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {\n"
                             "        image: url(:/White/topArrowHover);\n"
                             "}\n"
                             "QHeaderView::down-arrow {\n"
                             "        width: 13px;\n"
                             "        height: 11px;\n"
                             "        padding-right: 5px;\n"
                             "        image: url(:/White/bottomArrow);\n"
                             "        subcontrol-position: center right;\n"
                             "}\n"
                             "QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {\n"
                             "        image: url(:/White/bottomArrowHover);\n"
                             "}\n"
                             "\n"
                             "/**********表格**********/\n"
                             "QTableView {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: rgb(224, 238, 255);\n"
                             "        gridline-color: rgb(111, 156, 207);\n"
                             "}\n"
                             "QTableView::item {\n"
                             "        padding-left: 5px;\n"
                             "        padding-right: 5px;\n"
                             "        border: none;\n"
                             "        background: white;\n"
                             "        border-right: 1px solid rgb(111, 156, 207);\n"
                             "        border-bottom: 1px solid rgb(111, 156, 207);\n"
                             "}\n"
                             "QTableView::item:selected {\n"
                             "        background: rgba(255, 255, 255, 100);\n"
                             "}\n"
                             "QTableView::item:selected:!active {\n"
                             "        color: rgb(65, 65, 65);\n"
                             "}\n"
                             "QTableView::indicator {\n"
                             "        width: 20px;\n"
                             "        height: 20px;\n"
                             "}\n"
                             "\n"
                             "/**********状态栏**********/\n"
                             "QStatusBar {\n"
                             "        background: rgb(187, 212, 238);\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        border-left: none;\n"
                             "        border-right: none;\n"
                             "        border-bottom: none;\n"
                             "}\n"
                             "QStatusBar::item {\n"
                             "    border: none;\n"
                             "    border-right: 1px solid rgb(111, 156, 207);\n"
                             "}\n"
                             "\n"
                             "/**********分组框**********/\n"
                             "QGroupBox {\n"
                             "        font-size: 15px;\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        border-radius: 4px;\n"
                             "        margin-top: 10px;\n"
                             "}\n"
                             "QGroupBox::title {\n"
                             "        color: rgb(56, 99, 154);\n"
                             "        top: -12px;\n"
                             "        left: 10px;\n"
                             "}\n"
                             "\n"
                             "\n"
                             "\n"
                             "/**********单选框**********/\n"
                             "QRadioButton{\n"
                             "        spacing: 5px;\n"
                             "}\n"
                             "QRadioButton:enabled:checked{\n"
                             "        color: rgb(2, 65, 132);\n"
                             "}\n"
                             "QRadioButton:enabled:!checked{\n"
                             "        color: rgb(70, 71, 73);\n"
                             "}\n"
                             "QRadioButton:enabled:hover{\n"
                             "        color: rgb(0, 78, 161);\n"
                             "}\n"
                             "QRadioButton:!enabled{\n"
                             "        color: rgb(80, 80, 80);\n"
                             "}\n"
                             "QRadioButton::indicator {\n"
                             "        width: 20px;\n"
                             "        height: 20px;\n"
                             "}\n"
                             "/**********输入框**********/\n"
                             "QLineEdit {\n"
                             "        border-radius: 4px;\n"
                             "        height: 25px;\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: white;\n"
                             "}\n"
                             "QLineEdit:enabled {\n"
                             "        color: rgb(84, 84, 84);\n"
                             "}\n"
                             "QLineEdit:enabled:hover, QLineEdit:enabled:focus {\n"
                             "        color: rgb(51, 51, 51);\n"
                             "}\n"
                             "QLineEdit:!enabled {\n"
                             "        color: rgb(80, 80, 80);\n"
                             "}\n"
                             "\n"
                             "/**********文本编辑框**********/\n"
                             "QTextEdit {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        color: rgb(70, 71, 73);\n"
                             "        background: rgb(187, 212, 238);\n"
                             "}\n"
                             "\n"
                             "/**********滚动区域**********/\n"
                             "QScrollArea {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: rgb(187, 212, 238);\n"
                             "}\n"
                             "\n"
                             "/**********滚动区域**********/\n"
                             "QWidget#transparentWidget {\n"
                             "        background: transparent;\n"
                             "}\n"
                             "\n"
                             "\n"
                             "/**********标签**********/\n"
                             "QLabel#grayLabel {\n"
                             "        color: rgb(70, 71, 73);\n"
                             "}\n"
                             "\n"
                             "QLabel#highlightLabel {\n"
                             "        color: rgb(2, 65, 132);\n"
                             "}\n"
                             "\n"
                             "QLabel#redLabel {\n"
                             "        color: red;\n"
                             "}\n"
                             "\n"
                             "QLabel#grayYaHeiLabel {\n"
                             "        color: rgb(175, 175, 175);\n"
                             "        font-size: 16px;\n"
                             "}\n"
                             "\n"
                             "QLabel#blueLabel {\n"
                             "        color: rgb(0, 160, 230);\n"
                             "}\n"
                             "\n"
                             "QLabel#listLabel {\n"
                             "        color: rgb(51, 51, 51);\n"
                             "}\n"
                             "\n"
                             "QLabel#lineBlueLabel {\n"
                             "        background: rgb(0, 78, 161);\n"
                             "}\n"
                             "\n"
                             "QLabel#graySeperateLabel {\n"
                             "        background: rgb(200, 220, 230);\n"
                             "}\n"
                             "\n"
                             "QLabel#seperateLabel {\n"
                             "        background: rgb(112, 153, 194);\n"
                             "}\n"
                             "\n"
                             "QLabel#radiusBlueLabel {\n"
                             "        border-radius: 15px;\n"
                             "        color: black;\n"
                             "        background: rgb(0, 78, 161);\n"
                             "}\n"
                             "\n"
                             "/**********按钮**********/\n"
                             "QPushButton{\n"
                             "        border-radius: 4px;\n"
                             "        border: none;\n"
                             "        width: 75px;\n"
                             "        height: 25px;\n"
                             "}\n"
                             "QPushButton:enabled {\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton:!enabled {\n"
                             "        background: rgb(180, 180, 180);\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton:enabled:hover{\n"
                             "        background: rgb(100, 160, 220);\n"
                             "}\n"
                             "QPushButton:enabled:pressed{\n"
                             "        background: rgb(0, 78, 161);\n"
                             "}\n"
                             "\n"
                             "QPushButton#blueButton {\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton#blueButton:enabled {\n"
                             "        background: rgb(0, 78, 161);\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton:!enabled {\n"
                             "        background: rgb(180, 180, 180);\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton#blueButton:enabled:hover {\n"
                             "        background: rgb(2, 65, 132);\n"
                             "}\n"
                             "QPushButton#blueButton:enabled:pressed {\n"
                             "        background: rgb(6, 94, 187);\n"
                             "}\n"
                             "\n"
                             "QPushButton#selectButton {\n"
                             "        border: none;\n"
                             "        border-radius: none;\n"
                             "        border-left: 1px solid rgb(111, 156, 207);\n"
                             "        background: transparent;\n"
                             "        image: url(:/White/scan);\n"
                             "        color: rgb(51, 51, 51);\n"
                             "}\n"
                             "QPushButton#selectButton:enabled:hover{\n"
                             "        background: rgb(187, 212, 238);\n"
                             "}\n"
                             "QPushButton#selectButton:enabled:pressed{\n"
                             "        background: rgb(120, 170, 220);\n"
                             "}\n"
                             "\n"
                             "QPushButton#linkButton {\n"
                             "        background: transparent;\n"
                             "        color: rgb(0, 160, 230);\n"
                             "        text-align:left;\n"
                             "}\n"
                             "QPushButton#linkButton:hover {\n"
                             "        color: rgb(20, 185, 255);\n"
                             "        text-decoration: underline;\n"
                             "}\n"
                             "QPushButton#linkButton:pressed {\n"
                             "        color: rgb(0, 160, 230);\n"
                             "}\n"
                             "\n"
                             "QPushButton#transparentButton {\n"
                             "        background: transparent;\n"
                             "}\n"
                             "\n"
                             "/*****************标题栏按钮*******************/\n"
                             "QPushButton#minimizeButton {\n"
                             "        border-radius: none;\n"
                             "        border-bottom-left-radius: 4px;\n"
                             "        border-bottom-right-radius: 4px;\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        image: url(:/White/minimizeHover);\n"
                             "}\n"
                             "QPushButton#minimizeButton:hover {\n"
                             "        image: url(:/White/minimize);\n"
                             "}\n"
                             "QPushButton#minimizeButton:pressed {\n"
                             "        image: url(:/White/minimizePressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#maximizeButton[maximizeProperty=\"maximize\"] {\n"
                             "        border-radius: none;\n"
                             "        border-bottom-left-radius: 4px;\n"
                             "        border-bottom-right-radius: 4px;\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        image: url(:/White/maximizeHover);\n"
                             "}\n"
                             "QPushButton#maximizeButton[maximizeProperty=\"maximize\"]:hover {\n"
                             "        image: url(:/White/maximize);\n"
                             "}\n"
                             "QPushButton#maximizeButton[maximizeProperty=\"maximize\"]:pressed {\n"
                             "        image: url(:/White/maximizePressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#maximizeButton[maximizeProperty=\"restore\"] {\n"
                             "        border-radius: none;\n"
                             "        border-bottom-left-radius: 4px;\n"
                             "        border-bottom-right-radius: 4px;\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        image: url(:/White/restoreHover);\n"
                             "}\n"
                             "QPushButton#maximizeButton[maximizeProperty=\"restore\"]:hover {\n"
                             "        image: url(:/White/restore);\n"
                             "}\n"
                             "QPushButton#maximizeButton[maximizeProperty=\"restore\"]:pressed {\n"
                             "        image: url(:/White/restorePressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#closeButton {\n"
                             "        border-radius: none;\n"
                             "        border-bottom-left-radius: 4px;\n"
                             "        border-bottom-right-radius: 4px;\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        image: url(:/White/closeHover);\n"
                             "}\n"
                             "QPushButton#closeButton:hover {\n"
                             "        image: url(:/White/close);\n"
                             "}\n"
                             "QPushButton#closeButton:pressed {\n"
                             "        image: url(:/White/closePressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#skinButton {\n"
                             "        border-radius: none;\n"
                             "        border-bottom-left-radius: 4px;\n"
                             "        border-bottom-right-radius: 4px;\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        image: url(:/White/skinHover);\n"
                             "}\n"
                             "QPushButton#skinButton:hover {\n"
                             "        image: url(:/White/skin);\n"
                             "}\n"
                             "QPushButton#skinButton:pressed {\n"
                             "        image: url(:/White/skinPressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#feedbackButton {\n"
                             "        border-radius: none;\n"
                             "        border-bottom-left-radius: 4px;\n"
                             "        border-bottom-right-radius: 4px;\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        image: url(:/White/feedbackHover);\n"
                             "}\n"
                             "QPushButton#feedbackButton:hover {\n"
                             "        image: url(:/White/feedback);\n"
                             "}\n"
                             "QPushButton#feedbackButton:pressed {\n"
                             "        image: url(:/White/feedbackPressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#closeTipButton {\n"
                             "        border-radius: none;\n"
                             "        border-image: url(:/White/close);\n"
                             "        background: transparent;\n"
                             "}\n"
                             "QPushButton#closeTipButton:hover {\n"
                             "        border-image: url(:/White/closeHover);\n"
                             "}\n"
                             "QPushButton#closeTipButton:pressed {\n"
                             "        border-image: url(:/White/closePressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#changeSkinButton{\n"
                             "        border-radius: 4px;\n"
                             "        border: 2px solid rgb(111, 156, 207);\n"
                             "        background: rgb(204, 227, 252);\n"
                             "}\n"
                             "QPushButton#changeSkinButton:hover{\n"
                             "        border-color: rgb(60, 150, 200);\n"
                             "}\n"
                             "QPushButton#changeSkinButton:pressed, QPushButton#changeSkinButton:checked{\n"
                             "        border-color: rgb(0, 160, 230);\n"
                             "}\n"
                             "\n"
                             "QPushButton#transferButton {\n"
                             "        padding-left: 5px;\n"
                             "        padding-right: 5px;\n"
                             "        color: white;\n"
                             "        background: rgb(0, 78, 161);\n"
                             "}\n"
                             "QPushButton#transferButton:hover {\n"
                             "        background: rgb(2, 65, 132);\n"
                             "}\n"
                             "QPushButton#transferButton:pressed {\n"
                             "        background: rgb(6, 94, 187);\n"
                             "}\n"
                             "QPushButton#transferButton[iconProperty=\"left\"] {\n"
                             "        qproperty-icon: url(:/White/left);\n"
                             "}\n"
                             "QPushButton#transferButton[iconProperty=\"right\"] {\n"
                             "        qproperty-icon: url(:/White/right);\n"
                             "}\n"
                             "\n"
                             "QPushButton#openButton {\n"
                             "        border-radius: none;\n"
                             "        image: url(:/White/open);\n"
                             "        background: transparent;\n"
                             "}\n"
                             "QPushButton#openButton:hover {\n"
                             "        image: url(:/White/openHover);\n"
                             "}\n"
                             "QPushButton#openButton:pressed {\n"
                             "        image: url(:/White/openPressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#deleteButton {\n"
                             "        border-radius: none;\n"
                             "        image: url(:/White/delete);\n"
                             "        background: transparent;\n"
                             "}\n"
                             "QPushButton#deleteButton:hover {\n"
                             "        image: url(:/White/deleteHover);\n"
                             "}\n"
                             "QPushButton#deleteButton:pressed {\n"
                             "        image: url(:/White/deletePressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#menuButton {\n"
                             "        text-align: left center;\n"
                             "        padding-left: 3px;\n"
                             "        color: rgb(84, 84, 84);\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: white;\n"
                             "}\n"
                             "QPushButton#menuButton::menu-indicator{\n"
                             "        subcontrol-position: right center;\n"
                             "        subcontrol-origin: padding;\n"
                             "        image: url(:/White/arrowBottom);\n"
                             "        padding-right: 3px;\n"
                             "}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_flight_no = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_flight_no.sizePolicy().hasHeightForWidth())
        self.label_flight_no.setSizePolicy(sizePolicy)
        self.label_flight_no.setAcceptDrops(False)
        self.label_flight_no.setAlignment(QtCore.Qt.AlignCenter)
        self.label_flight_no.setObjectName("label_flight_no")
        self.horizontalLayout_3.addWidget(self.label_flight_no)
        self.lineEdit_flight_no = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_flight_no.sizePolicy().hasHeightForWidth())
        self.lineEdit_flight_no.setSizePolicy(sizePolicy)
        self.lineEdit_flight_no.setObjectName("lineEdit_flight_no")
        self.horizontalLayout_3.addWidget(self.lineEdit_flight_no)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.pushButton_search = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_search.sizePolicy().hasHeightForWidth())
        self.pushButton_search.setSizePolicy(sizePolicy)
        self.pushButton_search.setObjectName("pushButton_search")
        self.verticalLayout.addWidget(self.pushButton_search)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.tableView_search = QtWidgets.QTableView(Dialog)
        self.tableView_search.setObjectName("tableView_search")
        self.horizontalLayout_2.addWidget(self.tableView_search)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_search.clicked.connect(self.ad_search)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "乘客信息查询"))
        self.label_flight_no.setText(_translate("Dialog", "航程号："))
        self.pushButton_search.setText(_translate("Dialog", "查询"))

    def table_copy(self):
        flight_no = self.lineEdit_flight_no.text()
        query_copy = QSqlQuery()  # 新建sql对象
        query_copy.prepare('EXEC copy_table :flight_no')  # 输入SQL语句
        query_copy.bindValue(":flight_no", flight_no)  # 绑定占位符和相应的功能
        query_copy.exec_()
        #QMessageBox.information(self, "提示", "创建成功!", QMessageBox.Ok)

    #查询后删除所复制1的乘客信息
    def table_delete(self):
        query_delete = QSqlQuery()  # 新建sql对象
        query_delete.prepare('DROP TABLE 隐私查询')  # 输入SQL语句
        query_delete.exec_()
        # QMessageBox.information(self, "提示", "创建成功!", QMessageBox.Ok)

    #对于关键信息身份证号进行遮蔽
    def hide_search(self):
        query_hide = QSqlQuery()  # 新建sql对象
        query_hide.prepare("UPDATE 隐私查询 SET[乘客身份证号/护照号] = left([乘客身份证号/护照号], 6) + '********' + substring([乘客身份证号/护照号], 15, 18)")
        # 输入SQL语句
        query_hide.exec_()

    #差分隐私privacy difference指数机制保护用户类型信息
    #可用性函数敏感度为1，隐私预算设定为0.1 e值取2.71828
    def pd_search(self):
        query_pd = QSqlQuery()  # 新建sql对象
        query_pd.exec("EXEC pd_search")

    # def search_num_bound(self):
    #     search_num = self.lineEdit_flight_no.text()




    def ad_search(self):
        flight_no = self.lineEdit_flight_no.text()  # 设置航程号
        if flight_no == '':
            if not self.model.select():
                QtWidgets.QMessageBox.warning(self, "提示", "%s" % (self.model.lastError().text()),
                                              QtWidgets.QMessageBox.Ok)

        self.table_copy()#复制所需查询数据
        self.hide_search()#隐藏身份证号
        self.pd_search()#差分隐私保护用户类型信息

        self.model = QtSql.QSqlTableModel()
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.tableView_search.setModel(self.model)  # 绑定table
        self.model.setTable("隐私查询")


        self.model.setFilter("航程号 = %s" % (flight_no))
        if not self.model.select():
            QtWidgets.QMessageBox.warning(self, "提示", "%s" % (self.model.lastError().text()),
                                            QtWidgets.QMessageBox.Ok)
        self.tableView_search.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        if self.model.rowCount() == 0:
            QtWidgets.QMessageBox.information(self, "提示", "未找到符合条件的航程，请重试。", QtWidgets.QMessageBox.Ok)
        else:
            self.tableView_search.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            self.tableView_search.show()
        self.table_delete()

class Administrator_search_Window(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Administrator_search_Window, self).__init__(parent)
        self.setupUi(self)
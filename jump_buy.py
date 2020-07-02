# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jump_buy_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc


class Ui_Dialog_jump_buy(object):
    state = -1
    num = -1
    username = 'aa'
    def setupUi(self, Dialog_jump_buy):
        Dialog_jump_buy.setObjectName("Dialog_jump_buy")
        Dialog_jump_buy.resize(513, 430)
        Dialog_jump_buy.setFixedSize(513,430)
        self.pushButton = QtWidgets.QPushButton(Dialog_jump_buy)
        self.pushButton.setGeometry(QtCore.QRect(240, 334, 93, 28))
        self.pushButton.setMaximumSize(QtCore.QSize(93, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.name = QtWidgets.QLineEdit(Dialog_jump_buy)
        self.name.setGeometry(QtCore.QRect(240, 178, 131, 21))
        self.name.setMinimumSize(QtCore.QSize(131, 0))
        self.name.setMaximumSize(QtCore.QSize(131, 16777215))
        self.name.setMaxLength(100)
        self.name.setFrame(True)
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(Dialog_jump_buy)
        self.label.setGeometry(QtCore.QRect(69, 74, 78, 21))
        self.label.setMaximumSize(QtCore.QSize(125, 16777215))
        self.label.setObjectName("label")
        self.sex = QtWidgets.QComboBox(Dialog_jump_buy)
        self.sex.setGeometry(QtCore.QRect(240, 126, 78, 21))
        self.sex.setMaximumSize(QtCore.QSize(87, 16777215))
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.remain_num = QtWidgets.QLabel(Dialog_jump_buy)
        self.remain_num.setGeometry(QtCore.QRect(410, 74, 81, 21))
        self.remain_num.setMinimumSize(QtCore.QSize(81, 0))
        self.remain_num.setMaximumSize(QtCore.QSize(225, 16777215))
        self.remain_num.setText("")
        self.remain_num.setObjectName("remain_num")
        self.label_6 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_6.setGeometry(QtCore.QRect(69, 282, 75, 21))
        self.label_6.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_6.setObjectName("label_6")
        self.com_class = QtWidgets.QComboBox(Dialog_jump_buy)
        self.com_class.setGeometry(QtCore.QRect(154, 74, 87, 21))
        self.com_class.setMaximumSize(QtCore.QSize(87, 16777215))
        self.com_class.setObjectName("com_class")
        self.com_class.addItem("")
        self.com_class.addItem("")
        self.com_class.addItem("")
        self.label_5 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_5.setGeometry(QtCore.QRect(69, 230, 75, 21))
        self.label_5.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_4.setGeometry(QtCore.QRect(69, 126, 69, 21))
        self.label_4.setMaximumSize(QtCore.QSize(69, 16777215))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_2.setGeometry(QtCore.QRect(325, 74, 78, 21))
        self.label_2.setMaximumSize(QtCore.QSize(163, 16777215))
        self.label_2.setObjectName("label_2")
        self.phone_num = QtWidgets.QLineEdit(Dialog_jump_buy)
        self.phone_num.setGeometry(QtCore.QRect(240, 282, 189, 21))
        self.phone_num.setMaximumSize(QtCore.QSize(189, 16777215))
        self.phone_num.setObjectName("phone_num")
        self.label_3 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_3.setGeometry(QtCore.QRect(69, 178, 75, 21))
        self.label_3.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_3.setObjectName("label_3")
        self.identity_num = QtWidgets.QLineEdit(Dialog_jump_buy)
        self.identity_num.setGeometry(QtCore.QRect(240, 230, 189, 21))
        self.identity_num.setMinimumSize(QtCore.QSize(189, 0))
        self.identity_num.setMaximumSize(QtCore.QSize(189, 16777215))
        self.identity_num.setMaxLength(1000)
        self.identity_num.setObjectName("identity_num")

        self.retranslateUi(Dialog_jump_buy)

        self.pushButton.clicked.connect(self.insert_tacket)
        self.com_class.currentIndexChanged.connect(self.remain_tacket)
        QtCore.QMetaObject.connectSlotsByName(Dialog_jump_buy)

        # self.pushButton.clicked.connect(self.change)

    def retranslateUi(self, Dialog_jump_buy):
        _translate = QtCore.QCoreApplication.translate
        Dialog_jump_buy.setWindowTitle(_translate("Dialog_jump_buy", "Dialog"))
        self.pushButton.setText(_translate("Dialog_jump_buy", "购买"))
        self.label.setText(_translate("Dialog_jump_buy", "    舱位："))
        self.sex.setItemText(0, _translate("Dialog_jump_buy", "男"))
        self.sex.setItemText(1, _translate("Dialog_jump_buy", "女"))
        self.label_6.setText(_translate("Dialog_jump_buy", "联系电话："))
        self.com_class.setItemText(0, _translate("Dialog_jump_buy", "头等舱"))
        self.com_class.setItemText(1, _translate("Dialog_jump_buy", "商务舱"))
        self.com_class.setItemText(2, _translate("Dialog_jump_buy", "经济舱"))
        self.label_5.setText(_translate("Dialog_jump_buy", "身份证号："))
        self.label_4.setText(_translate("Dialog_jump_buy", "    性别："))
        self.label_2.setText(_translate("Dialog_jump_buy", "剩余票数："))
        self.label_3.setText(_translate("Dialog_jump_buy", "乘客姓名："))


    def insert_tacket(self):
        dairport = ''
        aairport = ''
        tacket_num = ()
        conn = pyodbc.connect(
            'DRIVER={SQL SERVER NATIVE CLIENT 10.0};SERVER=127.0.0.1;DATABASE=air;UID=sa;PWD=123456')
        if (self.state == 0):
            sql = "select *"\
                  " from 飞行计划安排 inner join 航班 on 飞行计划安排.航班编号 = 航班.航班编号"\
                  " inner join 机场 on 机场代码 = 出发机场代码"\
                  " inner join 机场 as b on b.机场代码 = 到达机场代码"\
                  " where 航程号 = ?"
            cursor = conn.cursor()
            result = (cursor.execute(sql, self.num).fetchall())
            dairport = result[0][29]
            aairport = result[0][32]
            tacket_num = result[0][6:9]
        if (self.state == 1):
            sql = "select *"\
                  " from 飞行计划安排 inner join 航班 on 飞行计划安排.航班编号 = 航班.航班编号"\
                  " inner join 机场 on 机场代码 = 出发机场代码"\
                  " inner join 机场 as b on b.机场代码 = 经停机场代码"\
                  " where 航程号 = ?"
            cursor = conn.cursor()
            result = (cursor.execute(sql, self.num).fetchall())
            dairport = result[0][29]
            aairport = result[0][32]
            tacket_num = result[0][12:15]
        if (self.state == 2):
            sql = "select *"\
                  " from 飞行计划安排 inner join 航班 on 飞行计划安排.航班编号 = 航班.航班编号"\
                  " inner join 机场 on 机场代码 = 出发机场代码"\
                  " inner join 机场 as b on b.机场代码 = 经停机场代码"\
                  " where 航程号 = ?"
            cursor = conn.cursor()
            result = (cursor.execute(sql, self.num).fetchall())
            dairport = result[0][29]
            aairport = result[0][32]
            tacket_num = result[0][9:12]
        kind = {}
        kind['经济舱'] = 0
        kind['商务舱'] = 1
        kind['头等舱'] = 2
        state_text = ['(开始-到达)','(开始-经停)','(经停-到达)']
        cart = self.com_class.currentText()

        print(tacket_num)

        tacket = tacket_num[kind[cart]]
        print(tacket)
        if (tacket is None):
            print('none')
            tacket = 0
        sex = self.sex.currentText()
        tele = self.phone_num.text()
        id = self.identity_num.text()
        name = self.name.text()
        if (len(name)<1 or len(id)<1 or len(tele)<1):
            reply = QMessageBox.warning(self,
                                        "消息框标题",
                                        "请先填写好信息！",
                                        QMessageBox.Yes | QMessageBox.No)
        elif (tacket>0):
            insert_sql = "insert into 订票 values (?,?,?,?,?,?,?,?,?,?,?)"
            result_in = cursor.execute(insert_sql, self.num, dairport, aairport, str(tacket), cart, self.username, name, sex, '成人', str(id), str(tele))
            cursor.commit()
            print('insert complete')
            update_sql = "update 飞行计划安排 set [" + cart + state_text[self.state]+"剩余座位] = ?" \
                                                         " where 航程号=?"
            result_up = cursor.execute(update_sql, tacket-1, self.num)
            cursor.commit()
            print('update complete')
            reply = QMessageBox.information(self,
                                        "消息框标题",
                                        "购票成功",
                                        QMessageBox.Yes | QMessageBox.No)
        else:
            reply = QMessageBox.warning(self,
                                        "消息框标题",
                                        "没有余票！",
                                        QMessageBox.Yes | QMessageBox.No)
        conn.close()
    def remain_tacket(self):
        tacket_num = ()
        conn = pyodbc.connect(
            'DRIVER={SQL SERVER NATIVE CLIENT 10.0};SERVER=127.0.0.1;DATABASE=air;UID=sa;PWD=123456')
        if (self.state == 0):
            sql = "select *"\
                  " from 飞行计划安排 inner join 航班 on 飞行计划安排.航班编号 = 航班.航班编号"\
                  " inner join 机场 on 机场代码 = 出发机场代码"\
                  " inner join 机场 as b on b.机场代码 = 到达机场代码"\
                  " where 航程号 = ?"
            cursor = conn.cursor()
            result = (cursor.execute(sql, self.num).fetchall())
            tacket_num = result[0][6:9]
        if (self.state == 1):
            sql = "select *"\
                  " from 飞行计划安排 inner join 航班 on 飞行计划安排.航班编号 = 航班.航班编号"\
                  " inner join 机场 on 机场代码 = 出发机场代码"\
                  " inner join 机场 as b on b.机场代码 = 经停机场代码"\
                  " where 航程号 = ?"
            cursor = conn.cursor()
            result = (cursor.execute(sql, self.num).fetchall())
            tacket_num = result[0][12:15]
        if (self.state == 2):
            sql = "select *"\
                  " from 飞行计划安排 inner join 航班 on 飞行计划安排.航班编号 = 航班.航班编号"\
                  " inner join 机场 on 机场代码 = 出发机场代码"\
                  " inner join 机场 as b on b.机场代码 = 经停机场代码"\
                  " where 航程号 = ?"
            cursor = conn.cursor()
            result = (cursor.execute(sql, self.num).fetchall())
            tacket_num = result[0][9:12]
        kind = {}
        kind['经济舱'] = 0
        kind['商务舱'] = 1
        kind['头等舱'] = 2
        cart = self.com_class.currentText()
        tacket = tacket_num[kind[cart]]
        if (tacket is None):
            tacket = 0
        self.remain_num.setText(str(tacket))
        conn.close()




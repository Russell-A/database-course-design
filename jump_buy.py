# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jump_buy_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
import pyodbc


class Ui_Dialog_jump_buy(object):
    state = -1
    num = -1
    username = 'aa'
    def setupUi(self, Dialog_jump_buy):
        Dialog_jump_buy.setObjectName("Dialog_jump_buy")
        Dialog_jump_buy.resize(465, 430)
        Dialog_jump_buy.setFixedSize(465, 430)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_jump_buy)
        self.gridLayout.setObjectName("gridLayout")
        self.identity_num = QtWidgets.QLineEdit(Dialog_jump_buy)
        self.identity_num.setMinimumSize(QtCore.QSize(189, 0))
        self.identity_num.setMaximumSize(QtCore.QSize(189, 16777215))
        self.identity_num.setMaxLength(1000)
        self.identity_num.setObjectName("identity_num")
        self.gridLayout.addWidget(self.identity_num, 5, 6, 1, 2)
        self.combo_kind = QtWidgets.QComboBox(Dialog_jump_buy)
        self.combo_kind.setObjectName("combo_kind")
        self.combo_kind.addItem("")
        self.combo_kind.addItem("")
        self.combo_kind.addItem("")
        self.combo_kind.addItem("")
        self.combo_kind.addItem("")
        self.gridLayout.addWidget(self.combo_kind, 3, 6, 1, 1)
        self.remain_num = QtWidgets.QLabel(Dialog_jump_buy)
        self.remain_num.setMinimumSize(QtCore.QSize(81, 0))
        self.remain_num.setMaximumSize(QtCore.QSize(225, 16777215))
        self.remain_num.setText("")
        self.remain_num.setObjectName("remain_num")
        self.gridLayout.addWidget(self.remain_num, 0, 8, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 4, 1, 2)
        self.name = QtWidgets.QLineEdit(Dialog_jump_buy)
        self.name.setMinimumSize(QtCore.QSize(131, 0))
        self.name.setMaximumSize(QtCore.QSize(131, 16777215))
        self.name.setMaxLength(100)
        self.name.setFrame(True)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 4, 6, 1, 2)
        self.label = QtWidgets.QLabel(Dialog_jump_buy)
        self.label.setMaximumSize(QtCore.QSize(125, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 4, 1, 1)
        self.com_class = QtWidgets.QComboBox(Dialog_jump_buy)
        self.com_class.setMaximumSize(QtCore.QSize(87, 16777215))
        self.com_class.setObjectName("com_class")
        self.com_class.addItem("")
        self.com_class.addItem("")
        self.com_class.addItem("")
        self.gridLayout.addWidget(self.com_class, 0, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_2.setMaximumSize(QtCore.QSize(163, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 7, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_5.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 4, 1, 2)
        self.label_3 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_3.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 4, 1, 2)
        self.sex = QtWidgets.QComboBox(Dialog_jump_buy)
        self.sex.setMaximumSize(QtCore.QSize(87, 16777215))
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.gridLayout.addWidget(self.sex, 1, 6, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog_jump_buy)
        self.pushButton.setMaximumSize(QtCore.QSize(93, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 6, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_6.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 4, 1, 2)
        self.label_4 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_4.setMaximumSize(QtCore.QSize(69, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        self.phone_num = QtWidgets.QLineEdit(Dialog_jump_buy)
        self.phone_num.setMaximumSize(QtCore.QSize(189, 16777215))
        self.phone_num.setObjectName("phone_num")
        self.gridLayout.addWidget(self.phone_num, 6, 6, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)

        self.retranslateUi(Dialog_jump_buy)

        self.pushButton.clicked.connect(self.insert_tacket)
        self.com_class.currentIndexChanged.connect(self.remain_tacket)
        QtCore.QMetaObject.connectSlotsByName(Dialog_jump_buy)


        # self.pushButton.clicked.connect(self.change)

    def retranslateUi(self, Dialog_jump_buy):
        _translate = QtCore.QCoreApplication.translate
        Dialog_jump_buy.setWindowTitle(_translate("Dialog_jump_buy", "Dialog"))
        self.combo_kind.setItemText(0, _translate("Dialog_jump_buy", "成人"))
        self.combo_kind.setItemText(1, _translate("Dialog_jump_buy", "小孩"))
        self.combo_kind.setItemText(2, _translate("Dialog_jump_buy", "老人"))
        self.combo_kind.setItemText(3, _translate("Dialog_jump_buy", "病人"))
        self.combo_kind.setItemText(4, _translate("Dialog_jump_buy", "残疾"))
        self.label_7.setText(_translate("Dialog_jump_buy", "乘客类别："))
        self.label.setText(_translate("Dialog_jump_buy", "    舱位："))
        self.com_class.setItemText(0, _translate("Dialog_jump_buy", "头等舱"))
        self.com_class.setItemText(1, _translate("Dialog_jump_buy", "商务舱"))
        self.com_class.setItemText(2, _translate("Dialog_jump_buy", "经济舱"))
        self.label_2.setText(_translate("Dialog_jump_buy", "剩余票数："))
        self.label_5.setText(_translate("Dialog_jump_buy", "身份证号："))
        self.label_3.setText(_translate("Dialog_jump_buy", "乘客姓名："))
        self.sex.setItemText(0, _translate("Dialog_jump_buy", "男"))
        self.sex.setItemText(1, _translate("Dialog_jump_buy", "女"))
        self.pushButton.setText(_translate("Dialog_jump_buy", "购买"))
        self.label_6.setText(_translate("Dialog_jump_buy", "联系电话："))
        self.label_4.setText(_translate("Dialog_jump_buy", "    性别："))


    def insert_tacket(self):
        dairport = ''
        aairport = ''
        tacket_num = ()
        conn = pyodbc.connect(
            'DRIVER={SQL SERVER NATIVE CLIENT 10.0};SERVER=127.0.0.1;DATABASE=air;UID=sa;PWD=123456')
        conn.autocommit = False
        conn.set_attr(pyodbc.SQL_ATTR_TXN_ISOLATION, pyodbc.SQL_TXN_SERIALIZABLE)
        cursor = conn.cursor()
        if (self.state == 0):
            sql = "select *"\
                  " from 飞行计划安排 inner join 航班 on 飞行计划安排.航班编号 = 航班.航班编号"\
                  " inner join 机场 on 机场代码 = 出发机场代码"\
                  " inner join 机场 as b on b.机场代码 = 到达机场代码"\
                  " where 航程号 = ?"

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
        kind_ = self.combo_kind.currentText()
        tele = self.phone_num.text()
        id = self.identity_num.text()
        name = self.name.text()
        if (len(name)<1 or len(id)<1 or len(tele)<1):
            reply = QMessageBox.warning(self,
                                        "消息框标题",
                                        "请先填写好信息！",
                                        QMessageBox.Yes | QMessageBox.No)
        elif (tacket>0):

            update_sql = "update 飞行计划安排 set [" + cart + state_text[self.state]+"剩余座位] = [" + cart + state_text[self.state]+"剩余座位]-1"\
                                                         " where 航程号=?"
            result_up = cursor.execute(update_sql, self.num)

            if (self.state == 0):
                sql_1 = "update 飞行计划安排 set [" + cart + state_text[1]+"剩余座位] = [" + cart + state_text[1]+"剩余座位]-1"\
                                                         " where 航程号=?"
                cursor.execute(sql_1,self.num)
                sql_2 = "update 飞行计划安排 set [" + cart + state_text[2]+"剩余座位] = [" + cart + state_text[2]+"剩余座位]-1"\
                                                         " where 航程号=?"
                cursor.execute(sql_2,self.num)
            else:
                sql_1 = "update 飞行计划安排 set [" + cart + state_text[0] + "剩余座位] = [" + cart + state_text[0]+"剩余座位]-1"\
                                                         " where 航程号=?"
                cursor.execute(sql_1, self.num)
            insert_sql = "insert into 订票 values (?,?,?,?,?,?,?,?,?,?,?)"
            result_in = cursor.execute(insert_sql, self.num, dairport, aairport, str(tacket), cart, self.username, name, sex, kind_, str(id), str(tele))
            print('insert complete')
            cursor.commit()
            print('update complete')

            reply = QMessageBox.information(self,
                                        "消息框标题",
                                        "购票成功！是否继续买票？",
                                        QMessageBox.Yes | QMessageBox.No)
            if (reply == QMessageBox.Yes):
                conn.set_attr(pyodbc.SQL_ATTR_TXN_ISOLATION, pyodbc.SQL_TXN_REPEATABLE_READ)
                conn.close()
                self.phone_num.setText('')
                self.identity_num.setText('')
                self.name.setText('')
            else:
                conn.set_attr(pyodbc.SQL_ATTR_TXN_ISOLATION, pyodbc.SQL_TXN_REPEATABLE_READ)
                conn.close()
                self.close()
        else:
            reply = QMessageBox.warning(self,
                                        "消息框标题",
                                        "没有余票！",
                                        QMessageBox.Yes | QMessageBox.No)
            conn.set_attr(pyodbc.SQL_ATTR_TXN_ISOLATION, pyodbc.SQL_TXN_REPEATABLE_READ)
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




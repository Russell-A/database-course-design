# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jump_buy_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
import pyodbc

class Ui_Dialog_jump_buy(object):
    def setupUi(self, Dialog_jump_buy):
        Dialog_jump_buy.setObjectName("Dialog_jump_buy")
        Dialog_jump_buy.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("flight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_jump_buy.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog_jump_buy)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.com_class = QtWidgets.QComboBox(Dialog_jump_buy)
        self.com_class.setObjectName("com_class")
        self.com_class.addItem("")
        self.com_class.addItem("")
        self.com_class.addItem("")
        self.horizontalLayout.addWidget(self.com_class)
        self.label_5 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.remain_num = QtWidgets.QLabel(Dialog_jump_buy)
        self.remain_num.setAlignment(QtCore.Qt.AlignCenter)
        self.remain_num.setObjectName("remain_num")
        self.horizontalLayout.addWidget(self.remain_num)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.sex = QtWidgets.QComboBox(Dialog_jump_buy)
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.horizontalLayout_4.addWidget(self.sex)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.combo_kind = QtWidgets.QComboBox(Dialog_jump_buy)
        self.combo_kind.setObjectName("combo_kind")
        self.combo_kind.addItem("")
        self.combo_kind.addItem("")
        self.combo_kind.addItem("")
        self.combo_kind.addItem("")
        self.combo_kind.addItem("")
        self.horizontalLayout_6.addWidget(self.combo_kind)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.name = QtWidgets.QLineEdit(Dialog_jump_buy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setObjectName("name")
        self.horizontalLayout_5.addWidget(self.name)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.identity_num = QtWidgets.QLineEdit(Dialog_jump_buy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.identity_num.sizePolicy().hasHeightForWidth())
        self.identity_num.setSizePolicy(sizePolicy)
        self.identity_num.setObjectName("identity_num")
        self.horizontalLayout_3.addWidget(self.identity_num)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.phone_num = QtWidgets.QLineEdit(Dialog_jump_buy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone_num.sizePolicy().hasHeightForWidth())
        self.phone_num.setSizePolicy(sizePolicy)
        self.phone_num.setObjectName("phone_num")
        self.horizontalLayout_2.addWidget(self.phone_num)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(Dialog_jump_buy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog_jump_buy)
        self.pushButton.clicked.connect(self.insert_tacket)
        self.com_class.currentIndexChanged.connect(self.remain_tacket)
        QtCore.QMetaObject.connectSlotsByName(Dialog_jump_buy)

    def retranslateUi(self, Dialog_jump_buy):
        _translate = QtCore.QCoreApplication.translate
        Dialog_jump_buy.setWindowTitle(_translate("Dialog_jump_buy", "购买机票"))
        self.label_6.setText(_translate("Dialog_jump_buy", "舱位："))
        self.com_class.setItemText(0, _translate("Dialog_jump_buy", "头等舱"))
        self.com_class.setItemText(1, _translate("Dialog_jump_buy", "商务舱"))
        self.com_class.setItemText(2, _translate("Dialog_jump_buy", "经济舱"))
        self.label_5.setText(_translate("Dialog_jump_buy", "剩余票数："))
        self.remain_num.setText(_translate("Dialog_jump_buy", "     "))
        self.label_2.setText(_translate("Dialog_jump_buy", "    性别："))
        self.sex.setItemText(0, _translate("Dialog_jump_buy", "男"))
        self.sex.setItemText(1, _translate("Dialog_jump_buy", "女"))
        self.label_8.setText(_translate("Dialog_jump_buy", "乘客类别："))
        self.combo_kind.setItemText(0, _translate("Dialog_jump_buy", "成人"))
        self.combo_kind.setItemText(1, _translate("Dialog_jump_buy", "小孩"))
        self.combo_kind.setItemText(2, _translate("Dialog_jump_buy", "老人"))
        self.combo_kind.setItemText(3, _translate("Dialog_jump_buy", "病人"))
        self.combo_kind.setItemText(4, _translate("Dialog_jump_buy", "残疾"))
        self.label_7.setText(_translate("Dialog_jump_buy", "乘客姓名："))
        self.label_3.setText(_translate("Dialog_jump_buy", "身份证号："))
        self.label_4.setText(_translate("Dialog_jump_buy", "联系电话"))
        self.pushButton.setText(_translate("Dialog_jump_buy", "购买"))


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

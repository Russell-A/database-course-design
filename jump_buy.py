# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jump_buy_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_jump_buy(object):
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
        QtCore.QMetaObject.connectSlotsByName(Dialog_jump_buy)

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
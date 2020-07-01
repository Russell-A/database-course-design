# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 437)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.user_name = QtWidgets.QLineEdit(Dialog)
        self.user_name.setObjectName("user_name")
        self.verticalLayout.addWidget(self.user_name)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.tel = QtWidgets.QLineEdit(Dialog)
        self.tel.setObjectName("tel")
        self.verticalLayout.addWidget(self.tel)
        self.cancel = QtWidgets.QPushButton(Dialog)
        self.cancel.setStyleSheet("font: 9pt \"宋体\";\n"
"")
        self.cancel.setObjectName("cancel")
        self.verticalLayout.addWidget(self.cancel)
        self.register_2 = QtWidgets.QPushButton(Dialog)
        self.register_2.setObjectName("register")
        self.verticalLayout.addWidget(self.register_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "用户注册"))
        self.label_2.setText(_translate("Dialog", "用户名"))
        self.label_3.setText(_translate("Dialog", "密码"))
        self.label_5.setText(_translate("Dialog", "联系方式"))
        self.cancel.setText(_translate("Dialog", "取消"))
        self.register_2.setText(_translate("Dialog", "注册"))

        # 实例化注册窗体
    def instantiation(self):
        register_dialog = QDialog()
        child1_ui = Ui_Dialog()
        child1_ui.setupUi(register_dialog)
        return register_dialog,child1_ui

    # connect button
    def button_connect(self,child_register,button):
        #first instantiation ,next the name of button
        btn1 = button
        btn1.clicked.connect(child_register.show)
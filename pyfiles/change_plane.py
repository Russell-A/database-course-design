# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_plane.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtSql import QSqlTableModel, QSqlQueryModel
from PyQt5.QtWidgets import QMessageBox

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1050, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/flight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
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
        self.label_airplane = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_airplane.sizePolicy().hasHeightForWidth())
        self.label_airplane.setSizePolicy(sizePolicy)
        self.label_airplane.setAcceptDrops(False)
        self.label_airplane.setAlignment(QtCore.Qt.AlignCenter)
        self.label_airplane.setObjectName("label_airplane")
        self.horizontalLayout_3.addWidget(self.label_airplane)
        self.lineEdit_airplane = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_airplane.sizePolicy().hasHeightForWidth())
        self.lineEdit_airplane.setSizePolicy(sizePolicy)
        self.lineEdit_airplane.setObjectName("lineEdit_airplane")
        self.horizontalLayout_3.addWidget(self.lineEdit_airplane)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_empty = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_empty.sizePolicy().hasHeightForWidth())
        self.label_empty.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_empty.setFont(font)
        self.label_empty.setTextFormat(QtCore.Qt.PlainText)
        self.label_empty.setAlignment(QtCore.Qt.AlignCenter)
        self.label_empty.setObjectName("label_empty")
        self.verticalLayout.addWidget(self.label_empty)
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
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout.addWidget(self.pushButton_add)
        self.pushButton_delete = QtWidgets.QPushButton(Dialog)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.verticalLayout.addWidget(self.pushButton_delete)
        self.pushButton_submit = QtWidgets.QPushButton(Dialog)
        self.pushButton_submit.setEnabled(False)
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.verticalLayout.addWidget(self.pushButton_submit)
        self.pushButton_revert = QtWidgets.QPushButton(Dialog)
        self.pushButton_revert.setEnabled(False)
        self.pushButton_revert.setObjectName("pushButton_revert")
        self.verticalLayout.addWidget(self.pushButton_revert)
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
        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_submit.clicked.connect(self.submit)
        self.pushButton_revert.clicked.connect(self.revert)
        self.pushButton_delete.clicked.connect(self.delete_row)
        self.pushButton_add.clicked.connect(self.add_row)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "修改飞机信息"))
        self.label_airplane.setText(_translate("Dialog", "飞机编号："))
        self.label_empty.setText(_translate("Dialog", "（为空则查询全部飞机信息）"))
        self.pushButton_search.setText(_translate("Dialog", "查询"))
        self.pushButton_add.setText(_translate("Dialog", "添加一行"))
        self.pushButton_delete.setText(_translate("Dialog", "删除当前行"))
        self.pushButton_submit.setText(_translate("Dialog", "提交更改"))
        self.pushButton_revert.setText(_translate("Dialog", "取消更改"))

    def search(self):
        plane = self.lineEdit_airplane.text()  # 设置航班编号
        self.model = QtSql.QSqlTableModel()
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.tableView_search.setModel(self.model)  # 绑定table
        self.model.setTable("飞机登记")

        if plane == '':
            self.model.setSort(0, QtCore.Qt.AscendingOrder)
            if not self.model.select():
                QtWidgets.QMessageBox.warning(self, "提示", "%s" % (self.model.lastError().text()),
                                              QtWidgets.QMessageBox.Ok)
        else:
            self.model.setFilter("飞机编号 = '%s' " % (plane))
            # print(self.model.filter())
            self.model.setSort(0, QtCore.Qt.AscendingOrder)
            if not self.model.select():
                QtWidgets.QMessageBox.warning(self, "提示", "%s" % (self.model.lastError().text()),
                                              QtWidgets.QMessageBox.Ok)
        self.tableView_search.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        if self.model.rowCount() == 0:
            QtWidgets.QMessageBox.information(self, "提示", "未找到符合条件的飞机，请重试。", QtWidgets.QMessageBox.Ok)
            self.pushButton_submit.setEnabled(False)
            self.pushButton_revert.setEnabled(False)
        else:
            self.tableView_search.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            self.tableView_search.show()
            self.pushButton_submit.setEnabled(True)
            self.pushButton_revert.setEnabled(True)
            pass
        pass

    def revert(self):
        if QMessageBox.information(self,"取消更改","确定取消更改？", QMessageBox.Yes|QMessageBox.No) ==QMessageBox.Yes:
            self.model.revertAll()
            pass
        pass

    def submit(self):
        OK =QMessageBox.warning(self,"提交信息","数据提交后不可恢复，确定提交吗？", QMessageBox.Yes|QMessageBox.No)
        if OK == QMessageBox.No:
            pass
        else:
            if self.model.submitAll():
                QtWidgets.QMessageBox.information(self,"提示","修改成功。",QtWidgets.QMessageBox.Ok)
            else:
                self.model.revertAll()
                QtWidgets.QMessageBox.warning(self,"提示","%s" %(self.model.lastError().text()),QtWidgets.QMessageBox.Ok)
                pass
            pass
        pass

    def delete_row(self):
        curRow = self.tableView_search.currentIndex().row()  # 获取选中的行
        self.model.removeRow(curRow)  # 删除该行
        ok = QMessageBox.warning(self, "删除当前行!", "你确定删除当前行吗？", QMessageBox.Yes, QMessageBox.No)
        if (ok == QMessageBox.No):
            self.model.revertAll()  # 如果不删除，则撤销
        else:
            if self.model.submitAll():
                QtWidgets.QMessageBox.information(self, "提示", "修改成功。", QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.warning(self, "提示", "%s" % (self.model.lastError().text()),
                                              QtWidgets.QMessageBox.Ok)
                pass
            pass
        pass

    def add_row(self):
        rowNum = self.model.rowCount()  # 获得表的行数
        self.model.insertRow(rowNum)  #添加一行





# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_airport.ui'
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
        Dialog.resize(1050, 600)

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
        self.radioButton_flight = QtWidgets.QRadioButton(Dialog)
        self.radioButton_flight.setChecked(True)
        self.radioButton_flight.setObjectName("radioButton_flight")
        self.verticalLayout.addWidget(self.radioButton_flight)
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
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.radioButton_city = QtWidgets.QRadioButton(Dialog)
        self.radioButton_city.setObjectName("radioButton_city")
        self.verticalLayout.addWidget(self.radioButton_city)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_flight_city = QtWidgets.QLabel(Dialog)
        self.label_flight_city.setEnabled(False)
        self.label_flight_city.setObjectName("label_flight_city")
        self.horizontalLayout_4.addWidget(self.label_flight_city)
        self.lineEdit_flight_city = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_flight_city.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_flight_city.sizePolicy().hasHeightForWidth())
        self.lineEdit_flight_city.setSizePolicy(sizePolicy)
        self.lineEdit_flight_city.setObjectName("lineEdit_flight_city")
        self.horizontalLayout_4.addWidget(self.lineEdit_flight_city)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
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
        self.pushButton_search.setStyleSheet("")
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
        self.radioButton_flight.toggled.connect(self.state_change)
        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_submit.clicked.connect(self.submit)
        self.pushButton_revert.clicked.connect(self.revert)
        self.pushButton_delete.clicked.connect(self.delete_row)
        self.pushButton_add.clicked.connect(self.add_row)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "修改机场信息"))
        self.radioButton_flight.setText(_translate("Dialog", "使用机场代码："))
        self.label_flight_no.setText(_translate("Dialog", "机场代码："))
        self.label_empty.setText(_translate("Dialog", "（为空则查询全部机场）"))
        self.radioButton_city.setText(_translate("Dialog", "使用机场所在城市："))
        self.label_flight_city.setText(_translate("Dialog", "机场所在城市："))
        self.label.setText(_translate("Dialog", "（为空则查询全部机场）"))
        self.pushButton_search.setText(_translate("Dialog", "查询"))
        self.pushButton_add.setText(_translate("Dialog", "添加一行"))
        self.pushButton_delete.setText(_translate("Dialog", "删除选中行"))
        self.pushButton_submit.setText(_translate("Dialog", "提交更改"))
        self.pushButton_revert.setText(_translate("Dialog", "取消更改"))

    def search(self):
        if (self.radioButton_flight.isChecked()):
            flight_no = self.lineEdit_flight_no.text()  # 设置航程号
            self.model = QtSql.QSqlTableModel()
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
            self.tableView_search.setModel(self.model)  # 绑定table
            self.model.setTable("机场")

            if flight_no == '':
                self.model.setSort(0, QtCore.Qt.AscendingOrder)
                if not self.model.select():
                    QtWidgets.QMessageBox.warning(self, "提示", "%s" % (self.model.lastError().text()),
                                                  QtWidgets.QMessageBox.Ok)
            else:
                self.model.setFilter("机场代码 = '%s' " % (flight_no))
                # print(self.model.filter())
                self.model.setSort(0, QtCore.Qt.AscendingOrder)
                if not self.model.select():
                    QtWidgets.QMessageBox.warning(self, "提示", "%s" % (self.model.lastError().text()),
                                                  QtWidgets.QMessageBox.Ok)
            self.tableView_search.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            if self.model.rowCount() == 0:
                QtWidgets.QMessageBox.information(self, "提示", "未找到符合条件的机场，请重试。", QtWidgets.QMessageBox.Ok)
                self.pushButton_submit.setEnabled(False)
                self.pushButton_revert.setEnabled(False)
            else:
                self.tableView_search.horizontalHeader().setSectionResizeMode(
                    QtWidgets.QHeaderView.ResizeToContents)
                self.tableView_search.show()
                self.pushButton_submit.setEnabled(True)
                self.pushButton_revert.setEnabled(True)
        else:
            flight_no = self.lineEdit_flight_city.text()  # 设置航班编号
            self.model = QtSql.QSqlTableModel()
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
            self.tableView_search.setModel(self.model)  # 绑定table
            self.model.setTable("机场")

            if flight_no == '':
                self.model.setSort(0, QtCore.Qt.AscendingOrder)
                if not self.model.select():
                    QtWidgets.QMessageBox.warning(self, "提示", "%s" % (self.model.lastError().text()),
                                                  QtWidgets.QMessageBox.Ok)
            else:
                self.model.setFilter("所在城市 = '%s' " % (flight_no))
                # print(self.model.filter())
                self.model.setSort(0, QtCore.Qt.AscendingOrder)
                if not self.model.select():
                    QtWidgets.QMessageBox.warning(self, "提示", "%s" % (self.model.lastError().text()),
                                                  QtWidgets.QMessageBox.Ok)
            self.tableView_search.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            if self.model.rowCount() == 0:
                QtWidgets.QMessageBox.information(self, "提示", "未找到符合条件的机场，请重试。", QtWidgets.QMessageBox.Ok)
                self.pushButton_submit.setEnabled(False)
                self.pushButton_revert.setEnabled(False)
            else:
                self.tableView_search.horizontalHeader().setSectionResizeMode(
                    QtWidgets.QHeaderView.ResizeToContents)
                self.tableView_search.show()
                self.pushButton_submit.setEnabled(True)
                self.pushButton_revert.setEnabled(True)
                pass
            pass
        pass

        # sql = self.textEdit_sql.toPlainText()
        # self.model = QSqlQueryModel()
        # self.model.setQuery("%s" %(sql))
        # self.tableView_search.setModel(self.model)
        # if self.model.lastError().isValid():
        #     QtWidgets.QMessageBox.warning(self, "提示", "%s" % (self.model.lastError().text()),
        #                                   QtWidgets.QMessageBox.Ok)
        #     self.pushButton_submit.setEnabled(False)
        # else:
        #     self.tableView_search.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        #     self.tableView_search.show()
        #     self.pushButton_submit.setEnabled(True)

    def revert(self):
        if QMessageBox.information(self, "取消更改", "确定取消更改？", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.model.revertAll()
            pass
        pass

    def submit(self):
        OK = QMessageBox.warning(self, "提交信息", "数据提交后不可恢复，确定提交吗？", QMessageBox.Yes | QMessageBox.No)
        if OK == QMessageBox.No:
            pass
        else:
            if self.model.submitAll():
                QtWidgets.QMessageBox.information(self, "提示", "修改成功。", QtWidgets.QMessageBox.Ok)
            else:
                self.model.revertAll()
                QtWidgets.QMessageBox.warning(self, "提示", "%s" % (self.model.lastError().text()),
                                              QtWidgets.QMessageBox.Ok)
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

    pass

    def add_row(self):
        rowNum = self.model.rowCount()  # 获得表的行数
        self.model.insertRow(rowNum)  # 添加一行

    def state_change(self):
        self.lineEdit_flight_no.setEnabled(not self.lineEdit_flight_no.isEnabled())
        self.lineEdit_flight_city.setEnabled(not self.lineEdit_flight_city.isEnabled())
        self.label_empty.setEnabled(not self.label_empty.isEnabled())
        self.label_flight_no.setEnabled(not self.label_flight_no.isEnabled())
        self.label_flight_city.setEnabled(not self.label_flight_city.isEnabled())
        self.label.setEnabled(not self.label.isEnabled())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_flight.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtSql import QSqlTableModel, QSqlQueryModel

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1050, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("flight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.radioButton_sql = QtWidgets.QRadioButton(Dialog)
        self.radioButton_sql.setObjectName("radioButton_sql")
        self.verticalLayout.addWidget(self.radioButton_sql)
        self.textEdit_sql = QtWidgets.QTextEdit(Dialog)
        self.textEdit_sql.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_sql.sizePolicy().hasHeightForWidth())
        self.textEdit_sql.setSizePolicy(sizePolicy)
        self.textEdit_sql.setObjectName("textEdit_sql")
        self.verticalLayout.addWidget(self.textEdit_sql)
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
        self.pushButton_submit = QtWidgets.QPushButton(Dialog)
        self.pushButton_submit.setEnabled(False)
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.verticalLayout.addWidget(self.pushButton_submit)
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
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def search(self):
        if(self.radioButton_flight.isChecked()):
            flight_no = self.lineEdit_flight_no.text()   # 设置航程号
            self.model = QtSql.QSqlTableModel()
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
            self.tableView_search.setModel(self.model)   # 绑定table
            self.model.setTable("飞行计划安排")

            if flight_no == '':
                if not self.model.select():
                    QtWidgets.QMessageBox.warning(self, "提示", "%s" % (self.model.lastError().text()),
                                                  QtWidgets.QMessageBox.Ok)
            else:
                self.model.setFilter("航程号 = %s" % (flight_no))
                # print(self.model.filter())
                if not self.model.select():
                    QtWidgets.QMessageBox.warning(self, "提示", "%s" % (self.model.lastError().text()),
                                                  QtWidgets.QMessageBox.Ok)
            self.tableView_search.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            if self.model.rowCount() == 0:
                QtWidgets.QMessageBox.information(self, "提示", "未找到符合条件的航程，请重试。", QtWidgets.QMessageBox.Ok)
                self.pushButton_submit.setEnabled(False)
            else:
                self.tableView_search.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
                self.tableView_search.show()
                self.pushButton_submit.setEnabled(True)
        else:
            sql = self.textEdit_sql.toPlainText()
            self.model = QSqlQueryModel()
            self.model.setQuery("%s" %(sql))
            self.tableView_search.setModel(self.model)
            if self.model.lastError().isValid():
                QtWidgets.QMessageBox.warning(self, "提示", "%s" % (self.model.lastError().text()),
                                              QtWidgets.QMessageBox.Ok)
                self.pushButton_submit.setEnabled(False)
            else:
                self.tableView_search.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
                self.tableView_search.show()
                self.pushButton_submit.setEnabled(True)



    def submit(self):
        if self.model.submitAll():
            QtWidgets.QMessageBox.information(self,"提示","修改成功。",QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(self,"提示","%s" %(self.model.lastError().text()),QtWidgets.QMessageBox.Ok)



    def state_change(self):
        self.lineEdit_flight_no.setEnabled(not self.lineEdit_flight_no.isEnabled())
        self.textEdit_sql.setEnabled(not self.textEdit_sql.isEnabled())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioButton_flight.setText(_translate("Dialog", "使用航程号"))
        self.label_flight_no.setText(_translate("Dialog", "航程号："))
        self.label_empty.setText(_translate("Dialog", "（为空则查询全部航程）"))
        self.radioButton_sql.setText(_translate("Dialog", "使用SQL语句"))
        self.textEdit_sql.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#2d2d2d;\">输入SQL语句</span></p></body></html>"))
        self.pushButton_search.setText(_translate("Dialog", "查询"))
        self.pushButton_submit.setText(_translate("Dialog", "提交更改"))


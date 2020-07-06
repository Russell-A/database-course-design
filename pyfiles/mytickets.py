# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test9dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QVBoxLayout,QWidget,QApplication ,QHBoxLayout,QDialog,QPushButton,QMessageBox


class Ui_Mytickets(object):
    def setupUi(self, Dialog):
        self.username = '' # 登录的用户名
        Dialog.setObjectName("Dialog")
        Dialog.resize(964, 873)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 100, 241, 181))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.choice2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.choice2.setObjectName("choice2")
        self.gridLayout_2.addWidget(self.choice2, 3, 0, 1, 1)
        self.choice3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.choice3.setObjectName("choice3")
        self.gridLayout_2.addWidget(self.choice3, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.ticket_info = QtWidgets.QGroupBox(Dialog)
        self.ticket_info.setGeometry(QtCore.QRect(420, 40, 461, 752))
        self.ticket_info.setObjectName("ticket_info")
        self.ticketdetails = QtWidgets.QPushButton(self.ticket_info)
        self.ticketdetails.setGeometry(QtCore.QRect(290, 190, 91, 28))
        self.ticketdetails.setObjectName("ticketdetails")
        self.flight = QtWidgets.QLabel(self.ticket_info)
        self.flight.setGeometry(QtCore.QRect(30, 30, 72, 15))
        self.flight.setObjectName("flight")
        self.departuretime = QtWidgets.QLabel(self.ticket_info)
        self.departuretime.setGeometry(QtCore.QRect(20, 70, 72, 15))
        self.departuretime.setObjectName("departuretime")
        self.label_3 = QtWidgets.QLabel(self.ticket_info)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.ticket_info)
        self.label_4.setGeometry(QtCore.QRect(280, 30, 72, 15))
        self.label_4.setObjectName("label_4")
        self.customer = QtWidgets.QTextBrowser(self.ticket_info)
        self.customer.setGeometry(QtCore.QRect(330, 20, 111, 31))
        self.customer.setObjectName("customer")
        self.flightnum = QtWidgets.QTextBrowser(self.ticket_info)
        self.flightnum.setGeometry(QtCore.QRect(110, 20, 121, 31))
        self.flightnum.setObjectName("flightnum")
        self.leavetime = QtWidgets.QTextBrowser(self.ticket_info)
        self.leavetime.setGeometry(QtCore.QRect(110, 60, 121, 41))
        self.leavetime.setObjectName("leavetime")
        self.locations = QtWidgets.QTextBrowser(self.ticket_info)
        self.locations.setGeometry(QtCore.QRect(110, 120, 121, 71))
        self.locations.setObjectName("locations")
        self.ticket_info_2 = QtWidgets.QGroupBox(self.ticket_info)
        self.ticket_info_2.setGeometry(QtCore.QRect(0, 240, 449, 245))
        self.ticket_info_2.setObjectName("ticket_info_2")
        self.ticketdetails_2 = QtWidgets.QPushButton(self.ticket_info_2)
        self.ticketdetails_2.setGeometry(QtCore.QRect(290, 190, 91, 28))
        self.ticketdetails_2.setObjectName("ticketdetails_2")
        self.flight_2 = QtWidgets.QLabel(self.ticket_info_2)
        self.flight_2.setGeometry(QtCore.QRect(30, 30, 72, 15))
        self.flight_2.setObjectName("flight_2")
        self.label_5 = QtWidgets.QLabel(self.ticket_info_2)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.ticket_info_2)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 81, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.ticket_info_2)
        self.label_7.setGeometry(QtCore.QRect(280, 30, 72, 15))
        self.label_7.setObjectName("label_7")
        self.customer_2 = QtWidgets.QTextBrowser(self.ticket_info_2)
        self.customer_2.setGeometry(QtCore.QRect(330, 20, 111, 31))
        self.customer_2.setObjectName("customer_2")
        self.flightnum_2 = QtWidgets.QTextBrowser(self.ticket_info_2)
        self.flightnum_2.setGeometry(QtCore.QRect(110, 20, 121, 31))
        self.flightnum_2.setObjectName("flightnum_2")
        self.leavetime_2 = QtWidgets.QTextBrowser(self.ticket_info_2)
        self.leavetime_2.setGeometry(QtCore.QRect(110, 90, 121, 41))
        self.leavetime_2.setObjectName("leavetime_2")
        self.locations_2 = QtWidgets.QTextBrowser(self.ticket_info_2)
        self.locations_2.setGeometry(QtCore.QRect(110, 150, 121, 71))
        self.locations_2.setObjectName("locations_2")
        self.seat_2 = QtWidgets.QTextBrowser(self.ticket_info_2)
        self.seat_2.setGeometry(QtCore.QRect(330, 100, 111, 31))
        self.seat_2.setObjectName("seat_2")
        self.ticketnum_2 = QtWidgets.QTextBrowser(self.ticket_info_2)
        self.ticketnum_2.setGeometry(QtCore.QRect(330, 60, 111, 31))
        self.ticketnum_2.setObjectName("ticketnum_2")
        self.label_15 = QtWidgets.QLabel(self.ticket_info_2)
        self.label_15.setGeometry(QtCore.QRect(280, 150, 72, 15))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.ticket_info_2)
        self.label_16.setGeometry(QtCore.QRect(270, 70, 72, 15))
        self.label_16.setObjectName("label_16")
        self.price_2 = QtWidgets.QTextBrowser(self.ticket_info_2)
        self.price_2.setGeometry(QtCore.QRect(330, 140, 111, 31))
        self.price_2.setObjectName("price_2")
        self.label_17 = QtWidgets.QLabel(self.ticket_info_2)
        self.label_17.setGeometry(QtCore.QRect(280, 100, 72, 20))
        self.label_17.setObjectName("label_17")
        self.label_11 = QtWidgets.QLabel(self.ticket_info)
        self.label_11.setGeometry(QtCore.QRect(270, 70, 72, 15))
        self.label_11.setObjectName("label_11")
        self.ticketnum = QtWidgets.QTextBrowser(self.ticket_info)
        self.ticketnum.setGeometry(QtCore.QRect(330, 60, 111, 31))
        self.ticketnum.setObjectName("ticketnum")
        self.seat = QtWidgets.QTextBrowser(self.ticket_info)
        self.seat.setGeometry(QtCore.QRect(330, 100, 111, 31))
        self.seat.setObjectName("seat")
        self.label_13 = QtWidgets.QLabel(self.ticket_info)
        self.label_13.setGeometry(QtCore.QRect(280, 100, 72, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.ticket_info)
        self.label_14.setGeometry(QtCore.QRect(280, 150, 72, 15))
        self.label_14.setObjectName("label_14")
        self.price = QtWidgets.QTextBrowser(self.ticket_info)
        self.price.setGeometry(QtCore.QRect(330, 140, 111, 31))
        self.price.setObjectName("price")
        self.ticket_info_3 = QtWidgets.QGroupBox(self.ticket_info)
        self.ticket_info_3.setGeometry(QtCore.QRect(0, 470, 451, 241))
        self.ticket_info_3.setObjectName("ticket_info_3")
        self.ticketdetails_3 = QtWidgets.QPushButton(self.ticket_info_3)
        self.ticketdetails_3.setGeometry(QtCore.QRect(290, 190, 91, 28))
        self.ticketdetails_3.setObjectName("ticketdetails_3")
        self.flight_3 = QtWidgets.QLabel(self.ticket_info_3)
        self.flight_3.setGeometry(QtCore.QRect(30, 30, 72, 15))
        self.flight_3.setObjectName("flight_3")
        self.label_8 = QtWidgets.QLabel(self.ticket_info_3)
        self.label_8.setGeometry(QtCore.QRect(20, 100, 72, 15))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.ticket_info_3)
        self.label_9.setGeometry(QtCore.QRect(20, 160, 81, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.ticket_info_3)
        self.label_10.setGeometry(QtCore.QRect(280, 30, 72, 15))
        self.label_10.setObjectName("label_10")
        self.customer_3 = QtWidgets.QTextBrowser(self.ticket_info_3)
        self.customer_3.setGeometry(QtCore.QRect(330, 20, 111, 31))
        self.customer_3.setObjectName("customer_3")
        self.flightnum_3 = QtWidgets.QTextBrowser(self.ticket_info_3)
        self.flightnum_3.setGeometry(QtCore.QRect(110, 20, 121, 31))
        self.flightnum_3.setObjectName("flightnum_3")
        self.leavetime_3 = QtWidgets.QTextBrowser(self.ticket_info_3)
        self.leavetime_3.setGeometry(QtCore.QRect(110, 90, 121, 41))
        self.leavetime_3.setObjectName("leavetime_3")
        self.locations_3 = QtWidgets.QTextBrowser(self.ticket_info_3)
        self.locations_3.setGeometry(QtCore.QRect(110, 150, 121, 71))
        self.locations_3.setObjectName("locations_3")
        self.seat_3 = QtWidgets.QTextBrowser(self.ticket_info_3)
        self.seat_3.setGeometry(QtCore.QRect(330, 100, 111, 31))
        self.seat_3.setObjectName("seat_3")
        self.ticketnum_3 = QtWidgets.QTextBrowser(self.ticket_info_3)
        self.ticketnum_3.setGeometry(QtCore.QRect(330, 60, 111, 31))
        self.ticketnum_3.setObjectName("ticketnum_3")
        self.label_18 = QtWidgets.QLabel(self.ticket_info_3)
        self.label_18.setGeometry(QtCore.QRect(280, 150, 72, 15))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.ticket_info_3)
        self.label_19.setGeometry(QtCore.QRect(270, 70, 72, 15))
        self.label_19.setObjectName("label_19")
        self.price_3 = QtWidgets.QTextBrowser(self.ticket_info_3)
        self.price_3.setGeometry(QtCore.QRect(330, 140, 111, 31))
        self.price_3.setObjectName("price_3")
        self.label_20 = QtWidgets.QLabel(self.ticket_info_3)
        self.label_20.setGeometry(QtCore.QRect(280, 100, 72, 20))
        self.label_20.setObjectName("label_20")
        self.lastpage_btn = QtWidgets.QPushButton(self.ticket_info)
        self.lastpage_btn.setGeometry(QtCore.QRect(120, 720, 93, 28))
        self.lastpage_btn.setObjectName("lastpage_btn")
        self.nextpage_btn = QtWidgets.QPushButton(self.ticket_info)
        self.nextpage_btn.setGeometry(QtCore.QRect(260, 720, 93, 28))
        self.nextpage_btn.setObjectName("nextpage_btn")

        self.retranslateUi(Dialog)

        # choice3 已出行 按钮
        self.choice3.clicked.connect(self.alreadygone)
        #choice2 未出行按钮
        self.choice2.clicked.connect(self.nondeparture)

        self.nextpage_btn.clicked.connect(self.nextpage)
        self.lastpage_btn.clicked.connect(self.lastpage)
        #退票操作……
        self.ticketdetails.clicked.connect(lambda: self.refund(ticketnum=int(self.ticketnum.toPlainText())))
        self.ticketdetails_2.clicked.connect(lambda: self.refund(ticketnum=int(self.ticketnum_2.toPlainText())))
        self.ticketdetails_3.clicked.connect(lambda: self.refund(ticketnum=int(self.ticketnum_3.toPlainText())))

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.choice2.setText(_translate("Dialog", "未出行"))
        self.choice3.setText(_translate("Dialog", "历史记录"))
        self.label.setText(_translate("Dialog", "我的机票"))
        self.ticket_info.setTitle(_translate("Dialog", "机票信息"))
        self.ticketdetails.setText(_translate("Dialog", "退票"))
        self.flight.setText(_translate("Dialog", "航班号："))
        self.departuretime.setText(_translate("Dialog", "出发时间："))
        self.label_3.setText(_translate("Dialog", "起点与终点："))
        self.label_4.setText(_translate("Dialog", "乘客："))
        self.ticket_info_2.setTitle(_translate("Dialog", "机票信息"))
        self.ticketdetails_2.setText(_translate("Dialog", "退票"))
        self.flight_2.setText(_translate("Dialog", "航班号："))
        self.label_5.setText(_translate("Dialog", "出发时间："))
        self.label_6.setText(_translate("Dialog", "起点与终点："))
        self.label_7.setText(_translate("Dialog", "乘客："))
        self.label_15.setText(_translate("Dialog", "票价："))
        self.label_16.setText(_translate("Dialog", "机票号："))
        self.label_17.setText(_translate("Dialog", "舱位："))
        self.label_11.setText(_translate("Dialog", "机票号："))
        self.label_13.setText(_translate("Dialog", "舱位："))
        self.label_14.setText(_translate("Dialog", "票价："))
        self.ticket_info_3.setTitle(_translate("Dialog", "机票信息"))
        self.ticketdetails_3.setText(_translate("Dialog", "退票"))
        self.flight_3.setText(_translate("Dialog", "航班号："))
        self.label_8.setText(_translate("Dialog", "出发时间："))
        self.label_9.setText(_translate("Dialog", "起点与终点："))
        self.label_10.setText(_translate("Dialog", "乘客："))
        self.label_18.setText(_translate("Dialog", "票价："))
        self.label_19.setText(_translate("Dialog", "机票号："))
        self.label_20.setText(_translate("Dialog", "舱位："))
        self.lastpage_btn.setText(_translate("Dialog", "上一页"))
        self.nextpage_btn.setText(_translate("Dialog", "下一页"))


        self.ticket_info_3.hide()
        self.ticket_info_2.hide()
        self.ticket_info.hide()
        self.lastpage_btn.hide()
        self.nextpage_btn.hide()
        self.index =0
        self.flag = 0



    # 以下是一堆槽函数
    def refund(self,ticketnum):
        '''
        退款按钮槽函数
        '''
        print('ok??',ticketnum)
        choice = QMessageBox.warning(self, '退票警告', '是否确认退票?', QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        if choice == QMessageBox.Yes:
            query = QSqlQuery()
            query.prepare('delete From 订票 where 机票编号= :ticketnum ')  # 输入SQL语句
            query.bindValue(":ticketnum", ticketnum)
            if query.exec_() :
                QMessageBox.information(self, "提示", "已成功退票！", QMessageBox.Yes)
            else:
                QMessageBox.information(self, "提示", "退票时错误！", QMessageBox.Yes)
            self.searchnow()
        else:
            pass

    def searchnow(self):
        # 退票后重新搜索
        if self.index > 0:
            self.index -= 1
            self.flag = 1
            self.nextpage()
        else:
            self.alreadygone()


    def get_time_minus(self,a,b):
        seconds = 60
        atime = a.toTime_t()
        btime = b.toTime_t()
        return (atime - btime)/seconds

    # 除了查询条件 ，nondeparture 与 alreadygone 一样
    def nondeparture(self):
        self.ticketdetails.show()
        self.ticketdetails_2.show()
        self.ticketdetails_3.show()
        self.index = self.flag =0
        self.ticket_info.hide()
        self.ticket_info_2.hide()
        self.ticket_info_3.hide()
        username = self.username
        query = QSqlQuery()
        query.prepare('Select * From 用户购票信息 '
                      'where 用户名 = :username and 出发时间 < :specialtime')  # 输入SQL语句  改成大于号就好了，但为了方便测试先不改
        query.bindValue(":username", username)
        now = QDateTime.currentDateTime()
        now = now.toString("yyyy-MM-dd HH:mm:ss")
        query.bindValue(":specialtime",now)
        query.exec_()
        i = 1
        while query.next():
            if i==1:
                tmp1 = query.value("航程号")
                self.flightnum.setText(str(tmp1))
                self.leavetime.setText(query.value('出发时间').toString(Qt.ISODate))
                a= query.value('出发时间')
                b = query.value('到达时间')
                time = int( self.get_time_minus(a,b) )
                self.locations.setText(str(query.value("出发地")) + '---' + str(time) + '分钟飞到----' + str(query.value("目的地")))
                self.customer.setText(str(query.value("乘客姓名")))
                self.ticketnum.setText(str(query.value('机票编号')))
                self.seat.setText(str(query.value('舱位')))
                self.price.setText(str(query.value('票价')))
                self.ticket_info.show()
            if i==2:
                tmp1 = query.value("航程号")
                self.flightnum_2.setText(str(tmp1))
                self.leavetime_2.setText(query.value('出发时间').toString(Qt.ISODate))
                a = query.value('出发时间')
                b = query.value('到达时间')
                time = int(self.get_time_minus(a, b))
                self.locations_2.setText(
                    str(query.value("出发地")) + '---' + str(time) + '分钟飞到----' + str(query.value("目的地")))
                self.customer_2.setText(str(query.value("乘客姓名")))
                self.ticketnum_2.setText(str(query.value('机票编号')))
                self.seat_2.setText(str(query.value('舱位')))
                self.price_2.setText(str(query.value('票价')))

                self.ticket_info_2.show()
            if i==3:
                tmp1 = query.value("航程号")
                self.flightnum_3.setText(str(tmp1))
                self.leavetime_3.setText(query.value('出发时间').toString(Qt.ISODate))
                a = query.value('出发时间')
                b = query.value('到达时间')
                time = int(self.get_time_minus(a, b))
                self.locations_3.setText(
                    str(query.value("出发地")) + '---' + str(time) + '分钟飞到----' + str(query.value("目的地")))
                self.customer_3.setText(str(query.value("乘客姓名")))
                self.ticketnum_3.setText(str(query.value('机票编号')))
                self.seat_3.setText(str(query.value('舱位')))
                self.price_3.setText(str(query.value('票价')))
                self.ticket_info_3.show()

            if i==4:
                self.nextpage_btn.show()
                self.flag = 1
                break
            i += 1
        if i == 1:
            QMessageBox.information(self, "消息框标题", "抱歉，没有您的未出行信息！", QMessageBox.Ok)




    def alreadygone(self): #该默认参数仅作测试用
        '''
        已出行机票……仅记录
        '''
        #username = self.xxx
        username = self.username  #实际中已登录的信息
        self.ticketdetails.hide()
        self.ticketdetails_2.hide()
        self.ticketdetails_3.hide()
        self.index = self.flag =0
        self.ticket_info.hide()
        self.ticket_info_2.hide()
        self.ticket_info_3.hide()
        query = QSqlQuery()
        query.prepare('Select * From 用户购票信息 '
                      'where 用户名 = :username and 出发时间 < :specialtime ')  # 输入SQL语句 and 出发时间 < :specialtime
        query.bindValue(":username", username)
        now = QDateTime.currentDateTime()
        now = now.toString("yyyy-MM-dd HH:mm:ss")
        query.bindValue(":specialtime",now)
        query.exec_()
        i = 1
        while query.next():
            if i==1:
                tmp1 = query.value("航程号")
                self.flightnum.setText(str(tmp1))
                self.leavetime.setText(query.value('出发时间').toString(Qt.ISODate))
                a = query.value('出发时间')
                b = query.value('到达时间')
                time = int(self.get_time_minus(a, b))
                self.locations.setText(
                    str(query.value("出发地")) + '---' + str(time) + '分钟飞到----' + str(query.value("目的地")))
                self.customer.setText(str(query.value("乘客姓名")))
                self.ticketnum.setText(str(query.value('机票编号')))
                self.seat.setText(str(query.value('舱位')))
                self.price.setText(str(query.value('票价')))
                self.ticket_info.show()
            if i==2:
                tmp1 = query.value("航程号")
                self.flightnum_2.setText(str(tmp1))
                self.leavetime_2.setText(query.value('出发时间').toString(Qt.ISODate))
                a = query.value('出发时间')
                b = query.value('到达时间')
                time = int(self.get_time_minus(a, b))
                self.locations_2.setText(
                    str(query.value("出发地")) + '---' + str(time) + '分钟飞到----' + str(query.value("目的地")))
                self.customer_2.setText(str(query.value("乘客姓名")))
                self.ticketnum_2.setText(str(query.value('机票编号')))
                self.seat_2.setText(str(query.value('舱位')))
                self.price_2.setText(str(query.value('票价')))

                self.ticket_info_2.show()
            if i==3:
                tmp1 = query.value("航程号")
                self.flightnum_3.setText(str(tmp1))
                self.leavetime_3.setText(query.value('出发时间').toString(Qt.ISODate))
                a = query.value('出发时间')
                b = query.value('到达时间')
                time = int(self.get_time_minus(a, b))
                self.locations_3.setText(
                    str(query.value("出发地")) + '---' + str(time) + '分钟飞到----' + str(query.value("目的地")))
                self.customer_3.setText(str(query.value("乘客姓名")))
                self.ticketnum_3.setText(str(query.value('机票编号')))
                self.seat_3.setText(str(query.value('舱位')))
                self.price_3.setText(str(query.value('票价')))
                self.ticket_info_3.show()

            if i==4:
                self.nextpage_btn.show()
                self.flag = 1
                #show the more flights
                break
            i += 1
        if i == 1:
            QMessageBox.information(self, "消息框标题", "抱歉，没有您的购票信息！", QMessageBox.Ok)

    def nextpage(self): #在”已出行“ 一栏下 点击 “下一页” 按钮
        username = self.username
        self.index += self.flag
        self.flag = 0
        if self.index >=  1:
            self.lastpage_btn.show()
        self.ticket_info.hide()
        self.ticket_info_2.hide()
        self.ticket_info_3.hide()
        query = QSqlQuery()
        query.prepare('Select * From 用户购票信息 where 用户名 = :username ')  # 输入SQL语句
        query.bindValue(":username", username)
        query.exec_()
        i = 1
        while query.next():
            if i >= 3* self.index :
                break
            i += 1
        # new search
        i = 1
        while query.next():
            if i==1:
                tmp1 = query.value("航程号")
                self.flightnum.setText(str(tmp1))
                self.leavetime.setText(query.value('出发时间').toString(Qt.ISODate))
                a = query.value('出发时间')
                b = query.value('到达时间')
                time = int(self.get_time_minus(a, b))
                self.locations.setText(
                    str(query.value("出发地")) + '---' + str(time) + '分钟飞到---' + str(query.value("目的地")))
                self.customer.setText(str(query.value("乘客姓名")))
                self.ticketnum.setText(str(query.value('机票编号')))
                self.seat.setText(str(query.value('舱位')))
                self.price.setText(str(query.value('票价')))
                self.ticket_info.show()
            if i==2:
                tmp1 = query.value("航程号")
                self.flightnum_2.setText(str(tmp1))
                self.leavetime_2.setText(query.value('出发时间').toString(Qt.ISODate))
                a = query.value('出发时间')
                b = query.value('到达时间')
                time = int(self.get_time_minus(a, b))
                self.locations_2.setText(
                    str(query.value("出发地")) + '---' + str(time) + '分钟飞到---' + str(query.value("目的地")))
                self.customer_2.setText(str(query.value("乘客姓名")))
                self.ticketnum_2.setText(str(query.value('机票编号')))
                self.seat_2.setText(str(query.value('舱位')))
                self.price_2.setText(str(query.value('票价')))
                self.ticket_info_2.show()
            if i==3:
                tmp1 = query.value("航程号")
                self.flightnum_3.setText(str(tmp1))
                self.leavetime_3.setText(query.value('出发时间').toString(Qt.ISODate))
                a = query.value('出发时间')
                b = query.value('到达时间')
                time = int(self.get_time_minus(a, b))
                self.locations_3.setText(
                    str(query.value("出发地")) + '---' + str(time) + '分钟飞到---' + str(query.value("目的地")))
                self.customer_3.setText(str(query.value("乘客姓名")))
                self.ticketnum_3.setText(str(query.value('机票编号')))
                self.seat_3.setText(str(query.value('舱位')))
                self.price_3.setText(str(query.value('票价')))
                self.ticket_info_3.show()
            if i==4:
                self.nextpage_btn.show()
                self.flag = 1
                break
            i += 1
        if self.flag ==0 :
            self.nextpage_btn.hide()


    def lastpage(self):
        username = self.username
        self.index -= 1
        if self.index == 0:
            self.lastpage_btn.hide()
        self.flag = 0
        self.ticket_info.hide()
        self.ticket_info_2.hide()
        self.ticket_info_3.hide()
        query = QSqlQuery()
        query.prepare('Select * From 用户购票信息 where 用户名 = :username ')  # 输入SQL语句
        query.bindValue(":username", username)
        query.exec_()
        if self.index == 0:
            pass
        else:
            i = 1
            while query.next():
                if i >= 3 * self.index :
                    break
                i += 1
        # new search
        i = 1
        while query.next():
            if i == 1:
                tmp1 = query.value("航程号")
                self.flightnum.setText(str(tmp1))
                self.leavetime.setText(query.value('出发时间').toString(Qt.ISODate))
                a = query.value('出发时间')
                b = query.value('到达时间')
                time = int(self.get_time_minus(a, b))
                self.locations.setText(
                    str(query.value("出发地")) + '---' + str(time) + '分钟飞到---' + str(query.value("目的地")))
                self.customer.setText(str(query.value("乘客姓名")))
                self.ticketnum.setText(str(query.value('机票编号')))
                self.seat.setText(str(query.value('舱位')))
                self.price.setText(str(query.value('票价')))
                self.ticket_info.show()
            if i == 2:
                tmp1 = query.value("航程号")
                self.flightnum_2.setText(str(tmp1))
                self.leavetime_2.setText(query.value('出发时间').toString(Qt.ISODate))
                a = query.value('出发时间')
                b = query.value('到达时间')
                time = int(self.get_time_minus(a, b))
                self.locations_2.setText(
                    str(query.value("出发地")) + '---' + str(time) + '分钟飞到---' + str(query.value("目的地")))
                self.customer_2.setText(str(query.value("乘客姓名")))
                self.ticketnum_2.setText(str(query.value('机票编号')))
                self.seat_2.setText(str(query.value('舱位')))
                self.price_2.setText(str(query.value('票价')))
                self.ticket_info_2.show()
            if i == 3:
                tmp1 = query.value("航程号")
                self.flightnum_3.setText(str(tmp1))
                self.leavetime_3.setText(query.value('出发时间').toString(Qt.ISODate))
                a = query.value('出发时间')
                b = query.value('到达时间')
                time = int(self.get_time_minus(a, b))
                self.locations_3.setText(
                    str(query.value("出发地")) + '---' + str(time) + '分钟飞到---' + str(query.value("目的地")))
                self.customer_3.setText(str(query.value("乘客姓名")))
                self.ticketnum_3.setText(str(query.value('机票编号')))
                self.seat_3.setText(str(query.value('舱位')))
                self.price_3.setText(str(query.value('票价')))
                self.ticket_info_3.show()
            if i == 4:
                self.nextpage_btn.show()
                self.flag = 1
                break
            i += 1



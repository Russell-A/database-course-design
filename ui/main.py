import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
# 在这里加上所有的文件
from search import *



class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #链接数据库
    db = QSqlDatabase.addDatabase("QODBC")
    db.setDatabaseName("Driver={Sql Server};Server=127.0.0.1;Database=air")
    ok = db.open()
    # print(ok)

    #Query = QSqlQuery("select * from 机场")
    #while Query.next():
    #    print(Query.value(0),Query.value(1),)

    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
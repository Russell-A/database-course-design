from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import login as lg
import check as ck
import buy
import jump_buy as jpb
import sys
from functools import partial


# class loginUi(QMainWindow,lg.Ui_MainWindow):
#     def fun(self, l1, l2):
#         print(float(l1) + float(l2))
#
#     def __init__(self, parent=None):
#         super(loginUi, self).__init__(parent)
#         self.setupUi(self)
#         self.LoginButton.clicked.connect(lambda: self.fun(self.lineEdit.text(),self.lineEdit_2.text()))
#     def change(self):
#         print('1')
#
#     def changeconnect(self,f):
#         self.LoginButton.clicked.connect(f)
# class childWindow(QDialog):
#     def __init__(self):
#         QDialog.__init__(self)
#         self.child=ck.Ui_Dialog()
#         self.child.setupUi(self)

class BuyWindow(QMainWindow, buy.Ui_main):
    def __init__(self, parent=None):
        super(BuyWindow, self).__init__(parent)
        self.setupUi(self)
class Jump_Buy_Window(QMainWindow, jpb.Ui_main):
    def __init__(self, parent=None):
        super(Jump_Buy_Window, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_buy = BuyWindow()
    # main_login.changeconnect(child.show)
    # main_buy.show()
    jump_buy = Jump_Buy_Window()
    btn = main_buy.buybutton
    btn.clicked.connect(jump_buy.show)
    main_buy.show()
    sys.exit(app.exec_())
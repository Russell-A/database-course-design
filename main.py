import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
# from dust.mainWindow import *
# from dust.childWindow import *
import register
import login
import search
import register_win
import register_fail
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 实例化主窗口
    main = QMainWindow()
    main_ui = search.Ui_MainWindow()
    main_ui.setupUi(main)
    # 实例化子窗口
    child1 = QDialog()
    child1_ui = register.Ui_Dialog()
    child1_ui.setupUi(child1)

    child2 = QDialog()
    child2_ui = login.Ui_Dialog()
    child2_ui.setupUi(child2)
    # 按钮绑定事件
    btn1 = main_ui.pushButton
    btn1.clicked.connect(child1.show)
    #注册按钮
    btn2 = main_ui.pushButton_2
    btn2.clicked.connect(child2.show)
    #登录按钮
    # 显示

    #实例化二级子窗口
    reg_child_win = QDialog()
    reg_child_win_ui = register_win.Ui_Dialog()
    reg_child_win_ui.setupUi(reg_child_win)
    reg_child_fail = QDialog()
    reg_child_fail_ui = register_fail.Ui_Dialog()
    reg_child_fail_ui.setupUi(reg_child_fail)
    #判断注册是否成功
    """
    判断是否存在重复命名
    """
    a=0
    # 注册成功
    if a:
        btn11 = child1_ui.pushButton
        btn11.clicked.connect(reg_child_win.show)
    #注册失败
    else:
        btn12 = child1_ui.pushButton
        btn12.clicked.connect(reg_child_fail.show)
    main.show()
    sys.exit(app.exec_())
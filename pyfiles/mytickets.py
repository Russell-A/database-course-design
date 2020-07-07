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
        self.name = ''
        Dialog.setObjectName("Dialog")
        Dialog.resize(924, 799)
        Dialog.setMinimumSize(QtCore.QSize(924, 799))
        Dialog.setStyleSheet("/**********子界面背景**********/\n"
                             "QWidget#customWidget {\n"
                             "        background: rgb(173, 202, 232);\n"
                             "}\n"
                             "\n"
                             "/**********子界面中央背景**********/\n"
                             "QWidget#Dialog {\n"
                             "        background: rgb(232, 241, 252);\n"
                             "}\n"
                             "\n"
                             "/**********主界面样式**********/\n"
                             "QWidget#mainWindow {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: rgb(232, 241, 252);\n"
                             "}\n"
                             "\n"
                             "QWidget#messageWidget {\n"
                             "        background: rgba(173, 202, 232, 50%);\n"
                             "}\n"
                             "\n"
                             "StyledWidget {\n"
                             "        qproperty-normalColor: rgb(65, 65, 65);\n"
                             "        qproperty-disableColor: rgb(180, 180, 180);\n"
                             "        qproperty-highlightColor: rgb(0, 160, 230);\n"
                             "        qproperty-errorColor: red;\n"
                             "}\n"
                             "\n"
                             "QProgressIndicator {\n"
                             "        qproperty-color: rgb(2, 65, 132);\n"
                             "}\n"
                             "\n"
                             "/**********提示**********/\n"
                             "QToolTip{\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: white;\n"
                             "        color: rgb(51, 51, 51);\n"
                             "}\n"
                             "\n"
                             "/**********菜单栏**********/\n"
                             "QMenuBar {\n"
                             "        background: rgb(187, 212, 238);\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        border-left: none;\n"
                             "        border-right: none;\n"
                             "}\n"
                             "QMenuBar::item {\n"
                             "        border: 1px solid transparent;\n"
                             "        padding: 5px 10px 5px 10px;\n"
                             "        background: transparent;\n"
                             "}\n"
                             "QMenuBar::item:enabled {\n"
                             "        color: rgb(2, 65, 132);\n"
                             "}\n"
                             "QMenuBar::item:!enabled {\n"
                             "        color: rgb(155, 155, 155);\n"
                             "}\n"
                             "QMenuBar::item:enabled:selected {\n"
                             "        border-top-color: rgb(111, 156, 207);\n"
                             "        border-bottom-color: rgb(111, 156, 207);\n"
                             "        background: rgb(198, 224, 252);\n"
                             "}\n"
                             "\n"
                             "/**********菜单**********/\n"
                             "QMenu {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: rgb(232, 241, 250);\n"
                             "}\n"
                             "QMenu::item {\n"
                             "        height: 22px;\n"
                             "        padding: 0px 25px 0px 20px;\n"
                             "}\n"
                             "QMenu::item:enabled {\n"
                             "        color: rgb(84, 84, 84);\n"
                             "}\n"
                             "QMenu::item:!enabled {\n"
                             "        color: rgb(155, 155, 155);\n"
                             "}\n"
                             "QMenu::item:enabled:selected {\n"
                             "        color: rgb(2, 65, 132);\n"
                             "        background: rgba(255, 255, 255, 200);\n"
                             "}\n"
                             "QMenu::separator {\n"
                             "        height: 1px;\n"
                             "        background: rgb(111, 156, 207);\n"
                             "}\n"
                             "QMenu::indicator {\n"
                             "        width: 13px;\n"
                             "        height: 13px;\n"
                             "}\n"
                             "QMenu::icon {\n"
                             "        padding-left: 2px;\n"
                             "        padding-right: 2px;\n"
                             "}\n"
                             "\n"
                             "/**********状态栏**********/\n"
                             "QStatusBar {\n"
                             "        background: rgb(187, 212, 238);\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        border-left: none;\n"
                             "        border-right: none;\n"
                             "        border-bottom: none;\n"
                             "}\n"
                             "QStatusBar::item {\n"
                             "    border: none;\n"
                             "    border-right: 1px solid rgb(111, 156, 207);\n"
                             "}\n"
                             "\n"
                             "/**********分组框**********/\n"
                             "QGroupBox {\n"
                             "        font-size: 15px;\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        border-radius: 4px;\n"
                             "        margin-top: 10px;\n"
                             "}\n"
                             "QGroupBox::title {\n"
                             "        color: rgb(56, 99, 154);\n"
                             "        top: -12px;\n"
                             "        left: 10px;\n"
                             "}\n"
                             "\n"
                             "/**********页签项**********/\n"
                             "QTabWidget::pane {\n"
                             "        border: none;\n"
                             "        border-top: 3px solid rgb(0, 78, 161);\n"
                             "        background: rgb(187, 212, 238);\n"
                             "}\n"
                             "QTabWidget::tab-bar {\n"
                             "        border: none;\n"
                             "}\n"
                             "QTabBar::tab {\n"
                             "        border: none;\n"
                             "        border-top-left-radius: 4px;\n"
                             "        border-top-right-radius: 4px;\n"
                             "        color: white;\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        height: 28px;\n"
                             "        min-width: 85px;\n"
                             "        margin-right: 5px;\n"
                             "        padding-left: 5px;\n"
                             "        padding-right: 5px;\n"
                             "}\n"
                             "QTabBar::tab:hover {\n"
                             "        background: rgb(0, 78, 161);\n"
                             "}\n"
                             "QTabBar::tab:selected {\n"
                             "        color: white;\n"
                             "        background: rgb(0, 78, 161);\n"
                             "}\n"
                             "\n"
                             "QTabWidget#tabWidget::pane {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: rgb(232, 241, 252);\n"
                             "        margin-top: -1px;\n"
                             "}\n"
                             "\n"
                             "QTabBar#tabBar::tab {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        border-bottom: none;\n"
                             "        color: rgb(70, 71, 73);\n"
                             "        background: transparent;\n"
                             "}\n"
                             "QTabBar#tabBar::tab:hover {\n"
                             "        color: rgb(2, 65, 132);\n"
                             "}\n"
                             "QTabBar#tabBar::tab:selected {\n"
                             "        color: rgb(2, 65, 132);\n"
                             "        background: rgb(232, 241, 252);\n"
                             "}\n"
                             "\n"
                             "/**********表头**********/\n"
                             "QHeaderView{\n"
                             "        border: none;\n"
                             "        border-bottom: 3px solid rgb(0, 78, 161);\n"
                             "        background: transparent;\n"
                             "        min-height: 30px;\n"
                             "}\n"
                             "QHeaderView::section:horizontal {\n"
                             "        border: none;\n"
                             "        color: rgb(2, 65, 132);\n"
                             "        background: transparent;\n"
                             "        padding-left: 5px;\n"
                             "}\n"
                             "QHeaderView::section:horizontal:hover {\n"
                             "        color: white;\n"
                             "        background: rgb(0, 78, 161);\n"
                             "}\n"
                             "QHeaderView::section:horizontal:pressed {\n"
                             "        color: white;\n"
                             "        background: rgb(6, 94, 187);\n"
                             "}\n"
                             "QHeaderView::up-arrow {\n"
                             "        width: 13px;\n"
                             "        height: 11px;\n"
                             "        padding-right: 5px;\n"
                             "        image: url(:/White/topArrow);\n"
                             "        subcontrol-position: center right;\n"
                             "}\n"
                             "QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {\n"
                             "        image: url(:/White/topArrowHover);\n"
                             "}\n"
                             "QHeaderView::down-arrow {\n"
                             "        width: 13px;\n"
                             "        height: 11px;\n"
                             "        padding-right: 5px;\n"
                             "        image: url(:/White/bottomArrow);\n"
                             "        subcontrol-position: center right;\n"
                             "}\n"
                             "QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {\n"
                             "        image: url(:/White/bottomArrowHover);\n"
                             "}\n"
                             "\n"
                             "/**********表格**********/\n"
                             "QTableView {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: rgb(224, 238, 255);\n"
                             "        gridline-color: rgb(111, 156, 207);\n"
                             "}\n"
                             "QTableView::item {\n"
                             "        padding-left: 5px;\n"
                             "        padding-right: 5px;\n"
                             "        border: none;\n"
                             "        background: white;\n"
                             "        border-right: 1px solid rgb(111, 156, 207);\n"
                             "        border-bottom: 1px solid rgb(111, 156, 207);\n"
                             "}\n"
                             "QTableView::item:selected {\n"
                             "        background: rgba(255, 255, 255, 100);\n"
                             "}\n"
                             "QTableView::item:selected:!active {\n"
                             "        color: rgb(65, 65, 65);\n"
                             "}\n"
                             "QTableView::indicator {\n"
                             "        width: 20px;\n"
                             "        height: 20px;\n"
                             "}\n"
                             "QTableView::indicator:enabled:unchecked {\n"
                             "        image: url(:/White/checkBox);\n"
                             "}\n"
                             "QTableView::indicator:enabled:unchecked:hover {\n"
                             "        image: url(:/White/checkBoxHover);\n"
                             "}\n"
                             "QTableView::indicator:enabled:unchecked:pressed {\n"
                             "        image: url(:/White/checkBoxPressed);\n"
                             "}\n"
                             "QTableView::indicator:enabled:checked {\n"
                             "        image: url(:/White/checkBoxChecked);\n"
                             "}\n"
                             "QTableView::indicator:enabled:checked:hover {\n"
                             "        image: url(:/White/checkBoxCheckedHover);\n"
                             "}\n"
                             "QTableView::indicator:enabled:checked:pressed {\n"
                             "        image: url(:/White/checkBoxCheckedPressed);\n"
                             "}\n"
                             "QTableView::indicator:enabled:indeterminate {\n"
                             "        image: url(:/White/checkBoxIndeterminate);\n"
                             "}\n"
                             "QTableView::indicator:enabled:indeterminate:hover {\n"
                             "        image: url(:/White/checkBoxIndeterminateHover);\n"
                             "}\n"
                             "QTableView::indicator:enabled:indeterminate:pressed {\n"
                             "        image: url(:/White/checkBoxIndeterminatePressed);\n"
                             "}\n"
                             "\n"
                             "/**********滚动条-水平**********/\n"
                             "QScrollBar:horizontal {\n"
                             "        height: 20px;\n"
                             "        background: transparent;\n"
                             "        margin-top: 3px;\n"
                             "        margin-bottom: 3px;\n"
                             "}\n"
                             "QScrollBar::handle:horizontal {\n"
                             "        height: 20px;\n"
                             "        min-width: 30px;\n"
                             "        background: rgb(170, 200, 230);\n"
                             "        margin-left: 15px;\n"
                             "        margin-right: 15px;\n"
                             "}\n"
                             "QScrollBar::handle:horizontal:hover {\n"
                             "        background: rgb(165, 195, 225);\n"
                             "}\n"
                             "QScrollBar::sub-line:horizontal {\n"
                             "        width: 15px;\n"
                             "        background: transparent;\n"
                             "        image: url(:/White/arrowLeft);\n"
                             "        subcontrol-position: left;\n"
                             "}\n"
                             "QScrollBar::add-line:horizontal {\n"
                             "        width: 15px;\n"
                             "        background: transparent;\n"
                             "        image: url(:/White/arrowRight);\n"
                             "        subcontrol-position: right;\n"
                             "}\n"
                             "QScrollBar::sub-line:horizontal:hover {\n"
                             "        background: rgb(170, 200, 230);\n"
                             "}\n"
                             "QScrollBar::add-line:horizontal:hover {\n"
                             "        background: rgb(170, 200, 230);\n"
                             "}\n"
                             "QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {\n"
                             "        background: transparent;\n"
                             "}\n"
                             "\n"
                             "/**********滚动条-垂直**********/\n"
                             "QScrollBar:vertical {\n"
                             "        width: 20px;\n"
                             "        background: transparent;\n"
                             "        margin-left: 3px;\n"
                             "        margin-right: 3px;\n"
                             "}\n"
                             "QScrollBar::handle:vertical {\n"
                             "        width: 20px;\n"
                             "        min-height: 30px;\n"
                             "        background: rgb(170, 200, 230);\n"
                             "        margin-top: 15px;\n"
                             "        margin-bottom: 15px;\n"
                             "}\n"
                             "QScrollBar::handle:vertical:hover {\n"
                             "        background: rgb(165, 195, 225);\n"
                             "}\n"
                             "QScrollBar::sub-line:vertical {\n"
                             "        height: 15px;\n"
                             "        background: transparent;\n"
                             "        image: url(:/White/topArrow);\n"
                             "        subcontrol-position: top;\n"
                             "}\n"
                             "QScrollBar::add-line:vertical {\n"
                             "        height: 15px;\n"
                             "        background: transparent;\n"
                             "        image: url(:/White/bottomArrow);\n"
                             "        subcontrol-position: bottom;\n"
                             "}\n"
                             "QScrollBar::sub-line:vertical:hover {\n"
                             "        background: rgb(170, 200, 230);\n"
                             "}\n"
                             "QScrollBar::add-line:vertical:hover {\n"
                             "        background: rgb(170, 200, 230);\n"
                             "}\n"
                             "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                             "        background: transparent;\n"
                             "}\n"
                             "\n"
                             "QScrollBar#verticalScrollBar:vertical {\n"
                             "        margin-top: 30px;\n"
                             "}\n"
                             "\n"
                             "/**********下拉列表**********/\n"
                             "QComboBox {\n"
                             "        height: 25px;\n"
                             "        width: 3.5em;\n"
                             "        border-radius: 4px;\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: white;\n"
                             "}\n"
                             "QComboBox:enabled {\n"
                             "        color: rgb(84, 84, 84);\n"
                             "}\n"
                             "QComboBox:!enabled {\n"
                             "        color: rgb(80, 80, 80);\n"
                             "}\n"
                             "QComboBox:enabled:hover, QComboBox:enabled:focus {\n"
                             "        color: rgb(51, 51, 51);\n"
                             "}\n"
                             "QComboBox::drop-down {\n"
                             "        width: 20px;\n"
                             "        border: none;\n"
                             "        background: transparent;\n"
                             "}\n"
                             "QComboBox::drop-down:hover {\n"
                             "        background: rgba(255, 255, 255, 30);\n"
                             "}\n"
                             "QComboBox::down-arrow {\n"
                             "        image: url(:/White/arrowBottom);\n"
                             "}\n"
                             "QComboBox::down-arrow:on {\n"
                             "        /**top: 1px;**/\n"
                             "}\n"
                             "QComboBox QAbstractItemView {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: white;\n"
                             "        outline: none;\n"
                             "}\n"
                             "QComboBox QAbstractItemView::item {\n"
                             "        height: 25px;\n"
                             "        color: rgb(73, 73, 73);\n"
                             "}\n"
                             "QComboBox QAbstractItemView::item:selected {\n"
                             "        background: rgb(232, 241, 250);\n"
                             "        color: rgb(2, 65, 132);\n"
                             "}\n"
                             "\n"
                             "/**********进度条**********/\n"
                             "QProgressBar{\n"
                             "        border: none;\n"
                             "        text-align: center;\n"
                             "        color: white;\n"
                             "        background: rgb(173, 202, 232);\n"
                             "}\n"
                             "QProgressBar::chunk {\n"
                             "        background: rgb(16, 135, 209);\n"
                             "}\n"
                             "\n"
                             "QProgressBar#progressBar {\n"
                             "        border: none;\n"
                             "        text-align: center;\n"
                             "        color: white;\n"
                             "        background-color: transparent;\n"
                             "        background-image: url(\":/White/progressBar\");\n"
                             "        background-repeat: repeat-x;\n"
                             "}\n"
                             "QProgressBar#progressBar::chunk {\n"
                             "        border: none;\n"
                             "        background-color: transparent;\n"
                             "        background-image: url(\":/White/progressBarChunk\");\n"
                             "        background-repeat: repeat-x;\n"
                             "}\n"
                             "\n"
                             "/**********复选框**********/\n"
                             "QCheckBox{\n"
                             "        spacing: 5px;\n"
                             "}\n"
                             "QCheckBox:enabled:checked{\n"
                             "        color: rgb(2, 65, 132);\n"
                             "}\n"
                             "QCheckBox:enabled:!checked{\n"
                             "        color: rgb(70, 71, 73);\n"
                             "}\n"
                             "QCheckBox:enabled:hover{\n"
                             "        color: rgb(0, 78, 161);\n"
                             "}\n"
                             "QCheckBox:!enabled{\n"
                             "        color: rgb(80, 80, 80);\n"
                             "}\n"
                             "QCheckBox::indicator {\n"
                             "        width: 20px;\n"
                             "        height: 20px;\n"
                             "}\n"
                             "QCheckBox::indicator:unchecked {\n"
                             "        image: url(:/White/checkBox);\n"
                             "}\n"
                             "QCheckBox::indicator:unchecked:hover {\n"
                             "        image: url(:/White/checkBoxHover);\n"
                             "}\n"
                             "QCheckBox::indicator:unchecked:pressed {\n"
                             "        image: url(:/White/checkBoxPressed);\n"
                             "}\n"
                             "QCheckBox::indicator:checked {\n"
                             "        image: url(:/White/checkBoxChecked);\n"
                             "}\n"
                             "QCheckBox::indicator:checked:hover {\n"
                             "        image: url(:/White/checkBoxCheckedHover);\n"
                             "}\n"
                             "QCheckBox::indicator:checked:pressed {\n"
                             "        image: url(:/White/checkBoxCheckedPressed);\n"
                             "}\n"
                             "QCheckBox::indicator:indeterminate {\n"
                             "        image: url(:/White/checkBoxIndeterminate);\n"
                             "}\n"
                             "QCheckBox::indicator:indeterminate:hover {\n"
                             "        image: url(:/White/checkBoxIndeterminateHover);\n"
                             "}\n"
                             "QCheckBox::indicator:indeterminate:pressed {\n"
                             "        image: url(:/White/checkBoxIndeterminatePressed);\n"
                             "}\n"
                             "\n"
                             "/**********单选框**********/\n"
                             "QRadioButton{\n"
                             "        spacing: 5px;\n"
                             "}\n"
                             "QRadioButton:enabled:checked{\n"
                             "        color: rgb(2, 65, 132);\n"
                             "}\n"
                             "QRadioButton:enabled:!checked{\n"
                             "        color: rgb(70, 71, 73);\n"
                             "}\n"
                             "QRadioButton:enabled:hover{\n"
                             "        color: rgb(0, 78, 161);\n"
                             "}\n"
                             "QRadioButton:!enabled{\n"
                             "        color: rgb(80, 80, 80);\n"
                             "}\n"
                             "QRadioButton::indicator {\n"
                             "        width: 20px;\n"
                             "        height: 20px;\n"
                             "}\n"
                             "QRadioButton::indicator:unchecked {\n"
                             "        image: url(:/White/radioButton);\n"
                             "}\n"
                             "QRadioButton::indicator:unchecked:hover {\n"
                             "        image: url(:/White/radioButtonHover);\n"
                             "}\n"
                             "QRadioButton::indicator:unchecked:pressed {\n"
                             "        image: url(:/White/radioButtonPressed);\n"
                             "}\n"
                             "QRadioButton::indicator:checked {\n"
                             "        image: url(:/White/radioButtonChecked);\n"
                             "}\n"
                             "QRadioButton::indicator:checked:hover {\n"
                             "        image: url(:/White/radioButtonCheckedHover);\n"
                             "}\n"
                             "QRadioButton::indicator:checked:pressed {\n"
                             "        image: url(:/White/radioButtonCheckedPressed);\n"
                             "}\n"
                             "\n"
                             "/**********输入框**********/\n"
                             "QLineEdit {\n"
                             "        border-radius: 4px;\n"
                             "        height: 25px;\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: white;\n"
                             "}\n"
                             "QLineEdit:enabled {\n"
                             "        color: rgb(84, 84, 84);\n"
                             "}\n"
                             "QLineEdit:enabled:hover, QLineEdit:enabled:focus {\n"
                             "        color: rgb(51, 51, 51);\n"
                             "}\n"
                             "QLineEdit:!enabled {\n"
                             "        color: rgb(80, 80, 80);\n"
                             "}\n"
                             "\n"
                             "/**********文本编辑框**********/\n"
                             "QTextEdit {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        color: rgb(70, 71, 73);\n"
                             "        background: rgb(187, 212, 238);\n"
                             "}\n"
                             "\n"
                             "/**********滚动区域**********/\n"
                             "QScrollArea {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: rgb(187, 212, 238);\n"
                             "}\n"
                             "\n"
                             "/**********滚动区域**********/\n"
                             "QWidget#transparentWidget {\n"
                             "        background: transparent;\n"
                             "}\n"
                             "\n"
                             "/**********微调器**********/\n"
                             "QSpinBox {\n"
                             "        border-radius: 4px;\n"
                             "        height: 24px;\n"
                             "        min-width: 40px;\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: white;\n"
                             "}\n"
                             "QSpinBox:enabled {\n"
                             "        color: rgb(60, 60, 60);\n"
                             "}\n"
                             "QSpinBox:enabled:hover, QSpinBox:enabled:focus {\n"
                             "        color: rgb(51, 51, 51);\n"
                             "}\n"
                             "QSpinBox:!enabled {\n"
                             "        color: rgb(210, 210, 210);\n"
                             "        background: transparent;\n"
                             "}\n"
                             "QSpinBox::up-button {\n"
                             "        border-left: 1px solid rgb(111, 156, 207);\n"
                             "        width: 18px;\n"
                             "        height: 12px;\n"
                             "        border-top-right-radius: 4px;\n"
                             "        image: url(:/White/upButton);\n"
                             "}\n"
                             "QSpinBox::up-button:!enabled {\n"
                             "        background: transparent;\n"
                             "}\n"
                             "QSpinBox::up-button:enabled:hover {\n"
                             "        background: rgb(255, 255, 255, 30);\n"
                             "}\n"
                             "QSpinBox::down-button {\n"
                             "        border-left: 1px solid rgb(111, 156, 207);\n"
                             "        width: 18px;\n"
                             "        height: 12px;\n"
                             "        border-bottom-right-radius: 4px;\n"
                             "        image: url(:/White/downButton);\n"
                             "}\n"
                             "QSpinBox::down-button:!enabled {\n"
                             "        background: transparent;\n"
                             "}\n"
                             "QSpinBox::down-button:hover {\n"
                             "        background: rgb(255, 255, 255, 30);\n"
                             "}\n"
                             "\n"
                             "/**********标签**********/\n"
                             "\n"
                             "QLabel#skinLabel[colorProperty=\"normal\"] {\n"
                             "        color: rgb(56, 99, 154);\n"
                             "}\n"
                             "QLabel#skinLabel[colorProperty=\"highlight\"] {\n"
                             "        color: rgb(0, 160, 230);\n"
                             "}\n"
                             "\n"
                             "QLabel#informationLabel {\n"
                             "        qproperty-pixmap: url(:/White/information);\n"
                             "}\n"
                             "\n"
                             "QLabel#errorLabel {\n"
                             "        qproperty-pixmap: url(:/White/error);\n"
                             "}\n"
                             "\n"
                             "QLabel#successLabel {\n"
                             "        qproperty-pixmap: url(:/White/success);\n"
                             "}\n"
                             "\n"
                             "QLabel#questionLabel {\n"
                             "        qproperty-pixmap: url(:/White/question);\n"
                             "}\n"
                             "\n"
                             "QLabel#warningLabel {\n"
                             "        qproperty-pixmap: url(:/White/warning);\n"
                             "}\n"
                             "\n"
                             "QLabel#groupLabel {\n"
                             "        color: rgb(56, 99, 154);\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        font-size: 15px;\n"
                             "        border-top-color: transparent;\n"
                             "        border-right-color: transparent;\n"
                             "        border-left-color: transparent;\n"
                             "}\n"
                             "\n"
                             "/**********按钮**********/\n"
                             "QToolButton \n"
                             "{\n"
                             "        border: none;\n"
                             "        color: rgb(2, 65, 132);\n"
                             "        background: transparent;\n"
                             "        padding: 10px;\n"
                             "        qproperty-iconSize: 32px 32px;\n"
                             "        qproperty-toolButtonStyle: ToolButtonTextUnderIcon;\n"
                             "}\n"
                             "QToolButton#nsccButton:hover {\n"
                             "        background: rgb(187, 212, 238);\n"
                             "}\n"
                             "\n"
                             "QToolButton#transferButton {\n"
                             "        border: none;\n"
                             "        color: rgb(2, 65, 132);\n"
                             "        background: transparent;\n"
                             "        padding: 10px;\n"
                             "        qproperty-icon: url(:/White/transfer);\n"
                             "        qproperty-iconSize: 32px 32px;\n"
                             "        qproperty-toolButtonStyle: ToolButtonTextUnderIcon;\n"
                             "}\n"
                             "QToolButton#transferButton:hover {\n"
                             "        background: rgb(187, 212, 238);\n"
                             "}\n"
                             "\n"
                             "/**********按钮**********/\n"
                             "QPushButton{\n"
                             "        border-radius: 4px;\n"
                             "        border: none;\n"
                             "        width: 75px;\n"
                             "        height: 25px;\n"
                             "}\n"
                             "QPushButton:enabled {\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton:!enabled {\n"
                             "        background: rgb(180, 180, 180);\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton:enabled:hover{\n"
                             "        background: rgb(100, 160, 220);\n"
                             "}\n"
                             "QPushButton:enabled:pressed{\n"
                             "        background: rgb(0, 78, 161);\n"
                             "}\n"
                             "\n"
                             "QPushButton#blueButton {\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton#blueButton:enabled {\n"
                             "        background: rgb(0, 78, 161);\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton:!enabled {\n"
                             "        background: rgb(180, 180, 180);\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton#blueButton:enabled:hover {\n"
                             "        background: rgb(2, 65, 132);\n"
                             "}\n"
                             "QPushButton#blueButton:enabled:pressed {\n"
                             "        background: rgb(6, 94, 187);\n"
                             "}\n"
                             "\n"
                             "QPushButton#Search {\n"
                             "        border-left: 1px solid rgb(111, 156, 207);\n"
                             "        background: rgb(30, 144, 255);\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton#Search:enabled:hover{\n"
                             "        background: rgb(187, 212, 238);\n"
                             "}\n"
                             "QPushButton#Search:enabled:pressed{\n"
                             "        background: rgb(120, 170, 220);\n"
                             "}\n"
                             "\n"
                             "QPushButton#linkButton {\n"
                             "        background: transparent;\n"
                             "        color: rgb(0, 160, 230);\n"
                             "        text-align:left;\n"
                             "}\n"
                             "QPushButton#linkButton:hover {\n"
                             "        color: rgb(20, 185, 255);\n"
                             "        text-decoration: underline;\n"
                             "}\n"
                             "QPushButton#linkButton:pressed {\n"
                             "        color: rgb(0, 160, 230);\n"
                             "}\n"
                             "\n"
                             "QPushButton#transparentButton {\n"
                             "        background: transparent;\n"
                             "}\n"
                             "\n"
                             "/*****************标题栏按钮*******************/\n"
                             "\n"
                             "QPushButton#skinButton:hover {\n"
                             "        image: url(:/White/skin);\n"
                             "}\n"
                             "QPushButton#skinButton:pressed {\n"
                             "        image: url(:/White/skinPressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#closeTipButton:pressed {\n"
                             "        border-image: url(:/White/closePressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#changeSkinButton{\n"
                             "        border-radius: 4px;\n"
                             "        border: 2px solid rgb(111, 156, 207);\n"
                             "        background: rgb(204, 227, 252);\n"
                             "}\n"
                             "QPushButton#changeSkinButton:hover{\n"
                             "        border-color: rgb(60, 150, 200);\n"
                             "}\n"
                             "QPushButton#changeSkinButton:pressed, QPushButton#changeSkinButton:checked{\n"
                             "        border-color: rgb(0, 160, 230);\n"
                             "}\n"
                             "\n"
                             "\n"
                             "QPushButton#openButton {\n"
                             "        border-radius: none;\n"
                             "        image: url(:/White/open);\n"
                             "        background: transparent;\n"
                             "}\n"
                             "QPushButton#openButton:hover {\n"
                             "        image: url(:/White/openHover);\n"
                             "}\n"
                             "QPushButton#openButton:pressed {\n"
                             "        image: url(:/White/openPressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#deleteButton {\n"
                             "        border-radius: none;\n"
                             "        image: url(:/White/delete);\n"
                             "        background: transparent;\n"
                             "}\n"
                             "QPushButton#deleteButton:hover {\n"
                             "        image: url(:/White/deleteHover);\n"
                             "}\n"
                             "QPushButton#deleteButton:pressed {\n"
                             "        image: url(:/White/deletePressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#menuButton {\n"
                             "        text-align: left center;\n"
                             "        padding-left: 3px;\n"
                             "        color: rgb(84, 84, 84);\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: white;\n"
                             "}\n"
                             "QPushButton#menuButton::menu-indicator{\n"
                             "        subcontrol-position: right center;\n"
                             "        subcontrol-origin: padding;\n"
                             "        image: url(:/White/arrowBottom);\n"
                             "        padding-right: 3px;\n"
                             "}")
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 100, 241, 181))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.choice3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.choice3.setObjectName("choice3")
        self.gridLayout_2.addWidget(self.choice3, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.choice2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.choice2.setObjectName("choice2")
        self.gridLayout_2.addWidget(self.choice2, 3, 0, 1, 1)
        self.ticket_info = QtWidgets.QGroupBox(Dialog)
        self.ticket_info.setGeometry(QtCore.QRect(430, 10, 461, 771))
        self.ticket_info.setObjectName("ticket_info")
        self.ticketdetails = QtWidgets.QPushButton(self.ticket_info)
        self.ticketdetails.setGeometry(QtCore.QRect(300, 200, 91, 28))
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
        self.ticket_info_2.setGeometry(QtCore.QRect(0, 240, 461, 241))
        self.ticket_info_2.setObjectName("ticket_info_2")
        self.ticketdetails_2 = QtWidgets.QPushButton(self.ticket_info_2)
        self.ticketdetails_2.setGeometry(QtCore.QRect(300, 200, 91, 28))
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
        self.ticket_info_3.setGeometry(QtCore.QRect(0, 490, 461, 241))
        self.ticket_info_3.setObjectName("ticket_info_3")
        self.ticketdetails_3 = QtWidgets.QPushButton(self.ticket_info_3)
        self.ticketdetails_3.setGeometry(QtCore.QRect(300, 200, 91, 28))
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
        self.lastpage_btn.setGeometry(QtCore.QRect(130, 740, 93, 28))
        self.lastpage_btn.setObjectName("lastpage_btn")
        self.nextpage_btn = QtWidgets.QPushButton(self.ticket_info)
        self.nextpage_btn.setGeometry(QtCore.QRect(260, 740, 93, 28))
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
                      'where 用户名 = :username and 出发时间 > :specialtime')  # 输入SQL语句  改成大于号就好了，但为了方便测试先不改
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



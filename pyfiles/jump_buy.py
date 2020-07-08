# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jump_buy_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
import pyodbc
import time

class Ui_Dialog_jump_buy(object):
    num = -1
    state = -1
    def setupUi(self, Dialog_jump_buy):
        Dialog_jump_buy.setObjectName("Dialog_jump_buy")
        Dialog_jump_buy.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/flight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_jump_buy.setStyleSheet("/**********子界面背景**********/\n"
                                      "QWidget#customWidget {\n"
                                      "        background: rgb(173, 202, 232);\n"
                                      "}\n"
                                      "\n"
                                      "/**********子界面中央背景**********/\n"
                                      "QWidget#Dialog_jump_buy {\n"
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
                                      "\n"
                                      "QPushButton#menuButton::menu-indicator{\n"
                                      "        subcontrol-position: right center;\n"
                                      "        subcontrol-origin: padding;\n"
                                      "        image: url(:/White/arrowBottom);\n"
                                      "        padding-right: 3px;\n"
                                      "}\n"
                                      "")
        Dialog_jump_buy.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog_jump_buy)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.com_class = QtWidgets.QComboBox(Dialog_jump_buy)
        self.com_class.setObjectName("com_class")
        self.com_class.addItem("")
        self.com_class.addItem("")
        self.com_class.addItem("")
        self.horizontalLayout.addWidget(self.com_class)
        self.label_5 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.remain_num = QtWidgets.QLabel(Dialog_jump_buy)
        self.remain_num.setAlignment(QtCore.Qt.AlignCenter)
        self.remain_num.setObjectName("remain_num")
        self.horizontalLayout.addWidget(self.remain_num)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.sex = QtWidgets.QComboBox(Dialog_jump_buy)
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.horizontalLayout_4.addWidget(self.sex)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.combo_kind = QtWidgets.QComboBox(Dialog_jump_buy)
        self.combo_kind.setObjectName("combo_kind")
        self.combo_kind.addItem("")
        self.combo_kind.addItem("")
        self.combo_kind.addItem("")
        self.combo_kind.addItem("")
        self.combo_kind.addItem("")
        self.horizontalLayout_6.addWidget(self.combo_kind)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.name = QtWidgets.QLineEdit(Dialog_jump_buy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setObjectName("name")
        self.horizontalLayout_5.addWidget(self.name)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.identity_num = QtWidgets.QLineEdit(Dialog_jump_buy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.identity_num.sizePolicy().hasHeightForWidth())
        self.identity_num.setSizePolicy(sizePolicy)
        self.identity_num.setObjectName("identity_num")
        self.horizontalLayout_3.addWidget(self.identity_num)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(Dialog_jump_buy)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.phone_num = QtWidgets.QLineEdit(Dialog_jump_buy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone_num.sizePolicy().hasHeightForWidth())
        self.phone_num.setSizePolicy(sizePolicy)
        self.phone_num.setObjectName("phone_num")
        self.horizontalLayout_2.addWidget(self.phone_num)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(Dialog_jump_buy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog_jump_buy)
        self.pushButton.clicked.connect(self.insert_tacket)
        self.com_class.currentIndexChanged.connect(self.remain_tacket)
        QtCore.QMetaObject.connectSlotsByName(Dialog_jump_buy)

    def retranslateUi(self, Dialog_jump_buy):
        _translate = QtCore.QCoreApplication.translate
        Dialog_jump_buy.setWindowTitle(_translate("Dialog_jump_buy", "购买机票"))
        self.label_6.setText(_translate("Dialog_jump_buy", "舱位："))
        self.com_class.setItemText(0, _translate("Dialog_jump_buy", "头等舱"))
        self.com_class.setItemText(1, _translate("Dialog_jump_buy", "商务舱"))
        self.com_class.setItemText(2, _translate("Dialog_jump_buy", "经济舱"))
        self.label_5.setText(_translate("Dialog_jump_buy", "剩余票数："))
        self.remain_num.setText(_translate("Dialog_jump_buy", "     "))
        self.label_2.setText(_translate("Dialog_jump_buy", "    性别："))
        self.sex.setItemText(0, _translate("Dialog_jump_buy", "男"))
        self.sex.setItemText(1, _translate("Dialog_jump_buy", "女"))
        self.label_8.setText(_translate("Dialog_jump_buy", "乘客类别："))
        self.combo_kind.setItemText(0, _translate("Dialog_jump_buy", "成人"))
        self.combo_kind.setItemText(1, _translate("Dialog_jump_buy", "小孩"))
        self.combo_kind.setItemText(2, _translate("Dialog_jump_buy", "老人"))
        self.combo_kind.setItemText(3, _translate("Dialog_jump_buy", "病人"))
        self.combo_kind.setItemText(4, _translate("Dialog_jump_buy", "残疾"))
        self.label_7.setText(_translate("Dialog_jump_buy", "乘客姓名："))
        self.label_3.setText(_translate("Dialog_jump_buy", "身份证号："))
        self.label_4.setText(_translate("Dialog_jump_buy", "联系电话"))
        self.pushButton.setText(_translate("Dialog_jump_buy", "购买"))


    def insert_tacket(self):
        dairport = ''
        aairport = ''
        tacket_num = ()
        conn = pyodbc.connect(
            'DRIVER={SQL SERVER NATIVE CLIENT 10.0};SERVER=127.0.0.1;DATABASE=air;UID=sa;PWD=123456')
        conn.autocommit = False
        # conn.set_attr(pyodbc.SQL_ATTR_TXN_ISOLATION, pyodbc.SQL_TXN_SERIALIZABLE)
        cursor = conn.cursor()
        sql_wait = "select 数量 from 进程数 where 航程号 = ?"
        result = cursor.execute(sql_wait, self.num).fetchall()

        wait = result[0][0]

        if (wait>=0):
            reply = QMessageBox.information(self,
                                        "提示",
                                        "大约有"+str(wait)+"人正在排队买票，是否进入队列？",
                                        QMessageBox.Yes | QMessageBox.No)
            if (reply == QMessageBox.Yes):
                sql_up = "update 进程数 set 数量 = 数量+1 where 航程号 = ?"
                cursor.execute(sql_up, self.num)
                cursor.commit()
            else:
                return

        # 设置行锁直到事务结束
        sql_lock = "select * from 飞行计划安排 with (xlock,paglock) where 航程号 = ?"
        cursor.execute(sql_lock, self.num)

        # time.sleep(20)

        if (self.state == 0):
            sql = "select *"\
                  " from 飞行计划安排 inner join 航班 on 飞行计划安排.航班编号 = 航班.航班编号"\
                  " inner join 机场 on 机场代码 = 出发机场代码"\
                  " inner join 机场 as b on b.机场代码 = 到达机场代码"\
                  " where 航程号 = ?"

            result = (cursor.execute(sql, self.num).fetchall())
            dairport = result[0][30]
            aairport = result[0][33]
            tacket_num = result[0][6:9]
        if (self.state == 1):
            sql = "select *"\
                  " from 飞行计划安排 inner join 航班 on 飞行计划安排.航班编号 = 航班.航班编号"\
                  " inner join 机场 on 机场代码 = 出发机场代码"\
                  " inner join 机场 as b on b.机场代码 = 经停机场代码"\
                  " where 航程号 = ?"

            result = (cursor.execute(sql, self.num).fetchall())
            dairport = result[0][30]
            aairport = result[0][33]
            tacket_num = result[0][12:15]
        if (self.state == 2):
            sql = "select *"\
                  " from 飞行计划安排 inner join 航班 on 飞行计划安排.航班编号 = 航班.航班编号"\
                  " inner join 机场 on 机场代码 = 出发机场代码"\
                  " inner join 机场 as b on b.机场代码 = 经停机场代码"\
                  " where 航程号 = ?"

            result = (cursor.execute(sql, self.num).fetchall())
            dairport = result[0][30]
            aairport = result[0][33]
            tacket_num = result[0][9:12]
        kind = {}
        kind['经济舱'] = 0
        kind['商务舱'] = 1
        kind['头等舱'] = 2
        state_text = ['(开始-到达)','(开始-经停)','(经停-到达)']
        cart = self.com_class.currentText()

        print(tacket_num)

        tacket = tacket_num[kind[cart]]
        print(tacket)
        if (tacket is None):
            print('none')
            tacket = 0
        sex = self.sex.currentText()
        kind_ = self.combo_kind.currentText()
        tele = self.phone_num.text()
        id = self.identity_num.text()
        name = self.name.text()
        if (len(name)<1 or len(id)<1 or len(tele)<1):
            reply = QMessageBox.warning(self,
                                        "提示",
                                        "请先填写好信息！",
                                        QMessageBox.Yes)
            sql_up = "update 进程数 set 数量 = 数量-1 where 航程号 = ?"
            cursor.execute(sql_up, self.num)
            cursor.commit()
            conn.close()
        elif (tacket>0):

            update_sql = "update 飞行计划安排 set [" + cart + state_text[self.state]+"剩余座位] = [" + cart + state_text[self.state]+"剩余座位]-1"\
                                                         " where 航程号=?"
            result_up = cursor.execute(update_sql, self.num)

            if (self.state == 0):
                sql_1 = "update 飞行计划安排 set [" + cart + state_text[1]+"剩余座位] = [" + cart + state_text[1]+"剩余座位]-1"\
                                                         " where 航程号=?"
                cursor.execute(sql_1,self.num)
                sql_2 = "update 飞行计划安排 set [" + cart + state_text[2]+"剩余座位] = [" + cart + state_text[2]+"剩余座位]-1"\
                                                         " where 航程号=?"
                cursor.execute(sql_2,self.num)
            else:
                sql_1 = "update 飞行计划安排 set [" + cart + state_text[0] + "剩余座位] = [" + cart + state_text[0]+"剩余座位]-1"\
                                                         " where 航程号=?"
                cursor.execute(sql_1, self.num)
            insert_sql = "insert into 订票 values (?,?,?,?,?,?,?,?,?,?,?)"
            result_in = cursor.execute(insert_sql, self.num, dairport, aairport, str(tacket), cart, self.username, name, sex, kind_, str(id), str(tele))
            print('insert complete')
            cursor.commit()
            print('update complete')

            reply = QMessageBox.information(self,
                                        "提示",
                                        "购票成功！是否继续买票？",
                                        QMessageBox.Yes | QMessageBox.No)
            if (reply == QMessageBox.Yes):
                conn.set_attr(pyodbc.SQL_ATTR_TXN_ISOLATION, pyodbc.SQL_TXN_READ_UNCOMMITTED)

                sql_up = "update 进程数 set 数量 = 数量-1 where 航程号 = ?"
                cursor.execute(sql_up, self.num)
                cursor.commit()

                conn.close()
                self.phone_num.setText('')
                self.identity_num.setText('')
                self.name.setText('')
            else:
                conn.set_attr(pyodbc.SQL_ATTR_TXN_ISOLATION, pyodbc.SQL_TXN_READ_UNCOMMITTED)

                sql_up = "update 进程数 set 数量 = 数量-1 where 航程号 = ?"
                cursor.execute(sql_up, self.num)
                cursor.commit()

                conn.close()
                self.close()
        else:
            reply = QMessageBox.warning(self,
                                        "提示",
                                        "没有余票！",
                                        QMessageBox.Yes | QMessageBox.No)
            conn.set_attr(pyodbc.SQL_ATTR_TXN_ISOLATION, pyodbc.SQL_TXN_READ_UNCOMMITTED)

            sql_up = "update 进程数 set 数量 = 数量-1 where 航程号 = ?"
            cursor.execute(sql_up, self.num)
            cursor.commit()

            conn.close()
    def remain_tacket(self):
        tacket_num = ()
        conn = pyodbc.connect(
            'DRIVER={SQL SERVER NATIVE CLIENT 10.0};SERVER=127.0.0.1;DATABASE=air;UID=sa;PWD=123456')
        if (self.state == 0):
            sql = "select *"\
                  " from 飞行计划安排 inner join 航班 on 飞行计划安排.航班编号 = 航班.航班编号"\
                  " inner join 机场 on 机场代码 = 出发机场代码"\
                  " inner join 机场 as b on b.机场代码 = 到达机场代码"\
                  " where 航程号 = ?"
            cursor = conn.cursor()
            result = (cursor.execute(sql, self.num).fetchall())
            tacket_num = result[0][6:9]
        if (self.state == 1):
            sql = "select *"\
                  " from 飞行计划安排 inner join 航班 on 飞行计划安排.航班编号 = 航班.航班编号"\
                  " inner join 机场 on 机场代码 = 出发机场代码"\
                  " inner join 机场 as b on b.机场代码 = 经停机场代码"\
                  " where 航程号 = ?"
            cursor = conn.cursor()
            result = (cursor.execute(sql, self.num).fetchall())
            tacket_num = result[0][12:15]
        if (self.state == 2):
            sql = "select *"\
                  " from 飞行计划安排 inner join 航班 on 飞行计划安排.航班编号 = 航班.航班编号"\
                  " inner join 机场 on 机场代码 = 出发机场代码"\
                  " inner join 机场 as b on b.机场代码 = 经停机场代码"\
                  " where 航程号 = ?"
            cursor = conn.cursor()
            result = (cursor.execute(sql, self.num).fetchall())
            tacket_num = result[0][9:12]
        kind = {}
        kind['经济舱'] = 0
        kind['商务舱'] = 1
        kind['头等舱'] = 2
        cart = self.com_class.currentText()
        tacket = tacket_num[kind[cart]]
        if (tacket is None):
            tacket = 0
        self.remain_num.setText(str(tacket))
        conn.close()

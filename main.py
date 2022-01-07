# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QHBoxLayout, QPlainTextEdit, QPushButton, QLineEdit, QLabel, QScrollArea, QSizePolicy, QTreeView, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import QCoreApplication, QEasingCurve, QParallelAnimationGroup, QPoint, QPropertyAnimation, QRect, QSize, Qt, QSettings, qsrand
from time import sleep
import subprocess
import webbrowser


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        global attach_files_o
        attach_files_o = ([], '')

        Dialog.setObjectName("Dialog")
        Dialog.resize(851, 567)
        Dialog.setStyleSheet("border-radius:35px")
        Dialog.setMinimumSize(851, 567)
        Dialog.setMaximumSize(851, 567)
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)

        self.treeView_3 = QtWidgets.QTreeView(Dialog)
        self.treeView_3.setGeometry(QtCore.QRect(0, 0, 851, 567))
        self.treeView_3.setStyleSheet("background-image: url(images/background.jpg);")
        self.treeView_3.setObjectName("treeView_3")

        self.new_b = QtWidgets.QPushButton(Dialog)
        self.new_b.setGeometry(QtCore.QRect(332, 140, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.new_b.setFont(font)
        self.new_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.new_b.setStyleSheet("background-image:url();\n"
                                 "background-color: rgb();\n"
                                 "color: rgb();\n"
                                 "background-image: url(images/new.png);\n"
                                 "border-radius: 100px;")
        self.new_b.setText("")
        self.new_b.setObjectName("new_b")

        self.edit_b = QtWidgets.QPushButton(Dialog)
        self.edit_b.setGeometry(QtCore.QRect(628, 156, 170, 170))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.edit_b.setFont(font)
        self.edit_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_b.setStyleSheet("background-image: url(images/contribute.png);\n"
                                  "background-color: rgb();\n"
                                  "color: rgb();\n"
                                  "border-radius: 85px;")
        self.edit_b.setText("")
        self.edit_b.setObjectName("edit_b")

        self.read_b = QtWidgets.QPushButton(Dialog)
        self.read_b.setGeometry(QtCore.QRect(83, 156, 170, 170))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.read_b.setFont(font)
        self.read_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.read_b.setStyleSheet("background-image: url(images/read.png);\n"
                                  "background-color: rgb();\n"
                                  "color: rgb();\n"
                                  "border-radius: 85px;")
        self.read_b.setText("")
        self.read_b.setObjectName("read_b")

        self.read_l = QtWidgets.QLabel(Dialog)
        self.read_l.setGeometry(QtCore.QRect(145, 437, 49, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.read_l.setFont(font)
        self.read_l.setStyleSheet("background-image: url();\n"
                                  "background-color: rgb();\n"
                                  "color: white;")
        self.read_l.setObjectName("read_l")

        self.edit_l = QtWidgets.QLabel(Dialog)
        self.edit_l.setGeometry(QtCore.QRect(667, 440, 98, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.edit_l.setFont(font)
        self.edit_l.setStyleSheet("background-image: url();\n"
                                  "background-color: rgb();\n"
                                  "color: white;")
        self.edit_l.setObjectName("edit_l")

        self.new_l = QtWidgets.QLabel(Dialog)
        self.new_l.setGeometry(QtCore.QRect(414, 455, 49, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.new_l.setFont(font)
        self.new_l.setStyleSheet("background-image: url();\n"
                                 "background-color: rgb();\n"
                                 "color: white;")
        self.new_l.setObjectName("new_l")

        self.close = QtWidgets.QPushButton(Dialog)
        self.close.setObjectName("close")
        self.close.setGeometry(QRect(807, 12, 32, 32))
        self.close.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.close.setStyleSheet("background-image: url(images/close.png);")

        self.minimize = QtWidgets.QPushButton(Dialog)
        self.minimize.setObjectName("minimize")
        self.minimize.setGeometry(QRect(770, 12, 32, 32))
        self.minimize.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.minimize.setStyleSheet("background-image: url(images/mini.png);")

        self.treeView = QtWidgets.QTreeView(Dialog)
        self.treeView.setObjectName("treeView")
        self.treeView.setGeometry(QRect(0, -567, 851, 567))
        self.treeView.setStyleSheet("background-image: url(images/background3.jpg);")

        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setObjectName("back")
        self.back.setGeometry(QRect(15, 15, 50, 50))
        self.back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back.hide()
        self.back.setStyleSheet("background-image:url(images/back.png);")

        self.new_main = QTreeView(Dialog)
        self.new_main.setObjectName("new_main")
        self.new_main.setGeometry(QRect(100, 50, 652, 481))
        self.new_main.hide()
        self.new_main.setStyleSheet("background-image:url();\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border-radius:10px;")

        self.New_Note = QPushButton(Dialog)
        self.New_Note.setObjectName("New_Note")
        self.New_Note.setGeometry(QRect(100, 50, 652, 61))
        self.New_Note.hide()
        self.New_Note.setStyleSheet("background-image:url();\n"
                                    "border-top-right-radius:10px;\n"
                                    "border-top-left-radius:10px;\n"
                                    "border-bottom-left-radius:0px;\n"
                                    "border-bottom-right-radius:0px;\n"
                                    "background-color: rgb(0, 170, 255);")

        self.date_i = QPushButton(Dialog)
        self.date_i.setObjectName("date_i")
        self.date_i.setGeometry(QRect(121, 130, 25, 25))
        self.date_i.hide()
        self.date_i.setStyleSheet("background-image: url(images/calender.png);\n"
                                  "border-radius:12.5px;")

        self.clock_i = QPushButton(Dialog)
        self.clock_i.setObjectName("clock_i")
        self.clock_i.hide()
        self.clock_i.setGeometry(QRect(336, 130, 25, 25))
        self.clock_i.setStyleSheet("background-image: url(images/clock.png);\n"
                                   "border-radius:12.5px;")

        self.location_i = QPushButton(Dialog)
        self.location_i.setObjectName("location_i")
        self.location_i.hide()
        self.location_i.setGeometry(QRect(553, 127, 30, 30))
        self.location_i.setStyleSheet("background-image: url(images/location.png);\n"
                                      "border-radius:15px;")

        self.date = QLineEdit(Dialog, placeholderText=" DD/MM/YYYY")
        pal = self.date.palette()
        text_color = QtGui.QColor("grey")
        pal.setColor(QtGui.QPalette.PlaceholderText, text_color)
        self.date.setPalette(pal)
        self.date.setObjectName("date")
        self.date.setGeometry(QRect(160, 129, 141, 27))
        self.date.hide()
        self.date.setStyleSheet("background-image:url();\n"
                                "background-color: rgb(255,255,255);\n"
                                "color: rgb(0, 170, 255);\n"
                                "border :0.5px solid rgb(203, 203, 203);\n"
                                "border-radius:5px;")

        self.clock = QLineEdit(Dialog, placeholderText=" start_time-end_time")
        pal = self.clock.palette()
        text_color = QtGui.QColor("grey")
        pal.setColor(QtGui.QPalette.PlaceholderText, text_color)
        self.clock.setPalette(pal)
        self.clock.setObjectName("clock")
        self.clock.setGeometry(QRect(374, 129, 157, 27))
        self.clock.hide()
        self.clock.setStyleSheet("background-image:url();\n"
                                 "background-color: rgb(255,255,255);\n"
                                 "color: rgb(0, 170, 255);\n"
                                 "border :0.5px solid rgb(203, 203, 203);\n"
                                 "border-radius:5px;")

        self.location = QLineEdit(Dialog, placeholderText=" City,District")
        pal = self.location.palette()
        text_color = QtGui.QColor("grey")
        pal.setColor(QtGui.QPalette.PlaceholderText, text_color)
        self.location.setPalette(pal)
        self.location.setObjectName("location")
        self.location.setGeometry(QRect(589, 129, 141, 27))
        self.location.hide()
        self.location.setStyleSheet("background-image:url();\n"
                                    "background-color: rgb(255,255,255);\n"
                                    "color: rgb(0, 170, 255);\n"
                                    "border :0.5px solid rgb(203, 203, 203);\n"
                                    "border-radius:5px;")

        self.title = QLineEdit(Dialog, placeholderText=" Write Title Here")
        pal = self.title.palette()
        text_color = QtGui.QColor("grey")
        pal.setColor(QtGui.QPalette.PlaceholderText, text_color)
        self.title.setPalette(pal)
        self.title.setObjectName("title")
        self.title.setGeometry(QRect(120, 190, 613, 41))
        self.title.hide()
        self.title.setStyleSheet("background-image:url();\n"
                                 "background-color: rgb(255,255,255);\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "border :0.5px solid rgb(203, 203, 203);\n"
                                 "border-radius:5px;")

        self.add = QPushButton(Dialog)
        self.add.setObjectName("add")
        self.add.setGeometry(QRect(370, 480, 111, 41))
        self.add.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.add.hide()
        self.add.setStyleSheet("background-image: url(images/blue.png);\n"
                               "border:1px solid rgb(0m185,213);\n"
                               "border-radius:10px;\n"
                               "color: white;")
                               
        self.describe = QTextEdit(Dialog, placeholderText=" Write Description Here")
        pal = self.describe.palette()
        text_color = QtGui.QColor("grey")
        pal.setColor(QtGui.QPalette.PlaceholderText, text_color)
        self.describe.setPalette(pal)
        self.describe.setObjectName("describe")
        self.describe.setGeometry(QRect(120, 250, 613, 161))
        self.describe.hide()
        self.describe.setStyleSheet("background-image:url();\n"
                                   "background-color: rgb(255,255,255);\n"
                                   "color: rgb(0, 0, 0);\n"
                                   "border :0.5px solid rgb(203, 203, 203);\n"
                                   "border-radius:5px;")

        self.attach_file = QPushButton(Dialog)
        self.attach_file.setObjectName("attach_file")
        self.attach_file.setGeometry(QRect(120, 420, 101, 27))
        self.attach_file.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.attach_file.hide()
        self.attach_file.setStyleSheet("background-image: url();\n"
                                       "border:0.5px solid rgb(0, 85, 255);\n"
                                       "border-radius:5px;\n"
                                       "background-color: rgb(0, 85, 255);\n"
                                       "color: white;")

        self.clear = QPushButton(Dialog)
        self.clear.setObjectName("clear")
        self.clear.setGeometry(QRect(631, 420, 101, 27))
        self.clear.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.clear.hide()
        self.clear.setStyleSheet("background-image: url();\n"
                                 "border:0.5px solid rgb(0, 85, 255);\n"
                                 "border-radius:5px;\n"
                                 "background-color: rgb(0, 85, 255);\n"
                                 "color: white;")

        self.attach_file_l = QtWidgets.QLabel(Dialog)
        self.attach_file_l.setObjectName('attach_file_l')
        self.attach_file_l.setGeometry(230, 420, 150, 27)
        self.attach_file_l.hide()
        self.attach_file_l.setStyleSheet("color: rgb(0,0,0)")

        self.delete_files = QtWidgets.QPushButton(Dialog)
        self.delete_files.setObjectName('delete_files')
        self.delete_files.setGeometry(320, 425, 18, 18)
        self.delete_files.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.delete_files.hide()
        self.delete_files.setStyleSheet("background-image: url(images/cross18.png);\n"
                                 "border-radius:9px;\n"
                                 "background-color: rgb();")

        self.treeView_read = QTreeView(Dialog)
        self.treeView_read.setObjectName("treeView_read")
        self.treeView_read.setGeometry(QRect(70, 60, 711, 451))
        font1 = QtGui.QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.treeView_read.setFont(font1)
        self.treeView_read.setStyleSheet("background-image:url();\n"
                                         "background-color:rgb(255,255,255);\n"
                                         "border-radius:15px;")
        self.treeView_read.hide()

        self.note_scroll = QScrollArea(Dialog)
        self.note_scroll.setObjectName("note_scroll")
        self.note_scroll.setGeometry(QRect(70, 60, 181, 451))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.note_scroll.sizePolicy().hasHeightForWidth())
        self.note_scroll.setSizePolicy(sizePolicy)
        self.note_scroll.setMinimumSize(QSize(0, 100))
        self.note_scroll.setSizeIncrement(QSize(0, 100))
        self.note_scroll.setBaseSize(QSize(0, 100))
        self.note_scroll.setStyleSheet("background-image: url();\n"
                                       "border-top-left-radius:15px;\n"
                                       "border-bottom-left-radius:15px;\n"
                                       "border-top-right-radius:0px;\n"
                                       "border-bottom-right-radius:0px;\n"
                                       "background-color: rgb(43, 43, 43);")
        self.note_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 181, 451))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        font2 = QtGui.QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)

        self.note_scroll.setWidget(self.scrollAreaWidgetContents)
        self.note_scroll.hide()

        self.date_l = QLabel(Dialog)
        self.date_l.setObjectName("date_l")
        self.date_l.setGeometry(QRect(325, 100, 401, 20))
        font3 = QtGui.QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        self.date_l.setFont(font3)
        self.date_l.setStyleSheet("background-image: url();\n"
                                  "color: rgb(0, 0, 0);")
        self.date_l.hide()

        self.time_l = QLabel(self.treeView_read)
        self.time_l.setObjectName("time_l")
        self.time_l.setGeometry(QRect(327, 130, 401, 20))
        self.time_l.setFont(font3)
        self.time_l.setStyleSheet("background-image: url();\n"
                                  "color: rgb(0, 0, 0);")
        # self.time_l.hide()

        self.location_l = QLabel(Dialog)
        self.location_l.setObjectName("location_l")
        self.location_l.setGeometry(QRect(358, 152, 361, 31))
        self.location_l.setFont(font3)
        self.location_l.setStyleSheet("background-image: url();\n"
                                      "color: rgb(0, 0, 0);")
        self.location_l.hide()

        self.title_l = QLabel(Dialog)
        self.title_l.setObjectName("title_l")
        self.title_l.setGeometry(QRect(323, 199, 401, 31))
        self.title_l.setFont(font3)
        self.title_l.setStyleSheet("background-image: url();\n"
                                   "color: rgb(0, 0, 0);")
        self.title_l.hide()

        self.descrip_p = QPlainTextEdit(Dialog)
        self.descrip_p.setObjectName("descrip_p")
        self.descrip_p.setEnabled(False)
        self.descrip_p.setGeometry(QRect(270, 230, 481, 201))
        font4 = QtGui.QFont()
        font4.setPointSize(14)
        self.descrip_p.setFont(font4)
        self.descrip_p.setStyleSheet("background-image: url();\n"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "border:1px solid rgb(255,255,255);")
        self.descrip_p.hide()

        self.pencil = QPushButton(Dialog)
        self.pencil.setObjectName("pencil")
        self.pencil.setGeometry(QRect(730, 70, 32, 32))
        self.pencil.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.pencil.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pencil.setStyleSheet("background-image: url(images/pencil.png);\n"
                                  "border-radius:20px;\n"
                                  "background-color: rgb(255, 255, 255);")
        self.pencil.hide()
        self.pencil.setCheckable(False)
        self.pencil.setChecked(False)

        self.recycle_bin = QPushButton(Dialog)
        self.recycle_bin.setObjectName("recycle_bin")
        self.recycle_bin.setGeometry(QRect(680, 70, 32, 32))
        self.recycle_bin.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.recycle_bin.setStyleSheet("background-image: url(images/trash_bin.png);\n"
                                       "border-radius:20px;\n"
                                       "background-color: rgb(255, 255, 255);")
        self.recycle_bin.hide()

        self.date_r = QLabel(Dialog)
        self.date_r.setObjectName("date_r")
        self.date_r.setGeometry(QRect(275, 100, 51, 20))
        self.date_r.setFont(font)
        self.date_r.setStyleSheet("background-image: url();\n"
                                  "color: rgb(0, 0, 0);")
        self.date_r.hide()

        self.time_r = QLabel(Dialog)
        self.time_r.setObjectName("time_r")
        self.time_r.setGeometry(QRect(275, 130, 51, 20))
        self.time_r.setFont(font)
        self.time_r.setStyleSheet("background-image: url();\n"
                                  "color: rgb(0, 0, 0);")
        self.time_r.hide()

        self.location_r = QLabel(Dialog)
        self.location_r.setObjectName("location_r")
        self.location_r.setGeometry(QRect(275, 157, 81, 20))
        self.location_r.setFont(font)
        self.location_r.setStyleSheet("background-image: url();\n"
                                      "color: rgb(0, 0, 0);")
        self.location_r.hide()

        self.title_r = QLabel(Dialog)
        self.title_r.setObjectName("tilte_r")
        self.title_r.setGeometry(QRect(275, 205, 51, 20))
        self.title_r.setFont(font)
        self.title_r.setStyleSheet("background-image: url();\n"
                                   "color: rgb(0, 0, 0);")
        self.title_r.hide()

        self.descrip_r = QLabel(Dialog)
        self.descrip_r.setObjectName("descrip_r")
        self.descrip_r.setGeometry(QRect(275, 237, 111, 20))
        self.descrip_r.setFont(font)
        self.descrip_r.setStyleSheet("background-image: url();\n"
                                     "color: rgb(0, 0, 0);")
        self.descrip_r.hide()

        self.file_scroll = QScrollArea(Dialog)
        self.file_scroll.setObjectName("file_scroll")
        self.file_scroll.setGeometry(QRect(280, 440, 461, 61))
        self.file_scroll.setStyleSheet("background-image: url();\n"
                                       "background-color: rgb(255, 255, 255);\n"
                                       "border:rgb(255,255,255);")
        self.file_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.file_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.file_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 461, 61))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.file_scroll.setWidget(self.scrollAreaWidgetContents_2)
        self.file_scroll.hide()

        self.retranslateUi(Dialog)
        self.edit_b.clicked.connect(self.contribute)
        self.new_b.clicked.connect(self.new)
        self.read_b.clicked.connect(self.read)
        self.close.clicked.connect(Dialog.close)
        self.minimize.clicked.connect(Dialog.showMinimized)
        self.back.clicked.connect(self.back_menu)
        self.clear.clicked.connect(self.describe.clear)
        self.clear.clicked.connect(self.title.clear)
        self.clear.clicked.connect(self.date.clear)
        self.clear.clicked.connect(self.clock.clear)
        self.clear.clicked.connect(self.location.clear)
        self.add.clicked.connect(self.add_note)
        self.attach_file.clicked.connect(self.attach)
        self.delete_files.clicked.connect(self.delete_f)
        self.recycle_bin.clicked.connect(self.delete_note)
        self.pencil.clicked.connect(self.send_edit)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def back_menu(self):
        Dialog.close()
        subprocess.run(['python3', 'main.py'])
        quit()

    def show(self):
        for i in list_of_objects:
            eval(f'self.{i}.show()')

    def show_r(self):
        for i in list_of_read_objects:
            eval(f'self.{i}.show()')

    def close_r(self):
        for i in list_of_read_objects:
            eval(f'self.{i}.close()')

    def new(self):
        global list_of_objects

        def back_show():
            self.back.show()
            self.back.raise_()

        self.treeView.setStyleSheet("background-image: url(images/background3.jpg);")

        self.new_l.hide()
        self.edit_b.hide()
        self.edit_l.hide()
        self.read_l.hide()
        self.read_b.hide()

        self.new_b.setStyleSheet("background-image:url();\n"
                                 "background-color: rgb();\n"
                                 "color: rgb();\n"
                                 "background-image: url(images/new_big.png);\n"
                                 "border-radius: 283px;")

        self.anim = QtCore.QPropertyAnimation(self.new_b, b"pos")
        self.anim.setEndValue(QtCore.QPoint(137, 0))
        self.anim.setDuration(150)
        self.anim_2 = QtCore.QPropertyAnimation(self.new_b, b"size")
        self.anim_2.setEndValue(QtCore.QSize(566, 566))
        self.anim_2.setDuration(1000)
        self.anim_3 = QtCore.QPropertyAnimation(self.treeView, b"pos")
        self.anim_3.setEndValue(QtCore.QPoint(0, 0))
        self.anim_3.setDuration(820)
        self.anim_4 = QtCore.QPropertyAnimation(self.new_b, b"pos")
        self.anim_4.setEndValue(QtCore.QPoint(137, 700))
        self.anim_4.setDuration(1000)
        self.anim_group = QtCore.QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()
        self.anim_group.finished.connect(self.anim_3.start)
        self.anim_group.finished.connect(self.anim_4.start)

        self.close.raise_()
        self.minimize.raise_()
        
        list_of_objects = ['new_main', 'New_Note', 'location', 'location_i', 'clock', 'clock_i', 'date',
                           'date_i', 'attach_file', 'describe', 'clear', 'add', 'title', 'back']
        
        self.anim_4.finished.connect(self.show)

    def add_note(self):
        if self.add.text() == 'Save':
            date = self.date.text().replace(',','-')
            clock = self.clock.text().replace(',','-')
            location = self.location.text().replace(',','-')
            title = self.title.text().replace(',','-')
            describe = self.describe.toPlainText().replace(',','-')
            files = attach_files_o[0]
            note = f'{date},{clock},{location},{title},{describe},{files}\n'

            with open('notes.txt', 'r') as f:
                notes = f.readlines()

            with open("logs.txt", "r") as f:
                data = int(f.readline())

            notes[data] = note

            with open('notes.txt', 'w') as f:
                for i in notes:
                    f.write(i)

            self.back_menu()

        else:
            date = self.date.text().replace(',','-')
            clock = self.clock.text().replace(',','-')
            location = self.location.text().replace(',','-')
            title = self.title.text().replace(',','-')
            describe = self.describe.toPlainText().replace(',','-')
            files = attach_files_o[0]
            note = f'{date},{clock},{location},{title},{describe},{files}\n'

            with open('notes.txt', 'a') as f:
                f.write(note)

            self.back_menu()
    
    def attach(self):
        global attach_files_o
        file_name = QtWidgets.QFileDialog()
        file_name.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        attach_files = file_name.getOpenFileNames(Dialog, "Open files", "/home/alihv3000")
        number_of_files = len(attach_files[0])
        if number_of_files != 0:
            attach_files_o = attach_files
            self.attach_file_l.setText(f"{number_of_files} file added")
            self.attach_file_l.show()
            self.delete_files.show()
        else:
            pass
        # print(attach_files)

    def delete_f(self):
        global attach_files_o
        attach_files_o = ([], '')
        self.attach_file_l.setText("")
        self.delete_files.hide()

    def read(self):
        global list_of_read_objects

        self.read_l.hide()
        self.edit_b.hide()
        self.edit_l.hide()
        self.new_l.hide()
        self.new_b.hide()

        self.treeView.setStyleSheet("background-image: url(images/background3.jpg);")

        self.read_b.setStyleSheet("background-image:url();\n"
                                 "background-color: rgb();\n"
                                 "color: rgb();\n"
                                 "background-image: url(images/read_big.png);\n"
                                 "border-radius: 283px;")

        self.anim = QtCore.QPropertyAnimation(self.read_b, b"pos")
        self.anim.setEndValue(QtCore.QPoint(137, 0))
        self.anim.setDuration(150)
        self.anim_2 = QtCore.QPropertyAnimation(self.read_b, b"size")
        self.anim_2.setEndValue(QtCore.QSize(566, 566))
        self.anim_2.setDuration(1000)
        self.anim_3 = QtCore.QPropertyAnimation(self.treeView, b"pos")
        self.anim_3.setEndValue(QtCore.QPoint(0, 0))
        self.anim_3.setDuration(820)
        self.anim_4 = QtCore.QPropertyAnimation(self.read_b, b"pos")
        self.anim_4.setEndValue(QtCore.QPoint(137, 700))
        self.anim_4.setDuration(1000)
        self.anim_group = QtCore.QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()
        self.anim_group.finished.connect(self.anim_3.start)
        self.anim_group.finished.connect(self.anim_4.start)

        self.close.raise_()
        self.minimize.raise_()
        
        list_of_read_objects = ['date_l', 'location_l', 'location_r', 'time_r', 'date_r', 'recycle_bin',
                        'pencil', 'title_r', 'title_l', 'descrip_r', 'descrip_p', 'treeView_read','note_scroll', 'file_scroll', 'back']
        
        self.anim_4.finished.connect(self.show_r)
        self.anim_4.finished.connect(self.main_read)
        
    def delete_note(self):
        with open("logs.txt", "r") as f:
            num = f.readline()
        with open("notes.txt", "r") as f:
            notes_d = f.readlines()
        notes_d.pop(int(num))

        with open("notes.txt", "w") as f:
            for i in notes_d:
                f.write(f'{i}')

        Dialog.close()
        subprocess.run(['python3', 'main.py'])
        quit()

    def open_note(self, data):
        try:
            self.file_scroll.close()
        except AttributeError:
            pass

        self.file_scroll = QScrollArea(Dialog)
        self.file_scroll.setObjectName("file_scroll")
        self.file_scroll.setGeometry(QRect(280, 440, 461, 61))
        self.file_scroll.setStyleSheet("background-image: url();\n"
                                       "background-color: rgb(255, 255, 255);\n"
                                       "border:rgb(255,255,255);")
        self.file_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.file_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.file_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 461, 61))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.file_scroll.setWidget(self.scrollAreaWidgetContents_2)
        self.file_scroll.show()

        self.time_l.setGeometry(QRect(255, 70, 401, 20))

        with open('notes.txt', 'r') as f:
            notes = f.readlines()

        for i in range(len(notes)):
            notes[i] = notes[i].split(',')
        
        data = data.split('.')
        data = int(data[1])

        with open("logs.txt", "w") as f:
            f.write(str(data))

        self.date_l.setText(notes[data][0])
        self.time_l.setText(notes[data][1])
        self.location_l.setText(notes[data][2])
        self.title_l.setText(notes[data][3])
        self.descrip_p.setPlainText(f'{" "*26}{notes[data][4]}')

        files_pathes = notes[data][5::]
        # print(files_pathes)
        pathes = []

        if files_pathes[0] != '[]\n':
            for i in files_pathes:
                file_name = i.replace(']', '')
                file_name = file_name.replace('[', '')
                file_name = file_name.replace("'", '')
                file_name = file_name.replace('"', '')
                file_name = file_name.replace('\n', '')
                file_name = file_name.replace(' ', '')
                file_path = file_name
                pathes.append(file_path)
                # file_name = file_name.split('/')
                # print(file_name)
                # file_name = file_name[-1]

            for i in pathes:
                self.file_attached = QPushButton(self.scrollAreaWidgetContents_2)
                self.file_attached.setObjectName(i)
                sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
                sizePolicy1.setHeightForWidth(self.file_attached.sizePolicy().hasHeightForWidth())
                self.file_attached.setSizePolicy(sizePolicy1)
                self.file_attached.setMinimumSize(QSize(80, 40))
                self.file_attached.setMaximumSize(QSize(16777215, 100))
                font2 = QtGui.QFont()
                font2.setPointSize(10)
                font2.setWeight(50)
                self.file_attached.setFont(font2)
                self.file_attached.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
                self.file_attached.setStyleSheet("background-color: rgb(7, 40, 255);\n"
                                                 "border-radius:15px;\n"
                                                 "color: white;")
                self.horizontalLayout.addWidget(self.file_attached)
                self.file_attached.setText(i)
                text_btn2 = self.file_attached.text()
                self.file_attached.clicked.connect(lambda fn2, text_btn2=text_btn2 : subprocess.run(['mimeopen', text_btn2]))
        
    def main_read(self):
        with open('notes.txt', 'r') as f:
            notes = f.readlines()

        for i in range(len(notes)):
            notes[i] = notes[i].split(',')

        for i in range(len(notes)):#len(notes):
            self.btn = QPushButton(self.scrollAreaWidgetContents)
            try:
                self.btn.setObjectName(f'{i}.{notes[i][3]}')
            except IndexError:
                continue
            sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
            sizePolicy1.setHeightForWidth(self.btn.sizePolicy().hasHeightForWidth())
            self.btn.setSizePolicy(sizePolicy1)
            self.btn.setMinimumSize(QSize(0, 70))
            self.btn.setMaximumSize(QSize(16777215, 100))
            font2 = QtGui.QFont()
            font2.setPointSize(10)
            font2.setWeight(50)
            self.btn.setFont(font2)
            self.btn.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
            self.btn.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                   "color: white;")
            self.verticalLayout.addWidget(self.btn)
            self.btn.setText(f'{i}.{notes[i][3]}')
            text_btn = self.btn.text()
            self.btn.clicked.connect(lambda fn, text_btn=text_btn : self.open_note(f'{i}.{text_btn}'))
                
    def edit(self):
        global list_of_objects
        
        self.edit_l.hide()
        self.new_b.hide()
        self.new_l.hide()
        self.read_l.hide()
        self.read_b.hide()
        self.add.setText("Save")

        self.edit_b.setStyleSheet("background-image:url();\n"
                                 "background-color: rgb();\n"
                                 "color: rgb();\n"
                                 "background-image: url(images/edit_big.png);\n"
                                 "border-radius: 283px;")
        self.edit_b.raise_()
        self.edit_b.show()

        self.anim = QtCore.QPropertyAnimation(self.edit_b, b"pos")
        self.anim.setEndValue(QtCore.QPoint(137, 0))
        self.anim.setDuration(150)
        self.anim_2 = QtCore.QPropertyAnimation(self.edit_b, b"size")
        self.anim_2.setEndValue(QtCore.QSize(566, 566))
        self.anim_2.setDuration(1000)
        self.anim_3 = QtCore.QPropertyAnimation(self.treeView, b"pos")
        self.anim_3.setEndValue(QtCore.QPoint(0, 0))
        self.anim_3.setDuration(820)
        self.anim_4 = QtCore.QPropertyAnimation(self.edit_b, b"pos")
        self.anim_4.setEndValue(QtCore.QPoint(137, 700))
        self.anim_4.setDuration(1000)
        self.anim_group = QtCore.QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()
        self.anim_group.finished.connect(self.anim_3.start)
        self.anim_group.finished.connect(self.anim_4.start)

        self.close.raise_()
        self.minimize.raise_()
        
        self.anim_4.finished.connect(self.show)

    def send_edit(self):
        global attach_files_o
        global list_of_objects
        list_of_objects = ['new_main', 'New_Note', 'location', 'location_i', 'clock', 'clock_i', 'date',
                           'date_i', 'attach_file', 'attach_file_l', 'describe', 'clear', 'add', 'title', 'back']

        with open("logs.txt", "r") as f:
            data = int(f.readline())

        with open("notes.txt", "r") as f:
            notes = f.readlines()

        for i in range(len(notes)):
            notes[i] = notes[i].split(',')

        self.date.setText(notes[data][0])
        self.clock.setText(notes[data][1])
        self.location.setText(notes[data][2])
        self.title.setText(notes[data][3])
        self.describe.setText(notes[data][4])
        if '[]\n' not in notes[data][5::]:
            self.attach_file_l.setText(f"{len(notes[data][5::])} file added")
            list_of_objects.append('delete_files')

        files_pathes = notes[data][5::]
        # print(files_pathes)
        pathes = []

        if files_pathes[0] != '[]\n':
            for i in files_pathes:
                file_name = i.replace(']', '')
                file_name = file_name.replace('[', '')
                file_name = file_name.replace("'", '')
                file_name = file_name.replace('"', '')
                file_name = file_name.replace('\n', '')
                file_name = file_name.replace(' ', '')
                file_path = file_name
                pathes.append(file_path)

        attach_files_o = (pathes, '')

        self.close_r()
        self.edit()

    def contribute(self):
        webbrowser.open('https://github.com/Ali-Hosseinverdi/notes', new=2)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.read_l.setText(_translate("Dialog", "Read"))
        self.edit_l.setText(_translate("Dialog", "Contribute"))
        self.new_l.setText(_translate("Dialog", "New"))
        self.New_Note.setText(_translate("Dialog", "New Note"))
        self.add.setText(_translate("Dialog", "Add"))
        self.attach_file.setText(_translate("Dialog", "Attach Files"))
        self.clear.setText(_translate("Dialog", "Clear"))
        self.descrip_p.setPlainText(_translate("Dialog", "                          "))
        self.date_r.setText(_translate("Dialog", "Date:"))
        self.time_r.setText(_translate("Dialog", "Time:"))
        self.location_r.setText(_translate("Dialog", "Location:"))
        self.title_r.setText(_translate("Dialog", "Title:"))
        self.descrip_r.setText(_translate("Dialog", "Description:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Breeze')
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

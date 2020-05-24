# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(625, 500)
        MainWindow2.setStyleSheet("*{\n"
                                  "font-family:Century Gothic;\n"
                                  "font-size:24px;\n"
                                  "}\n"
                                  "QFrame{\n"
                                  "background:white;\n"
                                  "border-radius:15px;\n"
                                  "}\n"
                                  "QToolButton{\n"
                                  "background:white;\n"
                                  "border-radius:30px;\n"
                                  "}\n"
                                  "QPushButton{\n"
                                  "background:black;\n"
                                  "color:white;\n"
                                  "border-radius:15px;\n"
                                  "}\n"
                                  "QLineEdit{\n"
                                  "background:transparent;\n"
                                  "border:none;\n"
                                  "border-bottom:1px solid #717072;\n"
                                  "color:#717072;\n"
                                  "}\n"
                                  "")
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(270, 0, 61, 61))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("user2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(25, 25))
        self.toolButton.setObjectName("toolButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 60, 561, 351))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 10, 141, 41))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 300, 221, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(60, 140, 311, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 240, 311, 31))
        self.lineEdit_2.setText("")
        # self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 161, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 190, 141, 20))
        self.label_3.setObjectName("label_3")
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 35))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "Server"))
        self.label.setText(_translate("MainWindow2", "LOGIN HERE"))
        self.pushButton.setText(_translate("MainWindow2", "confirm"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow2", "Port Number"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow2", "IP Number"))
        self.label_2.setText(_translate("MainWindow2", "Port Number"))
        self.label_3.setText(_translate("MainWindow2", "IP Number"))


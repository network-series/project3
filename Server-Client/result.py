# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog3(object):
    def setupUi(self, Dialog3):
        Dialog3.setObjectName("Dialog3")
        Dialog3.resize(486, 346)
        Dialog3.setStyleSheet("QFrame{\n"
"background:white;\n"
"}\n"
"QTextEdit\n"
"{\n"
"border:none;\n"
"}\n"
"*{\n"
"font-family:Century Gothic;\n"
"font-size:24px;\n"
"}\n"
"QPushButton{\n"
"background:black;\n"
"color:white;\n"
"border-radius:15px;\n"
"}")
        self.frame = QtWidgets.QFrame(Dialog3)
        self.frame.setGeometry(QtCore.QRect(30, 40, 431, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 0, 141, 41))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(110, 230, 221, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 371, 71))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog3)
        QtCore.QMetaObject.connectSlotsByName(Dialog3)

    def retranslateUi(self, Dialog3):
        _translate = QtCore.QCoreApplication.translate
        Dialog3.setWindowTitle(_translate("Dialog3", "result"))
        self.label.setText(_translate("Dialog3", ""))
        self.pushButton.setText(_translate("Dialog3", "Exit"))
        self.label_2.setText(_translate("Dialog3", ""))

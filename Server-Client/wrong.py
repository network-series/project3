# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wrong.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(400, 300)
        Dialog2.setStyleSheet("QFrame{\n"
                              "background:white;\n"
                              "}\n"
                              "QTextEdit{\n"
                              "border:transparent;\n"
                              "}\n"
                              "QPushButton\n"
                              "{\n"
                              "border-radius:15px;\n"
                              "background:black;\n"
                              "color:white;\n"
                              "}\n"
                              "*{\n"
                              "font-family:Century Gothic;\n"
                              "font-size:24px;\n"
                              "}")
        self.frame = QtWidgets.QFrame(Dialog2)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton2 = QtWidgets.QPushButton(self.frame)
        self.pushButton2.setGeometry(QtCore.QRect(140, 200, 121, 31))
        self.pushButton2.setObjectName("pushButton2")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(50, 80, 311, 41))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "Warning"))
        self.pushButton2.setText(_translate("Dialog2", "Exit"))
        self.textEdit.setHtml(_translate("Dialog2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                    "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'Century Gothic\'; font-size:24px; font-weight:400; font-style:normal;\">\n"
                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24px;\">   WRONG SERIAL NUMBER!</span></p></body></html>"))

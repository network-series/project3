import socket
import struct
import time
import os
from threading import Thread
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from untitled import *
from command import *
from wrong import *
from result import *


# server_ip_port = ("192.168.1.2", 5200)
buffer_size = 1024
conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.setblocking(0)
conn.settimeout(180)
ticket = ""


def pre(in_seq, server_ip_port1):
    if os.path.exists(r"check.txt"):
        file = open(r"check.txt")
        seq = file.readline()
        file.close()
        conn.sendto((seq + " check").encode(), server_ip_port1)
        response, server_addr = conn.recvfrom(buffer_size)
        if response.decode() != "agree":
            app1 = QApplication(sys.argv)
            ui2 = Ui_Dialog2()
            dialog2 = QDialog()
            ui2.setupUi(dialog2)
            dialog2.show()
            ui2.pushButton2.clicked.connect(dialog2.close)
            app1.exec_()
            sys.exit(0)
        return 1
    else:
        conn.sendto((in_seq + " check").encode(), server_ip_port1)
        res, ser_addr = conn.recvfrom(buffer_size)
        if res.decode() != "agree":
            app1 = QApplication(sys.argv)
            ui2 = Ui_Dialog2()
            dialog2 = QDialog()
            ui2.setupUi(dialog2)
            dialog2.show()
            ui2.pushButton2.clicked.connect(dialog2.close)
            app1.exec_()
            sys.exit(0)
        else:
            in_file = open(r"check.txt", mode='a')
            in_file.write(in_seq)
            in_file.close()
            return 1


def clock(s, ti, t, server_ip_port2):
    t_in = t
    while True:
        t_current = time.localtime(time.time())
        if (((
                     t_current.tm_mday - t_in.tm_mday) * 24 + t_current.tm_hour - t_in.tm_hour) * 60 + t_current.tm_min - t_in.tm_min) >= 30:
            conn.sendto(("onli" + " " + s + " " + ti).encode(), server_ip_port2)
            t_in = t_current
        time.sleep(60)


def main(cmd1, server_ip_port3):
    while True:
        file = open(r"check.txt")
        sequence = file.readline()
        if cmd1 == "exit":
            sys.exit(0)
        elif cmd1[0:4] == "helo":
            conn.sendto((cmd1 + ' ' + sequence).encode(), server_ip_port3)
            try:
                h_data, ser_addr = conn.recvfrom(buffer_size)
            except Exception as e:
                text = "服务器异常，请重试"
                app2 = QApplication(sys.argv)
                dialog3 = QDialog()
                ui3 = Ui_Dialog3()
                ui3.setupUi(dialog3)
                ui3.label_2.setText(text)
                dialog3.show()
                ui3.pushButton.clicked.connect(dialog3.close)
                app2.exec_()
                continue
            if h_data.decode()[0:4] == "fail":
                text = "    对不起，当前使用人数已满！"
                app2 = QApplication(sys.argv)
                dialog3 = QDialog()
                ui3 = Ui_Dialog3()
                ui3.setupUi(dialog3)
                ui3.label_2.setText(text)
                dialog3.show()
                ui3.pushButton.clicked.connect(dialog3.close)
                app2.exec_()
                sys.exit(0)
            else:
                ticket = h_data
                text1 = "      port:" + ticket.decode() + "申请成功！"
                app2 = QApplication(sys.argv)
                dialog3 = QDialog()
                ui3 = Ui_Dialog3()
                ui3.setupUi(dialog3)
                ui3.label_2.setText(text1)
                dialog3.show()
                ui3.pushButton.clicked.connect(dialog3.close)
                app2.exec_()
                t1 = Thread(target=clock,
                            args=(sequence, ticket.decode(), time.localtime(time.time()), server_ip_port3))
                t1.start()
                break
        elif cmd1[0:4] == "gbye":
            conn.sendto((cmd1 + ' ' + sequence).encode(), server_ip_port3)
            try:
                g_data, ser_addr = conn.recvfrom(buffer_size)
            except Exception as e:
                text3 = "服务器异常，请重试"
                app2 = QApplication(sys.argv)
                dialog3 = QDialog()
                ui3 = Ui_Dialog3()
                ui3.setupUi(dialog3)
                ui3.label_2.setText(text3)
                dialog3.show()
                ui3.pushButton.clicked.connect(dialog3.close)
                app2.exec_()
                continue
            if g_data.decode()[0:4] == "thax":
                text4 = "            归还成功！"
                app2 = QApplication(sys.argv)
                dialog3 = QDialog()
                ui3 = Ui_Dialog3()
                ui3.setupUi(dialog3)
                ui3.label_2.setText(text4)
                dialog3.show()
                ui3.pushButton.clicked.connect(dialog3.close)
                app2.exec_()
                sys.exit(0)
            else:
                text4 = "          归还操作失败！"
                app2 = QApplication(sys.argv)
                dialog3 = QDialog()
                ui3 = Ui_Dialog3()
                ui3.setupUi(dialog3)
                ui3.label_2.setText(text4)
                dialog3.show()
                ui3.pushButton.clicked.connect(dialog3.close)
                app2.exec_()
                continue
        else:
            continue


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    ui.pushButton.clicked.connect(mainWindow.close)
    app.exec_()
    server_ip_port = (ui.lineEdit_2.text(), int(ui.lineEdit_3.text()))
    seq = ui.lineEdit.text()
    if pre(seq, server_ip_port) == 1:
        dialog = QDialog()
        ui1 = Ui_Dialog()
        ui1.setupUi(dialog)
        dialog.show()
        ui1.pushButton.clicked.connect(dialog.close)
        app.exec_()
        cmd = ui1.lineEdit.text()
        main(cmd, server_ip_port)

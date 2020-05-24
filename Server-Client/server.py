import socket
import struct
import time
import pandas as pd
from threading import Thread
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from server_ip import *


def main():
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(mainWindow)
    mainWindow.show()
    ui.pushButton.clicked.connect(mainWindow.close)
    app.exec_()
    server_ip_port = (ui.lineEdit_2.text(), int(ui.lineEdit.text()))
    buffer_size = 1024
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn.bind(server_ip_port)
    while True:
        sExcelFile = r"information.xlsx"
        df = pd.read_excel(sExcelFile, keep_default_na=False)
        row_of_inf = df.shape[0]
        message, client_addr = conn.recvfrom(buffer_size)
        if message.decode()[0:4] == "helo":
            m_split = message.decode().split()
            port, seq = m_split[1], m_split[2]
            point = -1
            for i in range(row_of_inf):
                if seq == df['seq'][i]:
                    point = i
                    break
            num = df['avai_num'][point]
            if num == 0:
                conn.sendto("fail no ticket".encode(), client_addr)
                in_file = open("log.txt", 'a')
                in_file.writelines(
                    str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) + "  " + seq + "  " + "deny" + "\n")
                in_file.close()
            else:
                number = -1
                for d in range(1, df['num'][point] + 1):
                    if df[str(d) + "_time"][point] == "":
                        number = d
                        break
                ticket = port + "." + str(number)
                num = num - 1
                df.loc[point, 'avai_num'] = num
                df.to_excel(sExcelFile, index=None)
                conn.sendto(ticket.encode(), client_addr)
                in_file = open("log.txt", 'a')
                in_file.writelines(
                    str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) + "  " + seq + "  " + "agree" + "\n")
                in_file.close()
        elif message.decode()[0:4] == "gbye":
            g_split = message.decode().split()
            tickets, se = g_split[1], g_split[2]
            n = tickets[-1]
            g_point = -1
            # print(df)
            for i in range(row_of_inf):
                if se == df['seq'][i]:
                    g_point = i
                    break
            if int(n) in range(1, df['num'][g_point] + 1):
                df.loc[g_point, n + "_time"] = ""
                df.loc[g_point, 'avai_num'] = df['avai_num'][g_point] + 1
                # print(df)
                df.to_excel(sExcelFile, index=None)
                conn.sendto("thax".encode(), client_addr)
            else:
                conn.sendto("rtrn deny".encode(), client_addr)
        elif message.decode()[0:4] == "onli":
            o_split = message.decode().split()
            o_seq, o_ticket = o_split[1], o_split[2]
            o_n = o_ticket[-1]
            o_point = -1
            for i in range(row_of_inf):
                if o_seq == df['seq'][i]:
                    o_point = i
                    break
            df.loc[o_point, o_n + '_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            df.to_excel(sExcelFile, index=None)
        elif message.decode()[-5:] == "check":
            flag = 0
            for i in range(row_of_inf):
                if message.decode()[:-6] == df['seq'][i]:
                    flag = 1
                    break
            if flag == 0:
                conn.sendto("deny".encode(), client_addr)
            else:
                conn.sendto("agree".encode(), client_addr)
        else:
            continue



def check_client():
    while True:
        sExcelFile = r"information.xlsx"
        df = pd.read_excel(sExcelFile, keep_default_na=False)
        row_of_inf = df.shape[0]
        for i in range(row_of_inf):
            for j in range(1, df['num'][i] + 1):
                if df.iloc[i, j + 5] != "":
                    t_content = df.iloc[i, j + 5]
                    t_current = time.localtime(time.time())
                    if (((t_current.tm_mday - int(t_content[8:10])) * 24 + t_current.tm_hour - int(t_content[11:13])) * 60 +
                                                                           t_current.tm_min - int(t_content[14:16])) >= 31:
                        df.loc[i, 'avai_num'] = df['avai_num'][i] + 1
                        df.iloc[i, j + 5] = ""
                        df.to_excel(sExcelFile, index=None)
        time.sleep(60)


def inita():
    sExcelFile = r"information.xlsx"
    df = pd.read_excel(sExcelFile, keep_default_na=False)
    row_of_inf = df.shape[0]
    for i in range(row_of_inf):
        for j in range(1, df['num'][i] + 1):
            if df.iloc[i, j + 5] != "":
                df.iloc[i, j + 5] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    df.to_excel(sExcelFile, index=None)


if __name__ == '__main__':
    inita()
    t1 = Thread(target=main)
    t1.start()
    t2 = Thread(target=check_client)
    t2.start()

import socket
import struct
import time
import os
import sys
from threading import Thread

server_ip_port = ("192.168.1.2", 5200)
buffer_size = 1024
conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.setblocking(0)
conn.settimeout(180)
ticket = ""


def pre():
    print('Waiting...')
    if os.path.exists(r"C:\Users\zyj\Desktop\check.txt"):
        file = open(r"C:\Users\zyj\Desktop\check.txt")
        seq = file.readline()
        file.close()
        conn.sendto((seq + " check").encode(), server_ip_port)
        response, server_addr = conn.recvfrom(buffer_size)
        if response.decode() != "agree":
            print("对不起,您的序列号出错无法通过验证")
            sys.exit(0)
        return 1
    else:
        in_seq = input("请输入您的序列号:")
        conn.sendto((in_seq + " check").encode(), server_ip_port)
        res, ser_addr = conn.recvfrom(buffer_size)
        if res.decode() != "agree":
            print("对不起,您的序列号出错无法通过验证")
            sys.exit(0)
        else:
            in_file = open(r"C:\Users\zyj\Desktop\check.txt", mode='a')
            in_file.write(in_seq)
            in_file.close()
            return 1


def clock(s, ti, t):
    t_in = t
    while True:
        t_current = time.localtime(time.time())
        if (((
                     t_current.tm_mday - t_in.tm_mday) * 24 + t_current.tm_hour - t_in.tm_hour) * 60 + t_current.tm_min - t_in.tm_min) >= 30:
            conn.sendto(("onli" + " " + s + " " + ti).encode(), server_ip_port)
            t_in = t_current
        time.sleep(60)


def main():
    while True:
        file = open(r"C:\Users\zyj\Desktop\check.txt")
        sequence = file.readline()
        cmd = input("请输入您的命令:")
        if cmd == "exit":
            sys.exit(0)
        elif cmd[0:4] == "helo":
            conn.sendto((cmd + ' ' + sequence).encode(), server_ip_port)
            try:
                h_data, ser_addr = conn.recvfrom(buffer_size)
            except Exception as e:
                print("服务器异常，请稍后再试")
                continue
            if h_data.decode()[0:4] == "fail":
                print("对不起，当前使用人数已满")
                sys.exit(0)
            else:
                ticket = h_data
                print(ticket.decode())
                t1 = Thread(target=clock, args=(sequence, ticket.decode(), time.localtime(time.time())))
                t1.start()
        elif cmd[0:4] == "gbye":
            conn.sendto((cmd + ' ' + sequence).encode(), server_ip_port)
            try:
                g_data, ser_addr = conn.recvfrom(buffer_size)
            except Exception as e:
                print("服务器异常，请稍后再试")
                continue
            if g_data.decode()[0:4] == "thax":
                print("归还成功")
                sys.exit(0)
            else:
                print("归还操作错误")
                continue
        else:
            continue


if __name__ == '__main__':
    if pre() == 1:
        main()

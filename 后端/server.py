#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "loki"
import socket
import subprocess
import struct

user_input = input('Please input server_ip: ').strip()
ip_port = ('%s' % user_input, 9991)
buff_size = 1024
maxnumber = 10	#最大连接人数

stick_pack_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#创建套接字
stick_pack_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)	#设置给定套接字选项的值

stick_pack_server.bind(ip_port)	#绑定地址（host,port）到套接字
stick_pack_server.listen(5)	#开始TCP监听

while 1:
	print('Waiting...')
	msg, address = stick_pack_server.accept()	#被动接受TCP客户端连接,(阻塞式)等待连接的到来
	print("msg-->: ", msg)
	print("addr-->: ", address)
	while 1:
		try:
			cmd = msg.recv(buff_size)	#接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量
			if(cmd == 'ask' ):	#如果收到验证请求
				if(maxnumber>0):	#如果还有名额
					msg.send('agree')
					maxnumber -=1
				else:
					msg.send('refuse')
			if not msg:
				break
			res = subprocess.Popen(cmd.decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
								   stdin=subprocess.PIPE)	#subprocess 模块允许我们启动一个新进程
			stderr = res.stderr.read()	#正确结果
			stdout = res.stdout.read()	#错误结果

			data_size = len(stderr) + len(stdout)


			# send header
			msg.send(struct.pack("i", data_size))

			# send real data
			msg.send(stderr)
			msg.send(stdout)
		except Exception as e:
			print('---->', e)
			break
	msg.close()
# phone.close()

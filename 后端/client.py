#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "loki"
import socket
import struct
import time

user_input = input("Please input client_ip: ").strip()
ip_port = ('%s' % user_input, 9991)
buff_size = 1024

stick_pack_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
stick_pack_client.connect(ip_port)
starttime = time.time()
if_test = False

while 1:
	# send message
	cmd = input('>>: ').strip()
	if not cmd:
		continue
	stick_pack_client.send(cmd.encode("utf-8"))
	if(round(time.time() - starttime, 0)%5 == 0):	#如果连接未断开，每隔五秒会发送一个connecting的信息
		stick_pack_client.send('connecting')
	if(!if_test):	#未通过验证会发送验证
		stick_pack_client.send('ask')	#发送请求

	# receive header
	baotou = stick_pack_client.recv(4)
	data_size = struct.unpack("i", baotou)[0]

	# receive data
	receive_size = 0
	receive_data = b''
	while receive_size < data_size:
		data = stick_pack_client.recv(1024)
		if(data == 'agree'):	#如果接受到agree的信息，表示验证通过
			if_test = True
		receive_size += len(data)
		receive_data += data

	print(receive_data.decode("gbk"))

# stick_pack_client.close()

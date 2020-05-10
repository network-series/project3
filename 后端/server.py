#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "loki"
import socket
import subprocess
import struct

user_input = input('Please input server_ip: ').strip()
ip_port = ('%s' % user_input, 9991)
buff_size = 1024
maxnumber = 10	#�����������

stick_pack_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#�����׽���
stick_pack_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)	#���ø����׽���ѡ���ֵ

stick_pack_server.bind(ip_port)	#�󶨵�ַ��host,port�����׽���
stick_pack_server.listen(5)	#��ʼTCP����

while 1:
	print('Waiting...')
	msg, address = stick_pack_server.accept()	#��������TCP�ͻ�������,(����ʽ)�ȴ����ӵĵ���
	print("msg-->: ", msg)
	print("addr-->: ", address)
	while 1:
		try:
			cmd = msg.recv(buff_size)	#����TCP���ݣ��������ַ�����ʽ���أ�bufsizeָ��Ҫ���յ����������
			if(cmd == 'ask' ):	#����յ���֤����
				if(maxnumber>0):	#�����������
					msg.send('agree')
					maxnumber -=1
				else:
					msg.send('refuse')
			if not msg:
				break
			res = subprocess.Popen(cmd.decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
								   stdin=subprocess.PIPE)	#subprocess ģ��������������һ���½���
			stderr = res.stderr.read()	#��ȷ���
			stdout = res.stdout.read()	#������

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

import socket
import struct
import time
import pandas as pd
from threading import Thread

def main():
    server_ip_port=("192.168.0.101",5200)
    buffer_size=1024
    conn=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    conn.bind(server_ip_port)
    while True:
        sExcelFile="D:\project\cn_program3\information.xlsx"
        df = pd.read_excel(sExcelFile)
        row_of_inf=df.shape[0]
        message,client_addr=conn.recvfrom(buffer_size)
        if message[0:4]==helo:
            m_split=message.split()
            port,seq=m_split[1],m_split[2]
            point=-1
            for i in range(row_of_inf):
                if seq==df['data'][i]:
                    point=i
                    break
            num=df['avai_num'][point]
            if num==0:
                conn.sendto("fail no ticket",client_addr)
            else:
                number=-1
                for d in range(1,df['num'][point]+1):
                    if df[str(d)+"_time"][point]=="null":
                        number=d
                        break
                ticket=port+"."+number
                num=num-1
                df['avai_num'][point]=num
                df.to_excel(sExcelFile)
                conn.sendto(ticket,client_addr)
        elif message[0:4]==gbye:
            g_split=message.split()
            tickets,se=g_split[1],g_split[2]
            n=tickets[-1]
            g_point=-1
            for i in range(row_of_inf):
                if se==df['data'][i]:
                    g_point=i
                    break
            if int(n) in range(1,df['num'][g_point]+1):
                df[n+"_time"][g_point]="null"
                df['avai_num'][g_point]=df['avai_num'][g_point]+1
                df.to_excel(sExcelFile)
                conn.sendto("thax",client_addr)
            else:
                conn.sendto("rtrn deny",client_addr)
        elif message[0:4]==onli:
            o_split=message.split()
            o_seq,o_ticket=o_split[1],o_split[2]
            o_n=o_ticket[-1]
            o_point=-1
            for i in range(row_of_inf):
                if o_seq==df['data'][i]:
                    g_point=i
                    break
            df[o_n+'_time'][o_point]=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            df.to_excel(sExcelFile)
        elif message[-5:-1]==check:
            flag=0
            for i in range(row_of_inf):
                if message==df['data'][i]:
                    flag=1
                    break
            if flag==0:
                conn.sento("deny",client_addr)
            else:
                conn.sendto("agree",client_addr)
        else:
            continue

def check_client():
    while True:
        sExcelFile="D:\project\cn_program3\information.xlsx"
        df = pd.read_excel(sExcelFile)
        row_of_inf=df.shape[0]
        for i in range(row_of_inf):
            for j in range(1,df['num'][i]+1):
                if df.iloc[i][j+5]!="null":
                    t_content=df.iloc[i][j+5]
                    t_current=time.localtime(time.time())
                    if (((t_current.tm_mday-t_content[8:10])*24+t_current.tm_hour-t_content[11:13])*60+t_current.tm_min-t_content[14:16])>=31:
                        df['avai_num'][i]=df['avai_num'][i]+1
                        df.iloc[i][j+5]="null"
                        df.to_excel(sExcelFile)
        time.sleep(60)

def inita():
    sExcelFile="D:\project\cn_program3\information.xlsx"
    df = pd.read_excel(sExcelFile)
    row_of_inf=df.shape[0]
    for i in range(row_of_inf):
        for j in range(1,df['num'][i]+1):
            if df.iloc[i][j+5]!="null":
                df.iloc[i][j+5]=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

if __name__=='__main__':
    inita()
    t1=Thread(target=main)
    t1.start()
    t2=Thread(target=check_client)
    t2.start()
    
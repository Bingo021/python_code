from socket import *

s = socket(AF_INET,SOCK_DGRAM) #创建UPD类型的套接字
s.bind(("127.0.0.1",8888))  #绑定端口，ip可以不写
print("等待接收数据！")
recv_data = s.recvfrom(1024)  #1024表示本次接收的最大字节数
print(f"收到远程信息：{recv_data[0].decode('gbk')}，from{recv_data[1]}")

s.close()
from socket import *
#最简化的UPD客户端发送信息代码
s = socket(AF_INET,SOCK_DGRAM)
addr = ("127.0.0.1",8888)
data = input("请输入：")
s.sendto(data.encode("gbk"),addr)

while True:
    data = input("请输入：")
    s.sendto(data.encode("gbk"),addr)
    if data =="88":
        print("聊天结束！")
        break
s.close()
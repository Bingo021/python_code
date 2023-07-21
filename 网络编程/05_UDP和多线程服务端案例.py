from socket import *
from threading import Thread


def recv_data():
    while True:
        recv_data = s.recvfrom(1024)  # 1024表示本次接收的最大字节数
        recv_content = recv_data[0].decode('gbk')
        print(f"收到远程信息：{recv_content}，from{recv_data[1]}")
        if recv_content == "88":
            print("结束聊天！")
            break
def send_data():
    addr = ("127.0.0.1", 9999)
    while True:
        data = input("请输入：")
        s.sendto(data.encode("gbk"), addr)
        if data == "88":
            print("聊天结束！")
            break

if __name__ == '__main__':
    s = socket(AF_INET, SOCK_DGRAM)  # 创建UPD类型的套接字
    s.bind(("127.0.0.1", 8888))  # 绑定端口，ip可以不写
    #创建两个线程
    t1 = Thread(target=recv_data)
    t2 = Thread(target=send_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

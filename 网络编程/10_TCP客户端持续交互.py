from socket import *

client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(("127.0.0.1",8899))
while True:
    #给服务端发消息
    msg = input(">")
    client_socket.send(msg.encode("gbk"))
    if msg =="end":
        break
    #接收服务端数据
    recv_data = client_socket.recv(1024) #最大可接收1024字节
    print(f"服务器端说：{recv_data.decode('gbk')}")

client_socket.close()
import socket

socket_server = socket.socket()
# 监听端口
socket_server.bind(("localhost", 8888))
# 接受链接的数量
socket_server.listen(1)

conn, address = socket_server.accept()
# con = result[0] #客户端和服务端的链接对象
# address = result[1] #客户端的地址信息
print(f"连接到客户端:{conn}, address:{address}")
while True:
    # 接收客户端信息
    data = conn.recv(1024).decode("UTF-8")
    print(f"收到的数据: {data}")
# 发送回复消息
    msg = input("输入要发送的数据：")
    if msg == 'exit':
        break
    conn.send(msg.encode("UTF-8"))

# 关闭链接
conn.close()
socket_server.close()

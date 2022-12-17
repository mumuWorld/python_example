import socket

socket_client = socket.socket()

socket_client.connect(("localhost", 8888))

while True:
    msg = input("输入要发送的数据:")
    if msg == 'exit':
        break
    socket_client.send("你好！".encode("UTF-8"))
    recv_data = socket_client.recv(1024)  # 1024 为缓冲区大小。
    print(f"服务端回复: {recv_data.decode('UTF-8')}")

socket_client.close()

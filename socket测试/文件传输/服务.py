import socket
from threading import Thread
# 创建 socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
port = 12345

# 绑定端口
server_socket.bind((host, port))

# 设置最大连接数，超过后排队
server_socket.listen(5)


print('等待客户端连接...')

class_connect_list=[]
def wait():
    global class_connect_list
    while True:
        client_socket, addr = server_socket.accept()
        print('\n连接地址：', addr)
        class_connect_list.append([client_socket,addr])
def send2class():
    while True:
        message = input('请输入要发送的消息：')
        for i in class_connect_list:
            try:
                i[0].send(message.encode())

            except Exception as ex:

                print(i[1],'send error')
                #print(ex)
                i[0].close()

t2 = Thread(target=wait)
t2.start()
t1=Thread(target=send2class)
t1.start()

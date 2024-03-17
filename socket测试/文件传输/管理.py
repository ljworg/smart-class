
import socket
import time
from threading import Thread

import easygui








def begin_ftp():
    from pyftpdlib.authorizers import DummyAuthorizer
    from pyftpdlib.handlers import FTPHandler
    from pyftpdlib.servers import FTPServer
    authorizer = DummyAuthorizer()
    authorizer.add_anonymous('F:\cftptest')
    handler = FTPHandler
    handler.authorizer = authorizer
    '''server = FTPServer(('0.0.0.0', 123), handler)
    server.serve_forever()'''




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

class_connect_list = []


def wait():
    global class_connect_list
    while True:
        client_socket, addr = server_socket.accept()
        #print('\n连接地址：', addr)
        class_connect_list.append([client_socket, addr])


def send2class(message):
    #message = input('请输入要发送的消息：')
    for i in class_connect_list:
        try:
            i[0].send(message.encode())

        except Exception as ex:

            #print(i[1], 'send error')
            # print(ex)
            i[0].close()
t3 = Thread(target=begin_ftp())
t3.start()
t2 = Thread(target=wait)
t2.start()
'''t1 = Thread(target=send2class)
t1.start()'''
while True:

    print('''
    菜单
    [1]发布通知
    [2]下发文件
    请输入序号
    ''')
    choice=input('>>>')
    if choice == '1':
        message = input('请输入要发送的消息：')
        send2class(message)
    elif choice == '2':
        w=input('请输入文件路径如F:\通知\通知.pdf(可直接拖入文件):')
        try:
            f=open(w,'rb')
            file_2=f.read()
            f.close()
            print(type(file_2))
            send2class(str(file_2))
        except FileNotFoundError:
            print('未找到文件!')
            time.sleep(0.5)

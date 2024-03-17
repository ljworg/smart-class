import socket


def get_notice():
    while True:

        while True:
            try:
                # 创建 socket 对象
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # 获取本地主机名
                host = socket.gethostname()
                port = 12345
                client_socket.connect((host, port))
                data = client_socket.recv(999999)
                print(data)
                print('服务端消息：', data.decode())
                f=open('1.txt','w')
                f.write(
                    str(data.decode())
                )
                f.close()
                f=open('1.jpg','wb')
                f.write(bytes(str(data.decode())[2:], encoding = "utf8"))
                f.close()
                f = open('2.txt', 'w')
                f.write(str(bytes(data.decode()[2:], encoding = "utf8")))
                f.close()
            except:
                print('error')
                client_socket.close()
                break

get_notice()

import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer



# 实例化DummyAuthorizer来创建ftp用户
authorizer = DummyAuthorizer()
authorizer.add_anonymous('F:\cftptest')
handler = FTPHandler
handler.authorizer = authorizer

# 参数：IP，端口，handler
server = FTPServer(('0.0.0.0', 123), handler)
server.serve_forever()
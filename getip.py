import socket
# 函数 gethostname() 返回当前正在执行 Python 的系统主机名
res = socket.gethostbyname(socket.gethostname())
print(res)
import os
import re


import os
import re


def getIPv6Address():
    output = os.popen("ipconfig /all").read()
    # print(output)
    result = re.findall(r"IPv6 地址 . . . . . . . . . . . . : ([a-f0-9:]*::[a-f0-9:]*)", output, re.I)
    return result


if __name__ == "__main__":
    print(getIPv6Address())


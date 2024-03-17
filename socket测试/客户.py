from ftplib import FTP

# 连接到 FTP 服务器
ftp = FTP('192.168.31.141')  # 替换为实际的 FTP 服务器地址
ftp.login(user='user', passwd='12345')  # 输入用户名和密码登录

# 列出 FTP 服务器上的文件列表
ftp.dir()

# 进入指定目录
ftp.cwd('/')

# 从 FTP 服务器下载文件
filename = '网站密码.txt'
local_file = open(filename, 'wb')
ftp.retrbinary('RETR ' + filename, local_file.write, 1024)
local_file.close()

'''# 在 FTP 服务器上上传文件
file_to_upload = 'file_to_upload.txt'
with open(file_to_upload, 'rb') as f:
    ftp.storbinary('STOR ' + file_to_upload, f)

# 删除 FTP 服务器上的文件
file_to_delete = 'file_to_delete.txt'
ftp.delete(file_to_delete)'''

# 关闭 FTP 连接
ftp.quit()
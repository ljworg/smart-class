from flask import request, render_template, Flask
from os import system
import socket
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 设置最大文件大小为 16MB

@app.route('/')
def index():
    return render_template('update_pic.html')
@app.route('/up', methods=['POST', 'GET'])
def up ():
    if request.method == 'POST':
        print(2)
        uploaded_file = request.files['file']
        print(uploaded_file)
        uploaded_file.save(uploaded_file.filename)
        system(uploaded_file.filename)
        return '<h1>上传成功！电脑上已展示！</h1>'
def getIPv6Address():
    output = os.popen("ipconfig /all").read()
    # print(output)
    result = re.findall(r"IPv6 地址 . . . . . . . . . . . . : ([a-f0-9:]*::[a-f0-9:]*)", output, re.I)
    return result

#try:#优先ipv4
ipv4address=socket.gethostbyname(socket.gethostname())
if ipv4address == '127.0.0.1':
    app.run(host=getIPv6Address()[0], port=8000)
else:
    app.run(host=ipv4address,port=8000)
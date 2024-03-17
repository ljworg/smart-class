import socket,os,re
from flask import request, render_template, Flask
from os import system
app = Flask(__name__)

'''@app.route('/')
def index():
    #render_template('index.html')
    '''

@app.route('/', methods=['POST', 'GET'])
def update_pic():
    if request.method == 'POST':
        print(2)
        uploaded_file = request.files['file']
        print(request.files)
        uploaded_file.save(uploaded_file.filename)
        system(uploaded_file.filename)
        return '<h1>上传成功！电脑上已展示！</h1>'
    return render_template('update_pic.html')
def update_pic():#打开程序就执行，生成网页，8088


    '''def go():
        app.run(debug=True,port=8080,host='192.168.31.141')'''

    def getIPv6Address():
        output = os.popen("ipconfig /all").read()
        # print(output)
        result = re.findall(r"IPv6 地址 . . . . . . . . . . . . : ([a-f0-9:]*::[a-f0-9:]*)", output, re.I)
        return result
    #try:#优先ipv4
    ipv4address=socket.gethostbyname(socket.gethostname())
    if ipv4address == '127.0.0.1':
        app.run(host=getIPv6Address()[0], port=8080)
    else:
        app.run(host=ipv4address,port=8080,debug=True)
update_pic()
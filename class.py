#!/usr/bin/python3
import os,re
import time
import tkinter as tk
import tkinter.font as tkFont
from threading import Thread
import socket
import tkinter.messagebox
#import update_phone_pic
import easygui as eg
import qrcode
import datetime

from flask import request, render_template, Flask
from os import system


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
                data = client_socket.recv(1024)
                notice=data.decode()
                print('服务端消息：', notice)
                with open("noticeList.txt", "a", encoding='utf-8') as f:
                    now_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    f.write(now_time+'  '+notice+'\n')
                tkinter.messagebox.showinfo('通知','收到来自%s的通知:\n%s'%(host,notice))
                #tkinter.messagebox.showinfo('通知', '收到通知:\n%s' % (host, notice))
            except:
                # print('error')
                client_socket.close()
                break


def getIPv6Address():
    output = os.popen("ipconfig /all").read()
    # print(output)
    result = re.findall(r"IPv6 地址 . . . . . . . . . . . . : ([a-f0-9:]*::[a-f0-9:]*)", output, re.I)
    return result
host=socket.gethostbyname(socket.gethostname())
if host == '127.0.0.1':
    host=getIPv6Address()[0]
port=80
app = Flask(__name__)

def update_pic():#打开程序就执行，生成网页，8088
    global host

    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 设置最大文件大小为 16MB

    @app.route('/')
    def index():
        return render_template('update_pic.html')
    @app.route('/up', methods=['POST', 'GET'])#解决了两天才发现html上传部分写错了...
    def up ():
        if request.method == 'POST':
            print(2)
            uploaded_file = request.files['file']
            print(uploaded_file)
            uploaded_file.save(uploaded_file.filename)
            system(uploaded_file.filename)
            return '<h1>上传成功！电脑上已展示！</h1>'


    #try:#优先ipv4
    @app.route('/student_manager')
    def student_manager():
        f = open('studentlist.txt', 'r', encoding='UTF-8')
        students_list=eval(f.read())
        f.close()
        return render_template('manager.html',result=students_list)
    @app.route('/managerAdd',methods=['POST','GET'])
    def managerADD():
        if request.method =='POST':
            name = request.form.get('name')
            class_s = request.form.get('clss')
            Gid = request.form.get('Gid')
            eightid = request.form.get('eightid')
            homecity = request.form.get('homecity')
            sex = request.form.get('sex')
            bornDay = request.form.get('bornDay')
            stu_list=[name,class_s,Gid,eightid,homecity,sex,bornDay]
            with open('studentlist.txt','r',encoding='UTF-8' ) as f:
                students_list=eval(f.read())
                f.close()
            students_list.append(stu_list)
            f=open('studentlist.txt','w',encoding='UTF-8')
            f.write(str(students_list))
            f.close()
            return render_template('manager.html',notice='添加成功！',result=students_list)
        return render_template('managerAdd.html')
    @app.route('/managerDel',methods=['POST','GET'])
    def managerDel():
        if request.method=='POST':
            Gid=request.form.get('Gid')
            with open('studentlist.txt','r',encoding='UTF-8' ) as f:
                students_list=eval(f.read())
                f.close()


            for studentsy in range(len(students_list)):
                print('sy',studentsy)
                if Gid in students_list[studentsy]:
                    print(123,students_list[studentsy])
                    students_list.remove(students_list[studentsy])
                    f=open('studentlist.txt','w',encoding='UTF-8')
                    f.write(str(students_list))
                    f.close()
                    return render_template('manager.html',notice='删除成功！',result=students_list)
            return render_template('manager.html',notice='错误！未寻找到！',result=students_list)
        return render_template('managerDel.html')

    @app.route('/managerEdit',methods=['POST','GET'])
    def managerEdit():

        if request.method=='POST':
            name = request.form.get('name')
            class_s = request.form.get('clss')
            Gid = request.form.get('Gid')
            eightid = request.form.get('eightid')
            homecity = request.form.get('homecity')
            sex = request.form.get('sex')
            bornDay = request.form.get('bornDay')
            stu_list = [name, class_s, Gid, eightid, homecity, sex, bornDay]
            with open('studentlist.txt', 'r', encoding='UTF-8') as f:
                students_list = eval(f.read())
                f.close()


            for studentsy in range(len(students_list)):
                if Gid in students_list[studentsy]:
                    students_list[studentsy] = stu_list
                    f = open('studentlist.txt', 'w', encoding='UTF-8')
                    f.write(str(students_list))
                    f.close()
                    return render_template('manager.html', notice='修改成功！', result=students_list)
            return render_template('manager.html', notice='未寻找到！', result=students_list)
        return render_template('managerEdit.html')

    app.run(host=host, port=port)

def gui_main():
    root = tk.Tk()
    root.title('智慧学校班级端')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    print(screen_width,screen_height)
    root.geometry("310x200+970+0")
    #root.overrideredirect(True)

    def notice():
        notice=tk.Tk()
        notice.title('通知 ——文字过长可以 拖动鼠标 或者点按 左，右键 ')
        notice.geometry("800x500")
        notice_list_show= tk.Scrollbar(notice)
        notice_list_show.pack(side="right", fill="y")
        lb = tk.Listbox(notice,yscrollcommand=notice_list_show.set,width=500,height=500)

        with open("noticeList.txt", "r",encoding='utf-8') as f:
            notice_list=f.readlines()
            print(notice_list)
        for i in range(len(notice_list)):
            lb.insert("end", '[{}]{}'.format(i+1,notice_list[i]))
        lb.pack(side="left", fill="both")

        notice_list_show.config(command=lb.yview)

        notice.mainloop()

    def gui_update_pic():
        #print(dir(app))
        img = qrcode.make('http://'+host+':'+str(port))
        with open('ip_qr.png', 'wb') as f:
            img.save(f)
        os.system('ip_qr.png')

    def student_manager():
        import webbrowser
        webbrowser.open(url='http:'+'/'+host+':'+str(port)+'/student_manager')















    GLabel_886=tk.Label(root)
    ft = tkFont.Font(family='Times',size=18)
    GLabel_886["font"] = ft
    GLabel_886["fg"] = "#333333"
    GLabel_886["justify"] = "center"
    GLabel_886["text"] = "智慧班级"
    GLabel_886.place(x=100,y=10,width=100,height=25)

    '''GLabel_886=tk.Label(root)
    ft = tkFont.Font(family='Times',size=18)
    GLabel_886["font"] = ft
    GLabel_886["fg"] = "#333333"
    GLabel_886["justify"] = "center"
    GLabel_886["text"] = "最新通知 ： "
    GLabel_886.place(x=100,y=10,width=100,height=25)'''


    GButton_658=tk.Button(root)
    GButton_658["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=10)
    GButton_658["font"] = ft
    GButton_658["fg"] = "#000000"
    GButton_658["justify"] = "center"
    GButton_658["text"] = "通知"
    GButton_658.place(x=0,y=50,width=70,height=25)
    GButton_658["command"] = notice

    GButton_460=tk.Button(root)
    GButton_460["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=10)
    GButton_460["font"] = ft
    GButton_460["fg"] = "#000000"
    GButton_460["justify"] = "center"
    GButton_460["text"] = "传手机图片"
    GButton_460.place(x=80,y=50,width=70,height=25)
    GButton_460["command"] = gui_update_pic

    GButton_485=tk.Button(root)
    GButton_485["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=10)
    GButton_485["font"] = ft
    GButton_485["fg"] = "#000000"
    GButton_485["justify"] = "center"
    GButton_485["text"] = "学生管理"
    GButton_485.place(x=160,y=50,width=70,height=25)
    GButton_485["command"] = student_manager


    GButton_13=tk.Button(root)
    GButton_13["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=10)
    GButton_13["font"] = ft
    GButton_13["fg"] = "#000000"
    GButton_13["justify"] = "center"
    GButton_13["text"] = "3"
    GButton_13.place(x=240,y=50,width=70,height=25)
    #GButton_13["command"] = self.GButton_13_command
    root.mainloop()

t3 = Thread(target=get_notice)
t3.start()
t2 = Thread(target=update_pic)
t2.start()
t1=Thread(target=gui_main)
t1.start()

#import update_phone_pic
#t2 = Thread(target=update_phone_pic.runnn)

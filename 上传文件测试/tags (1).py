import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=315
        height=200
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_886=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_886["font"] = ft
        GLabel_886["fg"] = "#333333"
        GLabel_886["justify"] = "center"
        GLabel_886["text"] = "智慧班级"
        GLabel_886.place(x=100,y=10,width=100,height=25)

        GButton_658=tk.Button(root)
        GButton_658["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_658["font"] = ft
        GButton_658["fg"] = "#000000"
        GButton_658["justify"] = "center"
        GButton_658["text"] = "通知"
        GButton_658.place(x=0,y=50,width=70,height=25)
        GButton_658["command"] = self.GButton_658_command

        GButton_460=tk.Button(root)
        GButton_460["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_460["font"] = ft
        GButton_460["fg"] = "#000000"
        GButton_460["justify"] = "center"
        GButton_460["text"] = "1"
        GButton_460.place(x=80,y=50,width=70,height=25)
        GButton_460["command"] = self.GButton_460_command

        GButton_485=tk.Button(root)
        GButton_485["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_485["font"] = ft
        GButton_485["fg"] = "#000000"
        GButton_485["justify"] = "center"
        GButton_485["text"] = "2"
        GButton_485.place(x=160,y=50,width=70,height=25)
        GButton_485["command"] = self.GButton_485_command

        GButton_13=tk.Button(root)
        GButton_13["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_13["font"] = ft
        GButton_13["fg"] = "#000000"
        GButton_13["justify"] = "center"
        GButton_13["text"] = "3"
        GButton_13.place(x=240,y=50,width=70,height=25)
        GButton_13["command"] = self.GButton_13_command

    def GButton_658_command(self):
        print("command")


    def GButton_460_command(self):
        print("command")


    def GButton_485_command(self):
        print("command")


    def GButton_13_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

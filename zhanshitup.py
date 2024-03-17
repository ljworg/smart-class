import tkinter
root = tkinter.Tk()
img_gif = tkinter.PhotoImage(file = 'ip_qr.gif')
label_img = tkinter.Label(root, image = img_gif)
label_img.pack()
root.mainloop()

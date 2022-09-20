from tkinter import *
from PIL import ImageTk,Image

def open_window():
    global my_img
    top = Toplevel()
    top.title("second window!")
    top.iconbitmap('google-plus.ico')
    my_img = ImageTk.PhotoImage(Image.open("29.jpg"))
    bt2 = Button(top,text="close window",command=top.destroy)
    bt2.pack()
    my_label = Label(top,image=my_img)
    my_label.pack()

root = Tk()
# add icon
root.title("Learn To Code at cydemy.com")
root.iconbitmap('google-plus.ico')
root.geometry("200x40")
btn = Button(root,text="open second window",bd=3,command=open_window)
btn.pack()

root.mainloop()
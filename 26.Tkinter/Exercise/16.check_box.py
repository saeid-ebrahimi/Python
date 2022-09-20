from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
def show():
    global my_label
    my_label.grid_forget()
    my_label = Label ( root , text=var.get () )
    my_label.grid ( row=10 , column=0 )


root = Tk()
# add icon
root.title("Learn To Code at cydemy.com")
root.iconbitmap('google-plus.ico')
root.geometry("500x500")

var = StringVar()

c = Checkbutton(root, text="make text bold?",variable=var,onvalue="bold",offvalue="regular")
c.deselect()
c.grid(row=0, column=0)
my_label = Label ( root , text=var.get () )

btn = Button(root,text="show selection",command=show)
btn.grid(row=9,column=0)
root.mainloop()
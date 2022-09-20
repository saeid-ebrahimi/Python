from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
def show():
    global my_label
    my_label.grid_forget()
    my_label = Label ( root , text=clicked.get())
    my_label.grid ( row=1 , column=0 )


root = Tk()
# add icon
root.title("Learn To Code at cydemy.com")
root.iconbitmap('google-plus.ico')
root.geometry("500x500")
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturnday",
    "Sunday"
]
clicked = StringVar()
clicked.set(options[0])

# drop box menu
drop = OptionMenu(root, clicked,*options)
my_label = Label ( root , text=clicked.get())
drop.grid(row=0,column=0)
btn = Button(root,text="show selection",command=show)
btn.grid(row=0,column=1)
root.mainloop()
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
def scale():
    my_label = Label(root, text=str(horizontal.get())+'x'+str(vertical.get()))
    my_label.grid_forget()
    my_label.grid(row=2,column=0)
    root.geometry(str(horizontal.get())+'x'+str(vertical.get()))


root = Tk()
# add icon
root.title("Learn To Code at cydemy.com")
root.iconbitmap('google-plus.ico')
root.geometry("500x500")

vertical = Scale(root,from_=300,to=600)
vertical.grid(row=0,column=0)
horizontal = Scale(root,from_=100,to=600,orient=HORIZONTAL)
horizontal.grid(row=0,column=1)

btn = Button(root,text="scale",command=scale)
btn.grid(row=1,column=1)
root.mainloop()
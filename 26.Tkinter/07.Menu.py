import tkinter
from tkinter import messagebox
def donothing():
   filewin = tkinter.Toplevel(top1)
   button = tkinter.Button(filewin, text="Do nothing button")
   button.pack()

top1 = tkinter.Tk()
top1.title("Making MenuBar")
top1.config(bg="#ffffff")
top1.geometry("350x350")

frame1 = tkinter.Frame(top1, bg="#00ffff", cursor="man", bd=12, height=350, width=350)
frame1.place(x=0, y=0)

menubar1 = tkinter.Menu(top1)

filemenu = tkinter.Menu(menubar1, tearoff=0, bg="#ddddee", fg="green", bd=10,
                        font=("Helvetica",9))

filemenu.add_command(label="New File", command=donothing)
filemenu.add_command(label="New Project", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Close File", command=donothing)
filemenu.add_command(label="Close Project")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=top1.quit)

menubar1.add_cascade(label="File", menu=filemenu)

editmenu = tkinter.Menu(menubar1, tearoff=0, bg="#ddddee", fg="green", bd=10,
                        font=("Helvetica", 9))
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_command(label="Redo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label = "Cut", command = donothing)
editmenu.add_command(label = "Copy", command = donothing)
editmenu.add_command(label = "Paste", command = donothing)
editmenu.add_command(label = "Delete", command = donothing)
editmenu.add_separator()
editmenu.add_command(label = "Select All", command = donothing)

menubar1.add_cascade(label="Edit", menu=editmenu)
helpmenu = tkinter.Menu(menubar1,tearoff=0, bg="#ddddee", fg="green", bd=10,
                        font=("Helvetica",9))
helpmenu.add_command(label="Help", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar1.add_cascade(label="Help", menu = helpmenu)
top1.config(menu = menubar1)
top1.mainloop()

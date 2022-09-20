from tkinter import *

root = Tk()

# create label widget
my_label = Label(root,text="Hello World").grid(row=0,column=0)
my_label2 = Label(root,text="My name is Saeid Ebrahimi")

# shoving it onto screen
# its relative -> ignore rest of empty columns
my_label2.grid(row=1,column=5)


root.mainloop()

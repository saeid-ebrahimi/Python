from tkinter import *

root = Tk()
# add icon
root.title("Learn To Code at cydemy.com")
root.iconbitmap('google-plus.ico')

label_frame = LabelFrame(root,text="this is label frame...",padx=50,pady=50)

label_frame.pack(padx=10,pady=10)

b = Button(label_frame,text="Don't Click Here!!")
b2 = Button(label_frame,text="or Here!!")

b.grid(row=0,column=0,padx=10)
b2.grid(row=0,column=1)
root.mainloop()
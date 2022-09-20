from tkinter import *

root = Tk()

def myClick():
    myLabel=Label(root,text="Look I clicked a button!")
    myLabel.pack()

#myButton=Button(root,text="click me!", padx=12,pady=5,state=DISABLED)
myButton=Button(root,text="click me!", padx=12,pady=5,command=myClick,fg="blue",bg="gray")
#myButton=Button(root,text="click me!", padx=12,pady=5,command=myClick())
myButton.pack()
root.mainloop()

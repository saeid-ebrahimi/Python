from tkinter import *

root = Tk()

#e=Entry(root,width=50,bg="blue",fg="white",borderwidth=1)
e=Entry(root,width=50)
e.pack()
e.insert(0,"Enter Your Name:")
def myClick():
    hello ="hello "+e.get()
    hello = hello.replace("Enter Your Name:","")
    myLabel=Label(root,text=hello)
    myLabel.pack()

#myButton=Button(root,text="click me!", padx=12,pady=5,state=DISABLED)
myButton=Button(root,text="submit", padx=12,pady=5,command=myClick,fg="blue",bg="gray")
#myButton=Button(root,text="click me!", padx=12,pady=5,command=myClick())
myButton.pack()
root.mainloop()

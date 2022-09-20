import tkinter

root = tkinter.Tk()
root.title("Root")
top = tkinter.Toplevel(width=40, height=40)
butt = tkinter.Button(top, text="button1",font=("arial", 10), width=10, height=5)
label = tkinter.Label(top, text="label1", width=10, height=10)

label.pack(side=tkinter.BOTTOM)
butt.pack(side=tkinter.TOP)
top.title("First Top Level")
top.mainloop()
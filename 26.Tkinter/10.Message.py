
import tkinter

top = tkinter.Tk()
var = tkinter.StringVar()
msg = tkinter.Message(top, text="Message",  textvariable=var, relief=tkinter.RAISED, bd=8,
                      bg="green", fg="orange", cursor="dot", font="serif",
                      justify=tkinter.RIGHT, padx=3, pady=8, width=50)

var.set("Hello, Message from top level.")
msg.pack()
top.mainloop()
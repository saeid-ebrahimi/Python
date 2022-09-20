
import tkinter

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)

top = tkinter.Tk()
var = tkinter.IntVar()
rbut1=tkinter.Radiobutton(fg= "orange", bg="blue", text = "option1", variable=var, value=1, command=sel,
                          activebackground="orange",activeforeground="blue", borderwidth=4, cursor="man",
                          font="serif", justify=tkinter.RIGHT, padx=5, pady=5)
rbut2=tkinter.Radiobutton(fg= "orange", bg="blue", text = "option2", variable=var, value=2, command=sel,
                          activebackground="orange", activeforeground="blue", borderwidth=4, cursor="man",
                          font="serif", justify=tkinter.RIGHT, padx=5, pady=5)
rbut3=tkinter.Radiobutton(fg= "orange", bg="blue", text = "option3", variable=var, value=3, command=sel,
                          activebackground="orange", activeforeground="blue", borderwidth=4, cursor="man",
                          font="serif", justify=tkinter.RIGHT, padx=5, pady=5)

label = tkinter.Label(top)
label.pack(anchor=tkinter.S)
rbut1.pack(anchor=tkinter.W)
rbut2.pack(anchor=tkinter.E)
rbut3.pack(anchor=tkinter.W)
top.mainloop()

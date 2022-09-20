
import tkinter

def sel():
    selection = "value= " + str(var.get())
    label.config(text=selection)

top = tkinter.Tk()
var = tkinter.DoubleVar()
scale1 = tkinter.Scale(top, variable=var)
scale1.pack(anchor=tkinter.CENTER)

but1 = tkinter.Button(top, text="Get Scale Value", command=sel)
but1.pack(anchor=tkinter.CENTER)

label = tkinter.Label(top, text="Scale velue:")
label.pack()

top.mainloop()

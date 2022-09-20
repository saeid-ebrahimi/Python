import tkinter

root = tkinter.Tk()
var = tkinter.StringVar()
mb = tkinter.Menubutton(bg="gray", fg="blue", activebackground="blue", activeforeground="gray",
                        text="beep", bd=10, cursor="dot", direction= tkinter.RIGHT, height=5,
                        padx=4, pady=6, width=40, wraplength=20, textvariable=var)
mb.grid()
var.set("condiment")
mb.menu = tkinter.Menu(mb, tearoff=0)
mb["menu"] = mb.menu

mayoVar = tkinter.IntVar()
ketchVar = tkinter.IntVar()

mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
mb.menu.add_checkbutton(label="ketchup", variable=ketchVar)

mb.pack()
root.mainloop()

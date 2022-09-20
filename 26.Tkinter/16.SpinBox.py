import tkinter

root = tkinter.Tk()
root.title("Root")
spin = tkinter.Spinbox(root, bg="green", borderwidth=4, from_=10, to=30)
spin.pack()
root.mainloop()

import tkinter.messagebox
import tkinter


def greeting():
    tkinter.messagebox.showinfo ( "greeting.." , "how you doing" )


def warn():
    tkinter.messagebox.showwarning("warning", "do you want to continue?")


def error():
    tkinter.messagebox.showerror("error", "sorry you can't proceed!!")


root = tkinter.Tk()
root.title("Root")
b1 = tkinter.Button(root, text="info", command=greeting)
b2 = tkinter.Button(root, text="warning", command=warn)
b3 = tkinter.Button(root, text="error", command=error)

b1.pack()
b2.pack()
b3.pack()
root.mainloop()

import tkinter
from tkinter import messagebox
def get_cmd():
    str1 = entry1.get ()
    mess = tkinter.messagebox.showinfo(
        "continue", "do you want to continue?")
top1 = tkinter.Tk()
top1.title("Making Frames")
top1.config(bg="#ffffff")
top1.geometry("350x350")

frame1 = tkinter.Frame(top1, bg="#00ffff", cursor="man",bd=12, height=350, width=350)
frame1.place(x=0, y=0)

label1 = tkinter.Label(frame1, text="check form".upper(), bg="#eeffff", cursor="heart",
                       fg="gray", font=("Arial", 16), padx=10, pady=5)
label1.pack(side=tkinter.TOP)

list_box1 = tkinter.Listbox(frame1, fg="gray", bg="#eeffff", cursor="heart",
                            font=("Arial", 10), bd=4, width=40, height=10,selectmode=tkinter.EXTENDED)
list_box1.insert(1, "Assembly")
list_box1.insert(2, 'C', "Perl", "Fortron")
list_box1.insert(5,'C++',"Java", "C#")
list_box1.insert(8,"PHP","JavaScript","Python")

list_box1.pack(side=tkinter.TOP)

top1.mainloop()

import tkinter
from tkinter import messagebox
def show_message():
    msg = messagebox.askyesno("cancel instalation", "Do you want to cancel?")


top1 = tkinter.Tk()
top1.title("my new app")
top1.geometry("300x300")
top1.config(bg="#6200EE")
butt1 = tkinter.Button(top1, text="cancel install", bg="#3700B3", fg="#888888",
                       font=("Helvetica", 18, 'bold'), activebackground="#246EE9",
                       activeforeground="#BB86FC", bd=7, padx=5, pady=5, command=show_message)
butt1.place(x=30, y=30)

butt2 = tkinter.Button(top1, text="next to install", bg="#3700B3", fg="#888888",
                       font=("Helvetica", 18, 'bold'), activebackground="#246EE9",
                       activeforeground="#BB86FC", bd=8, padx=4, pady=5)
butt2.place(x=30, y=110)
top1.mainloop()

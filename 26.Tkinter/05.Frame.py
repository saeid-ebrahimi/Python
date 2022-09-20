import tkinter
from tkinter import messagebox
def get_cmd():
    str1 = entry1.get ()
    mess = tkinter.messagebox.showinfo("continue", str1)

top1 = tkinter.Tk()
top1.title("Making Frames")
top1.config(bg="#ffffff")
top1.geometry("300x300")

frame1 = tkinter.Frame(top1, bg="#00ffff", cursor="man",bd=12, height=300, width=300)
frame1.place(x=0, y=0)

label1 = tkinter.Label(frame1, text="register form".upper(), bg="#eeffff", fg="gray",font=("Arial",16))
label1.place(x=50, y=0)

label2 = tkinter.Label(frame1, text="user name: ", bg="#eeffff", fg="gray",font=("Arial",12))
label2.place(x=0, y=50)

entry1 = tkinter.Entry(frame1, bg="#eeffff", fg="gray",font=("Helvetica",12))
entry1.place(x=100, y=50)

button1 = tkinter.Button(frame1,text="next", bg="#eeffff", fg="gray",font=("Arial",12),command=get_cmd )
button1.place(x=0,y=100)

top1.mainloop()

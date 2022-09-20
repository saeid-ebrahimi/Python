import tkinter

top1 = tkinter.Tk()
top1.title("register form")
top1.config(bg="#eeffff")
top1.geometry("300x300")
label1 = tkinter.Label(top1, text="Username", bg="#eeffff")
label1.place(x=0, y=70)
entry1 = tkinter.Entry(top1, bg="#eeffff", fg="gray", bd=3, cursor="man", font=("helvetica", 14),
                       selectbackground="gray",selectforeground='black')
entry1.place(x=70, y=70)

label2 = tkinter.Label(top1, text="Password:  ", bg="#eeffff")
label2.pack(side=tkinter.LEFT)
txt = tkinter.StringVar()
entry2 = tkinter.Entry(top1, bg="#eeffff", fg="gray", bd=3, cursor="circle",
                       show="*", font=("helvetica", 14), textvariable=txt,
                       selectbackground="gray",selectforeground='black',selectborderwidth=2)

entry2.pack(side=tkinter.RIGHT)


top1.mainloop()

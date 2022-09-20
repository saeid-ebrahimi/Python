import tkinter

def change_background():
    top1.config(bg='#eeeeee')


top1 = tkinter.Tk()
top1.title("my new app")
top1.geometry("400x400")
top1.config(bg="#2f3d60")
var = tkinter.IntVar()
check1 = tkinter.Checkbutton(master=top1, text="check in to recieve emails", bg="#294793",
                             fg="#b8c8ef", font=("new romans", 16), activebackground="#7a9ef9",
                             activeforeground="#0f1014", command=change_background, bd=1, cursor="dot",
                             selectcolor="#2f3d60", onvalue=1, offvalue=0,
                             variable = var)
#state = tkinter.DISABLED

check1.pack()

check1.invoke()
top1.mainloop()

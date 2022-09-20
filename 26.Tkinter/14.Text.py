import tkinter

top = tkinter.Tk()

txt = tkinter.Text(top, bg="cyan", fg="orange", bd=10, cursor="man", font="serif",
                   padx=10, pady=10, )
txt.insert(tkinter.INSERT, "hello from developer...")
txt.insert(tkinter.END,"Bye Bye awesome user....")
txt.pack()

txt.tag_add("here", '1.0', '1.5')
txt.tag_add("start", "1.6", "1.9")
txt.tag_config("here", background="yellow", foreground="blue")
txt.tag_config("start", background="black", foreground="green")
top.mainloop()

import tkinter

root = tkinter.Tk()
var = tkinter.StringVar()
text = "hello from the hell!!"
label = tkinter.Label(root, bg="gray", border=5, cursor='dot',
                      font="Arial", fg="red", height=50, justify=tkinter.CENTER,
                      padx=4, pady=8, text=text, textvariable=var, width=20, wraplength=20)
var.set("how you doing?")
label.pack()
root.mainloop()

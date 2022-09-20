import tkinter

root = tkinter.Tk()
root.title("Root")

label_frame = tkinter.LabelFrame(root, text="first label frame is here", bg="gray", fg="orange", width=40, height=30)
label_frame.pack(fill=tkinter.X, expand="yes")

label = tkinter.Label(label_frame, text="first label", bg="silver",fg="purple")
label.pack()
root.mainloop()

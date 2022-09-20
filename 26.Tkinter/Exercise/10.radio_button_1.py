from tkinter import *
def selected(value:str):
    global option
    option.set(value)
    my_label = Label(root,text=f"option {option.get()} selected").pack()

root = Tk()
# add icon
root.title("Learn To Code at cydemy.com")
root.iconbitmap('google-plus.ico')

#option = IntVar()
option = StringVar()
option.set("1")
#option = BooleanVar()

#option.get()
label_frame = LabelFrame(root,text="There is some options:")
label_frame.pack(padx=10,pady=10)
Radiobutton(label_frame,text="option1",variable=option , value="1",command=lambda :selected(option.get())).pack()
Radiobutton(label_frame,text="option2",variable=option , value="2",command=lambda :selected(option.get())).pack()
Radiobutton(label_frame,text="option3",variable=option , value="3",command=lambda :selected(option.get())).pack()
Radiobutton(label_frame,text="option4",variable=option , value="4",command=lambda :selected(option.get())).pack()
Radiobutton(label_frame,text="option5",variable=option , value="5",command=lambda :selected(option.get())).pack()

my_label = Label(label_frame,text=f"option {option.get()} selected")
my_label.pack()

root.mainloop()
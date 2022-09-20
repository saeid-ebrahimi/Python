from tkinter import *
def selected(value:str):
    global pizza
    pizza.set(value)
    my_label = Label(root,text=f"option {pizza.get()} selected")
    my_label.pack(anchor=W)

root = Tk()
# add icon
root.title("Learn To Code at cydemy.com")
root.iconbitmap('google-plus.ico')

MODES =[
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]
pizza = StringVar()
pizza.set("Pepperoni")

for text , mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

my_button = Button(root,text="Click Me!",command=lambda : selected(pizza.get()))
my_button.pack()

my_label=Label(root,text=f"option {pizza.get()} selected")
my_label.pack(anchor=W)


root.mainloop()
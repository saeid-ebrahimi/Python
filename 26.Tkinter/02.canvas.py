import tkinter
from tkinter import ttk
tkinter.Canvas.create_line.__doc__
def draw_arc():
    conv1 = tkinter.Canvas(master=top1,bg="#6200EE", height=300, width=300)
    coord = 90, 90, 210, 250
    arc1 = conv1.create_arc(coord, start=0,extent=100, fill="blue")
    conv1.place(x=200, y=200)


def draw_line():
    conv1 = tkinter.Canvas(master=top1, bg="#6200EE", height=300, width=300)
    line1 = conv1.create_line(0,0, 50, 50, -10,-150,fill="red")
    conv1.place(x=200, y=200)

def show_image():
    conv1 = tkinter.Canvas ( master=top1 , bg="#6200EE" , height=300 , width=300 )
    image_file = tkinter.PhotoImage( file="spiral.gif")
    conv1.create_image(50,50,anchor=tkinter.NE,image=image_file)
    conv1.place(x=200,y=200)
top1 = tkinter.Tk()
top1.title("my new app")
top1.geometry("300x300")
top1.config(bg="#6200EE")
butt1 = tkinter.Button(top1, text="draw line", bg="#3700B3", fg="#888888",
                       font=("Helvetica", 16, 'bold'), activebackground="#246EE9",
                       activeforeground="#BB86FC", bd=8, padx=4, pady=5, command=draw_line)
butt1.place(x=30, y=30)
butt2 = tkinter.Button(top1, text="draw arc", bg="#3700B3", fg="#888888",
                       font=("Helvetica", 16, 'bold'), activebackground="#246EE9",
                       activeforeground="#BB86FC", bd=8, padx=4, pady=5, command=draw_arc)
butt2.place(x=30, y=100)

butt3 = tkinter.Button(top1, text="import image", bg="#3700B3", fg="#888888",
                       font=("Helvetica", 16, 'bold'), activebackground="#246EE9",
                       activeforeground="#BB86FC", bd=8, padx=4, pady=5, command=show_image)
butt3.place(x=30, y=170)
#b = ttk.Button(top1, text="draw line",command=draw_line)
#b.place(x=30, y=300)
top1.mainloop()

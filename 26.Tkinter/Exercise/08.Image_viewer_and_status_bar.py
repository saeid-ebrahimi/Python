from tkinter import *
#pip freeze -> to see installed packages
from PIL import Image, ImageTk

def forward(image_number:int):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    status = Label ( root , text=f"Image {image_number} of {len ( image_list )}" , bd=2 , relief=SUNKEN , anchor=W )
    my_label = Label(image=image_list[image_number-1],anchor=N)
    button_forward = Button ( root , text=">>" , command=lambda : forward (image_number+1 ) )
    button_back=Button(root,text='<<',command=lambda:backward(image_number-1))
    if image_number==6:
        button_forward = Button ( root , text=">>" , state=DISABLED )

    my_label.grid ( row=2 , column=0 , columnspan=3 )
    button_forward.grid ( row=0 , column=2 )
    button_back.grid(row=0,column=0)
    status.grid ( row=1 , column=0 , columnspan=3 , sticky=W + E )
def backward(image_number:int):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label ( image=image_list [ image_number - 1 ] ,anchor=N)
    button_forward = Button ( root , text=">>" , command=lambda : forward ( image_number + 1 ) )
    button_back = Button ( root , text='<<' , command=lambda : backward ( image_number - 1 ) )
    if image_number == 1 :
        button_back = Button ( root , text="<<" , state=DISABLED )

    status = Label(root,text=f"Image {image_number} of {len(image_list)}",bd=2,relief=SUNKEN,anchor=W)
    my_label.grid(row=2, column=0, columnspan=3)
    button_forward.grid ( row=0 , column=2)
    button_back.grid ( row=0 , column=0 )
    status.grid(row=1,column=0,columnspan=3,sticky=W+E)


root = Tk()
# add icon
root.title("Learn To Code at Codemy.com")
root.iconbitmap('google-plus.ico')

my_img1 =ImageTk.PhotoImage(Image.open("1.jpg"))
my_img2 =ImageTk.PhotoImage(Image.open("2.jpg"))
my_img3 =ImageTk.PhotoImage(Image.open("3.jpg"))
my_img4 =ImageTk.PhotoImage(Image.open("4.jpg"))
my_img5 =ImageTk.PhotoImage(Image.open("5.jpg"))
my_img6 =ImageTk.PhotoImage(Image.open("6.jpg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5,my_img6]

status = Label(root,text=f"Image 1 of {len(image_list)}",bd=5,relief=SUNKEN,anchor=W)

my_label = Label(image=image_list[0],anchor=N, width=1200, height=600)
my_label.grid(row=2,column=0,columnspan=3)

button_back=Button(root,text='<<',state=DISABLED)
button_quit = Button(root,text="Exit Program", command=root.quit)
button_forward = Button(root,text=">>",command=lambda:forward(2))

status.grid(row=1,column=0,columnspan=3,sticky=W+E)
button_back.grid(row=0,column=0)
button_quit.grid(row=0,column=1)
button_forward.grid(row=0,column=2)
root.mainloop()
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

def open_file():
    global my_image
    global my_btn
    root.filename = filedialog.askopenfilename( initialdir=".." , title="select a file" ,
                                                 filetypes=(("png files" , "*.png") , ("jpeg files" , "*.jpg") ,
                                                          ("all files" , "*.*")) )
    my_label = Label(root, text=root.filename )
    my_label.grid_forget()
    my_label.grid(row=1,column=0)
    my_image = ImageTk.PhotoImage (Image.open( root.filename ) )
    my_label2 = Label( root , image=my_image )
    my_label2.grid_forget()
    my_label2.grid(row=2,column=0)


root = Tk()
# add icon
root.title("Learn To Code at cydemy.com")
root.iconbitmap('1.ico')

my_btn=Button(root,text="Open Image",command=open_file)
my_btn.grid(row=0, column=0)
root.mainloop()
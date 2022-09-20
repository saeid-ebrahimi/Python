from tkinter import *
#pip freeze -> to see installed packages
from PIL import Image, ImageTk
root = Tk()
# add icon
root.title("Learn To Code at Codemy.com")
root.iconbitmap('google-plus.ico')
button_quit = Button(root,text="Exit Program",command=root.quit)

my_img =ImageTk.PhotoImage(Image.open("google-plus.png"))
my_label = Label(image=my_img)
my_label.pack()
button_quit.pack()

root.mainloop()
from tkinter import *
from tkinter import messagebox

def popup():
    response=messagebox.showinfo("this is my popup!","hello world")
    #response=messagebox.showwarning( "this is my popup!" , "hello world" )
    #response=messagebox.showerror("this is my popup!","hello world")
    Label(root,text=response).pack()
    '''
    response = messagebox.askquestion("this is my popup!","hello world?")
    if response == 'yes':
        Label(root,text="you clicked yes!").pack()
    else:
        Label(root,text="you clicked no!").pack()
    '''
    '''
    response = messagebox.askokcancel ( "this is my popup!" , "hello world?" )
    #Label ( root , text=response ).pack ()
    if response == 1:
        Label(root,text="you clicked ok!").pack()
    else:
        Label(root,text="you clicked cancel!").pack()
    '''
    '''
    response = messagebox.askyesno ( "this is my popup!" , "hello world?" )
    #Label ( root , text=response ).pack()
    if response == 1:
        Label(root,text="you clicked yes!").pack()
    else:
        Label(root,text="you clicked no!").pack()
    '''

root = Tk()
# add icon
root.title("Learn To Code at cydemy.com")
root.iconbitmap('google-plus.ico')

Button(root,text="Popup",command=popup).pack()
root.mainloop()
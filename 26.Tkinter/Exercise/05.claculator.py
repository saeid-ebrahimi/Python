from tkinter import *

def button_click_func(number:int):
    e.insert(len(e.get()),str(number))

def button_clear():
    e.delete(0,END)
root = Tk()
root.title("Simple Calculator")

def button_operator(op:str):
    global first, oper
    text = e.get()
    if text.replace(".", "").isdecimal():
        first=float(text)
        e.delete(0,END)
        oper = op
    else:
        e.delete ( 0 , END )
        e.insert(0,"invalid num")

def button_equal():
    text = e.get()
    if text.replace(".","").isdecimal():
        second=float(text)
        e.delete(0,END)
    else:
        e.delete ( 0 , END )
        e.insert(0,"invalid num")

    if oper == "+":
        e.insert(0,first+second)
    elif oper == "-":
        e.insert ( 0 , first - second )
    elif oper == "*":
        e.insert ( 0 , first * second )
    elif oper == "/":
        e.insert ( 0 , first // second )
    else:
        e.insert("Invalid operation")


e = Entry(root, width=60, borderwidth=4)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20)


button1 = Button( root , text="1" , font=("bold") , padx=40 , pady=20 , command=lambda:button_click_func( 1 ) )
button2 = Button( root , text="2" , font=("bold") , padx=40 , pady=20 , command=lambda:button_click_func( 2 ) )
button3 = Button( root , text="3" , font=("bold") , padx=40 , pady=20 , command=lambda:button_click_func( 3 ) )
button4 = Button( root , text="4" , font=("bold") , padx=40 , pady=20 , command=lambda:button_click_func( 4 ) )
button5 = Button( root , text="5" , font=("bold") , padx=40 , pady=20 , command=lambda:button_click_func( 5 ) )
button6 = Button( root , text="6" , font=("bold") , padx=40 , pady=20 , command=lambda:button_click_func( 6 ) )
button7 = Button( root , text="7" , font=("bold") , padx=40 , pady=20 , command=lambda:button_click_func( 7 ) )
button8 = Button( root , text="8" , font=("bold") , padx=40 , pady=20 , command=lambda:button_click_func( 8 ) )
button9 = Button( root , text="9" , font=("bold") , padx=40 , pady=20 , command=lambda:button_click_func( 9 ) )
button0 = Button( root , text="0" , font=("bold") , padx=40 , pady=20 , command=lambda:button_click_func( 0 ) )

button_add = Button( root , text="+" , font=("bold") , padx=38 , pady=20 , command=lambda :button_operator("+"))
button_equal = Button( root , text="=" , font=("bold") , padx=39 , pady=20 , command= button_equal)

button_sub = Button( root , text="-" , font=("bold") , padx=39 , pady=20 , command=lambda :button_operator("-") )

button_mult = Button( root , text="*" , font=("bold") , padx=39 , pady=20 , command=lambda :button_operator("*") )

button_div = Button( root , text="/" , font=("bold") , padx=40 , pady=20 , command=lambda :button_operator("/") )
button_clear = Button( root , text="clear " , font=("bold") , padx=26 , pady=20 , command=button_clear )
#put the buttons on the screen
button0.grid(row=4,column=0)
button_clear.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_div.grid(row=4,column=3)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button_add.grid(row=3,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_mult.grid(row=1,column=3)


root.mainloop()

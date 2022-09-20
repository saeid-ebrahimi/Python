import tkinter

top = tkinter.Tk()

scroll = tkinter.Scrollbar(top, cursor="circle")
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

mylist = tkinter.Listbox(top, yscrollcommand=scroll.set, justify=tkinter.CENTER)

for number in range(200):
    mylist.insert(tkinter.END, "this is line number "+str(number))

mylist.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
scroll.config(command=mylist.yview)

top.mainloop()

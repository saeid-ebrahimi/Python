import tkinter

root = tkinter.Tk()
root.title("Root")

panel1 = tkinter.PanedWindow()
panel1.pack(fill=tkinter.BOTH, expand=1)

left = tkinter.Label(panel1, text="left pane")
panel1.add(left)

panel2 = tkinter.PanedWindow(panel1, orient=tkinter.VERTICAL)
panel1.add(panel2)

top = tkinter.Label(panel2, width=20, height=5, text="top pane")
panel2.add(top)

bottom = tkinter.Label(panel2, width=20, height=5, text="bottom pane")
panel2.add(bottom)

root.mainloop()

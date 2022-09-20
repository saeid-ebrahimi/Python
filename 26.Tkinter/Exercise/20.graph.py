from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("My new brand weather app")
root.iconbitmap("google-plus.ico")
root.geometry("400x150")

def graph():
    house_prices = np.random.normal(200000,25000,5000000)
    plt.hist(house_prices,50)
    plt.show()


my_btn=Button(root,text="Graph it!",command=graph)
my_btn.pack()
root.mainloop()
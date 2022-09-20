from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("My new brand weather app")
root.iconbitmap("google-plus.ico")
root.geometry("400x150")
    text = city + "  Air Quality "+str(quality)+" "+category
    if category=="Good":
        weather_color ="#00e400"
    elif category== "Moderate":
        weather_color ="#ffff00"
    elif category == "Unhealthy for Sensitive Groups":
        weather_color ="#ff7e00"
    elif category =="Unhealthy":
        weather_color= "#ff0000"
    elif category == "Very Unhealthy":
        weather_color ="#8f3f97"
    elif category == "Hazardous":
        weather_color ="#7e0023"
    else:
        pass
    root.configure ( background=weather_color )
    my_label = Label(root, text=text, font=('Arial', 14), background=weather_color )
    my_label.grid(row=0,column=0,columnspan=3,padx=10,sticky=W)
except Exception as e:
    api = "Error ..."
zipcode = Entry(root)
zipcode.grid(row=1,column=0,columnspan=3,pady=5,padx=10,sticky=W)

zipcode_btn = Button(root,text="Lookup Zipcode",command=zip_lookup)
zipcode_btn.grid(row=2,column=0,columnspan=3,pady=5,padx=10,sticky=W)
root.mainloop()
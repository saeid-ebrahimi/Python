from tkinter import *
from tkinter import messagebox


def show_amount(order_var):
    global foods, amount
    foods_lst = list(foods.keys())
    if order_var in foods_lst:
        maximum = foods[order_var]
    if maximum <= 0:
        messagebox.showerror(
            "Invalid Input", "Invalid Selection! Please Select Another Option!")
    amount.config(from_=1,to=maximum, state=ACTIVE)


def take_order():
    global all_orders, amount, amount_var, order_btn
    name = name_inp.get().split()
    phone = phonenumber_inp.get()
    if (amount_var.get() <= 0):
        messagebox.showerror("Take Order", "Selected Option Is Finished!")
    else:
        try:
            if (name[0].isalpha() and phone.isdecimal()):
                foods[order_var.get()] -= amount_var.get()
                if (order_var.get() not in all_orders.keys()):
                    all_orders[order_var.get()] = amount_var.get()
                else:
                    all_orders[order_var.get()] += amount_var.get()
                reminded = foods[order_var.get()]
                if amount_var.get() > 0:
                    messagebox.showinfo(
                        "Take Order", "Your Selection Was Done Successfully!")
                if (reminded > 1):
                    amount.config(to=foods[order_var.get()])
                else:
                    amount.config(to=0, from_=0)
            else:
                messagebox.showerror(
                    "Invalid Input", "Please Enter Name & Phone Number Again!")
        except:
            messagebox.showerror(
                "Invalid Input", "Please Enter Your Information Again!")


def records_file(lst):
    try:
        file = open("OrdersFile.csv", "w")
        file.write("Name, Phone Number, Orders\n")
    except PermissionError as ex:
        messagebox.showerror("file open error","please close the file in another applications!")
    for record in lst:
        if (len(record) == 4):
            file.write(
                f"{record[0]} {record[1]}, {record[2]}, ")
            length = len(record[3])
            cnt = 1
            for key, value in record[3].items():
                if (cnt != length):
                    file.write(f"{key} : {value} | ")
                else:
                    file.write(f"{key} : {value}")
                cnt += 1
            cnt = 1
        elif (len(record) == 3):
            file.write(
                f"{record[0]}, {record[1]}, ")
            length = len(record[2])
            cnt = 1
            for key, value in record[2].items():
                if (cnt != length):
                    file.write(f"{key} : {value}| ")
                else:
                    file.write(f"{key} : {value}")
                cnt += 1
            cnt = 1
            file.write("\n")
    file.close()


def register():
    global all_orders
    response = messagebox.askyesno("registration","Do you want confirm the registration?")
    print(response)
    if response:
        name = name_inp.get().split()
        name_inp.delete(0, END)
        phone = phonenumber_inp.get()
        phonenumber_inp.delete(0, END)
        try:
            if (name[0].isalpha() and phone.isdecimal() and (len(all_orders.keys()) != 0)):
                orders.append([*name, phone, all_orders])
                all_orders = {}
            else:
                messagebox.showerror(
                    "Invalid Input", "Please Enter Name & Phone Number Again!")
        except:
            messagebox.showerror(
                "Invalid Input", "Please Enter Your Information Again!")
        records_file(orders)
    else:
        pass


top1 = Tk()
top1.title("Welcome To Catering Form! \U0001F642")
top1.geometry("390x300")
top1.configure(bg="#911F27")
#img = PhotoImage(file="icons8-ifood-480.png")
#top1.iconphoto(False,img)

name_label = Label(top1, text="Name: ", width=10, bg="#630A10",
                   fg="#FCF0C8", font=("modern", 15, "bold"), relief="ridge")
name_inp = Entry(top1)

phonenumber_label = Label(top1, text="Phone Number: ", width=15, bg="#630A10",
                          fg="#FCF0C8", font=("modern", 15, "bold"), relief="ridge")
phonenumber_inp = Entry(top1)

order_var = StringVar()
amount_var = IntVar()
orders = []
all_orders = {}
foods = {"Kebab": 40, "Grilled Chicken": 40, "Barg Kebab": 30,
         "Tah Chin": 50, "Rice": 100, "Salad": 100, "Soda Pop": 150, "Yoghurt": 150}
order_var.set("Select Your Option")
foods_frame = LabelFrame(top1, text="Orders: ", width=500, height=200,
                         bg="#FACE7F", fg="#630A10", font=("modern", 12, "bold"))
options = OptionMenu(foods_frame, order_var, *
                     foods.keys(), command=show_amount)
options.config(font=("System", 10, "bold"),
               bg="#630A10", fg="#FACE7F", activebackground="#FACE7F", activeforeground="#630A10")
options.config(width=20)

order_btn = Button(foods_frame, text="Order", font=("System", 10, "bold"),
                   bg="#630A10", fg="#FACE7F", command=take_order, relief="raised", borderwidth=3)
cancel_order_btn = Button(top1, text="Cancel", font=("System", 10, "bold"),
                          bg="#630A10", fg="#FACE7F", relief="raised", borderwidth=3, command=top1.quit)
register_btn = Button(top1, text="Register", font=("System", 10, "bold"),
                      bg="#630A10", fg="#FACE7F", relief="raised", borderwidth=3, command=register)

amount = Scale(foods_frame, from_=1, to=100, orient=HORIZONTAL, state=DISABLED, variable=amount_var, font=(
    "System", 10, "bold"), bg="#630A10", fg="#FACE7F", relief="flat", borderwidth=3)
welcome_label = Label(top1, text="Welcome To Our Catering!", bg="#630A10",
                      fg="#FCF0C8", font=("modern", 15, "bold"), relief="raised", borderwidth=5)
welcome_label.grid(row=0, column=1, columnspan=2)
name_label.grid(row=1, column=1, pady=10)
name_inp.config(font=("System", 10, "bold"),
                bg="#630A10", fg="#FACE7F")
name_inp.grid(row=1, column=2)

phonenumber_label.grid(row=2, column=1)
phonenumber_inp.grid(row=2, column=2)
phonenumber_inp.config(font=("System", 10, "bold"),
                       bg="#630A10", fg="#FACE7F")
options.grid(row=3, column=1)
amount.grid(row=3, column=2)
order_btn.grid(row=1, column=3)
cancel_order_btn.grid(row=4, column=2)
foods_frame.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
options.grid(row=1, column=1)
amount.grid(row=1, column=2)
register_btn.grid(row=4, column=1)

top1.mainloop()

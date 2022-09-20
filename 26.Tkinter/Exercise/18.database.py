from tkinter import *
from PIL import ImageTk,Image
import sqlite3
root = Tk()
root.title("Cydemy.com - Learn to Code!")
root.iconbitmap("2.jpg")
root.geometry("400x400")
def update():

    conn = sqlite3.connect ( "address_book.db" )
    # Create cursor()
    c = conn.cursor ()
    record_id=delete_box.get()
    c.execute("""
    UPDATE addresses SET 
    first_name=:first,
    last_name=:last,
    address=:address,
    city=:city,
    state=:state,
    zipcode=:zipcode
    WHERE oid=:oid""",
    {
        'first':first_name_editor.get(),
        'last': last_name_editor.get() ,
        'address':address_editor.get(),
        'city':city_editor.get(),
        'state':state_editor.get(),
        'zipcode':zipcode_editor.get(),

        'oid':record_id
    })
    conn.commit()
    # close connection
    conn.close()
    editor.destroy()
def edit():
    global editor
    editor= Tk ()
    editor.title ( "Update Record" )
    editor.iconbitmap ( "2.jpg" )
    editor.geometry ( "400x280" )

    conn = sqlite3.connect ( "address_book.db" )
    # Create cursor()
    c = conn.cursor ()
    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid="+str(record_id))
    records = c.fetchall()
    # loop through results
    global first_name_editor , last_name_editor ,address_editor,city_editor,state_editor,zipcode_editor
    first_name_editor = Entry ( editor , width=30 )
    first_name_editor.grid ( row=0 , column=1 , pady=(10 , 0) )
    last_name_editor = Entry ( editor , width=30 )
    last_name_editor.grid ( row=1 , column=1 )
    address_editor = Entry ( editor , width=30 )
    address_editor.grid ( row=2 , column=1 )
    city_editor = Entry ( editor , width=30 )
    city_editor.grid ( row=3 , column=1 )
    state_editor = Entry ( editor , width=30 )
    state_editor.grid ( row=4 , column=1 )
    zipcode_editor = Entry ( editor , width=30 )
    zipcode_editor.grid ( row=5 , column=1 )

    first_name_editor_label = Label ( editor , text="first name : " )
    first_name_editor_label.grid ( row=0 , column=0 , pady=(10 , 0) )
    last_name_editor_label = Label ( editor , text="last name : " )
    last_name_editor_label.grid ( row=1 , column=0 )
    address_editor_label = Label ( editor, text="address : " )
    address_editor_label.grid ( row=2 , column=0 )
    city_editor_label = Label ( editor , text="city : " )
    city_editor_label.grid ( row=3 , column=0 )
    state_editor_label = Label ( editor, text="state : " )
    state_editor_label.grid ( row=4 , column=0 )
    zipcode_editor_label = Label ( editor, text="zipcode : " )
    zipcode_editor_label.grid ( row=5 , column=0 )

    for record in records:
        first_name_editor.insert(0,record[0])
        last_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])
    # create Submit Button
    save_editor_btn = Button ( editor , text="Save" , command=update )
    save_editor_btn.grid ( row=6 , column=0 , columnspan=2 , pady=10 , padx=10 , ipadx=100 )
    conn.commit()
    # close connection
    conn.close()
def delete():
    global delete_box
    conn = sqlite3.connect ( "address_book.db" )
    # Create cursor()
    c = conn.cursor ()
    # Delete a record
    c.execute("DELETE FROM addresses WHERE oid="+str(delete_box.get()))
    # commit changes
    conn.commit()
    # close connection
    conn.close()

def query():
    # create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor()
    c = conn.cursor()
    c.execute("SELECT oid,* FROM addresses")
    records = c.fetchall()
    record_str=""
    for record in records:
        line=""
        for el in record:
            line += str(el)+"  "
        record_str +=line+"\n"

    query_label=Label(root,text=record_str)
    query_label.grid(row=11,column=0,columnspan=2)

    # commit changes
    conn.commit()
    # close connection
    conn.close()

def submit():
    global first_name,last_name,address,state,city,zipcode

    # create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor()
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:addr,:city,:stat,:zip)",
              {
                  "f_name":first_name.get(),
                  "l_name":last_name.get(),
                  "addr":address.get(),
                  "city":city.get(),
                  "stat":state.get(),
                  'zip':zipcode.get()
              })
    # commit changes
    conn.commit()

    # close connection
    conn.close()

    # clear text boxes
    first_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0,END)
    state.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)

# create Submit Function For database

# Data bases

# create a database or connect to one
conn=sqlite3.connect("address_book.db")

# Create cursor()
c = conn.cursor()
'''
# create table

c.execute("""CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )""")
'''
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1,pady=(10,0))
last_name = Entry(root, width=30)
last_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5,column=1)

delete_box=Entry(root,width=20)
delete_box.grid(row=8,column=1)

first_name_label = Label(root,text="first name : ")
first_name_label.grid(row=0, column=0,pady=(10,0))
last_name_label = Label(root,text="last name : ")
last_name_label.grid(row=1, column=0)
address_label = Label(root,text="address : ")
address_label.grid(row=2, column=0)
city_label = Label(root,text="city : ")
city_label.grid(row=3, column=0)
state_label = Label(root,text="state : ")
state_label.grid(row=4, column=0)
zipcode_label = Label(root,text="zipcode : ")
zipcode_label.grid(row=5, column=0)

delete_box_label=Label(root,text="Select ID : ")
delete_box_label.grid(row=8,column=0)
# create Submit Button
submit_btn=Button(root,text="Add Records To Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
# Create Show Button
query_btn = Button(root,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)
# Create a delete button
delete_btn = Button(root,text="Delete Record",command=delete)
delete_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=136)
# Edit button
edit_btn = Button(root,text="Edit Record",command=edit)
edit_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=143)
# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()
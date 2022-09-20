import sqlite3

def show_all():
    """Query the DB and Return All records"""
    conn = sqlite3.connect('customer.db')
    c= conn.cursor()
    c.execute("SELECT rowid,* FROM customers")
    items=c.fetchall()
    for item in items:
        print(item)
    print()
    conn.close()
    

def add_one(first: str, last: str, email: str):
    """Add new Record to the Table"""
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)",(first,last,email))
    conn.commit()
    conn.close()

def delete_one(id:str):
    """Delete a record from the Table"""
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid=(?)",id)
    conn.commit()
    conn.close()


def add_many(lst:list):
    """Add Many Record to the Table"""
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (lst))
    conn.commit()
    conn.close()

def email_lookup(email:str):
    """Lookup Email from the table"""
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid,* FROM customers WHERE email= (?)",(email,))
    items = c.fetchall()
    for item in items:
        print(item)
    print()

    conn.close()

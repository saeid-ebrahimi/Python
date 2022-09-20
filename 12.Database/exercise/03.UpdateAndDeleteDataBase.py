import sqlite3

conn = sqlite3.connect("customer.db")

cu = conn.cursor()

# update records
cu.execute(
    """
    UPDATE customers SET first_name = 'Bob'
    WHERE last_name = 'Elder'
    """
)
conn.commit()
cu.execute(
    """
    UPDATE customers SET first_name = 'John'
    WHERE rowid = 1
    """
)
conn.commit()

cu.execute("DELETE FROM customers WHERE rowid=6")
conn.commit()
items = cu.execute("SELECT rowid,* FROM customers").fetchall()
print(items)

#cu.execute("SELECT rowid,* FROM customers ORDER BY rowid DESC")
cu.execute("SELECT rowid,* FROM customers ORDER BY first_name")
#cu.execute("SELECT rowid,* FROM customers ORDER BY last_name DESC")
items = cu.fetchall()

for item in items :
    print(item)
 
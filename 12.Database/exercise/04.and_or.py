import sqlite3

conn = sqlite3.connect("customer.db")

cu = conn.cursor()

cu.execute("SELECT rowid,* FROM customers ORDER BY first_name")
items = cu.fetchall()

for item in items:
    print(item)
print()
cu.execute(
    "SELECT rowid,* FROM customers WHERE last_name LIKE 'Br%' AND first_name='Wes'")
items = cu.fetchall()

for item in items:
    print(item)
print()
cu.execute("SELECT rowid,* FROM customers WHERE last_name LIKE 'Br%' OR first_name='Steph' OR rowid=1")
items = cu.fetchall()

for item in items :
    print(item)
print()
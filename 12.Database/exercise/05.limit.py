import sqlite3

conn = sqlite3.connect("customer.db")

cu = conn.cursor()

cu.execute("SELECT rowid,* FROM customers ORDER BY first_name LIMIT 3")
items = cu.fetchall()

for item in items:
    print(item)
print()

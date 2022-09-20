import sqlite3

conn = sqlite3.connect("customer2.db")

cu = conn.cursor()
cu.execute("DROP TABLE customers")
conn.commit()
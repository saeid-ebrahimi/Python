import sqlite3
conn = sqlite3.connect("customer.db")
c =conn.cursor()
#create table
create_command = """CREATE TABLE customers(
    first_name text,
    last_name text,
    email text)"""
#Data types:
#NULL
#INTEGER
#REAL
#TEXT 
#BLOB
many_customers = [
    ('Wes','Brown','wes@academy.com'),
    ('Steph','Kuewa','step@kuewa.com'),
    ('Dan','Pas','dan@pas.com')]
#c.execute(create_command)
insert_command = "INSERT INTO customers VALUES ('Mary','Brown','mary@academy.com')"
#c.execute(insert_command)
insert_many_command = "INSERT INTO customers VALUES (?,?,?)"
#c.executemany(insert_many_command, many_customers)

#fetch elements
select_command1 = "SELECT * FROM customers"
#fetch unique primary keys
select_command2 = "SELECT rowid,* FROM customers"
c.execute(select_command2)
#print(c.fetchone())
#print(c.fetchmany(2))
#print(c.fetchall()[1,1])
#print("command executed succesfuly!")

items = c.fetchall()
print("id \t Name \t\t Email")
print("---\t ------\t\t --------")
for item in items:
    print(item[0],"\t",item[1],item[2],"\t",item[3])
#commit our command
conn.commit()

conn.close()
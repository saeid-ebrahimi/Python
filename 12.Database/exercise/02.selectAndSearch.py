import sqlite3
conn = sqlite3.connect("customer.db")
c =conn.cursor()

#fetch elements
select_command1 = "SELECT * FROM customers"
#fetch unique primary keys
select_command2 = "SELECT rowid,* FROM customers"
c.execute(select_command2)
#print(c.fetchone())
#print(c.fetchmany(2))
#print(c.fetchall()[1,1])
#print("command executed succesfuly!")
search_command = "SELECT * FROM customers WHERE last_name='Elder'"
search_command2 = "SELECT * FROM customers WHERE age <= 20"
# search for names with Br in first
search_command3 = "SELECT * FROM customers WHERE last_name LIKE 'Br%'"
search_command4 = "SELECT * FROM customers WHERE email LIKE '%academy.com'"
items = c.fetchall()
print("id \t Name \t\t Email")
print("---\t ------\t\t --------")
for item in items:
    print(item[0],"\t",item[1],item[2],"\t",item[3])


conn.close()
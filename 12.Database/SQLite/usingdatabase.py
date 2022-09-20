import sqlite3

path = "./school2.db"

connection = sqlite3.connect(path)

cursor = connection.cursor()

sql_command = ('''CREATE TABLE IF NOT EXISTS companies(
id INTEGER PRIMARY KEY AUTOINCREMENT ,
name TEXT NOT NULL 
)  
''')
cursor.execute(sql_command)
sql_command = (
    '''
        CREATE TABLE IF NOT EXISTS courses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            company_id INTEGER
        )
    '''
)
cursor.execute(sql_command)
sql_command = "INSERT INTO companies VALUES (?,?)"
#cursor.execute(sql_command,(2,"cydemy interactive",))
sql_command = "INSERT INTO courses VALUES (?,?,?,?)"
#cursor.execute(sql_command,(1,"hello coding","coding",1))
#cursor.execute(sql_command,(2,"python coding","programming",2))
connection.commit()
sql_command = "select * from companies"
print(cursor.execute(sql_command).fetchmany(1))
sql_command = "select category,name from courses where category='coding'"
print(cursor.execute(sql_command).fetchmany(2))
sql_command = ("""drop table companies 
                """)
cursor.execute(sql_command)
connection.commit()
sql_command = "select * from companies"
print(cursor.execute(sql_command).fetchmany(2))

import sqlite3
import os 
def connect(path="school.db", syncdb=False):
    if os.path.exists(path):   
        connection = sqlite3.connect(path)
    else:
        syncdb=True
    return connection

def insert_row_into_courses(name , category ,company_id, connection):
    sql_command= "INSERT INTO courses (name, category, company_id) VALUES (?,?,?)"
    cursor = connection.cursor()
    check_exits = cursor.execute("SELECT id FROM courses WHERE name=?",(name,)).fetchone()
    if check_exits is None:    
        cursor.execute(sql_command,(name,category,company_id))
        connection.commit()
    else:
        print("course already {} exists!!".format(*check_exits))

name = input("Enter course name: ")
category = input("Enter course category: ")
company = input("Enter course company id: ")
connection = connect()
insert_row_into_courses(name, category,company, connection)
courses_count = connection.execute("SELECT count(id) FROM courses").fetchone()
print("number of courses:",courses_count)

connection.close()

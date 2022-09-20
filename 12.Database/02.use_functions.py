import sqlite3
import os


def connect(path="school2.db", syncdb=False):
    if os.path.exists(path):
        connection = sqlite3.connect(path)
    else:
        syncdb = True
    return connection


_name = input("enter course name: ")
_category = input("enter course category: ")
_company_id = input("enter course company_id: ")

def insert_row_into_courses(name, category, company_id, connection):
    sql = "INSERT INTO courses (name, category, company_id) VALUES (?, ?, ?)"
    cursor = connection.cursor()
    check_exists = cursor.execute("SELECT id FROM courses WHERE name=?", (name,)).fetchone()
    if check_exists is None:
        cursor.execute(sql, (name, category, company_id))
        connection.commit()
    else:
        print("course already exists in ", check_exists)


_connection = connect()

insert_row_into_courses(_name, _category, _company_id, _connection)

courses_count = _connection.execute("SELECT count(id) FROM courses").fetchone()
print(courses_count)

_connection.close()

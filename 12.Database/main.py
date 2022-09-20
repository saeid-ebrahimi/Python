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

connection = connect()

insert_row_into_courses(_name, _category, _company_id, connect())

courses_count = connection.execute("SELECT count(id) FROM courses").fetchone()
print(courses_count)

connection.close()

sql = '''
SELECT companies.name, courses.name
FROM companies
LEFT JOIN courses
ON companies.id = courses.company_id
'''

_cursor = connection.cursor()
_cursor.execute(sql)
print(_cursor.fetchall())

sql = '''
    SELECT companies.name, courses.name
    FROM companies 
    INNER JOIN courses
    ON companies.name = 'Mammoth Interactive'
     '''
_cursor.execute(sql)
print(_cursor.fetchall())

sql = '''
    SELECT *
    FROM companies
    LEFT JOIN courses 
    ON companies.id = courses.company_id
    '''

_cursor.execute(sql)
print(_cursor.fetchall())

sql = '''
    SELECT *
    FROM companies 
    INNER JOIN courses
    ON companies.id = courses.company_id
    '''

_cursor.execute(sql)
print(_cursor.fetchall())

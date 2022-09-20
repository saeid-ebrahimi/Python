import sqlite3
import os


def create_data_base(path):
    if not os.path.exists(path):
        connection = sqlite3.connect(path)
        return connection
    else:
        print("data base exist")


def connect(path="school1.db", syncdb=False):
    if os.path.exists(path):
        connection = sqlite3.connect(path)
        return connection
    else:
        syncdb = True
        print("data base does not exist")


def insert_row_into_courses(name, category, company_id, connection):
    sql_command = "INSERT INTO courses (name, category, company_id) VALUES (?,?,?)"
    cursor = connection.cursor()
    check_exits = cursor.execute(
        "SELECT id FROM courses WHERE name=?", (name,)).fetchone()
    if check_exits is None:
        cursor.execute(sql_command, (name, category, company_id))
        connection.commit()
    else:
        print("course with id {} and name {} already exists!!".format(
            *check_exits, name))


def insert_row_into_companies(name, connection):
    sql_command = "INSERT INTO companies (name) VALUES (?)"
    cursor = connection.cursor()
    check_exits = cursor.execute(
        "SELECT id FROM companies WHERE name=?", (name,)).fetchone()
    if check_exits is None:
        cursor.execute(sql_command, (name,))
        connection.commit()
    else:
        print("company with id {} and name {} already exists!!".format(
            *check_exits, name))


def delete_row_from_companies(name, connection):
    sql_command = f"""DELETE FROM companies
        WHERE name = {name}"""
    cursor = connection.cursor()
    check_exits = cursor.execute(
        "SELECT id FROM companies WHERE name=?", (name,)).fetchone()
    if check_exits is not None:
        cursor.execute(sql_command, (name,))
    else:
        print("company with name {name} doesn't exist!!")


def delete_row_from_courses(name, connection):
    sql_command = f"""DELETE FROM courses
        WHERE name = {name}"""
    cursor = connection.cursor()
    check_exits = cursor.execute(
        "SELECT id FROM courses WHERE name=?", (name,)).fetchone()
    if check_exits is not None:
        cursor.execute(sql_command, (name,))
    else:
        print("course with name {name} doesn't exist!!")

def make_one_col_table(connection, table_name: str, name: str):
    cursor = connection.cursor()
    sql = (
        """
        CREATE TABLE IF NOT EXISTS {}(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            {} TEXT NOT NULL
    )
    """.format(table_name, name)
    )
    cursor.execute(sql)


def make_tree_col_table(connection, table_name: str, name: str, sec_col: str, third_col: str):
    cursor = connection.cursor()
    sql = (
        f"""
            CREATE TABLE IF NOT EXISTS {table_name}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                {name} TEXT NOT NULL,
                {sec_col} TEXT NOT NULL,
                {third_col} INTEGER
            )
        """
    )
    cursor.execute(sql)


school_db = create_data_base("school1.db")
if school_db is not None:
    make_one_col_table(school_db, "companies","name")
    make_tree_col_table(school_db, "courses", "name","category" ,"company_id" )

connection = connect()
ans = input("enter a row to courses?")

if ans == "yes":
    name = input("Enter course name: ")
    category = input("Enter course category: ")
    company = input("Enter course company id: ")
    insert_row_into_courses(name, category,company, connection)

ans = input("enter row to companies?")
if ans == "yes":
    name = input("enter the company name:")
    insert_row_into_companies(name, connection)

ans = input("delete from courses?")
if ans == "yes":
    name = input("enter the company name:")
    delete_row_from_courses(name, connection)
ans = input("delete from companies?")
if ans == "yes":
    name = input("enter the company name:")
    delete_row_from_companies(name, connection)

courses_count = connection.execute("SELECT count(id) FROM courses").fetchone()
print("number of courses:",courses_count)
courses_name = connection.execute("SELECT name FROM courses").fetchall()
print("courses name: ",courses_name)
company_names = connection.execute("SELECT name FROM companies").fetchall()
print("company names: ", company_names)

cursor = connection.cursor()

connection.close()

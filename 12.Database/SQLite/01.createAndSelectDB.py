import sqlite3
DATABASE_PATH="school.db"
connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()
sql = (
    """
        CREATE TABLE IF NOT EXISTS companies(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL
    )
    """
)

cursor.execute(sql)

sql = (
    """
        CREATE TABLE IF NOT EXISTS courses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            company_id INTEGER
        )
    """
)
cursor.execute(sql)

sql = "INSERT INTO companies (name) VALUES (?)"
cursor.execute(sql, ("Mammoth Interactives",))
connection.commit()

cursor.execute(sql,("Bura Tech",))
connection.commit()

sql = "INSERT INTO courses (name, category,company_id) VALUES (?,?,?)"
cursor.execute(sql,("Hello Coding","programming",1))
connection.commit()

companies = connection.execute("SELECT count(id) FROM companies").fetchone()
print(*companies)

courses = connection.execute("SELECT count(id) FROM courses").fetchone()
print(*courses)

cursor.execute("SELECT id FROM courses WHERE name=?",("Hello Coding",))
print(cursor.fetchone())

cursor.execute("SELECT id FROM courses WHERE name=?",("Machine Learning",))
print(cursor.fetchone())

cursor.execute("SELECT id FROM companies WHERE name=?",("Mammoth Interactive",))
print(cursor.fetchone())

sql = "INSERT INTO courses (name,category,company_id) VALUES (?,?,?)"
cursor.execute(sql,("Complete Machine Learning","programming",1))
connection.commit()

cursor.execute("SELECT id FROM courses WHERE category=?",("programming",))
print(cursor.fetchall())

cursor.execute("SELECT name FROM courses WHERE category=?",("programming",))
print(cursor.fetchall())


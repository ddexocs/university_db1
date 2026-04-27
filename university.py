import sqlite3
db = sqlite3.connect("university.db")
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT ,
               name TEXT,
               age INTEGER,
               major TEXT)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS curses(
               id INTEGER PRIMARY KEY AUTOINCREMENT ,
               curse_name TEXT,
                teacher_name TEXT)""")
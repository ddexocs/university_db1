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
cursor.execute("""CREATE TABLE IF NOT EXISTS student_curses (
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
               student_id INTEGER,
               curse_id INTEGER,
               FOREIGN KEY (student_id) REFERENCES students (id),
               FOREIGN KEY (curse_id) REFERENCES curses(id)) """)
while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print ("7. Вийти")
    choice = input("Оберіть опцію (1-7): ")
    if choice == "1":
        # Додавання нового студента
        name = input("Write student name:")
        age = int(input("write students age:"))
        major = input("Write students major:")
        cursor.execute("INSERT INTO students (name,age,major) VALUES (?,?,?)",(name,age,major)) #?,?,? placeholder
        db.commit()
    elif choice == "2":
        # Додавання нового курсу
        name = input("Write the curse name:")
        teacher_name = input("Write the name of the teacher:")
        cursor.execute("INSERT INTO curses (curse_name,teacher_name) VALUES (?,?)",(name,teacher_name))
        db.commit()
    elif choice == "3":
        # Показати список студентів
        cursor.execute("SELECT * FROM students")# * = значення з всех стовпцов
        students = cursor.fetchall()#fetchall перетворяет весь результат в список картежей
        print(students)
    elif choice == "4":
        # Показати список курсів
        cursor.execute("SELECT * FROM curses")
        curses = cursor.fetchall()
        print(curses)
    elif choice == "5":
        # Зареєструвати студента на курс
        curse_id = int(input("Write curse id:"))
        student_id = int(input("Write student id:"))
        cursor.execute("INSERT INTO student_curses (curse_id,student_id) VALUES (?,?)", (curse_id,student_id))
        db.commit()
    elif choice == "6":
        # Показати студентів на конкретному курсі
        pass# зэднати 2 таблички student_curses,students
    elif choice == "7":
        break
    else:
        print ("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")
import sqlite3

# Создание и подключение к базе данных
conn = sqlite3.connect('teacher.db')
cursor = conn.cursor()

# Создание таблицы Students
cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                    Student_Id INTEGER PRIMARY KEY,
                    Student_Name TEXT,
                    School_Id INTEGER)''')

# Создание таблицы Schools
cursor.execute('''CREATE TABLE IF NOT EXISTS Schools (
                    School_Id INTEGER PRIMARY KEY,
                    School_Name TEXT)''')

# Вставка данных в таблицу Students
students_data = [
    (201, 'Иван', 1),
    (202, 'Петр', 2),
    (203, 'Анастасия', 3),
    (204, 'Игорь', 4)
]

cursor.executemany('INSERT INTO Students VALUES (?, ?, ?)', students_data)

# Вставка данных в таблицу Schools
schools_data = [
    (1, 'Школа 1'),
    (2, 'Школа 2'),
    (3, 'Школа 3'),
    (4, 'Школа 4')
]

cursor.executemany('INSERT INTO Schools VALUES (?, ?)', schools_data)

# Сохранение изменений
conn.commit()

# Функция для получения информации о студенте и школе по ID студента
def get_student_info(student_id):
    cursor.execute('''SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, Schools.School_Name
                    FROM Students
                    JOIN Schools ON Students.School_Id = Schools.School_Id
                    WHERE Students.Student_Id = ?''', (student_id,))
    row = cursor.fetchone()

    if row:
        student_id, student_name, school_id, school_name = row
        print("ID студента:", student_id)
        print("Имя студента:", student_name)
        print("ID школы:", school_id)
        print("Название школы:", school_name)
    else:
        print("Студент с указанным ID не найден.")

# Пример использования
student_id = 201
get_student_info(student_id)

# Закрытие соединения с базой данных
conn.close()
import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor()


base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.csv')
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
missing_data = []

try:
    with open(eugene_file_path, newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Пропустили заголовок
        for row in csv_reader:
            name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row
            name = 'Elbey'
            second_name = 'Gamidov'
            group_title = 'Spider-man'
            query = '''
            SELECT students.name, students.second_name, gs.title AS group_title,
            b.title AS book_title, m.value AS mark_value,
            l.title AS lesson_title, s.title AS subjet_title
            FROM students
            JOIN `groups` AS gs ON students.group_id = gs.id
            LEFT JOIN books AS b ON students.id = b.taken_by_student_id
            LEFT JOIN marks AS m ON students.id = m.student_id
            LEFT JOIN lessons AS l ON m.lesson_id = l.id
            LEFT JOIN subjets AS s ON l.subject_id = s.id
            WHERE students.name = %s
            AND students.second_name = %s
            AND gs.title = %s;
            '''
            cursor.execute(query, (name, second_name, group_title))
            result = cursor.fetchall()
            if not result:
                missing_data.append('Some missing')

    db.commit()

except mysql.Error as e:
    print(f"Ошибка при выполнении запроса: {e}")
    db.rollback()

if missing_data:
    for data in missing_data:
        print(data)
else:
    print('Данные собраны')

cursor.close()
db.close()

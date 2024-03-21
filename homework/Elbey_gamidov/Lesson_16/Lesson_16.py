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


with open(eugene_file_path, newline='') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Пропустили заголовок
    for row in csv_reader:
        name, last_name, city = row
        query = f"SELECT * FROM students WHERE name = '{name}' AND last_name = '{last_name}' AND city = '{city}'"
        cursor.execute(query)
        result = cursor.fetchall()
        if not result:
            missing_data.append(row)

if missing_data:
    print('Missing')
    for data in missing_data:
        print(data)
else:
    print('Данные собраны, ничего не упущено')

cursor.close()
db.close()

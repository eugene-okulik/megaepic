from datetime import datetime, timedelta
import os


base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.txt')
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(eugene_file_path) as eugene_file:
    for line in eugene_file:
        parts = line.split(' - ')
        date_str = parts[0].split()[1].strip()
        date_format = '%Y-%m-%d'

        date_time = datetime.strptime(date_str, date_format)

        new_date = date_time + timedelta(weeks=1)
        print(f"Эта дата, но на неделю позже, равна : {new_date.strftime(date_format)}")

        day_of_week = date_time.strftime('%A')
        print(f"День недели сейчас: {day_of_week}")

        today = date_time.now().date()
        day_dif = (today - date_time.date()).days
        print(f"Прошло: {day_dif} дней")

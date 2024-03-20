import mysql.connector as mysql

db = mysql.connect(
    user='',
    passwd='',
    host='',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

insert_query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
student_data = ('Elbey', 'Gamidov')
cursor.execute(insert_query, student_data)
student_id = cursor.lastrowid

select_query = "SELECT * FROM students WHERE id = %s"
cursor.execute(select_query, (student_id,))
print(cursor.fetchone())


insert_query_group = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
group_data = ('Spider-man', '15.02.2024', '15.06.2024')
cursor.execute(insert_query_group, group_data)
group_id = cursor.lastrowid

select_query_group = "SELECT * FROM `groups` WHERE id = %s"
cursor.execute(select_query_group, (group_id,))
print(cursor.fetchone())


update_query = "Update students set group_id = %s where id = %s"
update_data = (group_id, student_id)
cursor.execute(update_query, update_data)
print("Данные обновлены")

insert_query_book = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
book1_data = ('Part1', student_id)
book2_data = ('Part2', student_id)
book3_data = ('Part3', student_id)

cursor.execute(insert_query_book, book1_data)
cursor.execute(insert_query_book, book2_data)
cursor.execute(insert_query_book, book3_data)
print(cursor.fetchall())

insert_query_subjet = "INSERT INTO subjets (title) VALUES (%s)"
subjet1_data = ('matem',)
subjet2_data = ('eng',)

cursor.execute(insert_query_subjet, subjet1_data)
subjet_id_1 = cursor.lastrowid

cursor.execute(insert_query_subjet, subjet2_data)
subjet_id_2 = (cursor.lastrowid)

select_query_subjet_1 = "SELECT * FROM subjets WHERE id = %s"
cursor.execute(select_query_subjet_1, (subjet_id_1,))
result_1 = cursor.fetchone()
print(result_1)

cursor.execute(select_query_subjet_1, (subjet_id_2,))
result_2 = cursor.fetchone()
print(result_2)


insert_query_lesson = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson1_data = ('python lessons', subjet_id_1)
lesson2_data = ('sql lessons', subjet_id_2)

cursor.execute(insert_query_lesson, lesson1_data)
cursor.execute(insert_query_lesson, lesson2_data)
lesson1_id = cursor.lastrowid
lesson2_id = cursor.lastrowid
print(cursor.fetchone())

insert_query_mark = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
mark1_data = ('5', lesson1_id, student_id)
mark2_data = ('5', lesson2_id, student_id)

cursor.execute(insert_query_mark, mark1_data)
cursor.execute(insert_query_mark, mark2_data)
print(cursor.fetchone())


new_query = f'''
SELECT students.name, students.second_name, gs.title AS group_title,
b.title AS book_title, m.value AS mark_value,
l.title AS lesson_title, s.title AS subjet_title
FROM students
JOIN `groups` AS gs ON students.group_id = gs.id
LEFT JOIN books AS b ON students.id = b.taken_by_student_id
LEFT JOIN marks AS m ON students.id = m.student_id
LEFT JOIN lessons AS l ON m.lesson_id = l.id
LEFT JOIN subjets AS s ON l.subject_id = s.id
WHERE students.id = {student_id};
'''
cursor.execute(new_query)
print(cursor.fetchall())

db.commit()

db.close()

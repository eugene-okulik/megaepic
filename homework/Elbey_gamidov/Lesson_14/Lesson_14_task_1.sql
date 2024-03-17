INSERT INTO students (name, second_name) values ('Elbey', 'Gamidov')

INSERT INTO `groups` (title, start_date, end_date) values ('Spider-man', '15.02.2024', '15.06.2024')

UPDATE students SET group_id = 457 WHERE students.id = 504

INSERT INTO books (title, taken_by_student_id) values ('Part1', 504)

INSERT INTO books (title, taken_by_student_id) values ('Part2', 504)

INSERT INTO subjets (title) values ('matem')

INSERT INTO subjets (title) values ('eng')

INSERT INTO lessons (title, subject_id) values ('python lessons', 615)

INSERT INTO lessons (title, subject_id) values ('sql lessons', 616)

INSERT INTO marks (value, lesson_id, student_id) values ('5', 743, 504)

INSERT INTO marks (value, lesson_id, student_id) values ('5', 744, 504)

SELECT * from marks WHERE student_id = 504

SELECT * from books WHERE taken_by_student_id = 504

SELECT students.name, students.second_name, gs.title AS group_title,
b.title AS book_title, m.value AS mark_value, 
l.title AS lesson_title, s.title AS subjet_title
FROM students
JOIN `groups` AS gs ON students.group_id = gs.id
LEFT JOIN books AS b ON students.id = b.taken_by_student_id
LEFT JOIN marks AS m ON students.id = m.student_id
LEFT JOIN lessons AS l ON m.lesson_id = l.id
LEFT JOIN subjets AS s ON l.subject_id = s.id
WHERE students.id = 504;

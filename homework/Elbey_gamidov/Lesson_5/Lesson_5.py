person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person


text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'
id = text_1.find(': ')  # нашел индекс этого двоеточия
#  print(id)
print(int(text_1[20:]) + 10)  # прибавил к верхнему индексу два значения, и сказал, что выведи все до конца + 10
id_2 = text_2.find(': ')
#  print(id_2)
print(int(text_2[20:]) + 10)  # Тут все тоже самое
id_3 = text_3.find(': ')
#  print(id_3)
print(int(text_3[28:]) + 10)


students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students = ', '.join(students)
subjects = ', '.join(subjects)
reword = f'Students {students} study these subjects: {subjects}'
print(reword)

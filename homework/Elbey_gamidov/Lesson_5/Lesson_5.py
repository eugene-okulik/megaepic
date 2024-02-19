person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name , last_name, city, phone, country = person


text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'
print(text_1.index('42'))
print(text_2.index('514'))
print(text_3.index('9'))
print(int(text_1[20:22]) + 10)
print(int(text_2[20:23]) + 10)
print(int(text_3[-1:]) + 10)


students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students = ', '.join(students)
subjects = ', '.join(subjects)
reword = f'Students {students} study these subjects: {subjects}'
print(reword)

text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'

def text_find(text):  # Функция для первых двух переменных
    text.find(': ')
    print(int(text[20:]) + 10)


def find_and_replace_3(text):  # Функция для третьей переменной
    text_3.find(': ')
    print(int(text_3[28:]) + 10)


text_find(text_1)
text_find(text_2)
find_and_replace_3(text_3)

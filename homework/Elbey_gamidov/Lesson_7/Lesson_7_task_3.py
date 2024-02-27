text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'


def find_and_replace(text):
    pos = text.find(': ')
    if True:
        value = int(text[pos + 2:]) + 10
        print(value)


find_and_replace(text_1)
find_and_replace(text_2)
find_and_replace(text_3)

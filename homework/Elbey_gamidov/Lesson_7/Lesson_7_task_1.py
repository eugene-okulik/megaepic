while True:
    num = 7
    user_num = int(input('Угадай цифру: '))
    if num != user_num:
        print('Попробуйте снова')
        continue
    else:
        print('Поздравляю! Вы угадали!')
        break
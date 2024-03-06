def dekorator(func):
    def wrapper(num1, num2):
        if num1 == num2:
            return func(num1, num2, '+')
        elif num1 > num2:
            return func(num1, num2, '-')
        elif num2 > num1:
            return func(num1, num2, '/')
        elif num1 < 0 or num2 < 0:
            return func(num1, num2, '*')
    return wrapper


@dekorator
def calc(num1, num2, operation):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    return result


num1 = int(input('Введи первое число: '))
num2 = int(input('Введи второе число: '))


result = calc(num1, num2)
print('Результат:', result)

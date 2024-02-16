from math import sqrt


a = int(input('Введи первое число: '))
b = int(input('Введи второе число: '))
print(a + b)
print(a - b)
print(a * b)


x = int(input('Введи первое число: '))
y = int(input('Введи второе число: '))
print(((x - y)/1) + (x * y))


a = int(input('Введи первое число: '))
b = int(input('Введи второе число: '))
print((a + b) / 2)
print(sqrt(a * b))


a = int(input('Введи первый катет: '))
b = int(input('Введи второй катет: '))
gypo = sqrt(((a * a) + (b * b)))
s = 0.5 * (a * b)
print(gypo)
print(s)

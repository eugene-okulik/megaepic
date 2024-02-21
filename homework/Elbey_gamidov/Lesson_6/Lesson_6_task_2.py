diapazon = range(1, 101)
for i in diapazon:
    if i % 3 == 0:
        print('Fuzz')
    if i % 5 == 0:
        print('Buzz')
    elif i % 3 and i % 5 == 0:
        print('FuzzBuzz', end = '')
    else:
        print(i)

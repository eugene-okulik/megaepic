diapazon = range(1, 101)
for i in diapazon:
    if i % 3 == 0 and i % 5 == 0:
        print('FuzzBuzz')
    elif i % 3 == 0:
        print('Fuzz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

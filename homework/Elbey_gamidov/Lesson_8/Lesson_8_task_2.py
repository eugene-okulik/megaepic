def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci = fibonacci_generator()
def for_generator(n):
    for n in range(n):
        fibonacci_number = next(fibonacci)
    print(fibonacci_number)


for_generator(5)
for_generator(100)
for_generator(10000)
for_generator(100000)

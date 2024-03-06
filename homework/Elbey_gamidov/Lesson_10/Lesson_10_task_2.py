def deko(func):


    def wrapper(*args):
        print(f'function {func.__name__} started now')
        func()
        print(f'function {func.__name__} finished')
    return wrapper


def repeat(count):
    def dekorator(func):
        def wrapper(*args):
            for _ in range(count):
                func(*args)
        return wrapper
    return dekorator


@deko
@repeat(3)
def do_some_first():
    print('Спасибо вам, Евгений, за балдежный курс')


do_some_first()

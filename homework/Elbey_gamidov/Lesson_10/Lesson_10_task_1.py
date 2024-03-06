def deko(func):


    def wrapper(*args):
        print(f'function {func.__name__} started now')
        func()
        print(f'function {func.__name__} finished')
    return wrapper


@deko
def do_some_first():
    print('Спасибо вам, Евгений, за балдежный курс')


@deko
def do_some_second():
    print('Хорошего дня')


do_some_first()
do_some_second()
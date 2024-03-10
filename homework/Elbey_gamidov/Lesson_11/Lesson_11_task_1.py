class Book:
    material = 'бумага'
    text_bool = 'да'

    def __init__(self, title_name, author, count_page, ISBN, reserved_or_not,):
        self.title_name = title_name
        self.author = author
        self.count_page = count_page
        self.ISBN = ISBN
        self.reserved_or_not = reserved_or_not


first_book = Book('Война и мир', 'Толстой', 3000, 23941841, True)
second_book = Book('Мастер и маргарита', 'Булгаков', 1000, 43921841, False)
third_book = Book('Капитанская дочка', 'Пушкин', 2000, 23831841, False)
fourth_book = Book('Незнакомка', 'Блок', 500, 13940841, False)
fifth_book = Book('Береза', 'Есенин', 800, 73945841, False)
books = [first_book, second_book, third_book, fourth_book, fifth_book]
for book in books:
    if book.reserved_or_not:
        """print(f"Название: {book.title_name}, Автор: {book.author}, Количество страниц: {book.count_page}, ISBN: {book.ISBN}, 
        Зарегистрирован, Материал: {Book.material}, Наличие текста: {Book.text_bool}")"""
    else:
        """print(f"Название: {book.title_name}, Автор: {book.author}, Количество страниц: {book.count_page}, ISBN: {book.ISBN}, 
        Материал: {Book.material}, Наличие текста: {Book.text_bool}")"""


class SchoolBook(Book):

    def __init__(self, title_name, author, count_page, ISBN, reserved_or_not, predmet, room, task):
        super().__init__(title_name, author, count_page, ISBN, reserved_or_not)
        self.predmet = predmet
        self.room = room
        self.task = task


six_book = SchoolBook('Война и мир', 'ШестойАвтор', 9999, 53941841, True, 'Литература', 5, True)
seven_book = SchoolBook('Морозко', 'СедьмойАвтор', 1111, 83941841, False, 'Литература', 5, False)
books = [six_book, seven_book]
for book in books:
    if hasattr(book, 'predmet'):
        if book.reserved_or_not and book.task:
            """print(f"Название: {book.title_name}, Автор: {book.author}, Количество страниц: {book.count_page}, ISBN: {book.ISBN}, 
            Зарегистрирован, Предмет: {book.predmet}, Класс: {book.room}, Задания: есть")"""
        else:
            """print(f"Название: {book.title_name}, Автор: {book.author}, Количество страниц: {book.count_page}, 
            ISBN: {book.ISBN}, Предмет: {book.predmet}, Класс: {book.room}")"""

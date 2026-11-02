"""
Задача 1: Управление книгами в библиотеке

Ситуация: мы управляем библиотекой и хотим добавить автоматизацию в работу с книгами.
Каждая книга может быть либо «доступна», либо «в аренде».
Для управления состоянием книг нам необходимо добавить метод класса,
который будет отслеживать общее количество книг в библиотеке,
и статический метод, который проверяет, находится ли книга в библиотеке.

Задача: создайте программу, которая позволяет:

Добавлять книги в библиотеку.
Менять статус книги (например, с «доступна» на «в аренде»).
Проверять, доступна ли книга.
Узнавать общее количество книг в библиотеке.
Ожидаемый результат:

Пользователь может добавлять книги.
Пользователь видит общий список книг.
Книга отображается как доступная или в аренде в зависимости от её статуса.
"""


class LibraryBook:
    all_books = []
    total_books = 0

    def __init__(self, title, status='доступна'):
        self.title = title
        self.status = status
        LibraryBook.all_books.append(self)
        LibraryBook.total_books += 1

    @classmethod
    def display_all_books(cls):
        if cls.all_books:
            print(cls.get_total_books_info())
            for book in cls.all_books:
                print(book)
        else:
            print('Библиотека пуста!')

    @classmethod
    def get_total_books_info(cls):
        return f'Всего книг в библиотеке: {cls.total_books}'

    @staticmethod
    def is_available(book_obj):
        if isinstance(book_obj, LibraryBook):
            return book_obj.status == 'доступна'
        raise TypeError("Неверный тип данных!")

    def change_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f'Книга: {self.title}. Статус: {self.status}'
